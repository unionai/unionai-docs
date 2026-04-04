---
title: flytekit.models.presto
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.presto

This is a deprecated module. Model files for plugins should go alongside the microlib.
See ``plugins/flytekit-kf-pytorch/flytekitplugins/kfpytorch/models.py`` as an example.
## Directory

### Classes

| Class | Description |
|-|-|
| [`PrestoQuery`](.././flytekit.models.presto#flytekitmodelsprestoprestoquery) |  |

## flytekit.models.presto.PrestoQuery

### Parameters

```python
class PrestoQuery(
    routing_group,
    catalog,
    schema,
    statement,
)
```
Initializes a new PrestoQuery.



| Parameter | Type | Description |
|-|-|-|
| `routing_group` |  | |
| `catalog` |  | |
| `schema` |  | |
| `statement` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `catalog` | `None` |  |
| `is_empty` | `None` |  |
| `routing_group` | `None` | The query string. |
| `schema` | `None` |  |
| `statement` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
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

**Returns:** PrestoQuery

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
**Returns:** _presto.PrestoQuery

