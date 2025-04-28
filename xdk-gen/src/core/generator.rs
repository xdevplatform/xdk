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
    /// Returns the name of the generator, this should be the name of the language (e.g., "python", "javascript")
    fn name(&self) -> &str;

    /// Returns a list of (template_name, template_content) pairs for rendering
    fn templates(&self) -> crate::core::Result<Vec<(String, String)>>;

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
        let templates = inner.templates()?;
        for (name, content) in &templates {
            env.add_template(name, content)?;
        }

        let operations_by_tag = extract_operations_by_tag(openapi)?;
        inner.generate(&env, &operations_by_tag, output_dir)
    }
}

#[macro_export]
macro_rules! language {
    (
        name: $name:ident,
        filters: [$($filter:ident),*],
        render: [
            $(
                multiple {
                    $(
                        render ($template:expr) to ($path:expr)
                    ),*
                }
            ),*,
            $(
                render ($s_template:expr) to ($s_path:expr)
            ),*
        ]
    ) => {
        use std::collections::HashMap;
        use std::path::{Path, PathBuf};
        use $crate::core::utils::render_template;
        use $crate::core::models::OperationInfo;
        use $crate::core::generator::LanguageGenerator;
        use $crate::core::Result;
        use $crate::core::models::{OperationContext, TagsContext};

        pub struct $name;

        impl LanguageGenerator for $name {
            fn name(&self) -> &'static str {
                stringify!($name)
            }

            fn templates(&self) -> Result<Vec<(String, String)>> {
                use std::fs;
                use std::path::PathBuf;
                use std::env;

                let language_name = stringify!($name).to_lowercase();

                // Try multiple potential locations for the templates directory
                let potential_paths = vec![
                    PathBuf::from("templates").join(&language_name),
                    PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap_or_else(|_| ".".to_string()))
                        .join("templates")
                        .join(&language_name),
                ];

                let mut templates = Vec::new();
                for template_dir in potential_paths {
                    if !template_dir.exists() || !template_dir.is_dir() {
                        continue;
                    }

                    for entry in fs::read_dir(&template_dir)?.filter_map(|e| e.ok()) {
                        if let Ok(file_type) = entry.file_type() {
                            if file_type.is_file() {
                                if let Some(file_name) = entry.file_name().to_str() {
                                    // Get the template name without the extension
                                    let template_name = if file_name.ends_with(".j2") || file_name.ends_with(".jinja") || file_name.ends_with(".jinja2") {
                                        file_name.rsplitn(2, '.').nth(1).unwrap_or(file_name)
                                    } else {
                                        file_name
                                    };
                                    templates.push((template_name.to_string(), fs::read_to_string(entry.path())?));
                                }
                            }
                        }
                    }
                }
                Ok(templates)
            }

            fn add_filters(&self, env: &mut minijinja::Environment) {
                $(env.add_filter(stringify!($filter), $filter);)*
            }

            fn generate(
                &self,
                env: &minijinja::Environment,
                operations: &HashMap<String, Vec<OperationInfo>>,
                output_dir: &Path,
            ) -> Result<()> {

                let tags: Vec<String> = operations.keys().cloned().collect();

                // Handle loop renders
                $(
                    for tag in &tags {
                        $(
                            let context = OperationContext {
                                tag: tag.to_string(),
                                operations: operations[tag].clone()
                            };
                            let output_path = PathBuf::from(format!($path, tag.replace(" ", "_").to_lowercase()));
                            let content = render_template(env, $template, &context)?;
                            let full_path = output_dir.join(&output_path);
                            std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                            std::fs::write(&full_path, content)?;
                        )*
                    }
                )*

                $(
                    let context = TagsContext {
                        tags: tags.clone(),
                    };
                    let output_path = PathBuf::from($s_path);
                    let content = render_template(env, $s_template, &context)?;
                    let full_path = output_dir.join(&output_path);
                    std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                    std::fs::write(&full_path, content)?;
                )*

                Ok(())
            }
        }
    };
}
