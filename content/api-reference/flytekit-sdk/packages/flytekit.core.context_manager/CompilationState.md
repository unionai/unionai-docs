---
title: CompilationState
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CompilationState

**Package:** `flytekit.core.context_manager`

Compilation state is used during the compilation of a workflow or task. It stores the nodes that were
created when walking through the workflow graph.

Attributes:
    prefix (str): This is because we may one day want to be able to have subworkflows inside other workflows. If
        users choose to not specify their node names, then we can end up with multiple "n0"s. This prefix allows
        us to give those nested nodes a distinct name, as well as properly identify them in the workflow.
    mode (int): refer to `flytekit.extend.ExecutionState.Mode`
    task_resolver (Optional[TaskResolverMixin]): Please see `flytekit.extend.TaskResolverMixin`
    nodes (Optional[List]): Stores currently compiled nodes so far.


```python
class CompilationState(
    prefix: str,
    mode: int,
    task_resolver: Optional[TaskResolverMixin],
    nodes: List,
)
```
| Parameter | Type | Description |
|-|-|-|
| `prefix` | `str` | |
| `mode` | `int` | |
| `task_resolver` | `Optional[TaskResolverMixin]` | |
| `nodes` | `List` | |

## Methods

| Method | Description |
|-|-|
| [`add_node()`](#add_node) |  |
| [`with_params()`](#with_params) | Create a new CompilationState where the mode and task resolver are defaulted to the current object, but they. |


### add_node()

```python
def add_node(
    n: Node,
)
```
| Parameter | Type | Description |
|-|-|-|
| `n` | `Node` | |

### with_params()

```python
def with_params(
    prefix: str,
    mode: Optional[int],
    resolver: Optional[TaskResolverMixin],
    nodes: Optional[List],
) -> CompilationState
```
Create a new CompilationState where the mode and task resolver are defaulted to the current object, but they
and all other args are taken if explicitly provided as an argument.

Usage:
    s.with_params("p", nodes=[])


| Parameter | Type | Description |
|-|-|-|
| `prefix` | `str` | |
| `mode` | `Optional[int]` | |
| `resolver` | `Optional[TaskResolverMixin]` | |
| `nodes` | `Optional[List]` | |

