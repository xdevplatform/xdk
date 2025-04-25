// Allow unused imports for now, as we'll add more commands later
#![allow(unused_imports)]

// Declare modules
mod error;
mod logging;
mod python;
mod utils;

use crate::error::{BuildError, Result};

use clap::{Parser, Subcommand};
use std::path::{Path, PathBuf};
use xdk_gen::core::SdkGeneratorError;
use xdk_openapi::{OpenApiContextGuard, parse_json_file, parse_yaml_file};

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Generate a Python SDK from an OpenAPI specification
    Python {
        /// Path to the OpenAPI specification file
        #[arg(short, long)]
        spec: PathBuf,

        /// Output directory for the generated SDK
        #[arg(short, long, default_value = "xdk/python")]
        output: PathBuf,
    },
    // Add other language commands here later
}

fn main() -> Result<()> {
    // Initialize logging (Assuming a setup function exists in logging module)
    // logging::setup_logger().map_err(|e| BuildError::Other(format!("Failed to setup logger: {}", e)))?;

    let cli = Cli::parse();

    // Initialize OpenApi context once
    let _guard = OpenApiContextGuard::new();

    match cli.command {
        Commands::Python { spec, output } => {
            let extension = spec
                .extension()
                .and_then(|ext| ext.to_str())
                // Use map_err to convert Option error to BuildError
                .ok_or_else(|| BuildError::CommandFailed("Invalid file extension".to_string()))?;

            // Assuming log_info! and log_error! are globally available or macros
            // log_info!("Parsing OpenAPI spec: {}", spec.display());

            let openapi = match extension {
                "yaml" | "yml" => parse_yaml_file(spec.to_str().unwrap())
                    // Convert xdk_openapi::OpenApiError via xdk_gen::SdkGeneratorError to BuildError
                    .map_err(|e| SdkGeneratorError::from(e.to_string()))?,
                "json" => parse_json_file(spec.to_str().unwrap())
                    // Convert xdk_openapi::OpenApiError via xdk_gen::SdkGeneratorError to BuildError
                    .map_err(|e| SdkGeneratorError::from(e.to_string()))?,
                _ => {
                    let err_msg = format!("Unsupported file extension: {}", extension);
                    // log_error!("{}", err_msg);
                    // Return specific BuildError variant if desired, otherwise use CommandFailed or Other
                    return Err(BuildError::CommandFailed(err_msg));
                }
            };

            // log_info!("Specification parsed successfully.");

            // Call the generate method - `?` handles the Result conversion
            python::generate(&openapi, &output)?;
        }
    }

    Ok(())
}
