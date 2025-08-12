# Makefile for Rust project

# Default target: runs checks and tests
all: check test

run-python:
	cargo run -- python --latest true

test-python:
	cd xdk/python && uv run pytest tests/

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
	rm -rf xdk/*

cargo-clean:
	cargo clean

.PHONY: all run-python test-python fmt clippy check build test clean cargo-clean
