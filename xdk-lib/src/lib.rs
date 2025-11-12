/// Core module for SDK generator
///
/// This module provides the core functionality and abstractions for SDK generation.
/// It handles common operations like parsing OpenAPI specs, extracting operations,
/// and providing error handling.
///
/// When creating a new language generator, you don't need to modify the core module.
/// Instead, you should implement a new language-specific module that uses the
/// abstractions provided here.
///
/// # Components
/// - `error`: Error types and handling for SDK generation
/// - `generator`: The SDK generator interface and implementation
/// - `models`: Common data models for SDK generation
/// - `testing`: Test generation for SDK generation
/// - `casing`: Casing conversion utilities for different naming conventions
/// - `config`: Configuration management for SDK generation
pub mod casing;
pub mod config;
pub mod error;
pub mod generator;
pub mod logging;
pub mod models;
pub mod openapi;
pub mod templates;
pub mod testing;

pub use casing::*;
pub use config::*;
pub use error::*;
pub use generator::*;
pub use logging::*;

// Re-export important functions for better API
pub use openapi::extract_operations_by_tag;
pub use templates::render_template;

/// Result type for SDK generator operations
pub type Result<T> = std::result::Result<T, SdkGeneratorError>;
