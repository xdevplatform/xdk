// Allow unused imports for now, as we'll add more commands later
#![allow(unused_imports)]

// Declare modules
mod error;
mod python;
mod utils;

use crate::error::{BuildError, Result};

use clap::{Parser, Subcommand};
use std::path::{Path, PathBuf};
use xdk_lib::{SdkGeneratorError, log_info};
use xdk_openapi::{OpenApiContextGuard, parse_json, parse_json_file, parse_yaml_file};

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
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,

        /// Output directory for the generated SDK
        #[arg(short, long, default_value = "xdk/python")]
        output: PathBuf,
    },
    /// List all clients and their methods from an OpenAPI specification
    List {
        /// Path to the OpenAPI specification file
        #[arg(short, long)]
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,
    },
    // Add other language commands here later
}

#[tokio::main]
async fn main() -> Result<()> {
    let cli = Cli::parse();

    // Initialize OpenApi context once
    let _guard = OpenApiContextGuard::new();

    let result = match cli.command {
        Commands::Python {
            spec,
            output,
            latest,
        } => {
            let openapi = parse_openapi_spec(spec, latest).await?;
            log_info!("Specification parsed successfully.");

            // Call the generate method - `?` handles the Result conversion
            python::generate(&openapi, &output)
        }
        Commands::List { spec, latest } => {
            let openapi = parse_openapi_spec(spec, latest).await?;
            log_info!("Specification parsed successfully.");

            // List clients and methods
            list_clients_and_methods(&openapi)
        }
    };

    // Handle the result with better error messaging
    if let Err(ref error) = result {
        use xdk_lib::log_error;
        match error {
            BuildError::IoError(io_error) => match io_error.kind() {
                std::io::ErrorKind::NotFound => {
                    log_error!("Command or file not found. This might be because:");
                    log_error!("  • 'uv' is not installed (install with: pip install uv)");
                    log_error!("  • A required file was not generated properly");
                    log_error!("  • Path does not exist");
                    log_error!("Original error: {}", io_error);
                }
                std::io::ErrorKind::PermissionDenied => {
                    log_error!("Permission denied. Please check file/directory permissions.");
                    log_error!("Original error: {}", io_error);
                }
                _ => {
                    log_error!("File system error occurred: {}", io_error);
                }
            },
            BuildError::CommandFailed(msg) => {
                log_error!("Command execution failed: {}", msg);
            }
            BuildError::FormatterFailed(msg) => {
                log_error!("Code formatting failed: {}", msg);
            }
            BuildError::SdkGenError(msg) => {
                log_error!("SDK generation failed: {}", msg);
            }
        }
        std::process::exit(1);
    }

    result
}

/// Parse OpenAPI specification from file or fetch latest
async fn parse_openapi_spec(
    spec: Option<PathBuf>,
    latest: Option<bool>,
) -> Result<xdk_openapi::OpenApi> {
    if latest == Some(true) {
        // Fetch the latest OpenAPI spec from api.x.com
        let client = reqwest::Client::new();
        let response = client
            .get("https://api.x.com/2/openapi.json")
            .send()
            .await
            .map_err(|e| {
                BuildError::CommandFailed(format!("Failed to fetch OpenAPI spec: {}", e))
            })?;

        let json_text = response.text().await.map_err(|e| {
            BuildError::CommandFailed(format!("Failed to read response: {}", e))
        })?;

        parse_json(&json_text)
            .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string())))
    } else {
        // Parse from local file
        let spec_path = spec.ok_or_else(|| {
            BuildError::CommandFailed("Spec file is required when not using --latest".to_string())
        })?;

        let extension = spec_path
            .extension()
            .and_then(|ext| ext.to_str())
            .ok_or_else(|| {
                BuildError::CommandFailed("Invalid file extension".to_string())
            })?;

        match extension {
            "yaml" | "yml" => parse_yaml_file(spec_path.to_str().unwrap())
                .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string()))),
            "json" => parse_json_file(spec_path.to_str().unwrap())
                .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string()))),
            _ => {
                let err_msg = format!("Unsupported file extension: {}", extension);
                Err(BuildError::CommandFailed(err_msg))
            }
        }
    }
}

/// List all clients and their methods from the OpenAPI specification
fn list_clients_and_methods(openapi: &xdk_openapi::OpenApi) -> Result<()> {
    use xdk_lib::utils::extract_operations_by_tag;
    use xdk_lib::{log_info, log_success};

    log_info!("Extracting operations by tag...");
    
    let operations_by_tag = extract_operations_by_tag(openapi)
        .map_err(|e| BuildError::SdkGenError(e))?;

    log_success!("Found {} client(s):", operations_by_tag.len());
    println!();

    for (tag, operations) in operations_by_tag.iter() {
        println!("📦 {}Client", tag);
        println!("   Methods:");
        
        for operation in operations {
            println!("   • {} ({} {})", 
                operation.operation_id, 
                operation.method.to_uppercase(), 
                operation.path
            );
        }
        println!();
    }

    Ok(())
}
