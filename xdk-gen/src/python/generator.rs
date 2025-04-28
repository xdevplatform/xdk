/// Python SDK Generator Implementation
///
/// This file demonstrates how to implement a language-specific generator using the `language!` macro.
/// It defines filters for Python-specific formatting and implements the generator.
///
/// When creating a generator for a new language, follow this pattern:
/// 1. Define language-specific filters (e.g., type conversion, naming conventions)
/// 2. Use the language! macro to create the generator struct
/// 3. Implement the rendering logic in the generate field
use crate::language;

/// MiniJinja filter for converting a string to snake_case
fn snake_case(value: &str) -> String {
    let chars = value.chars();
    let mut result = String::new();
    let mut prev_is_underscore = false;

    for c in chars {
        if c.is_uppercase() {
            if !result.is_empty() && !prev_is_underscore {
                result.push('_');
            }
            result.push(c.to_ascii_lowercase());
            prev_is_underscore = false;
        } else if c.is_alphanumeric() {
            result.push(c.to_ascii_lowercase());
            prev_is_underscore = false;
        } else if !prev_is_underscore {
            result.push('_');
            prev_is_underscore = true;
        }
    }

    result.trim_matches('_').to_string()
}

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

/*
    This is the main generator for the Python SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: Python,
    filters: [snake_case, python_type],
    render: [
        multiple {
            render ("models") to ("xdk/{}/models.py"),
            render ("client_module") to ("xdk/{}/__init__.py"),
            render ("client_class") to ("xdk/{}/client.py")
        },
        render ("main_client") to ("xdk/client.py"),
        render ("init_py") to ("xdk/__init__.py"),
        render ("setup_py") to ("setup.py"),
        render ("readme") to ("README.md"),
        render ("requirements_txt") to ("requirements.txt")
    ]
}
