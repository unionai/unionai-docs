---
paths:
  - "tools/llms_generator/**"
  - "unionai-docs-infra/tools/llms_generator/**"
  - "content/community/contributing-docs/llm-docs.md"
  - "content/api-reference/flyte-context.md"
  - "layouts/_default/single.md"
  - "layouts/_default/list.md"
  - "unionai-docs-infra/layouts/_default/single.md"
  - "unionai-docs-infra/layouts/_default/list.md"
---

# The agent-facing markdown surface

Every page is published twice: as HTML, and as a clean markdown **twin** at the page's own URL
with `.md` appended. Plus `llms.txt` (page index with headings) and `llms-full.txt` per variant.

The twin for the page at `<path>/` is the file **`<path>.md`** — *beside* that page's directory,
not inside it. A variant root has no twin; appending `.md` there redirects to that tree's
`llms.txt`.

## One shape only

**`page.md`, `section.md` and `_section.md` are retired and no longer generated.** All three 301
to the page twin, or to the tree's `llms.txt` at a variant root. Do not reintroduce them and do
not describe them as current. Stale code comments still mention them; they describe nothing the
build does.

## Two properties worth preserving

- Every twin opens with an **identity block** naming the product, version line and index URL, so
  a model handed one file in isolation knows what it is reading.
- A section landing twin ends with a **`## Subpages`** list giving each child's title, URL,
  description and headings — one fetch tells an agent what a section holds and what to read next.

## Shortcodes must resolve cleanly to markdown

`process_shortcodes.py` resolves every shortcode when generating twins. A shortcode that renders
correctly in HTML but resolves badly to markdown **degrades the agent surface without touching
the visible site**, so nothing on the page will look wrong.

Readers can also request markdown at the ordinary URL with `Accept: text/markdown` (a Cloudflare
transform rule, so the browser URL does not change). Keep `api-reference/flyte-context.md` — the
reader-facing description — consistent with any pipeline change.
