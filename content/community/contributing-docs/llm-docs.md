---
title: LLM-optimized documentation
weight: 9
variants: +flyte +union
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
| `_section.md` | A single-file bundle holding one level of a section: its landing page and its own pages in full, then each immediate sub-section. Generated for every section that has more than its own landing page, and capped at 200 KB. Internal links become hierarchical bold references; external links become absolute URLs. |
| `llms.txt` | Page index listing every page grouped by section, with H2/H3 headings for discoverability. Sections with bundles are marked with a "Section bundle (one level)" link. |
| `llms-full.txt` | The entire documentation for one variant as a single file, with all internal links converted to hierarchical bold references (e.g. `**Configure tasks > Resources**`). |

### Discovery hierarchy

```
dist/docs/llms.txt                          # Root: lists versions
dist/docs/v2/llms.txt                       # Version: lists variants
dist/docs/v2/{variant}/llms.txt             # Variant: page index with headings
dist/docs/v2/{variant}/llms-full.txt        # Full consolidated doc
dist/docs/v2/{variant}/**/page.md           # Per-page Markdown
dist/docs/v2/{variant}/**/_section.md       # Section bundles (one level down)
```

## How `page.md` files are generated

1. Hugo builds the site into `dist/` and also outputs a Markdown format into `tmp-md/`.
2. `process_shortcodes.py` reads from `tmp-md/`, resolves all shortcodes (variants, code includes, tabs, notes, etc.), and writes the result as `page.md` alongside each `index.html`.
3. `fix_internal_links_post_processing()` converts all internal links in `page.md` files to point to other `page.md` files using relative paths.
4. `build_llm_docs.py` then enhances subpage listings with H2/H3 headings, generates section bundles, converts all relative links to absolute URLs, and creates the `llms.txt` and `llms-full.txt` index files.

## How section bundles are generated

Bundle membership is structural, so there is nothing to opt into. Every section that has
more than its own landing page gets a `_section.md` at build time, and a section whose
only page is its landing page gets none, because that content already lives at its own
`page.md` URL.

A bundle holds one level of the tree: the section's landing page and its own pages in
full, then each immediate sub-section. It is capped at 200 KB (`BUNDLE_SIZE_LIMIT` in
`build_llm_docs.py`), and children are abridged to fit, largest first. A child is
abridged either because it has more beneath it, in which case its landing page stands in
and links onward to its own `_section.md`, or because the bundle hit the size cap, in
which case the child is cut to a short excerpt linking to its `page.md`. The manifest at
the top of each bundle reports the two separately. A section's own pages are never cut,
so a bundle that cannot fit even after abridging every sub-section is written over the
cap and says so in its manifest.

The LLM-optimized files are not surfaced as links on the pages they cover. They exist
in the build and are reached through `llms.txt`, so there is nothing to add to the page
body.

## The `llms-full.txt` link conversion

In `llms-full.txt`, all internal `page.md` links are converted to hierarchical bold references:

* Cross-page: `[Resources](../resources/page.md)` becomes `**Configure tasks > Resources**`
* Same-page anchor: `[Image building](#image-building)` becomes `**Container images > Image building**`
* External links (`http`/`https`) are preserved unchanged.

This makes the file self-contained with no broken references.

## Regenerating

LLM documentation is regenerated automatically as part of `make dist`.
To regenerate only the LLM files without a full rebuild:

```
make llm-docs
```

New pages are included automatically if linked via `## Subpages` in their parent's Hugo output.
