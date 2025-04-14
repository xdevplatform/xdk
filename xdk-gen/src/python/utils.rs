use crate::error::Result;
use openapi::OpenApi;
use std::collections::HashMap;
use super::models::{OperationInfo, RequestBody};

/// Extract operations by tag from the OpenAPI specification
pub fn extract_operations_by_tag(openapi: &OpenApi) -> Result<HashMap<String, Vec<OperationInfo>>> {
    let mut operations_by_tag: HashMap<String, Vec<OperationInfo>> = HashMap::new();

    for (path, path_item) in &openapi.paths {
        // Process GET operations
        if let Some(get_op) = &path_item.get {
            if let Some(tags) = &get_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "get".to_string(),
                        operation_id: get_op.summary.clone().unwrap_or_else(|| {
                            // Generate a default operation ID if none is provided
                            format!("get_{}", path.trim_start_matches('/').replace('/', "_"))
                        }),
                        summary: get_op.summary.clone().unwrap_or_default(),
                        description: get_op.description.clone().unwrap_or_default(),
                        parameters: get_op.parameters.clone().unwrap_or_default(),
                        request_body: get_op.request_body.as_ref().and_then(|rb| {
                            rb.as_ref().content.iter().next().map(|(content_type, media_type)| {
                                RequestBody {
                                    content_type: content_type.clone(),
                                    schema: media_type.schema.clone(),
                                    required: rb.as_ref().required.unwrap_or(false),
                                }
                            })
                        }),
                        responses: get_op.responses.iter().map(|(k, v)| (k.clone(), v.as_ref().description.clone())).collect(),
                    };
                    operations_by_tag.entry(normalized_tag).or_insert_with(Vec::new).push(operation_info);
                }
            }
        }

        // Process POST operations
        if let Some(post_op) = &path_item.post {
            if let Some(tags) = &post_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    println!("Operation: {}", serde_json::to_string_pretty(&post_op).unwrap());
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "post".to_string(),
                        operation_id: post_op.summary.clone().unwrap_or_else(|| {
                            // Generate a default operation ID if none is provided
                            format!("post_{}", path.trim_start_matches('/').replace('/', "_"))
                        }),
                        summary: post_op.summary.clone().unwrap_or_default(),
                        description: post_op.description.clone().unwrap_or_default(),
                        parameters: post_op.parameters.clone().unwrap_or_default(),
                        request_body: post_op.request_body.as_ref().and_then(|rb| {
                            rb.as_ref().content.iter().next().map(|(content_type, media_type)| {
                                RequestBody {
                                    content_type: content_type.clone(),
                                    schema: media_type.schema.clone(),
                                    required: rb.as_ref().required.unwrap_or(false),
                                }
                            })
                        }),
                        responses: post_op.responses.iter().map(|(k, v)| (k.clone(), v.as_ref().description.clone())).collect(),
                    };
                    operations_by_tag.entry(normalized_tag).or_insert_with(Vec::new).push(operation_info);
                }
            }
        }

        // Process PUT operations
        if let Some(put_op) = &path_item.put {
            if let Some(tags) = &put_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "put".to_string(),
                        operation_id: put_op.summary.clone().unwrap_or_else(|| {
                            // Generate a default operation ID if none is provided
                            format!("put_{}", path.trim_start_matches('/').replace('/', "_"))
                        }),
                        summary: put_op.summary.clone().unwrap_or_default(),
                        description: put_op.description.clone().unwrap_or_default(),
                        parameters: put_op.parameters.clone().unwrap_or_default(),
                        request_body: put_op.request_body.as_ref().and_then(|rb| {
                            rb.as_ref().content.iter().next().map(|(content_type, media_type)| {
                                RequestBody {
                                    content_type: content_type.clone(),
                                    schema: media_type.schema.clone(),
                                    required: rb.as_ref().required.unwrap_or(false),
                                }
                            })
                        }),
                        responses: put_op.responses.iter().map(|(k, v)| (k.clone(), v.as_ref().description.clone())).collect(),
                    };
                    operations_by_tag.entry(normalized_tag).or_insert_with(Vec::new).push(operation_info);
                }
            }
        }

        // Process DELETE operations
        if let Some(delete_op) = &path_item.delete {
            if let Some(tags) = &delete_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "delete".to_string(),
                        operation_id: delete_op.summary.clone().unwrap_or_else(|| {
                            // Generate a default operation ID if none is provided
                            format!("delete_{}", path.trim_start_matches('/').replace('/', "_"))
                        }),
                        summary: delete_op.summary.clone().unwrap_or_default(),
                        description: delete_op.description.clone().unwrap_or_default(),
                        parameters: delete_op.parameters.clone().unwrap_or_default(),
                        request_body: delete_op.request_body.as_ref().and_then(|rb| {
                            rb.as_ref().content.iter().next().map(|(content_type, media_type)| {
                                RequestBody {
                                    content_type: content_type.clone(),
                                    schema: media_type.schema.clone(),
                                    required: rb.as_ref().required.unwrap_or(false),
                                }
                            })
                        }),
                        responses: delete_op.responses.iter().map(|(k, v)| (k.clone(), v.as_ref().description.clone())).collect(),
                    };
                    operations_by_tag.entry(normalized_tag).or_insert_with(Vec::new).push(operation_info);
                }
            }
        }

        // Process PATCH operations
        if let Some(patch_op) = &path_item.patch {
            if let Some(tags) = &patch_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "patch".to_string(),
                        operation_id: patch_op.summary.clone().unwrap_or_else(|| {
                            // Generate a default operation ID if none is provided
                            format!("patch_{}", path.trim_start_matches('/').replace('/', "_"))
                        }),
                        summary: patch_op.summary.clone().unwrap_or_default(),
                        description: patch_op.description.clone().unwrap_or_default(),
                        parameters: patch_op.parameters.clone().unwrap_or_default(),
                        request_body: patch_op.request_body.as_ref().and_then(|rb| {
                            rb.as_ref().content.iter().next().map(|(content_type, media_type)| {
                                RequestBody {
                                    content_type: content_type.clone(),
                                    schema: media_type.schema.clone(),
                                    required: rb.as_ref().required.unwrap_or(false),
                                }
                            })
                        }),
                        responses: patch_op.responses.iter().map(|(k, v)| (k.clone(), v.as_ref().description.clone())).collect(),
                    };
                    operations_by_tag.entry(normalized_tag).or_insert_with(Vec::new).push(operation_info);
                }
            }
        }
    }

    Ok(operations_by_tag)
} 