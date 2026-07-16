---
title: Set up a local docs dev environment
weight: 1
variants: +flyte +union
---

# Set up a local docs dev environment

Follow these steps to build and preview the docs site on your own machine.
Once it is running, you can edit content and see your changes live.

## Prerequisites

The site is built with the [Hugo](https://gohugo.io/) static site generator.
Install Hugo version 0.145.0 or later:

```bash
brew install hugo
```

For other platforms, see [Hugo installation](https://gohugo.io/getting-started/installing/).
You also need `git` and `make`.

## Clone the repository

Clone [`unionai/unionai-docs`](https://github.com/unionai/unionai-docs) to your machine:

```bash
git clone https://github.com/unionai/unionai-docs.git
cd unionai-docs
```

Content lives in the `content/` folder as Markdown files.
The hierarchy of files and folders under `content/` maps directly to the URL and navigation structure of the site.

## Initialize the submodules

The docs repository uses two Git submodules that you must initialize before the first build:

* `unionai-docs-infra/` holds the shared build infrastructure (Hugo configuration, layouts, themes, and build tools).
* `unionai-examples/` holds the runnable example code that pages embed.

Initialize the build infrastructure:

```bash
make init-infra
```

Then initialize the examples:

```bash
make init-examples
```

To update the examples submodule to its latest `main` later, run `make update-examples`.

## Configure the live preview

Copy the sample local configuration file at the root of the repository to `hugo.local.toml`:

```bash
cp hugo.local.toml~sample hugo.local.toml
```

This file controls the development preview and is not committed.
By default it displays the `flyte` variant with the `show_inactive`, `highlight_active`, and `highlight_keys` flags enabled.

## Start the live preview

Start the development server:

```bash
make dev
```

This builds the site and launches a local server at `http://localhost:1313`.
Open that URL in your browser and leave the server running.
As you edit content, the preview reloads automatically to reflect your changes.

## Development settings

Adjust the preview by editing `hugo.local.toml`. Save the file and the browser refreshes automatically.

| Setting | Effect |
| --- | --- |
| `variant` | The variant to display (`flyte` or `union`). This is the "active" variant. |
| `show_inactive` | If `true`, also shows content that does not match the active variant, so you can see every variant at once. |
| `highlight_active` | If `true`, highlights the active variant's content to distinguish it from content common to all variants. |
| `highlight_keys` | If `true`, highlights [key](./shortcodes#key) replacements and their values. |

For more on variants, see [Variants](./variants).

## Build the production site

To build the site the way the production pipeline does, run:

```bash
make dist
```

This builds every variant and writes the result to the `dist/` folder.
To build and validate a single variant, run `make variant VARIANT=union` (or `VARIANT=flyte`).

Serve the production build locally to check it:

```bash
make serve
```

This serves the `dist/` folder at `http://localhost:9000`.
To use a different port, pass `PORT`:

```bash
make serve PORT=4444
```

For production build details and troubleshooting, see [Production builds and troubleshooting](./publishing).

## Next steps

* [Author content](./authoring) with Markdown, shortcodes, and variants.
* Follow the [writing guidelines](./writing-guidelines) so your docs match the rest of the site.
* [Submit your contribution](./submitting-contributions) as a pull request.
