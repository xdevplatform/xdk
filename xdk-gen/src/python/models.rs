/// Models for Python SDK generation
///
/// This file contains the context structs that are used for rendering templates
/// in the Python SDK generator. Each struct represents a specific context for a template.
///
/// When creating a generator for a new language, you should define similar context structs
/// based on your template needs.
use crate::core::models::OperationInfo;
use serde::Serialize;

/// Context for rendering a client class template
#[derive(Debug, Serialize)]
pub struct ClientClassContext {
    pub tag: String,
    pub operations: Vec<OperationInfo>,
}

/// Context for rendering a client module template
#[derive(Debug, Serialize)]
pub struct ClientModuleContext {
    pub tag: String,
    pub operations: Vec<OperationInfo>,
}

/// Context for rendering the main client template that imports all tag-specific clients
#[derive(Debug, Serialize)]
pub struct MainClientContext {
    pub tags: Vec<String>,
}

/// Context for rendering the setup.py file
#[derive(Debug, Serialize)]
pub struct SetupPyContext {
    pub version: String,
}

/// Context for rendering the README.md file
#[derive(Debug, Serialize)]
pub struct ReadmeContext {
    pub version: String,
}
