# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **multi-variant Hugo documentation site** for Flyte (open-source) and Union.ai products. A single source generates four documentation variants:
- **flyte** - Open-source Flyte orchestration platform
- **byoc** - Union Bring-Your-Own-Cloud
- **serverless** - Union managed cloud service
- **selfmanaged** - Union enterprise self-hosted

## Essential Commands

```bash
# Development (requires hugo.local.toml setup first)
cp hugo.local.toml~sample hugo.local.toml  # First time only
make dev                                    # Start dev server at localhost:1313

# Production build
make dist                                   # Build all variants to dist/
make serve PORT=4444                        # Serve dist/ locally

# Examples submodule
make init-examples                          # Initialize external/unionai-examples
make update-examples                        # Update to latest

# API documentation regeneration
make -f Makefile.api.flyte-sdk              # Flyte SDK API docs
make -f Makefile.api.plugins                # Plugin API docs
make -f Makefile.cli.flyte                  # CLI docs

# Validation
make check-images                           # Validate image references
make check-jupyter                          # Validate Jupyter notebooks
make validate-urls                          # Check for broken URLs
```

## Architecture

### Variant System

Pages use `variants:` frontmatter to control visibility:
```yaml
variants: +flyte +byoc +selfmanaged +serverless
```

Variant-specific content uses shortcodes:
```markdown
{{< variant flyte >}}
Flyte-specific content here
{{< /variant >}}

{{< variant byoc serverless >}}
Union cloud content here
{{< /variant >}}
```

### Key Shortcodes
- `{{< variant ... >}}` - Variant-conditional content
- `{{< key ... >}}` - Product name replacements
- `{{< docs_home {variant} >}}` - Generate doc root links (required for cross-doc links)
- `{{< tab >}}` / `{{< tabs >}}` - Tabbed content
- `{{< note >}}` - Note boxes

### Hugo Configuration Chain

Configs are merged in order:
1. `hugo.toml` - Core settings
2. `hugo.site.toml` - Site-wide settings
3. `hugo.ver.toml` - Version definitions
4. `config.{variant}.toml` - Variant-specific settings
5. `hugo.local.toml` - Local dev overrides (not committed)

### Directory Structure

- `content/` - Markdown source files
- `layouts/shortcodes/` - Custom Hugo shortcodes
- `external/unionai-examples/` - Git submodule with tutorials
- `tools/` - Python build tools (API generator, LLM doc builder, shortcode processor)
- `scripts/` - Build shell scripts
- `dist/` - Build output

### LLM Documentation Pipeline

The build generates `llms-full.txt` files for each variant - consolidated single-file docs optimized for LLM consumption with hierarchical link references.

## Development Setup

1. Install Hugo >= 0.145.0: `brew install hugo`
2. Copy config: `cp hugo.local.toml~sample hugo.local.toml`
3. Run: `make dev`

Development settings in `hugo.local.toml`:
- `variant` - Active variant (flyte, byoc, serverless, selfmanaged)
- `show_inactive` - Show content from other variants
- `highlight_active` - Highlight active variant content

## Build Constraints

- Pre-build checks block absolute URLs to union.ai/docs - use `{{< docs_home {variant} >}}` instead
- Hugo version must be >= 0.145.0
- Python 3.8+ required for build tools

## Content Guidelines

When adding documentation:
1. Set `variants:` frontmatter to specify which variants include the page
2. Use `{{< variant ... >}}` blocks for variant-specific content
3. Use `{{< key ... >}}` for product names that vary by variant
4. Link to other docs with `{{< docs_home {variant} >}}`, not absolute URLs

## Active Projects

- **Visual QA System** (`tools/visual_qa/`): Automated screenshot capture and Claude Vision analysis for detecting rendering issues. See `tools/visual_qa/PROJECT_STATUS.md` for current status, next steps, and commands.
