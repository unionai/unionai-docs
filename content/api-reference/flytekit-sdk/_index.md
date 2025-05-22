---
title: Flytekit SDK
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# Flytekit SDK

These are the Flytekit SDK API docs.

Flytekit is the core Python SDK for the Union and Flyte platforms.


## Developing on Flyte

For developing on the Flyte platform you need to add the `flytekit` package to your project:

```shell
$ uv add flytekit
```

This will install the Flytekit SDK and the `pyflyte` command-line tool.

When working with the FLytekit SDK you will be using the `pyflyte` CLI and the Flytekit SDK docs (not the Union SDK docs).


## Developing on Union

For developing on the Union platform you need to add the `union` package to your project:

```shell
$ uv add union
```

This will install the Union SDK, which is a superset of the Flytekit SDK.
It will also install the `union` command-line tool.

When working with the Union SDK you will be us=ing the `union` CLI and both the Flytekit SDK and the Union SDK docs.


