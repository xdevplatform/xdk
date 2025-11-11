//! Configuration module for XDK
//!
//! This module handles reading and parsing the xdk-config.toml file
//! which contains configuration for SDK generation, including versions.

use serde::Deserialize;
use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};

/// Configuration for XDK generation
#[derive(Debug, Deserialize, Clone)]
pub struct XdkConfig {
    /// Version configuration for each language
    pub versions: HashMap<String, String>,
}

impl XdkConfig {
    /// Load configuration from a file path
    pub fn from_file<P: AsRef<Path>>(path: P) -> crate::Result<Self> {
        let contents = fs::read_to_string(path.as_ref())?;
        let config: XdkConfig = toml::from_str(&contents)
            .map_err(|e| crate::SdkGeneratorError::FrameworkError(format!("Failed to parse config: {}", e)))?;
        Ok(config)
    }

    /// Load configuration from the default location (xdk-config.toml in workspace root)
    ///
    /// Searches for xdk-config.toml in the following locations:
    /// 1. Current directory
    /// 2. Parent directories (up to 5 levels)
    /// 3. CARGO_MANIFEST_DIR environment variable location
    pub fn load_default() -> crate::Result<Self> {
        // Try current directory first
        let current_dir = std::env::current_dir()?;
        if let Some(config_path) = Self::find_config_file(&current_dir) {
            return Self::from_file(config_path);
        }

        // Try CARGO_MANIFEST_DIR if available
        if let Ok(manifest_dir) = std::env::var("CARGO_MANIFEST_DIR") {
            let manifest_path = PathBuf::from(manifest_dir);
            if let Some(config_path) = Self::find_config_file(&manifest_path) {
                return Self::from_file(config_path);
            }
        }

        Err(crate::SdkGeneratorError::FrameworkError(
            "Could not find xdk-config.toml. Please ensure it exists in the workspace root.".to_string()
        ))
    }

    /// Find the config file by searching up the directory tree
    fn find_config_file(start_dir: &Path) -> Option<PathBuf> {
        let mut current = start_dir.to_path_buf();
        
        // Search up to 5 levels
        for _ in 0..5 {
            let config_path = current.join("xdk-config.toml");
            if config_path.exists() {
                return Some(config_path);
            }
            
            // Move to parent directory
            if !current.pop() {
                break;
            }
        }
        
        None
    }

    /// Get the version for a specific language
    pub fn get_version(&self, language: &str) -> Option<&str> {
        self.versions.get(language).map(|s| s.as_str())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::io::Write;
    use tempfile::NamedTempFile;

    #[test]
    fn test_parse_config() {
        let config_str = r#"
[versions]
python = "0.2.1-beta"
typescript = "0.1.0"
"#;
        let config: XdkConfig = toml::from_str(config_str).unwrap();
        assert_eq!(config.get_version("python"), Some("0.2.1-beta"));
        assert_eq!(config.get_version("typescript"), Some("0.1.0"));
    }

    #[test]
    fn test_get_version_returns_none_for_missing_language() {
        let config_str = r#"
[versions]
python = "0.2.1-beta"
"#;
        let config: XdkConfig = toml::from_str(config_str).unwrap();
        assert_eq!(config.get_version("python"), Some("0.2.1-beta"));
        assert_eq!(config.get_version("rust"), None);
    }

    #[test]
    fn test_from_file() {
        let mut temp_file = NamedTempFile::new().unwrap();
        let config_content = r#"
[versions]
python = "1.0.0"
typescript = "2.0.0-beta"
"#;
        temp_file.write_all(config_content.as_bytes()).unwrap();
        temp_file.flush().unwrap();

        let config = XdkConfig::from_file(temp_file.path()).unwrap();
        assert_eq!(config.get_version("python"), Some("1.0.0"));
        assert_eq!(config.get_version("typescript"), Some("2.0.0-beta"));
    }

    #[test]
    fn test_from_file_invalid_toml() {
        let mut temp_file = NamedTempFile::new().unwrap();
        temp_file.write_all(b"invalid toml content [[[").unwrap();
        temp_file.flush().unwrap();

        let result = XdkConfig::from_file(temp_file.path());
        assert!(result.is_err());
    }

    #[test]
    fn test_from_file_missing_file() {
        let result = XdkConfig::from_file("/nonexistent/path/xdk-config.toml");
        assert!(result.is_err());
    }

    #[test]
    fn test_version_format_with_beta() {
        let config_str = r#"
[versions]
python = "0.2.2-beta"
typescript = "0.1.1-beta"
"#;
        let config: XdkConfig = toml::from_str(config_str).unwrap();
        
        // Verify beta suffix is preserved
        let python_version = config.get_version("python").unwrap();
        assert!(python_version.ends_with("-beta"));
        assert_eq!(python_version, "0.2.2-beta");
        
        let typescript_version = config.get_version("typescript").unwrap();
        assert!(typescript_version.ends_with("-beta"));
        assert_eq!(typescript_version, "0.1.1-beta");
    }

    #[test]
    fn test_empty_versions() {
        let config_str = r#"
[versions]
"#;
        let config: XdkConfig = toml::from_str(config_str).unwrap();
        assert_eq!(config.get_version("python"), None);
        assert_eq!(config.get_version("typescript"), None);
    }
}
