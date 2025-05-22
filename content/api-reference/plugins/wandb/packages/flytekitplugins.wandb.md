---
title: flytekitplugins.wandb
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.wandb


.. currentmodule:: flytekitplugins.wandb

This package contains things that are useful when extending Flytekit.

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   wandb_init

## Directory

### Classes

| Class | Description |
|-|-|
| [`wandb_init`](.././flytekitplugins.wandb#flytekitpluginswandbwandb_init) | Abstract class for class decorators. |

## flytekitplugins.wandb.wandb_init

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
class wandb_init(
    task_function: typing.Optional[typing.Callable],
    project: typing.Optional[str],
    entity: typing.Optional[str],
    secret: typing.Union[flytekit.models.security.Secret, typing.Callable, NoneType],
    id: typing.Optional[str],
    host: str,
    api_host: str,
    init_kwargs: dict,
)
```
Weights and Biases plugin.


| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `project` | `typing.Optional[str]` |
| `entity` | `typing.Optional[str]` |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable, NoneType]` |
| `id` | `typing.Optional[str]` |
| `host` | `str` |
| `api_host` | `str` |
| `init_kwargs` | `dict` |

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called. |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator. |


#### execute()

```python
def execute(
    args,
    kwargs,
)
```
This method will be called when the decorated function is called.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


