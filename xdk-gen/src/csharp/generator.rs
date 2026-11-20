use serde::Serialize;
use xdk_lib::{Casing, camel_case, language, pascal_case};

fn cs_type(
    value: minijinja::Value,
    nullable: Option<bool>,
) -> std::result::Result<String, minijinja::Error> {
    let json: serde_json::Value = serde_json::to_value(&value).map_err(|e| {
        minijinja::Error::new(minijinja::ErrorKind::InvalidOperation, e.to_string())
    })?;
    Ok(xdk_lib::types::csharp_type_of(
        &json,
        "",
        nullable.unwrap_or(false),
    ))
}

fn cs_var_ident(value: &str) -> String {
    xdk_lib::types::csharp_var_ident(value)
}

fn cs_prop_ident(value: &str, enclosing: Option<String>) -> String {
    xdk_lib::types::csharp_prop_ident(value, enclosing.as_deref().unwrap_or(""))
}

fn cs_class_ident(value: &str) -> String {
    xdk_lib::types::csharp_schema_ident(value)
}

fn cs_string_literal(value: &str) -> String {
    format!("\"{}\"", xdk_lib::types::escape_string(value))
}

fn path_prefix(value: &str) -> String {
    value.split('{').next().unwrap_or(value).to_string()
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

#[derive(Debug, Serialize)]
struct CSharpSchemasContext {
    schemas: Vec<xdk_lib::types::SchemaDecl>,
}

language! {
    name: CSharpBase,
    filters: [
        camel_case,
        pascal_case,
        cs_type,
        cs_var_ident,
        cs_prop_ident,
        cs_class_ident,
        cs_string_literal,
        path_prefix,
        last_part
    ],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Pascal,
    import_casing: Casing::Pascal,
    variable_casing: Casing::Camel,
    render: [
        multiple {
            render "client_class" => "src/Xdk/Clients/{class_name}Client.cs"
        },
        render "main_client" => "src/Xdk/XClient.cs",
        render "client_options" => "src/Xdk/XClientOptions.cs",
        render "api_exception" => "src/Xdk/XApiException.cs",
        render "oauth1_auth" => "src/Xdk/Auth/OAuth1.cs",
        render "oauth2_pkce" => "src/Xdk/Auth/OAuth2Pkce.cs",
        render "oauth2_token" => "src/Xdk/Auth/OAuth2Token.cs",
        render "paginator" => "src/Xdk/Paginator.cs",
        render "stream_options" => "src/Xdk/Streaming/StreamOptions.cs",
        render "event_stream" => "src/Xdk/Streaming/EventStream.cs",
        render "sdk_csproj" => "src/Xdk/Xdk.csproj",
        render "solution_sln" => "Xdk.sln",
        render "readme" => "README.md",
        render "gitignore" => ".gitignore"
    ],
    tests: [
        multiple {
            render "test_structure" => "tests/Xdk.Tests/{class_name}StructureTests.cs",
            render "test_contracts" => "tests/Xdk.Tests/{class_name}ContractsTests.cs",
            render "test_pagination" => "tests/Xdk.Tests/{class_name}PaginationTests.cs"
        },
        render "test_core" => "tests/Xdk.Tests/XClientCoreTests.cs",
        render "test_helpers" => "tests/Xdk.Tests/MockHttpMessageHandler.cs",
        render "test_csproj" => "tests/Xdk.Tests/Xdk.Tests.csproj"
    ]
}

pub struct CSharp;

impl xdk_lib::generator::LanguageGenerator for CSharp {
    fn name(&self) -> String {
        "csharp".to_string()
    }

    fn add_filters(&self, env: &mut minijinja::Environment) {
        CSharpBase.add_filters(env);
    }

    fn generate(
        &self,
        env: &minijinja::Environment,
        operations: &std::collections::HashMap<Vec<String>, Vec<xdk_lib::models::OperationGroup>>,
        output_dir: &std::path::Path,
        version: &str,
    ) -> xdk_lib::Result<()> {
        CSharpBase.generate(env, operations, output_dir, version)?;

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

        let schemas = xdk_lib::types::csharp_schema_declarations(&raw_schemas);
        let context = CSharpSchemasContext { schemas };
        let schemas_path = output_dir.join("src/Xdk/Models/Schemas.cs");
        std::fs::create_dir_all(schemas_path.parent().unwrap_or(output_dir))?;
        let content = xdk_lib::templates::render_template_with_path(
            env,
            "schemas",
            &context,
            schemas_path.to_str().unwrap_or("src/Xdk/Models/Schemas.cs"),
        )?;
        std::fs::write(&schemas_path, content)?;

        Ok(())
    }
}
