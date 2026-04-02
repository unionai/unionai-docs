---
title: ImageConfig
version: 2.1.3.dev1+ge23e739d5
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

