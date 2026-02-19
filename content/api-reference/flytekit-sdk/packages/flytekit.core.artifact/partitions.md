---
title: Partitions
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Partitions

**Package:** `flytekit.core.artifact`

```python
class Partitions(
    partitions: Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `partitions` | `Optional[typing.Mapping[str, Union[str, art_id.InputBindingData, Partition]]]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `partitions` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`set_reference_artifact()`](#set_reference_artifact) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### set_reference_artifact()

```python
def set_reference_artifact(
    artifact: Artifact,
)
```
| Parameter | Type | Description |
|-|-|-|
| `artifact` | `Artifact` | |

### to_flyte_idl()

```python
def to_flyte_idl(
    kwargs,
) -> Optional[art_id.Partitions]
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

