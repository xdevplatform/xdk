use anyhow::Result;
use clap::{Parser, Subcommand};
use std::path::PathBuf;
use xdk_gen::{generate_python_sdk, SdkResult, SdkGeneratorError};
use xdk_openapi::OpenApi;

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Generate a Python SDK from an OpenAPI specification
    GeneratePython {
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
        Commands::GeneratePython { spec, output } => {
            generate_python(&spec, &output)?;
        }
    }

    Ok(())
}

fn generate_python(spec_path: &PathBuf, output_dir: &PathBuf) -> SdkResult<()> {
    // Read and parse the OpenAPI specification
    let spec_content = std::fs::read_to_string(spec_path)?;
    let openapi: OpenApi = serde_json::from_str(&spec_content)
        .map_err(|e| SdkGeneratorError::from(e.to_string()))?;

    // Generate the Python SDK
    generate_python_sdk(&openapi, output_dir)?;

    println!("Successfully generated Python SDK in {}", output_dir.display());
    Ok(())
}
