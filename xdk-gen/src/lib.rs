pub mod error;
pub mod python;

use crate::error::Result;
use openapi::OpenApi;
use std::path::Path;

/// Trait for SDK generators
pub trait SdkGenerator {
    /// Generate the SDK for the given OpenAPI specification
    fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> Result<()>;

    /// Get the name of the SDK
    fn name(&self) -> &str;
}

/// Create a Python SDK generator
pub fn create_python_generator() -> impl SdkGenerator {
    python::PythonSdkGenerator::new()
}

/// Generate a Python SDK for the given OpenAPI specification
pub fn generate_python_sdk(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    let generator = create_python_generator();
    generator.generate(openapi, output_dir)
}

/// Re-export the error types
pub use error::{Result as SdkResult, SdkGeneratorError};
