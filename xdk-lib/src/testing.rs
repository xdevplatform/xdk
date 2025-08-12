//! Language-agnostic test generation for SDK code
//!
//! This module provides functionality to generate comprehensive test suites
//! for any language by analyzing OpenAPI specifications and generating
//! language-neutral test specifications that can be rendered using templates.
//!
//! # Overview
//!
//! The `testing.rs` module is a **language-agnostic test generation system** that analyzes
//! OpenAPI specifications and produces comprehensive test specifications that can be rendered
//! into any target language using templates.
//!
//! ## Architecture Overview
//!
//! ```text
//! OpenAPI Spec -> testing.rs -> TestSpecification -> Templates -> Language-specific tests
//! ```
//!
//! ## Core Components
//!
//! ### Main Entry Point
//! - `generate_test_specifications()` - Analyzes OpenAPI operations grouped by tags and produces a complete test specification
//!
//! ### Four Test Categories Generated
//!
//! #### Structural Tests (`StructuralTest`)
//! - **Purpose**: Validate that generated SDK has correct structure and API surface
//! - **Contains**: Client class names, method signatures, expected imports
//! - **Example**: Ensures `UsersClient` has `get_user()` method with correct parameters
//!
//! #### Contract Tests (`ContractTest`)
//! - **Purpose**: Validate request/response contracts match OpenAPI specification
//! - **Contains**: HTTP methods, paths, parameters, response schemas, security requirements
//! - **Example**: Ensures `GET /users/{id}` returns expected JSON structure with required fields
//!
//! #### Pagination Tests (`PaginationTest`)
//! - **Purpose**: Test pagination functionality using cursor-based patterns
//! - **Contains**: Token parameters, max results parameters, data field mappings
//! - **Example**: Tests that `get_tweets()` works with `next_token` and `max_results`
//!
//! #### Mock Scenarios (`MockScenario`)
//! - **Purpose**: Integration testing with various HTTP response scenarios
//! - **Contains**: Success (200), Not Found (404), Rate Limit (429) scenarios with mock data
//! - **Example**: Tests how SDK handles rate limiting responses
//!
//! ## Key Analysis Functions
//!
//! ### Parameter Extraction
//! ```ignore
//! extract_parameters() -> (required_params, optional_params)
//! ```
//! - Analyzes OpenAPI parameter definitions
//! - Categorizes by required/optional status
//! - Extracts types, locations (query/path/header), descriptions
//!
//! ### Pagination Detection
//! ```ignore
//! detect_pagination_support() -> bool
//! ```
//! - Scans for pagination indicators: `pagination_token`, `next_token`, `cursor`, `max_results`, `limit`
//! - Automatically identifies which operations support pagination
//!
//! ### Response Schema Analysis
//! ```ignore
//! generate_response_schema() -> ResponseSchema
//! ```
//! - Extracts expected response fields from OpenAPI schemas
//! - Handles nested objects, arrays, required fields
//! - Supports schema references and complex types
//!
//! ### Smart Mock Data Generation
//! ```ignore
//! generate_mock_from_schema() -> serde_json::Value
//! ```
//! - Creates realistic mock data from OpenAPI schemas
//! - Uses schema examples when available
//! - Handles complex types: objects, arrays, oneOf, allOf, anyOf
//! - Falls back to type-appropriate defaults
//!
//! ## Language-Agnostic Design
//!
//! The system generates **language-neutral specifications** that templates can consume:
//!
//! ```ignore
//! // Language-neutral parameter representation
//! TestParameter {
//!     name: "user_id",
//!     param_type: "string",
//!     location: "path",
//!     required: true,
//! }
//! ```
//!
//! Templates then convert this to language-specific code:
//! - **Python**: `def get_user(self, user_id: str) -> UserResponse:`
//! - **JavaScript**: `getUserId(userId: string): Promise<UserResponse>`
//! - **Go**: `func (c *Client) GetUser(userID string) (*UserResponse, error)`
//!
//! ## Integration with Generator
//!
//! Used by the main generator at `generator.rs:128-140`:
//!
//! ```ignore
//! use xdk_lib::utils::render_template;
//!
//! let test_spec = generate_test_specifications(&operations_by_tag)?;
//! let context = TestTemplateContext { tag, test_spec };
//!
//! // Render language-specific tests using templates
//! render_template("test_structure.j2", &context)?;
//! render_template("test_contracts.j2", &context)?;
//! render_template("test_pagination.j2", &context)?;
//! ```
//!
//! ## Smart Features
//!
//! 1. **Schema-Aware Mock Generation**: Uses actual OpenAPI schemas to generate realistic test data
//! 2. **Automatic Pagination Detection**: Identifies paginated endpoints without manual configuration
//! 3. **Comprehensive Coverage**: Generates 3 test types per API tag (structure, contracts, pagination)
//! 4. **Fallback Handling**: Graceful degradation when schema information is incomplete
//! 5. **Security Context**: Extracts and includes security requirements in contract tests
//!
//! This system enables the XDK generator to produce comprehensive, realistic test suites for any
//! target language while maintaining consistency and leveraging the full OpenAPI specification.
use crate::models::OperationInfo;
use openapi::{RefOrValue, RequestBody, Schema, TypedSchema};
use serde::Serialize;
use std::collections::HashMap;

/// Complete test specification for an API
#[derive(Debug, Serialize, Clone)]
pub struct TestSpecification {
    /// Tests for validating SDK structure and API surface
    pub structural_tests: Vec<StructuralTest>,
    /// Tests for validating request/response contracts
    pub contract_tests: Vec<ContractTest>,
    /// Tests for pagination functionality
    pub pagination_tests: Vec<PaginationTest>,
    /// Mock response scenarios for integration testing
    pub mock_scenarios: Vec<MockScenario>,
}

/// Test specification for validating SDK structure
#[derive(Debug, Serialize, Clone)]
pub struct StructuralTest {
    /// Name of the client class/module being tested
    pub client_name: String,
    /// Methods that should exist on this client
    pub methods: Vec<MethodSignature>,
    /// Expected imports/dependencies
    pub expected_imports: Vec<String>,
}

/// Method signature information for structural testing
#[derive(Debug, Serialize, Clone)]
pub struct MethodSignature {
    /// Method name (e.g., "get_users") - cased for the target language
    pub method_name: String,
    /// Class name (e.g., "GetUsers") - for Request/Response models
    pub class_name: String,
    /// Required parameters
    pub required_params: Vec<TestParameter>,
    /// Optional parameters
    pub optional_params: Vec<TestParameter>,
    /// Return type information
    pub return_type: String,
    /// Whether this method supports pagination
    pub supports_pagination: bool,
}

/// Parameter information for testing
#[derive(Debug, Serialize, Clone)]
pub struct TestParameter {
    /// Parameter name (original from OpenAPI)
    pub name: String,
    /// Variable name (cased for the target language)
    pub variable_name: String,
    /// Parameter type (language-neutral)
    pub param_type: String,
    /// Where the parameter goes (query, path, header, body)
    pub location: String,
    /// Whether the parameter is required
    pub required: bool,
    /// Description for documentation
    pub description: Option<String>,
}

/// Contract test specification
#[derive(Debug, Serialize, Clone)]
pub struct ContractTest {
    /// Method name (cased for target language, e.g., "get_users")
    pub method_name: String,
    /// Class name (cased for models, e.g., "GetUsers")
    pub class_name: String,
    /// HTTP method
    pub method: String,
    /// URL path template
    pub path: String,
    /// Required parameters for this operation
    pub required_params: Vec<TestParameter>,
    /// Optional parameters for this operation
    pub optional_params: Vec<TestParameter>,
    /// Request body schema
    pub request_body_schema: Option<RequestBody>,
    /// Expected response schema information
    pub response_schema: ResponseSchema,
    /// Security requirements
    pub security_requirements: Vec<String>,
}

/// Response schema information for contract testing
#[derive(Debug, Serialize, Clone)]
pub struct ResponseSchema {
    /// Status code this schema applies to
    pub status_code: u16,
    /// Content type (e.g., "application/json")
    pub content_type: String,
    /// Fields that should be present in the response
    pub expected_fields: Vec<ResponseField>,
}

/// Field information in response schema
#[derive(Debug, Serialize, Clone)]
pub struct ResponseField {
    /// Field name
    pub name: String,
    /// Field type
    pub field_type: String,
    /// Whether field is required
    pub required: bool,
    /// Whether field is an array
    pub is_array: bool,
}

/// Pagination test specification
#[derive(Debug, Serialize, Clone)]
pub struct PaginationTest {
    /// Method name for testing
    pub method_name: String,
    /// Required parameters for this operation (excluding pagination params)
    pub required_params: Vec<TestParameter>,
    /// Pagination token parameter name
    pub token_param: Option<String>,
    /// Max results parameter name
    pub max_results_param: Option<String>,
    /// Response field containing next token
    pub next_token_field: Option<String>,
    /// Response field containing data array
    pub data_field: String,
}

/// Mock scenario for integration testing
#[derive(Debug, Serialize, Clone)]
pub struct MockScenario {
    /// Method name this scenario tests
    pub method_name: String,
    /// Scenario name (e.g., "success", "not_found", "rate_limit")
    pub scenario_name: String,
    /// HTTP status code to mock
    pub status_code: u16,
    /// Mock response body
    pub response_body: serde_json::Value,
    /// Request parameters for this scenario
    pub request_params: HashMap<String, serde_json::Value>,
    /// Description of what this scenario tests
    pub description: String,
}

/// Generate comprehensive test specifications from OpenAPI spec
pub fn generate_test_specifications(
    operations_by_tag: &HashMap<String, Vec<OperationInfo>>,
) -> crate::Result<HashMap<String, TestSpecification>> {
    let mut test_specifications = HashMap::new();

    for (tag, operations) in operations_by_tag {
        let mut structural_tests = Vec::new();
        let mut contract_tests = Vec::new();
        let mut pagination_tests = Vec::new();
        let mut mock_scenarios = Vec::new();

        // Generate structural tests for this tag
        let structural_test = generate_structural_test(tag, operations);
        structural_tests.push(structural_test);

        // Generate contract and mock tests for each operation
        for operation in operations {
            let contract_test = generate_contract_test(operation);
            contract_tests.push(contract_test);

            // Generate pagination tests if operation supports pagination
            if detect_pagination_support(operation) {
                let pagination_test = generate_pagination_test(operation);
                pagination_tests.push(pagination_test);
            }

            // Generate mock scenarios for this operation
            let scenarios = generate_mock_scenarios(operation);
            mock_scenarios.extend(scenarios);
        }

        test_specifications.insert(
            tag.to_string(),
            TestSpecification {
                structural_tests,
                contract_tests,
                pagination_tests,
                mock_scenarios,
            },
        );
    }

    Ok(test_specifications)
}

/// Generate structural test for a tag/client
fn generate_structural_test(tag: &str, operations: &[OperationInfo]) -> StructuralTest {
    let methods: Vec<MethodSignature> = operations.iter().map(generate_method_signature).collect();

    StructuralTest {
        client_name: format!("{}Client", tag),
        methods,
        expected_imports: vec![
            "typing".to_string(),
            "requests".to_string(),
            "pydantic".to_string(),
        ],
    }
}

/// Generate method signature from operation info
fn generate_method_signature(operation: &OperationInfo) -> MethodSignature {
    let (required_params, optional_params) = extract_parameters(operation);

    MethodSignature {
        method_name: operation.method_name.clone(),
        class_name: operation.class_name.clone(),
        required_params,
        optional_params,
        return_type: format!("{}Response", operation.class_name),
        supports_pagination: detect_pagination_support(operation),
    }
}

/// Extract parameters from operation (convert ParameterInfo to TestParameter)
fn extract_parameters(operation: &OperationInfo) -> (Vec<TestParameter>, Vec<TestParameter>) {
    let mut required_params = Vec::new();
    let mut optional_params = Vec::new();

    if let Some(parameters) = &operation.parameters {
        for param in parameters {
            // Only include path and query parameters for testing
            if param.location == "path" || param.location == "query" {
                let test_param = TestParameter {
                    name: param.original_name.clone(),
                    variable_name: param.variable_name.clone(), // Already cased
                    param_type: param.param_type.clone(),
                    location: param.location.clone(),
                    required: param.required,
                    description: param.description.clone(),
                };

                if param.required {
                    required_params.push(test_param);
                } else {
                    optional_params.push(test_param);
                }
            }
        }
    }

    (required_params, optional_params)
}

/// Generate contract test from operation
fn generate_contract_test(operation: &OperationInfo) -> ContractTest {
    let (required_params, optional_params) = extract_parameters(operation);

    ContractTest {
        method_name: operation.method_name.clone(),
        class_name: operation.class_name.clone(),
        method: operation.method.clone(),
        path: operation.path.clone(),
        required_params,
        optional_params,
        request_body_schema: generate_request_body_schema(operation),
        response_schema: generate_response_schema(operation),
        security_requirements: extract_security_requirements(operation),
    }
}

/// Generate response schema information
fn generate_response_schema(operation: &OperationInfo) -> ResponseSchema {
    // Try to find 200 response
    if let Some(response) = operation.responses.get("200") {
        ResponseSchema {
            status_code: 200,
            content_type: "application/json".to_string(),
            expected_fields: extract_response_fields(response),
        }
    } else {
        // Fallback to first available response
        let default_status = "200".to_string();
        let default_response = openapi::Response {
            description: None,
            content: None,
        };
        let (status_code, response) = operation
            .responses
            .iter()
            .next()
            .unwrap_or((&default_status, &default_response));

        ResponseSchema {
            status_code: status_code.parse().unwrap_or(200),
            content_type: "application/json".to_string(),
            expected_fields: extract_response_fields(response),
        }
    }
}

/// Generate request body schema information
fn generate_request_body_schema(operation: &OperationInfo) -> Option<RequestBody> {
    operation.request_body.clone()
}

/// Extract response fields from response schema
fn extract_response_fields(response: &openapi::Response) -> Vec<ResponseField> {
    let mut fields = Vec::new();

    if let Some(content) = &response.content {
        if let Some(json_content) = content.get("application/json") {
            fields.extend(extract_fields_from_schema(&json_content.schema));
        }
    }

    fields
}

/// Extract fields from schema recursively
fn extract_fields_from_schema(schema: &RefOrValue<Schema>) -> Vec<ResponseField> {
    let mut fields = Vec::new();

    match schema {
        RefOrValue::Value(schema) => {
            if let Schema::Typed(typed) = schema {
                if let TypedSchema::Object(obj) = typed.as_ref() {
                    if let Some(properties) = &obj.properties {
                        for (name, prop_schema) in properties {
                            fields.push(ResponseField {
                                name: name.clone(),
                                field_type: get_schema_type(prop_schema),
                                required: obj.required.as_ref()
                                    .map(|req| req.contains(name))
                                    .unwrap_or(false),
                                is_array: matches!(prop_schema, RefOrValue::Value(Schema::Typed(t)) if matches!(t.as_ref(), TypedSchema::Array(_))),
                            });
                        }
                    }
                }
            }
        }
        RefOrValue::Reference { .. } => {
            // For references, we'd need to resolve them from components
            // For now, add a generic field
            fields.push(ResponseField {
                name: "data".to_string(),
                field_type: "any".to_string(),
                required: false,
                is_array: false,
            });
        }
    }

    fields
}

/// Get type string from schema
fn get_schema_type(schema: &RefOrValue<Schema>) -> String {
    match schema {
        RefOrValue::Value(schema) => match schema {
            Schema::Typed(typed) => match typed.as_ref() {
                TypedSchema::String(_) => "string".to_string(),
                TypedSchema::Integer(_) => "integer".to_string(),
                TypedSchema::Number(_) => "number".to_string(),
                TypedSchema::Boolean(_) => "boolean".to_string(),
                TypedSchema::Array(_) => "array".to_string(),
                TypedSchema::Object(_) => "object".to_string(),
            },
            _ => "any".to_string(),
        },
        RefOrValue::Reference { .. } => "reference".to_string(),
    }
}

/// Extract security requirements from operation
fn extract_security_requirements(operation: &OperationInfo) -> Vec<String> {
    if let Some(security) = &operation.security {
        security
            .iter()
            .flat_map(|req| req.0.keys())
            .cloned()
            .collect()
    } else {
        Vec::new()
    }
}

/// Detect if operation supports pagination
/// Requires both a pagination token parameter AND a limit parameter for true pagination
fn detect_pagination_support(operation: &OperationInfo) -> bool {
    if let Some(parameters) = &operation.parameters {
        let has_token = parameters.iter().any(|param| {
            matches!(
                param.original_name.as_str(),
                "pagination_token" | "next_token" | "cursor"
            )
        });

        let has_limit = parameters.iter().any(|param| {
            matches!(
                param.original_name.as_str(),
                "max_results" | "limit" | "count"
            )
        });

        // Require BOTH token and limit parameters for true pagination support
        has_token && has_limit
    } else {
        false
    }
}

/// Generate pagination test for operation
fn generate_pagination_test(operation: &OperationInfo) -> PaginationTest {
    let (required_params, _optional_params) = extract_parameters(operation);
    let (token_param, max_results_param) = extract_pagination_params(operation);

    // Filter out pagination parameters from required params
    let filtered_required_params: Vec<TestParameter> = required_params
        .into_iter()
        .filter(|param| {
            !matches!(
                param.name.as_str(),
                "pagination_token" | "next_token" | "cursor" | "max_results" | "limit" | "count"
            )
        })
        .collect();

    PaginationTest {
        method_name: operation.method_name.clone(),
        required_params: filtered_required_params,
        token_param,
        max_results_param,
        next_token_field: Some("meta.next_token".to_string()),
        data_field: "data".to_string(),
    }
}

/// Extract pagination parameter names
fn extract_pagination_params(operation: &OperationInfo) -> (Option<String>, Option<String>) {
    let mut token_param = None;
    let mut max_results_param = None;

    if let Some(parameters) = &operation.parameters {
        for param in parameters {
            match param.original_name.as_str() {
                "pagination_token" | "next_token" | "cursor" => {
                    token_param = Some(param.original_name.clone());
                }
                "max_results" | "limit" | "count" => {
                    max_results_param = Some(param.original_name.clone());
                }
                _ => {}
            }
        }
    }

    (token_param, max_results_param)
}

/// Generate mock scenarios for an operation
fn generate_mock_scenarios(operation: &OperationInfo) -> Vec<MockScenario> {
    let mut scenarios = Vec::new();

    // Success scenario
    scenarios.push(MockScenario {
        method_name: operation.method_name.clone(),
        scenario_name: "success".to_string(),
        status_code: 200,
        response_body: generate_success_response(operation),
        request_params: generate_request_params(operation),
        description: "Successful response scenario".to_string(),
    });

    // Error scenarios
    scenarios.push(MockScenario {
        method_name: operation.method_name.clone(),
        scenario_name: "not_found".to_string(),
        status_code: 404,
        response_body: serde_json::json!({
            "error": {
                "type": "not_found",
                "message": "Resource not found"
            }
        }),
        request_params: generate_request_params(operation),
        description: "Resource not found scenario".to_string(),
    });

    scenarios.push(MockScenario {
        method_name: operation.method_name.clone(),
        scenario_name: "rate_limit".to_string(),
        status_code: 429,
        response_body: serde_json::json!({
            "error": {
                "type": "rate_limit_exceeded",
                "message": "Rate limit exceeded"
            }
        }),
        request_params: generate_request_params(operation),
        description: "Rate limit exceeded scenario".to_string(),
    });

    scenarios
}

/// Generate success response mock data from OpenAPI schema
fn generate_success_response(operation: &OperationInfo) -> serde_json::Value {
    // Try to generate response based on actual OpenAPI response schema
    if let Some(response) = operation.responses.get("200") {
        if let Some(mock_data) = generate_mock_from_response_schema(response) {
            return mock_data;
        }
    }

    // Fallback to simple mock response
    if detect_pagination_support(operation) {
        serde_json::json!({
            "data": [
                {"id": "1", "name": "Test Item 1"},
                {"id": "2", "name": "Test Item 2"}
            ],
            "meta": {
                "result_count": 2,
                "next_token": "next_page_token"
            }
        })
    } else {
        serde_json::json!({
            "data": {"id": "1", "name": "Test Item"}
        })
    }
}

/// Generate request parameters for testing using OpenAPI schema information
fn generate_request_params(operation: &OperationInfo) -> HashMap<String, serde_json::Value> {
    let mut params = HashMap::new();

    if let Some(parameters) = &operation.parameters {
        for param in parameters {
            // Try to generate value from schema first
            let value = if let Some(schema) = &param.schema {
                generate_mock_from_schema(schema).unwrap_or_else(|| {
                    // Fallback to simple type-based generation
                    generate_simple_param_value(&param.param_type)
                })
            } else {
                // Fallback to simple type-based generation
                generate_simple_param_value(&param.param_type)
            };

            params.insert(param.original_name.clone(), value);
        }
    }

    // Add some common path parameters if not present
    if params.is_empty() {
        params.insert(
            "id".to_string(),
            serde_json::Value::String("test_id".to_string()),
        );
    }

    params
}

/// Generate simple parameter value based on type
fn generate_simple_param_value(param_type: &str) -> serde_json::Value {
    match param_type {
        "string" => serde_json::Value::String("test_value".to_string()),
        "integer" => serde_json::Value::Number(serde_json::Number::from(42)),
        "number" => serde_json::Value::Number(serde_json::Number::from(42)),
        "boolean" => serde_json::Value::Bool(true),
        "array" => serde_json::json!(["item1", "item2"]),
        _ => serde_json::Value::String("test".to_string()),
    }
}

/// Generate mock data from OpenAPI response schema
fn generate_mock_from_response_schema(response: &openapi::Response) -> Option<serde_json::Value> {
    if let Some(content) = &response.content {
        if let Some(json_content) = content.get("application/json") {
            return generate_mock_from_schema(&json_content.schema);
        }
    }
    None
}

/// Generate mock data from OpenAPI schema
fn generate_mock_from_schema(schema: &RefOrValue<Schema>) -> Option<serde_json::Value> {
    match schema {
        RefOrValue::Value(schema) => {
            match schema {
                Schema::Typed(typed) => {
                    match typed.as_ref() {
                        TypedSchema::String(string_schema) => {
                            // Use example if available
                            if let Some(example) = &string_schema.base.example {
                                if let serde_json::Value::String(s) = example {
                                    Some(serde_json::Value::String(s.clone()))
                                } else {
                                    Some(example.clone())
                                }
                            } else if let Some(enum_values) = &string_schema.enum_values {
                                // Use first enum value if available
                                if let Some(first_value) = enum_values.first() {
                                    Some(serde_json::Value::String(first_value.clone()))
                                } else {
                                    Some(serde_json::Value::String("test_string".to_string()))
                                }
                            } else {
                                Some(serde_json::Value::String("test_string".to_string()))
                            }
                        }
                        TypedSchema::Integer(int_schema) => {
                            if let Some(example) = &int_schema.base.example {
                                if let serde_json::Value::Number(n) = example {
                                    Some(serde_json::Value::Number(n.clone()))
                                } else {
                                    Some(example.clone())
                                }
                            } else {
                                Some(serde_json::Value::Number(serde_json::Number::from(42)))
                            }
                        }
                        TypedSchema::Number(num_schema) => {
                            if let Some(example) = &num_schema.base.example {
                                if let serde_json::Value::Number(n) = example {
                                    Some(serde_json::Value::Number(n.clone()))
                                } else {
                                    Some(example.clone())
                                }
                            } else {
                                Some(serde_json::Value::Number(serde_json::Number::from(42)))
                            }
                        }
                        TypedSchema::Boolean(bool_schema) => {
                            if let Some(example) = &bool_schema.base.example {
                                if let serde_json::Value::Bool(b) = example {
                                    Some(serde_json::Value::Bool(*b))
                                } else {
                                    Some(example.clone())
                                }
                            } else {
                                Some(serde_json::Value::Bool(true))
                            }
                        }
                        TypedSchema::Array(array_schema) => {
                            if let Some(items_schema) = &array_schema.items {
                                // Generate 2-3 items for the array
                                let item1 = generate_mock_from_schema(items_schema)?;
                                let item2 = generate_mock_from_schema(items_schema)?;
                                Some(serde_json::json!([item1, item2]))
                            } else {
                                Some(serde_json::json!(["item1", "item2"]))
                            }
                        }
                        TypedSchema::Object(obj_schema) => {
                            let mut obj = serde_json::Map::new();

                            if let Some(properties) = &obj_schema.properties {
                                for (name, prop_schema) in properties {
                                    if let Some(value) = generate_mock_from_schema(prop_schema) {
                                        obj.insert(name.clone(), value);
                                    }
                                }
                            }

                            // If no properties, add some default fields
                            if obj.is_empty() {
                                obj.insert(
                                    "id".to_string(),
                                    serde_json::Value::String("1".to_string()),
                                );
                                obj.insert(
                                    "name".to_string(),
                                    serde_json::Value::String("Test Item".to_string()),
                                );
                            }

                            Some(serde_json::Value::Object(obj))
                        }
                    }
                }
                Schema::OneOf(one_of_schemas) => {
                    // Use first schema in oneOf
                    if let Some(first_schema) = one_of_schemas.one_of.first() {
                        generate_mock_from_schema(first_schema)
                    } else {
                        None
                    }
                }
                Schema::AnyOf(any_of_schemas) => {
                    // Use first schema in anyOf
                    if let Some(first_schema) = any_of_schemas.any_of.first() {
                        generate_mock_from_schema(first_schema)
                    } else {
                        None
                    }
                }
                Schema::AllOf(all_of_schemas) => {
                    // Merge all schemas in allOf (simplified implementation)
                    let mut merged_obj = serde_json::Map::new();

                    for schema in &all_of_schemas.all_of {
                        if let Some(serde_json::Value::Object(obj)) =
                            generate_mock_from_schema(schema)
                        {
                            for (key, value) in obj {
                                merged_obj.insert(key, value);
                            }
                        }
                    }

                    if merged_obj.is_empty() {
                        None
                    } else {
                        Some(serde_json::Value::Object(merged_obj))
                    }
                }
                _ => None,
            }
        }
        RefOrValue::Reference { .. } => {
            // For references, we'd need to resolve them from components
            // For now, return a generic object
            Some(serde_json::json!({
                "id": "1",
                "name": "Referenced Item"
            }))
        }
    }
}
