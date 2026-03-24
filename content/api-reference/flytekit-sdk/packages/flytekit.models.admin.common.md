---
title: flytekit.models.admin.common
version: 1.16.15
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.admin.common

## Directory

### Classes

| Class | Description |
|-|-|
| [`Sort`](.././flytekit.models.admin.common#flytekitmodelsadmincommonsort) |  |

## flytekit.models.admin.common.Sort

### Parameters

```python
class Sort(
    key,
    direction,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `direction` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `direction` | `None` |  |
| `is_empty` | `None` |  |
| `key` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Sort

#### from_python_std()

```python
def from_python_std(
    text,
)
```
| Parameter | Type | Description |
|-|-|-|
| `text` |  | |

**Returns:** Sort

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.common_pb2.Sort

