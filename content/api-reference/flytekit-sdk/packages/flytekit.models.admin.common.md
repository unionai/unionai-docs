---
title: flytekit.models.admin.common
version: 1.16.14
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
| `direction` | `None` | :rtype: int |
| `is_empty` | `None` |  |
| `key` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### from_python_std()

```python
def from_python_std(
    text,
)
```
| Parameter | Type | Description |
|-|-|-|
| `text` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.Sort


