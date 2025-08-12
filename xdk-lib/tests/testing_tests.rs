use xdk_lib::testing::{generate_test_specifications, TestSpecification, TestParameter, MethodSignature, ContractTest, PaginationTest, MockScenario};
use xdk_lib::models::{OperationInfo, ParameterInfo};
use std::collections::HashMap;

fn create_test_operation(
    method_name: &str,
    class_name: &str,
    method: &str,
    path: &str,
    parameters: Option<Vec<ParameterInfo>>,
) -> OperationInfo {
    OperationInfo {
        class_name: class_name.to_string(),
        method_name: method_name.to_string(),
        method: method.to_string(),
        path: path.to_string(),
        description: Some(format!("{} operation", method_name)),
        summary: Some(format!("{} summary", method_name)),
        security: None,
        parameters,
        request_body: None,
        responses: HashMap::new(),
    }
}

fn create_test_parameter(
    original_name: &str,
    variable_name: &str,
    location: &str,
    required: bool,
    param_type: &str,
) -> ParameterInfo {
    ParameterInfo {
        original_name: original_name.to_string(),
        variable_name: variable_name.to_string(),
        location: location.to_string(),
        required,
        param_type: param_type.to_string(),
        description: Some(format!("{} parameter", original_name)),
        schema: None,
    }
}

#[test]
fn test_generate_test_specifications_basic() {
    let mut operations_by_tag = HashMap::new();
    
    let operation = create_test_operation(
        "get_users",
        "GetUsers", 
        "GET",
        "/users",
        Some(vec![
            create_test_parameter("maxResults", "max_results", "query", false, "integer"),
        ]),
    );

    operations_by_tag.insert("users".to_string(), vec![operation]);

    let result = generate_test_specifications(&operations_by_tag).unwrap();
    
    assert_eq!(result.len(), 1);
    let test_spec = result.get("users").unwrap();
    
    // Check structural tests
    assert_eq!(test_spec.structural_tests.len(), 1);
    let structural_test = &test_spec.structural_tests[0];
    assert_eq!(structural_test.methods.len(), 1);
    
    let method = &structural_test.methods[0];
    assert_eq!(method.method_name, "get_users");
    assert_eq!(method.class_name, "GetUsers");
    assert_eq!(method.return_type, "GetUsersResponse");
    assert!(!method.supports_pagination);

    // Check contract tests
    assert_eq!(test_spec.contract_tests.len(), 1);
    let contract_test = &test_spec.contract_tests[0];
    assert_eq!(contract_test.method_name, "get_users");
    assert_eq!(contract_test.class_name, "GetUsers");
    assert_eq!(contract_test.method, "GET");
    assert_eq!(contract_test.path, "/users");

    // Check mock scenarios
    assert_eq!(test_spec.mock_scenarios.len(), 3); // success, not_found, rate_limit
    let success_scenario = test_spec.mock_scenarios.iter()
        .find(|s| s.scenario_name == "success")
        .unwrap();
    assert_eq!(success_scenario.method_name, "get_users");
    assert_eq!(success_scenario.status_code, 200);
}

#[test]
fn test_generate_test_specifications_with_pagination() {
    let mut operations_by_tag = HashMap::new();
    
    let operation = create_test_operation(
        "get_tweets",
        "GetTweets",
        "GET", 
        "/tweets",
        Some(vec![
            create_test_parameter("pagination_token", "pagination_token", "query", false, "string"),
            create_test_parameter("max_results", "max_results", "query", false, "integer"),
            create_test_parameter("query", "query", "query", true, "string"),
        ]),
    );

    operations_by_tag.insert("tweets".to_string(), vec![operation]);

    let result = generate_test_specifications(&operations_by_tag).unwrap();
    let test_spec = result.get("tweets").unwrap();
    
    // Should detect pagination support
    let method = &test_spec.structural_tests[0].methods[0];
    assert!(method.supports_pagination);

    // Should have pagination tests
    assert_eq!(test_spec.pagination_tests.len(), 1);
    let pagination_test = &test_spec.pagination_tests[0];
    assert_eq!(pagination_test.method_name, "get_tweets");
    assert_eq!(pagination_test.token_param, Some("pagination_token".to_string()));
    assert_eq!(pagination_test.max_results_param, Some("max_results".to_string()));
}

#[test]
fn test_generate_test_specifications_multiple_operations() {
    let mut operations_by_tag = HashMap::new();
    
    let get_operation = create_test_operation(
        "get_user",
        "GetUser",
        "GET",
        "/users/{id}",
        Some(vec![
            create_test_parameter("id", "id", "path", true, "string"),
        ]),
    );

    let post_operation = create_test_operation(
        "create_user",
        "CreateUser", 
        "POST",
        "/users",
        None,
    );

    operations_by_tag.insert("users".to_string(), vec![get_operation, post_operation]);

    let result = generate_test_specifications(&operations_by_tag).unwrap();
    let test_spec = result.get("users").unwrap();
    
    // Should have 2 methods in structural tests
    assert_eq!(test_spec.structural_tests[0].methods.len(), 2);
    
    // Should have 2 contract tests
    assert_eq!(test_spec.contract_tests.len(), 2);
    
    // Should have 6 mock scenarios (3 per operation)
    assert_eq!(test_spec.mock_scenarios.len(), 6);
}

#[test]
fn test_generate_test_specifications_multiple_tags() {
    let mut operations_by_tag = HashMap::new();
    
    let users_operation = create_test_operation(
        "get_users",
        "GetUsers",
        "GET",
        "/users",
        None,
    );

    let tweets_operation = create_test_operation(
        "get_tweets", 
        "GetTweets",
        "GET",
        "/tweets",
        None,
    );

    operations_by_tag.insert("users".to_string(), vec![users_operation]);
    operations_by_tag.insert("tweets".to_string(), vec![tweets_operation]);

    let result = generate_test_specifications(&operations_by_tag).unwrap();
    
    assert_eq!(result.len(), 2);
    assert!(result.contains_key("users"));
    assert!(result.contains_key("tweets"));
}

#[test]
fn test_test_parameter_structure() {
    let test_param = TestParameter {
        name: "maxResults".to_string(),
        variable_name: "max_results".to_string(),
        param_type: "integer".to_string(),
        location: "query".to_string(),
        required: false,
        description: Some("Maximum number of results".to_string()),
    };

    assert_eq!(test_param.name, "maxResults");
    assert_eq!(test_param.variable_name, "max_results");
    assert_eq!(test_param.param_type, "integer");
    assert_eq!(test_param.location, "query");
    assert!(!test_param.required);
}

#[test]
fn test_method_signature_structure() {
    let method_sig = MethodSignature {
        method_name: "get_user".to_string(),
        class_name: "GetUser".to_string(),
        required_params: vec![],
        optional_params: vec![],
        return_type: "GetUserResponse".to_string(),
        supports_pagination: false,
    };

    assert_eq!(method_sig.method_name, "get_user");
    assert_eq!(method_sig.class_name, "GetUser");
    assert_eq!(method_sig.return_type, "GetUserResponse");
    assert!(!method_sig.supports_pagination);
}

#[test]
fn test_contract_test_structure() {
    let contract_test = ContractTest {
        method_name: "get_user".to_string(),
        class_name: "GetUser".to_string(),
        method: "GET".to_string(),
        path: "/users/{id}".to_string(),
        required_params: vec![],
        optional_params: vec![],
        request_body_schema: None,
        response_schema: xdk_lib::testing::ResponseSchema {
            status_code: 200,
            content_type: "application/json".to_string(),
            expected_fields: vec![],
        },
        security_requirements: vec![],
    };

    assert_eq!(contract_test.method_name, "get_user");
    assert_eq!(contract_test.class_name, "GetUser");
    assert_eq!(contract_test.method, "GET");
    assert_eq!(contract_test.path, "/users/{id}");
    assert_eq!(contract_test.response_schema.status_code, 200);
}

#[test]
fn test_pagination_test_structure() {
    let pagination_test = PaginationTest {
        method_name: "get_tweets".to_string(),
        required_params: vec![],
        token_param: Some("pagination_token".to_string()),
        max_results_param: Some("max_results".to_string()),
        next_token_field: Some("next_token".to_string()),
        data_field: "data".to_string(),
    };

    assert_eq!(pagination_test.method_name, "get_tweets");
    assert_eq!(pagination_test.token_param, Some("pagination_token".to_string()));
    assert_eq!(pagination_test.max_results_param, Some("max_results".to_string()));
}

#[test]
fn test_mock_scenario_structure() {
    let mock_scenario = MockScenario {
        method_name: "get_user".to_string(),
        scenario_name: "success".to_string(),
        status_code: 200,
        response_body: serde_json::json!({"id": "123", "name": "John Doe"}),
        request_params: std::collections::HashMap::new(),
        description: "Successful user retrieval".to_string(),
    };

    assert_eq!(mock_scenario.method_name, "get_user");
    assert_eq!(mock_scenario.scenario_name, "success");
    assert_eq!(mock_scenario.status_code, 200);
    assert_eq!(mock_scenario.description, "Successful user retrieval");
}

#[test]
fn test_test_specification_serialization() {
    use serde_json;

    let test_spec = TestSpecification {
        structural_tests: vec![],
        contract_tests: vec![],
        pagination_tests: vec![],
        mock_scenarios: vec![],
    };

    let json = serde_json::to_string(&test_spec).expect("Serialization should work");
    assert!(json.contains("structural_tests"));
    assert!(json.contains("contract_tests"));
    assert!(json.contains("pagination_tests"));
    assert!(json.contains("mock_scenarios"));
}

#[test]
fn test_pagination_detection_edge_cases() {
    // Test operation with only token param (no limit) - should not support pagination
    let operation_token_only = create_test_operation(
        "get_items",
        "GetItems",
        "GET",
        "/items",
        Some(vec![
            create_test_parameter("next_token", "next_token", "query", false, "string"),
        ]),
    );

    // Test operation with only limit param (no token) - should not support pagination  
    let operation_limit_only = create_test_operation(
        "get_data",
        "GetData",
        "GET", 
        "/data",
        Some(vec![
            create_test_parameter("limit", "limit", "query", false, "integer"),
        ]),
    );

    let mut operations_by_tag = HashMap::new();
    operations_by_tag.insert("test".to_string(), vec![operation_token_only, operation_limit_only]);

    let result = generate_test_specifications(&operations_by_tag).unwrap();
    let test_spec = result.get("test").unwrap();

    // Neither operation should support pagination
    for method in &test_spec.structural_tests[0].methods {
        assert!(!method.supports_pagination);
    }

    // Should have no pagination tests
    assert_eq!(test_spec.pagination_tests.len(), 0);
}