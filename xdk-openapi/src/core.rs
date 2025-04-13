use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use crate::components::{Components, Parameter, Schema};
use crate::reference::Reference;

/// Represents an OpenAPI 3.0.0 specification
#[derive(Debug, Serialize, Deserialize)]
pub struct OpenApi {
    pub openapi: String,
    pub info: Info,
    pub paths: HashMap<String, PathItem>,
    pub components: Option<Components>,
    pub security: Option<Vec<HashMap<String, Vec<String>>>>,
}

/// Information about the API
#[derive(Debug, Serialize, Deserialize)]
pub struct Info {
    pub title: String,
    pub version: String,
    pub description: Option<String>,
    pub contact: Option<Contact>,
    pub license: Option<License>,
}

/// Contact information
#[derive(Debug, Serialize, Deserialize)]
pub struct Contact {
    pub name: Option<String>,
    pub url: Option<String>,
}

/// License information
#[derive(Debug, Serialize, Deserialize)]
pub struct License {
    pub name: String,
    pub url: Option<String>,
}

/// Represents a path item in the API
#[derive(Debug, Serialize, Deserialize)]
pub struct PathItem {
    #[serde(rename = "get")]
    pub get: Option<Operation>,
    #[serde(rename = "post")]
    pub post: Option<Operation>,
    #[serde(rename = "put")]
    pub put: Option<Operation>,
    #[serde(rename = "delete")]
    pub delete: Option<Operation>,
    #[serde(rename = "patch")]
    pub patch: Option<Operation>,
}

/// Represents an API operation
#[derive(Debug, Serialize, Deserialize)]
pub struct Operation {
    pub summary: Option<String>,
    pub description: Option<String>,
    pub tags: Option<Vec<String>>,
    pub parameters: Option<Vec<Reference<Parameter>>>,
    pub request_body: Option<RequestBody>,
    pub responses: HashMap<String, Response>,
}

/// Represents a request body
#[derive(Debug, Serialize, Deserialize)]
pub struct RequestBody {
    pub content: HashMap<String, MediaType>,
    pub required: Option<bool>,
}

/// Represents a response
#[derive(Debug, Serialize, Deserialize)]
pub struct Response {
    pub description: String,
    pub content: Option<HashMap<String, MediaType>>,
}

/// Represents a media type
#[derive(Debug, Serialize, Deserialize)]
pub struct MediaType {
    pub schema: Reference<Schema>,
} 