<!-- omit from toc -->
# Contributing content

**Table of contents**
- [Getting Started](#getting-started)
- [Pull Requests + Site Preview](#pull-requests--site-preview)
- [Live Preview](#live-preview)
- [Page Visibility](#page-visibility)
- [Page Order](#page-order)
- [Conditional Content](#conditional-content)
- [Special Content Generation](#special-content-generation)


## Getting started

Content is located in the [`content`](content/) folder.

To create a new page, simply create a new Markdown file in the appropriate folder and start writing it!


## Live preview

While editing, you can use Hugo's local live preview capabilities.
Simply execute

```
$ make dev
```

This will build the site and launch a local server at `http://localhost:1313`.
Go to that URL to the live preview.
As you edit the preview wull update

See [**Local Environment**](DEVELOPER.md) for more information.


## Pull Requests + Site Preview

Pull requests will create a preview build of the site on CloudFlare.
Check the pull request for a dynamic link to the site changes within that PR.


## Page Visibility

This site uses variants, which means different "flavors" of the content.
For a given -age, its variant visibility is governed by the `variants:` field in the front matter of the page source.
For each variant you specify `+<variant>` to include or `-<variant>` to exclude it.
For example:

```
---
title: My Page
variants: -flyte +serverless +byoc -byok
---
```

In this example the page will be:

* Included in Serverless and BYOC.
* Excluded from Flyte and BYOK.

> All variants must be explicitly listed in the `variants` field.
> This helps avoid missing or extraneous pages.

## Page order

Pages are ordered by the value of `weight` field (an integer >= 0) in the frontmatter of the page,

1. The higher the weight the lower the page sits in navigation ordering among its peers in the same folder.
2. Pages with no weight field (or `weight = 0`) will be ordered last.
3. Pages of the same weight will be sorted alphabetically by their title.
4. Folders are ordered among their peers (other folders and pages at the same level of the hierarchy) by the weight of their `_index.md` page.

For example:

---
title: My Page
weight: 3
---

## Conditional Content

The site has "flavors" of the documentation. We leverage the `{{< variant >}}` tag to control
which content is rendered on which flavor.

Refer to [**Variants**](SHORTCODES.md#variants) for detailed explanation.

## Special Content Generation

There are various short codes to generate content or special components (tabs, dropdowns, etc.)

Refer to [**Content Generation**](SHORTCODES.md) for more information.