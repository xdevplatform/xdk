use serde::Serialize;
/// Python SDK Generator Implementation
///
/// This file implements the Python generator using the `language!` macro,
/// plus a wrapper that renders schemas.py (Pydantic models for all OpenAPI
/// component schemas) so generated code can be fully typed.
use xdk_lib::{Casing, language, pascal_case};

/// MiniJinja filter rendering a full serialized OpenAPI schema as a Python
/// type expression (enums as Literal, arrays with item types, oneOf/anyOf as
/// Union, `$ref`s as schema model names prefixed with `ns`).
fn py_type(
    value: minijinja::Value,
    ns: Option<String>,
) -> std::result::Result<String, minijinja::Error> {
    let json: serde_json::Value = serde_json::to_value(&value).map_err(|e| {
        minijinja::Error::new(minijinja::ErrorKind::InvalidOperation, e.to_string())
    })?;
    Ok(xdk_lib::types::py_type_of(
        &json,
        ns.as_deref().unwrap_or("schemas."),
    ))
}

/// MiniJinja filter rendering an inline object schema as a full Pydantic
/// model class (plus hoisted nested models), for the rare operation whose
/// request/response body is not a component reference.
fn py_inline_model(
    value: minijinja::Value,
    class_name: String,
    doc: String,
) -> std::result::Result<String, minijinja::Error> {
    let json: serde_json::Value = serde_json::to_value(&value).map_err(|e| {
        minijinja::Error::new(minijinja::ErrorKind::InvalidOperation, e.to_string())
    })?;
    Ok(xdk_lib::types::py_inline_model(&json, &class_name, &doc))
}

/// MiniJinja filter mapping a `$ref` path to the Python-safe schema model
/// name (e.g. "#/components/schemas/List" -> "XList").
fn py_ref(value: &str) -> String {
    xdk_lib::types::py_schema_ident(value.rsplit('/').next().unwrap_or(value))
}

/// MiniJinja filter for getting the last part of a path (splits by both '/' and '.')
fn last_part(value: &str) -> String {
    // First try splitting by '/' (for $ref paths like "#/components/schemas/User")
    // Then by '.' (for other dot-separated paths)
    value
        .split('/')
        .next_back()
        .unwrap_or(value)
        .split('.')
        .next_back()
        .unwrap_or(value)
        .to_string()
}

/// Context for rendering the schemas.py template: the module body is fully
/// rendered in Rust (see xdk_lib::types::py_schema_module).
#[derive(Debug, Serialize)]
struct PySchemasContext {
    body: String,
}

/*
    This is the main generator for the Python SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: PythonBase,
    filters: [pascal_case, py_type, py_inline_model, py_ref, last_part],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Snake,
    import_casing: Casing::Snake,
    variable_casing: Casing::Snake,
    render: [
        multiple {
            render "models" => "xdk/{}/models.py",
            render "client_module" => "xdk/{}/__init__.py",
            render "client_class" => "xdk/{}/client.py"
        },
        render "main_client" => "xdk/client.py",
        render "oauth2_auth" => "xdk/oauth2_auth.py",
        render "oauth1_auth" => "xdk/oauth1_auth.py",
        render "paginator" => "xdk/paginator.py",
        render "streaming" => "xdk/streaming.py",
        render "init_py" => "xdk/__init__.py",
        render "pyproject_toml" => "pyproject.toml",
        render "sphinx_conf" => "conf.py",
        render "generate_docs_simple" => "scripts/generate-docs-simple.py",
        render "process_for_mintlify" => "scripts/process-for-mintlify.py",
        render "watch_docs" => "scripts/watch-docs.py",
        render "readme" => "README.md",
        render "gitignore" => ".gitignore"
    ],
    tests: [
        multiple {
            render "test_contracts" => "tests/{}/test_contracts.py",
            render "test_generic" => "tests/{}/test_generic.py",
            render "test_structure" => "tests/{}/test_structure.py",
            render "test_pagination" => "tests/{}/test_pagination.py"
        },
        render "conftest" => "tests/conftest.py"
    ]
}

/// Python generator with schema module generation
pub struct Python;

impl xdk_lib::generator::LanguageGenerator for Python {
    fn name(&self) -> String {
        "python".to_string()
    }

    fn add_filters(&self, env: &mut minijinja::Environment) {
        PythonBase.add_filters(env);
    }

    fn generate(
        &self,
        env: &minijinja::Environment,
        operations: &std::collections::HashMap<Vec<String>, Vec<xdk_lib::models::OperationGroup>>,
        output_dir: &std::path::Path,
        version: &str,
    ) -> xdk_lib::Result<()> {
        // First, generate all standard templates using the base generator
        PythonBase.generate(env, operations, output_dir, version)?;

        // Then generate xdk/schemas.py from OpenAPI components. Schemas are
        // serialized while the OpenAPI context guard is alive so `$ref`s
        // carry both the reference path and the resolved body.
        let raw_schemas: Vec<(String, serde_json::Value)> =
            xdk_openapi::OpenApiContextGuard::with_context(|ctx| {
                ctx.get_schemas()
                    .into_iter()
                    .filter_map(|(name, schema)| {
                        serde_json::to_value(&schema).ok().map(|json| (name, json))
                    })
                    .collect()
            })
            .unwrap_or_default();

        // Always write schemas.py: the generated package imports it
        // unconditionally, so a spec without component schemas must still
        // produce an (empty) module.
        let context = PySchemasContext {
            body: xdk_lib::types::py_schema_module(&raw_schemas),
        };
        let schemas_path = output_dir.join("xdk/schemas.py");
        let content = xdk_lib::templates::render_template_with_path(
            env,
            "schemas",
            &context,
            schemas_path.to_str().unwrap_or("xdk/schemas.py"),
        )?;
        std::fs::write(&schemas_path, content)?;

        Ok(())
    }
}
