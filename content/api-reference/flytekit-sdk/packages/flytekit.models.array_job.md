---
title: flytekit.models.array_job
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.array_job

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayJob`](.././flytekit.models.array_job#flytekitmodelsarray_jobarrayjob) | None. |

## flytekit.models.array_job.ArrayJob

```python
def ArrayJob(
    parallelism,
    size,
    min_successes,
    min_success_ratio,
):
```
Initializes a new ArrayJob.


| Parameter | Type |
|-|-|
| `parallelism` |  |
| `size` |  |
| `min_successes` |  |
| `min_success_ratio` |  |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_dict()

```python
def from_dict(
    idl_dict,
):
```
| Parameter | Type |
|-|-|
| `idl_dict` |  |

#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
):
```
| Parameter | Type |
|-|-|
| `idl_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_dict()

```python
def to_dict()
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
| min_success_ratio |  |  |
| min_successes |  |  |
| parallelism |  |  |
| size |  |  |

