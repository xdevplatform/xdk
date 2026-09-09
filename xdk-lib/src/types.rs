//! Language type rendering engine.
//!
//! Converts OpenAPI schemas (as serialized JSON, where `$ref`s carry both the
//! reference path and the inlined resolved value) into TypeScript and Python
//! type expressions and full schema-module declarations.
//!
//! The walker never follows `$ref`s recursively — a reference always renders as
//! the referenced type's name — so cyclic schemas cannot cause unbounded
//! recursion.

use serde_json::Value as Json;
use std::collections::{BTreeMap, HashMap, HashSet};

/// Maximum nesting depth for inline schema rendering. Deeper structures fall
/// back to the language's "unspecified" type instead of recursing forever.
const MAX_DEPTH: usize = 32;

// ============================================================
// Shared helpers
// ============================================================

/// Sanitize a schema/component name into a valid identifier.
/// e.g. "my-schema" -> "my_schema", "2fa" -> "_2fa".
pub fn sanitize_identifier(name: &str) -> String {
    let mut out: String = name
        .chars()
        .map(|c| {
            if c.is_ascii_alphanumeric() || c == '_' {
                c
            } else {
                '_'
            }
        })
        .collect();
    if out.is_empty() || out.chars().next().unwrap().is_ascii_digit() {
        out.insert(0, '_');
    }
    out
}

/// Extract the component name from a `$ref` path and sanitize it.
fn ref_name(path: &str) -> String {
    sanitize_identifier(path.rsplit('/').next().unwrap_or(path))
}

/// Names that would shadow typing/pydantic imports (or builtins) inside the
/// generated Python schemas module. Colliding schema names get an `X` prefix
/// (e.g. the X API's `List` becomes `XList`).
const PY_RESERVED_SCHEMA_NAMES: &[&str] = &[
    "Any",
    "Dict",
    "List",
    "Optional",
    "Union",
    "Literal",
    "BaseModel",
    "ConfigDict",
    "Field",
    "str",
    "int",
    "float",
    "bool",
    "dict",
    "list",
    "set",
    "tuple",
    "type",
    "object",
    "bytes",
];

/// Python-safe schema type name.
pub fn py_schema_ident(name: &str) -> String {
    let ident = sanitize_identifier(name);
    if PY_RESERVED_SCHEMA_NAMES.contains(&ident.as_str()) {
        format!("X{ident}")
    } else {
        ident
    }
}

/// Python-safe name for a referenced schema.
fn py_ref_name(path: &str) -> String {
    py_schema_ident(path.rsplit('/').next().unwrap_or(path))
}

/// Python 3 keywords: illegal as Pydantic field names (they cause a
/// SyntaxError in the generated class body).
const PY_KEYWORDS: &[&str] = &[
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", "class", "continue",
    "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import",
    "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while",
    "with", "yield",
];

/// Python-safe field name: sanitized, with keywords suffixed by `_` (the
/// caller adds a Field alias whenever the result differs from the original).
fn py_field_ident(name: &str) -> String {
    let ident = sanitize_identifier(name);
    if PY_KEYWORDS.contains(&ident.as_str()) {
        format!("{ident}_")
    } else {
        ident
    }
}

/// Get a non-null field from a JSON object (serialized Option fields are
/// explicit nulls, which must be treated as absent).
fn get<'a>(schema: &'a Json, key: &str) -> Option<&'a Json> {
    match schema.get(key) {
        Some(Json::Null) | None => None,
        Some(v) => Some(v),
    }
}

fn get_str<'a>(schema: &'a Json, key: &str) -> Option<&'a str> {
    get(schema, key).and_then(|v| v.as_str())
}

fn is_nullable(schema: &Json) -> bool {
    get(schema, "nullable")
        .and_then(|v| v.as_bool())
        .unwrap_or(false)
}

/// Mirror of the generated TypeScript runtime `snakeToCamel`: only
/// `_<lowercase letter>` boundaries are rewritten, everything else is kept.
/// Interface keys must use the exact same transform the runtime applies to
/// response payloads.
pub fn snake_to_camel(key: &str) -> String {
    let mut out = String::with_capacity(key.len());
    let mut chars = key.chars().peekable();
    while let Some(c) = chars.next() {
        if c == '_' {
            match chars.peek() {
                Some(&next) if next.is_ascii_lowercase() => {
                    out.push(next.to_ascii_uppercase());
                    chars.next();
                }
                _ => out.push(c),
            }
        } else {
            out.push(c);
        }
    }
    out
}

/// Escape a string for a double-quoted literal (valid in both TS and Python).
pub fn escape_string(s: &str) -> String {
    let mut out = String::with_capacity(s.len());
    for c in s.chars() {
        match c {
            '\\' => out.push_str("\\\\"),
            '"' => out.push_str("\\\""),
            '\n' => out.push_str("\\n"),
            '\r' => out.push_str("\\r"),
            '\t' => out.push_str("\\t"),
            _ => out.push(c),
        }
    }
    out
}

/// Escape text for inclusion inside a `/** ... */` doc comment.
fn escape_doc(s: &str) -> String {
    s.replace("*/", "*\\/").replace('\n', " ")
}

/// Escape text for inclusion inside a Python `"""..."""` docstring.
fn escape_py_doc(s: &str) -> String {
    s.replace('\\', "\\\\").replace("\"\"\"", "\\\"\\\"\\\"")
}

/// Is a TS property key a valid identifier, or does it need quoting?
fn ts_key(key: &str) -> String {
    let valid = !key.is_empty()
        && !key.chars().next().unwrap().is_ascii_digit()
        && key
            .chars()
            .all(|c| c.is_ascii_alphanumeric() || c == '_' || c == '$');
    if valid {
        key.to_string()
    } else {
        format!("\"{}\"", escape_string(key))
    }
}

/// Enum values rendered as literals ("a" | "b" for TS). Returns None when the
/// schema has no usable enum.
fn enum_literals(schema: &Json) -> Option<Vec<String>> {
    let values = get(schema, "enum")?.as_array()?;
    if values.is_empty() {
        return None;
    }
    let mut out = Vec::with_capacity(values.len());
    for v in values {
        match v {
            Json::String(s) => out.push(format!("\"{}\"", escape_string(s))),
            Json::Number(n) => out.push(n.to_string()),
            // Boolean, null, or exotic enum members: bail out to the base
            // type. (`true`/`false` literals are valid TS but invalid inside
            // Python's `Literal[...]`, and boolean enums are malformed on
            // string/integer schemas anyway.)
            _ => return None,
        }
    }
    Some(out)
}

/// Union member lists for oneOf/anyOf, deduplicated while preserving order.
fn dedupe(members: Vec<String>) -> Vec<String> {
    let mut seen = HashSet::new();
    members
        .into_iter()
        .filter(|m| seen.insert(m.clone()))
        .collect()
}

// ============================================================
// TypeScript rendering
// ============================================================

/// Render a schema JSON value as a TypeScript type expression.
///
/// `ns` is the prefix applied to referenced schema names (e.g. `"Schemas."`
/// in per-module files, `""` inside schemas.ts itself).
pub fn ts_type_of(schema: &Json, ns: &str) -> String {
    ts_type_inner(schema, ns, 0)
}

fn ts_type_inner(schema: &Json, ns: &str, depth: usize) -> String {
    if depth > MAX_DEPTH {
        return "any".to_string();
    }
    let obj = match schema {
        Json::Object(_) => schema,
        _ => return "any".to_string(),
    };

    let mut rendered = ts_type_core(obj, ns, depth);
    if is_nullable(obj) {
        // Avoid double parens on unions: `A | B | null` is fine.
        rendered = format!("{rendered} | null");
    }
    rendered
}

fn ts_type_core(schema: &Json, ns: &str, depth: usize) -> String {
    // References always render as the referenced name; never recurse into the
    // inlined body (cycle safety + nominal typing via schemas.ts).
    if let Some(path) = get_str(schema, "$ref") {
        return format!("{ns}{}", ref_name(path));
    }

    for key in ["oneOf", "anyOf"] {
        if let Some(members) = get(schema, key).and_then(|v| v.as_array()) {
            if members.is_empty() {
                return "any".to_string();
            }
            let parts = dedupe(
                members
                    .iter()
                    .map(|m| ts_union_member(m, ns, depth + 1))
                    .collect(),
            );
            return parts.join(" | ");
        }
    }

    if let Some(members) = get(schema, "allOf").and_then(|v| v.as_array()) {
        if members.is_empty() {
            return "any".to_string();
        }
        let parts = dedupe(
            members
                .iter()
                .map(|m| ts_union_member(m, ns, depth + 1))
                .collect(),
        );
        return parts.join(" & ");
    }

    match get_str(schema, "type") {
        Some("string") => match enum_literals(schema) {
            Some(lits) => lits.join(" | "),
            None => "string".to_string(),
        },
        Some("integer") | Some("number") => match enum_literals(schema) {
            Some(lits) => lits.join(" | "),
            None => "number".to_string(),
        },
        Some("boolean") => "boolean".to_string(),
        Some("array") => {
            let item = get(schema, "items")
                .map(|i| ts_type_inner(i, ns, depth + 1))
                .unwrap_or_else(|| "any".to_string());
            format!("Array<{item}>")
        }
        Some("object") | None => ts_object_type(schema, ns, depth),
        Some(_) => "any".to_string(),
    }
}

/// Union/intersection members that themselves contain unions need parens.
fn ts_union_member(schema: &Json, ns: &str, depth: usize) -> String {
    let rendered = ts_type_inner(schema, ns, depth);
    if rendered.contains(" | ") || rendered.contains(" & ") {
        format!("({rendered})")
    } else {
        rendered
    }
}

fn ts_object_type(schema: &Json, ns: &str, depth: usize) -> String {
    let props = get(schema, "properties").and_then(|p| p.as_object());
    let additional = get(schema, "additionalProperties");

    let inline = props.filter(|p| !p.is_empty()).map(|props| {
        let required: HashSet<&str> = get(schema, "required")
            .and_then(|r| r.as_array())
            .map(|arr| arr.iter().filter_map(|v| v.as_str()).collect())
            .unwrap_or_default();
        // Deterministic ordering for stable output.
        let sorted: BTreeMap<&String, &Json> = props.iter().collect();
        let fields: Vec<String> = sorted
            .iter()
            .map(|(key, prop)| {
                let opt = if required.contains(key.as_str()) {
                    ""
                } else {
                    "?"
                };
                let ty = ts_type_inner(prop, ns, depth + 1);
                format!("{}{}: {};", ts_key(&snake_to_camel(key)), opt, ty)
            })
            .collect();
        format!("{{ {} }}", fields.join(" "))
    });

    let map = additional.and_then(|ap| match ap {
        Json::Bool(true) => Some("Record<string, any>".to_string()),
        Json::Bool(false) => None,
        other => Some(format!(
            "Record<string, {}>",
            ts_type_inner(other, ns, depth + 1)
        )),
    });

    match (inline, map) {
        (Some(i), Some(m)) => format!("{i} & {m}"),
        (Some(i), None) => i,
        (None, Some(m)) => m,
        // Free-form object: the spec defines no member types.
        (None, None) => "Record<string, any>".to_string(),
    }
}

/// A rendered top-level schema declaration.
#[derive(Debug, serde::Serialize)]
pub struct SchemaDecl {
    pub name: String,
    pub code: String,
}

/// Build full TypeScript declarations for all component schemas
/// (the body of schemas.ts).
pub fn ts_schema_declarations(schemas: &[(String, Json)]) -> Vec<SchemaDecl> {
    let mut sorted: Vec<&(String, Json)> = schemas.iter().collect();
    sorted.sort_by(|a, b| a.0.cmp(&b.0));

    sorted
        .iter()
        .map(|(name, schema)| {
            let ident = sanitize_identifier(name);
            let description = get_str(schema, "description")
                .map(escape_doc)
                .unwrap_or_else(|| format!("Schema type for {name}"));
            let doc = format!("/**\n * {description}\n *\n * @public\n */");

            // Objects with properties render as interfaces (better docs,
            // declaration merging); everything else as type aliases.
            let is_plain_object = get_str(schema, "$ref").is_none()
                && get(schema, "oneOf").is_none()
                && get(schema, "anyOf").is_none()
                && get(schema, "allOf").is_none()
                && matches!(get_str(schema, "type"), Some("object") | None)
                && get(schema, "properties")
                    .and_then(|p| p.as_object())
                    .is_some_and(|p| !p.is_empty());

            let code = if is_plain_object {
                let body = ts_interface_body(schema);
                format!("{doc}\nexport interface {ident} {{\n{body}\n}}")
            } else {
                let ty = ts_type_of(schema, "");
                format!("{doc}\nexport type {ident} = {ty};")
            };
            SchemaDecl { name: ident, code }
        })
        .collect()
}

fn ts_interface_body(schema: &Json) -> String {
    let props = get(schema, "properties")
        .and_then(|p| p.as_object())
        .unwrap();
    let required: HashSet<&str> = get(schema, "required")
        .and_then(|r| r.as_array())
        .map(|arr| arr.iter().filter_map(|v| v.as_str()).collect())
        .unwrap_or_default();

    let sorted: BTreeMap<&String, &Json> = props.iter().collect();
    let mut lines = Vec::new();
    for (key, prop) in sorted {
        if let Some(desc) = get_str(prop, "description") {
            lines.push(format!("  /** {} */", escape_doc(desc)));
        }
        let opt = if required.contains(key.as_str()) {
            ""
        } else {
            "?"
        };
        let ty = ts_type_inner(prop, "", 1);
        lines.push(format!(
            "  {}{}: {};",
            ts_key(&snake_to_camel(key)),
            opt,
            ty
        ));
    }

    // additionalProperties alongside declared properties is intentionally not
    // emitted as an index signature: it would widen every member's type.
    // Unknown keys still arrive at runtime; they are just not declared.
    lines.join("\n")
}

// ============================================================
// Python rendering
// ============================================================

/// Render a schema JSON value as a Python type expression.
///
/// `ns` prefixes referenced schema names (e.g. `"schemas."` in per-tag
/// modules, `""` inside schemas.py where refs are emitted as quoted forward
/// references instead).
pub fn py_type_of(schema: &Json, ns: &str) -> String {
    py_type_inner(schema, ns, ns.is_empty(), 0)
}

/// Like `py_type_of`, but hoists inline object schemas into named Pydantic
/// models appended to `hoisted`. Used by the schemas.py builder.
fn py_type_hoisting(
    schema: &Json,
    ns: &str,
    quote_refs: bool,
    depth: usize,
    hoist_prefix: &str,
    hoisted: &mut Vec<(String, Json)>,
) -> String {
    if depth > MAX_DEPTH {
        return "Any".to_string();
    }
    let obj = match schema {
        Json::Object(_) => schema,
        _ => return "Any".to_string(),
    };

    // Inline object with properties: hoist into a named model. The name is
    // quoted (forward ref) only when the surrounding context requires it.
    if get_str(obj, "$ref").is_none()
        && matches!(get_str(obj, "type"), Some("object"))
        && get(obj, "properties")
            .and_then(|p| p.as_object())
            .is_some_and(|p| !p.is_empty())
    {
        let name = sanitize_identifier(hoist_prefix);
        hoisted.push((name.clone(), obj.clone()));
        let rendered = if quote_refs {
            format!("\"{name}\"")
        } else {
            name
        };
        return if is_nullable(obj) {
            format!("Optional[{rendered}]")
        } else {
            rendered
        };
    }

    // Compositions may contain inline objects too: hoist each variant.
    for key in ["oneOf", "anyOf"] {
        if get_str(obj, "$ref").is_none()
            && let Some(members) = get(obj, key).and_then(|v| v.as_array())
            && !members.is_empty()
        {
            let parts: Vec<String> = members
                .iter()
                .enumerate()
                .map(|(i, m)| {
                    py_type_hoisting(
                        m,
                        ns,
                        quote_refs,
                        depth + 1,
                        &format!("{hoist_prefix}Variant{}", i + 1),
                        hoisted,
                    )
                })
                .collect();
            let parts = dedupe(parts);
            let rendered = if parts.len() == 1 {
                parts.into_iter().next().unwrap()
            } else {
                format!("Union[{}]", parts.join(", "))
            };
            return if is_nullable(obj) {
                format!("Optional[{rendered}]")
            } else {
                rendered
            };
        }
    }

    // Arrays of inline objects: hoist the item type.
    if get_str(obj, "$ref").is_none() && matches!(get_str(obj, "type"), Some("array")) {
        let item = get(obj, "items")
            .map(|i| {
                py_type_hoisting(
                    i,
                    ns,
                    quote_refs,
                    depth + 1,
                    &format!("{hoist_prefix}Item"),
                    hoisted,
                )
            })
            .unwrap_or_else(|| "Any".to_string());
        let rendered = format!("List[{item}]");
        return if is_nullable(obj) {
            format!("Optional[{rendered}]")
        } else {
            rendered
        };
    }

    py_type_inner(obj, ns, quote_refs, depth)
}

fn py_type_inner(schema: &Json, ns: &str, quote_refs: bool, depth: usize) -> String {
    if depth > MAX_DEPTH {
        return "Any".to_string();
    }
    let obj = match schema {
        Json::Object(_) => schema,
        _ => return "Any".to_string(),
    };

    let core = py_type_core(obj, ns, quote_refs, depth);
    if is_nullable(obj) && !core.starts_with("Optional[") {
        format!("Optional[{core}]")
    } else {
        core
    }
}

fn py_type_core(schema: &Json, ns: &str, quote_refs: bool, depth: usize) -> String {
    if let Some(path) = get_str(schema, "$ref") {
        let name = py_ref_name(path);
        return if quote_refs {
            format!("\"{name}\"")
        } else {
            format!("{ns}{name}")
        };
    }

    for key in ["oneOf", "anyOf"] {
        if let Some(members) = get(schema, key).and_then(|v| v.as_array()) {
            if members.is_empty() {
                return "Any".to_string();
            }
            let parts = dedupe(
                members
                    .iter()
                    .map(|m| py_type_inner(m, ns, quote_refs, depth + 1))
                    .collect(),
            );
            return if parts.len() == 1 {
                parts.into_iter().next().unwrap()
            } else {
                format!("Union[{}]", parts.join(", "))
            };
        }
    }

    if let Some(members) = get(schema, "allOf").and_then(|v| v.as_array()) {
        // Python's typing has no intersections. A single-member allOf is that
        // member; otherwise prefer the first referenced model.
        if members.len() == 1 {
            return py_type_inner(&members[0], ns, quote_refs, depth + 1);
        }
        if let Some(first_ref) = members.iter().find(|m| get_str(m, "$ref").is_some()) {
            return py_type_inner(first_ref, ns, quote_refs, depth + 1);
        }
        return "Dict[str, Any]".to_string();
    }

    match get_str(schema, "type") {
        Some("string") => match enum_literals(schema) {
            Some(lits) => format!("Literal[{}]", lits.join(", ")),
            None => "str".to_string(),
        },
        Some("integer") => match enum_literals(schema) {
            Some(lits) => format!("Literal[{}]", lits.join(", ")),
            None => "int".to_string(),
        },
        Some("number") => "float".to_string(),
        Some("boolean") => "bool".to_string(),
        Some("array") => {
            let item = get(schema, "items")
                .map(|i| py_type_inner(i, ns, quote_refs, depth + 1))
                .unwrap_or_else(|| "Any".to_string());
            format!("List[{item}]")
        }
        Some("object") | None => {
            if let Some(ap) = get(schema, "additionalProperties") {
                match ap {
                    Json::Bool(false) | Json::Bool(true) => "Dict[str, Any]".to_string(),
                    other => format!(
                        "Dict[str, {}]",
                        py_type_inner(other, ns, quote_refs, depth + 1)
                    ),
                }
            } else {
                // Inline objects at type-expression position (parameters etc.)
                // cannot be classes; fall back to a mapping type.
                "Dict[str, Any]".to_string()
            }
        }
        Some(_) => "Any".to_string(),
    }
}

/// Render the field lines of a Pydantic model from an object schema.
/// Returns (field lines, hoisted inline-object schemas discovered).
fn py_model_fields(
    schema: &Json,
    class_name: &str,
    ns: &str,
    quote_refs: bool,
) -> (Vec<String>, Vec<(String, Json)>) {
    let mut hoisted = Vec::new();
    let props = match get(schema, "properties").and_then(|p| p.as_object()) {
        Some(p) if !p.is_empty() => p,
        _ => return (vec!["pass".to_string()], hoisted),
    };
    let required: HashSet<&str> = get(schema, "required")
        .and_then(|r| r.as_array())
        .map(|arr| arr.iter().filter_map(|v| v.as_str()).collect())
        .unwrap_or_default();

    let sorted: BTreeMap<&String, &Json> = props.iter().collect();
    let mut lines = Vec::new();
    // Required fields first (cosmetic; keyword-only in Pydantic anyway).
    for pass in [true, false] {
        for (key, prop) in &sorted {
            let is_required = required.contains(key.as_str());
            if is_required != pass {
                continue;
            }
            let field_name = py_field_ident(key);
            let hoist_prefix = format!("{class_name}{}", crate::pascal_case(key));
            let ty = py_type_hoisting(prop, ns, quote_refs, 1, &hoist_prefix, &mut hoisted);

            let mut field_args = Vec::new();
            if !is_required {
                field_args.push("default=None".to_string());
            }
            if field_name != **key {
                field_args.push(format!("alias=\"{}\"", escape_string(key)));
            }
            if let Some(desc) = get_str(prop, "description") {
                field_args.push(format!("description=\"{}\"", escape_string(desc)));
            }

            let annotation = if is_required {
                ty
            } else {
                format!("Optional[{ty}]")
            };
            let rhs = if field_args.is_empty() {
                if is_required {
                    String::new()
                } else {
                    " = None".to_string()
                }
            } else {
                format!(" = Field({})", field_args.join(", "))
            };
            lines.push(format!("    {field_name}: {annotation}{rhs}"));
        }
    }
    (lines, hoisted)
}

/// Kind of declaration a component schema produces in Python.
enum PyDeclKind {
    /// Pydantic BaseModel class (object with properties).
    Class(String),
    /// Plain type alias (primitives, arrays, unions, enums, maps).
    Alias(String),
}

/// Build the full body of schemas.py: Pydantic models for object schemas,
/// type aliases for everything else, in dependency-safe order.
pub fn py_schema_module(schemas: &[(String, Json)]) -> String {
    let mut sorted: Vec<&(String, Json)> = schemas.iter().collect();
    sorted.sort_by(|a, b| a.0.cmp(&b.0));

    let mut classes: Vec<(String, String)> = Vec::new(); // (name, code)
    let mut aliases: Vec<(String, String, HashSet<String>)> = Vec::new(); // (name, code, deps)
    let mut emitted: HashSet<String> = HashSet::new();

    let all_names: HashSet<String> = sorted.iter().map(|(n, _)| py_schema_ident(n)).collect();

    for (name, schema) in &sorted {
        let ident = py_schema_ident(name);
        if !emitted.insert(ident.clone()) {
            continue;
        }
        match py_declaration(&ident, name, schema) {
            PyDeclKind::Class(code) => classes.push((ident, code)),
            PyDeclKind::Alias(code) => {
                let deps = alias_deps(&code, &all_names, &ident);
                aliases.push((ident, code, deps));
            }
        }
    }

    // Topologically sort aliases among themselves (aliases can freely
    // reference classes, which are all emitted first).
    let alias_order = topo_sort_aliases(&aliases);

    let mut out = String::new();
    for (_, code) in &classes {
        out.push_str(code);
        out.push_str("\n\n");
    }
    for idx in alias_order {
        out.push_str(&aliases[idx].1);
        out.push_str("\n\n");
    }

    // Resolve every quoted forward reference eagerly so schema mismatches
    // fail at import time, not first validation.
    out.push_str(
        "for _model in list(globals().values()):\n    if (\n        isinstance(_model, type)\n        and _model is not BaseModel\n        and issubclass(_model, BaseModel)\n    ):\n        _model.model_rebuild()\n",
    );
    out
}

/// Names an alias's code depends on (very simple token scan).
fn alias_deps(code: &str, all_names: &HashSet<String>, self_name: &str) -> HashSet<String> {
    let mut deps = HashSet::new();
    let mut token = String::new();
    for c in code.chars().chain(std::iter::once(' ')) {
        if c.is_ascii_alphanumeric() || c == '_' {
            token.push(c);
        } else {
            if !token.is_empty() && token != self_name && all_names.contains(&token) {
                deps.insert(token.clone());
            }
            token.clear();
        }
    }
    deps
}

fn topo_sort_aliases(aliases: &[(String, String, HashSet<String>)]) -> Vec<usize> {
    let index: HashMap<&str, usize> = aliases
        .iter()
        .enumerate()
        .map(|(i, (n, _, _))| (n.as_str(), i))
        .collect();
    let mut order = Vec::with_capacity(aliases.len());
    let mut state = vec![0u8; aliases.len()]; // 0 = unvisited, 1 = visiting, 2 = done

    fn visit(
        i: usize,
        aliases: &[(String, String, HashSet<String>)],
        index: &HashMap<&str, usize>,
        state: &mut Vec<u8>,
        order: &mut Vec<usize>,
    ) {
        if state[i] != 0 {
            return; // done, or cycle (break arbitrarily)
        }
        state[i] = 1;
        for dep in &aliases[i].2 {
            if let Some(&j) = index.get(dep.as_str())
                && state[j] == 0
            {
                visit(j, aliases, index, state, order);
            }
        }
        state[i] = 2;
        order.push(i);
    }

    for i in 0..aliases.len() {
        visit(i, aliases, &index, &mut state, &mut order);
    }
    order
}

/// Collect all transitively hoisted inline-object models as (name, fields),
/// ordered children-before-parents so that unquoted references in a parent's
/// field annotations always point at an already-defined class.
fn collect_hoisted_classes(
    hoisted: Vec<(String, Json)>,
    ns: &str,
    quote_refs: bool,
) -> Vec<(String, Vec<String>)> {
    let mut queue = hoisted;
    let mut seen = HashSet::new();
    let mut discovered: Vec<(String, Vec<String>)> = Vec::new();
    let mut i = 0;
    while i < queue.len() {
        let (hname, hschema) = queue[i].clone();
        i += 1;
        if !seen.insert(hname.clone()) {
            continue;
        }
        let (hfields, children) = py_model_fields(&hschema, &hname, ns, quote_refs);
        queue.extend(children);
        discovered.push((hname, hfields));
    }
    // Children are always discovered after their parent; reversing puts them
    // first. Children never reference their parents, so this order is safe.
    discovered.reverse();
    discovered
}

fn py_declaration(ident: &str, original_name: &str, schema: &Json) -> PyDeclKind {
    let description = get_str(schema, "description").map(escape_py_doc);
    let is_object_model = get_str(schema, "$ref").is_none()
        && get(schema, "oneOf").is_none()
        && get(schema, "anyOf").is_none()
        && get(schema, "allOf").is_none()
        && matches!(get_str(schema, "type"), Some("object") | None)
        && get(schema, "properties")
            .and_then(|p| p.as_object())
            .is_some_and(|p| !p.is_empty());

    if is_object_model {
        let (fields, hoisted) = py_model_fields(schema, ident, "", true);
        let doc = description.unwrap_or_else(|| format!("Model for {original_name}"));
        let mut code = String::new();
        for (hname, hfields) in collect_hoisted_classes(hoisted, "", true) {
            code.push_str(&py_class_code(
                &hname,
                &format!("Nested model for {hname}"),
                &hfields,
            ));
            code.push_str("\n\n");
        }
        code.push_str(&py_class_code(ident, &doc, &fields));
        PyDeclKind::Class(code)
    } else {
        // Aliases hoist inline objects too (e.g. a oneOf of inline objects).
        // The hoisted classes are emitted immediately above the alias line so
        // the alias's unquoted references to them resolve; references to
        // *other* components stay unquoted too, so the whole declaration must
        // participate in the alias topo-sort (never the classes-first
        // section) or it can run before an alias it depends on.
        let mut hoisted = Vec::new();
        let ty = py_type_hoisting(schema, "", false, 0, ident, &mut hoisted);
        let mut code = String::new();
        for (hname, hfields) in collect_hoisted_classes(hoisted, "", true) {
            code.push_str(&py_class_code(
                &hname,
                &format!("Nested model for {hname}"),
                &hfields,
            ));
            code.push_str("\n\n");
        }
        if let Some(desc) = description {
            code.push_str(&format!("# {}\n", desc.replace('\n', " ")));
        }
        code.push_str(&format!("{ident} = {ty}"));
        PyDeclKind::Alias(code)
    }
}

fn py_class_code(name: &str, doc: &str, fields: &[String]) -> String {
    let mut code = format!("class {name}(BaseModel):\n    \"\"\"{doc}\"\"\"\n\n");
    for f in fields {
        code.push_str(f);
        code.push('\n');
    }
    code.push_str("\n    model_config = ConfigDict(populate_by_name=True, extra=\"allow\")");
    code
}

/// Render a full Pydantic class (plus any hoisted nested models) for an
/// inline (non-`$ref`) object schema, used by per-tag models.py for the rare
/// operation whose request/response body is defined inline.
pub fn py_inline_model(schema: &Json, class_name: &str, doc: &str) -> String {
    let (fields, hoisted) = py_model_fields(schema, class_name, "schemas.", false);
    let mut code = String::new();
    // Children-first: field annotations reference hoisted classes unquoted
    // (per-tag models have no rebuild epilogue), so every referenced class
    // must already be defined when its parent's class body is evaluated.
    for (hname, hfields) in collect_hoisted_classes(hoisted, "schemas.", false) {
        code.push_str(&py_class_code(
            &hname,
            &format!("Nested model for {hname}"),
            &hfields,
        ));
        code.push_str("\n\n");
    }
    code.push_str(&py_class_code(class_name, doc, &fields));
    code
}

// ============================================================
// Example value generation (for spec-valid test mocks)
// ============================================================

/// Build a minimal *valid* JSON instance of a schema: required object fields
/// only, first enum value, type-appropriate placeholders. Serialized schemas
/// carry resolved `$ref` bodies inline, so no resolution context is needed;
/// depth is capped for cycle safety.
pub fn example_json(schema: &Json) -> Json {
    example_inner(schema, 0)
}

fn example_inner(schema: &Json, depth: usize) -> Json {
    if depth > 8 || !schema.is_object() {
        return Json::Object(serde_json::Map::new());
    }

    // Compositions: use the first member (any valid variant satisfies
    // oneOf/anyOf consumers); for allOf, merge all object members.
    for key in ["oneOf", "anyOf"] {
        if let Some(members) = get(schema, key).and_then(|v| v.as_array())
            && let Some(first) = members.first()
        {
            return example_inner(first, depth + 1);
        }
    }
    if let Some(members) = get(schema, "allOf").and_then(|v| v.as_array()) {
        let mut merged = serde_json::Map::new();
        for member in members {
            if let Json::Object(obj) = example_inner(member, depth + 1) {
                merged.extend(obj);
            }
        }
        return Json::Object(merged);
    }

    if let Some(values) = get(schema, "enum").and_then(|v| v.as_array())
        && let Some(first) = values.first()
    {
        return first.clone();
    }

    match get_str(schema, "type") {
        Some("string") => match get_str(schema, "format") {
            Some("date-time") => Json::String("2021-01-01T00:00:00.000Z".to_string()),
            Some("date") => Json::String("2021-01-01".to_string()),
            _ => Json::String("test_value".to_string()),
        },
        Some("integer") => {
            // Respect minimum so validation-constrained fields stay valid.
            let min = get(schema, "minimum").and_then(|v| v.as_i64()).unwrap_or(1);
            Json::Number(serde_json::Number::from(min.max(1)))
        }
        Some("number") => Json::Number(serde_json::Number::from_f64(1.0).unwrap()),
        Some("boolean") => Json::Bool(true),
        Some("array") => {
            let item = get(schema, "items")
                .map(|i| example_inner(i, depth + 1))
                .unwrap_or_else(|| Json::Object(serde_json::Map::new()));
            Json::Array(vec![item])
        }
        Some("object") | None => {
            let mut obj = serde_json::Map::new();
            if let (Some(props), Some(required)) = (
                get(schema, "properties").and_then(|p| p.as_object()),
                get(schema, "required").and_then(|r| r.as_array()),
            ) {
                // Deterministic order.
                let mut names: Vec<&str> = required.iter().filter_map(|v| v.as_str()).collect();
                names.sort_unstable();
                for name in names {
                    if let Some(prop) = props.get(name) {
                        obj.insert(name.to_string(), example_inner(prop, depth + 1));
                    }
                }
            }
            Json::Object(obj)
        }
        Some(_) => Json::Object(serde_json::Map::new()),
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use serde_json::json;

    #[test]
    fn ts_ref() {
        assert_eq!(
            ts_type_of(&json!({"$ref": "#/components/schemas/User"}), "Schemas."),
            "Schemas.User"
        );
    }

    #[test]
    fn ts_string_enum() {
        let s = json!({"type": "string", "enum": ["a", "b"]});
        assert_eq!(ts_type_of(&s, ""), "\"a\" | \"b\"");
    }

    #[test]
    fn ts_array_of_ref_items() {
        let s = json!({"type": "array", "items": {"$ref": "#/components/schemas/Tweet"}});
        assert_eq!(ts_type_of(&s, "Schemas."), "Array<Schemas.Tweet>");
    }

    #[test]
    fn ts_one_of_union() {
        let s = json!({"oneOf": [{"$ref": "#/x/A"}, {"type": "string"}]});
        assert_eq!(ts_type_of(&s, ""), "A | string");
    }

    #[test]
    fn ts_nullable() {
        let s = json!({"type": "string", "nullable": true});
        assert_eq!(ts_type_of(&s, ""), "string | null");
    }

    #[test]
    fn ts_inline_object() {
        let s = json!({"type": "object", "properties": {"user_id": {"type": "string"}}, "required": ["user_id"]});
        assert_eq!(ts_type_of(&s, ""), "{ userId: string; }");
    }

    #[test]
    fn ts_additional_props() {
        let s = json!({"type": "object", "additionalProperties": {"type": "integer"}});
        assert_eq!(ts_type_of(&s, ""), "Record<string, number>");
    }

    #[test]
    fn py_ref_quoted_vs_ns() {
        let s = json!({"$ref": "#/components/schemas/User"});
        assert_eq!(py_type_of(&s, ""), "\"User\"");
        assert_eq!(py_type_of(&s, "schemas."), "schemas.User");
    }

    #[test]
    fn py_literal_enum() {
        let s = json!({"type": "string", "enum": ["asc", "desc"]});
        assert_eq!(py_type_of(&s, ""), "Literal[\"asc\", \"desc\"]");
    }

    #[test]
    fn py_array_and_nullable() {
        let s = json!({"type": "array", "items": {"type": "integer"}, "nullable": true});
        assert_eq!(py_type_of(&s, ""), "Optional[List[int]]");
    }

    #[test]
    fn py_union() {
        let s = json!({"anyOf": [{"$ref": "#/c/s/A"}, {"$ref": "#/c/s/B"}]});
        assert_eq!(py_type_of(&s, "schemas."), "Union[schemas.A, schemas.B]");
    }

    #[test]
    fn snake_to_camel_matches_runtime() {
        assert_eq!(snake_to_camel("created_at"), "createdAt");
        assert_eq!(
            snake_to_camel("edit_history_tweet_ids"),
            "editHistoryTweetIds"
        );
        assert_eq!(snake_to_camel("_internal"), "Internal");
        assert_eq!(snake_to_camel("tweet.fields"), "tweet.fields");
    }

    #[test]
    fn py_alias_with_hoisted_variant_orders_after_deps() {
        // A union alias with an inline variant must stay in the topo-sorted
        // alias section: its unquoted ref to UserId requires UserId first.
        let schemas = vec![
            (
                "Foo".to_string(),
                json!({"oneOf": [
                    {"type": "object", "properties": {"a": {"type": "string"}}},
                    {"$ref": "#/components/schemas/UserId"}
                ]}),
            ),
            ("UserId".to_string(), json!({"type": "string"})),
        ];
        let module = py_schema_module(&schemas);
        let userid_pos = module.find("UserId = str").unwrap();
        let foo_pos = module.find("Foo = Union[").unwrap();
        assert!(
            userid_pos < foo_pos,
            "UserId must be defined before the alias that references it:\n{module}"
        );
        // The hoisted variant class must precede the alias line too.
        let variant_pos = module.find("class FooVariant1(BaseModel):").unwrap();
        assert!(variant_pos < foo_pos);
    }

    #[test]
    fn py_inline_model_emits_children_first() {
        let schema = json!({
            "type": "object",
            "properties": {
                "a": {"type": "object", "properties": {
                    "b": {"type": "object", "properties": {"x": {"type": "string"}}}
                }}
            }
        });
        let code = py_inline_model(&schema, "Foo", "doc");
        let child = code.find("class FooAB(BaseModel):").unwrap();
        let parent = code.find("class FooA(BaseModel):").unwrap();
        let main = code.find("class Foo(BaseModel):").unwrap();
        assert!(
            child < parent && parent < main,
            "hoisted classes must be emitted children-first:\n{code}"
        );
    }

    #[test]
    fn py_keyword_field_gets_suffix_and_alias() {
        let schema = json!({"type": "object", "properties": {"from": {"type": "string"}}});
        let code = py_inline_model(&schema, "Foo", "doc");
        assert!(code.contains("from_: Optional[str]"), "{code}");
        assert!(code.contains("alias=\"from\""), "{code}");
    }

    #[test]
    fn boolean_enum_members_fall_back_to_base_type() {
        let s = json!({"type": "string", "enum": [true, false]});
        assert_eq!(ts_type_of(&s, ""), "string");
        assert_eq!(py_type_of(&s, "schemas."), "str");
    }

    #[test]
    fn py_schema_module_smoke() {
        let schemas = vec![
            (
                "UserId".to_string(),
                json!({"type": "string", "description": "unique id"}),
            ),
            (
                "User".to_string(),
                json!({"type": "object", "properties": {"id": {"$ref": "#/components/schemas/UserId"}, "name": {"type": "string"}}, "required": ["id"]}),
            ),
            (
                "UserIds".to_string(),
                json!({"type": "array", "items": {"$ref": "#/components/schemas/UserId"}}),
            ),
        ];
        let module = py_schema_module(&schemas);
        assert!(module.contains("class User(BaseModel):"));
        assert!(module.contains("id: \"UserId\""));
        assert!(module.contains("UserId = str"));
        assert!(module.contains("UserIds = List[UserId]"));
        // Alias ordering: UserId must be defined before UserIds uses it.
        assert!(module.find("UserId = str").unwrap() < module.find("UserIds = List").unwrap());
    }
}
