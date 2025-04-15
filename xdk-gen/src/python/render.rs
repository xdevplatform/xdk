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
            let chars = value.chars();
            let mut result = String::new();
            let mut prev_is_underscore = false;

            for c in chars {
                if c.is_uppercase() {
                    if !result.is_empty() && !prev_is_underscore {
                        result.push('_');
                    }
                    result.push(c.to_ascii_lowercase());
                    prev_is_underscore = false;
                } else if c.is_alphanumeric() {
                    result.push(c.to_ascii_lowercase());
                    prev_is_underscore = false;
                } else if !prev_is_underscore {
                    result.push('_');
                    prev_is_underscore = true;
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
        env.add_template(
            "python/client_class.j2",
            include_str!("../../templates/python/client_class.j2"),
        )?;
        env.add_template(
            "python/client_module.j2",
            include_str!("../../templates/python/client_module.j2"),
        )?;
        env.add_template(
            "python/main_client.j2",
            include_str!("../../templates/python/main_client.j2"),
        )?;
        env.add_template(
            "python/setup_py.j2",
            include_str!("../../templates/python/setup_py.j2"),
        )?;
        env.add_template(
            "python/readme.j2",
            include_str!("../../templates/python/readme.j2"),
        )?;
        env.add_template(
            "python/init_py.j2",
            include_str!("../../templates/python/init_py.j2"),
        )?;
        env.add_template(
            "python/requirements_txt.j2",
            include_str!("../../templates/python/requirements_txt.j2"),
        )?;

        Ok(env)
    }

    /// Generic method to render a template with a context
    pub fn render_template<T>(&self, template_name: &str, context: T) -> Result<String>
    where
        T: serde::Serialize,
    {
        let template = self.env.get_template(template_name)?;
        let rendered = template.render(context)?;
        Ok(rendered)
    }
}
