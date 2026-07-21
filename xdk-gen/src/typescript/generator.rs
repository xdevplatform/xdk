use serde::Serialize;
/// TypeScript SDK Generator Implementation
///
/// This file implements the TypeScript generator using the `language!` macro.
/// It defines filters for TypeScript-specific formatting and implements the generator.
use xdk_lib::{Casing, camel_case, language, pascal_case};

/// Helper function for snake_case conversion (for use as a filter)
fn snake_case(value: &str) -> String {
    Casing::Snake.convert_string(value)
}

/// MiniJinja filter rendering a full serialized OpenAPI schema as a
/// TypeScript type expression (enums as literal unions, arrays with item
/// types, oneOf/anyOf as unions, allOf as intersections, `$ref`s as schema
/// type names prefixed with `ns`).
fn ts_type(
    value: minijinja::Value,
    ns: Option<String>,
) -> std::result::Result<String, minijinja::Error> {
    let json: serde_json::Value = serde_json::to_value(&value).map_err(|e| {
        minijinja::Error::new(minijinja::ErrorKind::InvalidOperation, e.to_string())
    })?;
    Ok(xdk_lib::types::ts_type_of(
        &json,
        ns.as_deref().unwrap_or(""),
    ))
}

/// MiniJinja filter for getting the last part of a dot-separated path
fn last_part(value: &str) -> String {
    value.split('.').next_back().unwrap_or(value).to_string()
}

/// Context for rendering schemas template: declarations are fully rendered
/// in Rust (see xdk_lib::types); the template only concatenates them.
#[derive(Debug, Serialize)]
struct SchemasContext {
    schemas: Vec<xdk_lib::types::SchemaDecl>,
}

/*
    This is the main generator for the TypeScript SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: TypeScriptBase,
    filters: [camel_case, pascal_case, snake_case, ts_type, last_part],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Camel,
    import_casing: Casing::Snake,
    variable_casing: Casing::Camel,
    render: [
        multiple {
            render "models" => "src/{}/models.ts",
            render "client_module" => "src/{}/index.ts",
            render "client_class" => "src/{}/client.ts",
            render "stream_client" => "src/{}/stream_client.ts",
            render "event_driven_stream" => "src/{}/event_driven_stream.ts"
        },
        render "main_client" => "src/client.ts",
        render "http_client" => "src/http-client.ts",
        render "oauth2_auth" => "src/oauth2_auth.ts",
                render "oauth1_auth" => "src/oauth1_auth.ts",
                render "crypto_utils" => "src/crypto_utils.ts",
                render "stream_listener" => "src/stream_listener.ts",
                render "paginator" => "src/paginator.ts",
        render "index" => "src/index.ts",
        render "package_json" => "package.json",
        render "tsconfig" => "tsconfig.json",
        render "tsup.config" => "tsup.config.ts",
        render "typedoc.json" => "typedoc.json",
        render "npmignore" => ".npmignore",
        render "gitignore" => ".gitignore",
        render "generate_docs" => "scripts/generate-docs.js",
        render "generate_docs_simple" => "scripts/generate-docs-simple.js",
        render "watch_docs" => "scripts/watch-docs.js",
        render "process_for_mintlify" => "scripts/process-for-mintlify.js",
        render "readme" => "README.md"
    ],
    tests: [
        multiple {
            render "test_structure" => "tests/{}/test_structure.test.ts",
            render "test_generic" => "tests/{}/test_generic.test.ts",
            render "test_contracts" => "tests/{}/test_contracts.test.ts",
            render "test_pagination" => "tests/{}/test_pagination.test.ts"
        },
        render "jest.config" => "jest.config.cjs"
    ]
}

/// TypeScript generator with custom schema generation
pub struct TypeScript;

impl xdk_lib::generator::LanguageGenerator for TypeScript {
    fn name(&self) -> String {
        "typescript".to_string()
    }

    fn add_filters(&self, env: &mut minijinja::Environment) {
        TypeScriptBase.add_filters(env);
    }

    fn generate(
        &self,
        env: &minijinja::Environment,
        operations: &std::collections::HashMap<Vec<String>, Vec<xdk_lib::models::OperationGroup>>,
        output_dir: &std::path::Path,
        version: &str,
    ) -> xdk_lib::Result<()> {
        // First, generate all standard templates using the base generator
        TypeScriptBase.generate(env, operations, output_dir, version)?;

        // Then generate schemas.ts from OpenAPI components. Schemas are
        // serialized while the OpenAPI context guard is alive so `$ref`s
        // carry both the reference path and the resolved body, then rendered
        // into full TypeScript declarations in Rust.
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
        let schemas = xdk_lib::types::ts_schema_declarations(&raw_schemas);

        if !schemas.is_empty() {
            let context = SchemasContext { schemas };
            let schemas_path = output_dir.join("src/schemas.ts");
            let content = xdk_lib::templates::render_template_with_path(
                env,
                "schemas",
                &context,
                schemas_path.to_str().unwrap_or("src/schemas.ts"),
            )?;
            std::fs::write(&schemas_path, content)?;
        }

        Ok(())
    }
}
