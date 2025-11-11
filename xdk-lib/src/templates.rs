//! Template rendering utilities
//!
//! This module provides functionality for rendering Jinja2 templates
//! with context data for SDK generation.

use crate::Result;
use minijinja::Environment;
use serde::Serialize;

/// Render a template with the given context
///
/// # Arguments
/// * `env` - The MiniJinja environment containing templates
/// * `template` - The name of the template to render
/// * `context` - The context data to pass to the template
///
/// # Returns
/// The rendered template content as a string with automatic "do not edit" header
pub fn render_template<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
) -> Result<String> {
    let content = env.get_template(template)?.render(context)?;
    Ok(add_generated_header(template, &content, None))
}

/// Render a template with the given context and output path for better file type detection
///
/// # Arguments
/// * `env` - The MiniJinja environment containing templates
/// * `template` - The name of the template to render
/// * `context` - The context data to pass to the template
/// * `output_path` - The output file path for determining file type
///
/// # Returns
/// The rendered template content as a string with automatic "do not edit" header
pub fn render_template_with_path<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
    output_path: &str,
) -> Result<String> {
    let content = env.get_template(template)?.render(context)?;
    Ok(add_generated_header(template, &content, Some(output_path)))
}

/// Add a "generated file - do not edit" header to the content
///
/// Automatically detects the file type and uses the appropriate comment syntax
fn add_generated_header(template_name: &str, content: &str, output_path: Option<&str>) -> String {
    let header = get_header_for_file(template_name, output_path);

    if header.is_empty() {
        // No header for this file type
        return content.to_string();
    }

    format!("{}\n{}", header, content)
}

/// Get the appropriate header comment based on file type
///
/// Uses output path if available, otherwise falls back to template name
fn get_header_for_file(template_name: &str, output_path: Option<&str>) -> String {
    // Determine file extension from output path if available
    let file_type = if let Some(path) = output_path {
        if path.ends_with(".py") {
            "python"
        } else if path.ends_with(".ts") || path.ends_with(".js") {
            "typescript"
        } else if path.ends_with(".json") {
            "json"
        } else if path.ends_with(".md") {
            "markdown"
        } else if path.ends_with(".toml") {
            "toml"
        } else if path.ends_with("ignore") || path.ends_with(".gitignore") {
            "ignore"
        } else {
            // Fallback to template name detection
            ""
        }
    } else {
        ""
    };

    // Determine file type from template name if not determined from path
    let (comment_start, comment_line, comment_end) =
        if file_type == "python" || file_type == "toml" || file_type == "ignore" {
            ("", "#", "")
        } else if file_type == "typescript" {
            ("", "//", "")
        } else if file_type == "json" {
            return String::new();
        } else if file_type == "markdown" {
            ("<!--", "", "-->")
        } else if template_name.ends_with("_py")
            || template_name.contains("python")
            || template_name == "pyproject_toml"
            || template_name.contains("_toml")
            || template_name == "main_client"
            || template_name.starts_with("test_")
            || template_name == "conftest"
        {
            // Python and TOML files use # comments
            ("", "#", "")
        } else if template_name.ends_with("_ts")
            || template_name.contains("typescript")
            || template_name.contains(".ts")
            || template_name == "tsconfig"
            || template_name == "tsup.config"
            || template_name.contains("http_client")
            || template_name.contains("crypto")
            || template_name.contains("oauth1_auth")
            || template_name == "index"
            || template_name == "schemas"
            || template_name.contains("generate_docs")
        {
            // TypeScript/JavaScript files use // comments
            ("", "//", "")
        } else if template_name == "package_json"
            || template_name == "typedoc.json"
            || template_name.contains(".json")
        {
            // JSON files - no comments, return empty
            return String::new();
        } else if template_name == "readme" || template_name.ends_with("_md") {
            // Markdown files use HTML comments
            ("<!--", "", "-->")
        } else if template_name == "npmignore" || template_name.ends_with("ignore") {
            // Ignore files use # comments
            ("", "#", "")
        } else {
            // Default: use // for unknown types
            ("", "//", "")
        };

    let notice = "AUTO-GENERATED FILE - DO NOT EDIT";
    let details = "This file was automatically generated by the XDK build tool.";
    let warning = "Any manual changes will be overwritten on the next generation.";

    if comment_start.is_empty() && comment_end.is_empty() {
        // Single-line comment style (Python, TypeScript, etc.)
        format!(
            "{} {}\n{} {}\n{} {}",
            comment_line, notice, comment_line, details, comment_line, warning
        )
    } else {
        // Multi-line comment style (Markdown)
        format!(
            "{}\n{}\n{}\n{}",
            comment_start, notice, details, comment_end
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_python_header() {
        let header = get_header_for_file("client_class", Some("xdk/client.py"));
        assert!(header.contains("# AUTO-GENERATED FILE"));
        assert!(header.contains("# This file was automatically generated"));
        assert!(header.contains("# Any manual changes will be overwritten"));
    }

    #[test]
    fn test_typescript_header() {
        let header = get_header_for_file("http_client", Some("src/http-client.ts"));
        assert!(header.contains("// AUTO-GENERATED FILE"));
        assert!(header.contains("// This file was automatically generated"));
        assert!(header.contains("// Any manual changes will be overwritten"));
    }

    #[test]
    fn test_json_no_header() {
        let header = get_header_for_file("package_json", Some("package.json"));
        assert!(header.is_empty());
    }

    #[test]
    fn test_markdown_header() {
        let header = get_header_for_file("readme", Some("README.md"));
        assert!(header.contains("<!--"));
        assert!(header.contains("AUTO-GENERATED FILE"));
        assert!(header.contains("-->"));
    }

    #[test]
    fn test_add_generated_header() {
        let content = "def hello():\n    pass";
        let result = add_generated_header("client_class", content, Some("xdk/client.py"));
        assert!(result.starts_with("# AUTO-GENERATED FILE"));
        assert!(result.contains("def hello():\n    pass"));
    }

    #[test]
    fn test_toml_header() {
        let header = get_header_for_file("pyproject_toml", Some("pyproject.toml"));
        assert!(header.contains("# AUTO-GENERATED FILE"));
        assert!(header.contains("# This file was automatically generated"));
    }

    #[test]
    fn test_header_not_added_twice() {
        let content = "print('hello')";
        let result1 = add_generated_header("models", content, Some("xdk/models.py"));
        let result2 = add_generated_header("models", &result1, Some("xdk/models.py"));

        // Count occurrences of the header
        let count = result2.matches("AUTO-GENERATED FILE").count();
        // Should only appear twice (once in each header addition since we called it twice)
        assert_eq!(
            count, 2,
            "Header should appear exactly twice when added twice"
        );
    }

    #[test]
    fn test_typescript_file_detection() {
        let header = get_header_for_file("paginator", Some("src/paginator.ts"));
        assert!(header.contains("// AUTO-GENERATED FILE"));
        assert!(!header.contains("# AUTO-GENERATED FILE"));
    }

    #[test]
    fn test_python_file_detection() {
        let header = get_header_for_file("paginator", Some("xdk/paginator.py"));
        assert!(header.contains("# AUTO-GENERATED FILE"));
        assert!(!header.contains("// AUTO-GENERATED FILE"));
    }
}
