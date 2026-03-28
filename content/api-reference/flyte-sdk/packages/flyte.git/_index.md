---
title: flyte.git
version: 2.0.12.dev22+g879ad6de4
variants: +flyte +union
layout: py_api
sidebar_expanded: true
---

# flyte.git

## Directory

### Classes

| Class | Description |
|-|-|
| [`GitStatus`](../flyte.git/gitstatus) | A class representing the status of a git repository. |

### Methods

| Method | Description |
|-|-|
| [`config_from_root()`](#config_from_root) | Get the config file from the git root directory. |


## Methods

#### config_from_root()

```python
def config_from_root(
    path: pathlib.Path | str,
) -> flyte.config._config.Config | None
```
Get the config file from the git root directory.

By default, the config file is expected to be in `.flyte/config.yaml` in the git root directory.



| Parameter | Type | Description |
|-|-|-|
| `path` | `pathlib.Path \| str` | Path to the config file relative to git root directory (default |

**Returns:** Config object if found, None otherwise

