---
title: DbtNodeResult
description: "Small serializable summary of one dbt node result."
icon: braces
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# DbtNodeResult

**Package:** `flyteplugins.dbt`

Small serializable summary of one dbt node result.


## Parameters

```python
class DbtNodeResult(
    unique_id: str,
    name: str,
    resource_type: str,
    status: str,
    message: Optional[str] = None,
    failures: Optional[int] = None,
    execution_time: Optional[float] = None,
    relation_name: Optional[str] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `unique_id` | `str` | |
| `name` | `str` | |
| `resource_type` | `str` | |
| `status` | `str` | |
| `message` | `Optional[str]` | |
| `failures` | `Optional[int]` | |
| `execution_time` | `Optional[float]` | |
| `relation_name` | `Optional[str]` | |

