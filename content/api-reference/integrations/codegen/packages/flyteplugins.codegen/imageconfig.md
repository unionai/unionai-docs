---
title: ImageConfig
version: 2.1.7
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# ImageConfig

**Package:** `flyteplugins.codegen`

Configuration for Docker image building at runtime.


## Parameters

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

