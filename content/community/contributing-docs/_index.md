---
title: Contributing docs and examples
weight: 3
variants: +flyte +union
llm_readable_bundle: true
---

# Contributing docs and examples

{{< llm-bundle-note >}}

We welcome contributions to the docs and examples for both Flyte and Union.
This section explains how the docs site works and walks you through setting it up, authoring content, and submitting your changes.

## Where to start

* [Set up a local docs dev environment](./quick-start): clone the repository, initialize the submodules, and run the live preview.
* [Author content](./authoring): write pages with Markdown, shortcodes, and variants.
* [Writing guidelines](./writing-guidelines): the editorial conventions the site follows.
* [Submit a contribution](./submitting-contributions): open a pull request and get it merged.

The rest of this section is reference material: [Variants](./variants), [Versions](./versions), [Shortcodes](./shortcodes), [API docs](./api-docs), [LLM-optimized documentation](./llm-docs), [Redirects](./redirects), and [Production builds and troubleshooting](./publishing).

## How the docs site works

As the primary maintainer and contributor of the open-source Flyte project, Union.ai hosts the Flyte documentation.
Union.ai is also the company behind the commercial Union.ai product, which is built on Flyte.

Because Flyte and Union.ai share much of their functionality, most of the documentation content is common between them.
There are, however, significant differences between Flyte and Union.ai and among the Union.ai deployment options (BYOC and Self-managed).

To maintain the documentation for all of these variants efficiently, we use a single-source-of-truth approach:

* All content is stored in a single GitHub repository, [`unionai/unionai-docs`](https://github.com/unionai/unionai-docs).
* All content is published on a single website, [`www.union.ai/docs`]({{< docs_home root v2 >}}).
* A variant selector at the top of each page lets you choose which variant to view: Flyte OSS or Union.ai (which covers both BYOC and Self-managed deployments).
* A version selector lets you choose between v1 (Flyte/Union 1.x) and v2 (Flyte/Union 2.0, which you are viewing now).

### Versions

The two versions of the docs are stored in separate branches of the repository:

* The [`v1` branch](https://github.com/unionai/unionai-docs/tree/v1) holds the v1 docs.
* The [`main` branch](https://github.com/unionai/unionai-docs) holds the v2 docs.

See [Versions](./versions) for details.

### Common build infrastructure

The build infrastructure (Hugo configuration, layouts, themes, build scripts, and Python tools) lives in a separate repository, [`unionai/unionai-docs-infra`](https://github.com/unionai/unionai-docs-infra), imported as a [Git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) at `unionai-docs-infra/`.

Both the `main` (v2) and `v1` content branches share this infrastructure.
Changes to the build system are made once in `unionai-docs-infra` and picked up by both branches, keeping them in sync without duplicating build logic.

### Variants

Within each branch, the variants are supported by conditional rendering:

* Each page declares which variants it applies to in its `variants` frontmatter field.
* Within a page, rendering logic includes or excludes content based on the selected variant.

The result is that content common to all variants is authored once, while variant-specific content is rendered conditionally.
See [Variants](./variants) for details.

### Both Flyte and Union docs are open source

Because the docs are combined in one repository and the Flyte docs are open source, the Union docs are open source too.
Everyone can contribute: Flyte contributors, Union customers, and Union employees.

If you are a Flyte contributor, you contribute docs related to Flyte features, and in many cases those features are also available in Union.
Because the docs site is a single source for all the documentation, when you make a change related to Flyte that is also valid for Union, you do it in the same place.
This is by design and is a key feature of the docs site.
