mod generator;
pub use generator::Java;

#[cfg(test)]
mod tests {
    use crate::java::generator::Java;
    use std::fs;
    use tempfile::Builder;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApiContextGuard, parse_json_file};

    fn create_output_dir() -> std::path::PathBuf {
        Builder::new()
            .prefix("test_output_java")
            .tempdir()
            .expect("Failed to create temporary directory")
            .path()
            .to_path_buf()
    }

    #[test]
    fn test_java_sdk_generation_smoke() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let result = generate(Java, &openapi, &output_dir, "0.1.0-test");
        assert!(result.is_ok(), "Failed to generate Java SDK: {:?}", result);

        let pom = fs::read_to_string(output_dir.join("pom.xml")).unwrap();
        assert!(pom.contains("<version>0.1.0-test</version>"));

        let client =
            fs::read_to_string(output_dir.join("src/main/java/com/xdevplatform/xdk/XClient.java"))
                .unwrap();
        assert!(client.contains("xdk-java/0.1.0-test"));
        assert!(
            output_dir
                .join("src/main/java/com/xdevplatform/xdk/models/Schemas.java")
                .exists()
        );
    }
}
