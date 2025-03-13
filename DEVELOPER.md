<!-- omit from toc -->
# Local Environment & Developer

You can run the full environment locally and have live preview and other niceties.

- [Requirements](#requirements)
- [Running Locally](#running-locally)
  - [Changing 'variants'](#changing-variants)
  - [Identifying Problems: Missing Content](#identifying-problems-missing-content)
  - [Identifying Problems: Page Visibility](#identifying-problems-page-visibility)
- [Building Production](#building-production)
  - [Testing Production Build](#testing-production-build)

## Requirements

- Hugo (https://gohugo.io/)

      MacOS$ brew install hugo

## Running Locally

    make dev

This will launch the site in development mode.
The changes are hot reloaded: just change in your favorite editor and it will refresh immediately on the browser.

### Changing 'variants'

Variants are flavors of the site (that you can change at the top).
During development, you can render any variant by setting them in `hugo.local.toml`:

    variant = "byoc"

> You can copy it from `hugo.local.toml~sample` to get started.

Also note that you can render multiple variant content at the same time. You can
customize them by setting these in `hugo.local.toml`:

    # Shows variants that do not match
    variant_hide_in_development = false

    # Shows all variants at once (green = matches, red = not)
    variant_identify_variant_in_development = true

### Identifying Problems: Missing Content

Content may be hidden due to `{{< if-variant ... >}}` blocks. To see what's missing,
you can adjust the variant show/hide in development mode.

For a production-like look set:

    variant_hide_in_development = true
    variant_identify_variant_in_development = false

For a full-developer experience, set:

    variant_hide_in_development = false
    variant_identify_variant_in_development = true

### Identifying Problems: Page Visibility

The developer site will show you in red any pages missing from the variant.
For a page to exist in the variant (or be excluded, you have to pick one), it must be listed in the `variants:` at the top of the file.
Clicking on the red page will give you the path you must add to the appropriate variant in the YAML file and a link with guidance.

Please refer to [Authoring Content](AUTHOR.md) for more details.

## Building Production

    make dist

### Testing Production Build

You can run a local webserver and serve the `dist/` folder. The site must behave correctly, as it would be in its official URL.

To start a server:

    make serve PORT=<nnnnn>

Example:

    make server PORT=4444

Then you open the browser on `http://localhost:<port>` to see the content. In the example above, it would be `http://localhost:4444/`


This will create all the variants into the `dist` folder.
