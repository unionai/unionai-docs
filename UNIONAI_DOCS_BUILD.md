# Union.ai Documentation Build System

This document describes how the Union.ai documentation platform works, including local development, production builds, the Cloudflare Pages deployment pipeline, LLM documentation generation, and CI checks.

## Table of contents

- [Requirements](#requirements)
- [Local development](#local-development)
  - [Developer experience](#developer-experience)
  - [Controlling the development environment](#controlling-the-development-environment)
  - [Changing variants](#changing-variants)
- [Managing tutorial pages](#managing-tutorial-pages)
- [Production builds](#production-builds)
  - [What `make dist` does](#what-make-dist-does)
  - [Testing the production build locally](#testing-the-production-build-locally)
- [Cloudflare Pages deployment](#cloudflare-pages-deployment)
  - [Build settings](#build-settings)
  - [Environment variables](#environment-variables)
  - [How the Cloudflare build works](#how-the-cloudflare-build-works)
  - [Testing the Cloudflare build locally](#testing-the-cloudflare-build-locally)
- [Redirect management](#redirect-management)
  - [How redirects work](#how-redirects-work)
  - [Automatic redirect detection](#automatic-redirect-detection)
  - [Deploying redirects to Cloudflare](#deploying-redirects-to-cloudflare)
- [LLM documentation pipeline](#llm-documentation-pipeline)
  - [Overview](#overview)
  - [Architecture](#architecture)
  - [Processing pipeline](#processing-pipeline)
  - [Output files](#output-files)
  - [Key implementation details](#key-implementation-details)
  - [Benefits for LLM usage](#benefits-for-llm-usage)
- [CI checks on pull requests](#ci-checks-on-pull-requests)
  - [Check API Docs](#check-api-docs-check-api-docs)
  - [Check Images](#check-images-check-images)
  - [Check Jupyter Notebooks](#check-jupyter-notebooks-check-jupyter)
  - [Check Redirects](#check-redirects-check-redirects)
  - [Cloudflare Pages preview](#cloudflare-pages-preview)
  - [Quick fix for most failures](#quick-fix-for-most-failures)
- [Troubleshooting](#troubleshooting)
  - [Missing content](#missing-content)
  - [Page visibility](#page-visibility)
  - [Build failures](#build-failures)

---

## Requirements

1. **Hugo** (>= 0.145.0)

   ```
   brew install hugo
   ```

2. **Python** (>= 3.8) for build tools (API generator, LLM doc builder, shortcode processor).

3. **Local configuration file**

   Copy the sample configuration and customize it:

   ```
   cp hugo.local.toml~sample hugo.local.toml
   ```

   Review `hugo.local.toml` before starting development. See [Controlling the development environment](#controlling-the-development-environment) for available settings.

## Local development

Start the development server:

```
make dev
```

This launches the site at `localhost:1313` in development mode with hot reloading. Edit content files and the browser refreshes automatically.

### Developer experience

The development environment gives you live preview and variant-aware rendering. You can see content from all variants at once, highlight the active variant's content, and identify pages missing from a variant.

### Controlling the development environment

Change how the development environment works by setting values in `hugo.local.toml`:

| Setting              | Description                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `variant`            | The current variant to display. Change this, save, and the browser refreshes automatically with the new variant. |
| `show_inactive`      | If `true`, shows all content that did not match the variant. Useful for seeing all variant sections at once.      |
| `highlight_active`   | If `true`, highlights the *current* content for the variant.                                                     |
| `highlight_keys`     | If `true`, highlights replacement keys and their values.                                                         |

### Changing variants

Variants are flavors of the site (flyte, byoc, selfmanaged, serverless). During development, render any variant by setting it in `hugo.local.toml`:

```toml
variant = "byoc"
```

To show content from other variants alongside the active one:

```toml
show_inactive = true
```

To highlight the active variant's content (to distinguish it from common content):

```toml
highlight_active = true
```

## Managing tutorial pages

Tutorials are maintained in the [unionai-examples](https://github.com/unionai/unionai-examples) repository and imported as a git submodule in the `external` directory.

To initialize the submodule on a fresh clone:

```
make init-examples
```

To update the submodule to the latest `main` branch:

```
make update-examples
```

## Production builds

### What `make dist` does

```
make dist
```

This is the main production build command. It performs the following steps:

1. Converts Jupyter notebooks from `external/unionai-examples` to markdown
2. Runs `make update-redirects` to detect moved pages and update `redirects.csv`
3. Builds all four Hugo variants (flyte, byoc, selfmanaged, serverless) into the `dist/` directory
4. Generates LLM-optimized documentation (`llms-full.txt`) for each variant
5. Regenerates API reference documentation from the latest SDK packages

`make dist` is the single command that regenerates everything. If CI checks are failing, running `make dist` locally and committing the changed files will usually fix them.

### Testing the production build locally

Serve the `dist/` directory with a local web server:

```
make serve PORT=4444
```

If no port is specified, defaults to `PORT=9000`. Open `http://localhost:<port>` to view the site as it would appear at its official URL.

## Cloudflare Pages deployment

The production site is deployed via Cloudflare Pages.

### Build settings

Configure your Cloudflare Pages project with these settings:

| Setting                  | Value                              |
| ------------------------ | ---------------------------------- |
| **Framework preset**     | None (Custom/Static site)          |
| **Build command**        | `chmod +x build.sh && ./build.sh`  |
| **Build output directory** | `dist`                           |
| **Root directory**       | `/`                                |

### Environment variables

Set these in the Cloudflare Pages dashboard:

- `PYTHON_VERSION`: `3.9` (or higher)
- `NODE_VERSION`: `18` (or higher)

### How the Cloudflare build works

1. The `build.sh` script installs Python dependencies using pip3
2. Runs `make dist`, which builds all documentation variants
3. The Python processor (`process_shortcodes.py`) converts Hugo shortcodes to markdown
4. Output is generated in the `dist/` directory for Cloudflare Pages to serve

### Testing the Cloudflare build locally

To test the build process locally (without uv):

```bash
pip3 install -r requirements.txt
chmod +x build.sh
./build.sh
```

The build script automatically falls back from `uv run` to `python3` if uv is not available.

## Redirect management

### How redirects work

When content pages are moved or renamed, `redirects.csv` tracks the old-to-new URL mappings. These are deployed to Cloudflare as a Bulk Redirect List, so old URLs automatically redirect to the new locations.

Each row in `redirects.csv` has seven columns:

| Column | Description                |
| ------ | -------------------------- |
| 1      | Source URL                 |
| 2      | Target URL                 |
| 3      | HTTP status code (e.g., 302) |
| 4      | Include subdomains (TRUE/FALSE) |
| 5      | Subpath matching (TRUE/FALSE) |
| 6      | Preserve query string (TRUE/FALSE) |
| 7      | Preserve path suffix (TRUE/FALSE) |

### Automatic redirect detection

The `detect_moved_pages.py` script scans git history for file renames under `content/` and generates redirect entries for all four variants. Run it with:

```
make update-redirects
```

This is also called automatically by `make dist`.

### Deploying redirects to Cloudflare

Redirects are deployed to Cloudflare automatically via GitHub Actions when `redirects.csv` is modified on the `main` branch. The `deploy_redirects.py` script reads the CSV, converts it to the Cloudflare API format, and replaces all items in the Bulk Redirect List via a single PUT request.

The workflow can also be triggered manually from the Actions tab in GitHub.

For local deployment (requires environment variables `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_LIST_ID`):

```
make deploy-redirects
```

For a dry run that parses the CSV without making API calls:

```
python3 tools/redirect_generator/deploy_redirects.py --dry-run
```

## LLM documentation pipeline

### Overview

The build generates consolidated, LLM-optimized documentation files from the Hugo source. These are single-file documents with all internal links converted to hierarchical text references, designed for use with Large Language Models.

### Architecture

**Source content structure:**
```
content/
├── user-guide/
│   ├── getting-started/
│   │   ├── index.md
│   │   ├── local-setup.md
│   │   └── ...
│   ├── task-configuration/
│   └── ...
├── tutorials/
├── integrations/
└── ...
```

**Generated output structure:**
```
dist/docs/v2/
├── flyte/
│   ├── md/           # Hugo-generated markdown
│   └── llms-full.txt # LLM-optimized consolidated doc
├── byoc/
│   ├── md/
│   └── llms-full.txt
├── selfmanaged/
│   └── ...
└── serverless/
    └── ...
```

### Processing pipeline

1. **Documentation regeneration**: `make dist` rebuilds all Hugo variants.

2. **Variant discovery**: Automatically discovers available variants in `dist/docs/v2/`.

3. **Page traversal**: Starting from `md/index.md`, follows `## Subpages` links depth-first:
   ```markdown
   ## Subpages
   - [User Guide](user-guide/index.md)
   - [Tutorials](tutorials/index.md)
   ```

4. **Hierarchy building**: Builds complete page hierarchy as it traverses:
   - `index.md` → "Documentation"
   - `user-guide/index.md` → "Documentation > User Guide"
   - `user-guide/getting-started/local-setup.md` → "Documentation > User Guide > Getting Started > Local Setup"

5. **Heading analysis**: For each page, parses all markdown headings to build an anchor lookup:
   ```markdown
   # Local Setup                    → Page title (already in hierarchy)
   ## Setting up a configuration    → "Getting Started > Local Setup > Setting up a configuration file"
   ### Specify explicitly           → "Getting Started > Local Setup > Setting up a configuration file > Specify explicitly"
   ```

6. **Link processing**: Converts all internal links to hierarchical references:
   - **Cross-page links:** `[Local setup](local-setup.md)` → `**Getting started > Local setup**`
   - **Anchor links:** `[Config](local-setup.md#setting-up-a-configuration-file)` → `**Getting started > Local setup > Setting up a configuration file**`
   - **Same-page anchors:** `[Image building](#image-building)` → `**Task configuration > Container images > Image building**`
   - **External links:** Preserved unchanged
   - **Cross-variant links:** Preserved unchanged
   - **Static files:** Preserved unchanged

### Output files

Two files are generated per variant:

1. **`llms-full.txt`** — The complete consolidated documentation:
   - Complete documentation for that variant in depth-first order
   - Page delimiters: `=== PAGE: path/to/file.md ===`
   - Hierarchical internal links: All `.md` and `#anchor` links converted to `**Page > Section**` format
   - Preserved external links: GitHub, cross-variant, and static file links unchanged

2. **`llms.txt`** — A redirect/discovery file:
   - Brief explanation of the LLM documentation system
   - Link to the corresponding `llms-full.txt` file
   - Variant and version information
   - Usage guidance for LLMs and RAG systems

### Key implementation details

**Lookup table system.** The builder maintains a comprehensive lookup table mapping file paths and anchors to hierarchical names:
```
# Pages
"user-guide/getting-started/local-setup.md" → "Getting Started > Local Setup"

# Anchors
"local-setup.md#using-the-configuration-file" → "Getting Started > Local Setup > Using the configuration file"
```

**Anchor generation.** Heading titles are converted to URL anchors using standard rules:
- Lowercase conversion
- Space to hyphen replacement
- Special character removal
- Example: "Setting up a Configuration File" → "setting-up-a-configuration-file"

**Hierarchy optimization.** The system automatically strips redundant prefixes:
- Raw: "Documentation > Flyte > Getting Started > Local Setup"
- Optimized: "Getting Started > Local Setup" (in flyte variant)

**Error handling:**
- Missing files: Warnings logged, processing continues
- Broken links: Fallback to link text with current context
- Invalid anchors: Graceful fallback to text-based reference

### Benefits for LLM usage

**Internal references:**
- No broken links — all internal `.md` references point to content in the same file
- Searchable — LLMs can find any referenced content by searching hierarchical titles
- Context-rich — every reference includes full page and section hierarchy
- Consistent format — all internal references follow `**Page > Section**` pattern

**Complete content:**
- Single file — all documentation in one consolidated file per variant
- Proper order — content follows logical depth-first navigation structure
- No duplication — each page appears exactly once

**LLM-friendly format:**
- Clear delimiters for page boundaries
- Hierarchical structure matching how humans think about documentation
- No file system dependencies — all references are text-based within the same document

**Integration targets:**
- Vector databases for semantic search
- RAG systems for question answering
- AI assistants for documentation support
- API documentation tools that consume markdown
- Training datasets for domain-specific models

### Updating the LLM docs

The LLM documentation builder automatically regenerates content from the current Hugo source:

1. Modify files in `content/`
2. Run `make dist` (or `python build_llm_docs.py` directly)
3. New files are included automatically if linked via `## Subpages`
4. New Hugo variants are automatically detected and processed

## CI checks on pull requests

Every push triggers five checks. Four are GitHub Actions workflows; one is a Cloudflare Pages build preview.

### Check API Docs (`check-api-docs`)

**What it checks:** Whether the committed API reference docs match what the latest SDK versions would generate.

**Why it fails:** The upstream `flyte-sdk` or plugin packages released a new version and the generated API docs in `content/api-reference/` are stale.

**How to fix:**
```bash
make update-api-docs
```
Then commit the changed files in `content/api-reference/`, `data/flytesdk.yaml`, and `static/flytesdk-linkmap.json`.

### Check Images (`check-images`)

**What it checks:** That all images referenced in content files actually exist in the repository.

**Why it fails:** A content file references an image that doesn't exist, was deleted, or was moved without updating the reference.

**How to fix:** Ensure the image file exists at the path referenced in the markdown. Run `make check-images` locally to see which references are broken.

### Check Jupyter Notebooks (`check-jupyter`)

**What it checks:** That generated markdown from Jupyter notebooks is up to date with the source notebooks in `external/unionai-examples`.

**Why it fails:** A notebook in the examples submodule was updated but the generated markdown wasn't regenerated.

**How to fix:**
```bash
make update-examples    # pull latest notebooks
make dist               # regenerates everything including notebook markdown
```
Then commit the changed files.

### Check Redirects (`check-redirects`)

**What it checks:** That `redirects.csv` includes entries for all file renames detected in git history.

**Why it fails:** A content file was renamed or moved but the corresponding redirect entries weren't added to `redirects.csv`.

**How to fix:**
```bash
make update-redirects
```
Then commit the updated `redirects.csv`.

### Cloudflare Pages preview

**What it checks:** Builds a deploy preview of the site.

**How to use:** Click the "Details" link to view a preview of your changes. This is not a pass/fail check — it just provides a preview URL.

### Quick fix for most failures

Running `make dist` locally regenerates everything: API docs, redirects, and notebook conversions. It's the single command that covers all the generated-file checks. Commit any changed files afterward.

## Troubleshooting

### Missing content

Content may be hidden due to `{{< variant ... >}}` blocks. To see what's missing, adjust the variant show/hide settings in development mode.

For a production-like view:

```toml
show_inactive = false
highlight_active = false
```

For full developer visibility:

```toml
show_inactive = true
highlight_active = true
```

### Page visibility

The developer site shows in red any pages missing from the variant. For a page to exist in a variant, it must be listed in the `variants:` frontmatter at the top of the file. Clicking on a red page gives you the path you need to add.

See [Contributing docs and examples](https://union.ai/docs/flyte/community/contributing-docs) for authoring guidelines.

### Build failures

If the Cloudflare Pages build fails:

1. Check that Python 3.8+ is available
2. Verify that the `toml` package can be installed
3. Check Hugo version compatibility (must be >= 0.145.0)
4. Review build logs for specific Python errors

The build script automatically falls back from `uv run` to `python3` if uv is not available.
