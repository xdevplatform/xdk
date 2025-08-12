/// Represents different casing conventions for SDK generation
#[derive(Debug, Clone, Copy)]
pub enum Casing {
    /// snake_case: my_function_name
    Snake,
    /// camelCase: myFunctionName
    Camel,
    /// PascalCase: MyFunctionName
    Pascal,
    /// kebab-case: my-function-name
    Kebab,
    /// SCREAMING_SNAKE_CASE: MY_FUNCTION_NAME
    ScreamingSnake,
}

impl Casing {
    /// Convert a vector of words to the specified casing convention
    pub fn convert_words(&self, words: &[String]) -> String {
        match self {
            Casing::Snake => words.join("_").to_lowercase(),
            Casing::Camel => {
                if words.is_empty() {
                    String::new()
                } else {
                    let mut result = words[0].to_lowercase();
                    for word in &words[1..] {
                        result.push_str(&pascal_case(word));
                    }
                    result
                }
            }
            Casing::Pascal => words
                .iter()
                .map(|w| pascal_case(w))
                .collect::<Vec<_>>()
                .join(""),
            Casing::Kebab => words.join("-").to_lowercase(),
            Casing::ScreamingSnake => words.join("_").to_uppercase(),
        }
    }
}

/// Helper for converting a string to snake_case
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

/// Helper for converting a string to PascalCase
pub fn pascal_case(value: &str) -> String {
    let mut result = String::new();
    let mut capitalize_next = true;

    for c in value.chars() {
        if c == '_' || c == '-' || c == ' ' {
            // Skip separators and capitalize the next character
            capitalize_next = true;
        } else if c.is_uppercase() {
            // Uppercase letters indicate word boundaries
            result.push(c);
            capitalize_next = false;
        } else if c.is_alphanumeric() {
            if capitalize_next {
                result.push(c.to_ascii_uppercase());
                capitalize_next = false;
            } else {
                result.push(c.to_ascii_lowercase());
            }
        }
        // Skip non-alphanumeric characters (except separators handled above)
    }

    result
}

/// Helper for converting a string to camelCase
pub fn camel_case(value: &str) -> String {
    let pascal = pascal_case(value);
    if pascal.is_empty() {
        return pascal;
    }

    let mut chars = pascal.chars();
    match chars.next() {
        None => String::new(),
        Some(first) => first.to_lowercase().collect::<String>() + chars.as_str(),
    }
}

/// Helper for converting a string to kebab-case
pub fn kebab_case(value: &str) -> String {
    snake_case(value).replace('_', "-")
}

/// Helper for converting a string to SCREAMING_SNAKE_CASE
pub fn screaming_snake_case(value: &str) -> String {
    snake_case(value).to_uppercase()
}
