---
title: CachePolicy
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CachePolicy

**Package:** `flytekit.core.cache`

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

