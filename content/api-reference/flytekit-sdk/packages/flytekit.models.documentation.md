---
title: flytekit.models.documentation
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.documentation

## Directory

### Classes

| Class | Description |
|-|-|
| [`Description`](.././flytekit.models.documentation#flytekitmodelsdocumentationdescription) | Full user description with formatting preserved. |
| [`Documentation`](.././flytekit.models.documentation#flytekitmodelsdocumentationdocumentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`SourceCode`](.././flytekit.models.documentation#flytekitmodelsdocumentationsourcecode) | Link to source code used to define this task or workflow. |

## flytekit.models.documentation.Description

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

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.Description,
) -> Description
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.Description` | |

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
## flytekit.models.documentation.Documentation

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

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.DescriptionEntity,
) -> Documentation
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.DescriptionEntity` | |

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
## flytekit.models.documentation.SourceCode

Link to source code used to define this task or workflow.



```python
class SourceCode(
    link: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `link` | `typing.Optional[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.SourceCode,
) -> SourceCode
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.SourceCode` | |

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
