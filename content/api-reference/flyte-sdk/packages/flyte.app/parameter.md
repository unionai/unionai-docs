---
title: Parameter
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Parameter

**Package:** `flyte.app`

Parameter for application.



```python
class Parameter(
    name: str,
    value: ParameterTypes | _DelayedValue,
    env_var: Optional[str],
    download: bool,
    mount: Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of parameter. |
| `value` | `ParameterTypes \| _DelayedValue` | Value for parameter. |
| `env_var` | `Optional[str]` | Environment name to set the value in the serving environment. |
| `download` | `bool` | When True, the parameter will be automatically downloaded. This only works if the value refers to an item in a object store. i.e. `s3://...` |
| `mount` | `Optional[str]` | If `value` is a directory, then the directory will be available at `mount`. If `value` is a file, then the file will be downloaded into the `mount` directory. |
| `ignore_patterns` | `list[str]` | If `value` is a directory, then this is a list of glob patterns to ignore. |

