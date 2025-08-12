use openapi::{Parameter, RefOrValue};
use std::collections::HashMap;
use xdk_lib::{
    Casing,
    models::{Metadata, OperationGroup, OperationInfo, ParameterInfo, TagInfo},
};

#[test]
fn test_operation_info_with_casing() {
    let operation = OperationInfo {
        class_name: String::new(),
        method_name: String::new(),
        method: "GET".to_string(),
        path: "/users".to_string(),
        description: Some("Get users".to_string()),
        summary: Some("Retrieve users".to_string()),
        security: None,
        parameters: None,
        request_body: None,
        responses: HashMap::new(),
    };

    let updated_operation = operation.with_casing("get_users".to_string(), "GetUsers".to_string());

    assert_eq!(updated_operation.method_name, "get_users");
    assert_eq!(updated_operation.class_name, "GetUsers");
    assert_eq!(updated_operation.method, "GET");
    assert_eq!(updated_operation.path, "/users");
}

#[test]
fn test_tag_info_creation() {
    let tag_info = TagInfo {
        original: vec!["user".to_string(), "profile".to_string()],
        class_name: "UserProfile".to_string(),
        import_name: "user_profile".to_string(),
        property_name: "user_profile".to_string(),
        display_name: "User Profile".to_string(),
    };

    assert_eq!(tag_info.original, vec!["user", "profile"]);
    assert_eq!(tag_info.class_name, "UserProfile");
    assert_eq!(tag_info.import_name, "user_profile");
    assert_eq!(tag_info.property_name, "user_profile");
    assert_eq!(tag_info.display_name, "User Profile");
}

#[test]
fn test_parameter_info_structure() {
    let param_info = ParameterInfo {
        original_name: "maxResults".to_string(),
        variable_name: "max_results".to_string(),
        location: "query".to_string(),
        required: false,
        param_type: "integer".to_string(),
        description: Some("Maximum number of results".to_string()),
        schema: None,
    };

    assert_eq!(param_info.original_name, "maxResults");
    assert_eq!(param_info.variable_name, "max_results");
    assert_eq!(param_info.location, "query");
    assert!(!param_info.required);
    assert_eq!(param_info.param_type, "integer");
    assert_eq!(
        param_info.description,
        Some("Maximum number of results".to_string())
    );
}

#[test]
fn test_operation_group_structure() {
    let operation = OperationInfo {
        class_name: "GetUser".to_string(),
        method_name: "get_user".to_string(),
        method: "GET".to_string(),
        path: "/users/{id}".to_string(),
        description: None,
        summary: None,
        security: None,
        parameters: None,
        request_body: None,
        responses: HashMap::new(),
    };

    let metadata = Metadata {
        normalized_operation_id: vec!["get".to_string(), "user".to_string()],
    };

    let operation_group = OperationGroup {
        operation,
        metadata,
        raw_parameters: None,
    };

    assert_eq!(operation_group.operation.method_name, "get_user");
    assert_eq!(
        operation_group.metadata.normalized_operation_id,
        vec!["get", "user"]
    );
    assert!(operation_group.raw_parameters.is_none());
}

#[test]
fn test_parameter_info_serialization() {
    use serde_json;

    let param_info = ParameterInfo {
        original_name: "userId".to_string(),
        variable_name: "user_id".to_string(),
        location: "path".to_string(),
        required: true,
        param_type: "string".to_string(),
        description: Some("User identifier".to_string()),
        schema: None,
    };

    let json = serde_json::to_string(&param_info).expect("Serialization should work");
    assert!(json.contains("userId"));
    assert!(json.contains("user_id"));
    assert!(json.contains("path"));
    assert!(json.contains("true"));
}

#[test]
fn test_tag_info_serialization() {
    use serde_json;

    let tag_info = TagInfo {
        original: vec!["community".to_string(), "notes".to_string()],
        class_name: "CommunityNotes".to_string(),
        import_name: "community_notes".to_string(),
        property_name: "community_notes".to_string(),
        display_name: "Community Notes".to_string(),
    };

    let json = serde_json::to_string(&tag_info).expect("Serialization should work");
    assert!(json.contains("CommunityNotes"));
    assert!(json.contains("community_notes"));
    assert!(json.contains("Community Notes"));
}

#[test]
fn test_tag_info_factory_function() {
    let tag_words = vec!["community".to_string(), "notes".to_string()];

    // Test Python-style casing
    let python_tag = TagInfo::new(
        &tag_words,
        Casing::Pascal, // class_casing
        Casing::Snake,  // import_casing
        Casing::Snake,  // property_casing
    );

    assert_eq!(python_tag.original, vec!["community", "notes"]);
    assert_eq!(python_tag.class_name, "CommunityNotes");
    assert_eq!(python_tag.import_name, "community_notes");
    assert_eq!(python_tag.property_name, "community_notes");
    assert_eq!(python_tag.display_name, "community notes");

    // Test Java-style casing
    let java_tag = TagInfo::new(
        &tag_words,
        Casing::Pascal, // class_casing
        Casing::Pascal, // import_casing
        Casing::Camel,  // property_casing
    );

    assert_eq!(java_tag.class_name, "CommunityNotes");
    assert_eq!(java_tag.import_name, "CommunityNotes");
    assert_eq!(java_tag.property_name, "communityNotes");
}

#[test]
fn test_tag_info_factory_with_single_word() {
    let tag_words = vec!["tweets".to_string()];

    let tag_info = TagInfo::new(&tag_words, Casing::Pascal, Casing::Snake, Casing::Snake);

    assert_eq!(tag_info.class_name, "Tweets");
    assert_eq!(tag_info.import_name, "tweets");
    assert_eq!(tag_info.property_name, "tweets");
    assert_eq!(tag_info.display_name, "tweets");
}

#[test]
fn test_parameter_info_from_openapi_basic() {
    let param = Parameter {
        name: Some("maxResults".to_string()),
        r#in: Some("query".to_string()),
        description: Some("Maximum number of results".to_string()),
        required: Some(false),
        schema: None, // Simplified for testing
    };

    let parameters = Some(vec![RefOrValue::Value(param)]);

    let processed = ParameterInfo::from_openapi_parameters(&parameters, Casing::Snake);
    assert!(processed.is_some());

    let params = processed.unwrap();
    assert_eq!(params.len(), 1);
    assert_eq!(params[0].original_name, "maxResults");
    assert_eq!(params[0].variable_name, "max_results");
    assert_eq!(params[0].location, "query");
    assert!(!params[0].required);
    assert_eq!(params[0].param_type, "any"); // Default when no schema
}

#[test]
fn test_parameter_info_casing_variants() {
    let param = Parameter {
        name: Some("maxResults".to_string()),
        r#in: Some("query".to_string()),
        description: Some("Maximum number of results".to_string()),
        required: Some(false),
        schema: None,
    };

    let parameters = Some(vec![RefOrValue::Value(param)]);

    // Test with different casings
    let snake_case_result =
        ParameterInfo::from_openapi_parameters(&parameters, Casing::Snake).unwrap();
    assert_eq!(snake_case_result[0].variable_name, "max_results");

    let camel_case_result =
        ParameterInfo::from_openapi_parameters(&parameters, Casing::Camel).unwrap();
    assert_eq!(camel_case_result[0].variable_name, "maxResults");

    let pascal_case_result =
        ParameterInfo::from_openapi_parameters(&parameters, Casing::Pascal).unwrap();
    assert_eq!(pascal_case_result[0].variable_name, "MaxResults");
}

#[test]
fn test_parameter_info_path_param_required() {
    let param = Parameter {
        name: Some("userId".to_string()),
        r#in: Some("path".to_string()),
        description: Some("User ID".to_string()),
        required: Some(false), // Even if set to false, path params should be required
        schema: None,
    };

    let parameters = Some(vec![RefOrValue::Value(param)]);
    let processed = ParameterInfo::from_openapi_parameters(&parameters, Casing::Snake).unwrap();

    // Path parameters should always be required
    assert!(processed[0].required);
}

#[test]
fn test_parameter_info_empty_parameters() {
    let result = ParameterInfo::from_openapi_parameters(&None, Casing::Snake);
    assert!(result.is_none());

    let empty_params = Some(vec![]);
    let result = ParameterInfo::from_openapi_parameters(&empty_params, Casing::Snake).unwrap();
    assert_eq!(result.len(), 0);
}
