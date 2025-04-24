pub mod error;
pub mod generator;
pub mod models;
pub mod utils;

pub use error::*;

/// Result type for SDK generator operations
pub type Result<T> = std::result::Result<T, SdkGeneratorError>;
