---
title: Quick start
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Quick start

## Prerequisites

The docs site is built using the [Hugo](https://gohugo.io/) static site generator.
You will need to install it to build the site locally.
See [Hugo Installation](https://gohugo.io/getting-started/installing/).

## Clone the repository

Clone the [`unionai/docs`](https://github.com/unionai/docs) repository to your local machine.

The content is located in the `content/` folder in the form of Markdown files.
The hierarchy of the files and folders under `content/` directly reflect the URL and navigation structure of the site.

## Live preview

Next, set up the live preview by going to the root of your local repository check-out and copy `hugo.local.toml~sample` to `hugo.local.toml`:

```shell
$ cp hugo.local.toml~sample hugo.local.toml
```

This file contains the configuration for the live preview:

By default, it is set to display the `flyte` variant of the docs site along with enabling the flags `show_inactive`, `highlight_active`, and `highlight_keys` (more about these below)

Now you can start the live preview server by running:

```shell
$ make dev
```

This will build the site and launch a local server at `http://localhost:1313`.
Go to that URL to the live preview. Leave the server running.
As you edit the content you will see the changes reflected in the live preview.

## Distribution build

To build the site for distribution, run:

```shell
$ make dist
```

This will build the site locally just  as it is built by the Cloudflare CI for production.

You can view the result of the build by running a local server:

```shell
$ make serve
```

This will start a local server at `http://localhost:9000` and serve the contents of the `dist/` folder. You can also specify a port number:

```shell
$ make serve PORT=<nnnnn>
```