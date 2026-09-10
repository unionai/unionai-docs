---
title: LLM-optimized documentation
description: The markdown twins and index files the build generates for AI agents and search.
icon: robot
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
| `<page>.md` | Per-page Markdown, served at each page's own URL with `.md` appended. A section landing page's twin also carries a `## Subpages` block listing every page beneath it, with each child's description and H2/H3 headings, so it is the index for its section. |
| `llms.txt` | Page index listing every page grouped by section, with H2/H3 headings for discoverability. |
| `llms-full.txt` | The entire documentation for one variant as a single file, with all internal links converted to hierarchical bold references (e.g. `**Configure tasks > Resources**`). |

### Discovery hierarchy

```
dist/docs/llms.txt                          # Root: lists versions
dist/docs/v2/llms.txt                       # Version: lists variants
dist/docs/v2/{variant}/llms.txt             # Variant: page index with headings
dist/docs/v2/{variant}/llms-full.txt        # Full consolidated doc
dist/docs/v2/{variant}/**/<page>.md         # Per-page Markdown, section landings index their children
```

## How the page twins are generated

1. Hugo builds the site into `dist/` and also outputs a Markdown format into `tmp-md/`.
2. `process_shortcodes.py` reads from `tmp-md/`, resolves all shortcodes (variants, code includes, tabs, notes, etc.), and writes the result as the page's `.md` twin beside its rendered `index.html`.
3. `fix_internal_links_post_processing()` converts all internal links in the twins to point to other twins using relative paths.
4. `build_llm_docs.py` then enhances subpage listings with H2/H3 headings, converts all relative links to absolute URLs, and creates the `llms.txt` and `llms-full.txt` index files.


## The `llms-full.txt` link conversion

In `llms-full.txt`, all internal twin links are converted to hierarchical bold references:

* Cross-page: `[Resources](../resources.md)` becomes `**Configure tasks > Resources**`
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
