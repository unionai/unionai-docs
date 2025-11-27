---
title: Input
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# Input

**Package:** `union.app`

Input for application.



```python
class Input(
    value: typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery],
    name: typing.Optional[str],
    env_var: typing.Optional[str],
    type: typing.Optional[union.app._models.Input.Type],
    download: bool,
    mount: typing.Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery]` | |
| `name` | `typing.Optional[str]` | |
| `env_var` | `typing.Optional[str]` | |
| `type` | `typing.Optional[union.app._models.Input.Type]` | |
| `download` | `bool` | |
| `mount` | `typing.Optional[str]` | |
| `ignore_patterns` | `list[str]` | |

