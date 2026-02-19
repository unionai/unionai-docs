---
title: BlobMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BlobMetadata

**Package:** `flytekit.models.literals`

This is metadata for the Blob literal.



```python
class BlobMetadata(
    type,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `type` | `None` | :rtype: flytekit.models.core.types.BlobType |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.literals_pb2.BlobMetadata


