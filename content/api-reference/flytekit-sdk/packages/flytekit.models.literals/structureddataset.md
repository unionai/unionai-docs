---
title: StructuredDataset
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StructuredDataset

**Package:** `flytekit.models.literals`

```python
class StructuredDataset(
    uri: str,
    metadata: typing.Optional[flytekit.models.literals.StructuredDatasetMetadata],
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.


| Parameter | Type | Description |
|-|-|-|
| `uri` | `str` | |
| `metadata` | `typing.Optional[flytekit.models.literals.StructuredDatasetMetadata]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `metadata` | `None` |  |
| `uri` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.StructuredDataset,
) -> StructuredDataset
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDataset` | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
