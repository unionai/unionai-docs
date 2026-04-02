---
title: TimeFilter
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# TimeFilter

**Package:** `flyte.remote`

Filter for time-based fields (e.g. created_at, updated_at).



## Parameters

```python
class TimeFilter(
    after: datetime.datetime | None,
    before: datetime.datetime | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `after` | `datetime.datetime \| None` | Return only entries at or after this datetime (inclusive). |
| `before` | `datetime.datetime \| None` | Return only entries before this datetime (exclusive). |

