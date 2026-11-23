use serde::Serialize;
use xdk_lib::{Casing, camel_case, language, pascal_case};

fn java_type(
    value: minijinja::Value,
    ns: Option<String>,
) -> std::result::Result<String, minijinja::Error> {
    let json: serde_json::Value = serde_json::to_value(&value).map_err(|e| {
        minijinja::Error::new(minijinja::ErrorKind::InvalidOperation, e.to_string())
    })?;
    Ok(xdk_lib::types::java_type_of(
        &json,
        ns.as_deref().unwrap_or("Schemas."),
    ))
}

fn java_ident(value: &str) -> String {
    xdk_lib::types::java_field_ident(value)
}

fn java_class_ident(value: &str) -> String {
    xdk_lib::types::java_schema_ident(value)
}

fn java_string_literal(value: &str) -> String {
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
struct JavaSchemasContext {
    schemas: Vec<xdk_lib::types::SchemaDecl>,
}

language! {
    name: JavaBase,
    filters: [camel_case, pascal_case, java_type, java_ident, java_class_ident, java_string_literal, path_prefix, last_part],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Camel,
    import_casing: Casing::Snake,
    variable_casing: Casing::Camel,
    render: [
        multiple {
            render "client_class" => "src/main/java/com/x/xdk/clients/{class_name}Client.java"
        },
        render "main_client" => "src/main/java/com/x/xdk/XClient.java",
        render "client_config" => "src/main/java/com/x/xdk/XClientConfig.java",
        render "api_exception" => "src/main/java/com/x/xdk/XApiException.java",
        render "http_transport" => "src/main/java/com/x/xdk/http/HttpTransport.java",
        render "jdk_http_transport" => "src/main/java/com/x/xdk/http/JdkHttpTransport.java",
        render "oauth1_auth" => "src/main/java/com/x/xdk/auth/OAuth1.java",
        render "oauth2_pkce" => "src/main/java/com/x/xdk/auth/OAuth2Pkce.java",
        render "oauth2_token" => "src/main/java/com/x/xdk/auth/OAuth2Token.java",
        render "paginator" => "src/main/java/com/x/xdk/Paginator.java",
        render "stream_config" => "src/main/java/com/x/xdk/streaming/StreamConfig.java",
        render "event_stream" => "src/main/java/com/x/xdk/streaming/EventStream.java",
        render "mock_x_api_server" => "examples/com/x/xdk/testing/MockXApiServer.java",
        render "examples_use_cases" => "examples/com/x/xdk/examples/UseCaseExamples.java",
        render "canary_app" => "examples/com/x/xdk/canary/XdkCanaryApp.java",
        render "examples_readme" => "examples/README.md",
        render "pom_xml" => "pom.xml",
        render "readme" => "README.md",
        render "gitignore" => ".gitignore"
    ],
    tests: [
        multiple {
            render "test_structure" => "src/test/java/com/x/xdk/{class_name}StructureTest.java",
            render "test_contracts" => "src/test/java/com/x/xdk/{class_name}ContractsTest.java",
            render "test_pagination" => "src/test/java/com/x/xdk/{class_name}PaginationTest.java"
        },
        render "test_core" => "src/test/java/com/x/xdk/XClientCoreTest.java",
        render "test_e2e_loopback" => "src/test/java/com/x/xdk/XClientLoopbackE2ETest.java",
        render "test_examples_and_canary" => "src/test/java/com/x/xdk/UseCaseExamplesAndCanaryTest.java"
    ]
}

pub struct Java;

impl xdk_lib::generator::LanguageGenerator for Java {
    fn name(&self) -> String {
        "java".to_string()
    }

    fn add_filters(&self, env: &mut minijinja::Environment) {
        JavaBase.add_filters(env);
    }

    fn generate(
        &self,
        env: &minijinja::Environment,
        operations: &std::collections::HashMap<Vec<String>, Vec<xdk_lib::models::OperationGroup>>,
        output_dir: &std::path::Path,
        version: &str,
    ) -> xdk_lib::Result<()> {
        JavaBase.generate(env, operations, output_dir, version)?;

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

        let schemas = xdk_lib::types::java_schema_declarations(&raw_schemas);
        let context = JavaSchemasContext { schemas };
        let schemas_path = output_dir.join("src/main/java/com/x/xdk/models/Schemas.java");
        std::fs::create_dir_all(schemas_path.parent().unwrap_or(output_dir))?;
        let content = xdk_lib::templates::render_template_with_path(
            env,
            "schemas",
            &context,
            schemas_path
                .to_str()
                .unwrap_or("src/main/java/com/x/xdk/models/Schemas.java"),
        )?;
        std::fs::write(&schemas_path, content)?;

        Ok(())
    }
}
