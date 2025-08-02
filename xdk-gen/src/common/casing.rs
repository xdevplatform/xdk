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
    let mut chars = value.chars();

    // Capitalize the first character
    if let Some(first_char) = chars.next() {
        result.push(first_char.to_ascii_uppercase());
    }

    // Keep the rest of the string as-is
    for c in chars {
        result.push(c);
    }

    result
}
