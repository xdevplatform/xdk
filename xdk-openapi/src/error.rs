//! Error handling for OpenAPI parsing
//! 
//! This module provides error types for handling errors that can occur when
//! parsing OpenAPI specifications.

use thiserror::Error;

/// Errors that can occur when parsing OpenAPI specifications
/// 
/// This enum provides a unified error type for all errors that can occur when
/// parsing OpenAPI specifications. It uses the `thiserror` crate to automatically
/// implement the `std::error::Error` trait.
#[derive(Error, Debug, Clone)]
pub enum OpenApiError {
    /// Error parsing YAML
    #[error("Failed to parse YAML: {0}")]
    YamlParseError(String),
    
    /// Error parsing JSON
    #[error("Failed to parse JSON: {0}")]
    JsonParseError(String),
    
    /// IO error when reading files
    #[error("IO error: {0}")]
    IoError(String),
    
    /// Reference not found in the OpenAPI specification
    #[error("Reference not found: {0}")]
    ReferenceNotFound(String),

    /// Type mismatch when resolving a reference
    #[error("Type mismatch when resolving reference")]
    TypeMismatch,

    /// Internal error during processing
    #[error("Internal error: {0}")]
    InternalError(String),
}

// Manual From implementations since we removed #[from]

impl From<serde_yaml::Error> for OpenApiError {
    fn from(err: serde_yaml::Error) -> Self {
        OpenApiError::YamlParseError(err.to_string())
    }
}

impl From<serde_json::Error> for OpenApiError {
    fn from(err: serde_json::Error) -> Self {
        OpenApiError::JsonParseError(err.to_string())
    }
}

impl From<std::io::Error> for OpenApiError {
    fn from(err: std::io::Error) -> Self {
        OpenApiError::IoError(err.to_string())
    }
} 