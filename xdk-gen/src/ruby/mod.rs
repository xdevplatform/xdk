/// Ruby SDK Generator Module
///
/// This module implements the SDK generator for Ruby.
mod generator;

pub use generator::Ruby;

#[cfg(test)]
mod tests {
    use crate::ruby::generator::Ruby;
    use std::fs;
    use std::path::Path;
    use tempfile::Builder;
    use xdk_lib::Result;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApiContextGuard, parse_json_file};

    fn create_output_dir() -> std::path::PathBuf {
        let temp_dir = Builder::new()
            .prefix("test_output_ruby")
            .tempdir()
            .expect("Failed to create temporary directory");
        temp_dir.path().to_path_buf()
    }

    fn verify_sdk_structure(output_dir: &Path) {
        let lib_dir = output_dir.join("lib").join("xdk");
        assert!(lib_dir.exists(), "lib/xdk directory should exist");
        assert!(
            lib_dir.join("client.rb").exists(),
            "lib/xdk/client.rb should exist"
        );
        assert!(
            lib_dir.join("version.rb").exists(),
            "lib/xdk/version.rb should exist"
        );
        assert!(
            output_dir.join("xdk.gemspec").exists(),
            "xdk.gemspec should exist"
        );
        assert!(
            output_dir.join("README.md").exists(),
            "README.md should exist"
        );
    }

    #[test]
    fn test_simple_openapi() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();
        let result = generate(Ruby, &openapi, &output_dir, "0.0.1-test");
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);
        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_version_in_generated_files() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let test_version = "1.2.3-test";
        let result = generate(Ruby, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        let version_content = fs::read_to_string(output_dir.join("lib/xdk/version.rb"))
            .expect("Failed to read version.rb");
        assert!(
            version_content.contains("1.2.3-test"),
            "version.rb should contain the test version"
        );
    }
}
