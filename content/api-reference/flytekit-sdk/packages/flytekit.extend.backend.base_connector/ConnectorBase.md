---
title: ConnectorBase
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectorBase

**Package:** `flytekit.extend.backend.base_connector`

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class ConnectorBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_type_name` | `str` | |
| `task_type_version` | `int` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

