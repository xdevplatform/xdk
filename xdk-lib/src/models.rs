use crate::testing::TestSpecification;
/// Common data models for SDK generation
///
/// This file contains the core data models that are used across different language generators.
///
/// For now we are sharing context structs between languages.
/// If we require language specific contexts in the future, we will revist the design.
use openapi::{Parameter, RefOrValue, RequestBody, Response, SecurityRequirement, StatusCode};
use serde::Serialize;
use std::collections::HashMap;

/// Transformation rules for improving client and method names
#[derive(Debug, Clone)]
pub struct NameTransformation {
    /// Original tag name from OpenAPI spec
    pub original_tag: String,
    /// Improved client name
    pub normalized_tag: String,
    /// Mapping of original operation IDs to improved method names
    pub operation_mappings: HashMap<String, String>,
}

/// Information about an operation in the OpenAPI spec
#[derive(Debug, Serialize, Clone)]
pub struct OperationInfo {
    /// Original operation ID from the OpenAPI spec
    pub operation_id: String,
    /// Transformed method name (if transformation applied)
    pub normalized_operation_id: String,
    /// HTTP method (GET, POST, etc.)
    pub method: String,
    /// Path for the operation
    pub path: String,
    /// Description of the operation
    pub description: Option<String>,
    /// Summary of the operation
    pub summary: Option<String>,
    /// Security requirements for the operation
    pub security: Option<Vec<SecurityRequirement>>,
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

/// Context for rendering test templates
#[derive(Debug, Serialize)]
pub struct TestContext {
    pub tag: String,
    pub test_spec: TestSpecification,
}
