---
title: ClassDecorator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ClassDecorator

**Package:** `flytekit.core.utils`

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
class ClassDecorator(
    task_function,
    kwargs,
)
```
If the decorator is called with arguments, func will be None.
If the decorator is called without arguments, func will be function to be decorated.


| Parameter | Type | Description |
|-|-|-|
| `task_function` |  | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called. |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator. |


### execute()

```python
def execute(
    args,
    kwargs,
)
```
This method will be called when the decorated function is called.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


