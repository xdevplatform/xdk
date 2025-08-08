use crate::error::{BuildError, Result};
use std::path::Path;
use xdk_gen::TypeScript;
use xdk_lib::{log_info, generate};
use xdk_openapi::OpenApi;

/// Clean up excessive whitespace in generated TypeScript code
fn cleanup_typescript_file(content: &str) -> String {
    let lines: Vec<&str> = content.lines().collect();
    let mut cleaned_lines = Vec::new();
    let mut in_multiline_comment = false;
    let mut in_jsdoc = false;
    
    for line in lines {
        let trimmed = line.trim();
        
        // Skip empty lines unless we're in a JSDoc comment
        if trimmed.is_empty() {
            if in_jsdoc {
                cleaned_lines.push("");
            }
            continue;
        }
        
        // Handle JSDoc comments
        if trimmed.starts_with("/**") {
            in_jsdoc = true;
            cleaned_lines.push(line);
            continue;
        }
        
        if trimmed == "*/" {
            in_jsdoc = false;
            cleaned_lines.push(line);
            continue;
        }
        
        if in_jsdoc && trimmed.starts_with("*") {
            cleaned_lines.push(line);
            continue;
        }
        
        // Handle multiline comments
        if trimmed.starts_with("/*") && !trimmed.ends_with("*/") {
            in_multiline_comment = true;
            cleaned_lines.push(line);
            continue;
        }
        
        if in_multiline_comment {
            cleaned_lines.push(line);
            if trimmed.ends_with("*/") {
                in_multiline_comment = false;
            }
            continue;
        }
        
        // Handle import statements - don't add extra blank lines
        if trimmed.starts_with("import") {
            if let Some(prev) = cleaned_lines.last() {
                if !prev.trim().is_empty() {
                    cleaned_lines.push("");
                }
            }
            cleaned_lines.push(line);
            continue;
        }
        
        // Handle export statements
        if trimmed.starts_with("export") {
            if let Some(prev) = cleaned_lines.last() {
                if !prev.trim().is_empty() {
                    cleaned_lines.push("");
                }
            }
            cleaned_lines.push(line);
            continue;
        }
        
        // Handle class/interface declarations
        if trimmed.starts_with("export class") || trimmed.starts_with("export interface") {
            if let Some(prev) = cleaned_lines.last() {
                if !prev.trim().is_empty() {
                    cleaned_lines.push("");
                }
            }
            cleaned_lines.push(line);
            continue;
        }
        
        // Handle method declarations
        if trimmed.starts_with("async") && trimmed.contains("(") {
            if let Some(prev) = cleaned_lines.last() {
                if !prev.trim().is_empty() && !prev.trim().starts_with("/**") {
                    cleaned_lines.push("");
                }
            }
            cleaned_lines.push(line);
            continue;
        }
        
        // Regular line
        cleaned_lines.push(line);
    }
    
    // Remove trailing empty lines
    while let Some(last) = cleaned_lines.last() {
        if last.trim().is_empty() {
            cleaned_lines.pop();
        } else {
            break;
        }
    }
    
    cleaned_lines.join("\n")
}

/// Generate TypeScript SDK from OpenAPI spec
pub fn generate_typescript(openapi: &OpenApi, output_dir: &Path) -> Result<()> {
    log_info!("Generating TypeScript SDK...");
    std::fs::create_dir_all(output_dir).map_err(BuildError::IoError)?;

    // Initialize TypeScript generator
    let generator = TypeScript;

    // Generate the SDK
    generate(generator, openapi, output_dir).map_err(BuildError::SdkGenError)?;

    // Post-process generated TypeScript files to clean up whitespace
    log_info!("Cleaning up generated TypeScript files...");
    cleanup_typescript_files(output_dir)?;

    // Try to install dependencies and build, but don't fail if it doesn't work
    if let Err(e) = install_dependencies(output_dir) {
        log_info!("Warning: Could not install dependencies: {}", e);
        log_info!("You may need to run 'npm install' manually");
    } else if let Err(e) = build_sdk(output_dir) {
        log_info!("Warning: Could not build SDK: {}", e);
        log_info!("You may need to run 'npm run build' manually");
    }

    log_info!("TypeScript SDK generated successfully!");
    log_info!("To complete setup, run:");
    log_info!("  cd {}", output_dir.display());
    log_info!("  npm install");
    log_info!("  npm run build");
    Ok(())
}

fn cleanup_typescript_files(output_dir: &Path) -> Result<()> {
    use std::fs;
    use std::path::PathBuf;

    fn process_directory(dir: &Path) -> Result<()> {
        for entry in fs::read_dir(dir).map_err(BuildError::IoError)? {
            let entry = entry.map_err(BuildError::IoError)?;
            let path = entry.path();
            
            if path.is_dir() {
                process_directory(&path)?;
            } else if let Some(extension) = path.extension() {
                if extension == "ts" || extension == "js" {
                    let content = fs::read_to_string(&path).map_err(BuildError::IoError)?;
                    let cleaned_content = cleanup_typescript_file(&content);
                    fs::write(&path, cleaned_content).map_err(BuildError::IoError)?;
                }
            }
        }
        Ok(())
    }

    process_directory(output_dir)
}

fn install_dependencies(output_dir: &Path) -> Result<()> {
    log_info!("Installing dependencies...");

    let status = std::process::Command::new("npm")
        .arg("install")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to install dependencies: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Failed to install dependencies".to_string()))
    }
}

fn build_sdk(output_dir: &Path) -> Result<()> {
    log_info!("Building TypeScript SDK...");

    let status = std::process::Command::new("npm")
        .arg("run")
        .arg("build")
        .current_dir(output_dir)
        .status()
        .map_err(|e| BuildError::CommandFailed(format!("Failed to build SDK: {}", e)))?;

    if status.success() {
        Ok(())
    } else {
        Err(BuildError::CommandFailed("Failed to build SDK".to_string()))
    }
} 