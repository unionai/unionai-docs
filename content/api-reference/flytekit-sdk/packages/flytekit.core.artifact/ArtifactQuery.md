---
title: ArtifactQuery
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ArtifactQuery

**Package:** `flytekit.core.artifact`

```python
class ArtifactQuery(
    artifact: Artifact,
    name: str,
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[TimePartition],
    partitions: Optional[Partitions],
    tag: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `artifact` | `Artifact` | |
| `name` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |
| `time_partition` | `Optional[TimePartition]` | |
| `partitions` | `Optional[Partitions]` | |
| `tag` | `Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`get_partition_str()`](#get_partition_str) |  |
| [`get_str()`](#get_str) |  |
| [`get_time_partition_str()`](#get_time_partition_str) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### get_partition_str()

```python
def get_partition_str(
    kwargs,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### get_str()

```python
def get_str(
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### get_time_partition_str()

```python
def get_time_partition_str(
    kwargs,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> art_id.ArtifactQuery
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `bound` |  |  |

