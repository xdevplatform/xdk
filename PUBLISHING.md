# Publishing SDKs

## Release an SDK

1. Go to **[Actions → Release SDK](https://github.com/xdevplatform/xdk/actions/workflows/release.yml)**
2. Click **Run workflow**
3. Select SDK (`python`, `typescript`, or `all`)
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
