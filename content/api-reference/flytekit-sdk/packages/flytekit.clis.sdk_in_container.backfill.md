---
title: flytekit.clis.sdk_in_container.backfill
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.backfill

## Directory

### Methods

| Method | Description |
|-|-|
| [`resolve_backfill_window()`](#resolve_backfill_window) | Resolves the from_date -> to_date. |


## Methods

#### resolve_backfill_window()

```python
def resolve_backfill_window(
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    backfill_window: datetime.timedelta,
) -> typing.Tuple[datetime.datetime, datetime.datetime]
```
Resolves the from_date -> to_date


| Parameter | Type |
|-|-|
| `from_date` | `datetime.datetime` |
| `to_date` | `datetime.datetime` |
| `backfill_window` | `datetime.timedelta` |

