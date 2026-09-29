---
title: PartitionSchema
description: "The partition keys fixed for an artifact name: at most one time key with its granularity, plus string keys in declaration order."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# PartitionSchema

**Package:** `flyte.remote`

The partition keys fixed for an artifact name: at most one time key with its
granularity, plus string keys in declaration order. `declared` says whether
the keys were fixed by an explicit `Artifact.declare` (True) or by the first
version (False).


## Parameters

```python
class PartitionSchema(
    time_key: str | None,
    granularity: Granularity | None,
    keys: tuple[str, ...],
    declared: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `time_key` | `str \| None` | |
| `granularity` | `Granularity \| None` | |
| `keys` | `tuple[str, ...]` | |
| `declared` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `all_keys` | `tuple[str, ...]` | Every partition key, time key first. |

## Methods

| Method | Description |
|-|-|
| [`from_pb2()`](#from_pb2) |  |
| [`to_pb2()`](#to_pb2) |  |


### from_pb2()

```python
def from_pb2(
    schema: artifact_pb2.ArtifactPartitionSchema,
    declared: bool = False,
) -> PartitionSchema
```
| Parameter | Type | Description |
|-|-|-|
| `schema` | `artifact_pb2.ArtifactPartitionSchema` | |
| `declared` | `bool` | |

### to_pb2()

```python
def to_pb2()
```
