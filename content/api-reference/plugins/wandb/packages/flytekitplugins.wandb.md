---
title: flytekitplugins.wandb
version: 1.16.14
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
| [`wandb_init`](.././flytekitplugins.wandb#flytekitpluginswandbwandb_init) |  |

## flytekitplugins.wandb.wandb_init

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


| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Optional[typing.Callable]` | The user function to be decorated. Defaults to None. |
| `project` | `typing.Optional[str]` | The name of the project where you're sending the new run. (Required) |
| `entity` | `typing.Optional[str]` | An entity is a username or team name where you're sending runs. (Required) |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable, NoneType]` | Secret with your `WANDB_API_KEY` or a callable that returns the API key. The callable takes no arguments and returns a string. (Required) |
| `id` | `typing.Optional[str]` | A unique id for this wandb run. |
| `host` | `str` | |
| `api_host` | `str` | |
| `init_kwargs` | `dict` | |

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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


