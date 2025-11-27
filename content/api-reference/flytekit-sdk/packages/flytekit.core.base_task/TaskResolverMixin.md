---
title: TaskResolverMixin
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskResolverMixin

**Package:** `flytekit.core.base_task`

Flytekit tasks interact with the Flyte platform very, very broadly in two steps. They need to be uploaded to Admin,
and then they are run by the user upon request (either as a single task execution or as part of a workflow). In any
case, at execution time, for most tasks (that is those that generate a container target) the container image
containing the task needs to be spun up again at which point the container needs to know which task it's supposed
to run and how to rehydrate the task object.

For example, the serialization of a simple task ::

    # in repo_root/workflows/example.py
    @task
    def t1(...) -> ...: ...

might result in a container with arguments like ::

    pyflyte-execute --inputs s3://path/inputs.pb --output-prefix s3://outputs/location         --raw-output-data-prefix /tmp/data         --resolver flytekit.core.python_auto_container.default_task_resolver         --         task-module repo_root.workflows.example task-name t1

At serialization time, the container created for the task will start out automatically with the ``pyflyte-execute``
bit, along with the requisite input/output args and the offloaded data prefix. Appended to that will be two things,

#. the ``location`` of the task's task resolver, followed by two dashes, followed by
#. the arguments provided by calling the ``loader_args`` function below.

The ``default_task_resolver`` declared below knows that

* When ``loader_args`` is called on a task, to look up the module the task is in, and the name of the task (the
  key of the task in the module, either the function name, or the variable it was assigned to).
* When ``load_task`` is called, it interprets the first part of the command as the module to call
  ``importlib.import_module`` on, and then looks for a key ``t1``.

This is just the default behavior. Users should feel free to implement their own resolvers.


## Methods

| Method | Description |
|-|-|
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.base_task.Task
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `typing.List[str]` | |

### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.base_task.Task,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `t` | `flytekit.core.base_task.Task` | |

### name()

```python
def name()
```
### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
) -> typing.Optional[str]
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type | Description |
|-|-|-|
| `t` | `flytekit.core.base_task.Task` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `location` |  |  |

