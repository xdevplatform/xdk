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

mod core;
mod reference;
mod components;
mod parser;
mod error;

pub use core::*;
pub use reference::*;
pub use components::*;
pub use parser::*;
pub use error::*;


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_yaml() {
        let yaml = r#"
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Successful response
"#;
        let result = parse_yaml(yaml);
        assert!(result.is_ok());
        let openapi = result.unwrap();
        assert_eq!(openapi.openapi, "3.0.0");
        assert_eq!(openapi.info.title, "Test API");
        assert_eq!(openapi.info.version, "1.0.0");
        assert!(openapi.paths.contains_key("/test"));
    }

    #[test]
    fn test_parse_twitter_api_spec() {
        let result = parse_json_file("assets/oapi.json");
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
        assert!(params.iter().any(|p| p.as_ref().name.as_deref() == Some("query") && p.as_ref().required == Some(true)));
        assert!(params.iter().any(|p| p.as_ref().name.as_deref() == Some("max_results") && p.as_ref().required == Some(false)));
    }
}