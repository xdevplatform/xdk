/// TypeScript SDK Generator Implementation
///
/// This file demonstrates how to implement a language-specific generator using the `language!` macro.
/// It defines filters for TypeScript-specific formatting and implements the generator.
///
/// When creating a generator for a new language, follow this pattern:
/// 1. Define language-specific filters (e.g., type conversion, naming conventions)
/// 2. Use the language! macro to create the generator struct
/// 3. Implement the rendering logic in the generate field
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
    filters: [camel_case, pascal_case, snake_case, typescript_type, last_part],
    render: [
        multiple {
            render "models" => "src/{}/models.ts",
            render "client_module" => "src/{}/index.ts",
            render "client_class" => "src/{}/client.ts"
        },
        render "main_client" => "src/client.ts",
        render "oauth2_auth" => "src/oauth2_auth.ts",
        render "paginator" => "src/paginator.ts",
        render "index" => "src/index.ts",
        render "package_json" => "package.json",
        render "tsconfig" => "tsconfig.json",
        render "tsup.config" => "tsup.config.ts",
        render "readme" => "README.md"
    ]
} 