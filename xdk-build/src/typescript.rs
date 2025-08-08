use crate::error::{BuildError, Result};
use std::path::Path;
use xdk_gen::TypeScript;
use xdk_lib::{log_info, generate};
use xdk_openapi::OpenApi;

/// Generate TypeScript SDK from OpenAPI spec
pub fn generate_typescript(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating TypeScript SDK...");

    // Create output directory if it doesn't exist
    std::fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    // Initialize TypeScript generator
    let generator = TypeScript;

    // Generate the SDK
    generate(generator, openapi, output_dir).map_err(BuildError::SdkGenError)?;

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

/// Install npm dependencies
fn install_dependencies(output_dir: &Path) -> Result<()> {
    log_info!("Installing dependencies...");

    let status = std::process::Command::new("npm")
        .arg("install")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to install dependencies: {}", e)))?;

    if !status.success() {
        return Err(BuildError::CommandFailed(
            "Failed to install dependencies".to_string(),
        ));
    }

    Ok(())
}

/// Build the TypeScript SDK
fn build_sdk(output_dir: &Path) -> Result<()> {
    log_info!("Building TypeScript SDK...");

    let status = std::process::Command::new("npm")
        .arg("run")
        .arg("build")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to build SDK: {}", e)))?;

    if !status.success() {
        return Err(BuildError::CommandFailed("Failed to build SDK".to_string()));
    }

    Ok(())
} 