---
title: SchemaType
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SchemaType

**Package:** `flytekit.models.types`

```python
class SchemaType(
    columns,
)
```
| Parameter | Type | Description |
|-|-|-|
| `columns` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.types_pb2.SchemaType


## Properties

| Property | Type | Description |
|-|-|-|
| `columns` |  | {{< multiline >}}A list of columns defining the underlying data frame.
:rtype: list[SchemaType.SchemaColumn]
{{< /multiline >}} |
| `is_empty` |  |  |

