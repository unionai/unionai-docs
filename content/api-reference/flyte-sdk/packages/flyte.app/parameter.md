---
title: Parameter
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# Parameter

**Package:** `flyte.app`

Parameter for application.



## Parameters

```python
class Parameter(
    name: str,
    value: Optional[ParameterTypes | _DelayedValue],
    type: Optional[Literal['string', 'file', 'directory', 'app_endpoint']],
    env_var: Optional[str],
    download: bool,
    mount: Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of parameter. |
| `value` | `Optional[ParameterTypes \| _DelayedValue]` | Value for parameter. When ``None``, the value must be supplied at serving time via ``parameter_values`` in :func:`flyte.with_servecontext`. |
| `type` | `Optional[Literal['string', 'file', 'directory', 'app_endpoint']]` | Type of parameter. If ``None``, the type will be inferred from the value. |
| `env_var` | `Optional[str]` | Environment name to set the value in the serving environment. |
| `download` | `bool` | When True, the parameter will be automatically downloaded. This only works if the value refers to a file/directory in a object store. i.e. `s3://...` |
| `mount` | `Optional[str]` | If `value` is a directory, then the directory will be available at `mount`. If `value` is a file, then the file will be downloaded into the `mount` directory. |
| `ignore_patterns` | `list[str]` | If `value` is a directory, then this is a list of glob patterns to ignore. |

