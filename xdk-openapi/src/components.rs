//! OpenAPI components
//! 
//! This module contains the data structures for OpenAPI components.
//! Components are reusable parts of an OpenAPI specification that can be referenced
//! from multiple places.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use crate::reference::RefOrValue;

/// Represents a parameter in an API operation
/// 
/// Parameters define inputs to operations. They can be path parameters, query parameters,
/// header parameters, or cookie parameters.
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Parameter {
    /// The name of the parameter
    #[serde(skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    /// The location of the parameter (path, query, header, cookie)
    #[serde(rename = "in", skip_serializing_if = "Option::is_none")]
    pub r#in: Option<String>,
    /// Whether the parameter is required
    pub required: Option<bool>,
    /// The schema for the parameter
    #[serde(skip_serializing_if = "Option::is_none")]
    pub schema: Option<RefOrValue<Schema>>,
    /// A description of the parameter
    pub description: Option<String>,
}

/// Represents a schema
/// 
/// Schemas define the structure of data types used in the API.
/// They can represent primitive types, objects, arrays, and more.
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Schema {
    /// The type of the schema (string, number, integer, boolean, object, array)
    #[serde(rename = "type")]
    pub r#type: Option<String>,
    /// The format of the schema (e.g., date-time, email, uuid)
    pub format: Option<String>,
    /// The title of the schema
    pub title: Option<String>,
    /// A description of the schema
    pub description: Option<String>,
    /// Properties of an object schema
    pub properties: Option<HashMap<String, RefOrValue<Schema>>>,
    /// Items of an array schema
    pub items: Option<Box<RefOrValue<Schema>>>,
    /// Required properties of an object schema
    pub required: Option<Vec<String>>,
    /// An example value for the schema
    pub example: Option<serde_json::Value>,
    /// Enum values for the schema
    pub enum_values: Option<Vec<String>>,
    /// Enum values for the schema (alternative field name)
    #[serde(rename = "enum")]
    pub enum_field: Option<Vec<String>>,
    /// Minimum value for number/integer schemas
    pub minimum: Option<i64>,
    /// Maximum value for number/integer schemas
    pub maximum: Option<i64>,
    /// Default value for the schema
    pub default: Option<serde_json::Value>,
}

/// Represents the components section of the OpenAPI spec
/// 
/// Components are reusable parts of an OpenAPI specification that can be referenced
/// from multiple places.
#[derive(Debug, Serialize, Deserialize)]
pub struct Components {
    /// Schemas defined in the components section
    pub schemas: Option<HashMap<String, Schema>>,
    /// Parameters defined in the components section
    pub parameters: Option<HashMap<String, Parameter>>,
    /// Security schemes defined in the components section
    pub security_schemes: Option<HashMap<String, SecurityScheme>>,
}

/// Represents a security scheme
/// 
/// Security schemes define how the API can be secured.
#[derive(Debug, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum SecurityScheme {
    /// HTTP authentication
    #[serde(rename = "http")]
    Http {
        /// The HTTP authentication scheme (basic, bearer, digest)
        scheme: String,
        /// The bearer format (JWT, etc.)
        bearer_format: Option<String>,
    },
    /// OAuth 2.0 authentication
    #[serde(rename = "oauth2")]
    OAuth2 {
        /// The OAuth flows
        flows: OAuthFlows,
    },
    /// API key authentication
    #[serde(rename = "apiKey")]
    ApiKey {
        /// The location of the API key (header, query, cookie)
        r#in: String,
        /// The name of the API key
        name: String,
    },
}

/// Represents OAuth flows
/// 
/// OAuth flows define how OAuth 2.0 authentication can be performed.
#[derive(Debug, Serialize, Deserialize)]
pub struct OAuthFlows {
    /// Implicit flow
    pub implicit: Option<OAuthFlow>,
    /// Authorization code flow
    pub authorization_code: Option<OAuthFlow>,
    /// Client credentials flow
    pub client_credentials: Option<OAuthFlow>,
    /// Password flow
    pub password: Option<OAuthFlow>,
}

/// Represents an OAuth flow
/// 
/// An OAuth flow defines the URLs and scopes for an OAuth 2.0 authentication flow.
#[derive(Debug, Serialize, Deserialize)]
pub struct OAuthFlow {
    /// The authorization URL
    pub authorization_url: Option<String>,
    /// The token URL
    pub token_url: Option<String>,
    /// The refresh URL
    pub refresh_url: Option<String>,
    /// The scopes available for the flow
    pub scopes: HashMap<String, String>,
} 