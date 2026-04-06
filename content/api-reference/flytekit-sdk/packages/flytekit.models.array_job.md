---
title: flytekit.models.array_job
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.array_job

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayJob`](.././flytekit.models.array_job#flytekitmodelsarray_jobarrayjob) |  |

## flytekit.models.array_job.ArrayJob

### Parameters

```python
class ArrayJob(
    parallelism,
    size,
    min_successes,
    min_success_ratio,
)
```
Initializes a new ArrayJob.


| Parameter | Type | Description |
|-|-|-|
| `parallelism` |  | |
| `size` |  | |
| `min_successes` |  | |
| `min_success_ratio` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `min_success_ratio` | `None` |  |
| `min_successes` | `None` | An absolute number of the minimum number of successful completions of subtasks. As soon as this criteria is met,     the array job will be marked as successful and outputs will be computed. |
| `parallelism` | `None` | Defines the minimum number of instances to bring up concurrently at any given point. |
| `size` | `None` | Defines the number of instances to launch at most. This number should match the size of the input if the job  requires processing of all input data. This has to be a positive number. |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_dict()

```python
def from_dict(
    idl_dict,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_dict` |  | |

**Returns:** ArrayJob

#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_object` |  | |

**Returns:** FlyteCustomIdlEntity

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_dict()

```python
def to_dict()
```
**Returns:** dict[T, Text]

#### to_flyte_idl()

```python
def to_flyte_idl()
```
