---
title: Publishing
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# Publishing

## Requirements

1. Hugo (https://gohugo.io/)

```shell
$ brew install hugo
```

2. A preferences override file with your configuration

The tool is flexible and has multiple knobs. Please review `hugo.local.toml~sample`, and configure to meet your preferences.

```shell
$ cp hugo.local.toml~sample hugo.local.toml
```

3. Make sure you review `hugo.local.toml`.

## Managing the Tutorial Pages

The tutorials are maintained in the [unionai/unionai-examples](https://github.com/unionai/unionai-examples) repository and is imported as a git submodule in the `external`
directory.

To initialize the submodule on a fresh clone of this (`docs-builder`) repo, run:

```
$ make init-examples
```

To update the submodule to the latest `main` branch, run:

```
$ make update-examples
```

## Building and running locally

```
$ make dev
```

## Building Production

```
$ make dist
```

### Testing Production Build

You can run a local web server and serve the `dist/` folder. The site must behave correctly, as it would be in its official URL.

To start a server:

```
$ make serve PORT=<nnnnn>
```

Example:

```
$ make server PORT=4444
```

Then you open the browser on `http://localhost:<port>` to see the content. In the example above, it would be `http://localhost:4444/`


This will create all the variants into the `dist` folder.

## Developer Experience

This will launch the site in development mode.
The changes are hot reloaded: just change in your favorite editor and it will refresh immediately on the browser.

### Controlling Development Environment

You can change how the development environment works by settings values in `hugo.local.toml`. The following settings are available:

* `variant`          - The current variant to display. Change this in 'hugo.toml', save, and the browser will refresh automatically
                       with the new variant.
* `show_inactive`    - If 'true', it will show all the content that did not match the variant.
                       This is useful when the page contains multiple sections that vary with the selected variant,
                       so you can see all at once.
* `highlight_active` - If 'true', it will also highlight the *current* content for the variant.
* `highlight_keys`   - If 'true'', it highlights replacement keys and their values

### Changing 'variants'

Variants are flavors of the site (that you can change at the top).
During development, you can render any variant by setting it in `hugo.local.toml`:

```
variant = "byoc"
```

We call this the "active" variant.

You can also render variant content from other variants at the same time as well as highlighting the content of your active variant:

To show the content from variants other than the currently active one set:

```
show_inactive = true
```

To highlight the content of the currently active variant (to distinguish it from common content that applies to all variants), set:

```
highlight_active = true
```

> You can create you own copy of `hugo.local.toml` by copying from `hugo.local.toml~sample` to get started.

## Troubleshootting

### Identifying Problems: Missing Content

Content may be hidden due to `{{</* variant */>}}` blocks. To see what's missing,
you can adjust the variant show/hide in development mode.

For a production-like look set:

    show_inactive = false
    highlight_active = false

For a full-developer experience, set:

    show_inactive = true
    highlight_active = true

### Identifying Problems: Page Visibility

The developer site will show you in red any pages missing from the variant.
For a page to exist in the variant (or be excluded, you have to pick one), it must be listed in the `variants:` at the top of the file.
Clicking on the red page will give you the path you must add to the appropriate variant in the YAML file and a link with guidance.

Please refer to [Authoring](./authoring) for more details.

## Building Production

```
$ make dist
```

This will build all the variants and place the result in the `dist` folder.

### Testing Production Build

You can run a local web server and serve the `dist/` folder. The site must behave correctly, as it would be in its official URL.

To start a server:

```
$ make serve [PORT=<nnnnn>]
```

If specified without parameters, defaults to PORT=9000.

Example:

```
$ make serve PORT=4444
```

Then you open the browser on `http://localhost:<port>` to see the content. In the example above, it would be `http://localhost:4444/`


