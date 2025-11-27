---
title: Description
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Description

**Package:** `flytekit.models.documentation`

Full user description with formatting preserved. This can be rendered
by clients, such as the console or command line tools with in-tact
formatting.


```python
class Description(
    value: typing.Optional[str],
    uri: typing.Optional[str],
    icon_link: typing.Optional[str],
    format: <enum 'DescriptionFormat'>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Optional[str]` | |
| `uri` | `typing.Optional[str]` | |
| `icon_link` | `typing.Optional[str]` | |
| `format` | `<enum 'DescriptionFormat'>` | |

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
    pb2_object: flyteidl.admin.description_entity_pb2.Description,
) -> Description
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.Description` | |

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

