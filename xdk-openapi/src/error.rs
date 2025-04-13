use thiserror::Error;

#[derive(Error, Debug)]
pub enum OpenApiError {
    #[error("Failed to parse YAML: {0}")]
    YamlParseError(#[from] serde_yaml::Error),
    #[error("Failed to parse JSON: {0}")]
    JsonParseError(#[from] serde_json::Error),
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
    #[error("Reference not found: {0}")]
    ReferenceNotFound(String),
} 