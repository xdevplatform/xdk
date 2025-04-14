# XDK OpenAPI

A Rust library for parsing and working with OpenAPI 3.0.0 specifications.

This crate provides functionality to parse OpenAPI specifications from YAML or JSON formats,
and provides strongly-typed structures for working with the parsed data.

## Features

- Parse OpenAPI 3.0.0 specifications from YAML or JSON
- Strongly-typed representation of OpenAPI elements
- **Lazy resolution** of references (`$ref`)
- Support for reusable components
- Comprehensive error handling

## Usage

Add the dependency to your `Cargo.toml`:

```toml
[dependencies]
xdk-openapi = "0.1.0"
```

### Parsing and Context

This library uses a context (`OpenApiContext`) to manage the resolution of references (`$ref`) within the specification. Components defined in the `#/components` section are pre-parsed and stored in this context.

To ensure the context is available during parsing and subsequent reference resolution, you typically need to create an `OpenApiContextGuard` *before* calling the parsing functions (`parse_yaml`, `parse_json`, etc.). This guard initializes a thread-local context and cleans it up when it goes out of scope.

```rust
use xdk_openapi::{parse_yaml, OpenApiContextGuard};

// Create the guard. This sets up the context.
let _guard = OpenApiContextGuard::new(); 

let yaml = /* ... your YAML string ... */;

// The context is now available for parsing and reference resolution.
let result = parse_yaml(yaml);

// The guard goes out of scope here, cleaning up the context.
```

### Parse from YAML

```rust
use xdk_openapi::{parse_yaml, OpenApiContextGuard};

// Guard is needed for potential reference resolution
let _guard = OpenApiContextGuard::new();

let yaml = r#"
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        message:
          type: string
"#;

let result = parse_yaml(yaml);
assert!(result.is_ok());
let openapi = result.unwrap();
assert_eq!(openapi.openapi, "3.0.0");
assert_eq!(openapi.info.title, "Test API");
assert_eq!(openapi.info.version, "1.0.0");

// Accessing the referenced schema
let response_schema = openapi.paths.get("/test")
    .unwrap().get.as_ref()
    .unwrap().responses.get("200")
    .unwrap().clone_inner() // Resolves RefOrValue<Response>
    .content.unwrap()
    .get("application/json").unwrap()
    .schema.clone_inner(); // Resolves RefOrValue<Schema>

assert_eq!(response_schema.r#type.unwrap(), "object");

// Parse from a file (guard still required)
// let _guard = OpenApiContextGuard::new();
// let openapi_from_file = parse_yaml_file("path/to/openapi.yaml")?;
```

### Parse from JSON

```rust
use xdk_openapi::{parse_json, parse_json_file, OpenApiContextGuard};

// Guard is needed for potential reference resolution
let _guard = OpenApiContextGuard::new();

// Parse from a string
let json = r#"{
  "openapi": "3.0.0",
  "info": {
    "title": "Test API",
    "version": "1.0.0"
  },
  "paths": {
    "/test": {
      "get": {
        "summary": "Test endpoint",
        "responses": {
          "200": {
            "$ref": "#/components/responses/Success"
          }
        }
      }
    }
  },
  "components": {
    "responses": {
      "Success": {
        "description": "Successful response",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                 "status": { "type": "string" }
              }
            }
          }
        }
      }
    }
  }
}"#;

let result = parse_json(json);
assert!(result.is_ok());
let openapi = result.unwrap();

// Accessing the referenced response
let response = openapi.paths.get("/test")
    .unwrap().get.as_ref()
    .unwrap().responses.get("200")
    .unwrap().clone_inner(); // Resolves RefOrValue<Response>

assert_eq!(response.description, "Successful response");


// Parse from a file (guard still required)
// let _guard = OpenApiContextGuard::new();
// let openapi_from_file = parse_json_file("path/to/openapi.json")?;
```

### Handling References (`$ref`)

Many parts of an OpenAPI specification can either be defined inline or as a reference to a component in the `#/components` section (e.g., schemas, parameters, responses). This library handles this using the `RefOrValue<T>` enum.

- **`RefOrValue::Value(T)`**: Contains the actual value (e.g., a `Schema` struct).
- **`RefOrValue::Reference { path, resolved }`**: Contains the reference path string (e.g., `#/components/schemas/MySchema`).

**Lazy Resolution:**
When the specification is parsed, references are *not* immediately resolved. The `RefOrValue::Reference` variant is created, but the actual lookup happens only when you try to access the underlying value.

**Accessing Referenced Values:**
You can access the underlying value (resolving the reference if necessary) using methods like:

- **`.clone_inner()`**: Resolves the reference (if it's one) and returns a *clone* of the underlying value. Panics if the reference cannot be resolved.
- **`.try_resolve()`**: Attempts to resolve the reference and returns a `Result<Rc<T>, OpenApiError>`. This is useful for handling potential resolution errors. If it was a `Value`, it returns `Ok(Rc::new(value.clone()))`.
- **`.as_ref()`**: Resolves the reference and returns an `Rc<T>`. Panics if the reference cannot be resolved.

```rust
# use xdk_openapi::{parse_yaml, OpenApiContextGuard, RefOrValue, Schema};
# let _guard = OpenApiContextGuard::new();
# let yaml = r#"
# openapi: 3.0.0
# info:
#   title: Test API
#   version: 1.0.0
# paths:
#   /test:
#     get:
#       parameters:
#         - name: limit
#           in: query
#           schema:
#             type: integer
#         - $ref: '#/components/parameters/OffsetParam'
# components:
#   parameters:
#     OffsetParam:
#       name: offset
#       in: query
#       schema:
#         type: integer
# "#;
# let openapi = parse_yaml(yaml).unwrap();

let parameters = openapi.paths.get("/test").unwrap().get.as_ref().unwrap().parameters.as_ref().unwrap();

let param1_ref_or_value = &parameters[0]; // Direct value
let param2_ref_or_value = &parameters[1]; // Reference

// Using clone_inner (panics on resolution error)
let param1 = param1_ref_or_value.clone_inner();
let param2 = param2_ref_or_value.clone_inner();
assert_eq!(param1.name.unwrap(), "limit");
assert_eq!(param2.name.unwrap(), "offset");

// Using try_resolve (allows error handling)
match param2_ref_or_value.try_resolve() {
    Ok(param2_rc) => {
        assert_eq!(param2_rc.name.as_deref(), Some("offset"));
    }
    Err(e) => {
        eprintln!("Failed to resolve reference: {}", e);
    }
}
```

Remember that reference resolution requires the `OpenApiContext` to be available, which is typically managed by the `OpenApiContextGuard` as shown in the parsing examples.

## Examples

Check out the [examples](examples) directory for more usage examples.

## License

MIT