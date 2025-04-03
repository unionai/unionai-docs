---
title: flytekit.models.event
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.event

## Directory

### Classes

| Class | Description |
|-|-|
| [`TaskExecutionMetadata`](.././flytekit.models.event#flytekitmodelseventtaskexecutionmetadata) | . |

## flytekit.models.event.TaskExecutionMetadata

```python
class TaskExecutionMetadata(
    external_resources,
)
```
| Parameter | Type |
|-|-|
| `external_resources` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: TaskExecutionMetadata
```
| Parameter | Type |
|-|-|
| `proto` |  |

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
:rtype: flyteidl.event.TaskExecutionMetadata


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `external_resources` |  | {{< multiline >}}:rtype: google.protobuf.internal.containers.RepeatedCompositeFieldContainer
{{< /multiline >}} |
| `is_empty` |  |  |

