//! OpenAPI specification parsing
//!
//! This module provides functions for parsing OpenAPI specifications from YAML or JSON formats.
//! It supports both string inputs and file paths.

use crate::context::OpenApiContextGuard;
use crate::core::OpenApi;
use crate::error::OpenApiError;
use crate::error::Result;
use serde_json::Value as JsonValue;
use serde_yaml::Value as YamlValue;

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
///
/// # Note ///
/// This function assumes an `OpenApiContextGuard` has been created
/// in the calling scope to manage the thread-local context required for
/// reference resolution (including lazy resolution).
pub fn parse_yaml(yaml: &str) -> Result<OpenApi> {
    let value: YamlValue = serde_yaml::from_str(yaml)?;

    if let Some(components) = value.get("components") {
        OpenApiContextGuard::with_context_mut(|ctx| {
            if let Some(schemas) = components.get("schemas").and_then(|s| s.as_mapping()) {
                for (name, schema_val) in schemas {
                    if let Some(name_str) = name.as_str() {
                        match serde_yaml::from_value::<crate::components::Schema>(
                            schema_val.clone(),
                        ) {
                            Ok(schema) => ctx.add_schema(name_str.to_string(), schema),
                            Err(e) => {
                                eprintln!("Warning: Failed to parse schema {}: {}", name_str, e)
                            }
                        }
                    }
                }
            }
            if let Some(parameters) = components.get("parameters").and_then(|p| p.as_mapping()) {
                for (name, param_val) in parameters {
                    if let Some(name_str) = name.as_str() {
                        match serde_yaml::from_value::<crate::components::Parameter>(
                            param_val.clone(),
                        ) {
                            Ok(param) => ctx.add_parameter(name_str.to_string(), param),
                            Err(e) => {
                                eprintln!("Warning: Failed to parse parameter {}: {}", name_str, e)
                            }
                        }
                    }
                }
            }
            if let Some(responses) = components.get("responses").and_then(|r| r.as_mapping()) {
                for (name, resp_val) in responses {
                    if let Some(name_str) = name.as_str() {
                        match serde_yaml::from_value::<crate::core::Response>(resp_val.clone()) {
                            Ok(resp) => ctx.add_response(name_str.to_string(), resp),
                            Err(e) => {
                                eprintln!("Warning: Failed to parse response {}: {}", name_str, e)
                            }
                        }
                    }
                }
            }
            if let Some(request_bodies) = components
                .get("requestBodies")
                .and_then(|rb| rb.as_mapping())
            {
                for (name, rb_val) in request_bodies {
                    if let Some(name_str) = name.as_str() {
                        match serde_yaml::from_value::<crate::core::RequestBody>(rb_val.clone()) {
                            Ok(rb) => ctx.add_request_body(name_str.to_string(), rb),
                            Err(e) => eprintln!(
                                "Warning: Failed to parse requestBody {}: {}",
                                name_str, e
                            ),
                        }
                    }
                }
            }
            if let Some(security_schemes) = components
                .get("securitySchemes")
                .and_then(|ss| ss.as_mapping())
            {
                for (name, ss_val) in security_schemes {
                    if let Some(name_str) = name.as_str() {
                        match serde_yaml::from_value::<crate::components::SecurityScheme>(
                            ss_val.clone(),
                        ) {
                            Ok(ss) => ctx.add_security_scheme(name_str.to_string(), ss),
                            Err(e) => eprintln!(
                                "Warning: Failed to parse securityScheme {}: {}",
                                name_str, e
                            ),
                        }
                    }
                }
            }
        })
        .ok_or_else(|| {
            OpenApiError::InternalError(
                "Context not available during component pre-loading in parse_yaml".to_string(),
            )
        })?;
    }

    let openapi: OpenApi = serde_yaml::from_value(value)?;
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
/// ```no_run
/// use xdk_openapi::parse_yaml_file;
///
/// let result = parse_yaml_file("../assets/oapi_short.yaml");
/// assert!(result.is_ok());
/// ```
pub fn parse_yaml_file(path: &str) -> Result<OpenApi> {
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
///
/// # Note ///
/// This function assumes an `OpenApiContextGuard` has been created
/// in the calling scope to manage the thread-local context required for
/// reference resolution (including lazy resolution).
pub fn parse_json(json: &str) -> Result<OpenApi> {
    let value: JsonValue = serde_json::from_str(json)?;

    if let Some(components) = value.get("components") {
        OpenApiContextGuard::with_context_mut(|ctx| {
            if let Some(schemas) = components.get("schemas").and_then(|s| s.as_object()) {
                for (name, schema_val) in schemas {
                    match serde_json::from_value::<crate::components::Schema>(schema_val.clone()) {
                        Ok(schema) => ctx.add_schema(name.clone(), schema),
                        Err(e) => eprintln!("Warning: Failed to parse schema {}: {}", name, e),
                    }
                }
            }
            if let Some(parameters) = components.get("parameters").and_then(|p| p.as_object()) {
                for (name, param_val) in parameters {
                    match serde_json::from_value::<crate::components::Parameter>(param_val.clone())
                    {
                        Ok(param) => ctx.add_parameter(name.clone(), param),
                        Err(e) => eprintln!("Warning: Failed to parse parameter {}: {}", name, e),
                    }
                }
            }
            if let Some(responses) = components.get("responses").and_then(|r| r.as_object()) {
                for (name, resp_val) in responses {
                    match serde_json::from_value::<crate::core::Response>(resp_val.clone()) {
                        Ok(resp) => ctx.add_response(name.clone(), resp),
                        Err(e) => eprintln!("Warning: Failed to parse response {}: {}", name, e),
                    }
                }
            }
            if let Some(request_bodies) = components
                .get("requestBodies")
                .and_then(|rb| rb.as_object())
            {
                for (name, rb_val) in request_bodies {
                    match serde_json::from_value::<crate::core::RequestBody>(rb_val.clone()) {
                        Ok(rb) => ctx.add_request_body(name.clone(), rb),
                        Err(e) => eprintln!("Warning: Failed to parse requestBody {}: {}", name, e),
                    }
                }
            }
            if let Some(security_schemes) = components
                .get("securitySchemes")
                .and_then(|ss| ss.as_object())
            {
                for (name, ss_val) in security_schemes {
                    match serde_json::from_value::<crate::components::SecurityScheme>(
                        ss_val.clone(),
                    ) {
                        Ok(ss) => ctx.add_security_scheme(name.clone(), ss),
                        Err(e) => {
                            eprintln!("Warning: Failed to parse securityScheme {}: {}", name, e)
                        }
                    }
                }
            }
        })
        .ok_or_else(|| {
            OpenApiError::InternalError(
                "Context not available during component pre-loading in parse_json".to_string(),
            )
        })?;
    }

    let openapi: OpenApi = serde_json::from_value(value)?;
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
/// let result = parse_json_file("../tests/openapi/simple.json");
/// assert!(result.is_ok());
/// ```
pub fn parse_json_file(path: &str) -> Result<OpenApi> {
    let contents = std::fs::read_to_string(path)?;
    parse_json(&contents)
}
