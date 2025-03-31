---
title: flytekit.models.admin.common
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| Parameter | Type |
|-|-|
| `key` |  |
| `direction` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`from_python_std()`](#from_python_std) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Sort
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    text,
) -> Sort
```
| Parameter | Type |
|-|-|
| `text` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `direction` |  |  |
| `is_empty` |  |  |
| `key` |  |  |

