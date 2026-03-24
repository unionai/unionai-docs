---
title: flytekitplugins.dask.models
version: 1.16.15
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekitplugins.dask.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`DaskJob`](.././flytekitplugins.dask.models#flytekitpluginsdaskmodelsdaskjob) | Configuration for the custom dask job to run. |
| [`Scheduler`](.././flytekitplugins.dask.models#flytekitpluginsdaskmodelsscheduler) | Configuration for the scheduler pod. |
| [`WorkerGroup`](.././flytekitplugins.dask.models#flytekitpluginsdaskmodelsworkergroup) | Configuration for a dask worker group. |

## flytekitplugins.dask.models.DaskJob

Configuration for the custom dask job to run



### Parameters

```python
class DaskJob(
    scheduler: flytekitplugins.dask.models.Scheduler,
    workers: flytekitplugins.dask.models.WorkerGroup,
)
```
| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `flytekitplugins.dask.models.Scheduler` | Configuration for the scheduler |
| `workers` | `flytekitplugins.dask.models.WorkerGroup` | Configuration of the default worker group |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `scheduler` | `None` |  |
| `workers` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** The dask job serialized to protobuf

## flytekitplugins.dask.models.Scheduler

Configuration for the scheduler pod



### Parameters

```python
class Scheduler(
    image: typing.Optional[str],
    resources: typing.Optional[flytekit.models.task.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | Optional image to use. |
| `resources` | `typing.Optional[flytekit.models.task.Resources]` | Optional resources to use. |

### Properties

| Property | Type | Description |
|-|-|-|
| `image` | `None` |  |
| `is_empty` | `None` |  |
| `resources` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** The scheduler spec serialized to protobuf

## flytekitplugins.dask.models.WorkerGroup

Configuration for a dask worker group



### Parameters

```python
class WorkerGroup(
    number_of_workers: int,
    image: typing.Optional[str],
    resources: typing.Optional[flytekit.models.task.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `number_of_workers` | `int` | Number of workers in the group |
| `image` | `typing.Optional[str]` | Optional image to use for the pods of the worker group |
| `resources` | `typing.Optional[flytekit.models.task.Resources]` | Optional resources to use for the pods of the worker group |

### Properties

| Property | Type | Description |
|-|-|-|
| `image` | `None` |  |
| `is_empty` | `None` |  |
| `number_of_workers` | `None` |  |
| `resources` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** The dask cluster serialized to protobuf

