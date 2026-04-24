use xdk_lib::{Casing, language, pascal_case};

fn snake_case(value: &str) -> String {
    Casing::Snake.convert_string(value)
}

fn elixir_type(value: &str) -> String {
    match value {
        "string" => "String.t()",
        "integer" => "integer()",
        "number" => "float()",
        "boolean" => "boolean()",
        "array" => "list()",
        "object" => "map()",
        _ => "String.t()",
    }
    .to_string()
}

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

fn schema_name_from_ref(path: &str) -> String {
    if path.starts_with("#/components/schemas/") {
        path.trim_start_matches("#/components/schemas/").to_string()
    } else {
        path.split('/').next_back().unwrap_or(path).to_string()
    }
}

language! {
    name: Elixir,
    filters: [pascal_case, snake_case, elixir_type, last_part, schema_name_from_ref],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Snake,
    import_casing: Casing::Snake,
    variable_casing: Casing::Snake,
    render: [
        multiple {
            render "client_class" => "lib/xdk/{}.ex"
        },
        render "main_client" => "lib/xdk.ex",
        render "errors" => "lib/xdk/errors.ex",
        render "query" => "lib/xdk/query.ex",
        render "streaming" => "lib/xdk/streaming.ex",
        render "paginator" => "lib/xdk/paginator.ex",
        render "mix_exs" => "mix.exs",
        render "readme" => "README.md",
        render "gitignore" => ".gitignore",
        render "formatter" => ".formatter.exs"
    ],
    tests: [
        multiple {
            render "test_structure" => "test/xdk/{}_test.exs"
        },
        render "test_helper" => "test/test_helper.exs"
    ]
}
