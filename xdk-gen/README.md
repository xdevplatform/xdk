
# XDK OpenAPI

A Rust library for parsing and working with OpenAPI 3.0.0 specifications.

This crate provides functionality to parse OpenAPI specifications from YAML or JSON formats and offers strongly-typed structures for working with the parsed data. It supports reference resolution, allowing you to handle complex OpenAPI specifications with components and references efficiently.

## Features

- **Parsing**: Parse OpenAPI 3.0.0 specifications from YAML or JSON.
- **Strong Typing**: Provides strongly-typed Rust structures for OpenAPI elements.
- **Reference Resolution**: Lazily resolves references to components with caching for efficiency.
- **Error Handling**: Comprehensive error handling via the `OpenApiError` enum.
- **Serialization**: Supports serialization and deserialization using `serde`, resolving references during serialization.

## Usage

To use this crate, you need to set up an `OpenApiContextGuard` to manage the thread-local context for reference resolution. Then, parse your OpenAPI specification using `parse_yaml` or `parse_json`. After parsing, you can access the API's components, resolving references as needed using the `try_resolve` method.

### Example

```rust
use xdk_openapi::{OpenApiContextGuard, parse_yaml};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let yaml = r#"
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      summary: Test endpoint
      operationId: getTest
      responses:
        '200':
          description: Successful response
"#;

    // Set up the context
    let _guard = OpenApiContextGuard::new();

    // Parse the OpenAPI spec
    let openapi = parse_yaml(yaml)?;

    // Access the parsed data
    assert_eq!(openapi.openapi, "3.0.0");
    assert_eq!(openapi.info.title, "Test API");
    assert_eq!(openapi.info.version, "1.0.0");

    // Access a path and operation
    let path_item = openapi.paths.get("/test").unwrap();
    let get_op = path_item.get.as_ref().unwrap();
    assert_eq!(get_op.summary, Some("Test endpoint".to_string()));

    Ok(())
}
```

### Handling References

Fields that may contain references (e.g., parameters, schemas) are represented as `RefOrValue<T>`. To access the actual value, call `try_resolve`, which resolves the reference using the context if necessary and caches the result.

```rust
// Example with parameters
let get_op = openapi.paths.get("/test").unwrap().get.as_ref().unwrap();
if let Some(params) = &get_op.parameters {
    for param in params {
        let resolved_param = param.try_resolve()?;
        println!("Parameter name: {}", resolved_param.name.unwrap());
    }
}
```

## Context Management

The `OpenApiContextGuard` establishes a thread-local context required for resolving references. During parsing, components are added to this context. Keep the guard alive for the duration of your parsing and processing to ensure the context remains available.

**Note**: Since the context is thread-local, parsing and reference resolution should occur in the same thread. In a multi-threaded application, set up a guard in each thread that needs to resolve references.

```rust
let _guard = OpenApiContextGuard::new(); // Context is set up
let openapi = parse_yaml(yaml)?;        // Parsing populates the context
// Process the openapi object here
// Context is dropped when _guard goes out of scope
```

## Key Data Structures

- **`OpenApi`**: The root object containing the specification's version, info, paths, and components.
- **`Info`**: Metadata about the API (title, version, etc.).
- **`PathItem`**: Operations (GET, POST, etc.) for a specific path.
- **`Operation`**: Details of an HTTP method, including parameters and responses.
- **`RefOrValue<T>`**: Represents a value or a reference to a component (e.g., `Parameter`, `Schema`).

For full details, see the [OpenAPI 3.0.0 Specification](https://swagger.io/specification/).

## Reference Resolution

References are resolved lazily when `try_resolve` is called, using the context populated during parsing. Resolved values are cached to improve performance. When serializing an `OpenApi` struct, references are automatically resolved and serialized as their actual values.

## Error Handling

Functions return `Result<T, OpenApiError>`, where `OpenApiError` covers parsing errors, reference resolution failures, and more. Always handle these results to manage potential issues.

```rust
match parse_yaml(yaml) {
    Ok(openapi) => println!("Parsed successfully: {:?}", openapi.info.title),
    Err(e) => eprintln!("Error: {:?}", e),
}
```

## Limitations

- Supports only OpenAPI 3.0.0 specifications.
- Reference resolution is limited to components within the same document.

## Use in SDK Generation

This crate is designed as a foundation for SDK generators. Parse an OpenAPI spec, traverse the `OpenApi` struct, resolve references, and generate code based on the resolved data.

## License

Licensed under the MIT License.

