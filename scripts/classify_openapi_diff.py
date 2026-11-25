#!/usr/bin/env python3
"""Classify semantic changes between two OpenAPI specifications for XDK auto-releases.

Outputs a deterministic bump recommendation per SDK:
  - No structural API surface changes (prose/docs/key-order only) -> "none"
  - Backwards-compatible schema/parameter/enum/auth updates       -> "patch"
  - New endpoints/operations                                      -> "minor"
  - Breaking changes (removed endpoints/params/fields, newly
    required params/properties, type/format/nullable/$ref/enum/
    operationId/tag changes):
      * 0.x.y SDKs -> "minor" (SemVer 2.0.0 pre-1.0; never auto-jumps to 1.0.0)
      * >=1.0 SDKs -> "major"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
SDKS = ("python", "typescript", "java", "csharp")

# Keys that carry documentation/presentation metadata without changing SDK code.
DOC_ONLY_KEYS = frozenset(
    {
        "description",
        "summary",
        "example",
        "examples",
        "externalDocs",
        "title",
    }
)

# OpenAPI map-valued containers whose keys are API/schema/field/header/media names,
# NOT OpenAPI specification keywords (e.g. `properties.description`, `properties.title`,
# `headers.x-rate-limit-limit`). Never strip DOC_ONLY_KEYS or `x-*` keys inside these.
MAP_CONTAINER_KEYS = frozenset(
    {
        "properties",
        "patternProperties",
        "dependentSchemas",
        "paths",
        "schemas",
        "parameters",
        "requestBodies",
        "responses",
        "securitySchemes",
        "headers",
        "content",
    }
)

STRUCTURAL_COMPONENT_SECTIONS = (
    "schemas",
    "parameters",
    "requestBodies",
    "responses",
    "securitySchemes",
    "headers",
)

# List keys whose element order is semantically irrelevant in OpenAPI 3.0
# (and often serialized from unordered sets on the server).
SET_LIKE_LIST_KEYS = frozenset(
    {
        "required",
        "enum",
        "parameters",
        "oneOf",
        "anyOf",
        "allOf",
    }
)


def _canonical_sort_key(item: Any) -> str:
    return json.dumps(item, sort_keys=True, separators=(",", ":"))


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path} root must be a JSON object")
    return data


def validate_openapi_spec(spec: dict[str, Any], label: str, min_paths: int = 1) -> None:
    if not isinstance(spec.get("openapi"), str) or not spec["openapi"].strip():
        raise ValueError(f"{label}: missing valid 'openapi' version string")
    paths = spec.get("paths")
    if not isinstance(paths, dict) or len(paths) < min_paths:
        count = len(paths) if isinstance(paths, dict) else 0
        raise ValueError(
            f"{label}: expected at least {min_paths} paths, found {count}"
        )


def strip_docs_metadata(obj: Any, parent_key: str | None = None) -> Any:
    """Recursively remove prose/example/extension metadata and canonicalize unordered lists."""
    if isinstance(obj, dict):
        is_map_container = parent_key in MAP_CONTAINER_KEYS
        cleaned: dict[str, Any] = {}
        for key, value in obj.items():
            if not is_map_container and (key in DOC_ONLY_KEYS or key.startswith("x-")):
                continue
            # Entries inside a map container (e.g. a field schema under `properties`,
            # a status response under `responses`, a header under `headers`) are regular
            # OpenAPI objects, so reset parent_key to None when recursing into them.
            next_parent = None if is_map_container else key
            cleaned[key] = strip_docs_metadata(value, parent_key=next_parent)
        return cleaned
    if isinstance(obj, list):
        if parent_key == "security":
            # Each security requirement is {scheme_name: [scopes...]}; sort both scopes and entries.
            norm_entries: list[Any] = []
            for entry in obj:
                if isinstance(entry, dict):
                    norm_entries.append(
                        {
                            scheme: sorted(scopes) if isinstance(scopes, list) else scopes
                            for scheme, scopes in entry.items()
                        }
                    )
                else:
                    norm_entries.append(strip_docs_metadata(entry))
            return sorted(norm_entries, key=_canonical_sort_key)

        items = [strip_docs_metadata(item) for item in obj]
        if parent_key in SET_LIKE_LIST_KEYS:
            return sorted(items, key=_canonical_sort_key)
        return items
    return obj


def structural_view(spec: dict[str, Any]) -> dict[str, Any]:
    """Extract only API-surface sections that affect generated SDK code."""
    view: dict[str, Any] = {}

    raw_paths = spec.get("paths")
    if isinstance(raw_paths, dict):
        clean_paths: dict[str, Any] = {}
        for path_key, path_item in raw_paths.items():
            if not isinstance(path_item, dict):
                continue
            item_clean: dict[str, Any] = {}
            if "parameters" in path_item:
                item_clean["parameters"] = strip_docs_metadata(
                    path_item["parameters"], parent_key="parameters"
                )
            for method in HTTP_METHODS:
                if method in path_item and isinstance(path_item[method], dict):
                    item_clean[method] = strip_docs_metadata(path_item[method])
            clean_paths[path_key] = item_clean
        view["paths"] = clean_paths

    raw_components = spec.get("components")
    if isinstance(raw_components, dict):
        clean_components: dict[str, Any] = {}
        for section in STRUCTURAL_COMPONENT_SECTIONS:
            if section in raw_components and isinstance(raw_components[section], dict):
                clean_components[section] = strip_docs_metadata(
                    raw_components[section], parent_key=section
                )
        if clean_components:
            view["components"] = clean_components

    if "security" in spec:
        view["security"] = strip_docs_metadata(spec["security"], parent_key="security")

    return view


def resolve_ref(spec: dict[str, Any], obj: Any) -> Any:
    """Resolve local '#/.../...' JSON pointers inside an OpenAPI spec."""
    seen: set[str] = set()
    current = obj
    while isinstance(current, dict) and isinstance(current.get("$ref"), str):
        ref = current["$ref"]
        if not ref.startswith("#/") or ref in seen:
            break
        seen.add(ref)
        target: Any = spec
        for part in ref[2:].split("/"):
            part = part.replace("~1", "/").replace("~0", "~")
            if isinstance(target, dict) and part in target:
                target = target[part]
            else:
                return current
        current = target
    return current


def collect_operations(spec: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    ops: dict[tuple[str, str], dict[str, Any]] = {}
    for path, path_item in (spec.get("paths") or {}).items():
        if not isinstance(path_item, dict):
            continue
        path_params = path_item.get("parameters") or []
        for method in HTTP_METHODS:
            op = path_item.get(method)
            if isinstance(op, dict):
                merged = dict(op)
                if path_params:
                    merged["_path_parameters"] = path_params
                ops[(method.upper(), path)] = merged
    return ops


def _iter_params(spec: dict[str, Any], op: dict[str, Any]):
    """Yield ((in, name), resolved_param, raw_entry), path-level entries first."""
    for raw_list in (op.get("_path_parameters") or [], op.get("parameters") or []):
        if not isinstance(raw_list, list):
            continue
        for entry in raw_list:
            resolved = resolve_ref(spec, entry)
            if isinstance(resolved, dict) and "name" in resolved and "in" in resolved:
                yield (str(resolved["in"]), str(resolved["name"])), resolved, entry


def collect_params(spec: dict[str, Any], op: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    """Return {(in, name): resolved_param} with operation-level params overriding path-level."""
    return {key: resolved for key, resolved, _ in _iter_params(spec, op)}


def collect_param_entries(spec: dict[str, Any], op: dict[str, Any]) -> dict[tuple[str, str], Any]:
    """Return {(in, name): raw_entry}, i.e. the `$ref` object when the parameter is shared."""
    return {key: entry for key, _, entry in _iter_params(spec, op)}


def shared_component_name(old_raw: Any, new_raw: Any, section: str) -> str | None:
    """Return the component name when both sides are the same `#/components/<section>/<name>` ref.

    Such an entry is diffed once in the shared-components pass of `classify_diff` rather
    than once per referencing operation.
    """
    if not isinstance(old_raw, dict) or not isinstance(new_raw, dict):
        return None
    ref = old_raw.get("$ref")
    prefix = f"#/components/{section}/"
    if not isinstance(ref, str) or ref != new_raw.get("$ref") or not ref.startswith(prefix):
        return None
    name = ref[len(prefix):]
    return name if name and "/" not in name else None


def success_response_refs(spec: dict[str, Any]) -> set[str]:
    """Return every `$ref` used directly as a 2xx response by some operation."""
    refs: set[str] = set()
    for op in collect_operations(spec).values():
        responses = op.get("responses")
        if not isinstance(responses, dict):
            continue
        for status, response in responses.items():
            if (
                str(status).startswith("2")
                and isinstance(response, dict)
                and isinstance(response.get("$ref"), str)
            ):
                refs.add(response["$ref"])
    return refs


def schema_type_signature(spec: dict[str, Any], schema: Any) -> str:
    """Return a concise structural type signature including $ref, type, format, and nullable."""
    if not isinstance(schema, dict):
        return ""
    if isinstance(schema.get("$ref"), str):
        return f"$ref({schema['$ref']})"

    resolved = resolve_ref(spec, schema)
    if not isinstance(resolved, dict):
        return ""

    base = ""
    if "type" in resolved:
        t = str(resolved["type"])
        if t == "array" and "items" in resolved:
            base = f"array<{schema_type_signature(spec, resolved['items'])}>"
        else:
            base = t
    else:
        for comb in ("oneOf", "anyOf", "allOf"):
            if comb in resolved:
                base = comb
                break
        if not base and isinstance(resolved.get("properties"), dict):
            base = "object"

    fmt = resolved.get("format")
    if fmt:
        base = f"{base}({fmt})" if base else f"format({fmt})"
    if resolved.get("nullable"):
        base = f"{base}|null" if base else "null"
    return base


def schema_enum_values(schema: Any) -> set[str] | None:
    if not isinstance(schema, dict) or not isinstance(schema.get("enum"), list):
        return None
    return {json.dumps(v, sort_keys=True) for v in schema["enum"]}


def json_equal_structural(a: Any, b: Any, parent_key: str | None = None) -> bool:
    return strip_docs_metadata(a, parent_key=parent_key) == strip_docs_metadata(
        b, parent_key=parent_key
    )


def _schema_base_kind(schema: dict[str, Any]) -> str:
    if isinstance(schema.get("type"), str):
        return schema["type"]
    for comb in ("oneOf", "anyOf", "allOf"):
        if comb in schema:
            return comb
    if isinstance(schema.get("properties"), dict):
        return "object"
    return ""


def _diff_composition_branches(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    old_branches: list[Any],
    new_branches: list[Any],
    comb: str,
    location: str,
    breaking: list[str],
    seen_refs: frozenset[tuple[str, str]],
) -> None:
    """Detect breaking changes across allOf / oneOf / anyOf schema branches."""
    old_refs = {
        b["$ref"] for b in old_branches if isinstance(b, dict) and isinstance(b.get("$ref"), str)
    }
    new_refs = {
        b["$ref"] for b in new_branches if isinstance(b, dict) and isinstance(b.get("$ref"), str)
    }

    for removed_ref in sorted(old_refs - new_refs):
        breaking.append(f"Removed `{comb}` variant `{removed_ref}` on `{location}`")

    # For allOf, adding a new $ref branch could introduce required fields (checked if needed);
    # for oneOf/anyOf, adding a branch widens the union (non-breaking), removing narrows it.
    old_inlines = [
        b for b in old_branches if isinstance(b, dict) and not isinstance(b.get("$ref"), str)
    ]
    new_inlines = [
        b for b in new_branches if isinstance(b, dict) and not isinstance(b.get("$ref"), str)
    ]

    if comb == "allOf":
        # Merge inline object properties/required across allOf inline branches
        old_merged_props: dict[str, Any] = {}
        old_merged_req: set[str] = set()
        for b in old_inlines:
            if isinstance(b.get("properties"), dict):
                old_merged_props.update(b["properties"])
            if isinstance(b.get("required"), list):
                old_merged_req.update(str(r) for r in b["required"])

        new_merged_props: dict[str, Any] = {}
        new_merged_req: set[str] = set()
        for b in new_inlines:
            if isinstance(b.get("properties"), dict):
                new_merged_props.update(b["properties"])
            if isinstance(b.get("required"), list):
                new_merged_req.update(str(r) for r in b["required"])

        for prop in sorted(set(old_merged_props) - set(new_merged_props)):
            breaking.append(f"Removed property `{location}.{prop}`")
        for prop in sorted(new_merged_req - old_merged_req):
            breaking.append(f"Property `{location}.{prop}` became required")
        for prop in sorted(set(old_merged_props) & set(new_merged_props)):
            diff_schemas(
                old_spec,
                new_spec,
                old_merged_props[prop],
                new_merged_props[prop],
                f"{location}.{prop}",
                breaking,
                seen_refs,
            )

        # Also check any non-object inline allOf branches (e.g. enum/type restrictions)
        if len(old_inlines) == 1 and len(new_inlines) == 1:
            if not old_merged_props and not new_merged_props:
                diff_schemas(
                    old_spec,
                    new_spec,
                    old_inlines[0],
                    new_inlines[0],
                    f"{location}[allOf]",
                    breaking,
                    seen_refs,
                )
        return

    # oneOf / anyOf inline branches: match unchanged structural branches first, then pair by kind
    remaining_new = list(new_inlines)
    unmatched_old: list[dict[str, Any]] = []
    for ob in old_inlines:
        ob_norm = strip_docs_metadata(ob)
        matched_idx = None
        for idx, nb in enumerate(remaining_new):
            if strip_docs_metadata(nb) == ob_norm:
                matched_idx = idx
                break
        if matched_idx is not None:
            remaining_new.pop(matched_idx)
        else:
            unmatched_old.append(ob)

    for ob in unmatched_old:
        ob_kind = _schema_base_kind(ob)
        same_kind_idx = None
        for idx, nb in enumerate(remaining_new):
            if _schema_base_kind(nb) == ob_kind and ob_kind:
                same_kind_idx = idx
                break
        if same_kind_idx is not None:
            nb = remaining_new.pop(same_kind_idx)
            diff_schemas(
                old_spec,
                new_spec,
                ob,
                nb,
                f"{location}[{comb}]",
                breaking,
                seen_refs,
            )
        else:
            breaking.append(
                f"Removed or incompatible `{comb}` inline variant (`{ob_kind or 'schema'}`) on `{location}`"
            )


def diff_schemas(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    old_raw: Any,
    new_raw: Any,
    location: str,
    breaking: list[str],
    seen_refs: frozenset[tuple[str, str]] = frozenset(),
) -> None:
    """Recursively compare two OpenAPI schemas and append breaking changes."""
    if not isinstance(old_raw, dict):
        return
    if not isinstance(new_raw, dict):
        # A typed parameter, request body or response lost its schema altogether.
        if strip_docs_metadata(old_raw):
            breaking.append(f"Removed schema at `{location}`")
        return

    old_ref = old_raw.get("$ref") if isinstance(old_raw.get("$ref"), str) else None
    new_ref = new_raw.get("$ref") if isinstance(new_raw.get("$ref"), str) else None

    if old_ref is not None or new_ref is not None:
        if old_ref != new_ref:
            old_label = old_ref or (schema_type_signature(old_spec, old_raw) or "inline")
            new_label = new_ref or (schema_type_signature(new_spec, new_raw) or "inline")
            breaking.append(
                f"Schema reference changed at `{location}`: `{old_label}` -> `{new_label}`"
            )
            return

        # Both point to the exact same `$ref`.
        assert old_ref is not None and new_ref is not None
        # Component schemas are already diffed exhaustively in the top-level schemas pass,
        # so skip re-entering them here to avoid duplicate reports and cycles.
        if old_ref.startswith("#/components/schemas/"):
            return

        ref_pair = (old_ref, new_ref)
        if ref_pair in seen_refs:
            return
        seen_refs = seen_refs | {ref_pair}

    old_s = resolve_ref(old_spec, old_raw)
    new_s = resolve_ref(new_spec, new_raw)
    if not isinstance(old_s, dict) or not isinstance(new_s, dict):
        return

    # 1. Base type / combinator kind
    old_kind = _schema_base_kind(old_s)
    new_kind = _schema_base_kind(new_s)
    if old_kind != new_kind:
        breaking.append(
            f"Type changed at `{location}`: `{old_kind or 'any'}` -> `{new_kind or 'any'}`"
        )
        return

    # 2. Format changes (e.g. int32 -> int64, date-time added/removed)
    old_fmt = old_s.get("format")
    new_fmt = new_s.get("format")
    if old_fmt != new_fmt:
        breaking.append(
            f"Format changed at `{location}`: `{old_fmt or 'none'}` -> `{new_fmt or 'none'}`"
        )

    # 3. Nullability changes
    old_nullable = bool(old_s.get("nullable", False))
    new_nullable = bool(new_s.get("nullable", False))
    if old_nullable != new_nullable:
        breaking.append(
            f"Nullability changed at `{location}`: `{old_nullable}` -> `{new_nullable}`"
        )

    # 4. Enum added, removed, or values removed
    old_enum = schema_enum_values(old_s)
    new_enum = schema_enum_values(new_s)
    if old_enum is None and new_enum is not None:
        breaking.append(f"Added enum constraint at `{location}`")
    elif old_enum is not None and new_enum is None:
        breaking.append(f"Removed enum constraint at `{location}`")
    elif old_enum is not None and new_enum is not None:
        removed_vals = sorted(old_enum - new_enum)
        if removed_vals:
            breaking.append(
                f"Removed enum value(s) at `{location}`: {', '.join(removed_vals[:5])}"
            )

    # 5. Array items (recursive — catches items.enum, items.type, nested objects, etc.)
    old_has_items = "items" in old_s
    new_has_items = "items" in new_s
    if old_has_items and new_has_items:
        diff_schemas(
            old_spec,
            new_spec,
            old_s["items"],
            new_s["items"],
            f"{location}[]",
            breaking,
            seen_refs,
        )
    elif old_has_items != new_has_items:
        breaking.append(f"Array `items` schema changed at `{location}`")

    # 6. Object properties and required fields (recursive)
    old_props = old_s.get("properties") if isinstance(old_s.get("properties"), dict) else {}
    new_props = new_s.get("properties") if isinstance(new_s.get("properties"), dict) else {}

    for prop in sorted(set(old_props) - set(new_props)):
        breaking.append(f"Removed property `{location}.{prop}`")

    old_req = set(str(r) for r in (old_s.get("required") or []))
    new_req = set(str(r) for r in (new_s.get("required") or []))
    for prop in sorted(new_req - old_req):
        breaking.append(f"Property `{location}.{prop}` became required")

    for prop in sorted(set(old_props) & set(new_props)):
        diff_schemas(
            old_spec,
            new_spec,
            old_props[prop],
            new_props[prop],
            f"{location}.{prop}",
            breaking,
            seen_refs,
        )

    # 7. additionalProperties tightening or schema changes
    old_ap = old_s.get("additionalProperties")
    new_ap = new_s.get("additionalProperties")
    if old_ap is not False and new_ap is False:
        breaking.append(f"Disallowed `additionalProperties` at `{location}`")
    elif isinstance(old_ap, dict) and isinstance(new_ap, dict):
        diff_schemas(
            old_spec,
            new_spec,
            old_ap,
            new_ap,
            f"{location}.*",
            breaking,
            seen_refs,
        )

    # 8. Composition schemas (allOf, oneOf, anyOf)
    for comb in ("allOf", "oneOf", "anyOf"):
        old_branches = old_s.get(comb)
        new_branches = new_s.get(comb)
        if isinstance(old_branches, list) and isinstance(new_branches, list):
            _diff_composition_branches(
                old_spec,
                new_spec,
                old_branches,
                new_branches,
                comb,
                location,
                breaking,
                seen_refs,
            )


def diff_parameter(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    old_p: dict[str, Any],
    new_p: dict[str, Any],
    owner: str,
    location: str,
    breaking: list[str],
) -> None:
    """Compare two definitions of the same parameter. `owner` is already back-quoted."""
    p_name = str(new_p.get("name"))
    if not old_p.get("required") and new_p.get("required"):
        breaking.append(f"Parameter `{p_name}` became required on {owner}")
    diff_schemas(
        old_spec,
        new_spec,
        old_p.get("schema"),
        new_p.get("schema"),
        f"{location} param `{p_name}`",
        breaking,
    )


def diff_request_body(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    old_rb: dict[str, Any],
    new_rb: dict[str, Any],
    owner: str,
    location: str,
    breaking: list[str],
) -> None:
    """Compare two request bodies, including inline schemas and media types."""
    if not old_rb.get("required") and new_rb.get("required"):
        breaking.append(f"Request body became required on {owner}")
    old_content = old_rb.get("content") if isinstance(old_rb.get("content"), dict) else {}
    new_content = new_rb.get("content") if isinstance(new_rb.get("content"), dict) else {}
    for media in sorted(set(old_content) - set(new_content)):
        breaking.append(f"Removed `{media}` request body on {owner}")
    for media in sorted(set(old_content) & set(new_content)):
        old_mt = old_content[media] if isinstance(old_content[media], dict) else {}
        new_mt = new_content[media] if isinstance(new_content[media], dict) else {}
        diff_schemas(
            old_spec,
            new_spec,
            old_mt.get("schema"),
            new_mt.get("schema"),
            f"{location}({media})",
            breaking,
        )


def diff_response(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    old_resp: dict[str, Any],
    new_resp: dict[str, Any],
    owner: str,
    location: str,
    breaking: list[str],
) -> None:
    """Compare two success responses, including inline schemas and media types."""
    old_rc = old_resp.get("content") if isinstance(old_resp.get("content"), dict) else {}
    new_rc = new_resp.get("content") if isinstance(new_resp.get("content"), dict) else {}
    for media in sorted(set(old_rc) - set(new_rc)):
        breaking.append(f"Removed `{media}` from {owner}")
    for media in sorted(set(old_rc) & set(new_rc)):
        old_mt = old_rc[media] if isinstance(old_rc[media], dict) else {}
        new_mt = new_rc[media] if isinstance(new_rc[media], dict) else {}
        diff_schemas(
            old_spec,
            new_spec,
            old_mt.get("schema"),
            new_mt.get("schema"),
            f"{location}({media})",
            breaking,
        )


def diff_shared_components(
    old_spec: dict[str, Any],
    new_spec: dict[str, Any],
    breaking: list[str],
    schema_changes: list[str],
) -> None:
    """Diff `components.parameters`, `.requestBodies` and `.responses` entries, once each.

    An operation that only points at one of these through `$ref` is itself unchanged when
    the shared definition changes (e.g. a value removed from the `tweet.fields` enum), so
    the per-operation pass cannot see it.
    """
    old_components = old_spec.get("components")
    new_components = new_spec.get("components")
    if not isinstance(old_components, dict) or not isinstance(new_components, dict):
        return
    success_refs = success_response_refs(old_spec) | success_response_refs(new_spec)

    for section, noun in (
        ("parameters", "parameter"),
        ("requestBodies", "request body"),
        ("responses", "response"),
    ):
        old_shared = old_components.get(section)
        new_shared = new_components.get(section)
        if not isinstance(old_shared, dict) or not isinstance(new_shared, dict):
            continue
        for name in sorted(set(old_shared) & set(new_shared)):
            old_c = resolve_ref(old_spec, old_shared[name])
            new_c = resolve_ref(new_spec, new_shared[name])
            if not isinstance(old_c, dict) or not isinstance(new_c, dict):
                continue
            if json_equal_structural(old_c, new_c):
                continue
            schema_changes.append(f"Updated shared {noun} `{name}`")
            ref = f"#/components/{section}/{name}"
            owner = f"`{ref}`"
            if section == "parameters":
                old_key = (str(old_c.get("in")), str(old_c.get("name")))
                new_key = (str(new_c.get("in")), str(new_c.get("name")))
                if old_key != new_key:
                    breaking.append(
                        f"Shared parameter {owner} changed from {old_key[0]} `{old_key[1]}` "
                        f"to {new_key[0]} `{new_key[1]}`"
                    )
                    continue
                diff_parameter(old_spec, new_spec, old_c, new_c, owner, ref, breaking)
            elif section == "requestBodies":
                diff_request_body(old_spec, new_spec, old_c, new_c, owner, ref, breaking)
            elif ref in success_refs:
                diff_response(
                    old_spec, new_spec, old_c, new_c, f"shared response {owner}", ref, breaking
                )


def classify_diff(old_spec: dict[str, Any], new_spec: dict[str, Any]) -> dict[str, Any]:
    breaking: list[str] = []
    added_endpoints: list[str] = []
    modified_endpoints: list[str] = []
    schema_changes: list[str] = []

    old_view = structural_view(old_spec)
    new_view = structural_view(new_spec)

    if old_view == new_view:
        return {
            "changed": False,
            "change_level": "none",
            "breaking_changes": [],
            "added_endpoints": [],
            "modified_endpoints": [],
            "schema_changes": [],
            "summary": "No structural OpenAPI changes",
        }

    old_ops = collect_operations(old_spec)
    new_ops = collect_operations(new_spec)

    for key in sorted(set(old_ops) - set(new_ops)):
        method, path = key
        breaking.append(f"Removed endpoint `{method} {path}`")

    for key in sorted(set(new_ops) - set(old_ops)):
        method, path = key
        added_endpoints.append(f"`{method} {path}`")

    for key in sorted(set(old_ops) & set(new_ops)):
        method, path = key
        old_op = old_ops[key]
        new_op = new_ops[key]
        if json_equal_structural(old_op, new_op):
            continue

        endpoint_label = f"`{method} {path}`"
        modified_endpoints.append(endpoint_label)

        # operationId rename, addition, or removal changes generated method name
        old_op_id = old_op.get("operationId")
        new_op_id = new_op.get("operationId")
        if old_op_id != new_op_id:
            breaking.append(
                f"Changed operationId on {endpoint_label}: `{old_op_id or 'none'}` -> `{new_op_id or 'none'}`"
            )

        # Primary tag change moves method to a different sub-client class
        old_tags = old_op.get("tags") or []
        new_tags = new_op.get("tags") or []
        old_primary = old_tags[0] if old_tags else None
        new_primary = new_tags[0] if new_tags else None
        if old_primary != new_primary:
            breaking.append(
                f"Moved {endpoint_label} from tag `{old_primary}` to `{new_primary}`"
            )

        # Parameters diff
        old_params = collect_params(old_spec, old_op)
        new_params = collect_params(new_spec, new_op)
        old_param_entries = collect_param_entries(old_spec, old_op)
        new_param_entries = collect_param_entries(new_spec, new_op)

        for p_key in sorted(set(old_params) - set(new_params)):
            p_in, p_name = p_key
            breaking.append(f"Removed {p_in} parameter `{p_name}` on {endpoint_label}")

        for p_key in sorted(set(new_params) - set(old_params)):
            p_in, p_name = p_key
            if new_params[p_key].get("required") or p_in == "path":
                breaking.append(
                    f"Added required {p_in} parameter `{p_name}` on {endpoint_label}"
                )

        for p_key in sorted(set(old_params) & set(new_params)):
            if shared_component_name(
                old_param_entries.get(p_key), new_param_entries.get(p_key), "parameters"
            ):
                continue
            diff_parameter(
                old_spec,
                new_spec,
                old_params[p_key],
                new_params[p_key],
                endpoint_label,
                f"{method} {path}",
                breaking,
            )

        # Request body diff (including inline schemas & media types)
        old_rb_raw = old_op.get("requestBody")
        new_rb_raw = new_op.get("requestBody")
        old_rb = resolve_ref(old_spec, old_rb_raw) or {}
        new_rb = resolve_ref(new_spec, new_rb_raw) or {}
        if (
            isinstance(old_rb, dict)
            and isinstance(new_rb, dict)
            and not shared_component_name(old_rb_raw, new_rb_raw, "requestBodies")
        ):
            diff_request_body(
                old_spec,
                new_spec,
                old_rb,
                new_rb,
                endpoint_label,
                f"{method} {path} requestBody",
                breaking,
            )

        # 2xx responses diff (including inline response schemas & media types)
        old_responses = {
            str(k): v
            for k, v in (old_op.get("responses") or {}).items()
            if str(k).startswith("2")
        }
        new_responses = {
            str(k): v
            for k, v in (new_op.get("responses") or {}).items()
            if str(k).startswith("2")
        }
        for status in sorted(set(old_responses) - set(new_responses)):
            breaking.append(f"Removed `{status}` response on {endpoint_label}")
        for status in sorted(set(old_responses) & set(new_responses)):
            if shared_component_name(old_responses[status], new_responses[status], "responses"):
                continue
            old_resp = resolve_ref(old_spec, old_responses[status])
            new_resp = resolve_ref(new_spec, new_responses[status])
            if not isinstance(old_resp, dict) or not isinstance(new_resp, dict):
                continue
            diff_response(
                old_spec,
                new_spec,
                old_resp,
                new_resp,
                f"`{status}` response on {endpoint_label}",
                f"{method} {path} response[{status}]",
                breaking,
            )

    # Component schemas diff (recursive)
    old_schemas = (old_spec.get("components") or {}).get("schemas") or {}
    new_schemas = (new_spec.get("components") or {}).get("schemas") or {}

    for name in sorted(set(old_schemas) - set(new_schemas)):
        breaking.append(f"Removed schema `{name}`")

    for name in sorted(set(new_schemas) - set(old_schemas)):
        schema_changes.append(f"Added schema `{name}`")

    for name in sorted(set(old_schemas) & set(new_schemas)):
        old_s = old_schemas[name]
        new_s = new_schemas[name]
        if json_equal_structural(old_s, new_s):
            continue
        schema_changes.append(f"Updated schema `{name}`")
        diff_schemas(old_spec, new_spec, old_s, new_s, name, breaking)

    diff_shared_components(old_spec, new_spec, breaking, schema_changes)

    # Deduplicate breaking messages while preserving order
    breaking = list(dict.fromkeys(breaking))

    if breaking:
        change_level = "breaking"
    elif added_endpoints:
        change_level = "feature"
    else:
        change_level = "patch"

    parts: list[str] = []
    if breaking:
        parts.append(f"{len(breaking)} breaking change(s)")
    if added_endpoints:
        parts.append(f"{len(added_endpoints)} new endpoint(s)")
    if modified_endpoints:
        parts.append(f"{len(modified_endpoints)} updated endpoint(s)")
    if schema_changes:
        parts.append(f"{len(schema_changes)} schema change(s)")
    if not parts:
        parts.append("OpenAPI specification metadata/security update")

    prefix = "BREAKING: " if breaking else ""
    summary = prefix + ", ".join(parts)

    return {
        "changed": True,
        "change_level": change_level,
        "breaking_changes": breaking,
        "added_endpoints": added_endpoints,
        "modified_endpoints": modified_endpoints,
        "schema_changes": schema_changes,
        "summary": summary,
    }


def read_sdk_versions(config_path: Path) -> dict[str, str]:
    versions: dict[str, str] = {}
    text = config_path.read_text(encoding="utf-8")
    for sdk in SDKS:
        match = re.search(rf'^{sdk}\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
        if match:
            versions[sdk] = match.group(1)
    return versions


def compute_sdk_bumps(
    change_level: str,
    versions: dict[str, str],
    force_bump: str = "auto",
) -> dict[str, str]:
    if force_bump != "auto":
        return {sdk: force_bump for sdk in SDKS}
    if change_level == "none":
        return {sdk: "none" for sdk in SDKS}
    if change_level == "patch":
        return {sdk: "patch" for sdk in SDKS}
    if change_level == "feature":
        return {sdk: "minor" for sdk in SDKS}

    # Breaking change: SemVer 2.0.0 bumps minor for 0.x.y and major for >=1.0.0.
    bumps: dict[str, str] = {}
    for sdk in SDKS:
        ver = versions.get(sdk, "0.0.0")
        major_str = ver.split(".", 1)[0]
        major = int(major_str) if major_str.isdigit() else 0
        bumps[sdk] = "major" if major >= 1 else "minor"
    return bumps


def render_markdown(result: dict[str, Any], bumps: dict[str, str]) -> str:
    lines = [
        "## OpenAPI Spec Diff Summary",
        "",
        f"- **Changed:** `{str(result['changed']).lower()}`",
        f"- **Classification:** `{result['change_level']}`",
        f"- **Summary:** {result['summary']}",
        "- **Planned Bumps:** "
        + ", ".join(f"{sdk}=`{bumps[sdk]}`" for sdk in SDKS),
        "",
    ]

    def add_section(title: str, items: list[str], limit: int = 30) -> None:
        if not items:
            return
        lines.append(f"### {title} ({len(items)})")
        lines.append("")
        for item in items[:limit]:
            lines.append(f"- {item}")
        if len(items) > limit:
            lines.append(f"- ... and {len(items) - limit} more")
        lines.append("")

    add_section("Breaking Changes", result["breaking_changes"])
    add_section("Added Endpoints", result["added_endpoints"])
    add_section("Modified Endpoints", result["modified_endpoints"])
    add_section("Schema Changes", result["schema_changes"])

    return "\n".join(lines).rstrip() + "\n"


def write_github_outputs(
    github_output_path: Path,
    result: dict[str, Any],
    bumps: dict[str, str],
) -> None:
    should_release = any(b != "none" for b in bumps.values())
    with github_output_path.open("a", encoding="utf-8") as fh:
        fh.write(f"changed={'true' if result['changed'] else 'false'}\n")
        fh.write(f"should_release={'true' if should_release else 'false'}\n")
        fh.write(f"change_level={result['change_level']}\n")
        fh.write(f"summary={result['summary']}\n")
        for sdk in SDKS:
            fh.write(f"{sdk}_bump={bumps[sdk]}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("old_spec", type=Path, help="Committed baseline OpenAPI JSON")
    parser.add_argument("new_spec", type=Path, help="Newly fetched OpenAPI JSON")
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to xdk-config.toml (used to map breaking changes on 0.x vs >=1.0)",
    )
    parser.add_argument(
        "--min-paths",
        type=int,
        default=50,
        help="Minimum path count required in new_spec to guard against truncated fetches",
    )
    parser.add_argument(
        "--force-bump",
        choices=("auto", "patch", "minor", "major"),
        default="auto",
        help="Override automatic bump calculation",
    )
    parser.add_argument("--json-out", type=Path, default=None)
    parser.add_argument("--markdown-out", type=Path, default=None)
    parser.add_argument("--github-output", type=Path, default=None)
    args = parser.parse_args(argv)

    old_spec = load_json(args.old_spec)
    new_spec = load_json(args.new_spec)
    validate_openapi_spec(old_spec, str(args.old_spec), min_paths=1)
    validate_openapi_spec(new_spec, str(args.new_spec), min_paths=args.min_paths)

    result = classify_diff(old_spec, new_spec)
    versions = read_sdk_versions(args.config) if args.config else {}
    bumps = compute_sdk_bumps(result["change_level"], versions, args.force_bump)
    result["bumps"] = bumps
    result["should_release"] = any(b != "none" for b in bumps.values())

    md = render_markdown(result, bumps)
    if args.json_out:
        args.json_out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if args.markdown_out:
        args.markdown_out.write_text(md, encoding="utf-8")
    if args.github_output:
        write_github_outputs(args.github_output, result, bumps)

    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
