---
title: ToolTaskResolver
description: "Resolver for a task shadowed at module scope by a tool wrapper."
icon: braces
version: 2.7.1
variants: +flyte +union
layout: py_api
---

# ToolTaskResolver

**Package:** `flyteplugins.agents.core`

Resolver for a task shadowed at module scope by a tool wrapper.

Recovers the underlying task via the wrapper's `__wrapped_task__` hook so
the worker runs the task's own body instead of re-dispatching the tool.


## Properties

| Property | Type | Description |
|-|-|-|
| `import_path` | `str` | The import path of the resolver. This should be a valid python import path. |

## Methods

| Method | Description |
|-|-|
| [`load_app_env()`](#load_app_env) | Given the set of identifier keys, should return one AppEnvironment or raise an error if not found. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one TaskTemplate or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter TaskTemplate. |


### load_app_env()

```python
def load_app_env(
    loader_args: str,
) -> AppEnvironment
```
Given the set of identifier keys, should return one AppEnvironment or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `str` | |

### load_task()

```python
def load_task(
    loader_args,
)
```
Given the set of identifier keys, should return one TaskTemplate or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` |  | |

### loader_args()

```python
def loader_args(
    task: flyte._task.TaskTemplate,
    root_dir: pathlib.Path,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter TaskTemplate. Each string should not have
spaces or special characters. This is used to identify the task in the resolver.


| Parameter | Type | Description |
|-|-|-|
| `task` | `flyte._task.TaskTemplate` | |
| `root_dir` | `pathlib.Path` | |

