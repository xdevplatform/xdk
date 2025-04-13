use crate::core::OpenApi;
use crate::error::OpenApiError;

/// Parse an OpenAPI specification from a YAML string
pub fn parse_yaml(yaml: &str) -> Result<OpenApi, OpenApiError> {
    let openapi: OpenApi = serde_yaml::from_str(yaml)?;
    Ok(openapi)
}

/// Parse an OpenAPI specification from a YAML file
pub fn parse_yaml_file(path: &str) -> Result<OpenApi, OpenApiError> {
    let contents = std::fs::read_to_string(path)?;
    parse_yaml(&contents)
}

/// Parse an OpenAPI specification from a JSON string
pub fn parse_json(json: &str) -> Result<OpenApi, OpenApiError> {
    let openapi: OpenApi = serde_json::from_str(json)?;
    Ok(openapi)
}

/// Parse an OpenAPI specification from a JSON file
pub fn parse_json_file(path: &str) -> Result<OpenApi, OpenApiError> {
    let contents = std::fs::read_to_string(path)?;
    parse_json(&contents)
} 