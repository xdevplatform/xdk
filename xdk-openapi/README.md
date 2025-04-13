# XDK OpenAPI Parser

A minimal OpenAPI 3.0.0 specification parser for Rust.

## Features

- Parse OpenAPI 3.0.0 specifications from YAML or JSON
- Support for core OpenAPI elements:
  - Info
  - Paths
  - Components (schemas, parameters, security schemes)
  - Security

## Usage

Add the dependency to your `Cargo.toml`:

```toml
[dependencies]
xdk-openapi = "0.1.0"
```

### Parse from YAML

```rust
use xdk_openapi::{parse_yaml, parse_yaml_file};

// Parse from a string
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
"#;
let openapi = parse_yaml(yaml)?;

// Parse from a file
let openapi = parse_yaml_file("path/to/openapi.yaml")?;
```

### Parse from JSON

```rust
use xdk_openapi::{parse_json, parse_json_file};

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
            "description": "Successful response"
          }
        }
      }
    }
  }
}"#;
let openapi = parse_json(json)?;

// Parse from a file
let openapi = parse_json_file("path/to/openapi.json")?;
```

## Examples

Check out the [examples](examples) directory for more usage examples.

## License

MIT 