use crate::error::Result;
use minijinja::Environment;

/// Renderer for Python SDK templates
pub struct Renderer<'a> {
    env: Environment<'a>,
}

impl<'a> Renderer<'a> {
    /// Create a new renderer with a configured Jinja environment
    pub fn new() -> Result<Self> {
        let env = Self::create_jinja_env()?;
        Ok(Renderer { env })
    }

    /// Create the Jinja environment with custom filters and templates
    fn create_jinja_env() -> Result<Environment<'a>> {
        let mut env = Environment::new();
        
        // Add custom filters
        env.add_filter("snake_case", |value: &str| {
            let mut result = String::new();
            let mut chars = value.chars().peekable();
            let mut prev_is_underscore = false;
            
            while let Some(c) = chars.next() {
                if c.is_uppercase() {
                    if !result.is_empty() && !prev_is_underscore {
                        result.push('_');
                    }
                    result.push(c.to_ascii_lowercase());
                    prev_is_underscore = false;
                } else if c.is_alphanumeric() {
                    result.push(c.to_ascii_lowercase());
                    prev_is_underscore = false;
                } else {
                    if !prev_is_underscore {
                        result.push('_');
                        prev_is_underscore = true;
                    }
                }
            }
            
            // Remove leading/trailing underscores
            let result = result.trim_matches('_').to_string();
            
            Ok(result)
        });
        
        env.add_filter("python_type", |value: &str| {
            let python_type = match value {
                "string" => "str",
                "integer" => "int",
                "number" => "float",
                "boolean" => "bool",
                "array" => "List",
                "object" => "Dict[str, Any]",
                _ => "Any",
            };
            
            Ok(python_type.to_string())
        });
        
        // Load templates from files at compile time
        env.add_template("python/client_class.j2", include_str!("../../templates/python/client_class.j2"))?;
        env.add_template("python/client_module.j2", include_str!("../../templates/python/client_module.j2"))?;
        env.add_template("python/main_client.j2", include_str!("../../templates/python/main_client.j2"))?;
        env.add_template("python/setup_py.j2", include_str!("../../templates/python/setup_py.j2"))?;
        env.add_template("python/readme.j2", include_str!("../../templates/python/readme.j2"))?;
        env.add_template("python/init_py.j2", include_str!("../../templates/python/init_py.j2"))?;
        env.add_template("python/requirements_txt.j2", include_str!("../../templates/python/requirements_txt.j2"))?;
        
        Ok(env)
    }

    /// Generic method to render a template with a context
    pub fn render_template<T>(&self, template_name: &str, context: T) -> Result<String> 
    where
        T: serde::Serialize,
    {
        let template = self.env.get_template(template_name)?;
        let rendered = template.render(context)?;
        Ok(self.format(&rendered))
    }

    /// Clean up rendered content by removing unnecessary newlines while preserving code structure
    fn format(&self, content: &str) -> String {
        let lines: Vec<&str> = content.lines().collect();
        let mut result = Vec::new();
        
        for (i, line) in lines.iter().enumerate() {
            let line = line.trim_end();
            
            // Skip empty lines
            if line.is_empty() {
                continue;
            }
            
            // Add the current line
            result.push(line.to_string());
            
            // Add a newline after definitions, block starts, or before indented code
            let is_definition = line.starts_with("class ") || 
                               (line.starts_with("def ") && !line.contains("lambda"));
            let is_block_start = line.ends_with(':');
            let next_line_indented = i + 1 < lines.len() && 
                                    lines[i + 1].starts_with(char::is_whitespace);
            
            if is_definition || is_block_start || next_line_indented {
                result.push(String::new());
            }
        }
        
        // Join with newlines and ensure there's exactly one newline at the end
        let mut formatted = result.join("\n");
        if !formatted.ends_with('\n') {
            formatted.push('\n');
        }
        
        formatted
    }
} 