use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use crate::reference::Reference;

/// Represents a parameter in an API operation
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Parameter {
    #[serde(skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "in", skip_serializing_if = "Option::is_none")]
    pub r#in: Option<String>,
    pub required: Option<bool>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub schema: Option<Reference<Schema>>,
    pub description: Option<String>,
}

/// Represents a schema
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Schema {
    #[serde(rename = "type")]
    pub schema_type: Option<String>,
    pub format: Option<String>,
    pub title: Option<String>,
    pub description: Option<String>,
    pub properties: Option<HashMap<String, Reference<Schema>>>,
    pub items: Option<Box<Reference<Schema>>>,
    pub required: Option<Vec<String>>,
    pub example: Option<serde_json::Value>,
    pub enum_values: Option<Vec<String>>,
    #[serde(rename = "enum")]
    pub enum_field: Option<Vec<String>>,
    pub minimum: Option<i64>,
    pub maximum: Option<i64>,
    pub default: Option<serde_json::Value>,
}

/// Represents the components section of the OpenAPI spec
#[derive(Debug, Serialize, Deserialize)]
pub struct Components {
    pub schemas: Option<HashMap<String, Schema>>,
    pub parameters: Option<HashMap<String, Parameter>>,
    pub security_schemes: Option<HashMap<String, SecurityScheme>>,
}

/// Represents a security scheme
#[derive(Debug, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum SecurityScheme {
    #[serde(rename = "http")]
    Http {
        scheme: String,
        bearer_format: Option<String>,
    },
    #[serde(rename = "oauth2")]
    OAuth2 {
        flows: OAuthFlows,
    },
    #[serde(rename = "apiKey")]
    ApiKey {
        r#in: String,
        name: String,
    },
}

/// Represents OAuth flows
#[derive(Debug, Serialize, Deserialize)]
pub struct OAuthFlows {
    pub implicit: Option<OAuthFlow>,
    pub authorization_code: Option<OAuthFlow>,
    pub client_credentials: Option<OAuthFlow>,
    pub password: Option<OAuthFlow>,
}

/// Represents an OAuth flow
#[derive(Debug, Serialize, Deserialize)]
pub struct OAuthFlow {
    pub authorization_url: Option<String>,
    pub token_url: Option<String>,
    pub refresh_url: Option<String>,
    pub scopes: HashMap<String, String>,
} 