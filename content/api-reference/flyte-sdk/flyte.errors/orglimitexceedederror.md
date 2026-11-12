---
title: OrgLimitExceededError
description: "This error is raised when the server refuses to launch an action because the organization is at one of its limits, for example `max_actions_per_run`."
icon: exclamation-triangle
version: 2.13.2
variants: +flyte +union
layout: py_api
---

# OrgLimitExceededError

**Package:** `flyte.errors`

This error is raised when the server refuses to launch an action because the organization is at one of its limits,
for example `max_actions_per_run`. Retrying does not help; the message names the limit and the numbers.


## Parameters

```python
class OrgLimitExceededError(
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

