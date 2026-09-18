# CLAUDE.md — unionai-docs / unionai-docs-infra

This file provides guidance for working with the Union.ai documentation repositories. It is shared between `unionai-docs` (parent) and `unionai-docs-infra` (submodule).

## Selfmanaged & Selfhosted Context

For selfhosted or selfmanaged context, refer to the Notion guide:
https://www.notion.so/3108cc06513d81a08bb1d3b9135385f1

## Path-scoped rules

`.claude/rules/` carries subsystem knowledge that loads only when you touch the matching files —
search indexes, routing and redirects, generated content, the LLM surface, variants and versions,
and authoring. `contributing.md` there loads always: **sign off every commit (`git commit -s`)**,
since "Check DCO" is a required status check.

## Project Overview

Multi-variant Hugo documentation site for Flyte (open-source) and Union.ai products. A single source generates two variants:
- **flyte** — Open-source Flyte orchestration platform
- **union** — Union.ai commercial product (covers both BYOC and Self-managed deployments)

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

**`unionai-docs-infra/`** — shared build infrastructure (identical across branches).
**Policy (DOC-1329): content is versioned; chrome is promoted.** Infra/theme changes ship via a
submodule pointer bump, never a cut. Details: `unionai-docs-infra/VERSIONING.md`.
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

Every page MUST declare its variants in frontmatter — `variants: +flyte +union`. `+` includes,
`-` excludes, and **all variants must be listed explicitly**; there is no default.

Block-level gating uses a different syntax — a bare list of the variants that may see the block:

```markdown
{{< variant union >}}
{{< markdown >}}
This appears only in the Union variant.
{{< /markdown >}}
{{< /variant >}}
```

**Hugo quirk:** inside container shortcodes, wrap Markdown content with `{{< markdown >}}`.

Gating traps (naming every variant guards nothing; blocks do not nest) are in
`.claude/rules/variants-and-versions.md`.

### Variant keys

For inline text that varies by variant:

```markdown
The {{< key product_name >}} platform...
```

Keys are defined in `hugo.site.toml` under `[params.key]`. Common keys: `product_name`,
`product_full_name`, `cli`, `kit_name`, `kit_remote`, `docs_home`.

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

### API-reference autolinking

Inline `` `code` `` and Python code blocks are linked to their API reference at runtime by
`inline-code-linker.js` / `codeblock-linker.js`, using `linkmap/*-linkmap.json`.

**Do not write explicit Markdown links for identifiers the autolinker already handles.** Write the
bare backticked identifier — `` `flyte.io.File` ``, `` `flyte.init()` `` — and let the linker wrap
it. Keep an explicit link only when the link text isn't a single backticked identifier, the name
isn't fully qualified, or the target isn't the canonical API page.

Full matcher rules, notices, Python example pages and Jupyter frontmatter:
`.claude/rules/authoring.md` (loads automatically when you edit content).

## Development Setup

1. Install Hugo **extended** at the pin in `unionai-docs-infra/.hugoversion` — `brew install hugo`
2. `cp hugo.local.toml~sample hugo.local.toml`
3. `make dev`

`hugo.local.toml` keys: `variant`, `show_inactive`, `highlight_active`, `highlight_keys`.

## Build Constraints

- Pre-build checks block absolute URLs to union.ai/docs — use `{{< docs_home {variant} >}}` instead
- Hugo version must be >= the pin in `unionai-docs-infra/.hugoversion` (currently 0.161.1). **The floor equals the pin** so local dev and CI build with the same Hugo; `pre-flight.sh` fails below it and warns above it (brew tracks latest, so running ahead of CI is the common skew and the one a floor cannot catch)
- Python >= 3.10 required for the build tools (`requires-python` in `unionai-docs-infra/pyproject.toml`); CI runs 3.12

## API Documentation

Generated from Python docstrings by `tools/api_generator` (respects `__all__`; ignores `_`-prefixed
items and imports). **Never hand-edit `content/api-reference/`** — fix the docstring upstream.
See `.claude/rules/generated-content.md` and `unionai-docs-infra/tools/api_generator/README.md`.

## Redirects

Managed in `unionai-docs-infra/redirects.csv`, deployed automatically by `deploy-redirects.yml`.
The CSV cannot express patterns and retired pins need no row.
See `.claude/rules/routing-redirects.md` and `unionai-docs-infra/ROUTING-ARCHITECTURE.md`.

## LLM Documentation Pipeline

Every page gets a clean Markdown twin at **`<path>.md`**, plus `llms.txt` and `llms-full.txt` per
variant. **One shape only** — `page.md`, `section.md` and `_section.md` are retired and no longer
generated.

See `.claude/rules/llm-surface.md`, `unionai-docs-infra/README.md`, and the LLM-optimized
documentation page in the docs.
