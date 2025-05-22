---
title: Variants
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Variants

The docs site supports the ability to show or hide content based of the current variant selection.
There are separate mechanisms for:

* Including or excluding entire pages based on the selected variant.
* Conditional rendering of content within a page based on the selected variant using an if-then-like construct.
* Rendering keywords as variables that change based on the selected variant.

Currently, the docs site supports four variants:

- **Flyte**: The open-source Flyte project.
- **Serverless**: The Union.ai product that is hosted and managed by Union AI.
- **BYOC**: The Union.ai product that is hosted on the customer's infrastructure but managed by Union AI.
- **Self-managed**: The Union.ai product that is hosted and managed by the customer.

Each variant is referenced in the page logic using its respective code name: `flyte`, `serverless`, `byoc`, or `selfmanaged`.

The available set of variants are defined in the `config.<code_name>.toml` files in the root of the repository.

## Variants at the whole-page level

The docs site supports the ability to show or hide entire pages based of the selected variant.
Not all pages are available in all variants because features differ across the variants.

In the public website, if you are on page in one variant, and you change to a different variant, the page will change to the same page in the new variant *if it exists*.
If it does not exist, you will see a message indicating that the page is not available in the selected variant.

In the source Markdown, the presence or absence of a page in a given variant is governed by  `variants` field in the front matter parameter of the page.
For example, if you look at the Markdown source for [this page (the page you are currently viewing)](https://github.com/unionai/docs/content/community/contributing-docs.md), you will see the following front matter:

```markdown
---
title: Platform overview
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---
```

The `variants` field has the value:

`+flyte +serverless +byoc +selfmanaged`

The `+` indicates that the page is available for the specified variant.
In this case, the page is available for all four variants.
If you wanted to make the page available for only the `flyte` and `serverless` variants, you would change the `variants` field to:

`+flyte +serverless -byoc -selfmanaged`

In [live preview mode](./authoring-core-content#live-preview) with the `show_inactive` flag enabled, you will see all pages in the navigation tree, with the ones unavailable for the current variant grayed out.

As you can see, the `variants` field expects a space-separated list of keywords:

* The code names for the currently variants are, `flyte`, `serverless`, `byoc`, and `selfmanaged`.
* All supported variants must be included explicitly in every `variants` field with a leading `+` or `-`. There is no default behavior.
* The supported variants are configured in the root of the repository in the files named `config.<variant>.toml`.

## Conditional rendering within a page

Content can also differ *within a page* based on the selected variant.
This is done with conditional rendering using the `{{</* variant */>}}` and `{{</* key */>}}` [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/).

### {{</* variant */>}}

The syntax for the `{{</* variant */>}}` shortcode is:

```markdown
{{</* variant <variant_codes> */>}}
...
{{</* /variant */>}}
```

Where `<variant_codes>` is a list the code name for the variants you want to show the content for.

Note that the variant construct can only directly contain other shortcode constructs, not plain Markdown.
In the most common case, you will want to use the `{{</* markdown */>}}` shortcode  (which can contain Markdown) inside the `{{</* variant */>}}` shortcode to render Markdown content, like this:

```markdown
{{</* variant serverless byoc */>}}
{{</* markdown */>}}
This content is only visible in the `serverless` and `byoc` variants.
{{</* /markdown */>}}
{{</* button-link text="Contact Us" target="https://union.ai/contact" */>}}
{{</* /variant */>}}
```

For more details on the `{{</* variant */>}}` shortcode, see the [Shortcodes > `variant`](./shortcodes#variant).

### {{</* key */>}}

The syntax for the `{{</* key */>}}` shortcode is:

```markdown
{{</* key <key_name> */>}}
```

Where `<key_name>` is the name of the key you want to render.
For example, if you want to render the product name keyword, you would use:

```markdown
{{</* key product_name */>}}
```
The available key names are defined in the [params.key] section of the `hugo.site.toml` configuration file in the root of the repository.

For example the `product_name` used above is defined in that file as

```toml
[params.key.product_name]
flyte = "Flyte"
serverless = "Union.ai"
byoc = "Union.ai"
selfmanaged = "Union.ai"
```

Meaning that in any content that appears in the `flyte` variant of the site `{{</* key product_name */>}}` shortcode will be replaced with `Flyte`, and in any content that appears in the `serverless`, `byoc`, or `selfmanaged` variants, it will be replaced with `Union.ai`.


For more details on the `{{</* key */>}}` shortcode, see the [Shortcodes > `key`](./shortcodes#key)

## Full example

Here is full example. If you look at the Markdown source for [this page (the page you are currently viewing)](https://github.com/unionai/docs/content/community/contributing-docs/variants.md), you will see the following section:

```markdown
> **This text is visible in all variants.**
>
> {{</* variant flyte */>}}
> {{</* markdown */>}}
>
> **This text is only visible in the `flyte` variant.**
>
> {{</* /markdown */>}}
> {{</* /variant */>}}
> {{</* variant serverless byoc selfmanaged */>}}
> {{</* markdown */>}}
>
> **This text is only visible in the `serverless`, `byoc`, and `selfmanaged` variants.**
>
> {{</* /markdown */>}}
> {{</* /variant */>}}
>
> **Below is a `{{</* key product_full_name */>}}` shortcode.
> It will be replaced with the current variant's full name:**
>
> **{{</* key product_full_name */>}}**
```

This Markdown source is rendered as:

> **This text is visible in all variants.**
>
> {{< variant flyte >}}
> {{< markdown >}}
>
> **This text is only visible in the `flyte` variant.**
>
> {{< /markdown >}}
> {{< /variant >}}
> {{< variant serverless byoc selfmanaged>}}
> {{< markdown >}}
>
> **This text is only visible in the `serverless`, `byoc`, and `selfmanaged` variants.**
>
> {{< /markdown >}}
> {{< /variant >}}
>
> **Below is a `{{</* key product_full_name */>}}` shortcode.
> It will be replaced with the current variant's full name:**
>
> **{{< key product_full_name >}}**

If you switch between variants with the variant selector at the top of the page, you will see the content change accordingly.

## Adding a new variant

A variant is a term we use to identify a product or major section of the site.
Such variant has a dedicated token that identifies it, and all resources are
tagged to be either included or excluded when the variant is built.

> Adding new variants is a rare event and must be reserved when new products
> or major developments.
>
> If you are thinking adding a new variant is the way
> to go, please double-check with the infra admin to confirm before doing all
> the work below and waste your time.

### Location

When deploying, the variant takes a folder in the root

`https://<your-site-domain>/<variant>/<content>`

For example, if we have a variant `acme`, then when built the content goes to:

`https://<your-site-domain>/acme/<content>`

### Creating a new variant

To create a new variant a few steps are required:

| File                    | Changes                                                        |
| ----------------------- | -------------------------------------------------------------- |
| `hugo.site.toml`        | Add to `params.variant_weights` and all `params.key`           |
| `hugo.toml`             | Add to `params.search`                                         |
| `Makefile`              | Add a new `make variant` to `dist` target                      |
| `<content>.md`          | Add either `+<variant>` or `-<variant>` to all content pages   |
| `config.<variant>.toml` | Create a new file and configure `baseURL` and `params.variant` |

### Testing the new variant

As you develop the new variant, it is recommended to have a `pre-release/<variant>` semi-stable
branch to confirm everything is working and the content looks good. It will also allow others
to collaborate by creating PRs against it (`base=pre-release/<variant>` instead of `main`)
without trampling on each other and allowing for parallel reviews.

Once the variant branch is correct, you merge that branch into main.

### Building (just) the variant

You can build the production version of the variant,
which will also trigger all the safety checks as well,
by invoking the variant build:

```shell
$ make variant VARIANT=<variant>
```

For example:

```shell
make variant VARIANT=serverless
```
