use super::models::OperationInfo;
use crate::Result;
use minijinja::Environment;
use openapi::OpenApi;
use serde::Serialize;
use std::collections::HashMap;

/// Transform tag names to better client names based on common patterns
pub fn normalize_tag(tag: &str) -> String {
    // Handle special cases for better naming
    match tag.to_lowercase().as_str() {
        "tweets" => "posts".to_string(),
        _ => {
            // Apply general transformations
            tag.replace(" ", "_").replace("-", "_").to_lowercase()
        }
    }
}

/// Convert normalized tag to PascalCase for class names
pub fn normalize_tag_to_pascal_case(tag: &str) -> String {
    let normalized = normalize_tag(tag);

    // Convert snake_case to PascalCase
    normalized
        .split('_')
        .map(|word| {
            let mut chars = word.chars();
            match chars.next() {
                None => String::new(),
                Some(first) => first.to_uppercase().collect::<String>() + chars.as_str(),
            }
        })
        .collect::<String>()
}

pub fn normalize_operation_id(operation_id: &str, _path: &str, _method: &str, tag: &str) -> String {
    let mut words = split_into_words(operation_id);

    // Normalize tag to lowercase for case-insensitive comparison
    let normalized_tag = tag.to_lowercase();

    let mapped_tag = match normalized_tag.as_str() {
        "tweets" => "posts",
        "community_notes" => "notes",
        "direct_messages" => "dm_conversations",
        _ => &normalized_tag,
    };

    // Generate singular/plural variations of the tag
    let tag_variations = generate_tag_variations(mapped_tag);

    // Remove the first occurrence of any tag variation
    for variation in tag_variations {
        if let Some(start_index) = find_tag_sequence(&words, &variation) {
            remove_tag_sequence(&mut words, start_index, &variation);
            break; // Only remove the first occurrence
        }
    }

    // Convert words back to camelCase
    words_to_camel_case(&words)
}

/// Convert a vector of words to camelCase
fn words_to_camel_case(words: &[String]) -> String {
    if words.is_empty() {
        return String::new();
    }

    let mut result = String::new();

    for (i, word) in words.iter().enumerate() {
        if i == 0 {
            // First word should be lowercase
            result.push_str(&word.to_lowercase());
        } else {
            // Subsequent words should be capitalized
            let mut chars = word.chars();
            if let Some(first) = chars.next() {
                result.push(first.to_uppercase().next().unwrap());
                result.push_str(&chars.as_str().to_lowercase());
            }
        }
    }

    result
}

/// Generate singular and plural variations of a tag for matching
fn generate_tag_variations(tag: &str) -> Vec<String> {
    let mut variations = vec![tag.to_string()];

    // Add singular version if tag is plural
    if tag.ends_with('s') {
        variations.push(tag[..tag.len() - 1].to_string());
    } else {
        // Add plural version if tag is singular
        variations.push(format!("{}s", tag));
    }

    variations
}

/// Find the starting index of a tag sequence in the words vector
fn find_tag_sequence(words: &[String], tag: &str) -> Option<usize> {
    let tag_words: Vec<&str> = tag.split('_').collect();

    for (i, window) in words.windows(tag_words.len()).enumerate() {
        let window_lower: Vec<String> = window.iter().map(|w| w.to_lowercase()).collect();
        if window_lower == tag_words {
            return Some(i);
        }
    }

    None
}

/// Remove a tag sequence from the words vector starting at the given index
fn remove_tag_sequence(words: &mut Vec<String>, start_index: usize, tag: &str) {
    let tag_words: Vec<&str> = tag.split('_').collect();

    // Remove the sequence of words
    for _ in 0..tag_words.len() {
        if start_index < words.len() {
            words.remove(start_index);
        }
    }
}

/// Split a camelCase string into words based on uppercase boundaries
fn split_into_words(s: &str) -> Vec<String> {
    if s.is_empty() {
        return vec![];
    }

    let mut words = Vec::new();
    let mut current_word = String::new();
    let chars: Vec<char> = s.chars().collect();

    for (i, &ch) in chars.iter().enumerate() {
        if ch.is_uppercase() && i > 0 {
            // If we have a current word and encounter an uppercase letter, start a new word
            if !current_word.is_empty() {
                words.push(current_word.clone());
                current_word.clear();
            }
            current_word.push(ch.to_lowercase().next().unwrap());
        } else {
            current_word.push(ch);
        }
    }

    // Add the last word if it's not empty
    if !current_word.is_empty() {
        words.push(current_word);
    }

    // Filter out empty strings
    words.into_iter().filter(|word| !word.is_empty()).collect()
}

/// Extract operations by tag from the OpenAPI specification with automatic name transformations
pub fn extract_operations_by_tag(openapi: &OpenApi) -> Result<HashMap<String, Vec<OperationInfo>>> {
    let mut operations_by_tag: HashMap<String, Vec<OperationInfo>> = HashMap::new();

    /// Helper function to process an operation and add it to the operations_by_tag map
    fn process_operation(
        operations_by_tag: &mut HashMap<String, Vec<OperationInfo>>,
        path: &str,
        method: &str,
        operation: &Option<openapi::Operation>,
    ) {
        if let Some(op) = operation {
            if let Some(tags) = &op.tags {
                // Only use the first tag
                if let Some(first_tag) = tags.first() {
                    // Normalize tag name
                    let normalized_tag = normalize_tag(first_tag);

                    // Normalize operation ID
                    let normalized_operation_id =
                        normalize_operation_id(&op.operation_id, path, method, first_tag);

                    let operation_info = OperationInfo {
                        path: path.to_string(),
                        method: method.to_string(),
                        operation_id: normalized_operation_id,
                        summary: op.summary.clone(),
                        description: op.description.clone(),
                        parameters: op.parameters.clone(),
                        security: op.security.clone(),
                        request_body: op.request_body.clone(),
                        responses: op.responses.clone(),
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
                }
            }
        }
    }

    for (path, path_item) in &openapi.paths {
        // Process each HTTP method type using the same logic
        process_operation(&mut operations_by_tag, path, "get", &path_item.get);
        process_operation(&mut operations_by_tag, path, "post", &path_item.post);
        process_operation(&mut operations_by_tag, path, "put", &path_item.put);
        process_operation(&mut operations_by_tag, path, "delete", &path_item.delete);
        process_operation(&mut operations_by_tag, path, "patch", &path_item.patch);
    }

    Ok(operations_by_tag)
}

pub fn render_template<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
) -> Result<String> {
    Ok(env.get_template(template)?.render(context)?)
}
