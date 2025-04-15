// Allow unused imports for now, as we'll add more commands later
#![allow(unused_imports)]

// Declare modules
mod logging;
mod python;
mod generator;
mod utils;

use clap::{Parser, Subcommand};
use std::path::{Path, PathBuf};
use xdk_gen::{Result, SdkGeneratorError}; 
use xdk_openapi::{OpenApiContextGuard, parse_json_file, parse_yaml_file};

// Import the generator trait and the specific Python generator
use generator::LanguageGenerator;
use python::PythonGenerator;

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
    let cli = Cli::parse();

    // Initialize OpenApi context once
    let _guard = OpenApiContextGuard::new(); 

    match cli.command {
        Commands::Python { spec, output } => {
            // Determine the file extension
            let extension = spec
                .extension()
                .and_then(|ext| ext.to_str())
                .ok_or_else(|| SdkGeneratorError::from("Invalid file extension"))?;
            
            log_info!("Parsing OpenAPI spec: {}", spec.display());

            // Parse the OpenAPI specification based on the file extension
            let openapi = match extension {
                "yaml" | "yml" => parse_yaml_file(spec.to_str().unwrap())
                    .map_err(|e| SdkGeneratorError::from(e.to_string()))?,
                "json" => parse_json_file(spec.to_str().unwrap())
                    .map_err(|e| SdkGeneratorError::from(e.to_string()))?,
                _ => {
                    let err_msg = format!("Unsupported file extension: {}", extension);
                    log_error!("{}", err_msg);
                    return Err(SdkGeneratorError::from(err_msg));
                }
            };
            
            log_info!("Specification parsed successfully.");

            // Create a Python generator instance
            let python_generator = PythonGenerator::default();

            // Call the generate method
            python_generator.generate(&openapi, &output)?;
        }
        // Handle other commands here
    }

    Ok(())
}