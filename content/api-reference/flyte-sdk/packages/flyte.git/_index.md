---
title: flyte.git
version: 2.0.0b34
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.git

## Directory

### Methods

| Method | Description |
|-|-|
| [`config_from_root()`](#config_from_root) | Get the config file from the git root directory. |


## Methods

#### config_from_root()

```python
def config_from_root(
    path: pathlib._local.Path | str,
) -> flyte.config._config.Config | None
```
Get the config file from the git root directory.

By default, the config file is expected to be in `.flyte/config.yaml` in the git root directory.


| Parameter | Type | Description |
|-|-|-|
| `path` | `pathlib._local.Path \| str` | |

