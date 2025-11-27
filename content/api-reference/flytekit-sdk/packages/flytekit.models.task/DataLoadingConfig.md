---
title: DataLoadingConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataLoadingConfig

**Package:** `flytekit.models.task`

```python
class DataLoadingConfig(
    input_path: str,
    output_path: str,
    enabled: bool,
    format: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a5250>,
    io_strategy: flytekit.models.task.IOStrategy,
)
```
| Parameter | Type | Description |
|-|-|-|
| `input_path` | `str` | |
| `output_path` | `str` | |
| `enabled` | `bool` | |
| `format` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a5250>` | |
| `io_strategy` | `flytekit.models.task.IOStrategy` | |

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
    pb2: flyteidl.core.tasks_pb2.DataLoadingConfig,
) -> DataLoadingConfig
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `flyteidl.core.tasks_pb2.DataLoadingConfig` | |

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
| `is_empty` |  |  |

