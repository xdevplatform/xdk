/// Python SDK Generator Implementation
///
/// This file demonstrates how to implement a language-specific generator using the `language!` macro.
/// It defines filters for Python-specific formatting and implements the generator.
///
/// When creating a generator for a new language, follow this pattern:
/// 1. Define language-specific filters (e.g., type conversion, naming conventions)
/// 2. Use the language! macro to create the generator struct
/// 3. Implement the rendering logic in the generate field
use crate::common::casing::{pascal_case, snake_case};
use xdk_lib::language;

/// MiniJinja filter for converting to Python types
fn python_type(value: &str) -> String {
    let python_type = match value {
        "string" => "str",
        "integer" => "int",
        "number" => "float",
        "boolean" => "bool",
        "array" => "List",
        "object" => "Dict[str, Any]",
        _ => "Any",
    };
    python_type.to_string()
}

/// MiniJinja filter for getting the last part of a dot-separated path
fn last_part(value: &str) -> String {
    value.split('.').last().unwrap_or(value).to_string()
}
/*
    This is the main generator for the Python SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: Python,
    filters: [snake_case, pascal_case, python_type, last_part],
    render: [
        multiple {
            render "models" => "xdk/{}/models.py",
            render "client_module" => "xdk/{}/__init__.py",
            render "client_class" => "xdk/{}/client.py"
        },
        render "main_client" => "xdk/client.py",
        render "oauth2_auth" => "xdk/oauth2_auth.py",
        render "paginator" => "xdk/paginator.py",
        render "init_py" => "xdk/__init__.py",
        render "pyproject_toml" => "pyproject.toml",
        render "readme" => "README.md"
    ]
}
