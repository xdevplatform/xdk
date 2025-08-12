//! OpenAPI specification parsing and processing
//!
//! This module handles the core logic for parsing OpenAPI specifications
//! and transforming them into the internal data structures used by the
//! XDK generator system.

use crate::Result;
use crate::models::{Metadata, OperationGroup, OperationInfo};
use openapi::OpenApi;
use std::collections::HashMap;

/// Extract operations by tag from the OpenAPI specification with automatic name transformations
pub fn extract_operations_by_tag(
    openapi: &OpenApi,
) -> Result<HashMap<Vec<String>, Vec<OperationGroup>>> {
    let mut operations_by_tag: HashMap<Vec<String>, Vec<OperationGroup>> = HashMap::new();

    /// Helper function to process an operation and add it to the operations_by_tag map
    fn process_operation(
        operations_by_tag: &mut HashMap<Vec<String>, Vec<OperationGroup>>,
        path: &str,
        method: &str,
        operation: &Option<openapi::Operation>,
    ) {
        if let Some(op) = operation
            && let Some(tags) = &op.tags
            && let Some(first_tag) = tags.first()
        {
            let normalized_tag: Vec<String> = normalize_tag(first_tag);

            let normalized_operation_id: Vec<String> = normalize_operation_id(&op.operation_id);

            let operation_info = OperationInfo {
                path: path.to_string(),
                method: method.to_string(),
                class_name: String::new(), // Will be set when casing is applied
                method_name: String::new(), // Will be set when casing is applied
                summary: op.summary.clone(),
                description: op.description.clone(),
                parameters: None, // Will be processed with casing in the macro
                security: op.security.clone(),
                request_body: op.request_body.clone(),
                responses: op.responses.clone(),
            };
            let operation_group = OperationGroup {
                operation: operation_info,
                metadata: Metadata {
                    normalized_operation_id: clean_operation_id(
                        normalized_operation_id,
                        normalized_tag.clone(),
                    ),
                },
                raw_parameters: op.parameters.clone(),
            };
            operations_by_tag
                .entry(normalized_tag)
                .or_default()
                .push(operation_group);
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

/// Normalize tag names for consistent processing
pub fn normalize_tag(tag: &str) -> Vec<String> {
    tag.split_whitespace()
        .map(|word| {
            word.to_lowercase()
                .replace("tweets", "posts")
                .replace("tweet", "post")
        })
        .collect()
}

/// Normalize operation ID into word components
pub fn normalize_operation_id(operation_id: &str) -> Vec<String> {
    let chars: Vec<char> = operation_id.chars().collect();
    let mut words: Vec<String> = Vec::new();
    let mut current = String::new();

    for i in 0..chars.len() {
        let ch = chars[i];
        if ch.is_uppercase() {
            let prev_lower = i > 0 && chars[i - 1].is_lowercase();
            let prev_upper = i > 0 && chars[i - 1].is_uppercase();
            let next_lower = i + 1 < chars.len() && chars[i + 1].is_lowercase();
            if !current.is_empty() && (prev_lower || (prev_upper && next_lower)) {
                words.push(current.clone());
                current.clear();
            }
        }
        current.push(ch.to_lowercase().next().unwrap());
    }

    if !current.is_empty() {
        words.push(current);
    }

    words
}

/// Clean operation ID by removing words that appear in the tag
pub fn clean_operation_id(
    operation_id_as_vec: Vec<String>,
    tag_as_vec: Vec<String>,
) -> Vec<String> {
    let mut cleaned_operation_id = Vec::new();
    for word in operation_id_as_vec {
        if !tag_as_vec.contains(&word) {
            cleaned_operation_id.push(word.to_lowercase());
        }
    }
    cleaned_operation_id
}
