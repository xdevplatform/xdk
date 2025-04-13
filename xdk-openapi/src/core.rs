//! Core OpenAPI 3.0.0 data structures
//! 
//! This module contains the primary data structures that represent an OpenAPI 3.0.0 specification.
//! These structures are designed to be serializable and deserializable using serde.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use crate::components::{Components, Parameter, Schema};
use crate::reference::Reference;

/// Represents an OpenAPI 3.0.0 specification
/// 
/// This is the root object of an OpenAPI document. It contains all the information
/// about the API, including paths, components, and security requirements.
#[derive(Debug, Serialize, Deserialize)]
pub struct OpenApi {
    /// The version of the OpenAPI specification being used
    pub openapi: String,
    /// Information about the API
    pub info: Info,
    /// The available paths and operations for the API
    pub paths: HashMap<String, PathItem>,
    /// Reusable components for the API
    pub components: Option<Components>,
    /// Security requirements for the API
    pub security: Option<Vec<HashMap<String, Vec<String>>>>,
}

/// Information about the API
/// 
/// Contains metadata about the API, such as title, version, description,
/// contact information, and license.
#[derive(Debug, Serialize, Deserialize)]
pub struct Info {
    /// The title of the API
    pub title: String,
    /// The version of the API
    pub version: String,
    /// A description of the API
    pub description: Option<String>,
    /// Contact information for the API
    pub contact: Option<Contact>,
    /// License information for the API
    pub license: Option<License>,
}

/// Contact information for the API
/// 
/// Contains information about the contact for the API.
#[derive(Debug, Serialize, Deserialize)]
pub struct Contact {
    /// The name of the contact
    pub name: Option<String>,
    /// The URL of the contact
    pub url: Option<String>,
}

/// License information for the API
/// 
/// Contains information about the license for the API.
#[derive(Debug, Serialize, Deserialize)]
pub struct License {
    /// The name of the license
    pub name: String,
    /// The URL of the license
    pub url: Option<String>,
}

/// Represents a path item in the API
/// 
/// A path item represents a set of operations that can be performed on a specific path.
/// Each path item can have multiple HTTP methods associated with it.
#[derive(Debug, Serialize, Deserialize)]
pub struct PathItem {
    /// GET operation for this path
    #[serde(rename = "get")]
    pub get: Option<Operation>,
    /// POST operation for this path
    #[serde(rename = "post")]
    pub post: Option<Operation>,
    /// PUT operation for this path
    #[serde(rename = "put")]
    pub put: Option<Operation>,
    /// DELETE operation for this path
    #[serde(rename = "delete")]
    pub delete: Option<Operation>,
    /// PATCH operation for this path
    #[serde(rename = "patch")]
    pub patch: Option<Operation>,
}

/// Represents an API operation
/// 
/// An operation represents a specific HTTP method that can be performed on a path.
/// It contains information about parameters, request body, responses, and other metadata.
#[derive(Debug, Serialize, Deserialize)]
pub struct Operation {
    /// A short summary of the operation
    pub summary: Option<String>,
    /// A detailed description of the operation
    pub description: Option<String>,
    /// Tags for grouping operations
    pub tags: Option<Vec<String>>,
    /// Parameters for the operation
    pub parameters: Option<Vec<Reference<Parameter>>>,
    /// Request body for the operation
    pub request_body: Option<RequestBody>,
    /// Responses for the operation
    pub responses: HashMap<String, Response>,
}

/// Represents a request body
/// 
/// A request body contains the content that can be sent in a request.
#[derive(Debug, Serialize, Deserialize)]
pub struct RequestBody {
    /// The content of the request body, keyed by media type
    pub content: HashMap<String, MediaType>,
    /// Whether the request body is required
    pub required: Option<bool>,
}

/// Represents a response
/// 
/// A response contains information about a possible response from the API.
#[derive(Debug, Serialize, Deserialize)]
pub struct Response {
    /// A description of the response
    pub description: String,
    /// The content of the response, keyed by media type
    pub content: Option<HashMap<String, MediaType>>,
}

/// Represents a media type
/// 
/// A media type contains a schema that describes the structure of the content.
#[derive(Debug, Serialize, Deserialize)]
pub struct MediaType {
    /// The schema for the media type
    pub schema: Reference<Schema>,
} 