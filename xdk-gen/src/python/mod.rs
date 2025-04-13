mod models;
mod render;
mod utils;
mod generator;

pub use generator::PythonSdkGenerator;

#[cfg(test)]
mod tests {
    use super::*;
    use crate::SdkGenerator;
    use openapi::OpenApi;
    use tempfile::tempdir;

    #[test]
    fn test_generate_python_sdk() {
        // Create a temporary directory for the output
        let temp_dir = tempdir().unwrap();
        let output_dir = temp_dir.path();

        // Create a minimal OpenAPI specification
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
        let generator = PythonSdkGenerator::new();
        let result = generator.generate(&openapi, output_dir);
        assert!(result.is_ok());

        // Verify that the output directory contains the expected files
        let package_dir = output_dir.join("xdk");
        assert!(package_dir.exists());
        assert!(package_dir.join("__init__.py").exists());
        assert!(package_dir.join("client.py").exists());
        assert!(package_dir.join("tweets.py").exists());
        assert!(package_dir.join("tweets_client.py").exists());
        assert!(output_dir.join("setup.py").exists());
        assert!(output_dir.join("README.md").exists());
        assert!(output_dir.join("requirements.txt").exists());
    }
} 