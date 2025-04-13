mod python;

use openapi::OpenApi;
use std::path::Path;

/// Trait for SDK generators
pub trait SdkGenerator {
    /// Generate the SDK for the given OpenAPI specification
    fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> std::io::Result<()>;

    /// Get the name of the SDK
    fn name(&self) -> &str;
}