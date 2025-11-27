---
title: TimePartition
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TimePartition

**Package:** `flytekit.core.artifact`

```python
class TimePartition(
    value: Union[art_id.LabelValue, art_id.InputBindingData, str, datetime.datetime, None],
    op: Optional[Op],
    other: Optional[timedelta],
    granularity: Granularity,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Union[art_id.LabelValue, art_id.InputBindingData, str, datetime.datetime, None]` | |
| `op` | `Optional[Op]` | |
| `other` | `Optional[timedelta]` | |
| `granularity` | `Granularity` | |

## Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

