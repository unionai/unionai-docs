---
title: Contributing docs and examples
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Contributing docs and examples

We welcome contributions to the docs and examples for both Flyte and Union.
This section will explain how the docs site works, how to author and build it locally, and how to publish your changes.

## The combined Flyte and Union docs site

As the primary maintainer and contributor of the open-source Flyte project, Union AI is responsible for hosting the Flyte documentation.

Additionally, Union AI is also the company behind the commercial Union.ai product, which is based on Flyte.

Since Flyte and Union.ai share a lot of common functionality, much of the documentation content is common between the two.
However, there are some significant differences between not only Flyte and Union.ai but also among the different Union.ai product offering (Serverless, BYOC, and Self-managed).

To effectively and efficiently maintain the documentation for all of these variants, we employ a single-source-of-truth approach where:

* All content is stored in a single GitHub repository, [`unionai/unionai-docs`](https://github.com/unionai/unionai-docs)
* All content is published on a single website, [`www.union.ai/docs`]({{< docs_home root v2 >}}).
* The website has a variant selector at the top of the page that lets you choose which variant you want to view:
    * Flyte OSS
    * Union Serverless
    * Union BYOC
    * Union Self-managed
* There is also version selector. Currently two versions are available:
    * v1 (the original docs for Flyte/Union 1.x)
    * v2 (the new docs for Flyte/Union 2.0, which is the one you are currently viewing)

## Versions

The two versions of the docs are stored in separate branches of the GitHub repository:

* [`v1` branch](https://github.com/unionai/unionai-docs/tree/v1) for the v1 docs.
* [`main` branch](https://github.com/unionai/unionai-docs) for the v2 docs.

See [Versions](./versions) for more details.

## Variants

Within each branch the multiple variants are supported by using conditional rendering:

* Each page of content has a `variants` front matter field that specifies which variants the page is applicable to.
* Within each page, rendering logic can be used to include or exclude content based on the selected variant.

The result is that:
* Content that is common to all variants is authored and stored once.
  There is no need to keep multiple copies of the same content in-sync.
* Content specific to a variant is conditionally rendered based on the selected variant.

See [Variants](./variants) for more details.

## Both Flyte and Union docs are open source

Since the docs are now combined in one repository, and the Flyte docs are open source, the Union docs are also open source.
All the docs are available for anyone to contribute to: Flyte contributors, Union customers, and Union employees.

If you are a Flyte contributor, you will be contributing docs related to Flyte features and functionality, but in many cases these features and functionality will also be available in Union.
Because the docs site is a single source for all the documentation, when you make changes related to Flyte that are also valid for Union you do so in the same place.
This is by design and is a key feature of the docs site.
