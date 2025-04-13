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
#[derive(Error, Debug)]
pub enum OpenApiError {
    /// Error parsing YAML
    #[error("Failed to parse YAML: {0}")]
    YamlParseError(#[from] serde_yaml::Error),
    
    /// Error parsing JSON
    #[error("Failed to parse JSON: {0}")]
    JsonParseError(#[from] serde_json::Error),
    
    /// IO error when reading files
    #[error("IO error: {0}")]
    IoError(#[from] std::io::Error),
    
    /// Reference not found in the OpenAPI specification
    #[error("Reference not found: {0}")]
    ReferenceNotFound(String),
} 