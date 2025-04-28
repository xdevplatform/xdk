/// Common data models for SDK generation
///
/// This file contains the core data models that are used across different language generators.
///
/// For now we are sharing context structs between languages.
/// If we require language specific contexts in the future, we will revist the design.
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

/// Context for rendering a client class template
#[derive(Debug, Serialize)]
pub struct OperationContext {
    pub tag: String,
    pub operations: Vec<OperationInfo>,
}

/// Context for rendering the main client template that imports all tag-specific clients
#[derive(Debug, Serialize)]
pub struct TagsContext {
    pub tags: Vec<String>,
}
