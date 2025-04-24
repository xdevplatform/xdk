use minijinja::Environment;
use std::collections::HashMap;
use std::path::Path;

use super::models::{ClientClassContext, ClientModuleContext, MainClientContext};
use crate::core::Result;
use crate::core::generator::LanguageGenerator;
use crate::core::models::OperationInfo;
use crate::define_generator;

/// MiniJinja filter for converting a string to snake_case
fn snake_case(value: &str) -> String {
    let chars = value.chars();
    let mut result = String::new();
    let mut prev_is_underscore = false;

    for c in chars {
        if c.is_uppercase() {
            if !result.is_empty() && !prev_is_underscore {
                result.push('_');
            }
            result.push(c.to_ascii_lowercase());
            prev_is_underscore = false;
        } else if c.is_alphanumeric() {
            result.push(c.to_ascii_lowercase());
            prev_is_underscore = false;
        } else if !prev_is_underscore {
            result.push('_');
            prev_is_underscore = true;
        }
    }

    result.trim_matches('_').to_string()
}

/// MiniJinja filter for converting to Python types
fn python_type(value: &str) -> String {
    let python_type = match value {
        "string" => "str",
        "integer" => "int",
        "number" => "float",
        "boolean" => "bool",
        "array" => "List",
        "object" => "Dict[str, Any]",
        _ => "Any",
    };
    python_type.to_string()
}

define_generator! {
    PythonGenerator {
        name: "python",
        templates: [
            ("python/client_module.j2", include_str!("../../templates/python/client_module.j2")),
            ("python/client_class.j2", include_str!("../../templates/python/client_class.j2")),
            ("python/main_client.j2", include_str!("../../templates/python/main_client.j2")),
            ("python/init_py.j2", include_str!("../../templates/python/init_py.j2")),
            ("python/setup_py.j2", include_str!("../../templates/python/setup_py.j2")),
            ("python/readme.j2", include_str!("../../templates/python/readme.j2")),
            ("python/requirements_txt.j2", include_str!("../../templates/python/requirements_txt.j2"))
        ],
        filters: [snake_case, python_type],
        generate: |env, operations, output_dir| {
            use crate::core::utils::render_template;
            use std::fs;

            // Create the package directory
            let package_dir = output_dir.join("xdk");
            fs::create_dir_all(&package_dir)?;

            // Generate the client modules for each tag
            for (tag, operations) in operations {
                // Convert tag to snake_case for file names
                let tag_snake_case = tag.replace(" ", "_").to_lowercase();

                // Create a directory for this tag
                let tag_dir = package_dir.join(&tag_snake_case);
                fs::create_dir_all(&tag_dir)?;

                // Create the client module file
                let client_module_path = tag_dir.join("__init__.py");
                let client_module_content = render_template(env, "python/client_module.j2", &ClientModuleContext {
                    tag: tag.to_string(),
                    operations: operations.to_vec(),
                })?;
                fs::write(&client_module_path, client_module_content)?;

                // Create the client class file
                let client_class_path = tag_dir.join("client.py");
                let client_class_content = render_template(env, "python/client_class.j2", &ClientClassContext {
                    tag: tag.to_string(),
                    operations: operations.to_vec(),
                })?;
                fs::write(&client_class_path, client_class_content)?;
            }

            // Generate the main client file
            let main_client_path = package_dir.join("client.py");
            let main_client_content = render_template(env, "python/main_client.j2", &MainClientContext {
                tags: operations.keys().cloned().collect::<Vec<_>>(),
            })?;
            fs::write(&main_client_path, main_client_content)?;

            // Generate the __init__.py file
            let init_py_path = package_dir.join("__init__.py");
            let init_py_content = render_template(env, "python/init_py.j2", &())?;
            fs::write(&init_py_path, init_py_content)?;

            // Generate the setup.py file
            let setup_py_path = output_dir.join("setup.py");
            let setup_py_content = render_template(env, "python/setup_py.j2", &())?;
            fs::write(&setup_py_path, setup_py_content)?;

            // Generate the README.md file
            let readme_path = output_dir.join("README.md");
            let readme_content = render_template(env, "python/readme.j2", &())?;
            fs::write(&readme_path, readme_content)?;

            // Generate the requirements.txt file
            let requirements_txt_path = output_dir.join("requirements.txt");
            let requirements_txt_content = render_template(env, "python/requirements_txt.j2", &())?;
            fs::write(&requirements_txt_path, requirements_txt_content)?;

            Ok(())
        }
    }
}
