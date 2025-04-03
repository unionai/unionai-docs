---
title: Union SDK
version: 0.1.170
variants: +byoc +byok +serverless -flyte
layout: py_api
---

# Union SDK

The Union SDK provides the Python API for writing Union workflows. It consists
of the open-source `flytekit` package in addition to the `union` package which
supports additional functionality specific to Union.

## Developing on Union

For developing on the Union platform you need to add the `union` package to your
project:

```shell
$ uv add union
```

This will install the Union SDK, which is a superset of the Flytekit SDK.
It will also install the `union` command-line tool.

When working with the Union SDK you will be us=ing the `union` CLI and both the
Flytekit SDK and the Union SDK docs.


