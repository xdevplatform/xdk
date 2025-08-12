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
/// The rendered template content as a string
pub fn render_template<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
) -> Result<String> {
    Ok(env.get_template(template)?.render(context)?)
}
