use crate::core::Result;
use openapi::OpenApi;
use std::collections::HashMap;
use std::fs;
use std::path::Path;

use super::utils::extract_operations_by_tag;
use super::models::OperationInfo;
use minijinja::Environment;

pub trait LanguageGenerator {
    fn name(&self) -> &str;
    fn templates(&self) -> Vec<(String, String)>;
    fn add_filters(&self, env: &mut Environment);
    fn generate(&self, env: &Environment, operations: &HashMap<String, Vec<OperationInfo>>, output_dir: &Path) -> Result<()>;
}

/// SDK generator
pub struct SdkGenerator<T: LanguageGenerator> {
    inner: T,
}

impl<T: LanguageGenerator> SdkGenerator<T> {
    pub fn new(inner: T) -> Self {
        Self { 
            inner
        }
    }

    pub fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> Result<()> {
        // Get the language generator
        let inner = &self.inner;
            
        // Create the output directory if it doesn't exist
        fs::create_dir_all(output_dir)?;

        // Create the minijinja environment
        let mut env = Environment::new();

        // Add filters from the generator
        inner.add_filters(&mut env);

        // Add templates
        let templates = inner.templates();
        for (name, content) in &templates {
            env.add_template(name, content)?;
        }

        // Extract operations by tag
        let operations_by_tag = extract_operations_by_tag(openapi)?;

        // Generate using the language-specific generator function
        inner.generate(&env, &operations_by_tag, output_dir)
    }

}

#[macro_export]
macro_rules! define_generator {
    (
        $struct_name:ident {
            name: $name:expr,
            templates: [$(($t_name:expr, $t_content:expr)),*],
            filters: [$($filter:ident),*],
            generate: |$env:ident, $operations:ident, $output_dir:ident| $body:block
        }
    ) => {
        pub struct $struct_name;

        impl LanguageGenerator for $struct_name {
            fn name(&self) -> &'static str {
                $name
            }

            fn templates(&self) -> Vec<(String, String)> {
                vec![$(($t_name.to_string(), $t_content.to_string())),*]
            }

            fn add_filters(&self, env: &mut Environment) {
                $(env.add_filter(stringify!($filter), $filter);)*
            }

            fn generate(
                &self,
                $env: &Environment,
                $operations: &HashMap<String, Vec<OperationInfo>>,
                $output_dir: &Path,
            ) -> Result<()> {
                $body
            }
        }
    };
}