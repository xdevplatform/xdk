use std::path::Path;
use xdk_gen::Result;
use xdk_openapi::OpenApi;

/// Trait for language-specific SDK generators.
pub trait LanguageGenerator {
    /// Generates the SDK for a specific language.
    /// 
    /// This method handles code generation, environment setup (if necessary),
    /// and code formatting.
    fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> Result<()>;
} 