/// Common data models for SDK generation
///
/// This file contains the core data models that are used across different language generators.
/// They represent common concepts like operations, parameters, etc. from the OpenAPI spec.
///
/// When creating a language generator, you should use these models for the common OpenAPI
/// concepts, and create language-specific models for template rendering.
use openapi::{Parameter, RefOrValue, RequestBody, Response, StatusCode};
use serde::Serialize;
use std::collections::HashMap;
/// Information about an operation in the OpenAPI spec
#[derive(Debug, Serialize, Clone)]
pub struct OperationInfo {
    /// Operation ID from the OpenAPI spec
    pub operation_id: String,
    /// HTTP method (GET, POST, etc.)
    pub method: String,
    /// Path for the operation
    pub path: String,
    /// Description of the operation
    pub description: Option<String>,
    /// Summary of the operation
    pub summary: Option<String>,
    /// Parameters for the operation
    pub parameters: Option<Vec<RefOrValue<Parameter>>>,
    /// Request body information
    pub request_body: Option<RequestBody>,
    /// Response information
    pub responses: HashMap<StatusCode, Response>,
}
