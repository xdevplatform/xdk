use anyhow::Result;
use clap::{Parser, Subcommand};
use std::path::PathBuf;
use xdk_gen::{generate_python_sdk, SdkResult, SdkGeneratorError};
use xdk_openapi::{parse_yaml_file, parse_json_file, OpenApiContextGuard};

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
}

fn main() -> Result<()> {
    let cli = Cli::parse();

    match cli.command {
        Commands::Python { spec, output } => {
            generate_python(&spec, &output)?;
        }
    }

    Ok(())
}

fn generate_python(spec_path: &PathBuf, output_dir: &PathBuf) -> SdkResult<()> {
    // Determine the file extension
    let extension = spec_path.extension()
        .and_then(|ext| ext.to_str())
        .ok_or_else(|| SdkGeneratorError::from("Invalid file extension"))?;
    
    let _guard = OpenApiContextGuard::new();
    // Parse the OpenAPI specification based on the file extension
    let openapi = match extension {
        "yaml" | "yml" => {
            parse_yaml_file(spec_path.to_str().unwrap())
                .map_err(|e| SdkGeneratorError::from(e.to_string()))?
        },
        "json" => {
            parse_json_file(spec_path.to_str().unwrap())
                .map_err(|e| SdkGeneratorError::from(e.to_string()))?
        },
        _ => return Err(SdkGeneratorError::from(format!("Unsupported file extension: {}", extension))),
    };

    // Generate the Python SDK
    generate_python_sdk(&openapi, output_dir)?;

    println!("Successfully generated Python SDK in {}", output_dir.display());
    Ok(())
}
