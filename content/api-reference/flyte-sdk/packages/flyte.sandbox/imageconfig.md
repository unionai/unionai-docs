---
title: ImageConfig
version: 2.0.4
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# ImageConfig

**Package:** `flyte.sandbox`

Configuration for Docker image building at runtime.


```python
class ImageConfig(
    registry: typing.Optional[str],
    registry_secret: typing.Optional[str],
    python_version: typing.Optional[tuple[int, int]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `registry` | `typing.Optional[str]` | |
| `registry_secret` | `typing.Optional[str]` | |
| `python_version` | `typing.Optional[tuple[int, int]]` | |

