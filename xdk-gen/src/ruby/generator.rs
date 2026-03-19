/// Ruby SDK Generator Implementation
///
/// This file implements the Ruby generator using the `language!` macro.
/// It defines filters for Ruby-specific formatting and implements the generator.
use xdk_lib::{Casing, language, pascal_case};

/// MiniJinja filter for converting OpenAPI types to Ruby types
fn ruby_type(value: &str) -> String {
    let ruby_type = match value {
        "string" => "String",
        "integer" => "Integer",
        "number" => "Float",
        "boolean" => "Boolean",
        "array" => "Array",
        "object" => "Hash",
        _ => "Object",
    };
    ruby_type.to_string()
}

/// MiniJinja filter for getting the last part of a path (splits by both '/' and '.')
fn last_part(value: &str) -> String {
    value
        .split('/')
        .next_back()
        .unwrap_or(value)
        .split('.')
        .next_back()
        .unwrap_or(value)
        .to_string()
}

/// Helper function for snake_case conversion (for use as a filter)
fn snake_case(value: &str) -> String {
    Casing::Snake.convert_string(value)
}

/*
    This is the main generator for the Ruby SDK
    It declares the templates and filters used as well as the rendering logic
*/
language! {
    name: Ruby,
    filters: [pascal_case, snake_case, ruby_type, last_part],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Snake,
    import_casing: Casing::Snake,
    variable_casing: Casing::Snake,
    render: [
        multiple {
            render "models" => "lib/xdk/{}/models.rb",
            render "client_class" => "lib/xdk/{}/client.rb"
        },
        render "main_client" => "lib/xdk/client.rb",
        render "version" => "lib/xdk/version.rb",
        render "lib_entry" => "lib/xdk.rb",
        render "gemspec" => "xdk.gemspec",
        render "gemfile" => "Gemfile",
        render "readme" => "README.md",
        render "gitignore" => ".gitignore"
    ],
    tests: [
        multiple {
            render "test_contracts" => "spec/{}/contracts_spec.rb",
            render "test_structure" => "spec/{}/structure_spec.rb"
        },
        render "spec_helper" => "spec/spec_helper.rb"
    ]
}
