---
title: ResourceExhaustedError
description: "This error is raised when the server refuses a request for now, for example because the organization is at its `max_concurrent_runs` or `max_queue_depth`: it succeeds once running work finishes."
icon: exclamation-triangle
version: 2.14.0
variants: +flyte +union
layout: py_api
---

# ResourceExhaustedError

**Package:** `flyte.errors`

This error is raised when the server refuses a request for now, for example because the organization is at its
`max_concurrent_runs` or `max_queue_depth`: it succeeds once running work finishes. `org_limit` holds the limit's
name and numbers, when the server sent them.


## Parameters

```python
class ResourceExhaustedError(
    message: str,
    org_limit: flyte.errors.OrgLimit | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `org_limit` | `flyte.errors.OrgLimit \| None` | |

