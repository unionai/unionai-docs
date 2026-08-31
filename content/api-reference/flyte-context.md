---
title: LLM-optimized documentation
description: LLM-optimized documentation for Union.ai and Flyte, provided at three levels of granularity and following the llms.txt convention so AI coding agents and search engines can consume the docs.
variants: +flyte +union
weight: 1
---

# LLM-optimized documentation

This site provides LLM-optimized documentation at three levels of granularity,
designed for use by AI coding agents such as
[Claude Code](https://docs.anthropic.com/en/docs/claude-code),
[Cursor](https://www.cursor.com/),
[Windsurf](https://windsurf.com/),
and similar tools.
These files also follow the [`llms.txt` convention](https://llmstxt.org/),
making them discoverable by AI search engines.

They are addressed by convention rather than linked from the pages they cover: append
`.md` to any page URL. Start from the `llms.txt` index below, which lists every page.

All links within LLM-optimized files use absolute URLs (`https://www.union.ai/docs/...`),
so files work correctly when copied locally and used outside the docs site.

## Per-page markdown (`<page>.md`)

Every page on this site has a parallel version in clean Markdown, served at the page's own
URL with `.md` appended. For example, this page is at:

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

and its Markdown version is at:

{{< variant union >}}
{{< markdown >}}
* [`{{< docs_home union v2 >}}/api-reference/flyte-context.md`](flyte-context.md)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v2 >}}/api-reference/flyte-context.md`](flyte-context.md)
{{< /markdown >}}
{{< /variant >}}

## Section indexes

A section landing page's Markdown carries a `## Subpages` block listing every page directly
beneath it. Each entry gives the page's title, its URL, a one-line description of what the
page is for, and that page's own H2 and H3 headings.

So a section landing page is the index for its section: fetch one file to see what the
section contains and what is inside each page, then fetch only the pages you need.

## Page index (`llms.txt`)

The `llms.txt` file is a compact index of every page on the site, organized by section.
Each entry includes the H2/H3 headings found on that page, so an agent can identify the
right page to fetch without downloading it first.

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

The `llms-full.txt` file contains the entire documentation set in a single file. It is
large, so prefer `llms.txt` plus the pages it points at unless you genuinely need
everything at once.

{{< variant union >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/union/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/flyte/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}
