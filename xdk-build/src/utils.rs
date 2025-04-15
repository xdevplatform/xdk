use crate::error::{BuildError, Result};
use crate::{log_error, log_info};
use colored::*;
use std::process::{Command, Output};

/// Helper function to run a command and check its status
pub fn run_command(cmd: &mut Command) -> Result<Output> {
    // Color the command for logging
    let cmd_str = format!("{:?}", cmd).to_string().replace("\"", "").cyan();
    log_info!("Executing: {}", cmd_str);
    let output_res = cmd.output();

    let output = match output_res {
        Ok(o) => o,
        Err(e) => {
            let err_msg = format!("Failed to execute command '{}': {}", cmd_str, e);
            log_error!("{}", err_msg);
            return Err(BuildError::IoError(e));
        }
    };

    if !output.status.success() {
        let stdout = String::from_utf8_lossy(&output.stdout);
        let error_message = format!(
            "\nCommand script failed with status: {}\nCaptured output: {}",
            output.status, stdout
        );
        log_error!("{}", error_message);
        return Err(BuildError::FormatterFailed(format!(
            "Script {} failed with status {}.",
            cmd_str, output.status
        )));
    }
    Ok(output)
}
