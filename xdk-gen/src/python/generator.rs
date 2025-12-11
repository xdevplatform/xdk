/// Python SDK Generator Implementation
///
/// This file demonstrates how to implement a language-specific generator using the `language!` macro.
/// It defines filters for Python-specific formatting and implements the generator.
///
/// When creating a generator for a new language, follow this pattern:
/// 1. Define language-specific filters (e.g., type conversion, naming conventions)
/// 2. Use the language! macro to create the generator struct
/// 3. Implement the rendering logic in the generate field
use xdk_lib::{Casing, language, pascal_case};

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
/*
    This is the main generator for the Python SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: Python,
    filters: [pascal_case, python_type, last_part],
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
