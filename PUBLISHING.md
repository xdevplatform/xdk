# Publishing the TypeScript SDK

This guide explains how to publish new versions of the TypeScript SDK to npm.

## Quick Start

### Automated Publishing (Recommended)

1. **Bump version and regenerate:**
   ```bash
   make release-typescript-patch  # or minor/major
   ```

2. **Review, commit, and tag:**
   ```bash
   git diff
   git add xdk-config.toml xdk/typescript/
   git commit -m "Bump TypeScript SDK to v0.1.2"
   git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
   ```

3. **Push (triggers automated publish):**
   ```bash
   git push origin main
   git push origin typescript-sdk-v0.1.2
   ```

GitHub Actions will automatically:
- Generate the SDK from the latest OpenAPI spec
- Build it
- Publish to npm
- Create a GitHub release

### Manual Publishing

If you prefer to publish manually:

```bash
# 1. Bump version
make version-patch

# 2. Regenerate SDK
make typescript

# 3. Publish
make publish-typescript
```

## Version Management

### Version Bump Types

- **Patch** (`make version-patch`): Bug fixes, small changes
  - `0.1.1` → `0.1.2`
  - `0.1.1-beta` → `0.1.1-beta2`

- **Minor** (`make version-minor`): New features, backward compatible
  - `0.1.1` → `0.2.0`

- **Major** (`make version-major`): Breaking changes
  - `0.1.1` → `1.0.0`

- **Beta** (`make version-beta`): Pre-release versions
  - `0.1.1` → `0.1.1-beta1`
  - `0.1.1-beta1` → `0.1.1-beta2`

### Setting a Specific Version

```bash
./scripts/bump-version.sh 0.2.0
```

## Setup

### Initial Setup (One-time)

1. **Create npm token:**
   - Visit https://www.npmjs.com/settings/YOUR_USERNAME/tokens
   - Create an "Automation" token
   - Copy the token

2. **Add to GitHub Secrets:**
   - Go to your repo → Settings → Secrets and variables → Actions
   - Add secret: `NPM_TOKEN` = your npm token

3. **Verify npm login (for manual publishing):**
   ```bash
   npm whoami
   # If not logged in:
   npm login
   ```

## Workflow Details

### Automated Workflow

The GitHub Actions workflow (`.github/workflows/publish-typescript-sdk.yml`) runs when you push a tag matching `typescript-sdk-v*`.

**What it does:**
1. Extracts version from tag name
2. Updates `xdk-config.toml` with the version
3. Generates SDK from latest OpenAPI spec
4. Builds the SDK
5. Publishes to npm
6. Creates a GitHub release

**Tag format:** `typescript-sdk-v0.1.2`

### Manual Workflow

1. **Bump version in config:**
   ```bash
   make version-patch
   ```

2. **Regenerate SDK:**
   ```bash
   make typescript
   ```

3. **Test the build:**
   ```bash
   cd xdk/xdk/typescript
   npm run build
   ```

4. **Dry run publish:**
   ```bash
   make publish-typescript-dry-run
   ```

5. **Publish:**
   ```bash
   make publish-typescript
   ```

## Version Storage

The version is stored in:
- **Source of truth:** `xdk/xdk-config.toml` (line: `typescript = "0.1.1-beta"`)
- **Generated:** `xdk/xdk/typescript/package.json` (automatically updated during generation)

The SDK generator reads the version from `xdk-config.toml` and uses it in the generated `package.json`.

## Troubleshooting

### Version already published

If you try to publish a version that already exists:
- The script will warn you
- You can either:
  - Bump to a new version
  - Force publish (not recommended)

### Build fails

If the build fails:
1. Check that all dependencies are installed: `cd xdk/xdk/typescript && npm ci`
2. Verify TypeScript compilation: `npm run type-check`
3. Check for linting errors: `npm run lint`

### GitHub Actions fails

Common issues:
1. **Missing NPM_TOKEN secret:** Add it in repo settings
2. **npm publish fails:** Check token permissions
3. **Build fails:** Check the Actions logs for specific errors

## Best Practices

1. **Always test before publishing:**
   ```bash
   make publish-typescript-dry-run
   ```

2. **Use semantic versioning:**
   - Patch for bug fixes
   - Minor for new features
   - Major for breaking changes

3. **Tag releases:**
   ```bash
   git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
   ```

4. **Update changelog:**
   - Document changes in CHANGELOG.md
   - Link to relevant issues/PRs

5. **Verify after publishing:**
   ```bash
   npm view @xdevplatform/xdk versions
   npm view @xdevplatform/xdk@0.1.2
   ```

## Examples

### Example: Patch Release

```bash
# 1. Bump patch version
make release-typescript-patch

# 2. Review changes
git diff xdk-config.toml

# 3. Commit
git add xdk-config.toml xdk/typescript/
git commit -m "Bump TypeScript SDK to v0.1.2"

# 4. Tag and push
git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
git push origin main
git push origin typescript-sdk-v0.1.2
```

### Example: Beta Release

```bash
# 1. Bump beta version
make version-beta
make typescript

# 2. Test locally
cd xdk/xdk/typescript
npm run build

# 3. Publish beta
make publish-typescript
```

## Related Files

- `xdk/xdk-config.toml` - Version configuration
- `xdk/scripts/bump-version.sh` - Version bumping script
- `xdk/scripts/publish-typescript.sh` - Publishing script
- `.github/workflows/publish-typescript-sdk.yml` - CI/CD workflow
- `xdk/Makefile` - Make targets for common tasks

