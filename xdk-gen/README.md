# XDK Generator

A Rust library for generating language-specific SDKs from OpenAPI specifications.

## Features

- Transform OpenAPI 3.0.0 specifications into language-specific SDKs
- Template-based code generation using Minijinja
- Extensible architecture for adding support for more languages

## Usage

Add the dependency to your `Cargo.toml`:

```toml
[dependencies]
xdk-gen = "0.1.0"
```

### Generating a Python SDK

```rust
use xdk_gen::{generate_python_sdk, error::Result};
use xdk_openapi::{parse_yaml, OpenApiContextGuard};
use std::path::Path;

fn main() -> Result<()> {
    // Create a guard for the OpenAPI context
    let _guard = OpenApiContextGuard::new();
    
    // Parse the OpenAPI specification
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
    
    // Generate the Python SDK
    let output_dir = Path::new("output/python-sdk");
    generate_python_sdk(&openapi, output_dir)?;
    
    println!("Python SDK generated successfully at {}", output_dir.display());
    Ok(())
}
```

## Templates

The generator uses Minijinja templates to create the SDK code. Templates are located in the `templates` directory:

- `templates/python/`: Templates for Python SDK generation
  - `client_class.j2`: Template for client class generation
  - `client_module.j2`: Template for client module generation
  - `main_client.j2`: Template for the main client class
  - `clients.j2`: Template for client implementations
  - `client.j2`: Template for client base class
  - `requirements_txt.j2`: Template for requirements.txt
  - `readme.j2`: Template for README.md
  - `setup_py.j2`: Template for setup.py
  - `init_py.j2`: Template for __init__.py

## Examples

Check out the [examples](examples) directory for more usage examples:

- `generate_python_sdk.rs`: Example of generating a Python SDK from an OpenAPI specification

## License

MIT 