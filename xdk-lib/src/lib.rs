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
/// - `utils`: Utility functions for SDK generation
/// - `testing`: Test generation for SDK generation
pub mod error;
pub mod generator;
pub mod models;
pub mod testing;
pub mod utils;

pub use error::*;
pub use generator::*;

/// Result type for SDK generator operations
pub type Result<T> = std::result::Result<T, SdkGeneratorError>;
