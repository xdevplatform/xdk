#!/bin/bash
# Script to publish the TypeScript SDK to npm
# Usage: ./scripts/publish-typescript.sh [--dry-run]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SDK_DIR="$ROOT_DIR/xdk/typescript"

if [ ! -d "$SDK_DIR" ]; then
    echo "Error: TypeScript SDK directory not found at $SDK_DIR"
    echo "Please run 'make typescript' first to generate the SDK"
    exit 1
fi

cd "$SDK_DIR"

# Check if dist directory exists and has files
if [ ! -d "dist" ] || [ -z "$(ls -A dist 2>/dev/null)" ]; then
    echo "Error: dist directory is empty or doesn't exist"
    echo "Please run 'npm run build' first"
    exit 1
fi

# Get version from package.json
VERSION=$(node -p "require('./package.json').version")
echo "Publishing @xdevplatform/xdk@$VERSION"

# Check if already published
if npm view "@xdevplatform/xdk@$VERSION" version > /dev/null 2>&1; then
    echo "Warning: Version $VERSION is already published to npm"
    read -p "Do you want to continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted"
        exit 1
    fi
fi

# Check for uncommitted changes (optional, can be disabled)
if [ "$1" != "--skip-git-check" ]; then
    if [ -n "$(git status --porcelain)" ]; then
        echo "Warning: You have uncommitted changes"
        read -p "Do you want to continue anyway? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Aborted"
            exit 1
        fi
    fi
fi

# Publish to npm
if [ "$1" == "--dry-run" ]; then
    echo "Dry run mode - would publish:"
    npm publish --dry-run
else
    echo "Publishing to npm..."
    npm publish
    echo ""
    echo "✓ Successfully published @xdevplatform/xdk@$VERSION"
    echo ""
    echo "You can install it with:"
    echo "  npm install @xdevplatform/xdk@$VERSION"
fi

