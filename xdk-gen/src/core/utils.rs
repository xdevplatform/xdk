use super::models::{OperationInfo, RequestBody};
use crate::core::Result;
use minijinja::Environment;
use openapi::OpenApi;
use serde::Serialize;
use std::collections::HashMap;

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
                        operation_id: get_op.operation_id.clone().unwrap_or_default(),
                        summary: get_op.summary.clone().unwrap_or_default(),
                        description: get_op.description.clone().unwrap_or_default(),
                        parameters: get_op.parameters.clone().unwrap_or_default(),
                        request_body: get_op
                            .request_body
                            .as_ref()
                            .map(|rb_ref| rb_ref.try_resolve()) // Option<Result<Rc<RequestBody>, Error>>
                            .transpose()? // Result<Option<Rc<RequestBody>>, Error>
                            .and_then(|rb_rc| {
                                // Option<Rc<RequestBody>> -> Option<RequestBody>
                                rb_rc
                                    .content
                                    .iter()
                                    .next()
                                    .map(|(content_type, media_type)| RequestBody {
                                        content_type: content_type.clone(),
                                        schema: media_type.schema.clone(),
                                        required: rb_rc.required.unwrap_or(false),
                                    })
                            }),
                        responses: get_op
                            .responses
                            .iter()
                            .map(|(k, v_ref)| {
                                // &RefOrValue<Response>
                                v_ref
                                    .try_resolve()
                                    .map_err(Into::into) // Convert OpenApiError to SdkGeneratorError
                                    .map(|v_rc| (k.clone(), v_rc.description.clone())) // Result<(String, String), SdkGeneratorError>
                            })
                            .collect::<Result<HashMap<_, _>>>()?, // Result<HashMap<String, String>, SdkGeneratorError>
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
                }
            }
        }

        // Process POST operations
        if let Some(post_op) = &path_item.post {
            if let Some(tags) = &post_op.tags {
                for tag in tags {
                    // Normalize tag name
                    let normalized_tag = tag.replace(" ", "_");
                    let operation_info = OperationInfo {
                        path: path.clone(),
                        method: "post".to_string(),
                        operation_id: post_op.operation_id.clone().unwrap_or_default(),
                        summary: post_op.summary.clone().unwrap_or_default(),
                        description: post_op.description.clone().unwrap_or_default(),
                        parameters: post_op.parameters.clone().unwrap_or_default(),
                        request_body: post_op
                            .request_body
                            .as_ref()
                            .map(|rb_ref| rb_ref.try_resolve()) // Option<Result<Rc<RequestBody>, Error>>
                            .transpose()? // Result<Option<Rc<RequestBody>>, Error>
                            .and_then(|rb_rc| {
                                // Option<Rc<RequestBody>> -> Option<RequestBody>
                                rb_rc
                                    .content
                                    .iter()
                                    .next()
                                    .map(|(content_type, media_type)| RequestBody {
                                        content_type: content_type.clone(),
                                        schema: media_type.schema.clone(),
                                        required: rb_rc.required.unwrap_or(false),
                                    })
                            }),
                        responses: post_op
                            .responses
                            .iter()
                            .map(|(k, v_ref)| {
                                // &RefOrValue<Response>
                                v_ref
                                    .try_resolve()
                                    .map_err(Into::into) // Convert OpenApiError to SdkGeneratorError
                                    .map(|v_rc| (k.clone(), v_rc.description.clone())) // Result<(String, String), SdkGeneratorError>
                            })
                            .collect::<Result<HashMap<_, _>>>()?, // Result<HashMap<String, String>, SdkGeneratorError>
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
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
                        operation_id: put_op.operation_id.clone().unwrap_or_default(),
                        summary: put_op.summary.clone().unwrap_or_default(),
                        description: put_op.description.clone().unwrap_or_default(),
                        parameters: put_op.parameters.clone().unwrap_or_default(),
                        request_body: put_op
                            .request_body
                            .as_ref()
                            .map(|rb_ref| rb_ref.try_resolve()) // Option<Result<Rc<RequestBody>, Error>>
                            .transpose()? // Result<Option<Rc<RequestBody>>, Error>
                            .and_then(|rb_rc| {
                                // Option<Rc<RequestBody>> -> Option<RequestBody>
                                rb_rc
                                    .content
                                    .iter()
                                    .next()
                                    .map(|(content_type, media_type)| RequestBody {
                                        content_type: content_type.clone(),
                                        schema: media_type.schema.clone(),
                                        required: rb_rc.required.unwrap_or(false),
                                    })
                            }),
                        responses: put_op
                            .responses
                            .iter()
                            .map(|(k, v_ref)| {
                                // &RefOrValue<Response>
                                v_ref
                                    .try_resolve()
                                    .map_err(Into::into) // Convert OpenApiError to SdkGeneratorError
                                    .map(|v_rc| (k.clone(), v_rc.description.clone())) // Result<(String, String), SdkGeneratorError>
                            })
                            .collect::<Result<HashMap<_, _>>>()?, // Result<HashMap<String, String>, SdkGeneratorError>
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
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
                        operation_id: delete_op.operation_id.clone().unwrap_or_default(),
                        summary: delete_op.summary.clone().unwrap_or_default(),
                        description: delete_op.description.clone().unwrap_or_default(),
                        parameters: delete_op.parameters.clone().unwrap_or_default(),
                        request_body: delete_op
                            .request_body
                            .as_ref()
                            .map(|rb_ref| rb_ref.try_resolve()) // Option<Result<Rc<RequestBody>, Error>>
                            .transpose()? // Result<Option<Rc<RequestBody>>, Error>
                            .and_then(|rb_rc| {
                                // Option<Rc<RequestBody>> -> Option<RequestBody>
                                rb_rc
                                    .content
                                    .iter()
                                    .next()
                                    .map(|(content_type, media_type)| RequestBody {
                                        content_type: content_type.clone(),
                                        schema: media_type.schema.clone(),
                                        required: rb_rc.required.unwrap_or(false),
                                    })
                            }),
                        responses: delete_op
                            .responses
                            .iter()
                            .map(|(k, v_ref)| {
                                // &RefOrValue<Response>
                                v_ref
                                    .try_resolve()
                                    .map_err(Into::into) // Convert OpenApiError to SdkGeneratorError
                                    .map(|v_rc| (k.clone(), v_rc.description.clone())) // Result<(String, String), SdkGeneratorError>
                            })
                            .collect::<Result<HashMap<_, _>>>()?, // Result<HashMap<String, String>, SdkGeneratorError>
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
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
                        operation_id: patch_op.operation_id.clone().unwrap_or_default(),
                        summary: patch_op.summary.clone().unwrap_or_default(),
                        description: patch_op.description.clone().unwrap_or_default(),
                        parameters: patch_op.parameters.clone().unwrap_or_default(),
                        request_body: patch_op
                            .request_body
                            .as_ref()
                            .map(|rb_ref| rb_ref.try_resolve()) // Option<Result<Rc<RequestBody>, Error>>
                            .transpose()? // Result<Option<Rc<RequestBody>>, Error>
                            .and_then(|rb_rc| {
                                // Option<Rc<RequestBody>> -> Option<RequestBody>
                                rb_rc
                                    .content
                                    .iter()
                                    .next()
                                    .map(|(content_type, media_type)| RequestBody {
                                        content_type: content_type.clone(),
                                        schema: media_type.schema.clone(),
                                        required: rb_rc.required.unwrap_or(false),
                                    })
                            }),
                        responses: patch_op
                            .responses
                            .iter()
                            .map(|(k, v_ref)| {
                                // &RefOrValue<Response>
                                v_ref
                                    .try_resolve()
                                    .map_err(Into::into) // Convert OpenApiError to SdkGeneratorError
                                    .map(|v_rc| (k.clone(), v_rc.description.clone())) // Result<(String, String), SdkGeneratorError>
                            })
                            .collect::<Result<HashMap<_, _>>>()?, // Result<HashMap<String, String>, SdkGeneratorError>
                    };
                    operations_by_tag
                        .entry(normalized_tag)
                        .or_default()
                        .push(operation_info);
                }
            }
        }
    }

    Ok(operations_by_tag)
}

pub fn render_template<C: Serialize>(env: &Environment, template: &str, context: &C) -> Result<String> {
    Ok(env.get_template(template)?.render(context)?)
}