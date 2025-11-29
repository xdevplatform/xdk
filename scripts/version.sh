#!/bin/bash
# Unified version management script for all SDKs
# Usage: ./scripts/version.sh <sdk> <bump-type>
#
# Examples:
#   ./scripts/version.sh python patch
#   ./scripts/version.sh typescript minor
#   ./scripts/version.sh all major
#   ./scripts/version.sh python 1.0.0  # Set specific version

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG_FILE="$ROOT_DIR/xdk-config.toml"

VALID_SDKS=("python" "typescript")
VALID_BUMPS=("patch" "minor" "major" "beta")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_usage() {
    echo "Usage: $0 <sdk> <bump-type|version>"
    echo ""
    echo "SDKs:"
    echo "  python       Python SDK"
    echo "  typescript   TypeScript SDK"
    echo "  all          All SDKs"
    echo ""
    echo "Bump types:"
    echo "  patch        Increment patch version (0.1.1 -> 0.1.2)"
    echo "  minor        Increment minor version (0.1.1 -> 0.2.0)"
    echo "  major        Increment major version (0.1.1 -> 1.0.0)"
    echo "  beta         Add/increment beta tag (0.1.1 -> 0.1.1-beta.1)"
    echo ""
    echo "Or specify a version directly:"
    echo "  $0 python 1.0.0"
    echo "  $0 all 2.0.0-beta.1"
}

get_current_version() {
    local sdk=$1
    grep -E "^${sdk} = " "$CONFIG_FILE" | sed -E 's/.*= "([^"]+)".*/\1/'
}

parse_version() {
    local version=$1
    
    if [[ $version =~ ^([0-9]+)\.([0-9]+)\.([0-9]+)(-([a-zA-Z0-9.]+))?$ ]]; then
        MAJOR="${BASH_REMATCH[1]}"
        MINOR="${BASH_REMATCH[2]}"
        PATCH="${BASH_REMATCH[3]}"
        PRERELEASE="${BASH_REMATCH[5]}"
        return 0
    else
        return 1
    fi
}

bump_version() {
    local sdk=$1
    local bump=$2
    
    local current_version=$(get_current_version "$sdk")
    
    if [ -z "$current_version" ]; then
        echo -e "${RED}Error: Could not find version for '$sdk' in $CONFIG_FILE${NC}"
        exit 1
    fi
    
    echo -e "${BLUE}[$sdk]${NC} Current version: $current_version"
    
    # Check if bump is a specific version
    if [[ $bump =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
        local new_version="$bump"
    else
        # Parse current version
        if ! parse_version "$current_version"; then
            echo -e "${RED}Error: Invalid version format: $current_version${NC}"
            exit 1
        fi
        
        case "$bump" in
            patch)
                if [ -n "$PRERELEASE" ]; then
                    # Keep prerelease tag, bump patch
                    new_version="$MAJOR.$MINOR.$((PATCH + 1))-$PRERELEASE"
                else
                    new_version="$MAJOR.$MINOR.$((PATCH + 1))"
                fi
                ;;
            minor)
                new_version="$MAJOR.$((MINOR + 1)).0"
                ;;
            major)
                new_version="$((MAJOR + 1)).0.0"
                ;;
            beta)
                if [ -n "$PRERELEASE" ] && [[ $PRERELEASE =~ ^beta\.([0-9]+)$ ]]; then
                    local beta_num="${BASH_REMATCH[1]}"
                    new_version="$MAJOR.$MINOR.$PATCH-beta.$((beta_num + 1))"
                elif [ -n "$PRERELEASE" ] && [[ $PRERELEASE =~ ^beta([0-9]*)$ ]]; then
                    # Legacy format conversion
                    local beta_num="${BASH_REMATCH[1]}"
                    if [ -z "$beta_num" ]; then
                        beta_num=1
                    else
                        beta_num=$((beta_num + 1))
                    fi
                    new_version="$MAJOR.$MINOR.$PATCH-beta.$beta_num"
                else
                    new_version="$MAJOR.$MINOR.$PATCH-beta.1"
                fi
                ;;
            *)
                echo -e "${RED}Error: Invalid bump type '$bump'${NC}"
                print_usage
                exit 1
                ;;
        esac
    fi
    
    # Update config file
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' "s/^${sdk} = \".*\"/${sdk} = \"$new_version\"/" "$CONFIG_FILE"
    else
        sed -i "s/^${sdk} = \".*\"/${sdk} = \"$new_version\"/" "$CONFIG_FILE"
    fi
    
    echo -e "${GREEN}[$sdk]${NC} New version: $new_version"
}

# Validate inputs
if [ $# -lt 2 ]; then
    print_usage
    exit 1
fi

SDK=$1
BUMP=$2

if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}Error: xdk-config.toml not found at $CONFIG_FILE${NC}"
    exit 1
fi

# Determine which SDKs to bump
if [ "$SDK" = "all" ]; then
    SDKS_TO_BUMP=("${VALID_SDKS[@]}")
else
    # Validate SDK name
    valid=false
    for s in "${VALID_SDKS[@]}"; do
        if [ "$s" = "$SDK" ]; then
            valid=true
            break
        fi
    done
    
    if [ "$valid" = false ]; then
        echo -e "${RED}Error: Invalid SDK '$SDK'${NC}"
        echo "Valid SDKs: ${VALID_SDKS[*]}"
        exit 1
    fi
    
    SDKS_TO_BUMP=("$SDK")
fi

# Perform the version bump(s)
echo -e "${YELLOW}Bumping versions...${NC}"
echo ""

for sdk in "${SDKS_TO_BUMP[@]}"; do
    bump_version "$sdk" "$BUMP"
done

echo ""
echo -e "${GREEN}✓ Updated xdk-config.toml${NC}"
echo ""
echo "Next steps:"
echo "  1. Review changes: git diff xdk-config.toml"
echo "  2. Commit: git add xdk-config.toml && git commit -m \"chore: bump SDK versions\""
echo "  3. Push to trigger release workflow (or run manually in GitHub Actions)"

