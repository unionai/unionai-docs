---
title: UnionType
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# UnionType

**Package:** `flytekit.models.types`

Models _types_pb2.UnionType



```python
class UnionType(
    variants: typing.List[ForwardRef('LiteralType')],
)
```
| Parameter | Type | Description |
|-|-|-|
| `variants` | `typing.List[ForwardRef('LiteralType')]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `variants` | `None` |  |

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
    proto: flyteidl.core.types_pb2.UnionType,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.UnionType` | |

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
