---
title: Schema
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Schema

**Package:** `flytekit.models.literals`

```python
class Schema(
    uri,
    type,
)
```
A strongly typed schema that defines the interface of data retrieved from the underlying storage medium.



| Parameter | Type | Description |
|-|-|-|
| `uri` |  | |
| `type` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `type` | `None` | :rtype: flytekit.models.types.SchemaType |
| `uri` | `None` | :rtype: Text |

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.literals_pb2.Schema


