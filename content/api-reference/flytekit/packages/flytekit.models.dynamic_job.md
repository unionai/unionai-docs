---
title: flytekit.models.dynamic_job
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.dynamic_job

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicJobSpec`](.././flytekit.models.dynamic_job#flytekitmodelsdynamic_jobdynamicjobspec) | None. |

## flytekit.models.dynamic_job.DynamicJobSpec

```python
def DynamicJobSpec(
    tasks,
    nodes,
    min_successes,
    outputs,
    subworkflows,
):
```
Initializes a new FutureTaskDocument.



| Parameter | Type |
|-|-|
| `tasks` |  |
| `nodes` |  |
| `min_successes` |  |
| `outputs` |  |
| `subworkflows` |  |

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
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| min_successes |  |  |
| nodes |  |  |
| outputs |  |  |
| subworkflows |  |  |
| tasks |  |  |

