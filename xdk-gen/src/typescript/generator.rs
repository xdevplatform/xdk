/// TypeScript SDK Generator Implementation
///
/// This file implements the TypeScript generator using the `language!` macro.
/// It defines filters for TypeScript-specific formatting and implements the generator.
use xdk_lib::{Casing, language, pascal_case, camel_case};

/// Helper function for snake_case conversion (for use as a filter)
fn snake_case(value: &str) -> String {
    Casing::Snake.convert_string(value)
}

/// MiniJinja filter for converting to TypeScript types
fn typescript_type(value: &str) -> String {
    let ts_type = match value {
        "string" => "string",
        "integer" => "number",
        "number" => "number",
        "boolean" => "boolean",
        "array" => "Array<any>",
        "object" => "Record<string, any>",
        _ => "any",
    };
    ts_type.to_string()
}

/// MiniJinja filter for getting the last part of a dot-separated path
fn last_part(value: &str) -> String {
    value.split('.').last().unwrap_or(value).to_string()
}

/// MiniJinja filter for extracting schema name from a reference path
/// e.g., "#/components/schemas/User" -> "User"
fn schema_name_from_ref(path: &str) -> String {
    if path.starts_with("#/components/schemas/") {
        path.trim_start_matches("#/components/schemas/").to_string()
    } else {
        // Fallback: try to get last part after /
        path.split('/').last().unwrap_or(path).to_string()
    }
}

/// Extract schema name from a reference path
/// e.g., "#/components/schemas/User" -> "User"
fn extract_schema_name_from_ref(path: &str) -> Option<String> {
    if path.starts_with("#/components/schemas/") {
        Some(path.trim_start_matches("#/components/schemas/").to_string())
    } else {
        None
    }
}

/*
    This is the main generator for the TypeScript SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: TypeScript,
    filters: [camel_case, pascal_case, snake_case, typescript_type, last_part, schema_name_from_ref],
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
        render "generate_docs" => "scripts/generate-docs.js",
        render "readme" => "README.md"
    ],
    tests: [
        multiple {},
    ]
} 