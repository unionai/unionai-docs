---
title: LLM-optimized documentation
description: How AI agents and coding tools read these docs as Markdown. Append .md to any page URL for that page, use llms.txt as the index of every page, or take the whole site as llms-full.txt. Every page also has a menu that opens it in Claude or ChatGPT.
variants: +flyte +union
weight: 8
---

# LLM-optimized documentation

Every page on this site is also available as clean Markdown, and the whole site is indexed
for AI coding agents such as
[Claude Code](https://docs.anthropic.com/en/docs/claude-code),
[Cursor](https://www.cursor.com/), and
[Windsurf](https://windsurf.com/).
The files follow the [`llms.txt` convention](https://llmstxt.org/), so AI search engines find
them too.

There are three levels of granularity:

| What you get | Where | Use it when |
|---|---|---|
| One page as Markdown | append `.md` to the page URL | an agent needs one page |
| An index of every page | `llms.txt` | an agent needs to find the right page first |
| The entire site in one file | `llms-full.txt` | you need everything at once |

## Open a page in Claude or ChatGPT

Every page has a menu at the top right, on the breadcrumb row. **Open in Claude** hands the
page's Markdown URL to Claude with a prompt asking it to read the page so you can ask questions
about it. The dropdown beside it offers:

* **Open in Claude** and **Open in ChatGPT**: the same action, for either assistant.
* **Copy page**: copies the page's Markdown text to your clipboard, for pasting into a tool
  that cannot fetch URLs.
* **View as Markdown**: opens the page's Markdown version in the browser.

## One page as Markdown

Append `.md` to any page URL. For example, this page is at:

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

The same rule applies to section landing pages: `.../user-guide/tasks/` becomes
`.../user-guide/tasks.md`. A section landing page's Markdown ends with a **Subpages** list of
every page directly beneath it, with each page's URL and headings, so one fetch tells an agent
what the section contains and which page to read next.

Two details worth knowing:

* Each Markdown file starts with a short identity block naming the product, the version line,
  and the index URL, so a model knows what it is reading even when it is handed the file with
  no other context.
* The variant root has no Markdown version of its own. Appending `.md` to the root URL
  redirects to that variant's `llms.txt`, which is the index for the whole tree.

You can also request Markdown at the page's own URL by sending an `Accept: text/markdown`
header:

{{< variant union >}}
{{< markdown >}}
```shell
$ curl -H "Accept: text/markdown" {{< docs_home union v2 >}}/user-guide/tasks/
```
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
```shell
$ curl -H "Accept: text/markdown" {{< docs_home flyte v2 >}}/user-guide/tasks/
```
{{< /markdown >}}
{{< /variant >}}

All links inside the Markdown files are absolute (`https://www.union.ai/docs/...`), so a file
keeps working after it is copied out of the site.

## An index of every page (`llms.txt`)

`llms.txt` lists every page on the site, grouped by section, with the H2 and H3 headings found
on each page. An agent can pick the right page from the index and then fetch only that page's
Markdown.

To give a coding agent standing access to the docs, download `llms.txt` and append its
contents to the `AGENTS.md`, `CLAUDE.md`, or equivalent file in your project root. Put it in a
file the tool **loads into context by default**. Adding it as a skill or tool works less well,
because the agent then has to decide to load it rather than always having it available.

{{< variant union >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/union/llms.txt) (about 50K tokens)
{{< /markdown >}}
{{< /variant >}}

{{< variant flyte >}}
{{< markdown >}}
* [`llms.txt`](https://www.union.ai/docs/v2/flyte/llms.txt) (about 40K tokens)
{{< /markdown >}}
{{< /variant >}}

> [!NOTE]
> You are viewing the **{{< key product_full_name >}}** docs.
> To get the `llms.txt` for a different product variant, use the variant selector at the top of the page.

## The entire site in one file (`llms-full.txt`)

`llms-full.txt` is the whole documentation set in a single file. It is several megabytes, so
prefer `llms.txt` plus the pages it points to unless you need everything at once.

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
