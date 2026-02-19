---
title: NamedEntityMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NamedEntityMetadata

**Package:** `flytekit.models.named_entity`

```python
class NamedEntityMetadata(
    description,
    state,
)
```
| Parameter | Type | Description |
|-|-|-|
| `description` |  | |
| `state` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `description` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `state` | `None` | enum value from NamedEntityState :rtype: int |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.common_pb2.NamedEntityMetadata


