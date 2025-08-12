use openapi::OpenApi;
use std::collections::HashMap;
use std::env;
use std::fs;
use std::path::{Path, PathBuf};

use super::models::OperationGroup;
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
        operations: &HashMap<Vec<String>, Vec<OperationGroup>>,
        output_dir: &Path,
    ) -> crate::Result<()>;

    // Test generation is now integrated into the main generate method
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

    // Generate SDK code
    language.generate(&env, &operations_by_tag, output_dir)?;

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
/// * `class_casing` - Casing convention for class/tag names (e.g., Casing::Pascal)
/// * `operation_casing` - Casing convention for operation/method names (e.g., Casing::Snake)
/// * `import_casing` - Casing convention for import/module names (e.g., Casing::Snake for Python, Casing::Pascal for Java)
/// * `variable_casing` - Casing convention for variable/property names (e.g., Casing::Snake)
/// * `render` - Configuration for how templates should be rendered
///   * `multiple` - Block that defines templates to be rendered for each API tag
///   * `render ($template) to ($path)` - Render a template to a specific path
/// * `tests` - Configuration for how test templates should be rendered
///   * `multiple` - Block that defines test templates to be rendered for each API tag
///   * `render ($template) to ($path)` - Render a test template to a specific path
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
///     class_casing: Casing::Pascal,
///     operation_casing: Casing::Snake,
///     import_casing: Casing::Snake,
///     variable_casing: Casing::Snake,
///     render: [
///         multiple { // Render once per API tag
///             render "module" => "python/src/{}.py"
///         },
///         render "__init__" => "python/src/__init__.py" // Render once for the entire SDK
///     ],
///     tests: [
///         multiple { // Render once per API tag
///             render "test_contracts" => "tests/{}/test_contracts.py",
///             render "test_generic" => "tests/{}/test_generic.py"
///         },
///         render "conftest" => "tests/conftest.py" // Render once for all tests
///     ]
/// }
/// ```
#[macro_export]
macro_rules! language {
    (
        name: $name:ident,
        filters: [$($filter:ident),*],
        class_casing: $class_casing:expr,
        operation_casing: $operation_casing:expr,
        import_casing: $import_casing:expr,
        variable_casing: $variable_casing:expr,
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
        ],
        tests: [
            $(
                multiple {
                    $(
                        render $test_template:expr => $test_path:expr
                    ),*
                }
            ),*,
            $(
                render $s_test_template:expr => $s_test_path:expr
            ),*
        ]
    ) => {
        use std::collections::HashMap;
        use std::path::{Path, PathBuf};
        use $crate::utils::{render_template, create_tag_info};
        use $crate::models::{OperationInfo, OperationGroup};
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
                operations: &HashMap<Vec<String>, Vec<OperationGroup>>,
                output_dir: &Path,
            ) -> Result<()> {

                let tags: Vec<Vec<String>> = operations.keys().cloned().collect();

                // Handle per-tag template renders
                $(
                    for tag in &tags {
                        // Process operations once per tag with proper casing
                        let operations_with_converted_ids: Vec<OperationInfo> = operations[tag]
                            .iter()
                            .map(|op_group| {
                                let method_name = $operation_casing.convert_words(
                                    &op_group.metadata.normalized_operation_id,
                                );
                                let class_name = $class_casing.convert_words(
                                    &op_group.metadata.normalized_operation_id,
                                );
                                op_group
                                    .operation
                                    .clone()
                                    .with_casing(method_name, class_name)
                            })
                            .collect();

                        let tag_info = create_tag_info(tag, $class_casing, $import_casing, $variable_casing);
                        let context = OperationContext {
                            tag: tag_info,
                            operations: operations_with_converted_ids
                        };

                        $(
                            let tag_path = tag.join("_").to_lowercase();
                            let output_path = PathBuf::from(format!($path, tag_path));
                            let content = render_template(env, $template, &context)?;
                            let full_path = output_dir.join(&output_path);
                            std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                            std::fs::write(&full_path, content)?;
                        )*
                    }
                )*

                // Handle singleton template renders (once per SDK)
                let tag_infos: Vec<_> = tags.iter().map(|tag| create_tag_info(tag, $class_casing, $import_casing, $variable_casing)).collect();
                let tags_context = TagsContext {
                    tags: tag_infos,
                };

                $(
                    let output_path = PathBuf::from($s_path);
                    let content = render_template(env, $s_template, &tags_context)?;
                    let full_path = output_dir.join(&output_path);
                    std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                    std::fs::write(&full_path, content)?;
                )*

                // Generate test specifications with proper casing applied
                let operations_for_tests: HashMap<String, Vec<OperationInfo>> = operations
                    .iter()
                    .map(|(tag_vec, operation_groups)| {
                        let tag_string = tag_vec.join("_");
                        let operations_with_casing = operation_groups
                            .iter()
                            .map(|og| {
                                let method_name = $operation_casing.convert_words(&og.metadata.normalized_operation_id);
                                let class_name = $class_casing.convert_words(&og.metadata.normalized_operation_id);
                                og.operation.clone().with_casing(method_name, class_name)
                            })
                            .collect();
                        (tag_string, operations_with_casing)
                    })
                    .collect();

                let test_specs = $crate::testing::generate_test_specifications(&operations_for_tests)?;

                // Convert test specs to use Vec<String> keys to match our tag format
                let converted_test_specs: HashMap<Vec<String>, $crate::testing::TestSpecification> = test_specs
                    .iter()
                    .map(|(tag_string, spec)| {
                        let tag_vec: Vec<String> = tag_string.split('_').map(|s| s.to_string()).collect();
                        (tag_vec, spec.clone())
                    })
                    .collect();

                let test_tags: Vec<Vec<String>> = converted_test_specs.keys().cloned().collect();

                // Handle per-tag test template renders
                $(
                    for tag in &test_tags {
                        let tag_info = create_tag_info(tag, $class_casing, $import_casing, $variable_casing);
                        let tag_path = tag.join("_").to_lowercase();

                        if let Some(test_spec) = converted_test_specs.get(tag) {
                            let test_context = TestContext {
                                tag: tag_info.clone(),
                                test_spec: test_spec.clone(),
                            };

                            $(
                                if let Ok(_) = env.get_template($test_template) {
                                    // Special handling for pagination tests - only generate if there are valid pagination tests
                                    let should_generate = if $test_template == "test_pagination" {
                                        !test_spec.pagination_tests.is_empty() &&
                                        test_spec.pagination_tests.iter().any(|test|
                                            !test.method_name.is_empty()
                                        )
                                    } else {
                                        true
                                    };

                                    if should_generate {
                                        let output_path = PathBuf::from(format!($test_path, tag_path));
                                        let content = render_template(env, $test_template, &test_context)?;
                                        let full_path = output_dir.join(&output_path);
                                        std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                                        std::fs::write(&full_path, content)?;

                                        // Generate __init__.py for each tag test folder if it's in a subdirectory
                                        if let Some(parent) = full_path.parent() {
                                            if parent != output_dir {
                                                let init_path = parent.join("__init__.py");
                                                if !init_path.exists() {
                                                    std::fs::write(&init_path, "")?;
                                                }
                                            }
                                        }
                                    }
                                }
                            )*
                        }
                    }
                )*

                // Handle singleton test template renders (once per SDK)
                let test_tag_infos: Vec<_> = test_tags.iter().map(|tag| create_tag_info(tag, $class_casing, $import_casing, $variable_casing)).collect();
                let test_tags_context = TagsContext {
                    tags: test_tag_infos,
                };

                $(
                    if let Ok(_) = env.get_template($s_test_template) {
                        let output_path = PathBuf::from($s_test_path);
                        let content = render_template(env, $s_test_template, &test_tags_context)?;
                        let full_path = output_dir.join(&output_path);
                        std::fs::create_dir_all(full_path.parent().unwrap_or(output_dir))?;
                        std::fs::write(&full_path, content)?;
                    }
                )*

                Ok(())
            }
        }
    };
}
