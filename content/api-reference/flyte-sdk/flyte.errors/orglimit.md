---
title: OrgLimit
description: "The org limit a request was refused at, as the server reported it."
icon: braces
version: 2.15.0
variants: +flyte +union
layout: py_api
---

# OrgLimit

**Package:** `flyte.errors`

The org limit a request was refused at, as the server reported it.



## Parameters

```python
class OrgLimit(
    limit: str,
    ceiling: int,
    current: int,
    requested: int,
    tier_default: int | None = None,
    upgrade_url: str = '',
    tier: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `limit` | `str` | The limit's name, e.g. `max_concurrent_runs`. |
| `ceiling` | `int` | The org's current value for the limit. |
| `current` | `int` | The org's usage before the request. |
| `requested` | `int` | How much the request would have added. |
| `tier_default` | `int \| None` | The limit's default for the org's tier; None when the server didn't say or the org's plan has no tier defaults. It differs from `ceiling` when the org's limit was raised (or lowered) for it. |
| `upgrade_url` | `str` | Where to ask for the limit to be raised; empty when the server didn't say. |
| `tier` | `str` | The tier `tier_default` belongs to, e.g. `Teams` or `Enterprise`; empty when the server didn't say. |

