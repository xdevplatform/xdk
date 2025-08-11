use openapi::OpenApi;
use std::collections::HashMap;
use std::env;
use std::fs;
use std::path::{Path, PathBuf};

use super::models::OperationInfo;
use super::testing::generate_test_specifications;
use super::utils::extract_operations_by_tag;
use minijinja::Environment;

/// Trait that defines the interface for language-specific SDK generators.
///
/// Implement this trait to create a generator for a new language. The recommended
/// way is to use the `define_generator!` macro, which simplifies the implementation.
pub trait LanguageGenerator {
    /// Returns the name of the generator; this should be the name of the language (e.g., "python", "javascript")
    fn name(&self) -> String;

    /// Loads templates from the filesystem for this language
    ///
    /// Searches for templates in multiple potential locations:
    /// 1. ./templates/{language_name}/
    /// 2. ../{project_root}/xdk-gen/templates/{language_name}/
    ///
    /// # Returns
    /// A HashMap containing template names and their contents
    fn templates(&self) -> crate::Result<HashMap<String, String>> {
        let language_name = self.name();

        let potential_paths = vec![
            PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap_or_else(|_| ".".to_string()))
                .join("templates")
                .join(&language_name),
            PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap_or_else(|_| ".".to_string()))
                .parent()
                .unwrap_or(Path::new("."))
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
                            let template_name = if file_name.ends_with(".j2")
                                || file_name.ends_with(".jinja")
                                || file_name.ends_with(".jinja2")
                            {
                                file_name.rsplit_once('.').map(|x| x.0).unwrap_or(file_name)
                            } else {
                                file_name
                            };
                            templates.insert(
                                template_name.to_string(),
                                fs::read_to_string(entry.path())?,
                            );
                        }
                    }
                }
            }
        }
        if templates.is_empty() {
            return Err(crate::SdkGeneratorError::FrameworkError(format!(
                "No templates found for language: {language_name}"
            )));
        }
        Ok(templates)
    }

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
    ) -> crate::Result<()>;

    /// Generates test code for the language (optional)
    ///
    /// # Parameters
    /// * `env` - The MiniJinja environment with templates and filters
    /// * `test_spec` - The test specification containing all test scenarios
    /// * `output_dir` - The directory where the generated test code will be written
    fn generate_tests(
        &self,
        _env: &Environment,
        _test_specs: &HashMap<String, crate::testing::TestSpecification>,
        _output_dir: &Path,
    ) -> crate::Result<()> {
        // Default implementation - no test generation
        // Languages can override this to implement test generation
        Ok(())
    }
}

/// SDK generation function that takes a language generator and an OpenAPI specification
/// and generates the SDK code for the given language in the output directory.
pub fn generate<T>(language: T, openapi: &OpenApi, output_dir: &Path) -> crate::Result<()>
where
    T: LanguageGenerator,
{
    fs::create_dir_all(output_dir)?;
    let mut env = Environment::new();
    language.add_filters(&mut env);
    let templates = language.templates()?;
    for (name, content) in &templates {
        env.add_template(name, content)?;
    }

    let operations_by_tag = extract_operations_by_tag(openapi)?;

    // Generate test specifications
    let test_specs = generate_test_specifications(&operations_by_tag)?;

    // Generate SDK code
    language.generate(&env, &operations_by_tag, output_dir)?;

    // Generate tests if test templates are available
    language
        .generate_tests(&env, &test_specs, output_dir)
        .unwrap_or_else(|e| {
            // If test generation fails, it's not critical - just log and continue
            eprintln!("Warning: Test generation failed: {}", e);
        });

    Ok(())
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
/// # use xdk_lib::language;
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
///             render "module" => "python/src/{}.py"
///         },
///         render "__init__" => "python/src/__init__.py" // Render once for the entire SDK
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
        use $crate::utils::render_template;
        use $crate::models::OperationInfo;
        use $crate::generator::LanguageGenerator;
        use $crate::Result;
        use $crate::models::{OperationContext, TagsContext, TestContext};

        /// Generator implementation for the specified language
        pub struct $name;

        impl LanguageGenerator for $name {
            fn name(&self) -> String {
                stringify!($name).to_lowercase()
            }
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
                                tag: $crate::utils::normalize_tag_to_pascal_case(tag),
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

            /// TODO: Can we make this more generic/a default implementation?
            /// Generate test code - can be overridden by specific implementations
            fn generate_tests(
                &self,
                env: &minijinja::Environment,
                test_specs: &HashMap<String, $crate::testing::TestSpecification>,
                output_dir: &Path,
            ) -> Result<()> {
                // Check if language has test templates available
                if env.get_template("test_structure").is_ok() ||
                   env.get_template("test_contracts").is_ok() ||
                   env.get_template("test_pagination").is_ok() {

                    // Use the same tag iteration as the main generate function
                    let tags: Vec<String> = test_specs.keys().cloned().collect();

                    for tag in tags {
                        let context = TestContext {
                            tag: tag.clone(),
                            test_spec: test_specs[&tag].clone(),
                        };

                        let tag_folder = output_dir.join("tests").join(tag.replace(" ", "_").to_lowercase());

                        // Generate structural tests if template exists
                        if let Ok(template) = env.get_template("test_structure") {
                            let content = template.render(&context).map_err(|e| $crate::SdkGeneratorError::TemplateError(e))?;
                            let path = tag_folder.join("test_structure.py");
                            std::fs::create_dir_all(tag_folder.clone())?;
                            std::fs::write(&path, content)?;
                        }

                        // Generate contract tests if template exists
                        match env.get_template("test_contracts") {
                            Ok(template) => {
                                let content = template.render(&context).map_err(|e| $crate::SdkGeneratorError::TemplateError(e))?;
                                let path = tag_folder.join("test_contracts.py");
                                std::fs::create_dir_all(tag_folder.clone())?;
                                std::fs::write(&path, content)?;
                            }
                            Err(e) => {
                                eprintln!("Debug: test_contracts template not found: {}", e);
                            }
                        }

                        // Generate pagination tests only if there are valid pagination tests to generate
                        let has_valid_pagination_tests = !context.test_spec.pagination_tests.is_empty()
                            && context.test_spec.pagination_tests.iter().any(|test|
                                !test.method_name.is_empty() && !test.operation_id.is_empty()
                            );

                        if has_valid_pagination_tests {
                            match env.get_template("test_pagination") {
                                Ok(template) => {
                                    let content = template.render(&context).map_err(|e| $crate::SdkGeneratorError::TemplateError(e))?;
                                    let path = tag_folder.join("test_pagination.py");
                                    std::fs::create_dir_all(tag_folder.clone())?;
                                    std::fs::write(&path, content)?;
                                }
                                Err(e) => {
                                    eprintln!("Debug: test_pagination template not found: {}", e);
                                }
                            }
                        }

                        // Generate generic tests if template exists
                        match env.get_template("test_generic") {
                            Ok(template) => {
                                let content = template.render(&context).map_err(|e| $crate::SdkGeneratorError::TemplateError(e))?;
                                let path = tag_folder.join("test_generic.py");
                                std::fs::create_dir_all(tag_folder.clone())?;
                                std::fs::write(&path, content)?;
                            }
                            Err(e) => {
                                eprintln!("Debug: test_generic template not found: {}", e);
                            }
                        }

                        // Generate __init__.py for each tag folder
                        let tag_init_path = tag_folder.join("__init__.py");
                        std::fs::write(&tag_init_path, "")?;
                    }

                    // Generate test configuration files for Python
                    if stringify!($name).to_lowercase() == "python" {
                        let conftest_content = r#""""Test configuration and fixtures."""

import pytest
from unittest.mock import Mock
from xdk import Client


@pytest.fixture
def mock_client():
    """Provide a mock client for testing."""
    return Client(base_url="https://api.example.com")


@pytest.fixture  
def mock_session():
    """Provide a mock session for HTTP requests."""
    return Mock()
"#;

                        let conftest_path = output_dir.join("tests").join("conftest.py");
                        std::fs::create_dir_all(conftest_path.parent().unwrap_or(output_dir))?;
                        std::fs::write(&conftest_path, conftest_content)?;

                        // Generate __init__.py for tests package
                        let tests_init_path = output_dir.join("tests").join("__init__.py");
                        std::fs::write(&tests_init_path, "")?;
                    }
                }

                Ok(())
            }
        }
    };
}
