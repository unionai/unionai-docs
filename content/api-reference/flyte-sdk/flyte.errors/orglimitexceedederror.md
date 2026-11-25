---
title: OrgLimitExceededError
description: "This error is raised when the server refuses a request because the organization is at one of its limits, for example `max_actions_per_run` or `max_clusters`."
icon: exclamation-triangle
version: 2.15.0
variants: +flyte +union
layout: py_api
---

# OrgLimitExceededError

**Package:** `flyte.errors`

This error is raised when the server refuses a request because the organization is at one of its limits, for
example `max_actions_per_run` or `max_clusters`. Retrying does not help: the limit has to be raised. `org_limit`
holds the limit's name and numbers, when the server sent them.


## Parameters

```python
class OrgLimitExceededError(
    message: str,
    org_limit: flyte.errors.OrgLimit | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |
| `org_limit` | `flyte.errors.OrgLimit \| None` | |

