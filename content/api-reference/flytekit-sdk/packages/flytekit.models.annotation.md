---
title: flytekit.models.annotation
version: 1.16.15
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.annotation

## Directory

### Classes

| Class | Description |
|-|-|
| [`TypeAnnotation`](.././flytekit.models.annotation#flytekitmodelsannotationtypeannotation) | Python class representation of the flyteidl TypeAnnotation message. |

## flytekit.models.annotation.TypeAnnotation

Python class representation of the flyteidl TypeAnnotation message.


### Parameters

```python
class TypeAnnotation(
    annotations: typing.Dict[str, typing.Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `annotations` | `typing.Dict[str, typing.Any]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`merge_annotations()`](#merge_annotations) | Merges two annotations together. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** TypeAnnotation

#### merge_annotations()

```python
def merge_annotations(
    annotation: TypeAnnotation,
    other_annotation: TypeAnnotation,
) -> TypeAnnotation
```
Merges two annotations together. If the same key exists in both annotations, the value in the other annotation
will be used.


| Parameter | Type | Description |
|-|-|-|
| `annotation` | `TypeAnnotation` | |
| `other_annotation` | `TypeAnnotation` | |

**Returns:** TypeAnnotation

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.types_pb2.TypeAnnotation

