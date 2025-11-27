---
title: Error
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Error

**Package:** `flytekit.models.types`

```python
class Error(
    failed_node_id: str,
    message: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `failed_node_id` | `str` | |
| `message` | `str` | |

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
    pb2_object: flyteidl.core.types_pb2.Error,
) -> Error
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.types_pb2.Error` | |

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
| `failed_node_id` |  |  |
| `is_empty` |  |  |
| `message` |  |  |

