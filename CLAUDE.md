# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the combined documentation repository for Flyte OSS and Union.ai products (BYOC and Self-managed). It uses Hugo as the static site generator with a custom variant system to support multiple product flavors from a single source.

## Build and Development Commands

### Initial Setup
```bash
# Install Hugo (required)
brew install hugo

# Create local configuration file
cp hugo.local.toml~sample hugo.local.toml

# Initialize tutorial examples submodule
make init-examples
```

### Development
```bash
# Start development server with live reload
make dev

# Update examples submodule to latest main
make update-examples
```

### Production Build
```bash
# Build all variants to dist/
make dist

# Build a single variant
make variant VARIANT=flyte    # or byoc, selfmanaged

# Serve production build locally
make serve PORT=9000  # defaults to port 9000
```

### Testing and Validation
```bash
# Check Jupyter notebooks
make check-jupyter

# Check images
make check-images
```

## Architecture

### Multi-Variant System

The repository serves documentation for **four variants** from a single codebase:
- `flyte` - Flyte OSS (open-source)
- `byoc` - Union.ai BYOC (Bring Your Own Cloud)
- `selfmanaged` - Union.ai Self-managed
- `serverless` - Union.ai Serverless (currently commented out)

**Key concepts:**

1. **Page-level variants**: Each Markdown file has `variants:` front matter specifying which product versions include that page:
   ```yaml
   variants: +flyte +byoc +selfmanaged -serverless
   ```

2. **Content-level variants**: Use `{{< variant >}}` shortcode for conditional content within pages:
   ```markdown
   {{< variant flyte >}}
   Flyte-specific content
   {{< /variant >}}
   ```

3. **Dynamic keywords**: The `{{< key >}}` shortcode renders product-specific terms. All keywords are defined in `hugo.site.toml` under `[params.key]` with values for each variant:
   - `{{< key product_name >}}` → "Flyte" or "Union.ai"
   - `{{< key cli >}}` → "pyflyte" or "union"
   - See `hugo.site.toml` lines 68-184 for all available keys

### Configuration Files

Hugo configuration is split across multiple files that are merged:

- `hugo.toml` - Core settings that never change
- `hugo.site.toml` - Site-wide content configuration (variant weights, keywords)
- `hugo.dev.toml` - Development mode settings
- `hugo.ver.toml` - Version-specific settings
- `hugo.local.toml` - Local developer overrides (not committed)
- `config.{variant}.toml` - Per-variant settings (baseURL, variant name)

Build commands combine these: `hugo.toml,hugo.site.toml,hugo.ver.toml,config.flyte.toml`

### Content Structure

```
content/
├── user-guide/        # User documentation
├── tutorials/         # Tutorial content
├── api-reference/     # API documentation
├── integrations/      # Integration guides
├── community/         # Contributing guides
└── __docs_builder__/  # Internal test pages (excluded from all variants)
```

### External Content

Tutorial examples are maintained in a separate repository (`unionai/unionai-examples`) and imported as a git submodule in `external/unionai-examples/`.

### Development Mode Features

When running `make dev`, configure `hugo.local.toml` to control the experience:

- `variant` - Current variant to display (flyte/byoc/selfmanaged)
- `show_inactive` - Show content from other variants (grayed out)
- `highlight_active` - Highlight current variant's content
- `highlight_keys` - Show key replacements visually

### Build Process

The `make dist` command:
1. Runs pre-flight checks (`scripts/pre-build-checks.sh`, `scripts/pre-flight.sh`)
2. Builds each variant separately with its config: `scripts/run_hugo.sh`
3. Outputs to `dist/{variant}/` directories
4. Generates variant-specific 404 pages: `scripts/gen_404.sh`

## Important Notes

- **Versions**: The repository has two documentation versions:
  - `v1` branch for Flyte/Union 1.x
  - `main` branch for Flyte/Union 2.0 (current)

- **All variants must be explicitly declared**: Every page must list all four variants with `+` or `-` prefix. No defaults.

- **Contributing docs**: Detailed authoring guidance is in `content/community/contributing-docs/` including information about variants, shortcodes, and publishing.

- **Redirects**: Maintained in `redirects.csv` at the repository root.
