---
title: flytekit.models.presto
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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

```python
class PrestoQuery(
    routing_group,
    catalog,
    schema,
    statement,
)
```
Initializes a new PrestoQuery.



| Parameter | Type |
|-|-|
| `routing_group` |  |
| `catalog` |  |
| `schema` |  |
| `statement` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| `catalog` |  |  |
| `is_empty` |  |  |
| `routing_group` |  | {{< multiline >}}The query string.
{{< /multiline >}} |
| `schema` |  |  |
| `statement` |  |  |

