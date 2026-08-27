---
title: LLM-optimized documentation
description: LLM-optimized documentation for Union.ai and Flyte, provided at four levels of granularity and following the llms.txt convention so AI coding agents and search engines can consume the docs.
variants: +flyte +union
weight: 1
---

# LLM-optimized documentation

This site provides LLM-optimized documentation at four levels of granularity,
designed for use by AI coding agents such as
[Claude Code](https://docs.anthropic.com/en/docs/claude-code),
[Cursor](https://www.cursor.com/),
[Windsurf](https://windsurf.com/),
and similar tools.
These files also follow the [`llms.txt` convention](https://llmstxt.org/),
making them discoverable by AI search engines.

These files are not linked from the pages they cover. They are addressed by convention:
append `/page.md` to any page URL, or `/_section.md` to a section URL. Start from the
`llms.txt` index below, which lists every page and every available bundle.

All links within LLM-optimized files use absolute URLs (`https://www.union.ai/docs/...`),
so files work correctly when copied locally and used outside the docs site.

## Per-page markdown (`page.md`)

Every page on this site has a parallel LLM-optimized version in clean Markdown,
accessible at the same URL path with `/page.md` appended.
For example, this page is at:

{{< variant union >}}
{{< markdown >}}
* `{{< docs_home union v2 >}}/api-reference/flyte-context/`
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* `{{< docs_home flyte v2 >}}/api-reference/flyte-context/`
{{< /markdown >}}
{{< /variant >}}

and its LLM-optimized version is at:

{{< variant union >}}
{{< markdown >}}
* [`{{< docs_home union v2 >}}/api-reference/flyte-context/page.md`](page.md)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v2 >}}/api-reference/flyte-context/page.md`](page.md)
{{< /markdown >}}
{{< /variant >}}

Section landing pages include a `## Subpages` table listing child pages with their H2/H3 headings,
making it easy to identify the right page to fetch.

## Section bundles (`_section.md`)

Every section that holds more than its own landing page also has a bundle file, which
gathers one level of that section into a single `_section.md`. A section whose only page
is its landing page gets no bundle, because that content already lives at its own
`page.md` URL.

Bundles are addressed the same way `page.md` files are: append `/_section.md` to any
section URL. There is no list to consult, so a section added later is reachable by the
same rule, and `llms.txt` marks the sections that carry one.

A bundle holds the section's landing page and its own pages in full, then each immediate
sub-section. It is capped at 200 KB, so a large section is abridged to fit. A child is
abridged for one of two reasons, and the two mean different things:

* It has more beneath it, so its landing page stands in for its subtree and links onward
  to that sub-section's own `_section.md`.
* The bundle reached the size cap, so the child is cut to a short excerpt that links to
  its `page.md`.

Every bundle opens with a manifest naming which children were abridged and under which of
the two reasons, so you can tell whether what you are holding is the whole section and
fetch the rest when it is not.

## Page index (`llms.txt`)

The `llms.txt` file is a compact index of all LLM-optimized pages, organized by section.
Each page entry includes the H2/H3 headings found on that page, so an agent can identify
the right page to fetch without downloading it first.

Sections that have a `_section.md` bundle are marked in the index with a link to it.

Download it and append its contents to the `AGENTS.md`, `CLAUDE.md` or similar file in your project root.
Make sure you append the index into a file that is **loaded into context by default** by your coding tool.
Adding it as a skill or tool is less effective because the agent must decide to load it
rather than having the information always available.

{{< variant union >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/union/llms.txt) (~50K tokens)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/flyte/llms.txt) (~50K tokens)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms.txt` for a different product variant, use the variant selector at the top of the page.

## Full documentation (`llms-full.txt`)

The `llms-full.txt` file contains the entire {{< key product_name >}} version 2.0 documentation as a single Markdown file.
This file is very large and is not suitable for direct inclusion in an LLM context window,
but it may be useful for RAG-based tools.

{{< variant union >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/union/llms-full.txt) (~2M tokens)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/flyte/llms-full.txt) (~2M tokens)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms-full.txt` for a different product variant, use the variant selector at the top of the page.
