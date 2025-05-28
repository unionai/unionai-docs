---
title: flytekit.models.admin.common
version: 0.1.dev2192+g7c539c3.d20250403
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
| Parameter | Type |
|-|-|
| `key` |  |
| `direction` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Sort
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    text,
) -> e: Sort
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.Sort


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `direction` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `key` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

