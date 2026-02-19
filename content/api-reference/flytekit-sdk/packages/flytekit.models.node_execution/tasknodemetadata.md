---
title: TaskNodeMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskNodeMetadata

**Package:** `flytekit.models.node_execution`

```python
class TaskNodeMetadata(
    cache_status: int,
    catalog_key: flytekit.models.core.catalog.CatalogMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cache_status` | `int` | |
| `catalog_key` | `flytekit.models.core.catalog.CatalogMetadata` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cache_status` | `None` |  |
| `catalog_key` | `None` |  |
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
    p: flyteidl.admin.node_execution_pb2.TaskNodeMetadata,
) -> TaskNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.TaskNodeMetadata` | |

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
