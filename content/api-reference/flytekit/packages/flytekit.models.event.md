---
title: flytekit.models.event
version: 1.15.4.dev2+g3e3ce2426
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
def TaskExecutionMetadata(
    external_resources,
):
```
| Parameter | Type |
|-|-|
| `external_resources` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
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
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| external_resources |  |  |
| is_empty |  |  |

