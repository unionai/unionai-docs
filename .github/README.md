# CI/CD Setup for Union.ai Documentation

This directory contains GitHub Actions workflows for building and deploying the Union.ai documentation site to Cloudflare Workers.

## Architecture

The site is migrated from Cloudflare Pages to a GitHub Actions + Cloudflare Workers setup:

- **Building**: Done entirely in GitHub Actions
- **Deployment**: Static assets uploaded to Cloudflare Workers
- **Routing**: Handled by a Cloudflare Worker script

## Workflows

### 1. Production Build and Deploy (`build-and-deploy.yml`)

**Trigger**: Push to `main` or `v1` branches

**Process**:
1. Builds both versions (v1 and v2) regardless of which branch was updated
2. Combines them into a single site structure:
   ```
   final_dist/
   ├── index.html (redirects to /docs/byoc/)
   └── docs/
       ├── v2/ (from main branch)
       │   ├── flyte/
       │   ├── serverless/
       │   ├── byoc/
       │   └── selfmanaged/
       └── v1/ (from v1 branch)
           ├── flyte/
           ├── serverless/
           ├── byoc/
           └── selfmanaged/
   ```
3. Deploys to production Cloudflare Workers

### 2. PR Preview (`pr-preview.yml`)

**Trigger**: PR opened/updated against `main` or `v1`

**Process**:
1. Builds the PR branch version
2. Builds the stable version of the other branch
3. Combines them for preview
4. Deploys to a PR-specific preview environment
5. Comments on the PR with preview links

**PR Comment Features**:
- Direct links to all variants in the changed version
- Automatic updates when PR is updated
- Includes both the modified version and stable other version

### 3. PR Cleanup (`cleanup-pr.yml`)

**Trigger**: PR closed

**Process**:
1. Removes the preview deployment
2. Adds a cleanup comment to the PR

## Build Script

The `scripts/build-combined.sh` script handles the complex build logic:

- **Production builds**: Build both v1 and v2, combine them
- **Preview builds**: Build PR branch + stable other version, combine them
- Handles branch switching and cleanup automatically
- Provides detailed logging

## Required Secrets

Set these in your GitHub repository settings:

- `CLOUDFLARE_API_TOKEN`: Token with Workers and Pages permissions
- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare account ID

## Cloudflare Worker

The `worker.js` file contains the routing logic:

- Redirects root (`/`) to `/docs/byoc/`
- Adds version prefixes when missing (defaults to v2)
- Handles legacy domain redirects
- Serves static files

## Version Management

- **v2** (latest): `main` branch → `/docs/v2/`
- **v1** (archived): `v1` branch → `/docs/v1/`

## Directory Structure

```
.github/workflows/
├── build-and-deploy.yml    # Production builds
├── pr-preview.yml          # PR preview builds
└── cleanup-pr.yml          # PR cleanup

scripts/
└── build-combined.sh       # Build script for combining versions

worker.js                   # Cloudflare Worker routing logic
wrangler.toml              # Cloudflare deployment config
```

## Features

- ✅ Production builds when either branch updates
- ✅ PR previews for all contributors (including forks)
- ✅ Automatic PR comments with preview links
- ✅ Combined multi-version site structure
- ✅ Support for all variants (flyte, serverless, byoc, selfmanaged)
- ✅ Proper cleanup of preview environments
- ✅ Detailed build logging and error handling

## Migration Notes

This setup replaces the previous Cloudflare Pages deployment with:

1. **Better control**: Full control over build process in GitHub Actions
2. **Combined builds**: Both versions built and deployed together
3. **Enhanced PR previews**: Automatic comments with preview links
4. **Fork support**: Works with PRs from repository forks
5. **Cleaner architecture**: Clear separation of building vs. serving