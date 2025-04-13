//! OpenAPI specification parsing
//! 
//! This module provides functions for parsing OpenAPI specifications from YAML or JSON formats.
//! It supports both string inputs and file paths.

use crate::core::OpenApi;
use crate::error::OpenApiError;

/// Parse an OpenAPI specification from a YAML string
/// 
/// # Arguments
/// 
/// * `yaml` - The YAML string containing the OpenAPI specification
/// 
/// # Returns
/// 
/// A parsed OpenAPI specification or an error if parsing failed
/// 
/// # Examples
/// 
/// ```
/// use xdk_openapi::parse_yaml;
/// 
/// let yaml = r#"
/// openapi: 3.0.0
/// info:
///   title: Test API
///   version: 1.0.0
/// paths:
///   /test:
///     get:
///       summary: Test endpoint
///       responses:
///         '200':
///           description: Successful response
/// "#;
/// 
/// let result = parse_yaml(yaml);
/// assert!(result.is_ok());
/// ```
pub fn parse_yaml(yaml: &str) -> Result<OpenApi, OpenApiError> {
    let openapi: OpenApi = serde_yaml::from_str(yaml)?;
    Ok(openapi)
}

/// Parse an OpenAPI specification from a YAML file
/// 
/// # Arguments
/// 
/// * `path` - The path to the YAML file containing the OpenAPI specification
/// 
/// # Returns
/// 
/// A parsed OpenAPI specification or an error if parsing failed
/// 
/// # Examples
/// 
/// ```
/// use xdk_openapi::parse_yaml_file;
/// 
/// let result = parse_yaml_file("../assets/oapi_short.yaml");
/// assert!(result.is_ok());
/// ```
pub fn parse_yaml_file(path: &str) -> Result<OpenApi, OpenApiError> {
    let contents = std::fs::read_to_string(path)?;
    parse_yaml(&contents)
}

/// Parse an OpenAPI specification from a JSON string
/// 
/// # Arguments
/// 
/// * `json` - The JSON string containing the OpenAPI specification
/// 
/// # Returns
/// 
/// A parsed OpenAPI specification or an error if parsing failed
/// 
/// # Examples
/// 
/// ```
/// use xdk_openapi::parse_json;
/// 
/// let json = r#"{
///   "openapi": "3.0.0",
///   "info": {
///     "title": "Test API",
///     "version": "1.0.0"
///   },
///   "paths": {
///     "/test": {
///       "get": {
///         "summary": "Test endpoint",
///         "responses": {
///           "200": {
///             "description": "Successful response"
///           }
///         }
///       }
///     }
///   }
/// }"#;
/// 
/// let result = parse_json(json);
/// assert!(result.is_ok());
/// ```
pub fn parse_json(json: &str) -> Result<OpenApi, OpenApiError> {
    let openapi: OpenApi = serde_json::from_str(json)?;
    Ok(openapi)
}

/// Parse an OpenAPI specification from a JSON file
/// 
/// # Arguments
/// 
/// * `path` - The path to the JSON file containing the OpenAPI specification
/// 
/// # Returns
/// 
/// A parsed OpenAPI specification or an error if parsing failed
/// 
/// # Examples
/// 
/// ```
/// use xdk_openapi::parse_json_file;
/// 
/// let result = parse_json_file("../assets/oapi_short.json");
/// assert!(result.is_ok());
/// ```
pub fn parse_json_file(path: &str) -> Result<OpenApi, OpenApiError> {
    let contents = std::fs::read_to_string(path)?;
    parse_json(&contents)
} 