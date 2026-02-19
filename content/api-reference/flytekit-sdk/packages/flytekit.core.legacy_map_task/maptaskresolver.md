---
title: MapTaskResolver
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# MapTaskResolver

**Package:** `flytekit.core.legacy_map_task`

Special resolver that is used for MapTasks.
This exists because it is possible that MapTasks are created using nested "partial" subtasks.
When a maptask is created its interface is interpolated from the interface of the subtask - the interpolation,
simply converts every input into a list/collection input.

For example:
  interface -&gt; (i: int, j: str) -&gt; str  =&gt; map_task interface -&gt; (i: List[int], j: List[str]) -&gt; List[str]

But in cases in which `j` is bound to a fixed value by using `functools.partial` we need a way to ensure that
the interface is not simply interpolated, but only the unbound inputs are interpolated.

```python
def foo((i: int, j: str) -> str:
    ...

mt = map_task(functools.partial(foo, j=10))

print(mt.interface)
```

output:

        (i: List[int], j: str) -&gt; List[str]

But, at runtime this information is lost. To reconstruct this, we use MapTaskResolver that records the "bound vars"
and then at runtime reconstructs the interface with this knowledge



```python
class MapTaskResolver(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Loader args should be of the form. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


### find_lhs()

```python
def find_lhs()
```
### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


### load_task()

```python
def load_task(
    loader_args: typing.List[str],
    max_concurrency: int,
) -> flytekit.core.legacy_map_task.MapPythonTask
```
Loader args should be of the form
vars "var1,var2,.." resolver "resolver" [resolver_args]


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `typing.List[str]` | |
| `max_concurrency` | `int` | |

### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.legacy_map_task.MapPythonTask,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `t` | `flytekit.core.legacy_map_task.MapPythonTask` | |

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

