use openapi::{Parameter, RefOrValue, Schema};
use serde::Serialize;
use std::collections::HashMap;

#[derive(Debug, Serialize, Clone)]
pub struct OperationInfo {
    pub path: String,
    pub method: String,
    pub operation_id: String,
    pub summary: String,
    pub description: String,
    pub parameters: Vec<RefOrValue<Parameter>>,
    pub request_body: Option<RequestBody>,
    pub responses: HashMap<String, String>,
}

#[derive(Debug, Serialize, Clone)]
pub struct RequestBody {
    pub content_type: String,
    pub schema: RefOrValue<Schema>,
    pub required: bool,
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
