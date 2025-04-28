use crate::error::{BuildError, Result};
use crate::utils::run_command; // Import from utils module
use crate::{log_error, log_info, log_success};
use colored::*;
use std::fs;
use std::path::Path;
use std::process::Command;
use xdk_gen::{Python, core::generator::SdkGenerator};
use xdk_openapi::OpenApi; // Add fs for directory removal

/// Generates the Python SDK.
pub fn generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Python SDK code...");
    let generator = SdkGenerator::new(Python);
    generator.generate(openapi, output_dir)?;
    log_success!("SDK code generated.");

    // Create and manage a single virtual environment for formatting
    let venv_path = output_dir.join(".venv");
    let python_executable = "python3.12"; // Assuming python3.12 is in PATH

    // 1. Create the virtual environment
    log_info!(
        "Creating Python virtual environment at: {}",
        venv_path.display().to_string().magenta()
    );
    let mut create_venv_cmd = Command::new(python_executable);
    create_venv_cmd.arg("-m").arg("venv").arg(&venv_path);
    run_command(&mut create_venv_cmd)?;
    log_success!("Virtual environment created successfully.");

    // Determine platform-specific paths within the venv
    let venv_python_path = venv_path.join("bin").join("python");
    let venv_bin_path = venv_path.join("bin");

    // 2. Install dependencies (black)
    let dependencies = fs::read_to_string(output_dir.join("requirements.txt"))?;
    let dependencies = dependencies.split("\n").collect::<Vec<&str>>();
    log_info!(
        "Installing {} using {}",
        dependencies.join(" and "),
        venv_python_path.display().to_string().magenta()
    );
    let mut install_deps_cmd = Command::new(&venv_python_path);
    install_deps_cmd
        .arg("-m")
        .arg("pip")
        .arg("install")
        .arg("-r")
        .arg(output_dir.join("requirements.txt"));
    run_command(&mut install_deps_cmd)?;
    log_success!("Formatting dependencies installed successfully.");

    // 3. Run black formatter
    let venv_black_path = venv_bin_path.join("black");
    run_black(output_dir, &venv_black_path)?;

    // 4. Run custom formatter
    // Assuming the build tool runs from the workspace root
    // Adjust this path if the execution context is different
    let script_path = Path::new("utils/python/format.py");
    run_formatter(output_dir, &venv_python_path, script_path)?;

    log_success!(
        "Successfully generated Python SDK in {}",
        output_dir.display().to_string().magenta()
    );
    Ok(())
}

// Run black using the provided virtual environment executable
fn run_black(output_dir: &Path, venv_black_path: &Path) -> Result<()> {
    log_info!(
        "Formatting code with black using {}",
        venv_black_path.display().to_string().magenta()
    );
    let mut run_black_cmd = Command::new(venv_black_path);
    run_black_cmd.arg(output_dir); // Format the entire output directory
    run_command(&mut run_black_cmd)?;
    log_success!("Black formatted successfully.");
    Ok(())
}

// Run the custom formatter script using the provided virtual environment Python
fn run_formatter(output_dir: &Path, venv_python_path: &Path, script_path: &Path) -> Result<()> {
    log_info!(
        "Running formatter script {} using {}",
        script_path.display().to_string().magenta(),
        venv_python_path.display().to_string().magenta()
    );
    let mut run_script_cmd = Command::new(venv_python_path);
    run_script_cmd.arg(script_path);
    run_script_cmd.arg(output_dir);

    // Execute the command and capture its output
    let output = run_command(&mut run_script_cmd)?;

    // Log stdout even on success if it's not empty
    let stdout = String::from_utf8_lossy(&output.stdout);
    if !stdout.trim().is_empty() {
        println!();
        stdout
            .split("\n")
            .collect::<Vec<&str>>()
            .into_iter()
            .for_each(|line| {
                let parts = line.split(" ").collect::<Vec<&str>>();
                if parts.len() == 2 {
                    log_info!("{} {}", parts[0], parts[1].magenta());
                }
            });
        println!();
    }

    log_success!("Formatter script executed successfully.");
    Ok(())
}
