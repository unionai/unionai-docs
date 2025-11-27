---
title: TypeAnnotation
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TypeAnnotation

**Package:** `flytekit.models.annotation`

Python class representation of the flyteidl TypeAnnotation message.


```python
class TypeAnnotation(
    annotations: typing.Dict[str, typing.Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `annotations` | `typing.Dict[str, typing.Any]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`merge_annotations()`](#merge_annotations) | Merges two annotations together. |
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

### merge_annotations()

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

### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.types_pb2.TypeAnnotation


## Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}:rtype: dict[str, Any]
{{< /multiline >}} |

