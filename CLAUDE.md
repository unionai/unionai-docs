# CLAUDE.md — unionai-docs (v1 branch)

> **This is the v1 (legacy) branch.** It documents Flyte/Union 1.x, which is outdated.
> Active development is on the `main` branch (Flyte/Union 2.0.x).
> Only make changes here for v1-specific fixes — new features go on `main`.

This file provides guidance for working with the Union.ai documentation repositories. It is shared between `unionai-docs` (parent) and `unionai-docs-infra` (submodule).

## Project Overview

Multi-variant Hugo documentation site for Flyte (open-source) and Union.ai products. A single source generates four variants:
- **flyte** — Open-source Flyte orchestration platform
- **byoc** — Union Bring-Your-Own-Cloud
- **serverless** — Union managed cloud service
- **selfmanaged** — Union enterprise self-hosted

## Essential Commands

```bash
# Development (requires hugo.local.toml setup first)
cp hugo.local.toml~sample hugo.local.toml  # First time only
make dev                                    # Start dev server at localhost:1313

# Production build
make dist                                   # Build all variants to dist/
make serve PORT=4444                        # Serve dist/ locally

# Examples submodule
make init-examples                          # Initialize unionai-examples
make update-examples                        # Update to latest

# API documentation regeneration
make -f unionai-docs-infra/Makefile.api.sdk              # SDK API + CLI docs
make -f unionai-docs-infra/Makefile.api.plugins          # Plugin API docs

# Validation
make check-images                           # Validate image references
make check-jupyter                          # Validate Jupyter notebooks
make validate-urls                          # Check for broken URLs
```

## Repository Layout

The repo separates **version-specific content/config** (top level) from **shared build infrastructure** (`unionai-docs-infra/`):

**Top level** — files that differ between `main` (v2) and `v1` branches:
- `makefile.inc` — VERSION, VARIANTS
- `api-packages.toml` — API package registry
- `content/`, `data/`, `linkmap/`, `include/` — Content and generated data

**`unionai-docs-infra/`** — shared build infrastructure (identical across branches):
- `Makefile` — Real build logic (top-level Makefile forwards to this)
- `hugo.toml`, `hugo.site.toml`, `hugo.ver.toml`, `config.{variant}.toml` — Hugo config
- `static/` — Shared static assets (CSS, JS, images)
- `scripts/` — Build shell scripts
- `tools/` — Python build tools
- `layouts/` — Hugo templates, partials, shortcodes
- `themes/` — Hugo theme
- `redirects.csv` — Redirect data

## Hugo Configuration Chain

Configs merge in order:
1. `unionai-docs-infra/hugo.toml` — Core settings (directory remapping for layouts, etc.)
2. `hugo.site.toml` — Site-wide settings (version-specific)
3. `unionai-docs-infra/hugo.ver.toml` — Version definitions
4. `unionai-docs-infra/config.{variant}.toml` — Variant-specific settings
5. `hugo.local.toml` — Local dev overrides (not committed)

## Variant System

### Page-level variants

Every page MUST declare which variants it appears in via frontmatter:

```yaml
---
title: My Page
weight: 3
variants: +flyte +serverless +byoc -selfmanaged
---
```

- `+` includes, `-` excludes
- All variants must be explicitly listed (no defaults)

### Content-level variants

```markdown
{{< variant serverless byoc >}}
{{< markdown >}}
This appears only in Serverless and BYOC.
{{< /markdown >}}
{{< /variant >}}
```

**Hugo quirk**: Inside container shortcodes, wrap Markdown content with `{{< markdown >}}`.

### Variant keys

For inline text that varies by variant:

```markdown
The {{< key product_name >}} platform...
```

Keys defined in `hugo.site.toml` under `[params.key]`. Common keys: `product_name`, `product_full_name`, `cli`, `kit_name`, `kit_remote`, `docs_home`.

## Key Shortcodes

- `{{< variant ... >}}` — Variant-conditional content
- `{{< key ... >}}` — Product name replacements
- `{{< docs_home {variant} >}}` — Doc root links (required for cross-doc links)
- `{{< tabs >}}` / `{{< tab >}}` — Tabbed content
- `{{< code file="..." fragment=name lang=python >}}` — Code inclusion from external files
- `{{< link-card >}}` — Clickable cards
- `{{< py_class_ref class.name >}}` — Python API refs

Fragments in source files:
```python
# {{docs-fragment name}}
code here
# {{/docs-fragment}}
```

Examples at: `http://localhost:1313/__docs_builder__/shortcodes/` (dev mode only)

## Page Settings (Frontmatter)

```yaml
---
title: Page Title
weight: 3              # Lower weight = higher in nav
variants: +flyte ...   # Variant visibility (all must be listed)
top_menu: true         # Makes this a top tab
sidebar_expanded: true # Expands section by default
toc_max: 3             # Max heading level in TOC
mermaid: true          # Enable Mermaid diagrams
---
```

Navigation: lower `weight` = higher position. `weight: 0` or missing = alphabetical at end.

## Content Authoring

### Notices

```markdown
> [!NOTE] Title
> Content here

> [!WARNING] Title
> Warning content
```

### Python example pages

```yaml
---
layout: py_example
example_file: /path/to/file.py
run_command: union run --remote path/to/file.py main
source_location: https://github.com/unionai/unionai-examples/tree/main/path
---
```

### Jupyter notebooks

```yaml
---
jupyter_notebook: /path/to/notebook.ipynb
---
```

## Development Setup

1. Install Hugo >= 0.145.0: `brew install hugo`
2. Copy config: `cp hugo.local.toml~sample hugo.local.toml`
3. Run: `make dev`

Dev settings in `hugo.local.toml`:
```toml
variant = "byoc"           # Active variant
show_inactive = true       # Show other variants grayed out
highlight_active = true    # Highlight active variant content
highlight_keys = true      # Show key replacements
```

## Build Constraints

- Pre-build checks block absolute URLs to union.ai/docs — use `{{< docs_home {variant} >}}` instead
- Hugo version must be >= 0.145.0
- Python 3.8+ required for build tools

## API Documentation

Generated from Python packages using `tools/api_generator`:
- Build with `make -f unionai-docs-infra/Makefile.api.sdk` or `Makefile.api.plugins`
- Respects `__all__` in packages
- Ignores `_` prefixed items and imports (unless in `__all__`)

## Redirects

Managed in `unionai-docs-infra/redirects.csv`. Applied to CloudFlare by Union employee.

## LLM Documentation Pipeline

The build generates `llms.txt` (page index) and `llms-full.txt` (complete docs) for each variant, optimized for LLM consumption.
