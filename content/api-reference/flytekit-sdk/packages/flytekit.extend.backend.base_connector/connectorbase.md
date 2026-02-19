---
title: ConnectorBase
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectorBase

**Package:** `flytekit.extend.backend.base_connector`

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
| `task_category` | `None` | task category that the connector supports |

