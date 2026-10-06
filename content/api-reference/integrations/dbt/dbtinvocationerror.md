---
title: DbtInvocationError
description: "Raised when dbt finishes cleanly but reports failed node results."
icon: exclamation-triangle
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# DbtInvocationError

**Package:** `flyteplugins.dbt`

Raised when dbt finishes cleanly but reports failed node results.


## Parameters

```python
class DbtInvocationError(
    cli_args: list[str],
    results: list[DbtNodeResult],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cli_args` | `list[str]` | |
| `results` | `list[DbtNodeResult]` | |

