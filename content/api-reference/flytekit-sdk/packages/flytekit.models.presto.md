---
title: flytekit.models.presto
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _presto. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> n: PrestoQuery
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _presto.PrestoQuery


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `catalog` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `routing_group` |  | {{< multiline >}}The query string.
:rtype: str
{{< /multiline >}} |
| `schema` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `statement` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |

