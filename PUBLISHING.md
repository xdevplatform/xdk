# Publishing SDKs

## Release an SDK

1. Go to **[Actions → Release SDK](https://github.com/xdevplatform/xdk/actions/workflows/release.yml)**
2. Click **Run workflow**
3. Select SDK (`python`, `typescript`, `java`, `csharp`, or `all`)
4. Select bump type (`patch`, `minor`, `major`, `beta`)
5. Click **Run workflow**

The workflow handles versioning, generation, testing, and publishing automatically.

## Version Bumps

| Type | Example | Use For |
|------|---------|---------|
| `patch` | 0.2.3 → 0.2.4 | Bug fixes |
| `minor` | 0.2.3 → 0.3.0 | New features |
| `major` | 0.2.3 → 1.0.0 | Breaking changes |
| `beta` | 0.2.3 → 0.2.3-beta.1 | Pre-releases |

## Options

| Option | What it does |
|--------|--------------|
| **Dry run** | Generate and test only, no push or publish |
| **Skip publish** | Push code to SDK repo but don't publish to PyPI/npm |

## Check Current Versions

```bash
make versions
```

## SDK Repos

| SDK | Repo | Package |
|-----|------|---------|
| Python | [xdk-python](https://github.com/xdevplatform/xdk-python) | [PyPI](https://pypi.org/project/xdk/) |
| TypeScript | [xdk-typescript](https://github.com/xdevplatform/xdk-typescript) | [npm](https://www.npmjs.com/package/@xdevplatform/xdk) |
| Java | [xdk-java](https://github.com/xdevplatform/xdk-java) | Maven Central (`com.x:xdk`) |
| C# | [xdk-csharp](https://github.com/xdevplatform/xdk-csharp) | NuGet (`XDevPlatform.Xdk`) |

## Required Secrets

### Generator Repo (`xdevplatform/xdk`)
- `XDK_PAT` — Personal access token or GitHub App token to push version bumps to `main`
- `SDK_DEPLOY_KEY_PYTHON` — SSH write deploy key for `xdevplatform/xdk-python`
- `SDK_DEPLOY_KEY_TYPESCRIPT` — SSH write deploy key for `xdevplatform/xdk-typescript`
- `SDK_DEPLOY_KEY_JAVA` — SSH write deploy key for `xdevplatform/xdk-java`
- `SDK_DEPLOY_KEY_CSHARP` — SSH write deploy key for `xdevplatform/xdk-csharp`

### Java SDK Repo (`xdevplatform/xdk-java`)
- `SONATYPE_USERNAME` / `SONATYPE_TOKEN` — Sonatype Central Portal user token credentials for `com.x` (same credentials as `chat-xdk`)
- `MAVEN_GPG_PRIVATE_KEY` / `MAVEN_GPG_PASSPHRASE` — Armored GPG signing key and passphrase

### C# SDK Repo (`xdevplatform/xdk-csharp`)
- `NUGET_USER` — NuGet.org profile name registered with the OIDC Trusted Publisher policy (`xdevplatform/xdk-csharp`, workflow `publish.yml`), or `NUGET_API_KEY` fallback
