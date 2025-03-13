<!-- omit from toc -->
# Special Blocks and Code Generators

This site has special blocks that can be used to generate code for Union.

- [How to specify a "short code"](#how-to-specify-a-short-code)
- [Variants](#variants)
- [Component Library](#component-library)
  - [`{{< audio >}}`](#-audio-)
  - [`{{< code >}}` (deprecated as we will inline all code)](#-code--deprecated-as-we-will-inline-all-code)
  - [`{{< grid >}}`](#-grid-)
  - [`{{< if-variant >}}`](#-if-variant-)
  - [`{{< link-card >}}`](#-link-card-)
  - [`{{< markdown >}}`](#-markdown-)
  - [`{{< multiline >}}`](#-multiline-)
  - [`{{< tabs >}}` and `{{< tab >}}`](#-tabs--and--tab-)
  - [`{{< var >}}`](#-var-)

## How to specify a "short code"

The short code is a string that is used to generate the code that is displayed.

You can specify parameteres, when applicable, or have content inside of it, if applicable.

> If you specify content, you have to have a close tag.

Examples:

    # A code that just output something

    {{< var product_name >}}

    # A code that has inside content

    {{< markdown >}}
    * You markdown
    * goes here
    {{< /markdown >}}

    # A code with parameters

    {{< link-card target="union-sdk" icon="workflow" title="Union SDK" >}}
    The Union SDK provides the Python API for building Union workflows and apps.
    {{< /link-card >}}

> If you're wondering why we have a `{{< markdown >}}` when we can generate markdown natively...
> it is because inside a container we need to specify what content we're rendering.

## Variants

The big difference of this site, compared to other documentation sites, is that
we generate multiple "flavors" of the documentation that are slightly different
from each other. We are calling these "variants."

When you are writing your content, and you want a specific part of the content
to be conditional to a flavor, say "BYOC", you surround that with `if-variant`.

> `if-variant` is a container, so inside you will specify what you are wrapping.
> You can wrap any of the shortcodes listed in this document.

Example:

    {{< if-variant serverless byoc >}}
        {{< markdown >}}
        **The quick brown fox signed up for Union!**
        {{< /markdown >}}

        {{< link-button text="Contact Us" target="https://union.ai/contact" >}}
    {{< /if-variant >}}

## Component Library

### `{{< audio >}}`

Generates an audio media player.

> TODO(peeter): document parameters

### `{{< code >}}` (deprecated as we will inline all code)

Includes source code from an external file.

> TODO(peeter): document parameters

### `{{< grid >}}`

Creates a fixed column grid for lining up content.

> TODO(peeter): document parameters

### `{{< if-variant >}}`

Filters content based on which flavor you're seeing.

> TODO(peeter): document parameters

### `{{< link-card >}}`

A floatable, clickable, navigatable card.

> TODO(peeter): document parameters


### `{{< markdown >}}`

Generates a markdown block, to be used inside containers such as `{{< dropdown >}}` or `{{< if-variant >}}`.

> TODO(peeter): document parameters

### `{{< multiline >}}`

Generates a multiple line, single paragraph. Useful for making a multiline table cell.

> TODO(peeter): document parameters

### `{{< tabs >}}` and `{{< tab >}}`

Generates a tab panel with content switching per tab.

> TODO(peeter): document parameters

### `{{< var >}}`

Prints one of the pre-defined product text, such as "Product Name". Used to not hardcode these across the page,
and allow changing them per-variant.

> `{{< var >}}` is variant sensitive, and it will change its content based on the current variant.

You can specify which value, per variant, in `hugo.toml`.

Example:

    [params.var.product_full]
    flyte = "Flyte"
    serverless = "Union Serverless"
    byoc = "Union BYOC"
    byok = "Union BYOK"

You can use it directly inside the code:

    The {{< var product_name >}} platform empowers AI development teams to rapidly ship high-quality