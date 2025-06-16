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

* All content is stored in a single GitHub repository, [`unionai/docs`](https://github.com/unionai/docs)
* All content is published on a single website, [`www.union.ai/docs`](https://www.union.ai/docs)
* The website has a variant selector at the top of the page that lets you choose which variant you want to view.

Multiple variants of the documentation are supported as follows:

* There are currently four product variants: Flyte, Serverless, BYOC, and Self-managed.
* Content that is common to all variants is authored and stored once. There is no need to keep multiple copies of the same content in-sync.
* Content specific to a variant is conditionally rendered based on the selected variant.

And finally:

* Different version of the documentation are also supported, independently of the variants.

For details on how this works, see [Variants](./variants.md) and [Versions](./versions.md).

## Both Flyte and Union docs are open source

Since the docs are now combined in one repository, and the Flyte docs are open source, the Union docs are also open source.
All the docs are available for anyone to contribute to: Flyte contributors, Union customers, and Union employees.

If you are a Flyte contributor, you will be contributing docs related to Flyte features and functionality, but in many cases these features and functionality will also be available in Union.
Because the docs site is a single source for all the documentation, when you make changes related to Flyte that are also valid for Union you do so in the same place.
This is by design and is a key feature of the docs site.
