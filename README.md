# Union.ai Docs Builder

## Requirements

- Hugo (https://gohugo.io/)

      MacOS$ brew install hugo

## Running Locally

    make dev

This will launch the site in development mode. The changes are hot reloaded: just change in your favorite editor and it will refresh immediately on the browser.

### Changing 'variants'

Variants are flavors of the site (that you can change at the top). During
development, you can render any variant by setting them in `hugo.local.toml`:

    variant = "byoc"

> You can copy it from `hugo.local.toml~sample` to get started.

Also note that you can render multiple variant content at the same time. You can
customize them by setting these in `hugo.local.toml`:

    # Shows variants that do not match
    variant_hide_in_development = false

    # Shows all variants at once (green = matches, red = not)
    variant_identify_variant_in_development = true

### Identifying Problems: Missing Content

Content may be hidden due to `if variant { ... }` blocks. To see what's missing,
you can adjust the variant show/hide in development mode.

For a production-like look set:

    variant_hide_in_development = true
    variant_identify_variant_in_development = false

For a full-developer experience, set:

    variant_hide_in_development = false
    variant_identify_variant_in_development = true

### Identifying Problems

The developer site will show you in red any pages missing from the variant. For a page to exist in the variant, it must be listed in the `allowed_pages.yaml` file. Clicking on the red page will give you the path you must add to the appropriate variant in the YAML file.

## Building Production

    make

This will create all the variants into the `dist` folder.
