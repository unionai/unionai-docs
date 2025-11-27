---
title: flytekit.clis.sdk_in_container.backfill
version: 1.16.10
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


| Parameter | Type | Description |
|-|-|-|
| `from_date` | `datetime.datetime` | |
| `to_date` | `datetime.datetime` | |
| `backfill_window` | `datetime.timedelta` | |

