use crate::error::Result;
use minijinja::Environment;
use super::models::{ClientClassContext, ClientModuleContext, MainClientContext, ReadmeContext, SetupPyContext, OperationInfo};

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

    /// Generate the client class for a tag
    pub fn generate_client_class(&self, tag: &str, operations: &[OperationInfo]) -> String {
        let template = self.env.get_template("python/client_class.j2").unwrap();
        let context = ClientClassContext {
            tag: tag.to_string(),
            operations: operations.to_vec(),
        };
        template.render(context).unwrap_or_default()
    }

    /// Generate the client module for a tag
    pub fn generate_client_module(&self, tag: &str, operations: &[OperationInfo]) -> String {
        let template = self.env.get_template("python/client_module.j2").unwrap();
        let context = ClientModuleContext {
            tag: tag.to_string(),
            operations: operations.to_vec(),
        };
        template.render(context).unwrap_or_default()
    }

    /// Generate the main client class
    pub fn generate_main_client(&self, tags: &[String]) -> String {
        let template = self.env.get_template("python/main_client.j2").unwrap();
        let context = MainClientContext {
            tags: tags.to_vec(),
        };
        template.render(context).unwrap_or_default()
    }

    /// Generate the setup.py file
    pub fn generate_setup_py(&self) -> String {
        let template = self.env.get_template("python/setup_py.j2").unwrap();
        let context = SetupPyContext {
            version: "0.1.0".to_string(),
        };
        template.render(context).unwrap_or_default()
    }

    /// Generate the README.md file
    pub fn generate_readme(&self) -> String {
        let template = self.env.get_template("python/readme.j2").unwrap();
        let context = ReadmeContext {
            version: "0.1.0".to_string(),
        };
        template.render(context).unwrap_or_default()
    }

    /// Generate the __init__.py file
    pub fn generate_init_py(&self) -> String {
        let template = self.env.get_template("python/init_py.j2").unwrap();
        template.render(()).unwrap_or_default()
    }

    /// Generate the requirements.txt file
    pub fn generate_requirements_txt(&self) -> String {
        let template = self.env.get_template("python/requirements_txt.j2").unwrap();
        template.render(()).unwrap_or_default()
    }
} 