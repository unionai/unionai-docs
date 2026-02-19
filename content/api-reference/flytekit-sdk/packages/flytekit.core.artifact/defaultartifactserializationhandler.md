---
title: DefaultArtifactSerializationHandler
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DefaultArtifactSerializationHandler

**Package:** `flytekit.core.artifact`

## Methods

| Method | Description |
|-|-|
| [`artifact_query_to_idl()`](#artifact_query_to_idl) |  |
| [`partitions_to_idl()`](#partitions_to_idl) |  |
| [`time_partition_to_idl()`](#time_partition_to_idl) |  |


### artifact_query_to_idl()

```python
def artifact_query_to_idl(
    aq: ArtifactQuery,
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type | Description |
|-|-|-|
| `aq` | `ArtifactQuery` | |
| `kwargs` | `**kwargs` | |

### partitions_to_idl()

```python
def partitions_to_idl(
    p: Optional[Partitions],
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `Optional[Partitions]` | |
| `kwargs` | `**kwargs` | |

### time_partition_to_idl()

```python
def time_partition_to_idl(
    tp: Optional[TimePartition],
    kwargs,
) -> Optional[art_id.TimePartition]
```
| Parameter | Type | Description |
|-|-|-|
| `tp` | `Optional[TimePartition]` | |
| `kwargs` | `**kwargs` | |

