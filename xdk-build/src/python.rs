use crate::error::{BuildError, Result};
use crate::utils::run_command; // Import from utils module
use colored::*;
use std::fs;
use std::path::Path;
use std::process::Command;
use xdk_gen::Python;
use xdk_lib::{log_error, log_info, log_success};
use xdk_openapi::OpenApi; // Add fs for directory removal

/// Generates the Python SDK.
pub fn generate(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating Python SDK code...");

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
    if let Err(e) = xdk_lib::generator::generate(Python, openapi, output_dir) {
        log_error!("Failed to generate Python SDK code: {}", e);
        return Err(BuildError::SdkGenError(e));
    }
    log_success!("SDK code generated.");

    // Create and manage a single virtual environment for formatting using uv
    let venv_path = output_dir.join(".venv");

    // 1. Create the virtual environment using uv
    log_info!(
        "Creating Python virtual environment with uv at: {}",
        venv_path.display().to_string().magenta()
    );
    let mut create_venv_cmd = Command::new("uv");
    create_venv_cmd.arg("venv").arg(&venv_path);
    run_command(&mut create_venv_cmd)?;
    log_success!("Virtual environment created successfully.");

    // Determine platform-specific paths within the venv
    let venv_python_path = venv_path.join("bin").join("python");
    let venv_bin_path = venv_path.join("bin");

    // Verify the virtual environment was created properly
    if !venv_python_path.exists() {
        log_error!(
            "Virtual environment Python executable not found at: {}",
            venv_python_path.display()
        );
        log_error!("This might indicate the virtual environment creation failed silently.");
        return Err(BuildError::CommandFailed(
            "Virtual environment Python executable not found".to_string(),
        ));
    }

    // 2. Install dependencies using uv from pyproject.toml
    log_info!("Installing dev dependencies from pyproject.toml using uv");

    // Verify pyproject.toml exists
    let pyproject_path = output_dir.join("pyproject.toml");
    if !pyproject_path.exists() {
        log_error!("pyproject.toml not found at: {}", pyproject_path.display());
        log_error!("This indicates the SDK generation may have failed.");
        return Err(BuildError::CommandFailed(
            "pyproject.toml file not found after SDK generation".to_string(),
        ));
    }

    let mut install_deps_cmd = Command::new("uv");
    install_deps_cmd
        .arg("pip")
        .arg("install")
        .arg("-e")
        .arg(".[dev]")
        .arg("--python")
        .arg(".venv/bin/python") // Use relative path since we're changing current_dir
        .current_dir(output_dir);
    run_command(&mut install_deps_cmd)?;
    log_success!("Development dependencies installed successfully.");

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
    // Verify black executable exists
    if !venv_black_path.exists() {
        log_error!(
            "Black formatter not found at: {}",
            venv_black_path.display()
        );
        log_error!("This might indicate the dev dependencies installation failed.");
        return Err(BuildError::CommandFailed(
            "Black formatter executable not found in virtual environment".to_string(),
        ));
    }

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
    // Verify the formatter script exists
    if !script_path.exists() {
        log_error!("Formatter script not found at: {}", script_path.display());
        log_error!("Expected to find the script at: {}", script_path.display());
        return Err(BuildError::CommandFailed(
            "Custom formatter script not found".to_string(),
        ));
    }

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