use openapi::{Parameter, Reference};
use serde::Serialize;
use std::collections::HashMap;

#[derive(Debug, Serialize, Clone)]
pub struct OperationInfo {
    pub path: String,
    pub method: String,
    pub operation_id: String,
    pub summary: String,
    pub description: String,
    pub parameters: Vec<Reference<Parameter>>,
    pub request_body: Option<String>,
    pub responses: HashMap<String, String>,
}

#[derive(Debug, Serialize)]
pub struct ClientClassContext {
    pub tag: String,
    pub operations: Vec<OperationInfo>,
}

#[derive(Debug, Serialize)]
pub struct ClientModuleContext {
    pub tag: String,
    pub operations: Vec<OperationInfo>,
}

#[derive(Debug, Serialize)]
pub struct MainClientContext {
    pub tags: Vec<String>,
}

#[derive(Debug, Serialize)]
pub struct SetupPyContext {
    pub version: String,
}

#[derive(Debug, Serialize)]
pub struct ReadmeContext {
    pub version: String,
} 