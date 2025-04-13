use std::io;
use std::path::PathBuf;
use thiserror::Error;

/// Errors that can occur during SDK generation
#[derive(Debug, Error)]
pub enum SdkGeneratorError {
    /// IO error occurred during file operations
    #[error("IO error: {0}")]
    IoError(#[from] io::Error),
    
    /// Template error occurred during rendering
    #[error("Template error: {0}")]
    TemplateError(String),
    
    /// Invalid OpenAPI specification
    #[error("Invalid OpenAPI: {0}")]
    InvalidOpenApi(String),
    
    /// Missing required field in OpenAPI specification
    #[error("Missing field: {0}")]
    MissingField(String),
    
    /// Invalid path
    #[error("Invalid path: {0:?}")]
    InvalidPath(PathBuf),
    
    /// Other errors
    #[error("Error: {0}")]
    Other(String),
}

impl From<String> for SdkGeneratorError {
    fn from(err: String) -> Self {
        SdkGeneratorError::Other(err)
    }
}

impl From<&str> for SdkGeneratorError {
    fn from(err: &str) -> Self {
        SdkGeneratorError::Other(err.to_string())
    }
}

impl From<minijinja::Error> for SdkGeneratorError {
    fn from(err: minijinja::Error) -> Self {
        SdkGeneratorError::TemplateError(err.to_string())
    }
}

/// Result type for SDK generator operations
pub type Result<T> = std::result::Result<T, SdkGeneratorError>; 