use crate::error::{BuildError, Result};
use std::path::Path;
use xdk_gen::TypeScript;
use xdk_lib::{log_info, generate};
use xdk_openapi::OpenApi;

/// Generate TypeScript SDK from OpenAPI spec
pub fn generate_typescript(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating TypeScript SDK...");
    std::fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    // Initialize TypeScript generator
    let generator = TypeScript;

    // Generate the SDK
    generate(generator, openapi, output_dir).map_err(BuildError::SdkGenError)?;

    // Format generated TypeScript files with Prettier
    log_info!("Formatting generated TypeScript files with Prettier...");
    format_typescript_files(output_dir)?;

    // Try to install dependencies and build, but don't fail if it doesn't work
    if let Err(e) = install_dependencies(output_dir) {
        log_info!("Warning: Could not install dependencies: {}", e);
        log_info!("You may need to run 'npm install' manually");
    } else if let Err(e) = build_sdk(output_dir) {
        log_info!("Warning: Could not build SDK: {}", e);
        log_info!("You may need to run 'npm run build' manually");
    }

    log_info!("TypeScript SDK generated successfully!");
    log_info!("To complete setup, run:");
    log_info!("  cd {}", output_dir.display());
    log_info!("  npm install");
    log_info!("  npm run build");
    Ok(())
}

fn format_typescript_files(output_dir: &Path) -> Result<()> {
    use std::fs;
    use std::path::PathBuf;

    fn process_directory(dir: &Path) -> Result<()> {
        for entry in fs::read_dir(dir).map_err(BuildError::IoError)? {
            let entry = entry.map_err(BuildError::IoError)?;
            let path = entry.path();

            // Skip node_modules directory
            if path.file_name().map_or(false, |name| name == "node_modules") {
                continue;
            }

            if path.is_dir() {
                process_directory(&path)?;
            } else if let Some(extension) = path.extension() {
                if extension == "ts" || extension == "js" {
                    // Only format files in src directory
                    if path.to_string_lossy().contains("/src/") {
                        // Try to format with Prettier if available
                        if let Err(e) = format_file_with_prettier(&path) {
                            log_info!("Warning: Could not format {} with Prettier: {}", path.display(), e);
                            log_info!("You may need to install Prettier: npm install -g prettier");
                        }
                    }
                }
            }
        }
        Ok(())
    }

    process_directory(output_dir)
}

fn format_file_with_prettier(file_path: &Path) -> Result<()> {
    let status = std::process::Command::new("prettier")
        .arg("--write")
        .arg(file_path)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to run Prettier: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Prettier formatting failed".to_string()))
    }
}

fn install_dependencies(output_dir: &Path) -> Result<()> {
    log_info!("Installing dependencies...");

    let status = std::process::Command::new("npm")
        .arg("install")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to install dependencies: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Failed to install dependencies".to_string()))
    }
}

fn build_sdk(output_dir: &Path) -> Result<()> {
    log_info!("Building TypeScript SDK...");

    let status = std::process::Command::new("npm")
        .arg("run")
        .arg("build")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to build SDK: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Failed to build SDK".to_string()))
    }
} 