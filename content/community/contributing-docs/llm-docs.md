---
title: LLM-optimized documentation
weight: 8
variants: +flyte +serverless +byoc +selfmanaged
---

# LLM-optimized documentation

The build pipeline generates LLM-optimized versions of every page and several index files,
designed for use by AI coding agents and AI search engines.

## Output files

The `make dist` command (specifically the `make llm-docs` step) produces the following
in each variant's `dist/docs/v2/{variant}/` directory:

| File | Description |
|------|-------------|
| `page.md` | Per-page LLM-optimized Markdown, generated alongside every `index.html`. Links between pages use relative `page.md` references, then are converted to absolute URLs in a final pass. |
| `section.md` | A single-file bundle concatenating all pages in a section. Only generated for sections with `llm_readable_bundle: true` in frontmatter. Internal links become hierarchical bold references; external links become absolute URLs. |
| `llms.txt` | Page index listing every page grouped by section, with H2/H3 headings for discoverability. Sections with bundles are marked with a "Section bundle" link. |
| `llms-full.txt` | The entire documentation for one variant as a single file, with all internal links converted to hierarchical bold references (e.g. `**Configure tasks > Resources**`). |

### Discovery hierarchy

```
dist/docs/llms.txt                          # Root: lists versions
dist/docs/v2/llms.txt                       # Version: lists variants
dist/docs/v2/{variant}/llms.txt             # Variant: page index with headings
dist/docs/v2/{variant}/llms-full.txt        # Full consolidated doc
dist/docs/v2/{variant}/**/page.md           # Per-page Markdown
dist/docs/v2/{variant}/**/section.md        # Section bundles (where enabled)
```

## How `page.md` files are generated

1. Hugo builds the site into `dist/` and also outputs a Markdown format into `tmp-md/`.
2. `process_shortcodes.py` reads from `tmp-md/`, resolves all shortcodes (variants, code includes, tabs, notes, etc.), and writes the result as `page.md` alongside each `index.html`.
3. `fix_internal_links_post_processing()` converts all internal links in `page.md` files to point to other `page.md` files using relative paths.
4. `build_llm_docs.py` then enhances subpage listings with H2/H3 headings, generates section bundles, converts all relative links to absolute URLs, and creates the `llms.txt` and `llms-full.txt` index files.

## Enabling section bundles

To produce a `section.md` bundle for a documentation section:

1. Add `llm_readable_bundle: true` to the frontmatter of the section's `_index.md`:

   ```yaml
   ---
   title: Configure tasks
   weight: 8
   variants: +flyte +serverless +byoc +selfmanaged
   llm_readable_bundle: true
   ---
   ```

2. Add the `{{</* llm-bundle-note */>}}` shortcode in the body of the same `_index.md`,
   right after the page title:

   ```markdown
   # Configure tasks

   {{</* llm-bundle-note */>}}

   As we saw in ...
   ```

   This renders a note on the HTML page pointing readers to the `section.md` file.

Both the frontmatter parameter and the shortcode are required.
A CI check (`check-llm-bundle-notes`) verifies they are always in sync.

## The `llms-full.txt` link conversion

In `llms-full.txt`, all internal `page.md` links are converted to hierarchical bold references:

* Cross-page: `[Resources](../resources/page.md)` becomes `**Configure tasks > Resources**`
* Same-page anchor: `[Image building](#image-building)` becomes `**Container images > Image building**`
* External links (http/https) are preserved unchanged.

This makes the file self-contained with no broken references.

## Regenerating

LLM documentation is regenerated automatically as part of `make dist`.
To regenerate only the LLM files without a full rebuild:

```
make llm-docs
```

New pages are included automatically if linked via `## Subpages` in their parent's Hugo output.
