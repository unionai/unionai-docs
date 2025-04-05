<!-- omit from toc -->
# Contributing content

**Table of contents**
- [Getting started](#getting-started)
- [Live preview](#live-preview)
- [Pull Requests + Site Preview](#pull-requests--site-preview)
- [Page Visibility](#page-visibility)
- [Page order](#page-order)
- [Page settings](#page-settings)
- [Conditional Content](#conditional-content)
- [Warnings and Notices](#warnings-and-notices)
- [Special Content Generation](#special-content-generation)
- [Python Generated Content](#python-generated-content)
  - [Run on Union Instructions](#run-on-union-instructions)
- [Mermaid Graphs](#mermaid-graphs)
- [Mapped Keys (`{{< key >}}`)](#mapped-keys--key-)


## Getting started

Content is located in the [`content`](content/) folder.

To create a new page, simply create a new Markdown file in the appropriate folder and start writing it!


## Live preview

While editing, you can use Hugo's local live preview capabilities.
Simply execute

    $ make dev

This will build the site and launch a local server at `http://localhost:1313`.
Go to that URL to the live preview. Leave the server running.
As you edit the preview will update automatically.

See [**Local Environment**](DEVELOPER.md) for how to setup your machine.


## Pull Requests + Site Preview

Pull requests will create a preview build of the site on CloudFlare.
Check the pull request for a dynamic link to the site changes within that PR.


## Page Visibility

This site uses variants, which means different "flavors" of the content.
For a given -age, its variant visibility is governed by the `variants:` field in the front matter of the page source.
For each variant you specify `+<variant>` to include or `-<variant>` to exclude it.
For example:

    ---
    title: My Page
    variants: -flyte +serverless +byoc -byok
    ---

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

## Page settings

| Setting            | Type | Description                                                                       |
| ------------------ | ---- | --------------------------------------------------------------------------------- |
| `top_menu`         | bool | If `true` the item becomes a tab at the top and its hierarchy goes to the sidebar |
| `sidebar_expanded` | bool | If `true` the section becomes expanded in the side bar. Permanently.              |
| `site_root`        | bool | If `true` indicates that the page is the site landing page                        |
| `toc_max`          | int  | Maximum heading to incorporate in the right navigation table of contents.         |

## Conditional Content

The site has "flavors" of the documentation. We leverage the `{{< variant >}}` tag to control
which content is rendered on which flavor.

Refer to [**Variants**](SHORTCODES.md#variants) for detailed explanation.

## Warnings and Notices

You can write regular markdown and use the notation below to create information and warning boxes:

    > [!NOTE] This is the note title
    > You write the note content here. It can be
    > anything you want.

Or if you want a warning:

    > [!WARNING] This is the title of the warning
    > And here you write what you want to warn about.

## Special Content Generation

There are various short codes to generate content or special components (tabs, dropdowns, etc.)

Refer to [**Content Generation**](SHORTCODES.md) for more information.

## Python Generated Content

You can generate pages from Python markdown-decorated files.

Declaring the file: At the top of your .md file, add:

    ---
    layout: py_example
    example_file: /path/to/your/file.py
    ---

A file like this:

    # # Credit Default Prediction with XGBoost & NVIDIA RAPIDS
    #
    # In this tutorial, we will use NVIDIA RAPIDS `cudf` DataFrame library for preprocessing
    # data and XGBoost, an optimized gradient boosting library, for credit default prediction.
    # We'll learn how to declare NVIDIA  `A100` for our training function and `ImageSpec`
    # for specifying our python dependencies.

    # {{run-on-union}}

    # ## Declaring workflow dependencies
    #
    # First, we start by importing all the dependencies that is required by this workflow:

    import os
    import gc
    from pathlib import Path
    from typing import Tuple

    import fsspec
    from flytekit import task, workflow, current_context, Resources, ImageSpec, Deck
    from flytekit.types.file import FlyteFile
    from flytekit.extras.accelerators import A100

Note that all markdown are as comments, and code blocks are as normal python code.

The generator will convert the markdown into a page and the code into blocks.

### Run on Union Instructions

We can add the run on Union instructions anywhere in the content.
Annotate the location you want to include it with `{{run-on-union}}`. Like this:

    # The quick brown fox wants to see the Union instructions.
    #
    # {{run-on-union}}
    #
    # And it shall have it.

## Mapped Keys (`{{< key >}}`)

Key is a very special command that allows us to define mapped values to a variant.
For example, the product name changes if it is Flyte, Union BYOC, etc. For that,
we can define a single key `product_full_name` and map it to reflect automatically,
without the need to `if variant` around it.

Please refer to [{{< key >}} shortcode](SHORTCODES.md#-key-) for more details.
## Mermaid Graphs

To embed Mermaid diagrams in a page, insert the code inside a block like this:

    ```mermaid
    your mermaid graph goes here
    ```

Also add `mermaid: true` to the top of your page to enable rendering.

> You can use [Mermaid's playground](https://www.mermaidchart.com/play) to design diagrams and get the code 
