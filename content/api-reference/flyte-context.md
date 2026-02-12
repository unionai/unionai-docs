---
title: AI coding agent support
variants: +flyte +byoc +selfmanaged +serverless
weight: 1
---

# AI coding agent support

## Clean Markdown

Every page on this site has a parallel LLM-readable version in clean Markdown,
accessible at the same URL path with `/content.md` appended.
For example, this page is at:

{{< variant byoc >}}
{{< markdown >}}
* [`{{< docs_home byoc v2 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v2 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}
* [`{{< docs_home selfmanaged v2 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

and its LLM-readable version is at:

{{< variant byoc >}}
{{< markdown >}}
* [`{{< docs_home byoc v2 >}}/api-reference/flyte-context/content.md`](content.md)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v2 >}}/api-reference/flyte-context/content.md`](content.md)
{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}
* [`{{< docs_home selfmanaged v2 >}}/api-reference/flyte-context/content.md`](content.md)
{{< /markdown >}}
{{< /variant >}}

These pages are designed to be consumed by AI coding agents such as
[Claude Code](https://docs.anthropic.com/en/docs/claude-code),
[Cursor](https://www.cursor.com/),
[Windsurf](https://windsurf.com/),
and similar tools.

## Page index (`llms.txt`)

The `llms.txt` file is a compact index of all of these LLM-readable pages.
Adding this index into the context of your coding tool gives it direct access to these docs.

Download it and append its contents to the `AGENTS.md`, `CLAUDE.md` or similar file in your project root.
Make sure you append the index into a file that is **loaded into context by default** by your coding tool.
Adding it as a skill or tool is less effective because the agent must decide to load it
rather than having the information always available.


{{< variant byoc >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/byoc/llms.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/flyte/llms.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/selfmanaged/llms.txt)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms.txt` for a different product variant, use the variant selector at the top of the page.

## Full documentation (`llms-full.txt`)

The `llms-full.txt` file contains the entire {{< key product_name >}} version 2.0 documentation as a single Markdown file.
This file is very large and is not suitable for direct inclusion in an LLM context window,
but it may be useful for RAG-based tools.

{{< variant byoc >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/byoc/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/flyte/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant selfmanaged >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v2/selfmanaged/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms-full.txt` for a different product variant, use the variant selector at the top of the page.
