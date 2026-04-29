---
title: ImageConfig
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# ImageConfig

**Package:** `flyte.sandbox`

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

