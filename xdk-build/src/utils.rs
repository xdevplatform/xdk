use crate::error::{BuildError, Result};
use colored::*;
use std::process::{Command, Output};
use xdk_lib::{log_error, log_info};

/// Helper function to run a command and check its status
pub fn run_command(cmd: &mut Command) -> Result<Output> {
    // Color the command for logging
    let cmd_str = format!("{:?}", cmd).to_string().replace("\"", "").cyan();
    log_info!("Executing: {}", cmd_str);
    let output_res = cmd.output();

    let output = match output_res {
        Ok(o) => o,
        Err(e) => {
            // Provide more specific error context based on the error kind
            match e.kind() {
                std::io::ErrorKind::NotFound => {
                    let program = cmd.get_program().to_string_lossy();
                    let err_msg = format!(
                        "Command '{}' not found. Please ensure '{}' is installed and available in your PATH.",
                        program, program
                    );
                    log_error!("{}", err_msg);

                    // Provide specific installation instructions for common tools
                    if program == "uv" {
                        log_error!("To install uv, run: pip install uv");
                        log_error!(
                            "Or visit: https://docs.astral.sh/uv/getting-started/installation/"
                        );
                    } else if program == "python" || program == "python3" {
                        log_error!("Please install Python from: https://www.python.org/downloads/");
                    }
                }
                std::io::ErrorKind::PermissionDenied => {
                    let err_msg = format!(
                        "Permission denied when trying to execute '{}'. Please check file permissions.",
                        cmd.get_program().to_string_lossy()
                    );
                    log_error!("{}", err_msg);
                }
                _ => {
                    let err_msg = format!(
                        "Failed to execute command '{}': {}",
                        cmd.get_program().to_string_lossy(),
                        e
                    );
                    log_error!("{}", err_msg);
                }
            }
            return Err(BuildError::IoError(e));
        }
    };

    if !output.status.success() {
        let stdout = String::from_utf8_lossy(&output.stdout);
        let stderr = String::from_utf8_lossy(&output.stderr);
        let error_message = format!(
            "\nCommand '{}' failed with status: {}\nStdout: {}\nStderr: {}",
            cmd_str, output.status, stdout, stderr
        );
        log_error!("{}", error_message);
        return Err(BuildError::FormatterFailed(format!(
            "Command '{}' failed with status {}.",
            cmd_str, output.status
        )));
    }
    Ok(output)
}
