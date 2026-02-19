---
title: SystemMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SystemMetadata

**Package:** `flytekit.models.execution`

```python
class SystemMetadata(
    execution_cluster: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_cluster` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `execution_cluster` | `None` |  |
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
    pb2_object: flyteidl.admin.execution_pb2.SystemMetadata,
) -> SystemMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.execution_pb2.SystemMetadata` | |

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
