---
title: CachePolicy
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# CachePolicy

**Package:** `union`

```python
protocol CachePolicy()
```
## Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) |  |


### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flytekit.core.cache.VersionParameters` | |

