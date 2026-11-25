#![allow(unused_imports)]

mod csharp;
mod docs;
mod error;
mod java;
mod python;
mod typescript;
mod utils;

use crate::error::{BuildError, Result};

use clap::{Parser, Subcommand};
use std::path::{Path, PathBuf};
use xdk_lib::{SdkGeneratorError, log_info};
use xdk_openapi::{OpenApi, OpenApiContextGuard, parse_json, parse_json_file, parse_yaml_file};

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
    /// Generate a TypeScript SDK from an OpenAPI specification
    #[command(name = "typescript")]
    TypeScript {
        /// Path to the OpenAPI specification file
        #[arg(short, long)]
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,

        /// Output directory for the generated SDK
        #[arg(short, long, default_value = "xdk/typescript")]
        output: PathBuf,
    },
    /// Generate a Java SDK from an OpenAPI specification
    #[command(name = "java")]
    Java {
        /// Path to the OpenAPI specification file
        #[arg(short, long)]
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,

        /// Output directory for the generated SDK
        #[arg(short, long, default_value = "xdk/java")]
        output: PathBuf,
    },
    /// Generate a C# SDK from an OpenAPI specification
    #[command(name = "csharp")]
    CSharp {
        /// Path to the OpenAPI specification file
        #[arg(short, long)]
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,

        /// Output directory for the generated SDK
        #[arg(short, long, default_value = "xdk/csharp")]
        output: PathBuf,
    },
    /// Generate Mintlify SDK reference MDX, OpenAPI Overlay code samples, and docs.json navigation
    #[command(name = "docs")]
    Docs {
        /// Path to the OpenAPI specification file (defaults to <output>/openapi.json if present)
        #[arg(short, long)]
        spec: Option<PathBuf>,

        #[arg(short, long)]
        latest: Option<bool>,

        /// Output directory (e.g. path to xdevplatform/docs checkout)
        #[arg(short, long, default_value = "xdk/docs")]
        output: PathBuf,

        /// Create minimal MDX endpoint stubs under x-api/ for operations not yet present
        #[arg(long, default_value_t = false)]
        sync_endpoint_stubs: bool,
    },
}

async fn load_openapi_spec(spec: Option<PathBuf>, latest: Option<bool>) -> Result<OpenApi> {
    if latest == Some(true) {
        let client = reqwest::Client::new();
        let response = client
            .get("https://api.x.com/2/openapi.json")
            .send()
            .await
            .map_err(|e| {
                BuildError::CommandFailed(format!("Failed to fetch OpenAPI spec: {}", e))
            })?;

        let json_text = response
            .text()
            .await
            .map_err(|e| BuildError::CommandFailed(format!("Failed to read response: {}", e)))?;

        parse_json(&json_text)
            .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string())))
    } else {
        let spec_path = spec.ok_or_else(|| {
            BuildError::CommandFailed(
                "Either `--spec <path>` or `--latest true` must be provided".to_string(),
            )
        })?;
        let extension = spec_path
            .extension()
            .and_then(|ext| ext.to_str())
            .ok_or_else(|| BuildError::CommandFailed("Invalid file extension".to_string()))?;

        let path_str = spec_path.to_str().ok_or_else(|| {
            BuildError::CommandFailed("Invalid UTF-8 path for OpenAPI spec".to_string())
        })?;

        match extension {
            "yaml" | "yml" => parse_yaml_file(path_str)
                .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string()))),
            "json" => parse_json_file(path_str)
                .map_err(|e| BuildError::SdkGenError(SdkGeneratorError::from(e.to_string()))),
            _ => Err(BuildError::CommandFailed(format!(
                "Unsupported file extension: {}",
                extension
            ))),
        }
    }
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
        } => load_openapi_spec(spec, latest).await.and_then(|openapi| {
            log_info!("Specification parsed successfully.");
            python::generate(&openapi, &output)
        }),
        Commands::TypeScript {
            spec,
            output,
            latest,
        } => load_openapi_spec(spec, latest).await.and_then(|openapi| {
            log_info!("Specification parsed successfully.");
            typescript::generate(&openapi, &output)
        }),
        Commands::Java {
            spec,
            output,
            latest,
        } => load_openapi_spec(spec, latest).await.and_then(|openapi| {
            log_info!("Specification parsed successfully.");
            java::generate(&openapi, &output)
        }),
        Commands::CSharp {
            spec,
            output,
            latest,
        } => load_openapi_spec(spec, latest).await.and_then(|openapi| {
            log_info!("Specification parsed successfully.");
            csharp::generate(&openapi, &output)
        }),
        Commands::Docs {
            spec,
            output,
            latest,
            sync_endpoint_stubs,
        } => {
            let resolved_spec = spec.or_else(|| {
                let candidate = output.join("openapi.json");
                candidate.exists().then_some(candidate)
            });
            load_openapi_spec(resolved_spec, latest)
                .await
                .and_then(|openapi| {
                    log_info!("Specification parsed successfully.");
                    docs::generate(&openapi, &output, sync_endpoint_stubs)
                })
        }
    };

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
