---
title: union.bin.runtime
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.bin.runtime


Union runtime module, this is the entrypoint script for the Union runtime.

Caution: Startup time for this module is very important, as it is the entrypoint for the Union runtime.
Refrain from importing any modules here. If you need to import any modules, do it inside the main function.

## Directory

### Variables

| Property | Type | Description |
|-|-|-|
| `ROOT_RUN_NAME` | `str` |  |
| `RUN_NAME` | `str` |  |

