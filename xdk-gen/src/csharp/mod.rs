mod generator;
pub use generator::CSharp;

#[cfg(test)]
mod tests {
    use crate::csharp::generator::CSharp;
    use std::fs;
    use tempfile::Builder;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApiContextGuard, parse_json_file};

    fn create_output_dir() -> std::path::PathBuf {
        Builder::new()
            .prefix("test_output_csharp")
            .tempdir()
            .expect("Failed to create temporary directory")
            .path()
            .to_path_buf()
    }

    #[test]
    fn test_csharp_sdk_generation_smoke() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let result = generate(CSharp, &openapi, &output_dir, "0.1.0-test");
        assert!(result.is_ok(), "Failed to generate C# SDK: {:?}", result);

        let csproj = fs::read_to_string(output_dir.join("src/Xdk/Xdk.csproj")).unwrap();
        assert!(csproj.contains("<PackageId>XDevPlatform.Xdk</PackageId>"));
        assert!(csproj.contains("<Version>0.1.0-test</Version>"));

        let client = fs::read_to_string(output_dir.join("src/Xdk/XClient.cs")).unwrap();
        assert!(client.contains("xdk-csharp/0.1.0-test"));
        assert!(output_dir.join("src/Xdk/Models/Schemas.cs").exists());
    }
}
