use crate::{log_error, log_info};
use colored::*;
use std::process::{Command, Output};
use xdk_gen::{Result, SdkGeneratorError};

/// Helper function to run a command and check its status
pub fn run_command(cmd: &mut Command) -> Result<Output> {
    // Color the command for logging
    let cmd_str = format!("{:?}", cmd).cyan();
    log_info!("Executing: {}", cmd_str);
    let output_res = cmd.output();

    let output = match output_res {
        Ok(o) => o,
        Err(e) => {
            let err_msg = format!("Failed to execute command '{}': {}", cmd_str, e);
            log_error!("{}", err_msg);
            return Err(SdkGeneratorError::from(format!(
                "Failed to execute command '{:?}': {}",
                cmd, e
            )));
        }
    };

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        let stdout = String::from_utf8_lossy(&output.stdout);
        // Color the failed command in the error message
        let error_message = format!(
            "Command failed: {}\nExit status: {}\nstdout: {}\nstderr: {}",
            cmd_str, // Use the colored command string
            output.status,
            stdout,
            stderr
        );
        log_error!("{}", error_message);
        // Return non-colored error for potential programmatic use
        return Err(SdkGeneratorError::from(format!(
            "Command failed: {:?}\nExit status: {}\nstdout: {}\nstderr: {}",
            cmd, output.status, stdout, stderr
        )));
    }
    Ok(output)
}
