<!-- omit from toc -->
# Contributing Content

**Table Of Contents**
- [Getting Started](#getting-started)
- [Pull Requests + Site Preview](#pull-requests--site-preview)
- [Live Preview](#live-preview)
- [Page Visibility](#page-visibility)
- [Page Order](#page-order)
- [Conditional Content](#conditional-content)
- [Special Content Generation](#special-content-generation)

## Getting Started

Content is located in the [`content`](content/) folder.

To create a new page, simply create a new Markdown file in the appropriate folder and start writing it!

## Pull Requests + Site Preview

Pull requests will create a live preview of the site.
Please check the pull request for a dynamic link to the site changes within that PR.

## Live Preview

This site has live preview capabilities.

Please refer to [**Local Environment**](DEVELOPER.md) for more information.

## Page Visibility

This site uses variants, which means different "flavors" of the content.
For each variant you specify `+<variant>` to include or `-<variant>` to exclude it.

Example:

    ---
    title: My Page
    variants: -flyte +serverless +byoc -byok
    ---

In this example the page will be:

* Included: in Serverless and BYOC
* Excluded: in Flyte and BYOK

> All variants must be included, so the site builder knows what to do with it.
> We will assume neither always included nor always excluded to avoid extraneous
> or missing pages.

## Page Order

Pages are ordered by their `weight`, following these rules:

1. Higher weight sinks to the bottom (shows at the end)
2. Pages with no weight (or weight = 0) will ordered last
3. Pages of the same weight will be sorted alphabetically by its title

Example:

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