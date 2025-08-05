/// Python SDK Generator Module
///
/// This module implements the SDK generator for Python. It serves as a reference
/// implementation for creating generators for other languages.
///
/// # Structure
/// - `generator.rs`: Contains the PythonGenerator implementation using the define_generator! macro
/// - `models.rs`: Contains context structs used for rendering templates
/// - Tests in this file demonstrate how to use the generator with various OpenAPI specs
mod generator;

pub use generator::Python;

#[cfg(test)]
mod tests {
    use crate::python::generator::Python;
    use std::fs;
    use std::path::Path;
    use tempfile::Builder;
    use xdk_lib::Result;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApi, OpenApiContextGuard, parse_json_file};

    // Helper function to create output directory for a test
    fn create_output_dir() -> std::path::PathBuf {
        let temp_dir = Builder::new()
            .prefix("test_output")
            .tempdir()
            .expect("Failed to create temporary directory");

        // make a real dir from tempdir on ./test_output
        // let output_dir = Path::new("./test_output");
        // fs::create_dir_all(output_dir).expect("Failed to create test_output directory");

        // // copy the tempdir to the output_dir
        // fs::copy_dir_all(temp_dir.path(), output_dir).expect("Failed to copy tempdir to test_output directory");

        temp_dir.path().to_path_buf()
    }

    // Helper function to verify basic SDK structure
    fn verify_sdk_structure(output_dir: &Path) {
        let package_dir = output_dir.join("xdk");
        assert!(package_dir.exists(), "Package directory should exist");
        assert!(
            package_dir.join("__init__.py").exists(),
            "__init__.py should exist"
        );
        assert!(
            package_dir.join("client.py").exists(),
            "client.py should exist"
        );

        // Verify basic files exist
        assert!(
            output_dir.join("pyproject.toml").exists(),
            "pyproject.toml should exist"
        );
        assert!(
            output_dir.join("README.md").exists(),
            "README.md should exist"
        );
    }

    macro_rules! assert_file_contains_text {
        ($output_dir:expr, $rel_path:expr, $text:expr) => {
            // Construct the full path using the passed output_dir
            let full_path = $output_dir.join($rel_path);
            let contents = fs::read_to_string(&full_path).unwrap_or_else(|err| {
                panic!("Failed to read file {:?}: {}", full_path, err);
            });
            assert!(
                contents.contains($text),
                "File {:?} should contain text: {}\nActual contents:\n---\n{}\n---",
                full_path,
                $text,
                contents
            );
        };
    }

    fn setup_generator_and_generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
        generate(Python, openapi, output_dir)
    }

    #[test]
    fn test_simple_openapi() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();
        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);

        // Check for tag directories and their files
        let posts_dir = output_dir.join("xdk").join("posts");
        assert!(posts_dir.exists(), "posts directory should exist");
        assert!(
            posts_dir.join("__init__.py").exists(),
            "posts/__init__.py should exist"
        );
        assert!(
            posts_dir.join("client.py").exists(),
            "posts/client.py should exist"
        );
    }

    #[test]
    fn test_components_reference() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/components_reference.json").unwrap();
        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_nested_refs() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/nested_refs.json").unwrap();
        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_request_response_refs() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/request_response_refs.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_parameters_with_ref() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/parameters_with_ref.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_schema_with_components_ref() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/schema_with_components_ref.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_single_schema_no_ref() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/single_schema_no_ref.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_multiple_paths_with_refs() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/multiple_paths_with_refs.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_all_of() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/all_of.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_single_path() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/single_path.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_info() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/info.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        verify_sdk_structure(&output_dir);
    }

    #[test]
    fn test_operation_id_maps_to_function_name() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi =
            parse_json_file("../tests/openapi/operation_id_maps_to_function_name.json").unwrap();

        let result = setup_generator_and_generate(&openapi, &output_dir);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);
        assert_file_contains_text!(
            output_dir,
            "xdk/communities/client.py",
            "search"
        );

        verify_sdk_structure(&output_dir);
    }
}
