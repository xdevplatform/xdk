# SDK Publishing Scripts

This directory contains scripts for managing SDK versions and publishing.

## Version Management

### Bump Version

Bump the TypeScript SDK version in `xdk-config.toml`:

```bash
# Increment patch version (0.1.1 -> 0.1.2)
./scripts/bump-version.sh patch

# Increment minor version (0.1.1 -> 0.2.0)
./scripts/bump-version.sh minor

# Increment major version (0.1.1 -> 1.0.0)
./scripts/bump-version.sh major

# Add or increment beta tag (0.1.1 -> 0.1.1-beta1)
./scripts/bump-version.sh beta

# Set specific version
./scripts/bump-version.sh 0.2.0
```

Or use the Makefile targets:

```bash
make version-patch
make version-minor
make version-major
make version-beta
```

## Publishing

### Manual Publishing

1. **Bump version and regenerate:**
   ```bash
   make release-typescript-patch  # or minor/major
   ```

2. **Review changes:**
   ```bash
   git diff
   ```

3. **Commit and tag:**
   ```bash
   git add xdk-config.toml xdk/typescript/
   git commit -m "Bump TypeScript SDK to v0.1.2"
   git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
   git push origin main
   git push origin typescript-sdk-v0.1.2
   ```

4. **Publish to npm:**
   ```bash
   make publish-typescript
   ```

   Or manually:
   ```bash
   cd xdk/xdk/typescript
   npm publish
   ```

### Automated Publishing (GitHub Actions)

The GitHub Actions workflow automatically publishes when you push a tag:

1. **Bump version and regenerate:**
   ```bash
   make release-typescript-patch
   ```

2. **Commit, tag, and push:**
   ```bash
   git add xdk-config.toml xdk/typescript/
   git commit -m "Bump TypeScript SDK to v0.1.2"
   git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
   git push origin main
   git push origin typescript-sdk-v0.1.2
   ```

3. **GitHub Actions will automatically:**
   - Generate the SDK
   - Build it
   - Publish to npm
   - Create a GitHub release

### Setup for Automated Publishing

1. **Create an npm token:**
   - Go to https://www.npmjs.com/settings/YOUR_USERNAME/tokens
   - Create a token with "Automation" type
   - Copy the token

2. **Add the token to GitHub Secrets:**
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Add a new secret named `NPM_TOKEN` with your npm token value

3. **Verify the workflow:**
   - The workflow file is at `.github/workflows/publish-typescript-sdk.yml`
   - It triggers on tags matching `typescript-sdk-v*`

## Workflow Summary

### Quick Release (Recommended)

```bash
# 1. Bump version and regenerate
make release-typescript-patch

# 2. Review and commit
git diff
git add xdk-config.toml xdk/typescript/
git commit -m "Bump TypeScript SDK to v0.1.2"

# 3. Tag and push (triggers automated publish)
git tag -a "typescript-sdk-v0.1.2" -m "TypeScript SDK v0.1.2"
git push origin main
git push origin typescript-sdk-v0.1.2
```

### Manual Publish (Alternative)

```bash
# 1. Bump version
make version-patch

# 2. Regenerate SDK
make typescript

# 3. Publish manually
make publish-typescript
```

## Version Format

Versions follow semantic versioning:
- `1.2.3` - Stable release
- `1.2.3-beta` - Beta release
- `1.2.3-beta2` - Beta release (incremented)

The version is stored in `xdk-config.toml` and automatically used when generating the SDK.

