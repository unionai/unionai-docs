---
title: LiteralOffloadedMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LiteralOffloadedMetadata

**Package:** `flytekit.models.literals`

```python
class LiteralOffloadedMetadata(
    uri: typing.Optional[str],
    size_bytes: typing.Optional[int],
    inferred_type: typing.Optional[flytekit.models.types.LiteralType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `uri` | `typing.Optional[str]` | |
| `size_bytes` | `typing.Optional[int]` | |
| `inferred_type` | `typing.Optional[flytekit.models.types.LiteralType]` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `inferred_type` |  |  |
| `is_empty` |  |  |
| `size_bytes` |  |  |
| `uri` |  |  |

