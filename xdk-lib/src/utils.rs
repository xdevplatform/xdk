use super::models::OperationInfo;
use crate::Result;
use minijinja::Environment;
use openapi::OpenApi;
use serde::Serialize;
use std::collections::HashMap;

/// Transform tag names to better client names based on common patterns
pub fn normalize_tag(tag: &str) -> String {
    let mut transformed = tag.to_string();
    
    // Handle special cases for better naming
    match transformed.to_lowercase().as_str() {
        "tweets" => "posts".to_string(),
        "aaasubscriptions" | "aaa subscriptions" => "account_activity".to_string(),
        _ => {
            // Apply general transformations
            transformed = transformed
                .replace(" ", "_")
                .replace("-", "_")
                .to_lowercase();
            
            transformed
        }
    }
}

/// Generate resource name variants for stripping
fn generate_resource_variants(resource_name: &str, mapped_resource: &str) -> Vec<String> {
    let mut variants = Vec::new();
    
    // PascalCase: "account_activity" -> "AccountActivity"
    let pascal = resource_name
        .split('_')
        .map(|w| {
            let mut c = w.chars();
            match c.next() {
                None => String::new(),
                Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
            }
        })
        .collect::<String>();
    variants.push(pascal.clone());
    
    // PascalCase for mapped resource
    if mapped_resource != resource_name {
        let pascal_mapped = mapped_resource
            .split('_')
            .map(|w| {
                let mut c = w.chars();
                match c.next() {
                    None => String::new(),
                    Some(f) => f.to_uppercase().collect::<String>() + c.as_str(),
                }
            })
            .collect::<String>();
        variants.push(pascal_mapped);
    }
    
    // Capitalize first letter only
    if let Some(first) = resource_name.chars().next() {
        let mut cap = first.to_uppercase().collect::<String>();
        cap.push_str(&resource_name[1..]);
        variants.push(cap);
    }
    
    if mapped_resource != resource_name {
        if let Some(first) = mapped_resource.chars().next() {
            let mut cap = first.to_uppercase().collect::<String>();
            cap.push_str(&mapped_resource[1..]);
            variants.push(cap);
        }
    }
    
    // Add singular/plural variations
    if resource_name.ends_with('s') {
        // Remove 's' for singular form
        let singular = &resource_name[..resource_name.len()-1];
        if let Some(first) = singular.chars().next() {
            let mut cap = first.to_uppercase().collect::<String>();
            cap.push_str(&singular[1..]);
            variants.push(cap);
        }
    } else {
        // Add 's' for plural form
        let plural = format!("{}s", resource_name);
        if let Some(first) = plural.chars().next() {
            let mut cap = first.to_uppercase().collect::<String>();
            cap.push_str(&plural[1..]);
            variants.push(cap);
        }
    }
    
    // Add singular/plural variations for mapped resource
    if mapped_resource != resource_name {
        if mapped_resource.ends_with('s') {
            let singular = &mapped_resource[..mapped_resource.len()-1];
            if let Some(first) = singular.chars().next() {
                let mut cap = first.to_uppercase().collect::<String>();
                cap.push_str(&singular[1..]);
                variants.push(cap);
            }
        } else {
            let plural = format!("{}s", mapped_resource);
            if let Some(first) = plural.chars().next() {
                let mut cap = first.to_uppercase().collect::<String>();
                cap.push_str(&plural[1..]);
                variants.push(cap);
            }
        }
    }
    
    variants
}

/// Strip resource name variants from operation ID
fn strip_resource_variants(operation_id: &str, variants: &[String]) -> (String, bool) {
    let mut result = operation_id.to_string();
    let mut changed = false;
    
    for variant in variants {
        // Try to strip at the start (case-insensitive)
        if result.len() >= variant.len() && result[..variant.len()].eq_ignore_ascii_case(&variant) {
            result = result[variant.len()..].to_string();
            changed = true;
            break;
        }
        
        // Try to strip after a lowercase prefix (e.g., searchCommunities)
        if let Some(idx) = result.find(&*variant) {
            // For PascalCase, ensure the match is at a segment boundary
            let before = if idx == 0 { None } else { result[..idx].chars().last() };
            let after = result[idx + variant.len()..].chars().next();
            let is_boundary = (before.map(|c| c.is_lowercase()).unwrap_or(true)) &&
                (after.map(|c| c.is_uppercase()).unwrap_or(true) || after.is_none());

            // Special case: don't strip if the variant appears as part of a larger word
            // For example, in "getPostsReposts", "posts" is part of "PostsReposts", so don't strip it
            let is_part_of_larger_word = if idx > 0 && idx + variant.len() < result.len() {
                let before_char = result[..idx].chars().last().unwrap();
                let after_char = result[idx + variant.len()..].chars().next().unwrap();
                // If both before and after are uppercase, it's likely part of a larger word
                before_char.is_uppercase() && after_char.is_uppercase()
            } else {
                false
            };

            if is_boundary && !is_part_of_larger_word {
                result = format!("{}{}", &result[..idx], &result[idx + variant.len()..]);
                changed = true;
                break;
            }
        }
    }
    
    (result.trim_matches('_').to_string(), changed)
}

/// Handle special tag operations (e.g., "stream")
fn handle_special_tag(transformed: &str, tag: &str) -> Option<String> {
    let special_tags = ["stream"];
    
    if special_tags.contains(&tag) {
        let tag_lower = tag.to_lowercase();
        let mut result = transformed.to_string();
        
        if result.starts_with(&tag_lower) {
            result = result[tag_lower.len()..].trim_matches('_').to_string();
        }
        
        let final_result = if result.contains('_') {
            snake_case_to_camel_case(&result)
        } else {
            result.to_ascii_lowercase()
        };
        
        Some(final_result)
    } else {
        None
    }
}

/// Strip common prefixes from non-special operations
fn strip_common_prefixes(transformed: &str) -> String {
    let special_tags = ["stream"];
    let mut result = transformed.to_string();
    
    for prefix in &special_tags {
        if result.to_lowercase().starts_with(&prefix.to_lowercase()) {
            result = result[prefix.len()..].trim_matches('_').to_string();
            // If the result is a single word after stripping "stream", lowercase it
            if !result.contains('_') && result.len() > 0 {
                result = result.to_ascii_lowercase();
            }
            break;
        }
    }
    
    result
}

/// Get resource name from path
fn get_resource_name_from_path(path: &str) -> Option<&str> {
    let path_segments: Vec<&str> = path.split('/').collect();
    if path_segments.len() > 2 {
        Some(path_segments[2])
    } else {
        None
    }
}

/// Map resource names (e.g., "tweets" -> "posts")
fn map_resource_name(resource_name: &str) -> &str {
    match resource_name.to_lowercase().as_str() {
        "tweets" => "posts",
        _ => resource_name,
    }
}

pub fn normalize_operation_id(operation_id: &str, path: &str, _method: &str, tag: &str) -> String {
    let mut transformed = operation_id.to_string();
    
    // Convert camelCase to snake_case first and always lowercase
    transformed = camel_case_to_snake_case(&transformed).to_ascii_lowercase();
    
    // Apply general transformations
    transformed = transformed
        .replace(" ", "_")
        .replace("-", "_")
        .to_lowercase();

    // Handle special tag operations
    if let Some(result) = handle_special_tag(&transformed, tag) {
        return result;
    }

    // Strip common prefixes for non-special operations
    transformed = strip_common_prefixes(&transformed);

    // Get resource name from path
    let resource_name = match get_resource_name_from_path(path) {
        Some(name) => name,
        None => return snake_case_to_camel_case(&transformed),
    };

    // Map resource names
    let mapped_resource = map_resource_name(resource_name);

    // Generate resource variants and strip them
    let variants = generate_resource_variants(resource_name, mapped_resource);
    let (result, changed) = strip_resource_variants(operation_id, &variants);
    
    // Apply final transformations
    if changed && !result.is_empty() {
        // Convert the cleaned result to snake_case, then back to camelCase
        let snake_result = camel_case_to_snake_case(&result);
        let camel_result = snake_case_to_camel_case(&snake_result);
        // If the result is a single word after resource stripping, lowercase it
        if !camel_result.contains('_') && camel_result.len() > 0 && camel_result.chars().next().unwrap().is_uppercase() {
            camel_result.to_ascii_lowercase()
        } else {
            camel_result
        }
    } else {
        // Convert the transformed result back to camelCase
        snake_case_to_camel_case(&transformed)
    }
}

/// Convert camelCase to snake_case, handling various input formats
fn camel_case_to_snake_case(s: &str) -> String {
    // If already snake_case, return as is
    if s.contains('_') && !s.chars().any(|c| c.is_uppercase()) {
        return s.to_string();
    }
    
    let mut result = String::new();
    let chars: Vec<char> = s.chars().collect();
    
    for &ch in chars.iter() {
        if ch.is_uppercase() {
            // Add underscore before uppercase letter (except at the beginning)
            if !result.is_empty() {
                result.push('_');
            }
            result.push(ch.to_lowercase().next().unwrap());
        } else {
            result.push(ch);
        }
    }
    
    result.to_ascii_lowercase()
}

/// Convert snake_case to camelCase
fn snake_case_to_camel_case(s: &str) -> String {
    if s.is_empty() {
        return s.to_string();
    }
    
    let mut result = String::new();
    let mut capitalize_next = false;
    
    for ch in s.chars() {
        if ch == '_' {
            capitalize_next = true;
        } else {
            if capitalize_next {
                result.push(ch.to_uppercase().next().unwrap());
                capitalize_next = false;
            } else {
                result.push(ch);
            }
        }
    }
    
    result
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
                    let normalized_operation_id = normalize_operation_id(&op.operation_id, path, method, first_tag);
                    
                    let operation_info = OperationInfo {
                        path: path.to_string(),
                        normalized_operation_id: normalized_operation_id,
                        method: method.to_string(),
                        operation_id: op.operation_id.clone(),
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

/// Generate a comprehensive list of client and method names from an OpenAPI spec
pub fn generate_client_method_list(openapi: &OpenApi) -> Result<String> {
    let operations_by_tag = extract_operations_by_tag(openapi)?;
    
    let mut output = String::new();
    output.push_str("# Generated Client and Method Names\n\n");
    
    for (tag, operations) in operations_by_tag.iter() {
        output.push_str(&format!("## {}\n", tag));
        output.push_str(&format!("**Client Class**: `{}Client`\n\n", tag));
        output.push_str("**Methods**:\n");
        
        for operation in operations {
            output.push_str(&format!("- `{}` ({} {})\n", 
                operation.normalized_operation_id, 
                operation.method.to_uppercase(), 
                operation.path
            ));
        }
        output.push_str("\n");
    }
    
    Ok(output)
}

/// Generate a detailed list showing original vs normalized operation IDs
pub fn generate_detailed_client_method_list(openapi: &OpenApi) -> Result<String> {
    let operations_by_tag = extract_operations_by_tag(openapi)?;
    
    let mut output = String::new();
    output.push_str("# Detailed Client and Method Names\n\n");
    output.push_str("This shows the transformation from original operation IDs to normalized method names.\n\n");
    
    for (tag, operations) in operations_by_tag.iter() {
        output.push_str(&format!("## {}\n", tag));
        output.push_str(&format!("**Client Class**: `{}Client`\n\n", tag));
        output.push_str("**Methods**:\n");
        
        for operation in operations {
            output.push_str(&format!("- `{}` → `{}` ({} {})\n", 
                operation.operation_id,
                operation.normalized_operation_id, 
                operation.method.to_uppercase(), 
                operation.path
            ));
        }
        output.push_str("\n");
    }
    
    Ok(output)
}

pub fn render_template<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
) -> Result<String> {
    Ok(env.get_template(template)?.render(context)?)
}