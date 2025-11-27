---
title: EnumType
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# EnumType

**Package:** `flytekit.models.core.types`

Models _types_pb2.EnumType


```python
class EnumType(
    values: typing.List[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `values` | `typing.List[str]` | |

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
    proto: _types_pb2.EnumType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `_types_pb2.EnumType` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

