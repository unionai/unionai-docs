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
  - [Generated output structure](#generated-output-structure)
  - [Processing pipeline](#processing-pipeline)
  - [Section bundles](#section-bundles-sectionmd)
  - [Key implementation details](#key-implementation-details)
  - [Updating the LLM docs](#updating-the-llm-docs)
- [CI checks on pull requests](#ci-checks-on-pull-requests)
  - [Check API Docs](#check-api-docs-check-api-docs)
  - [Check Images](#check-images-check-images)
  - [Check Jupyter Notebooks](#check-jupyter-notebooks-check-jupyter)
  - [Check Redirects](#check-redirects-check-redirects)
  - [Cloudflare Pages preview](#cloudflare-pages-preview)
  - [Quick fix for most failures](#quick-fix-for-most-failures)

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

The build generates LLM-optimized documentation at four levels of granularity, designed for AI coding agents and AI search engines:

| File | Scope | Description |
|------|-------|-------------|
| `page.md` | Per page | Clean Markdown version of every page, with links to other `page.md` files |
| `section.md` | Per section | Single-file bundle of all pages in a section (where enabled) |
| `llms.txt` | Per variant | Page index with H2/H3 headings, grouped by section |
| `llms-full.txt` | Per variant | Entire documentation as one file with hierarchical link references |

### Generated output structure

```
dist/docs/llms.txt                          # Root discovery: lists versions
dist/docs/v2/llms.txt                       # Version discovery: lists variants
dist/docs/v2/{variant}/
├── llms.txt                                # Page index with headings
├── llms-full.txt                           # Full consolidated doc
├── page.md                                 # Root page
├── user-guide/
│   ├── page.md                             # User Guide landing page
│   ├── task-configuration/
│   │   ├── page.md                         # Section landing page
│   │   ├── section.md                      # Section bundle (all pages concatenated)
│   │   ├── resources/
│   │   │   └── page.md
│   │   ├── caching/
│   │   │   └── page.md
│   │   └── ...
│   └── ...
└── ...
```

### Processing pipeline

The `make llm-docs` target (called automatically by `make dist`) runs two scripts in sequence:

**Stage 1: `process_shortcodes.py`** — Generates `page.md` files

1. Reads Hugo's Markdown output from `tmp-md/` (Hugo builds this alongside HTML via the MD output format).
2. Resolves all shortcodes: `{{< variant >}}`, `{{< code >}}`, `{{< tabs >}}`, `{{< note >}}`, `{{< key >}}`, `{{< llm-bundle-note >}}`, etc.
3. Writes the result as `page.md` alongside each `index.html` in `dist/`.
4. Converts all internal links to point to other `page.md` files using relative paths.

**Stage 2: `build_llm_docs.py`** — Generates bundles and indexes

1. **Lookup tables**: Traverses all `page.md` files depth-first via `## Subpages` links, building a lookup table mapping file paths and anchors to hierarchical titles (e.g. `"user-guide/task-configuration/resources/page.md"` → `"Configure tasks > Resources"`).
2. **`llms-full.txt`**: Processes all pages, converting internal `page.md` links to hierarchical bold references (e.g. `**Configure tasks > Resources**`).
3. **Subpage enhancement**: Adds H2/H3 headings to `## Subpages` listings in `page.md` files.
4. **Section bundles**: Generates `section.md` for sections with `llm_readable_bundle: true`.
5. **Link absolutization**: Converts all relative links in `page.md` files to absolute URLs (`https://www.union.ai/docs/...`).
6. **`llms.txt`**: Creates the page index with headings and bundle references.

### Section bundles (`section.md`)

To enable a `section.md` bundle for a documentation section, two things are required in the section's `_index.md`:

1. Frontmatter: `llm_readable_bundle: true`
2. Body: `{{< llm-bundle-note >}}` shortcode (renders a note pointing to the bundle)

A CI check (`check-llm-bundle-notes`) verifies these are always in sync.

In section bundles, links to pages within the section become hierarchical bold references, while links to pages outside the section become absolute URLs.

### Key implementation details

**Link conversion in `llms-full.txt`:**
- Cross-page: `[Resources](../resources/page.md)` → `**Configure tasks > Resources**`
- Anchor: `[Caching](../caching/page.md#cache-versions)` → `**Configure tasks > Caching > Cache versions**`
- Same-page: `[Image building](#image-building)` → `**Container images > Image building**`
- External links preserved unchanged

**Hierarchy optimization:** Strips the `Documentation > {Variant}` prefix automatically.

**Error handling:** Missing files log warnings; broken links fall back to link text with context. A `link-issues.txt` report is written per variant.

### Updating the LLM docs

LLM documentation regenerates automatically as part of `make dist`. To regenerate only the LLM files:

```
make llm-docs
```

New pages are included automatically if linked via `## Subpages` in their parent's Hugo output. New variants are detected automatically.

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
