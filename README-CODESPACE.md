# OpenClaw - GitHub Codespace Deployment

## Quick Start

### 1. Open in GitHub Codespace
Click "Code" → "Create codespace on main"

### 2. Development Environment
Your codespace will automatically:
- Install Node.js 20
- Install pnpm
- Install all dependencies
- Be ready to develop!

### 3. Run OpenClaw
```bash
# Development
pnpm start

# Build
pnpm build

# Development with hot reload
pnpm dev
```

### 4. Use in Codespace
- Open terminal in Codespace
- Run commands directly
- Full Node.js development environment

## Features

- ✅ Automatic dependency installation
- ✅ Pre-configured VS Code extensions
- ✅ GitHub Actions for CI/CD
- ✅ Docker support
- ✅ NPM publishing ready

## Deploy Options

### GitHub Actions (Auto-deploy)
- CI: Build & test on push
- CD: Auto-publish to NPM on release

### Docker
```bash
# Build image
docker build -t openclaw .

# Run
docker run -it openclaw
```

### NPM Package
```bash
# Publish to NPM (requires token)
pnpm publish
```

## Documentation
See [README.md](README.md) for full usage.

---
Powered by GitHub Codespaces 🚀
