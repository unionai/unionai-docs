---
title: flytekit.core.artifact_utils
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.artifact_utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`idl_partitions_from_dict()`](#idl_partitions_from_dict) |  |
| [`idl_time_partition_from_datetime()`](#idl_time_partition_from_datetime) |  |


## Methods

#### idl_partitions_from_dict()

```python
def idl_partitions_from_dict(
    p: Optional[Dict[str, str]],
) -> Optional[Partitions]
```
| Parameter | Type |
|-|-|
| `p` | `Optional[Dict[str, str]]` |

#### idl_time_partition_from_datetime()

```python
def idl_time_partition_from_datetime(
    tp: Optional[datetime],
    time_partition_granularity: Optional[Granularity],
) -> Optional[TimePartition]
```
| Parameter | Type |
|-|-|
| `tp` | `Optional[datetime]` |
| `time_partition_granularity` | `Optional[Granularity]` |

