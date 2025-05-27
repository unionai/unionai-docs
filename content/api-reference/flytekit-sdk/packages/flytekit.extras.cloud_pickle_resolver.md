---
title: flytekit.extras.cloud_pickle_resolver
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.cloud_pickle_resolver

## Directory

### Classes

| Class | Description |
|-|-|
| [`ExperimentalNaiveCloudPickleResolver`](.././flytekit.extras.cloud_pickle_resolver#flytekitextrascloud_pickle_resolverexperimentalnaivecloudpickleresolver) | Please do not use this resolver, basically ever. |

### Variables

| Property | Type | Description |
|-|-|-|
| `experimental_cloud_pickle_resolver` | `ExperimentalNaiveCloudPickleResolver` |  |

## flytekit.extras.cloud_pickle_resolver.ExperimentalNaiveCloudPickleResolver

Please do not use this resolver, basically ever. This is here for demonstration purposes only. The critical flaw
of this resolver is that pretty much any task that it resolves results in loader_args that are enormous. This
payload is serialized as part of the ``TaskTemplate`` protobuf object and will live in Admin and then be loaded
into Flyte Propeller memory and will pretty much clog up performance along the entire platform.

TODO: Replace this with a version that will upload the data to S3 or some other durable store upon ``loader_args``
  and will download the data upon ``load_task``. This will require additional changes to Admin however.


```python
class ExperimentalNaiveCloudPickleResolver(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
) -> typing.Optional[str]
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

