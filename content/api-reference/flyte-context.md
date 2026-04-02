---
title: LLM-optimized documentation
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

Every page on the site also has an **LLM-optimized** section in the right-hand sidebar
that points to:
* This "LLM-optimized documentation" page (for explanation).
* An LLM-optimized version of that page.
* An LLM-optimized single file containing the whole section (only on top pages of key sections).
* The full site index for LLMs.

All links within LLM-optimized files use absolute URLs (`https://www.union.ai/docs/...`),
so files work correctly when copied locally and used outside the docs site.

## Per-page Markdown (`page.md`)

Every page on this site has a parallel LLM-optimized version in clean Markdown,
accessible at the same URL path with `/page.md` appended and via the "**This page**" link in the "**LLM-optimized**" section of the right sidebar.
For example, this page is at:

{{< variant union >}}
{{< markdown >}}
* [`{{< docs_home union v2 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v2 >}}/api-reference/flyte-context/`](.)
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

## Section bundles (`section.md`)

For key documentation sections, a curated bundle file concatenates all pages in the section
into a single `section.md` file.

These are accessible at the same URL path as the top page of the section, with `/section.md` appended and via the "**This section in one file**" link in the "**LLM-optimized**" section of the right sidebar.

These `section.md` files are sized to fit within modern LLM context windows
and are ideal for pasting into a prompt or adding to project context.

Available bundle files:

{{< llm-readable-list >}}

## Page index (`llms.txt`)

The `llms.txt` file is a compact index of all LLM-optimized pages, organized by section.
Each page entry includes the H2/H3 headings found on that page, so an agent can identify
the right page to fetch without downloading it first.

Sections that have a `section.md` bundle are marked in the index.

Download it and append its contents to the `AGENTS.md`, `CLAUDE.md` or similar file in your project root.
Make sure you append the index into a file that is **loaded into context by default** by your coding tool.
Adding it as a skill or tool is less effective because the agent must decide to load it
rather than having the information always available.

{{< variant union >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/union/llms.txt) (~32K tokens)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/flyte/llms.txt) (~32K tokens)
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
* [`llms-full.txt`](https://www.union.ai/docs/v2/union/llms-full.txt) (~1.4M tokens)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/flyte/llms-full.txt) (~1.4M tokens)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms-full.txt` for a different product variant, use the variant selector at the top of the page.
