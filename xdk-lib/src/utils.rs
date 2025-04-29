use super::models::OperationInfo;
use crate::Result;
use minijinja::Environment;
use openapi::OpenApi;
use serde::Serialize;
use std::collections::HashMap;

/// Extract operations by tag from the OpenAPI specification
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
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.to_string(),
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

pub fn render_template<C: Serialize>(
    env: &Environment,
    template: &str,
    context: &C,
) -> Result<String> {
    Ok(env.get_template(template)?.render(context)?)
}
