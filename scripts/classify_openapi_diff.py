#!/usr/bin/env python3
"""Classify semantic changes between two OpenAPI specifications for XDK auto-releases.

Outputs a deterministic bump recommendation per SDK:
  - No structural API surface changes (prose/docs/key-order only) -> "none"
  - Backwards-compatible schema/parameter/enum/auth updates       -> "patch"
  - New endpoints/operations                                      -> "minor"
  - Breaking changes (removed endpoints/params/fields, newly
    required params, type/operationId/tag changes, removed enums):
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

STRUCTURAL_COMPONENT_SECTIONS = (
    "schemas",
    "parameters",
    "requestBodies",
    "responses",
    "securitySchemes",
    "headers",
)


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


def strip_docs_metadata(obj: Any, parent_key: str | None = None) -> Any:
    """Recursively remove prose/example/extension metadata and canonicalize unordered lists."""
    if isinstance(obj, dict):
        cleaned: dict[str, Any] = {}
        for key, value in obj.items():
            if key in DOC_ONLY_KEYS or key.startswith("x-"):
                continue
            cleaned[key] = strip_docs_metadata(value, parent_key=key)
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
                clean_components[section] = strip_docs_metadata(raw_components[section])
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


def collect_params(spec: dict[str, Any], op: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    """Return {(in, name): resolved_param} with operation-level params overriding path-level."""
    params: dict[tuple[str, str], dict[str, Any]] = {}
    for raw_list in (op.get("_path_parameters") or [], op.get("parameters") or []):
        if not isinstance(raw_list, list):
            continue
        for entry in raw_list:
            resolved = resolve_ref(spec, entry)
            if isinstance(resolved, dict) and "name" in resolved and "in" in resolved:
                params[(str(resolved["in"]), str(resolved["name"]))] = resolved
    return params


def schema_type_signature(spec: dict[str, Any], schema: Any) -> str:
    resolved = resolve_ref(spec, schema)
    if not isinstance(resolved, dict):
        return ""
    if "type" in resolved:
        t = str(resolved["type"])
        if t == "array" and "items" in resolved:
            return f"array<{schema_type_signature(spec, resolved['items'])}>"
        return t
    for comb in ("oneOf", "anyOf", "allOf"):
        if comb in resolved:
            return comb
    return ""


def schema_enum_values(spec: dict[str, Any], schema: Any) -> set[str] | None:
    resolved = resolve_ref(spec, schema)
    if not isinstance(resolved, dict) or not isinstance(resolved.get("enum"), list):
        return None
    return {json.dumps(v, sort_keys=True) for v in resolved["enum"]}


def json_equal_structural(a: Any, b: Any) -> bool:
    return strip_docs_metadata(a) == strip_docs_metadata(b)


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

        # operationId rename changes generated method name
        old_op_id = old_op.get("operationId")
        new_op_id = new_op.get("operationId")
        if old_op_id and new_op_id and old_op_id != new_op_id:
            breaking.append(
                f"Renamed operationId on {endpoint_label}: `{old_op_id}` -> `{new_op_id}`"
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
            p_in, p_name = p_key
            old_p = old_params[p_key]
            new_p = new_params[p_key]
            if not old_p.get("required") and new_p.get("required"):
                breaking.append(
                    f"Parameter `{p_name}` became required on {endpoint_label}"
                )
            old_t = schema_type_signature(old_spec, old_p.get("schema"))
            new_t = schema_type_signature(new_spec, new_p.get("schema"))
            if old_t and new_t and old_t != new_t:
                breaking.append(
                    f"Parameter `{p_name}` type changed on {endpoint_label}: `{old_t}` -> `{new_t}`"
                )
            old_enum = schema_enum_values(old_spec, old_p.get("schema"))
            new_enum = schema_enum_values(new_spec, new_p.get("schema"))
            if old_enum is not None and new_enum is not None:
                removed_vals = sorted(old_enum - new_enum)
                if removed_vals:
                    breaking.append(
                        f"Removed enum value(s) on parameter `{p_name}` ({endpoint_label}): {', '.join(removed_vals[:5])}"
                    )

        # Request body diff
        old_rb = resolve_ref(old_spec, old_op.get("requestBody")) or {}
        new_rb = resolve_ref(new_spec, new_op.get("requestBody")) or {}
        if isinstance(old_rb, dict) and isinstance(new_rb, dict):
            if not old_rb.get("required") and new_rb.get("required"):
                breaking.append(f"Request body became required on {endpoint_label}")
            old_rb_schema = (
                (old_rb.get("content") or {}).get("application/json", {}).get("schema")
            )
            new_rb_schema = (
                (new_rb.get("content") or {}).get("application/json", {}).get("schema")
            )
            if old_rb_schema and not new_rb_schema:
                breaking.append(f"Removed JSON request body on {endpoint_label}")

        # 2xx responses diff
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

    # Component schemas diff
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

        old_t = schema_type_signature(old_spec, old_s)
        new_t = schema_type_signature(new_spec, new_s)
        if old_t and new_t and old_t != new_t:
            breaking.append(f"Schema `{name}` type changed: `{old_t}` -> `{new_t}`")

        old_enum = schema_enum_values(old_spec, old_s)
        new_enum = schema_enum_values(new_spec, new_s)
        if old_enum is not None and new_enum is not None:
            removed_vals = sorted(old_enum - new_enum)
            if removed_vals:
                breaking.append(
                    f"Removed enum value(s) on schema `{name}`: {', '.join(removed_vals[:5])}"
                )

        if isinstance(old_s, dict) and isinstance(new_s, dict):
            old_props = old_s.get("properties") or {}
            new_props = new_s.get("properties") or {}
            if isinstance(old_props, dict) and isinstance(new_props, dict):
                for prop in sorted(set(old_props) - set(new_props)):
                    breaking.append(f"Removed property `{name}.{prop}`")
                for prop in sorted(set(old_props) & set(new_props)):
                    pt_old = schema_type_signature(old_spec, old_props[prop])
                    pt_new = schema_type_signature(new_spec, new_props[prop])
                    if pt_old and pt_new and pt_old != pt_new:
                        breaking.append(
                            f"Property `{name}.{prop}` type changed: `{pt_old}` -> `{pt_new}`"
                        )
                    pe_old = schema_enum_values(old_spec, old_props[prop])
                    pe_new = schema_enum_values(new_spec, new_props[prop])
                    if pe_old is not None and pe_new is not None:
                        removed_vals = sorted(pe_old - pe_new)
                        if removed_vals:
                            breaking.append(
                                f"Removed enum value(s) on `{name}.{prop}`: {', '.join(removed_vals[:5])}"
                            )

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
