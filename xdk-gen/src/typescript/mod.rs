mod generator;
pub use generator::TypeScript;

#[cfg(test)]
mod tests {
    use crate::typescript::generator::TypeScript;
    use std::fs;
    use tempfile::Builder;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApiContextGuard, parse_json_file};

    fn create_output_dir() -> std::path::PathBuf {
        let temp_dir = Builder::new()
            .prefix("test_output_ts")
            .tempdir()
            .expect("Failed to create temporary directory");
        temp_dir.path().to_path_buf()
    }

    #[test]
    fn test_version_in_package_json() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();
        
        // Generate with a specific test version
        let test_version = "1.2.3-test";
        let result = generate(TypeScript, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        // Verify version appears in package.json
        let package_json_path = output_dir.join("package.json");
        let contents = fs::read_to_string(&package_json_path)
            .expect("Failed to read package.json");
        assert!(contents.contains("\"version\": \"1.2.3-test\""), 
                "package.json should contain version 1.2.3-test");
    }

    #[test]
    fn test_user_agent_in_client() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();
        
        // Test with beta version
        let test_version = "0.1.1-beta";
        let result = generate(TypeScript, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        // Verify User-Agent format: xdk-typescript/<version>
        let client_path = output_dir.join("src/client.ts");
        let contents = fs::read_to_string(&client_path)
            .expect("Failed to read client.ts");
        assert!(contents.contains("'User-Agent': 'xdk-typescript/0.1.1-beta'"), 
                "client.ts should contain User-Agent with version 0.1.1-beta");
    }

    #[test]
    fn test_user_agent_not_in_config_interface() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();
        
        let test_version = "1.0.0";
        let result = generate(TypeScript, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        // Verify userAgent is NOT in ClientConfig interface (it should be static)
        let client_path = output_dir.join("src/client.ts");
        let contents = fs::read_to_string(&client_path)
            .expect("Failed to read client.ts");
        
        // Check that ClientConfig interface doesn't have userAgent field
        let config_section = contents.split("export interface ClientConfig")
            .nth(1)
            .and_then(|s| s.split("}").next())
            .expect("Failed to find ClientConfig interface");
        
        assert!(!config_section.contains("userAgent"), 
                "ClientConfig should not contain userAgent field - it should be static");
    }
}
