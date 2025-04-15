# Makefile for Rust project

# Default target: runs checks and tests
all: check test

# Check formatting
fmt:
	cargo fmt --all -- --check

# Run clippy linter
clippy:
	cargo clippy -- -D warnings

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
	cargo clean

.PHONY: all fmt clippy check build test clean
