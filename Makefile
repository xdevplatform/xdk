# Makefile for Rust project

# Default target: runs checks and tests
all: check test

python:
	cargo run -- python --latest true

typescript:
	cargo run -- typescript --latest true

test-python:
	cd xdk/python && uv run pytest tests/

# Check formatting
fmt:
	cargo fmt --all -- --check

# Run clippy linter
clippy:
	cargo clippy --all --all-targets --all-features -- -D warnings

# Run all checks (fmt and clippy)
check: fmt clippy

# Build the project
build:
	cargo build

# Run tests
test:
	cargo test --verbose

# Clean build artifacts
clean:
	rm -rf xdk/*

cargo-clean:
	cargo clean

# Version management
version-patch:
	@./scripts/bump-version.sh patch

version-minor:
	@./scripts/bump-version.sh minor

version-major:
	@./scripts/bump-version.sh major

version-beta:
	@./scripts/bump-version.sh beta

# TypeScript SDK publishing
publish-typescript: typescript
	@./scripts/publish-typescript.sh

publish-typescript-dry-run: typescript
	@./scripts/publish-typescript.sh --dry-run

# Full workflow: bump version, regenerate, and prepare for publishing
release-typescript-patch: version-patch typescript
	@echo "✓ Version bumped and SDK regenerated"
	@echo "Next: Review changes, commit, tag, and publish"

release-typescript-minor: version-minor typescript
	@echo "✓ Version bumped and SDK regenerated"
	@echo "Next: Review changes, commit, tag, and publish"

release-typescript-major: version-major typescript
	@echo "✓ Version bumped and SDK regenerated"
	@echo "Next: Review changes, commit, tag, and publish"

.PHONY: all python test-python fmt clippy check build test clean cargo-clean
.PHONY: version-patch version-minor version-major version-beta
.PHONY: publish-typescript publish-typescript-dry-run
.PHONY: release-typescript-patch release-typescript-minor release-typescript-major
