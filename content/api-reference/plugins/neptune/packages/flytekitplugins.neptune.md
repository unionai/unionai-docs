---
title: flytekitplugins.neptune
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.neptune


.. currentmodule:: flytekitplugins.neptune

This package contains things that are useful when extending Flytekit.

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   neptune_scale_run

## Directory

### Methods

| Method | Description |
|-|-|
| [`neptune_scale_run()`](#neptune_scale_run) | Neptune Scale Plugin. |


## Methods

#### neptune_scale_run()

```python
def neptune_scale_run(
    project: str,
    secret: typing.Union[flytekit.models.security.Secret, typing.Callable],
    run_id: typing.Optional[str],
    experiment_name: typing.Optional[str],
    init_run_kwargs: dict,
) -> Callable[..., _neptune_scale_run_class]
```
Neptune Scale Plugin.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | Name of the project where the run should go, in the form `workspace-name/project_name`. (Required) |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable]` | Secret with your `NEPTUNE_API_KEY` or a callable that returns the API key. The callable takes no arguments and returns a string. (Required) |
| `run_id` | `typing.Optional[str]` | A unique id for this Neptune run. If not provided, Neptune will generate its own id. |
| `experiment_name` | `typing.Optional[str]` | If provided, the run will be logged as an experiment with this name. |
| `init_run_kwargs` | `dict` | |

