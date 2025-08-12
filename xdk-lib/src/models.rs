use crate::Casing;
/// Common data models for SDK generation
///
/// This file contains the core data models that are used across different language generators.
/// It also provides factory functions for creating properly configured model instances.
///
/// For now we are sharing context structs between languages.
/// If we require language specific contexts in the future, we will revist the design.
use crate::testing::TestSpecification;
use openapi::{
    Parameter, RefOrValue, RequestBody, Response, Schema, SecurityRequirement, StatusCode,
};
use serde::Serialize;
use std::collections::HashMap;

#[derive(Debug, Serialize, Clone)]
pub struct OperationGroup {
    pub operation: OperationInfo,
    pub metadata: Metadata,
    /// Raw parameters from OpenAPI (before casing is applied)
    pub raw_parameters: Option<Vec<RefOrValue<Parameter>>>,
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
    /// Parameters for the operation (processed with casing applied)
    pub parameters: Option<Vec<ParameterInfo>>,
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

/// Information about a parameter with different casing variants
#[derive(Debug, Serialize, Clone)]
pub struct ParameterInfo {
    /// Original parameter name from OpenAPI
    pub original_name: String,
    /// Variable name (cased for target language, e.g., "user_id")
    pub variable_name: String,
    /// Parameter location (path, query, header, cookie)
    pub location: String,
    /// Whether the parameter is required
    pub required: bool,
    /// Parameter type
    pub param_type: String,
    /// Parameter description
    pub description: Option<String>,
    /// Parameter schema (for complex validation)
    pub schema: Option<RefOrValue<openapi::Schema>>,
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

impl TagInfo {
    /// Create TagInfo with different casing variants based on language configuration
    pub fn new(
        tag_words: &[String],
        class_casing: Casing,
        import_casing: Casing,
        property_casing: Casing,
    ) -> Self {
        Self {
            original: tag_words.to_vec(),
            class_name: class_casing.convert_words(tag_words),
            import_name: import_casing.convert_words(tag_words),
            property_name: property_casing.convert_words(tag_words),
            display_name: tag_words.join(" "),
        }
    }
}

impl ParameterInfo {
    /// Convert OpenAPI parameters to ParameterInfo with casing applied
    pub fn from_openapi_parameters(
        parameters: &Option<Vec<RefOrValue<Parameter>>>,
        variable_casing: Casing,
    ) -> Option<Vec<Self>> {
        parameters.as_ref().map(|params| {
            params
                .iter()
                .filter_map(|param_ref| {
                    // Handle both direct parameters and parameter references
                    let param = match param_ref {
                        RefOrValue::Value(p) => p,
                        RefOrValue::Reference { .. } => return None, // Skip references for now
                    };

                    if let (Some(name), Some(location)) = (&param.name, &param.r#in) {
                        let param_type = extract_param_type(param);
                        let is_required = param.required.unwrap_or(false) || location == "path";

                        Some(Self {
                            original_name: name.clone(),
                            variable_name: variable_casing.convert_string(name),
                            location: location.clone(),
                            required: is_required,
                            param_type,
                            description: param.description.clone(),
                            schema: param.schema.clone(),
                        })
                    } else {
                        None
                    }
                })
                .collect()
        })
    }
}

/// Extract parameter type from parameter schema
fn extract_param_type(param: &Parameter) -> String {
    if let Some(RefOrValue::Value(Schema::Typed(typed))) = &param.schema {
        match typed.as_ref() {
            openapi::TypedSchema::String(_) => "string".to_string(),
            openapi::TypedSchema::Integer(_) => "integer".to_string(),
            openapi::TypedSchema::Number(_) => "number".to_string(),
            openapi::TypedSchema::Boolean(_) => "boolean".to_string(),
            openapi::TypedSchema::Array(_) => "array".to_string(),
            openapi::TypedSchema::Object(_) => "object".to_string(),
        }
    } else if let Some(RefOrValue::Reference { .. }) = &param.schema {
        "reference".to_string()
    } else {
        "any".to_string()
    }
}
