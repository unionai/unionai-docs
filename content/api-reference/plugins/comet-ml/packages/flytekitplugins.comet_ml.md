---
title: flytekitplugins.comet_ml
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.comet_ml

## Directory

### Methods

| Method | Description |
|-|-|
| [`comet_ml_login()`](#comet_ml_login) | Comet plugin. |


## Methods

#### comet_ml_login()

```python
def comet_ml_login(
    project_name: str,
    workspace: str,
    secret: typing.Union[flytekit.models.security.Secret, typing.Callable],
    experiment_key: typing.Optional[str],
    host: str,
    login_kwargs: dict,
)
```
Comet plugin.


| Parameter | Type | Description |
|-|-|-|
| `project_name` | `str` | Send your experiment to a specific project. (Required) |
| `workspace` | `str` | Attach an experiment to a project that belongs to this workspace. (Required) |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable]` | Secret with your `COMET_API_KEY` or a callable that returns the API key. The callable takes no arguments and returns a string. (Required) |
| `experiment_key` | `typing.Optional[str]` | Experiment key. |
| `host` | `str` | |
| `login_kwargs` | `dict` | |

