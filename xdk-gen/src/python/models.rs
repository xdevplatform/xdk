use crate::core::models::OperationInfo;
use serde::Serialize;

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
