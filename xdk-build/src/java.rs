use crate::error::{BuildError, Result};
use std::fs;
use std::path::Path;
use xdk_gen::Java;
use xdk_lib::{XdkConfig, generate as generate_sdk, log_info, log_success};
use xdk_openapi::OpenApi;

/// Generate Java SDK from OpenAPI spec
pub fn generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Java SDK...");
    clean_generated_dirs(output_dir)?;
    fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    let config = XdkConfig::load_default().map_err(BuildError::SdkGenError)?;
    let version = config.get_version("java").ok_or_else(|| {
        BuildError::SdkGenError(xdk_lib::SdkGeneratorError::FrameworkError(
            "Java version not found in config".to_string(),
        ))
    })?;

    generate_sdk(Java, openapi, output_dir, version).map_err(BuildError::SdkGenError)?;

    log_success!(
        "Java SDK generated successfully in {}!",
        output_dir.display()
    );
    log_info!("To build and test, run:");
    log_info!("  cd {} && mvn test", output_dir.display());
    Ok(())
}

fn clean_generated_dirs(output_dir: &Path) -> Result<()> {
    let path = output_dir.join("src");
    if path.exists() {
        fs::remove_dir_all(&path).map_err(BuildError::IoError)?;
    }
    Ok(())
}
