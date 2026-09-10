---
paths:
  - "tools/algolia_indexer/**"
  - "unionai-docs-infra/tools/algolia_indexer/**"
  - "layouts/partials/search.html"
  - "unionai-docs-infra/layouts/partials/search.html"
  - "SITEMAPS-AND-SEARCH.md"
  - "unionai-docs-infra/SITEMAPS-AND-SEARCH.md"
---

# On-site search and Ask AI

`tools/algolia_indexer/README.md` is the authority. Read it rather than recalling; index names
and shapes have changed before and the docs lagged.

## Two indexes, one application

| Index | Built by | Consumer | Chunking |
|---|---|---|---|
| `union` | `build_records.py` | keyword site search | per heading anchor |
| `union-markdown` | `build_markdown_records.py` | the Ask AI agent | per page |

Both cover **every** version and variant. Neither is restricted to a line at build time —
scoping happens at query time from the URL's version/variant segments.

## Two traps

- **`nbHits` means different things.** `union` sets `distinct` on `url_without_anchor`, so it
  counts **pages**. `union-markdown` sets no `attributeForDistinct`, so it counts **records**.
- **Check which Algolia application you are querying.** A retired crawler wrote to a different
  app whose stale answers look identical to live ones. The live app ID is in the page's
  `window.__SEARCH_CONFIG` — read it there rather than trusting a copy.

## No crawler

The indexes are built from `dist/` at deploy time and pushed by `make index-search`. There is no
seed list, no `startUrls`, no `exclusionPatterns`. Served implies searchable, and `noindex` (a
Google signal) is independent of site-search membership.
