use crate::SdkGenerator;
use crate::error::Result;
use openapi::OpenApi;
use std::fs;
use std::path::Path;

use super::render::Renderer;
use super::utils::extract_operations_by_tag;

/// Python SDK generator
pub struct PythonSdkGenerator;

impl PythonSdkGenerator {
    /// Create a new Python SDK generator
    pub fn new() -> Self {
        PythonSdkGenerator
    }
}

impl SdkGenerator for PythonSdkGenerator {
    fn generate(&self, openapi: &OpenApi, output_dir: &Path) -> Result<()> {
        // Create the output directory if it doesn't exist
        fs::create_dir_all(output_dir)?;
        
        // Create the renderer
        let renderer = Renderer::new()?;
        
        // Extract operations by tag
        let operations_by_tag = extract_operations_by_tag(openapi)?;
        
        // Create the package directory
        let package_dir = output_dir.join("xdk");
        fs::create_dir_all(&package_dir)?;
        
        // Generate the client modules for each tag
        for (tag, operations) in &operations_by_tag {
            // Create the client module file
            let client_module_path = package_dir.join(format!("{}.py", tag.to_lowercase()));
            let client_module_content = renderer.generate_client_module(tag, operations);
            fs::write(&client_module_path, client_module_content)?;
            
            // Create the client class file
            let client_class_path = package_dir.join(format!("{}_client.py", tag.to_lowercase()));
            let client_class_content = renderer.generate_client_class(tag, operations);
            fs::write(&client_class_path, client_class_content)?;
        }
        
        // Generate the main client file
        let main_client_path = package_dir.join("client.py");
        let main_client_content = renderer.generate_main_client(&operations_by_tag.keys().cloned().collect::<Vec<_>>());
        fs::write(&main_client_path, main_client_content)?;
        
        // Generate the __init__.py file
        let init_py_path = package_dir.join("__init__.py");
        let init_py_content = renderer.generate_init_py();
        fs::write(&init_py_path, init_py_content)?;
        
        // Generate the setup.py file
        let setup_py_path = output_dir.join("setup.py");
        let setup_py_content = renderer.generate_setup_py();
        fs::write(&setup_py_path, setup_py_content)?;
        
        // Generate the README.md file
        let readme_path = output_dir.join("README.md");
        let readme_content = renderer.generate_readme();
        fs::write(&readme_path, readme_content)?;
        
        // Generate the requirements.txt file
        let requirements_txt_path = output_dir.join("requirements.txt");
        let requirements_txt_content = renderer.generate_requirements_txt();
        fs::write(&requirements_txt_path, requirements_txt_content)?;
        
        Ok(())
    }

    fn name(&self) -> &str {
        "python"
    }
} 