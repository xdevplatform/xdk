mod generator;

pub use generator::Elixir;

#[cfg(test)]
mod tests {
    use crate::elixir::generator::Elixir;
    use std::fs;
    use tempfile::Builder;
    use xdk_lib::generator::generate;
    use xdk_openapi::{OpenApiContextGuard, parse_json_file};

    fn create_output_dir() -> std::path::PathBuf {
        Builder::new()
            .prefix("test_output_elixir")
            .tempdir()
            .expect("Failed to create temporary directory")
            .path()
            .to_path_buf()
    }

    #[test]
    fn test_generates_mix_exs() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let result = generate(Elixir, &openapi, &output_dir, "0.1.0");
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        assert!(output_dir.join("mix.exs").exists());
        assert!(output_dir.join("lib/xdk.ex").exists());
        assert!(output_dir.join("lib/xdk/errors.ex").exists());
    }

    #[test]
    fn test_version_in_mix_exs() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let test_version = "1.2.3-test";
        let result = generate(Elixir, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        let mix_exs = fs::read_to_string(output_dir.join("mix.exs")).unwrap();
        assert!(
            mix_exs.contains("1.2.3-test"),
            "mix.exs should contain version 1.2.3-test"
        );
    }

    #[test]
    fn test_user_agent_in_client() {
        let output_dir = create_output_dir();
        let _guard = OpenApiContextGuard::new();
        let openapi = parse_json_file("../tests/openapi/simple.json").unwrap();

        let test_version = "0.1.0";
        let result = generate(Elixir, &openapi, &output_dir, test_version);
        assert!(result.is_ok(), "Failed to generate SDK: {:?}", result);

        let client = fs::read_to_string(output_dir.join("lib/xdk.ex")).unwrap();
        assert!(
            client.contains("xdk-elixir/"),
            "client should contain User-Agent prefix"
        );
        assert!(
            client.contains("@version \"0.1.0\""),
            "client should contain @version module attribute with version"
        );
    }
}
