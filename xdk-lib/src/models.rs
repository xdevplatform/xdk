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
    /// Security requirements for the operation
    pub security: Option<Vec<SecurityRequirement>>,
    /// Parameters for the operation
    pub parameters: Option<Vec<RefOrValue<Parameter>>>,
    /// Request body information
    pub request_body: Option<RequestBody>,
    /// Response information
    pub responses: HashMap<StatusCode, Response>,
}

impl OperationInfo {
    /// Get parameters sorted by required status (required first, then optional)
    pub fn sorted_parameters(&self) -> Option<Vec<RefOrValue<Parameter>>> {
        self.parameters.as_ref().map(|params| {
            let mut sorted_params = params.clone();
            sorted_params.sort_by(|a, b| {
                let a_required = match a {
                    RefOrValue::Value(param) => param.required.unwrap_or(false),
                    RefOrValue::Reference { .. } => false, // Treat refs as optional for sorting
                };
                let b_required = match b {
                    RefOrValue::Value(param) => param.required.unwrap_or(false),
                    RefOrValue::Reference { .. } => false,
                };
                // Sort required first (true comes before false)
                b_required.cmp(&a_required)
            });
            sorted_params
        })
    }
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
