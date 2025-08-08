use crate::error::{BuildError, Result};
use std::path::Path;
use xdk_gen::Python;
use xdk_lib::{log_info, generate};
use xdk_openapi::OpenApi;

/// Generate Python SDK from OpenAPI spec
pub fn generate_python(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Python SDK...");
    std::fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    // Initialize Python generator
    let generator = Python;

    // Generate the SDK
    generate(generator, openapi, output_dir).map_err(BuildError::SdkGenError)?;

    // Format generated Python files with Black
    log_info!("Formatting generated Python files with Black...");
    format_python_files(output_dir)?;

    log_info!("Python SDK generated successfully!");
    Ok(())
}

fn format_python_files(output_dir: &Path) -> Result<()> {
    use std::fs;
    use std::path::PathBuf;

    fn process_directory(dir: &Path) -> Result<()> {
        for entry in fs::read_dir(dir).map_err(BuildError::IoError)? {
            let entry = entry.map_err(BuildError::IoError)?;
            let path = entry.path();

            if path.is_dir() {
                process_directory(&path)?;
            } else if let Some(extension) = path.extension() {
                if extension == "py" {
                    // Try to format with Black if available
                    if let Err(e) = format_file_with_black(&path) {
                        log_info!("Warning: Could not format {} with Black: {}", path.display(), e);
                        log_info!("You may need to install Black: pip install black");
                    }
                }
            }
        }
        Ok(())
    }

    process_directory(output_dir)
}

fn format_file_with_black(file_path: &Path) -> Result<()> {
    let status = std::process::Command::new("black")
        .arg("--quiet")
        .arg(file_path)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to run Black: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Black formatting failed".to_string()))
    }
}
