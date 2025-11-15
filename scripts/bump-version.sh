#!/bin/bash
# Script to bump the TypeScript SDK version in xdk-config.toml
# Usage: ./scripts/bump-version.sh [patch|minor|major|beta|version]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$ROOT_DIR/xdk-config.toml"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: xdk-config.toml not found at $CONFIG_FILE"
    exit 1
fi

# Get current version
CURRENT_VERSION=$(grep -E '^typescript = ' "$CONFIG_FILE" | sed -E 's/.*= "([^"]+)".*/\1/')

if [ -z "$CURRENT_VERSION" ]; then
    echo "Error: Could not find current TypeScript version in $CONFIG_FILE"
    exit 1
fi

echo "Current version: $CURRENT_VERSION"

# Parse version parts
if [[ $CURRENT_VERSION =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)(-([a-zA-Z0-9]+))?$ ]]; then
    MAJOR="${BASH_REMATCH[1]}"
    MINOR="${BASH_REMATCH[2]}"
    PATCH="${BASH_REMATCH[3]}"
    PRERELEASE="${BASH_REMATCH[5]}"
else
    echo "Error: Invalid version format: $CURRENT_VERSION"
    exit 1
fi

# Determine new version
case "$1" in
    patch)
        if [ -n "$PRERELEASE" ]; then
            # If it's a prerelease, increment patch version and keep the prerelease tag
            # e.g., 0.1.1-beta -> 0.1.2-beta
            NEW_VERSION="$MAJOR.$MINOR.$((PATCH + 1))-$PRERELEASE"
        else
            NEW_VERSION="$MAJOR.$MINOR.$((PATCH + 1))"
        fi
        ;;
    minor)
        if [ -n "$PRERELEASE" ]; then
            NEW_VERSION="$MAJOR.$((MINOR + 1)).0"
        else
            NEW_VERSION="$MAJOR.$((MINOR + 1)).0"
        fi
        ;;
    major)
        NEW_VERSION="$((MAJOR + 1)).0.0"
        ;;
    beta)
        if [ -n "$PRERELEASE" ] && [[ $PRERELEASE =~ ^beta\.([0-9]+)$ ]]; then
            # Format: beta.1, beta.2, etc. (standard SemVer)
            BETA_NUM="${BASH_REMATCH[1]}"
            BETA_NUM=$((BETA_NUM + 1))
            NEW_VERSION="$MAJOR.$MINOR.$PATCH-beta.$BETA_NUM"
        elif [ -n "$PRERELEASE" ] && [[ $PRERELEASE =~ ^beta([0-9]*)$ ]]; then
            # Legacy format: beta, beta1, beta2, etc. (convert to standard)
            BETA_NUM="${BASH_REMATCH[1]}"
            if [ -z "$BETA_NUM" ]; then
                BETA_NUM=1
            else
                BETA_NUM=$((BETA_NUM + 1))
            fi
            NEW_VERSION="$MAJOR.$MINOR.$PATCH-beta.$BETA_NUM"
        else
            NEW_VERSION="$MAJOR.$MINOR.$PATCH-beta.1"
        fi
        ;;
    *)
        if [ -n "$1" ]; then
            # Use provided version
            NEW_VERSION="$1"
        else
            echo "Usage: $0 [patch|minor|major|beta|version]"
            echo "  patch  - Increment patch version (0.1.1 -> 0.1.2 or 0.1.1-beta -> 0.1.2-beta)"
            echo "  minor  - Increment minor version (0.1.1 -> 0.2.0)"
            echo "  major  - Increment major version (0.1.1 -> 1.0.0)"
            echo "  beta   - Add or increment beta tag (0.1.1 -> 0.1.1-beta.1)"
            echo "  version - Use specific version (e.g., 0.2.0)"
            exit 1
        fi
        ;;
esac

echo "New version: $NEW_VERSION"

# Update xdk-config.toml
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/^typescript = \".*\"/typescript = \"$NEW_VERSION\"/" "$CONFIG_FILE"
else
    # Linux
    sed -i "s/^typescript = \".*\"/typescript = \"$NEW_VERSION\"/" "$CONFIG_FILE"
fi

echo "✓ Updated xdk-config.toml with version $NEW_VERSION"
echo ""
echo "Next steps:"
echo "  1. Regenerate the SDK: make typescript"
echo "  2. Review changes: git diff"
echo "  3. Commit and tag: git commit -am \"Bump TypeScript SDK to $NEW_VERSION\" && git tag -a \"typescript-sdk-v$NEW_VERSION\" -m \"TypeScript SDK v$NEW_VERSION\""
echo "  4. Publish: make publish-typescript"

