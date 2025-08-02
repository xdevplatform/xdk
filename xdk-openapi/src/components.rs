//! OpenAPI components
//!
//! This module contains the data structures for OpenAPI components.
//! Components are reusable parts of an OpenAPI specification that can be referenced
//! from multiple places.

use crate::reference::RefOrValue;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

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
/// This enum captures the different types of schemas supported by OpenAPI 3.0.0.
#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(untagged)]
pub enum Schema {
    /// Composition schema using anyOf
    AnyOf(Box<AnyOfSchema>),
    /// Composition schema using allOf
    AllOf(Box<AllOfSchema>),
    /// Composition schema using oneOf
    OneOf(Box<OneOfSchema>),
    /// Negation schema using not
    Not(Box<NotSchema>),
    /// Typed schema with a specific type
    Typed(Box<TypedSchema>),
}

/// A schema with a specific type
#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(tag = "type")]
pub enum TypedSchema {
    /// Object schema
    #[serde(rename = "object")]
    Object(Box<ObjectSchema>),
    /// Array schema
    #[serde(rename = "array")]
    Array(Box<ArraySchema>),
    /// String schema
    #[serde(rename = "string")]
    String(Box<StringSchema>),
    /// Integer schema
    #[serde(rename = "integer")]
    Integer(Box<IntegerSchema>),
    /// Number schema
    #[serde(rename = "number")]
    Number(Box<NumberSchema>),
    /// Boolean schema
    #[serde(rename = "boolean")]
    Boolean(Box<BooleanSchema>),
}

/// Base fields common to all schemas
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct BaseSchema {
    /// The title of the schema
    pub title: Option<String>,
    /// A description of the schema
    pub description: Option<String>,
    /// An example value for the schema
    pub example: Option<serde_json::Value>,
    /// Default value for the schema
    pub default: Option<serde_json::Value>,
    /// Whether the schema is deprecated
    pub deprecated: Option<bool>,
}

/// Object schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct ObjectSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Properties of the object
    pub properties: Option<HashMap<String, RefOrValue<Schema>>>,
    /// Required property names
    pub required: Option<Vec<String>>,
    /// Additional properties behavior
    #[serde(rename = "additionalProperties")]
    pub additional_properties: Option<Box<AdditionalProperties>>,
    /// Discriminator for polymorphism
    pub discriminator: Option<Discriminator>,
    /// Minimum number of properties
    #[serde(rename = "minProperties")]
    pub min_properties: Option<u32>,
    /// Maximum number of properties
    #[serde(rename = "maxProperties")]
    pub max_properties: Option<u32>,
}

/// Array schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct ArraySchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Schema for array items
    pub items: Option<Box<RefOrValue<Schema>>>,
    /// Minimum number of items
    #[serde(rename = "minItems")]
    pub min_items: Option<u32>,
    /// Maximum number of items
    #[serde(rename = "maxItems")]
    pub max_items: Option<u32>,
    /// Whether items must be unique
    #[serde(rename = "uniqueItems")]
    pub unique_items: Option<bool>,
}

/// String schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct StringSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// String format (e.g., date-time, email, uuid)
    pub format: Option<String>,
    /// Minimum string length
    #[serde(rename = "minLength")]
    pub min_length: Option<u32>,
    /// Maximum string length
    #[serde(rename = "maxLength")]
    pub max_length: Option<u32>,
    /// Regex pattern
    pub pattern: Option<String>,
    /// Enumeration of valid values
    #[serde(rename = "enum")]
    pub enum_values: Option<Vec<String>>,
}

/// Integer schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct IntegerSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Integer format (e.g., int32, int64)
    pub format: Option<String>,
    /// Minimum value
    pub minimum: Option<i64>,
    /// Maximum value
    pub maximum: Option<i64>,
    /// Exclusive minimum
    #[serde(rename = "exclusiveMinimum")]
    pub exclusive_minimum: Option<bool>,
    /// Exclusive maximum
    #[serde(rename = "exclusiveMaximum")]
    pub exclusive_maximum: Option<bool>,
    /// Multiple of constraint
    #[serde(rename = "multipleOf")]
    pub multiple_of: Option<f64>,
    /// Enumeration of valid values
    #[serde(rename = "enum")]
    pub enum_values: Option<Vec<i64>>,
}

/// Number schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct NumberSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Number format (e.g., float, double)
    pub format: Option<String>,
    /// Minimum value
    pub minimum: Option<f64>,
    /// Maximum value
    pub maximum: Option<f64>,
    /// Exclusive minimum
    #[serde(rename = "exclusiveMinimum")]
    pub exclusive_minimum: Option<bool>,
    /// Exclusive maximum
    #[serde(rename = "exclusiveMaximum")]
    pub exclusive_maximum: Option<bool>,
    /// Multiple of constraint
    #[serde(rename = "multipleOf")]
    pub multiple_of: Option<f64>,
    /// Enumeration of valid values
    #[serde(rename = "enum")]
    pub enum_values: Option<Vec<f64>>,
}

/// Boolean schema fields
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct BooleanSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
}

/// AnyOf composition schema
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct AnyOfSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Schemas to match any of
    #[serde(rename = "anyOf")]
    pub any_of: Vec<RefOrValue<Schema>>,
    /// Discriminator for polymorphism
    pub discriminator: Option<Discriminator>,
}

/// AllOf composition schema
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct AllOfSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Schemas to match all of
    #[serde(rename = "allOf")]
    pub all_of: Vec<RefOrValue<Schema>>,
    /// Discriminator for polymorphism
    pub discriminator: Option<Discriminator>,
}

/// OneOf composition schema
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct OneOfSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Schemas to match exactly one of
    #[serde(rename = "oneOf")]
    pub one_of: Vec<RefOrValue<Schema>>,
    /// Discriminator for polymorphism
    pub discriminator: Option<Discriminator>,
}

/// Not composition schema
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct NotSchema {
    #[serde(flatten)]
    pub base: BaseSchema,
    /// Schema that must not match
    pub not: Box<RefOrValue<Schema>>,
}

/// Additional properties behavior for object schemas
#[derive(Debug, Serialize, Deserialize, Clone)]
#[serde(untagged)]
pub enum AdditionalProperties {
    /// Boolean value - true allows any additional properties, false disallows them
    Boolean(bool),
    /// Schema for additional properties
    Schema(Box<RefOrValue<Schema>>),
}

/// Discriminator for polymorphic schemas
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct Discriminator {
    /// Property name that holds the discriminator value
    #[serde(rename = "propertyName")]
    pub property_name: String,
    /// Mapping of discriminator values to schema names
    pub mapping: Option<HashMap<String, String>>,
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
        flows: Box<OAuthFlows>,
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
