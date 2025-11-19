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

    /// Convert a single string to the specified casing convention
    /// This first splits the string into words based on common delimiters and casing
    pub fn convert_string(&self, value: &str) -> String {
        let words = split_into_words(value);
        self.convert_words(&words)
    }
}

/// Split a string into words based on various delimiters and casing conventions
fn split_into_words(value: &str) -> Vec<String> {
    let mut words = Vec::new();
    let mut current_word = String::new();
    let chars = value.chars().peekable();

    for c in chars {
        if c == '_' || c == '-' || c == ' ' || c == '.' {
            // Delimiter found, finish current word
            if !current_word.is_empty() {
                words.push(current_word);
                current_word = String::new();
            }
        } else if c.is_uppercase() {
            // Uppercase letter indicates new word boundary (camelCase/PascalCase)
            if !current_word.is_empty() {
                words.push(current_word);
                current_word = String::new();
            }
            current_word.push(c.to_lowercase().next().unwrap());
        } else if c.is_alphanumeric() {
            current_word.push(c);
        }
        // Skip other characters
    }

    // Add the last word if any
    if !current_word.is_empty() {
        words.push(current_word);
    }

    words
}

/// Helper for converting a string to PascalCase
pub fn pascal_case(value: &str) -> String {
    let mut result = String::new();
    let mut capitalize_next = true;

    for c in value.chars() {
        if c == '_' || c == '-' || c == ' ' || c == '.' {
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
