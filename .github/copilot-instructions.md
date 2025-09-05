# Union.ai Documentation Site

Union.ai documentation is a Hugo-based static site that generates documentation for Flyte OSS and Union.ai products (BYOC, Serverless, Self-managed). The site supports multiple "variants" that customize content for different product offerings.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

- **Bootstrap, build, and test the repository:**
  - `sudo apt update && sudo apt install -y curl tar`
  - `wget https://github.com/gohugoio/hugo/releases/download/v0.145.0/hugo_extended_0.145.0_linux-amd64.tar.gz`
  - `tar -xzf hugo_extended_0.145.0_linux-amd64.tar.gz && sudo mv hugo /usr/local/bin/hugo`
  - `cp hugo.local.toml~sample hugo.local.toml`
  - **CRITICAL**: Fix submodule URL for HTTPS access: `git config submodule.external/unionai-examples.url https://github.com/unionai/unionai-examples.git`
  - `make init-examples` -- initializes git submodules (required for tutorials). NEVER CANCEL: May take 5-10 minutes depending on network. Set timeout to 15+ minutes.
  - `hugo version` -- verify Hugo v0.145.0+ is installed

- **Development workflow:**
  - `make dev` -- starts development server at http://localhost:1313/dev/site/p/. NEVER CANCEL: Build takes 30-60 seconds. Set timeout to 2+ minutes.
  - Development server supports hot-reload for content changes
  - Access site at http://localhost:1313/dev/site/p/ to test functionality

- **Production builds:**
  - `make dist` -- builds all variants (flyte, byoc, selfmanaged). Takes under 2 seconds. NEVER CANCEL: Set timeout to 2+ minutes for safety.
  - Creates `dist/` folder with all product variants
  - `sudo apt install caddy -y` -- install web server for serving production builds
  - `make serve PORT=9000` -- serves production build locally at http://localhost:9000

## Validation

- **Always manually validate any new code by testing the development server.**
- **ALWAYS run through at least one complete end-to-end scenario after making changes:**
  1. Start development server with `make dev`
  2. Navigate to http://localhost:1313/dev/site/p/
  3. Test navigation between main sections (User guide, Tutorials, API reference, Integrations, Community)
  4. Verify content loads correctly and images display properly
  5. Test variant switching using the Product selector dropdown
- **Build validation commands:**
  - `make check-images` -- validates all image references in markdown files. Takes 5-10 seconds.
  - `make check-jupyter` -- validates Jupyter notebook consistency. Takes 5-10 seconds.
  - `make dist` -- full production build validation. Takes under 2 seconds but validates all variants.

## Common tasks

The following are outputs from frequently run commands. Reference them instead of viewing, searching, or running bash commands to save time.

### Repository root structure
```
.
├── .github/               # GitHub workflows and settings
├── .gitmodules           # Git submodule configuration
├── DEVELOPER.md          # Developer documentation
├── Makefile             # Build automation
├── README.md            # Project overview
├── content/             # Hugo content (markdown files)
├── external/            # Git submodules (unionai-examples)
├── hugo.*.toml          # Hugo configuration files
├── layouts/             # Hugo template layouts
├── scripts/             # Build and validation scripts
├── static/              # Static assets
├── themes/              # Hugo theme (union)
└── tools/               # Development tools
```

### Key Hugo configuration files
- `hugo.toml` -- core Hugo configuration (never changes)
- `hugo.site.toml` -- site-specific settings
- `hugo.dev.toml` -- development environment overrides
- `hugo.local.toml` -- local developer preferences (copied from hugo.local.toml~sample)
- `config.{variant}.toml` -- variant-specific settings (flyte, byoc, selfmanaged, serverless)

### Important build commands
- `make usage` -- shows all available make targets
- `make dev` -- development server with hot-reload
- `make dist` -- production build (all variants)
- `make serve [PORT=9000]` -- serve production build locally
- `make init-examples` -- initialize git submodules
- `make update-examples` -- update submodules to latest

### Content structure and variants
- Content in `content/` directory uses Hugo's markdown format
- Variant-specific content uses `{{< variant ... >}}` shortcodes
- Each markdown file must declare supported variants in frontmatter: `variants: +flyte +byoc +selfmanaged`
- External examples are referenced from `external/unionai-examples/` submodule
- Code snippets use `{{< code file="path" fragment="section-name" lang="python" >}}` shortcode

### Development environment controls
Edit `hugo.local.toml` to control development experience:
- `variant = "flyte"` -- current variant to display
- `show_inactive = true` -- show content from other variants
- `highlight_active = true` -- highlight current variant content
- `highlight_keys = true` -- highlight replacement keys and values

## Critical Requirements

- **Hugo version**: MUST be v0.145.0 or greater (extended version)
- **Git submodules**: Required for tutorial content. Use HTTPS URL: `https://github.com/unionai/unionai-examples.git`
- **Build timing**: Complete production build takes under 2 seconds
- **Development server**: Builds in 30-60 seconds, serves at localhost:1313
- **Validation**: Always test navigation and content rendering manually
- **NEVER CANCEL**: All build commands complete quickly, but set generous timeouts to avoid interruption

## Known Issues and Workarounds

- **Submodule SSH access**: Default .gitmodules uses SSH. Change to HTTPS with: `git config submodule.external/unionai-examples.url https://github.com/unionai/unionai-examples.git`
- **Ubuntu Hugo version**: Default apt package (v0.123.7) is too old. Manual installation required from GitHub releases.
- **External CDN resources**: Some external JavaScript/CSS may be blocked in restricted environments, causing console errors but not affecting core functionality
- **Missing fragment markers**: Build warnings about missing fragment markers are expected when submodule content is incomplete

## File Locations Reference

- **Main content**: `content/user-guide/`, `content/tutorials/`, `content/api-reference/`
- **Examples**: `external/unionai-examples/` (git submodule)
- **Build scripts**: `scripts/` directory
- **Validation tools**: `tools/` directory
- **Theme**: `themes/union/`
- **Generated output**: `dist/` (production), `public/` (development)