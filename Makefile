# XDK SDK Generator

.PHONY: all check build test clean help
.PHONY: generate python typescript elixir
.PHONY: test-python test-typescript test-elixir test-sdks
.PHONY: fmt clippy test-generator
.PHONY: versions

# =====================================
# Default
# =====================================

all: check test-generator

# =====================================
# SDK Generation (local dev)
# =====================================

generate: python typescript elixir

python:
	cargo run -- python --latest true

typescript:
	cargo run -- typescript --latest true

elixir:
	cargo run -- elixir --latest true

# =====================================
# SDK Testing (local dev)
# =====================================

test-sdks: test-python test-typescript test-elixir

test-python: python
	cd xdk/python && uv sync && uv run pytest tests/ -v

test-typescript: typescript
	cd xdk/typescript && npm ci && npm run build && npm run type-check && npm test

test-elixir: elixir
	cd xdk/elixir && mix deps.get && mix test

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
	@grep -E "^(python|typescript|elixir) = " xdk-config.toml

# =====================================
# Cleanup
# =====================================

clean:
	rm -rf xdk/python xdk/typescript xdk/elixir

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
	@echo "  make test-python     Generate + test Python SDK"
	@echo "  make test-typescript Generate + test TypeScript SDK"
	@echo "  make elixir          Generate Elixir SDK"
	@echo "  make test-elixir     Generate + test Elixir SDK"
	@echo ""
	@echo "Generator:"
	@echo "  make check           Run fmt + clippy"
	@echo "  make test-generator  Run Rust tests"
	@echo "  make build           Build generator"
	@echo ""
	@echo "Release:"
	@echo "  ./scripts/version.sh <python|typescript|all> <patch|minor|major>"
	@echo "  git add xdk-config.toml && git commit && git push"
	@echo "  Then: Actions -> Release SDK -> Run workflow"
