---
title: Documentation
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Documentation

**Package:** `flytekit.models.documentation`

DescriptionEntity contains detailed description for the task/workflow/launch plan.
Documentation could provide insight into the algorithms, business use case, etc.


```python
class Documentation(
    short_description: typing.Optional[str],
    long_description: typing.Optional[flytekit.models.documentation.Description],
    source_code: typing.Optional[flytekit.models.documentation.SourceCode],
)
```
| Parameter | Type | Description |
|-|-|-|
| `short_description` | `typing.Optional[str]` | One-liner overview of the entity. |
| `long_description` | `typing.Optional[flytekit.models.documentation.Description]` | Full user description with formatting preserved. |
| `source_code` | `typing.Optional[flytekit.models.documentation.SourceCode]` | link to source code used to define this entity |

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
    pb2_object: flyteidl.admin.description_entity_pb2.DescriptionEntity,
) -> Documentation
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.DescriptionEntity` | |

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
