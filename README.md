# XDK Project

## Overview

Welcome to the XDK project! This repository contains a collection of Rust crates designed for generating and managing SDKs (or XDKs) for the X APIs. The project focuses on creating high-quality, type-safe SDKs for various programming languages, starting with Python, from OpenAPI specifications.

## Components

The project is organized into several crates within this workspace:

*   `xdk-gen`: A code generation library that transforms OpenAPI specifications into language-specific SDKs.
*   `xdk-build`: A command-line tool for building and generating SDKs from OpenAPI specifications. Provides a user-friendly interface for the code generation process.
*   `xdk-openapi`: A minimal OpenAPI 3.0.0 specification parser. (See [`xdk-openapi/README.md`](xdk-openapi/README.md) for details)
*   `assets`: Contains shared assets, examples, or configuration files used by the project.

## Getting Started

### Prerequisites

*   Rust toolchain (install via [rustup](https://rustup.rs/))

### Building

To build all crates in the workspace, run the following command from the root directory:

```bash
cargo build
```

To build a specific crate, use the `-p` flag:

```bash
cargo build -p xdk-openapi
```

### Running Tests

To run tests for all crates:

```bash
cargo test
```

To run tests for a specific crate:

```bash
cargo test -p xdk-openapi
```

### Generating SDKs

To generate a Python SDK from an OpenAPI specification:

```bash
cargo run -p xdk-build -- python --spec path/to/openapi.yaml --output path/to/output
```

## License

This project is licensed under the MIT License. See the `LICENSE` file (if available) or individual crate licenses for details. 