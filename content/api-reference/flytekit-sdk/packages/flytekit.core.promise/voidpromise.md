---
title: VoidPromise
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# VoidPromise

**Package:** `flytekit.core.promise`

This object is returned for tasks that do not return any outputs (declared interface is empty)
VoidPromise cannot be interacted with and does not allow comparisons or any operations



```python
class VoidPromise(
    task_name: str,
    ref: Optional[NodeOutput],
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_name` | `str` | |
| `ref` | `Optional[NodeOutput]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `ref` | `None` |  |
| `task_name` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is a placeholder and should do nothing. |
| [`with_overrides()`](#with_overrides) |  |


### runs_before()

```python
def runs_before(
    args,
    kwargs,
)
```
This is a placeholder and should do nothing. It is only here to enable local execution of workflows
where a task returns nothing.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### with_overrides()

```python
def with_overrides(
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

