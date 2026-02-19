---
title: SourceCode
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SourceCode

**Package:** `flytekit.models.documentation`

Link to source code used to define this task or workflow.



```python
class SourceCode(
    link: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `link` | `typing.Optional[str]` | |

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
    pb2_object: flyteidl.admin.description_entity_pb2.SourceCode,
) -> SourceCode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.SourceCode` | |

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
