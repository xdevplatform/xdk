//! # XDK OpenAPI
//!
//! A Rust library for parsing and working with OpenAPI 3.0.0 specifications.
//!
//! This crate provides functionality to parse OpenAPI specifications from YAML or JSON formats,
//! and provides strongly-typed structures for working with the parsed data.
//!
//! ## Features
//!
//! - Parse OpenAPI 3.0.0 specifications from YAML or JSON
//! - Strongly-typed representation of OpenAPI elements
//! - Support for references and components
//! - Comprehensive error handling
//!
//! ## Example
//!
//! ```rust
//! use xdk_openapi::parse_yaml;
//!
//! let yaml = r#"
//! openapi: 3.0.0
//! info:
//!   title: Test API
//!   version: 1.0.0
//! paths:
//!   /test:
//!     get:
//!       summary: Test endpoint
//!       operationId: getTest
//!       responses:
//!         '200':
//!           description: Successful response
//! "#;
//!
//! let result = parse_yaml(yaml);
//! assert!(result.is_ok());
//! let openapi = result.unwrap();
//! assert_eq!(openapi.openapi, "3.0.0");
//! assert_eq!(openapi.info.title, "Test API");
//! assert_eq!(openapi.info.version, "1.0.0");
//! ```

mod components;
mod context;
mod core;
mod error;
mod parser;
mod reference;

pub use components::*;
pub use context::*;
pub use core::*;
pub use error::*;
pub use parser::*;
pub use reference::*;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_info() {
        let result = parse_json_file("../tests/openapi/info.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert_eq!(openapi.openapi, "3.0.0");
        assert_eq!(openapi.info.title, "Test API");
        assert_eq!(openapi.info.version, "1.0.0");
    }

    #[test]
    fn test_parse_with_components_reference() {
        let _guard = OpenApiContextGuard::new();
        let result = parse_json_file("../tests/openapi/components_reference.json");
        if let Err(e) = &result {
            println!("Error parsing OpenAPI spec: {:?}", e);
        }
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert!(openapi.paths.contains_key("/test"));
        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        assert_eq!(post_op.summary, Some("Test endpoint".to_string()));
        assert!(post_op.request_body.is_some());

        let request_body = post_op.request_body.as_ref().unwrap();
        let body = request_body.content.get("application/json").unwrap();

        let schema = body.schema.try_resolve().unwrap();
        if let Schema::Typed(typed_schema) = schema.as_ref() {
            if let TypedSchema::Object(object_schema) = typed_schema.as_ref() {
                assert!(
                    object_schema
                        .properties
                        .as_ref()
                        .unwrap()
                        .contains_key("name")
                );
                assert!(
                    object_schema
                        .properties
                        .as_ref()
                        .unwrap()
                        .contains_key("age")
                );
            } else {
                panic!("Expected object schema");
            }
        } else {
            panic!("Expected typed schema");
        }
    }

    #[test]
    fn test_parse_with_single_path() {
        let result = parse_json_file("../tests/openapi/single_path.json");
        if let Err(e) = &result {
            println!("Error parsing OpenAPI spec: {:?}", e);
        }
        assert!(result.is_ok());
    }

    #[test]
    fn test_parse_with_all_of() {
        let _guard = OpenApiContextGuard::new();
        let result = parse_json_file("../tests/openapi/all_of.json");
        if let Err(e) = &result {
            println!("Error parsing OpenAPI spec: {:?}", e);
        }
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert!(openapi.paths.contains_key("/test"));
        let get_op = openapi.paths.get("/test").unwrap().get.as_ref().unwrap();
        assert_eq!(get_op.summary, Some("Test endpoint".to_string()));
        assert!(get_op.responses.contains_key("200"));
        let response = get_op.responses.get("200").unwrap();
        assert_eq!(
            response.description,
            Some("Successful response".to_string())
        );
    }

    #[test]
    fn test_parse_with_any_of_request() {
        let _guard = OpenApiContextGuard::new();
        let result = parse_json_file("../tests/openapi/any_of_request.json");
        if let Err(e) = &result {
            println!("Error parsing OpenAPI spec: {:?}", e);
        }
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert!(openapi.paths.contains_key("/test"));
        let get_op = openapi.paths.get("/test").unwrap().get.as_ref().unwrap();
        assert_eq!(get_op.summary, Some("Test endpoint".to_string()));
        assert!(get_op.responses.contains_key("200"));
        let response = get_op.responses.get("200").unwrap();
        assert_eq!(
            response.description,
            Some("Successful response".to_string())
        );

        // Should be able to access anyOf schemas in components
        if let Some(components) = &openapi.components
            && let Some(schemas) = &components.schemas
        {
            if let Some(Schema::AnyOf(any_of)) = schemas.get("TestSchemaAnyOf") {
                assert_eq!(any_of.any_of.len(), 3);
                println!(
                    "Successfully parsed anyOf schema with {} variants",
                    any_of.any_of.len()
                );
            }
            if let Some(Schema::AllOf(all_of)) = schemas.get("TestSchemaAllOf") {
                assert_eq!(all_of.all_of.len(), 3);
                println!(
                    "Successfully parsed allOf schema with {} variants",
                    all_of.all_of.len()
                );
            }
        }
    }

    #[test]
    fn test_parse_twitter_api_spec() {
        let _guard = OpenApiContextGuard::new();
        let result = parse_json_file("../tests/openapi/openapi.json");
        if let Err(e) = &result {
            println!("Error parsing OpenAPI spec: {:?}", e);
        }
        assert!(result.is_ok());
        let openapi = result.unwrap();

        // Verify basic structure
        assert_eq!(openapi.openapi, "3.0.0");
        assert_eq!(openapi.info.title, "X API v2");

        // Verify paths exist
        assert!(openapi.paths.contains_key("/2/communities/search"));
        assert!(openapi.paths.contains_key("/2/communities/{id}"));

        // Verify a specific endpoint
        let communities_search = openapi.paths.get("/2/communities/search").unwrap();
        let get_op = communities_search.get.as_ref().unwrap();
        assert_eq!(get_op.summary, Some("Search Communities".to_string()));
        assert!(get_op.parameters.is_some());

        // Verify parameters
        let params = get_op.parameters.as_ref().unwrap();
        assert!(
            params
                .iter()
                .any(|p| p.try_resolve().unwrap().name.as_deref() == Some("query"))
        );
        assert!(
            params
                .iter()
                .any(|p| p.try_resolve().unwrap().name.as_deref() == Some("max_results"))
        );
    }

    #[test]
    fn test_parse_security_requirement() {
        let result = parse_json_file("../tests/openapi/security_requirement.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert!(openapi.paths.contains_key("/2/tweets"));
        let get_op = openapi
            .paths
            .get("/2/tweets")
            .unwrap()
            .get
            .as_ref()
            .unwrap();
        assert!(get_op.security.is_some());
        let security = get_op.security.as_ref().unwrap();
        assert_eq!(security.len(), 1);
        let security_requirement = security[0].clone();
        assert_eq!(security_requirement.0.get("BearerToken"), Some(&vec![]));
    }

    #[test]
    fn test_schema_validation_fields() {
        let result = parse_json_file("../tests/openapi/schema_validation.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::Typed(typed_schema) = schema.as_ref()
            && let TypedSchema::Object(object_schema) = typed_schema.as_ref()
        {
            let properties = object_schema.properties.as_ref().unwrap();

            // Test string validation fields
            let username_schema = properties.get("username").unwrap().try_resolve().unwrap();
            if let Schema::Typed(typed) = username_schema.as_ref()
                && let TypedSchema::String(string_schema) = typed.as_ref()
            {
                assert_eq!(string_schema.min_length, Some(3));
                assert_eq!(string_schema.max_length, Some(50));
                assert_eq!(string_schema.pattern, Some("^[a-zA-Z0-9_]+$".to_string()));
                assert_eq!(
                    string_schema.base.description,
                    Some("Username field".to_string())
                );
            }
        }
    }

    #[test]
    fn test_additional_properties() {
        let result = parse_json_file("../tests/openapi/additional_properties.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::Typed(typed) = schema.as_ref()
            && let TypedSchema::Object(object_schema) = typed.as_ref()
        {
            assert!(object_schema.additional_properties.is_some());
        }
    }

    #[test]
    fn test_enum_schemas() {
        let result = parse_json_file("../tests/openapi/enum_schemas.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::Typed(typed) = schema.as_ref()
            && let TypedSchema::Object(object_schema) = typed.as_ref()
        {
            let properties = object_schema.properties.as_ref().unwrap();

            // Test string enum exists
            let status_schema = properties.get("status").unwrap().try_resolve().unwrap();
            if let Schema::Typed(typed_status) = status_schema.as_ref()
                && let TypedSchema::String(string_schema) = typed_status.as_ref()
            {
                assert!(string_schema.enum_values.is_some());
                assert_eq!(
                    string_schema.base.description,
                    Some("Status of the item".to_string())
                );
            }
        }
    }

    #[test]
    fn test_one_of_schema_composition() {
        let result = parse_json_file("../tests/openapi/one_of_schema.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::OneOf(one_of_schema) = schema.as_ref() {
            assert_eq!(one_of_schema.one_of.len(), 2);
            assert!(one_of_schema.discriminator.is_some());
            let discriminator = one_of_schema.discriminator.as_ref().unwrap();
            assert_eq!(discriminator.property_name, "type");
            assert!(discriminator.mapping.is_some());
        } else {
            panic!("Expected oneOf schema");
        }
    }

    #[test]
    fn test_not_schema_composition() {
        let result = parse_json_file("../tests/openapi/not_schema.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::Not(not_schema) = schema.as_ref() {
            let inner_schema = not_schema.not.try_resolve().unwrap();
            if let Schema::Typed(typed) = inner_schema.as_ref()
                && let TypedSchema::String(string_schema) = typed.as_ref()
            {
                assert_eq!(
                    string_schema.enum_values,
                    Some(vec!["forbidden".to_string()])
                );
            }
        } else {
            panic!("Expected not schema");
        }
    }

    #[test]
    fn test_complex_array_schemas() {
        let result = parse_json_file("../tests/openapi/complex_arrays.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::Typed(typed) = schema.as_ref()
            && let TypedSchema::Object(object_schema) = typed.as_ref()
        {
            let properties = object_schema.properties.as_ref().unwrap();

            // Test simple array validation
            let simple_array = properties
                .get("simple_array")
                .unwrap()
                .try_resolve()
                .unwrap();
            if let Schema::Typed(typed_array) = simple_array.as_ref()
                && let TypedSchema::Array(array_schema) = typed_array.as_ref()
            {
                assert_eq!(array_schema.min_items, Some(1));
                assert_eq!(array_schema.max_items, Some(100));
                assert_eq!(array_schema.unique_items, Some(true));
            }
        }
    }

    #[test]
    fn test_parameter_schemas() {
        let result = parse_json_file("../tests/openapi/parameter_schemas.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let get_op = openapi
            .paths
            .get("/users/{userId}")
            .unwrap()
            .get
            .as_ref()
            .unwrap();
        assert!(get_op.parameters.is_some());
        let params = get_op.parameters.as_ref().unwrap();
        assert_eq!(params.len(), 3);

        // Test path parameter
        let user_id_param = params[0].try_resolve().unwrap();
        assert_eq!(user_id_param.name.as_deref(), Some("userId"));
        assert_eq!(user_id_param.r#in.as_deref(), Some("path"));
        assert_eq!(user_id_param.required, Some(true));
    }

    #[test]
    fn test_deeply_nested_all_of_composition() {
        let _guard = OpenApiContextGuard::new();
        let result = parse_json_file("../tests/openapi/deeply_nested_all_of.json");
        assert!(result.is_ok());
        let openapi = result.unwrap();

        let post_op = openapi.paths.get("/test").unwrap().post.as_ref().unwrap();
        let request_body = post_op.request_body.as_ref().unwrap();
        let content = request_body.content.get("application/json").unwrap();
        let schema = content.schema.try_resolve().unwrap();

        if let Schema::AllOf(all_of_schema) = schema.as_ref() {
            assert_eq!(all_of_schema.all_of.len(), 3);
        } else {
            panic!("Expected allOf schema");
        }
    }

    #[test]
    fn test_invalid_openapi_structure() {
        let result = parse_json_file("../tests/openapi/invalid_yaml.json");
        // This should parse but be missing required info field
        assert!(result.is_err());
    }
}
