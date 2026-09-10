---
title: LLM-optimized documentation
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

These files are not linked from the pages they cover. They are addressed by convention:
append `.md` to any page URL. Start from the `llms.txt` index below, which lists every page.

> [!NOTE] One shape: `<path>.md`
> The older names `page.md`, `section.md` and `_section.md` are **retired and no longer
> generated**. All three now redirect to the page's Markdown version. If you have an older
> note or script that appends `/page.md`, update it to append `.md` to the page URL instead.

All links within LLM-optimized files use absolute URLs (`https://www.union.ai/docs/...`),
so files work correctly when copied locally and used outside the docs site.

## Per-page Markdown (`<path>.md`)

Every page on this site has a parallel LLM-optimized version in clean Markdown,
accessible at the page's own URL with `.md` appended. Note that the file sits *beside* the
page's directory rather than inside it. For example, this page is at:

{{< variant union >}}
{{< markdown >}}
* [`{{< docs_home union v1 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v1 >}}/api-reference/flyte-context/`](.)
{{< /markdown >}}
{{< /variant >}}

and its LLM-optimized version is at:

{{< variant union >}}
{{< markdown >}}
* [`{{< docs_home union v1 >}}/api-reference/flyte-context.md`](../flyte-context.md)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`{{< docs_home flyte v1 >}}/api-reference/flyte-context.md`](../flyte-context.md)
{{< /markdown >}}
{{< /variant >}}

A section landing page's Markdown ends with a `## Subpages` list of every page directly beneath
it, with each child's URL, description and its own H2/H3 headings. One fetch therefore tells an
agent what the section contains and which page to read next.

Two more details worth knowing:

* Each Markdown file opens with a short identity block naming the product and the version line,
  so a model knows what it is reading when handed the file with no other context.
* The variant root has no Markdown version of its own. Appending `.md` there redirects to that
  variant's `llms.txt`, which indexes the whole tree.

You can also request Markdown at the page's own URL by sending an `Accept: text/markdown` header:

```shell
$ curl -H "Accept: text/markdown" {{< docs_home union v1 >}}/user-guide/
```

## Page index (`llms.txt`)

The `llms.txt` file is a compact index of all LLM-optimized pages, organized by section.
Each page entry includes the H2/H3 headings found on that page, so an agent can identify
the right page to fetch without downloading it first.

Download it and append its contents to the `AGENTS.md`, `CLAUDE.md` or similar file in your project root.
Make sure you append the index into a file that is **loaded into context by default** by your coding tool.
Adding it as a skill or tool is less effective because the agent must decide to load it
rather than having the information always available.

{{< variant union >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v1/union/llms.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v1/flyte/llms.txt)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms.txt` for a different product variant, use the variant selector at the top of the page.

## Full documentation (`llms-full.txt`)

The `llms-full.txt` file contains the entire {{< key product_name >}} version 1.0 documentation as a single Markdown file.
This file is very large and is not suitable for direct inclusion in an LLM context window,
but it may be useful for RAG-based tools.

{{< variant union >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v1/union/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms-full.txt`](https://www.union.ai/docs/v1/flyte/llms-full.txt)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms-full.txt` for a different product variant, use the variant selector at the top of the page.
