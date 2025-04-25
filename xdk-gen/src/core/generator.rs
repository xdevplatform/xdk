use openapi::OpenApi;
use std::collections::HashMap;
use std::fs;
use std::path::Path;

use super::models::OperationInfo;
use super::utils::extract_operations_by_tag;
use minijinja::Environment;

/// Trait that defines the interface for language-specific SDK generators.
///
/// Implement this trait to create a generator for a new language. The recommended
/// way is to use the `define_generator!` macro which simplifies the implementation.
pub trait LanguageGenerator {
    /// Returns the name of the generator (e.g., "python", "javascript")
    fn name(&self) -> &str;

    /// Returns a list of (template_name, template_content) pairs for rendering
    fn templates(&self) -> Vec<(String, String)>;

    /// Adds language-specific filters to the MiniJinja environment
    fn add_filters(&self, env: &mut Environment);

    /// Generates the SDK code for the language
    ///
    /// # Parameters
    /// * `env` - The MiniJinja environment with templates and filters
    /// * `operations` - A map of operations grouped by tag
    /// * `output_dir` - The directory where the generated code will be written
    fn generate(
        &self,
        env: &Environment,
        operations: &HashMap<String, Vec<OperationInfo>>,
        output_dir: &Path,
    ) -> crate::core::Result<()>;
}

/// SDK generator that orchestrates the generation process.
///
/// This struct wraps a language-specific generator and handles common operations like
/// setting up the MiniJinja environment and processing the OpenAPI spec.
pub struct SdkGenerator<T: LanguageGenerator> {
    inner: T,
}

impl<T: LanguageGenerator> SdkGenerator<T> {
    /// Creates a new SDK generator with the given language generator
    pub fn new(inner: T) -> Self {
        Self { inner }
    }

    /// Generates the SDK for the given OpenAPI specification and writes it to the output directory
    ///
    /// # Parameters
    /// * `openapi` - The parsed OpenAPI specification
    /// * `output_dir` - The directory where the generated code will be written
    pub fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> crate::core::Result<()> {
        let inner = &self.inner;
        fs::create_dir_all(output_dir)?;
        let mut env = Environment::new();
        inner.add_filters(&mut env);
        let templates = inner.templates();
        for (name, content) in &templates {
            env.add_template(name, content)?;
        }

        let operations_by_tag = extract_operations_by_tag(openapi)?;
        inner.generate(&env, &operations_by_tag, output_dir)
    }
}

/// Macro for defining a language generator.
///
/// This macro simplifies the implementation of the `LanguageGenerator` trait by allowing
/// you to define all required components in a single declaration.
///
/// # Example
///
/// ```no_run
/// use xdk_gen::language;
/// 
/// fn camel_case(value: &str) -> String {
///     unimplemented!("Implements camel_case filter for Python")
/// }
/// 
/// fn js_type(value: &str) -> String {
///     unimplemented!("Implements js_type filter for Python")
/// }
/// 
/// language! {
///     Python {
///         name: "python",
///         templates: [
///             ("python/client.j2", include_str!("../../templates/python/client.j2"))
///         ],
///         filters: [camel_case, js_type],
///         generate: |env, operations, output_dir| {
///             // Implementation of the generate method
///             // Use your language-specific code generation logic here
///             Ok(())
///         }
///     }
/// }
/// ```
///
/// The generated struct will automatically implement the `LanguageGenerator` trait.
#[macro_export]
macro_rules! language {
    (
        $struct_name:ident {
            name: $name:expr,
            templates: [$(($t_name:expr, $t_content:expr)),*],
            filters: [$($filter:ident),*],
            generate: |$env:ident, $operations:ident, $output_dir:ident| $body:block
        }
    ) => {
        use $crate::core::generator::LanguageGenerator;

        pub struct $struct_name;

        impl LanguageGenerator for $struct_name {
            fn name(&self) -> &'static str {
                $name
            }

            fn templates(&self) -> Vec<(String, String)> {
                vec![$(($t_name.to_string(), $t_content.to_string())),*]
            }

            fn add_filters(&self, env: &mut minijinja::Environment) {
                $(env.add_filter(stringify!($filter), $filter);)*
            }

            fn generate(
                &self,
                $env: &minijinja::Environment,
                $operations: &std::collections::HashMap<String, Vec<$crate::core::models::OperationInfo>>,
                $output_dir: &std::path::Path,
            ) -> $crate::core::Result<()> {
                $body
            }
        }
    };
}
