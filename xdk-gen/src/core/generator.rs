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
    fn templates(&self) -> crate::core::Result<HashMap<String, String>>;

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

/// Macro for creating a language-specific SDK generator.
///
/// This macro reduces boilerplate by implementing the `LanguageGenerator` trait
/// for a given struct. It provides a convenient way to configure templates,
/// filters, and rendering logic for a specific language.
///
/// # Parameters
/// * `name` - Name of the language generator struct to create
/// * `filters` - A list of filter functions to be added to the MiniJinja environment
/// * `render` - Configuration for how templates should be rendered
///   * `multiple` - Block that defines templates to be rendered for each API tag
///   * `render ($template) to ($path)` - Render a template to a specific path
///
/// # Example
/// ```
/// # use xdk_gen::language;
/// # fn snake_case(value: &str) -> String {
/// #     value.to_lowercase()
/// # }
/// # fn pascal_case(value: &str) -> String {
/// #     value.to_uppercase()
/// # }
///
/// language! {
///     name: Python,
///     filters: [snake_case, pascal_case],
///     render: [
///         multiple { // Render once per API tag
///             render("module") to("python/src/{}.py")
///         },
///         render("__init__") to("python/src/__init__.py") // Render once for the entire SDK
///     ]
/// }
/// ```
#[macro_export]
macro_rules! language {
    (
        name: $name:ident,
        filters: [$($filter:ident),*],
        render: [
            $(
                multiple {
                    $(
                        render $template:expr => $path:expr
                    ),*
                }
            ),*,
            $(
                render $s_template:expr => $s_path:expr
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

        /// Generator implementation for the specified language
        pub struct $name;

        impl LanguageGenerator for $name {
            /// Returns the name of the generator as a string
            fn name(&self) -> &'static str {
                stringify!($name)
            }

            /// Loads templates from the filesystem for this language
            ///
            /// Searches for templates in multiple potential locations:
            /// 1. ./templates/{language_name}/
            /// 2. ../{project_root}/xdk-gen/templates/{language_name}/
            ///
            /// # Returns
            /// A HashMap containing template names and their contents
            fn templates(&self) -> Result<HashMap<String, String>> {
                use std::fs;
                use std::path::PathBuf;
                use std::env;

                let language_name = stringify!($name).to_lowercase();

                // Try multiple potential locations for the templates directory
                let potential_paths = vec![
                    PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap_or_else(|_| ".".to_string()))
                        .join("templates")
                        .join(&language_name),
                    // Find the workspace root directory that contains xdk-gen
                    PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap_or_else(|_| ".".to_string()))
                        .parent().unwrap_or(Path::new("."))
                        .join("xdk-gen")
                        .join("templates")
                        .join(&language_name),
                ];

                let mut templates = HashMap::new();
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
                                    templates.insert(template_name.to_string(), fs::read_to_string(entry.path())?);
                                }
                            }
                        }
                    }
                }
                if templates.is_empty() {
                    return Err($crate::core::SdkGeneratorError::FrameworkError(format!("No templates found for language: {}", language_name)));
                }
                Ok(templates)
            }

            /// Adds the specified language-specific filters to the MiniJinja environment
            fn add_filters(&self, env: &mut minijinja::Environment) {
                $(env.add_filter(stringify!($filter), $filter);)*
            }

            /// Generates the SDK code by rendering templates with appropriate contexts
            ///
            /// This implementation handles two types of template rendering:
            /// 1. Templates that are rendered once per API tag (like modules)
            /// 2. Templates that are rendered once for the entire SDK (like index files)
            ///
            /// # Parameters
            /// * `env` - The MiniJinja environment with templates and filters
            /// * `operations` - A map of operations grouped by tag
            /// * `output_dir` - The directory where the generated code will be written
            fn generate(
                &self,
                env: &minijinja::Environment,
                operations: &HashMap<String, Vec<OperationInfo>>,
                output_dir: &Path,
            ) -> Result<()> {

                let tags: Vec<String> = operations.keys().cloned().collect();

                // Handle per-tag template renders
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

                // Handle singleton template renders (once per SDK)
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
