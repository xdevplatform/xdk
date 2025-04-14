# XDK Builder

A command-line tool for building and generating SDKs from OpenAPI specifications.

## Features

- Generate language-specific SDKs from OpenAPI specifications
- User-friendly command-line interface using Clap
- Supports both YAML and JSON OpenAPI specifications

## Installation

```bash
cargo install xdk-build
```

## Usage

### Command-line Interface

```bash
xdk-build [OPTIONS] <COMMAND>
```

### Commands

#### Python

Generate a Python SDK from an OpenAPI specification:

```bash
xdk-build python --spec <SPEC_FILE> --output <OUTPUT_DIR>
```

Options:
- `-s, --spec <SPEC_FILE>`: Path to the OpenAPI specification file (YAML or JSON)
- `-o, --output <OUTPUT_DIR>`: Output directory for the generated SDK (default: "xdk/python")

Example:

```bash
xdk-build python --spec api/openapi.yaml --output sdk/python
```

## Examples

### Generate a Python SDK from a YAML specification

```bash
xdk-build python --spec api/openapi.yaml --output sdk/python
```

### Generate a Python SDK from a JSON specification

```bash
xdk-build python --spec api/openapi.json --output sdk/python
```

## License

MIT 