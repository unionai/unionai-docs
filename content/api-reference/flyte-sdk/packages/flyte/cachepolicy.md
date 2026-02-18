---
title: CachePolicy
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CachePolicy

**Package:** `flyte`

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
    params: flyte._cache.cache.VersionParameters,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | |
| `params` | `flyte._cache.cache.VersionParameters` | |

