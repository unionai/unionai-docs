---
title: PrestoQuery
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PrestoQuery

**Package:** `flytekit.models.presto`

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

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _presto. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: _presto.PrestoQuery


## Properties

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

