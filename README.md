# Flyte and Union.ai documentation

- **[Flyte Docs](https://www.union.ai/docs/flyte/user-guide/)**
- **[Union BYOC](https://www.union.ai/docs/byoc/user-guide/)**
- **[Union Serverless](https://www.union.ai/docs/serverless/tutorials/)**

This repository holds all documentation for the [Flyte OSS project](https://www.flyte.org) and the [Union.ai](https://www.union.ai) products.

## Repository structure

The docs system uses three repositories:

- **[unionai-docs](https://github.com/unionai/unionai-docs)** (this repo) — version-specific content (`content/`, `data/`, `linkmap/`, `include/`), configuration (`api-packages.toml`, `makefile.inc`), and CI workflows.
- **[unionai-docs-infra](https://github.com/unionai/unionai-docs-infra)** (submodule within `unionai-docs` at `unionai-docs-infra/`) — shared build infrastructure: Hugo config, layouts, themes, Python tools, scripts, and redirect data. Identical across `main` (v2) and `v1` branches.
- **[unionai-examples](https://github.com/unionai/unionai-examples)** (submodule within `unionai-docs` at `unionai-examples/`), contains example code referenced by the docs.

## Quick start

```shell
# Clone with submodules
git clone --recurse-submodules https://github.com/unionai/unionai-docs.git
cd unionai-docs

# Set up local config
cp unionai-docs-infra/hugo.local.toml~sample hugo.local.toml

# Start dev server at localhost:1313
make dev
```

Requires Hugo >= 0.145.0 (`brew install hugo`).

## Further reading

- **[unionai-docs-infra/README.md](https://github.com/unionai/unionai-docs-infra/blob/main/README.md)** — comprehensive build system documentation (local dev, production builds, CI checks, Cloudflare deployment, LLM docs pipeline).
- **[Contributing docs and examples](https://union.ai/docs/flyte/community/contributing-docs)** — authoring guide, shortcodes, variants, API docs (source at `content/community/contributing-docs/`).
