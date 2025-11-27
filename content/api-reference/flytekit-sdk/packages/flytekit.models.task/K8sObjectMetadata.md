---
title: K8sObjectMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# K8sObjectMetadata

**Package:** `flytekit.models.task`

```python
class K8sObjectMetadata(
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
)
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type | Description |
|-|-|-|
| `labels` | `typing.Optional[typing.Dict[str, str]]` | |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` | |

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
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sObjectMetadata` | |

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
| `annotations` |  |  |
| `is_empty` |  |  |
| `labels` |  |  |

