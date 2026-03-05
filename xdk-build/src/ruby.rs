use crate::error::{BuildError, Result};
use colored::*;
use std::path::Path;
use std::process::Command;
use xdk_gen::Ruby;
use xdk_lib::{XdkConfig, log_error, log_info, log_success};
use xdk_openapi::OpenApi;

/// Generates the Ruby SDK.
pub fn generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Ruby SDK code...");

    // Load configuration to get version
    let config = XdkConfig::load_default().map_err(BuildError::SdkGenError)?;
    let version = config.get_version("ruby").ok_or_else(|| {
        BuildError::SdkGenError(xdk_lib::SdkGeneratorError::FrameworkError(
            "Ruby version not found in config".to_string(),
        ))
    })?;

    // Create output directory if it doesn't exist
    if let Err(e) = std::fs::create_dir_all(output_dir) {
        log_error!(
            "Failed to create output directory '{}': {}",
            output_dir.display(),
            e
        );
        return Err(BuildError::IoError(e));
    }

    // Generate the SDK code
    if let Err(e) = xdk_lib::generator::generate(Ruby, openapi, output_dir, version) {
        log_error!("Failed to generate Ruby SDK code: {}", e);
        return Err(BuildError::SdkGenError(e));
    }
    log_success!("SDK code generated.");

    // Optionally run rubocop for formatting (if available)
    if which_exists("rubocop") {
        log_info!("Formatting code with rubocop...");
        let mut fmt_cmd = Command::new("rubocop");
        fmt_cmd.arg("-a").arg(output_dir);
        // Best-effort formatting; don't fail the build if rubocop isn't configured
        let _ = fmt_cmd.output();
        log_success!("Rubocop formatting complete.");
    }

    log_success!(
        "Successfully generated Ruby SDK in {}",
        output_dir.display().to_string().magenta()
    );
    Ok(())
}

fn which_exists(cmd: &str) -> bool {
    Command::new("which")
        .arg(cmd)
        .output()
        .map(|o| o.status.success())
        .unwrap_or(false)
}
