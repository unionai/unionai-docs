---
paths:
  - "content/api-reference/**"
  - "api-packages.toml"
  - "linkmap/**"
  - "include/**"
  - "tools/api_generator/**"
  - "unionai-docs-infra/tools/api_generator/**"
---

# Generated API reference — do not hand-edit

Most of `content/api-reference/` is generated from SDK and plugin docstrings. **Editing a
generated page is always wrong**: the next regeneration silently reverts it.

Fix the **docstring upstream** in `flyte-sdk` (or the plugin package), then regenerate.

- `make check-api-docs` is the drift gate — it fails if committed output no longer matches the
  installed packages.
- `make update-api-docs` regenerates.
- `api-packages.toml` is the registry. Per-package flags a tool must respect: `frozen` (skip
  regen and drift checks entirely), `variants`, `output_folder`, Hugo `weight`, and pinned
  `install` specifiers where a released version pair is broken.

**Prose that *cites* a changed symbol is a separate problem.** A change to the public surface can
ripple into the hand-written guides, and no drift check catches that.

## Inline identifiers are linked at runtime — do not hand-write the link

Backticked identifiers in prose (`flyte.io.File`, `flyte.init()`) are turned into API-reference
links **in the browser** by `assets/js/inline-code-linker.js`, resolving against `linkmap/*.json`.
Write the bare backticked identifier.

Keep an explicit Markdown link only when the link text is not a single inline-code span, the
identifier is in no linkmap, or the target is not the canonical API page.
