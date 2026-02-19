# Top-Level Directory & File Inventory

## Hugo Site Structure

| Item | Description |
|---|---|
| `content/` | Markdown source files for all documentation pages |
| `layouts/` | Hugo layout templates, shortcodes, page templates, `robots.txt` |
| `themes/` | Hugo `union/` theme with site-wide layouts |
| `static/` | Static assets (CSS, JS, images) served as-is |
| `data/` | Hugo data files (API docs YAML, configuration data) |
| `archetypes/` | Hugo archetype for `hugo new` content scaffolding |
| `public/` | Hugo dev server output directory (used by `make dev`, gitignored) |
| `dist/` | Production build output (used by `make dist`, gitignored) |

## Hugo Configuration

Hugo merges all `hugo.*.toml` and `config.*.toml` files into a single configuration.

| Item | Description |
|---|---|
| `hugo.toml` | Core Hugo settings: output formats, menus, module config |
| `hugo.site.toml` | Site-wide settings: variant keys, product names, params |
| `hugo.ver.toml` | Version definitions (current version number) |
| `hugo.dev.toml` | Dev server overrides: baseURL, redirect rules (used by `make dev`) |
| `hugo.local.toml` | Local developer overrides: variant selection, content visibility (gitignored) |
| `hugo.local.toml~sample` | Template for creating `hugo.local.toml` |
| `config.byoc.toml` | Variant-specific config for BYOC |
| `config.flyte.toml` | Variant-specific config for Flyte OSS |
| `config.selfmanaged.toml` | Variant-specific config for Self-managed |
| `config.serverless.toml` | Variant-specific config for Serverless |

## Build System

| Item | Description |
|---|---|
| `Makefile` | Primary build orchestrator: `make dist`, `make dev`, `make serve`, `make llm-docs`, etc. |
| `makefile.inc` | Shared Makefile variables (version number) |
| `Makefile.api.sdk` | Config-driven API documentation generation for SDKs and CLIs |
| `Makefile.api.plugins` | API documentation generation for Flyte plugins |
| `build.sh` | Cloudflare Pages build entry point (installs deps, runs `make dist`) |
| `scripts/` | Shell scripts: serve (`Caddyfile`), pre-build checks, 404 page generation |
| `tools/` | Python tools: LLM doc builder, shortcode processor, API generator, link checker, redirect generator, URL validator |
| `include/` | Makefile include fragments and API documentation preambles |
| `pyproject.toml` | Python package configuration for build tools |
| `requirements.txt` | Minimal Python deps (`toml`) for Cloudflare Pages builds |
| `setup-api-generator.sh` | Developer script to set up the API generator virtual environment |

## Content Infrastructure

| Item | Description |
|---|---|
| `external/` | Git submodule containing `unionai-examples` (tutorial and example code) |
| `redirects.csv` | Redirect rules deployed to Cloudflare |
| `.redirects-checkpoint` | Git commit hash tracking the last redirect update |
| `.redirects-exclude` | Path patterns excluded from redirect detection |
| `api-packages.toml` | Package list for API documentation generation |
| `404.html.tmpl` | Template for generating variant-specific 404 pages |
| `404.inc.html~flyte` | Flyte-specific 404 page include with legacy redirect JavaScript |
| `index.html.tmpl` | Template for root `index.html` (auto-redirects to `/byoc/` variant) |
| `templates/` | Contains `markdown.tmpl` for protobuf documentation generation |

## Validation & Testing

| Item | Description |
|---|---|
| `tests/` | Test scripts: CLI docs coverage, link processing, markdown tree analysis |
| `.link-checker-exclude` | Regex exclusion patterns for the internal link checker |

## CI/CD & Project Config

| Item | Description |
|---|---|
| `.github/` | GitHub Actions workflows: check-api-docs, check-images, check-links, check-redirects, deploy-redirects |
| `.gitignore` | Git ignore rules |
| `.gitmodules` | Git submodule config for `external/unionai-examples` |
| `CLAUDE.md` | Instructions for Claude Code when working in this repository |
| `CODEOWNERS` | GitHub code ownership rules |
| `README.md` | Project README |
| `LICENSE` | Apache 2.0 license |
| `UNIONAI_DOCS_BUILD.md` | Comprehensive build system documentation |
| `TOP_LEVEL_AUDIT.md` | This file |

## Local Development Artifacts (gitignored)

These are generated locally and not tracked in git.

| Item | Description |
|---|---|
| `.venv/` | Python virtual environment |
| `__pycache__/` | Python bytecode cache |
| `.hugo_build.lock` | Hugo build lock file |
| `uv.lock` | UV package manager lock file |
| `.vscode/` | VS Code workspace settings |
| `.claude/` | Claude Code configuration |
