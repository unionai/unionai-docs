---
title: TimeFilter
description: "Filter for time-based fields (e.g. created_at, updated_at)."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# TimeFilter

**Package:** `flyte.remote`

Filter for time-based fields (e.g. created_at, updated_at).



## Parameters

```python
class TimeFilter(
    after: datetime.datetime | None = None,
    before: datetime.datetime | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `after` | `datetime.datetime \| None` | Return only entries at or after this datetime (inclusive). |
| `before` | `datetime.datetime \| None` | Return only entries before this datetime (exclusive). |

