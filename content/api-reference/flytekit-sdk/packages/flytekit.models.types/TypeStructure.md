---
title: TypeStructure
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TypeStructure

**Package:** `flytekit.models.types`

Models _types_pb2.TypeStructure


```python
class TypeStructure(
    tag: str,
    dataclass_type: typing.Dict[str, ForwardRef('LiteralType')],
)
```
| Parameter | Type | Description |
|-|-|-|
| `tag` | `str` | |
| `dataclass_type` | `typing.Dict[str, ForwardRef('LiteralType')]` | |

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
    proto: flyteidl.core.types_pb2.TypeStructure,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.TypeStructure` | |

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
| `dataclass_type` |  |  |
| `is_empty` |  |  |
| `tag` |  |  |

