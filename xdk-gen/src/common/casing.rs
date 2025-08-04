/// MiniJinja filter for converting a string to snake_case
pub fn snake_case(value: &str) -> String {
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

    result.trim_matches('_').to_string()
}

/// MiniJinja filter for converting a string to PascalCase
pub fn pascal_case(value: &str) -> String {
    let mut result = String::new();
    let mut capitalize_next = true;

    for c in value.chars() {
        if c == '_' {
            // Skip underscores and capitalize the next character
            capitalize_next = true;
        } else if c.is_alphanumeric() {
            if capitalize_next {
                result.push(c.to_ascii_uppercase());
                capitalize_next = false;
            } else {
                result.push(c.to_ascii_lowercase());
            }
        }
        // Skip non-alphanumeric characters (except underscores handled above)
    }

    result
}
