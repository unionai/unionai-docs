---
title: Writing guidelines
weight: 4
variants: +flyte +union
---

# Writing guidelines

These guidelines describe the editorial conventions the docs follow.
Following them keeps your contribution consistent with the rest of the site.
They cover *how to write* the content; for the mechanics of authoring pages (frontmatter, shortcodes, variants), see [Author content](./authoring).

## Lead with the task

Start a page or section with what the reader needs to do, not with background.
State the goal, then show the shortest example that achieves it, then explain the details.
Move context, caveats, and edge cases below the first working example.

## Write in a clear, active voice

* Use the active voice ("Call `flyte.init()` before submitting a run"), not the passive ("`flyte.init()` should be called").
* Address the reader as "you".
* Keep sentences short and concrete. Prefer plain verbs (`use`, not `leverage` or `utilize`).
* Cut filler. Phrases like "it is worth noting that", "in order to", and "a wide range of" add words without adding meaning.

## Structure a page

A typical page follows this shape:

1. A brief description of what the feature does.
2. A minimal, runnable example early on.
3. The parameters and options, explained after the example.
4. Common use cases and gotchas at the end.

Use headings to break up the page, and keep each section focused on one idea.

## Use sentence case for headings

Write headings and titles in sentence case: capitalize only the first word and any proper nouns.

* Write "Set up a local dev environment", not "Set Up A Local Dev Environment".
* Keep product names and acronyms capitalized as they normally appear: Flyte, Union.ai, Kubernetes, API, SDK, CLI.

## Use notes and warnings deliberately

Use a note for helpful, non-critical information and a warning for something that can cause data loss, breakage, or a security problem. Do not overuse them; if every paragraph is a callout, none of them stand out.

```markdown
> [!NOTE] Optional title
> Helpful, non-critical information.

> [!WARNING] Optional title
> Something the reader must not miss.
```

See [Authoring > Warnings and notices](./authoring#warnings-and-notices) for the syntax.

## Keep terminology consistent

Use the same term for the same thing throughout. Match the spelling and casing the rest of the docs use:

* **Union.ai** for the company and product (not "Union AI" or "UnionAI").
* **Flyte** for the open-source project (lowercase `flyte` only for the package, CLI, or module name, in code).
* **Kubernetes**, not "k8s", in prose.

When you write about a Flyte 2 concept as an ordinary noun ("create a task", "the workflow"), use lowercase.
Capitalize the name only when you mean the literal API class, and then write it in backticks so it links to the API reference: `` `Task` ``, `` `TaskEnvironment` ``, `` `File` ``.

## Make examples runnable and tested

Code examples should run as written. Prefer examples that a reader can copy, paste, and execute.
Longer, runnable examples belong in the [`unionai/unionai-examples`](https://github.com/unionai/unionai-examples) repository and are embedded into pages; see [Author content](./authoring#python-generated-content) for how that works.

## Link to the API reference by writing the identifier

When you mention an API identifier in prose or a code block, write it in backticks and let the site link it automatically. Do not write an explicit Markdown link to the API reference.

```markdown
✅  A `flyte.io.File` is a reference to an offloaded file.
✅  Call `flyte.init()` before submitting a run.
```

See [Authoring > Linking to the API reference](./authoring#linking-to-the-api-reference) for the details.
