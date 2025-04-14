mod models;
mod render;
mod utils;
mod generator;

pub use generator::PythonSdkGenerator;

#[cfg(test)]
mod tests {
    use super::*;
    use crate::SdkGenerator;
    use openapi::{parse_json_file, OpenApi, RefOrValue};
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
                        responses.insert("200".to_string(), RefOrValue::Value(response));
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
        
        // Check for tag directories and their files
        let tweets_dir = package_dir.join("tweets");
        assert!(tweets_dir.exists());
        assert!(tweets_dir.join("__init__.py").exists());
        assert!(tweets_dir.join("client.py").exists());
        
        // Verify no other files exist in the output directory
        let output_files: std::collections::HashSet<_> = std::fs::read_dir(output_dir)
            .unwrap()
            .filter_map(|entry| entry.ok())
            .map(|entry| entry.file_name().to_string_lossy().to_string())
            .collect();
        
        let expected_output_files = std::collections::HashSet::from([
            "xdk".to_string(),
            "setup.py".to_string(),
            "README.md".to_string(),
            "requirements.txt".to_string(),
        ]);
        
        assert_eq!(output_files, expected_output_files, "Unexpected files in output directory");
        
        // Verify no other files exist in the package directory
        let package_files: std::collections::HashSet<_> = std::fs::read_dir(&package_dir)
            .unwrap()
            .filter_map(|entry| entry.ok())
            .map(|entry| entry.file_name().to_string_lossy().to_string())
            .collect();
        
        let expected_package_files = std::collections::HashSet::from([
            "__init__.py".to_string(),
            "client.py".to_string(),
            "tweets".to_string(),
        ]);
        
        assert_eq!(package_files, expected_package_files, "Unexpected files in package directory");
    }

    #[test]
    fn test_generate_python_sdk_from_file() {
        // Create a temporary directory for the output
        let temp_dir = tempdir().unwrap();
        let output_dir = temp_dir.path();

        let openapi = parse_json_file("../assets/oapi_short.json").unwrap();
        let result = PythonSdkGenerator::new().generate(&openapi, output_dir);
        assert!(result.is_ok());

        // Verify that the output directory contains the expected files
        let package_dir = output_dir.join("xdk");
        assert!(package_dir.exists());
        assert!(package_dir.join("__init__.py").exists());
        assert!(package_dir.join("client.py").exists());
        
        // Check for tag directories and their files
        let communities_dir = package_dir.join("communities");
        assert!(communities_dir.exists());
        assert!(communities_dir.join("__init__.py").exists());
        assert!(communities_dir.join("client.py").exists());
        
        let direct_messages_dir = package_dir.join("direct_messages");
        assert!(direct_messages_dir.exists());
        assert!(direct_messages_dir.join("__init__.py").exists());
        assert!(direct_messages_dir.join("client.py").exists());
        
        let tweets_dir = package_dir.join("tweets");
        assert!(tweets_dir.exists());
        assert!(tweets_dir.join("__init__.py").exists());
        assert!(tweets_dir.join("client.py").exists());
        
        assert!(output_dir.join("setup.py").exists());
        assert!(output_dir.join("README.md").exists());
        assert!(output_dir.join("requirements.txt").exists());
        
        // Verify no other files exist in the output directory
        let output_files: std::collections::HashSet<_> = std::fs::read_dir(output_dir)
            .unwrap()
            .filter_map(|entry| entry.ok())
            .map(|entry| entry.file_name().to_string_lossy().to_string())
            .collect();
        
        let expected_output_files = std::collections::HashSet::from([
            "xdk".to_string(),
            "setup.py".to_string(),
            "README.md".to_string(),
            "requirements.txt".to_string(),
        ]);
        
        assert_eq!(output_files, expected_output_files, "Unexpected files in output directory");
        
        // Verify no other files exist in the package directory
        let package_files: std::collections::HashSet<_> = std::fs::read_dir(&package_dir)
            .unwrap()
            .filter_map(|entry| entry.ok())
            .map(|entry| entry.file_name().to_string_lossy().to_string())
            .collect();
        
        let expected_package_files = std::collections::HashSet::from([
            "__init__.py".to_string(),
            "client.py".to_string(),
            "communities".to_string(),
            "direct_messages".to_string(),
            "tweets".to_string(),
        ]);
        
        assert_eq!(package_files, expected_package_files, "Unexpected files in package directory");
    }
} 