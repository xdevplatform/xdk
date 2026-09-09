# XDK - X API SDK Generator

A Rust-based SDK generator that creates language-specific SDKs for the X API from OpenAPI specifications.

## SDKs

| Language | Package | Repo |
|----------|---------|------|
| Python | `pip install xdk` | [xdk-python](https://github.com/xdevplatform/xdk-python) |
| TypeScript | `npm install @xdevplatform/xdk` | [xdk-typescript](https://github.com/xdevplatform/xdk-typescript) |

## Architecture

```
xdk/
├── xdk-openapi/    # OpenAPI 3.0 parser
├── xdk-lib/        # Shared models and utilities
├── xdk-gen/        # Language generators (uses language! macro)
├── xdk-build/      # CLI tool
└── xdk-gen/templates/
    ├── python/     # Jinja2 templates for Python
    └── typescript/ # Jinja2 templates for TypeScript
```

## Development

### Prerequisites

- Rust toolchain ([rustup](https://rustup.rs/))
- Python 3.8+ with [uv](https://github.com/astral-sh/uv)
- Node.js 18+

### Generate SDKs Locally

```bash
make python       # Generate Python SDK to xdk/python/
make typescript   # Generate TypeScript SDK to xdk/typescript/
```

### Run Tests

```bash
make check           # Rust fmt + clippy
make test-generator  # Rust unit tests
make test-python     # Generate + test Python SDK
make test-typescript # Generate + test TypeScript SDK
```

## Publishing

See [PUBLISHING.md](PUBLISHING.md). TL;DR: Go to Actions → Release SDK → Run workflow.

## Adding a New Language

### 1. Create the generator

Add a new file in `xdk-gen/src/<language>/`:

```rust
// xdk-gen/src/go/generator.rs
use xdk_lib::language;

language! {
    name: Go,
    filters: [go_type, pascal_case, snake_case],
    class_casing: Casing::Pascal,
    operation_casing: Casing::Pascal,
    variable_casing: Casing::Snake,
    render: [
        multiple {
            render "models" => "{}/models.go",
            render "client" => "{}/client.go",
        },
        render "main_client" => "client.go"
    ],
    tests: [
        multiple {
            render "tests" => "{}_test.go",
        }
    ]
}
```

### 2. Create templates

Add Jinja2 templates in `xdk-gen/templates/<language>/`:

```
xdk-gen/templates/go/
├── models.j2
├── client.j2
├── main_client.j2
└── tests.j2
```

### 3. Register the generator

Update `xdk-gen/src/lib.rs` to export your generator.

Update `xdk-build/src/main.rs` to add the CLI command.

### 4. Add version config

Update `xdk-config.toml`:

```toml
[versions]
go = "0.1.0"
```

### 5. Create SDK repo

Create `xdevplatform/xdk-go` with CI workflows (see existing SDK repos for examples).

### 6. Update release workflow

Add the new language to `.github/workflows/release.yml`.

## License

MIT
