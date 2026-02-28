use crate::error::{BuildError, Result};
use std::path::Path;
use xdk_gen::Elixir;
use xdk_lib::{XdkConfig, generate as generate_sdk, log_info, log_success};
use xdk_openapi::OpenApi;

pub fn generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Elixir SDK...");
    std::fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    let config = XdkConfig::load_default().map_err(BuildError::SdkGenError)?;
    let version = config.get_version("elixir").ok_or_else(|| {
        BuildError::SdkGenError(xdk_lib::SdkGeneratorError::FrameworkError(
            "Elixir version not found in config".to_string(),
        ))
    })?;

    generate_sdk(Elixir, openapi, output_dir, version).map_err(BuildError::SdkGenError)?;

    log_info!("Formatting generated Elixir files...");
    let status = std::process::Command::new("mix")
        .arg("format")
        .current_dir(output_dir)
        .status();

    match status {
        Ok(s) if s.success() => log_success!("Elixir SDK formatted."),
        _ => log_info!("Warning: mix format not available, skipping formatting"),
    }

    log_success!("Elixir SDK generated in {}", output_dir.display());
    Ok(())
}
