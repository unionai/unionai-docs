---
title: IOStrategy
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# IOStrategy

**Package:** `flytekit.models.task`

Provides methods to manage data in and out of the Raw container using Download Modes. This can only be used if DataLoadingConfig is enabled.



```python
class IOStrategy(
    download_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10940bd40>,
    upload_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10949c590>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `download_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10940bd40>` | |
| `upload_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10949c590>` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

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
    pb2_object: flyteidl.core.tasks_pb2.IOStrategy,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.IOStrategy` | |

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
