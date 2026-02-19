---
title: Input
version: 0.1.201
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
| `value` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery]` | Value for input. |
| `name` | `typing.Optional[str]` | Name of input. |
| `env_var` | `typing.Optional[str]` | Environment name to set the value in the serving environment. |
| `type` | `typing.Optional[union.app._models.Input.Type]` | |
| `download` | `bool` | When True, the input will be automatically downloaded. This only works if the value refers to an item in a object store. i.e. `s3://...` |
| `mount` | `typing.Optional[str]` | If `value` is a directory, then the directory will be available at `mount`. If `value` is a file, then the file will be downloaded into the `mount` directory. |
| `ignore_patterns` | `list[str]` | If `value` is a directory, then this is a list of glob patterns to ignore. |

