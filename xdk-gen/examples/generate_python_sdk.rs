use xdk_gen::{generate_python_sdk, error::Result};
use openapi::OpenApi;
use std::path::Path;
use std::fs;

fn main() -> Result<()> {
    // Create a minimal OpenAPI specification for testing
    let openapi = OpenApi {
        openapi: "3.0.0".to_string(),
        info: openapi::Info {
            title: "Test API".to_string(),
            version: "1.0.0".to_string(),
            description: None,
            contact: None,
            license: None,
        },
        paths: {
            let mut paths = std::collections::HashMap::new();
            let mut path_item = openapi::PathItem {
                get: None,
                post: None,
                put: None,
                delete: None,
                patch: None,
            };

            let operation = openapi::Operation {
                summary: Some("Get tweets".to_string()),
                description: Some("Returns tweets".to_string()),
                tags: Some(vec!["Tweets".to_string()]),
                parameters: Some(vec![]),
                request_body: None,
                responses: {
                    let mut responses = std::collections::HashMap::new();
                    let response = openapi::Response {
                        description: "Successful response".to_string(),
                        content: None,
                    };
                    responses.insert("200".to_string(), response);
                    responses
                },
            };

            path_item.get = Some(operation);
            paths.insert("/2/tweets".to_string(), path_item);
            paths
        },
        components: None,
        security: None,
    };

    // Generate the Python SDK
    let output_dir = Path::new("output/python-sdk");
    fs::create_dir_all(output_dir)?;
    generate_python_sdk(&openapi, output_dir)?;

    println!("Python SDK generated successfully at {}", output_dir.display());
    Ok(())
} 