# XDK SDK Generator

.PHONY: all check build test clean help
.PHONY: generate python typescript java csharp
.PHONY: test-python test-typescript test-java test-csharp test-sdks
.PHONY: fmt clippy test-generator
.PHONY: versions

# =====================================
# Default
# =====================================

all: check test-generator

# =====================================
# SDK Generation (local dev)
# =====================================

generate: python typescript java csharp

python:
	cargo run -- python --latest true

typescript:
	cargo run -- typescript --latest true

java:
	cargo run -- java --latest true

csharp:
	cargo run -- csharp --latest true

# =====================================
# SDK Testing (local dev)
# =====================================

test-sdks: test-python test-typescript test-java test-csharp

test-python: python
	cd xdk/python && uv sync && uv run pytest tests/ -v

test-typescript: typescript
	cd xdk/typescript && npm ci && npm run build && npm run type-check && npm test

test-java: java
	cd xdk/java && mvn test -B

test-csharp: csharp
	cd xdk/csharp && dotnet test --nologo

# =====================================
# Generator
# =====================================

fmt:
	cargo fmt --all -- --check

clippy:
	cargo clippy --all --all-targets --all-features -- -D warnings

check: fmt clippy

build:
	cargo build

test-generator:
	cargo test --verbose

test: test-generator test-sdks

# =====================================
# Version Management
# =====================================

versions:
	@grep -E "^(python|typescript|java|csharp) = " xdk-config.toml

# =====================================
# Cleanup
# =====================================

clean:
	rm -rf xdk/python xdk/typescript xdk/java xdk/csharp

cargo-clean:
	cargo clean

# =====================================
# Help
# =====================================

help:
	@echo "XDK SDK Generator"
	@echo ""
	@echo "Local Development:"
	@echo "  make python          Generate Python SDK"
	@echo "  make typescript      Generate TypeScript SDK"
	@echo "  make java            Generate Java SDK"
	@echo "  make csharp          Generate C# SDK"
	@echo "  make test-python     Generate + test Python SDK"
	@echo "  make test-typescript Generate + test TypeScript SDK"
	@echo "  make test-java       Generate + test Java SDK"
	@echo "  make test-csharp     Generate + test C# SDK"
	@echo ""
	@echo "Generator:"
	@echo "  make check           Run fmt + clippy"
	@echo "  make test-generator  Run Rust tests"
	@echo "  make build           Build generator"
	@echo ""
	@echo "Release:"
	@echo "  ./scripts/version.sh <python|typescript|java|csharp|all> <patch|minor|major>"
	@echo "  git add xdk-config.toml && git commit && git push"
	@echo "  Then: Actions -> Release SDK -> Run workflow"
