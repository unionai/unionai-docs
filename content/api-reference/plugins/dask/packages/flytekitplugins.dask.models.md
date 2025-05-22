---
title: flytekitplugins.dask.models
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
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



```python
class DaskJob(
    scheduler: flytekitplugins.dask.models.Scheduler,
    workers: flytekitplugins.dask.models.WorkerGroup,
)
```
| Parameter | Type |
|-|-|
| `scheduler` | `flytekitplugins.dask.models.Scheduler` |
| `workers` | `flytekitplugins.dask.models.WorkerGroup` |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :return: The dask job serialized to protobuf. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
:return: The dask job serialized to protobuf


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `scheduler` |  | {{< multiline >}}:return: Configuration for the scheduler pod
{{< /multiline >}} |
| `workers` |  | {{< multiline >}}:return: Configuration of the default worker group
{{< /multiline >}} |

## flytekitplugins.dask.models.Scheduler

Configuration for the scheduler pod



```python
class Scheduler(
    image: typing.Optional[str],
    resources: typing.Optional[flytekit.models.task.Resources],
)
```
| Parameter | Type |
|-|-|
| `image` | `typing.Optional[str]` |
| `resources` | `typing.Optional[flytekit.models.task.Resources]` |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :return: The scheduler spec serialized to protobuf. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
:return: The scheduler spec serialized to protobuf


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `image` |  | {{< multiline >}}:return: The optional image for the scheduler pod
{{< /multiline >}} |
| `is_empty` |  |  |
| `resources` |  | {{< multiline >}}:return: Optional resources for the scheduler pod
{{< /multiline >}} |

## flytekitplugins.dask.models.WorkerGroup

Configuration for a dask worker group



```python
class WorkerGroup(
    number_of_workers: int,
    image: typing.Optional[str],
    resources: typing.Optional[flytekit.models.task.Resources],
)
```
| Parameter | Type |
|-|-|
| `number_of_workers` | `int` |
| `image` | `typing.Optional[str]` |
| `resources` | `typing.Optional[flytekit.models.task.Resources]` |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :return: The dask cluster serialized to protobuf. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
:return: The dask cluster serialized to protobuf


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `image` |  | {{< multiline >}}:return: The optional image to use for the worker pods
{{< /multiline >}} |
| `is_empty` |  |  |
| `number_of_workers` |  | {{< multiline >}}:return: Optional number of workers for the worker group
{{< /multiline >}} |
| `resources` |  | {{< multiline >}}:return: Optional resources to use for the worker pods
{{< /multiline >}} |

