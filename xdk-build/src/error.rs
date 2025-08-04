use std::io;
use thiserror::Error;
use xdk_lib::SdkGeneratorError;

/// Errors that can occur during the SDK build process.
#[derive(Error, Debug)]
pub enum BuildError {
    /// IO error occurred during file operations.
    #[error("File system operation failed: {0}")]
    IoError(#[from] io::Error),

    /// Error during SDK generation (from xdk-gen crate).
    #[error("SDK generation failed: {0}")]
    SdkGenError(#[from] SdkGeneratorError),

    /// A command failed to execute successfully.
    #[error("Command execution failed: {0}")]
    CommandFailed(String),

    /// The Python formatter script failed.
    #[error("Code formatting failed: {0}")]
    FormatterFailed(String),
}

/// Result type for SDK build operations.
pub type Result<T> = std::result::Result<T, BuildError>;
