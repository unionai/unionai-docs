---
title: TaskReference
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskReference

**Package:** `flytekit.core.reference_entity`

A reference object containing metadata that points to a remote task.


```python
class TaskReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |
| `version` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

