---
title: Input
version: 2.0.0b32.dev0+g54ab96db3.d20251127
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Input

**Package:** `flyte.app`

Input for application.



```python
class Input(
    value: str | flyte.io.File | flyte.io.Dir,
    name: Optional[str],
    env_var: Optional[str],
    download: bool,
    mount: Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `str \| flyte.io.File \| flyte.io.Dir` | Value for input. |
| `name` | `Optional[str]` | Name of input. |
| `env_var` | `Optional[str]` | Environment name to set the value in the serving environment. |
| `download` | `bool` | When True, the input will be automatically downloaded. This only works if the value refers to an item in a object store. i.e. `s3://...` |
| `mount` | `Optional[str]` | If `value` is a directory, then the directory will be available at `mount`. If `value` is a file, then the file will be downloaded into the `mount` directory. |
| `ignore_patterns` | `list[str]` | If `value` is a directory, then this is a list of glob patterns to ignore. |

