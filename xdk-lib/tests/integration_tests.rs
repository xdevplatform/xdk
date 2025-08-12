use minijinja::Environment;
use openapi::{Parameter, RefOrValue};
use serde::Serialize;
use std::collections::HashMap;
use std::fs;
use tempfile::TempDir;
use xdk_lib::{
    Casing,
    models::{OperationInfo, ParameterInfo, TagInfo},
    templates::render_template,
    testing::generate_test_specifications,
};

#[derive(Serialize)]
struct TestContext {
    tag: xdk_lib::models::TagInfo,
    operations: Vec<OperationInfo>,
}

#[test]
fn test_end_to_end_tag_processing() {
    // Test the complete flow from tag words to different casing variants
    let tag_words = vec!["community".to_string(), "notes".to_string()];

    // Test different language configurations
    let python_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Snake, Casing::Snake);
    let java_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Pascal, Casing::Camel);
    let csharp_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Pascal, Casing::Pascal);

    // Python style
    assert_eq!(python_tag.class_name, "CommunityNotes");
    assert_eq!(python_tag.import_name, "community_notes");
    assert_eq!(python_tag.property_name, "community_notes");

    // Java style
    assert_eq!(java_tag.class_name, "CommunityNotes");
    assert_eq!(java_tag.import_name, "CommunityNotes");
    assert_eq!(java_tag.property_name, "communityNotes");

    // C# style
    assert_eq!(csharp_tag.class_name, "CommunityNotes");
    assert_eq!(csharp_tag.import_name, "CommunityNotes");
    assert_eq!(csharp_tag.property_name, "CommunityNotes");
}

#[test]
fn test_end_to_end_parameter_processing() {
    // Create OpenAPI parameters
    let params = vec![
        RefOrValue::Value(Parameter {
            name: Some("maxResults".to_string()),
            r#in: Some("query".to_string()),
            required: Some(false),
            schema: None,
            description: Some("Maximum number of results".to_string()),
        }),
        RefOrValue::Value(Parameter {
            name: Some("userId".to_string()),
            r#in: Some("path".to_string()),
            required: Some(true),
            schema: None,
            description: None,
        }),
        RefOrValue::Value(Parameter {
            name: Some("authToken".to_string()),
            r#in: Some("header".to_string()),
            required: Some(false),
            schema: None,
            description: Some("Authorization token".to_string()),
        }),
    ];

    let parameters = Some(params);

    // Test different language parameter casing
    let python_params = ParameterInfo::from_openapi_parameters(&parameters, Casing::Snake).unwrap();
    let java_params = ParameterInfo::from_openapi_parameters(&parameters, Casing::Camel).unwrap();
    let csharp_params =
        ParameterInfo::from_openapi_parameters(&parameters, Casing::Pascal).unwrap();

    // All should have 3 parameters
    assert_eq!(python_params.len(), 3);
    assert_eq!(java_params.len(), 3);
    assert_eq!(csharp_params.len(), 3);

    // Find maxResults parameter and check casing
    let max_results_python = python_params
        .iter()
        .find(|p| p.original_name == "maxResults")
        .unwrap();
    let max_results_java = java_params
        .iter()
        .find(|p| p.original_name == "maxResults")
        .unwrap();
    let max_results_csharp = csharp_params
        .iter()
        .find(|p| p.original_name == "maxResults")
        .unwrap();

    assert_eq!(max_results_python.variable_name, "max_results");
    assert_eq!(max_results_java.variable_name, "maxResults");
    assert_eq!(max_results_csharp.variable_name, "MaxResults");
}

#[test]
fn test_end_to_end_operation_processing() {
    // Create test operation with parameters
    let params = vec![
        ParameterInfo {
            original_name: "max_results".to_string(),
            variable_name: "max_results".to_string(),
            location: "query".to_string(),
            required: false,
            param_type: "integer".to_string(),
            description: Some("Maximum results".to_string()),
            schema: None,
        },
        ParameterInfo {
            original_name: "next_token".to_string(),
            variable_name: "next_token".to_string(),
            location: "query".to_string(),
            required: false,
            param_type: "string".to_string(),
            description: Some("Pagination token".to_string()),
            schema: None,
        },
    ];

    let operation = OperationInfo {
        class_name: "GetTweets".to_string(),
        method_name: "get_tweets".to_string(),
        method: "GET".to_string(),
        path: "/tweets".to_string(),
        description: Some("Retrieve tweets".to_string()),
        summary: Some("Get tweets".to_string()),
        security: None,
        parameters: Some(params),
        request_body: None,
        responses: HashMap::new(),
    };

    // Test that operation can be used for test generation
    let mut operations_by_tag = HashMap::new();
    operations_by_tag.insert("tweets".to_string(), vec![operation]);

    let test_specs = generate_test_specifications(&operations_by_tag).unwrap();
    let tweets_spec = test_specs.get("tweets").unwrap();

    // Should detect pagination (has both token and limit params)
    let method = &tweets_spec.structural_tests[0].methods[0];
    assert!(method.supports_pagination);
    assert_eq!(method.method_name, "get_tweets");
    assert_eq!(method.class_name, "GetTweets");

    // Should have pagination tests
    assert_eq!(tweets_spec.pagination_tests.len(), 1);
    let pagination_test = &tweets_spec.pagination_tests[0];
    assert_eq!(pagination_test.method_name, "get_tweets");
}

#[test]
fn test_end_to_end_template_rendering() {
    // Create test data
    let tag_info = TagInfo::new(
        &["user".to_string(), "profile".to_string()],
        Casing::Pascal,
        Casing::Snake,
        Casing::Snake,
    );

    let operation = OperationInfo {
        class_name: "GetUserProfile".to_string(),
        method_name: "get_user_profile".to_string(),
        method: "GET".to_string(),
        path: "/users/{id}/profile".to_string(),
        description: Some("Get user profile".to_string()),
        summary: None,
        security: None,
        parameters: Some(vec![ParameterInfo {
            original_name: "userId".to_string(),
            variable_name: "user_id".to_string(),
            location: "path".to_string(),
            required: true,
            param_type: "string".to_string(),
            description: Some("User ID".to_string()),
            schema: None,
        }]),
        request_body: None,
        responses: HashMap::new(),
    };

    let context = TestContext {
        tag: tag_info,
        operations: vec![operation],
    };

    // Create template
    let mut env = Environment::new();
    let template = r#"
# {{ tag.class_name }} Client

Class: {{ tag.class_name }}
Import: {{ tag.import_name }}
Property: {{ tag.property_name }}

## Operations

{% for operation in operations %}
### {{ operation.method_name }}
- Method: {{ operation.method }}
- Path: {{ operation.path }}
- Class: {{ operation.class_name }}
{% if operation.parameters %}
Parameters:
{% for param in operation.parameters %}
  - {{ param.variable_name }} ({{ param.param_type }}, {{ param.location }}){% if param.required %} *required*{% endif %}
{% endfor %}
{% endif %}
{% endfor %}
"#;

    env.add_template("test_client", template).unwrap();

    let result = render_template(&env, "test_client", &context).unwrap();

    // Verify template rendered correctly
    assert!(result.contains("# UserProfile Client"));
    assert!(result.contains("Class: UserProfile"));
    assert!(result.contains("Import: user_profile"));
    assert!(result.contains("Property: user_profile"));
    assert!(result.contains("### get_user_profile"));
    assert!(result.contains("Method: GET"));
    assert!(result.contains("Path: /users/{id}/profile"));
    assert!(result.contains("Class: GetUserProfile"));
    assert!(result.contains("user_id (string, path) *required*"));
}

#[test]
fn test_end_to_end_file_generation() {
    use std::io::Write;

    // Create temporary directory for test output
    let temp_dir = TempDir::new().unwrap();
    let output_dir = temp_dir.path();

    // Create test data
    let tag_info = TagInfo::new(
        &["users".to_string()],
        Casing::Pascal,
        Casing::Snake,
        Casing::Snake,
    );

    let operation = OperationInfo {
        class_name: "GetUsers".to_string(),
        method_name: "get_users".to_string(),
        method: "GET".to_string(),
        path: "/users".to_string(),
        description: Some("List users".to_string()),
        summary: None,
        security: None,
        parameters: None,
        request_body: None,
        responses: HashMap::new(),
    };

    let context = TestContext {
        tag: tag_info,
        operations: vec![operation],
    };

    // Create simple template
    let mut env = Environment::new();
    env.add_template("client", "class {{ tag.class_name }}Client:\n    def {{ operations[0].method_name }}(self):\n        pass").unwrap();

    // Render and write file
    let rendered = render_template(&env, "client", &context).unwrap();
    let file_path = output_dir.join("users_client.py");

    let mut file = fs::File::create(&file_path).unwrap();
    file.write_all(rendered.as_bytes()).unwrap();

    // Verify file was created and contains expected content
    let content = fs::read_to_string(&file_path).unwrap();
    assert!(content.contains("class UsersClient:"));
    assert!(content.contains("def get_users(self):"));
}

#[test]
fn test_end_to_end_multiple_languages() {
    // Test that the same operation can be processed for different languages
    let operation_id_words = vec!["get".to_string(), "user".to_string(), "profile".to_string()];
    let tag_words = vec!["user".to_string(), "management".to_string()];

    // Simulate processing for Python
    let python_operation_method = Casing::Snake.convert_words(&operation_id_words);
    let python_operation_class = Casing::Pascal.convert_words(&operation_id_words);
    let python_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Snake, Casing::Snake);

    // Simulate processing for Java
    let java_operation_method = Casing::Camel.convert_words(&operation_id_words);
    let java_operation_class = Casing::Pascal.convert_words(&operation_id_words);
    let java_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Pascal, Casing::Camel);

    // Simulate processing for C#
    let csharp_operation_method = Casing::Pascal.convert_words(&operation_id_words);
    let csharp_operation_class = Casing::Pascal.convert_words(&operation_id_words);
    let csharp_tag = TagInfo::new(&tag_words, Casing::Pascal, Casing::Pascal, Casing::Pascal);

    // Verify Python style
    assert_eq!(python_operation_method, "get_user_profile");
    assert_eq!(python_operation_class, "GetUserProfile");
    assert_eq!(python_tag.import_name, "user_management");
    assert_eq!(python_tag.property_name, "user_management");

    // Verify Java style
    assert_eq!(java_operation_method, "getUserProfile");
    assert_eq!(java_operation_class, "GetUserProfile");
    assert_eq!(java_tag.import_name, "UserManagement");
    assert_eq!(java_tag.property_name, "userManagement");

    // Verify C# style
    assert_eq!(csharp_operation_method, "GetUserProfile");
    assert_eq!(csharp_operation_class, "GetUserProfile");
    assert_eq!(csharp_tag.import_name, "UserManagement");
    assert_eq!(csharp_tag.property_name, "UserManagement");
}

#[test]
fn test_end_to_end_error_handling() {
    // Test error scenarios throughout the pipeline

    // Test invalid template
    let mut env = Environment::new();
    env.add_template("invalid", "{{ invalid_variable.nonexistent_field }}")
        .unwrap();

    #[derive(Serialize)]
    struct EmptyContext {}

    let result = render_template(&env, "invalid", &EmptyContext {});
    assert!(result.is_err());

    // Test empty operations for test generation
    let empty_operations = HashMap::new();
    let test_specs = generate_test_specifications(&empty_operations).unwrap();
    assert!(test_specs.is_empty());

    // Test parameter processing with empty parameters
    let result = ParameterInfo::from_openapi_parameters(&None, Casing::Snake);
    assert!(result.is_none());

    let empty_params = Some(vec![]);
    let result = ParameterInfo::from_openapi_parameters(&empty_params, Casing::Snake).unwrap();
    assert!(result.is_empty());
}

#[test]
fn test_template_rendering_functionality() {
    use minijinja::Environment;
    use serde::Serialize;

    #[derive(Serialize)]
    struct TestTemplateContext {
        name: String,
        count: i32,
    }

    let mut env = Environment::new();
    env.add_template("test", "Hello {{ name }}! Count: {{ count }}")
        .unwrap();

    let context = TestTemplateContext {
        name: "World".to_string(),
        count: 42,
    };

    let result = render_template(&env, "test", &context).unwrap();
    assert_eq!(result, "Hello World! Count: 42");
}

#[test]
fn test_template_rendering_with_tag_info() {
    use minijinja::Environment;

    let mut env = Environment::new();
    env.add_template(
        "tag_test",
        "Class: {{ tag.class_name }}, Import: {{ tag.import_name }}",
    )
    .unwrap();

    #[derive(serde::Serialize)]
    struct TagContext {
        tag: TagInfo,
    }

    let tag_info = TagInfo::new(
        &["user".to_string(), "profile".to_string()],
        Casing::Pascal,
        Casing::Snake,
        Casing::Snake,
    );

    let context = TagContext { tag: tag_info };

    let result = render_template(&env, "tag_test", &context).unwrap();
    assert_eq!(result, "Class: UserProfile, Import: user_profile");
}
