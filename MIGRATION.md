# Migration Setup Instructions

## Overview

This document provides setup instructions for migrating the Union.ai documentation from Cloudflare Pages to GitHub Actions + Cloudflare Pages deployment.

## Prerequisites

### Required Secrets

You need to configure the following secrets in your GitHub repository:

1. **CLOUDFLARE_API_TOKEN**
   - Go to [Cloudflare Dashboard → My Profile → API Tokens](https://dash.cloudflare.com/profile/api-tokens)
   - Click "Create Token"
   - Use the "Custom token" template
   - Required permissions:
     - `Zone:Zone Settings:Edit`
     - `Zone:Zone:Read`
     - `Account:Cloudflare Pages:Edit`
   - Include Resources:
     - `Include: All accounts`
     - `Include: All zones`

2. **CLOUDFLARE_ACCOUNT_ID**
   - Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
   - Select your account
   - Copy the Account ID from the right sidebar

### Cloudflare Pages Project Setup

1. Go to [Cloudflare Dashboard → Pages](https://dash.cloudflare.com/pages)
2. Create a new project called `unionai-docs`
3. **Important**: Don't connect it to GitHub - we'll deploy directly from GitHub Actions
4. Note the project name for the workflows

## Workflow Configuration

The three workflows are:

### 1. Production Deployment (`build-and-deploy.yml`)

**Triggers:**
- Push to `main` branch (builds v2 + v1)
- Push to `v1` branch (builds v1 + v2)

**Process:**
1. Builds both versions regardless of which branch was updated
2. Combines them into a unified site structure
3. Deploys to production Cloudflare Pages

### 2. PR Preview (`pr-preview.yml`)

**Triggers:**
- PR opened/updated against `main` or `v1`

**Process:**
1. Builds the PR branch
2. Builds the stable version of the other branch
3. Combines them for preview
4. Deploys to a PR-specific preview URL
5. Comments on PR with preview links

### 3. PR Cleanup (`cleanup-pr.yml`)

**Triggers:**
- PR closed

**Process:**
1. Removes preview deployment
2. Adds cleanup comment

## Site Structure

The combined site structure will be:

```
production-site/
├── index.html (redirects to /docs/byoc/)
├── _redirects (Cloudflare Pages routing rules)
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

## URL Structure

- **Root**: `https://your-domain.com/` → redirects to `/docs/byoc/`
- **Latest version**: `https://your-domain.com/docs/v2/byoc/`
- **Previous version**: `https://your-domain.com/docs/v1/byoc/`
- **Version-less URLs**: `https://your-domain.com/docs/byoc/` → redirects to v2

## Testing the Migration

### Local Testing

1. Install Hugo 0.145.0+
2. Run the build script:
   ```bash
   # From main or v1 branch
   ./scripts/build-combined.sh --type production --output test_dist
   
   # Check the output
   find test_dist -type f | head -20
   ```

### Preview Testing

1. Create a test PR against `main` or `v1`
2. Check that the workflow runs
3. Verify the PR comment appears with preview links
4. Test the preview URLs

### Production Testing

1. Push a small change to `main` or `v1`
2. Verify the production workflow runs
3. Check that both versions are built and deployed
4. Test the live site URLs

## Migration Steps

1. **Setup Phase:**
   - [ ] Configure secrets in GitHub
   - [ ] Create Cloudflare Pages project
   - [ ] Test workflows in a fork first

2. **Testing Phase:**
   - [ ] Test PR previews work
   - [ ] Test production deployments work
   - [ ] Verify all variants build correctly
   - [ ] Test redirects work as expected

3. **Go-Live Phase:**
   - [ ] Update DNS to point to new Cloudflare Pages URL
   - [ ] Monitor for any issues
   - [ ] Update any hardcoded URLs in the codebase

## Troubleshooting

### Common Issues

1. **Submodule failures:**
   - The workflows handle this gracefully by creating placeholder directories
   - Missing submodules will cause warnings but not failures

2. **Hugo build warnings:**
   - The CI builds use a lenient mode that doesn't fail on warnings
   - Missing code fragments from examples will show as warnings

3. **Branch switching failures:**
   - Make sure both `main` and `v1` branches exist in the repository
   - The build script will fail gracefully if branches don't exist

### Debugging

1. Check GitHub Actions logs for detailed build output
2. Look for artifacts uploaded by the workflows
3. Test the build script locally to isolate issues

## Rollback Plan

If issues occur:

1. **Immediate:** Revert DNS changes to point back to old Cloudflare Pages
2. **Short-term:** Disable the workflows while investigating
3. **Long-term:** Fix issues and redeploy

The old Cloudflare Pages setup can remain as a backup during the transition period.