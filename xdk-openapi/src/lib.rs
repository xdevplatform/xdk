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
        assert_eq!(schema.r#type.as_ref().unwrap(), "object");
        assert!(schema.properties.as_ref().unwrap().contains_key("name"));
        assert!(schema.properties.as_ref().unwrap().contains_key("age"));
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
        assert_eq!(openapi.info.title, "Twitter API v2");
        assert_eq!(openapi.info.version, "2.134");

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
}
