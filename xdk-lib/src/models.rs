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

#[derive(Debug, Serialize, Clone)]
pub struct OperationGroup {
    pub operation: OperationInfo,
    pub metadata: Metadata,
}

/// Information about an operation in the OpenAPI spec
#[derive(Debug, Serialize, Clone)]
pub struct OperationInfo {
    /// Class name for Request/Response models (e.g., "GetUsers")
    pub class_name: String,
    /// Method name (same as operation_id for consistency)
    pub method_name: String,
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

#[derive(Debug, Serialize, Clone)]
pub struct Metadata {
    pub normalized_operation_id: Vec<String>,
}

/// Context for rendering a client class template
#[derive(Debug, Serialize)]
pub struct OperationContext {
    pub tag: TagInfo,
    pub operations: Vec<OperationInfo>,
}

/// Information about a tag with different casing variants
#[derive(Debug, Serialize, Clone)]
pub struct TagInfo {
    /// Original tag words
    pub original: Vec<String>,
    /// Class name (e.g., "CommunityNotes")
    pub class_name: String,
    /// Import name/module name (e.g., "community_notes")
    pub import_name: String,
    /// Property name (e.g., "community_notes")
    pub property_name: String,
    /// Display name (e.g., "Community Notes")
    pub display_name: String,
}

/// Context for rendering the main client template that imports all tag-specific clients
#[derive(Debug, Serialize)]
pub struct TagsContext {
    pub tags: Vec<TagInfo>,
}

/// Context for rendering test templates
#[derive(Debug, Serialize)]
pub struct TestContext {
    pub tag: TagInfo,
    pub test_spec: TestSpecification,
}

impl OperationInfo {
    pub fn with_casing(self, method_name: String, class_name: String) -> Self {
        Self {
            method_name,
            class_name,
            ..self
        }
    }
}
