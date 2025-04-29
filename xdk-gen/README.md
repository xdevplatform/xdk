# XDK Generator

A Rust crate for generating language-specific SDKs from OpenAPI specifications.

## Overview

The XDK Generator is a powerful tool that automatically generates Software Development Kits (SDKs) for various programming languages based on OpenAPI specifications. It provides a modular and extensible framework for creating language-specific SDK generators.

## Features

- Modular architecture for language-specific generators
- Built on top of `xdk-lib` for common operations
- Uses OpenAPI specifications as input
- Template-based code generation using `minijinja`
- Extensible design for adding new language support

## Supported Languages

Currently supports:
- Python

## Usage

Add the following to your `Cargo.toml`:

```toml
[dependencies]
xdk-gen = "0.1.0"
```

## Creating a New Language Generator

To create a generator for a new language:

1. Create a new module folder (e.g., `javascript/`)
2. Implement the following required files:
   - `mod.rs`: Module exports and potentially tests
   - `generator.rs`: Implementation of the generator using the `language!` macro

Everything else (parsing, utilities, error handling) is abstracted in the `xdk-lib` crate.

## Dependencies

- `xdk-openapi`: For OpenAPI specification handling
- `xdk-lib`: Core library for common operations
- `minijinja`: Template engine for code generation
- `serde`: Serialization/deserialization
- `serde_json`: JSON handling
- `thiserror`: Error handling

## Example

See the `python` module for a reference implementation of a language generator.

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
