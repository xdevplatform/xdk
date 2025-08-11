/// TypeScript SDK Generator Implementation
///
/// This file implements the TypeScript generator using the `language!` macro.
/// It defines filters for TypeScript-specific formatting and implements the generator.
use crate::common::casing::{pascal_case, camel_case, snake_case};
use xdk_lib::language;

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

/// MiniJinja filter for getting the TypeScript type from a parameter schema
fn parameter_typescript_type(schema_json: &str) -> String {
    // Parse the JSON string to extract type information
    if let Ok(schema) = serde_json::from_str::<serde_json::Value>(schema_json) {
        if let Some(schema_obj) = schema.as_object() {
            if let Some(type_value) = schema_obj.get("type") {
                if let Some(type_str) = type_value.as_str() {
                    return typescript_type(type_str);
                }
            }
            // Check for $ref
            if let Some(ref_value) = schema_obj.get("$ref") {
                if let Some(ref_str) = ref_value.as_str() {
                    // Extract type from reference name
                    if ref_str.contains("TweetId") || ref_str.contains("UserId") || ref_str.contains("ListId") {
                        return "string".to_string();
                    }
                }
            }
        }
    }
    "any".to_string()
}

/// MiniJinja filter for getting the last part of a dot-separated path
fn last_part(value: &str) -> String {
    value.split('.').last().unwrap_or(value).to_string()
}

/*
    This is the main generator for the TypeScript SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: TypeScript,
    filters: [camel_case, pascal_case, snake_case, typescript_type, parameter_typescript_type, last_part],
    render: [
        multiple {
            render "models" => "src/{}/models.ts",
            render "client_module" => "src/{}/index.ts",
            render "client_class" => "src/{}/client.ts"
        },
        render "main_client" => "src/client.ts",
        render "http_client" => "src/http-client.ts",
        render "oauth2_auth" => "src/oauth2_auth.ts",
        render "paginator" => "src/paginator.ts",
        render "index" => "src/index.ts",
        render "package_json" => "package.json",
        render "tsconfig" => "tsconfig.json",
        render "tsup.config" => "tsup.config.ts",
        render "readme" => "README.md"
    ]
} 