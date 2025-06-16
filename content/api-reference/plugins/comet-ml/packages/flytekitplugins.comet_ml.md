---
title: flytekitplugins.comet_ml
version: 0.0.0+develop
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


| Parameter | Type |
|-|-|
| `project_name` | `str` |
| `workspace` | `str` |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable]` |
| `experiment_key` | `typing.Optional[str]` |
| `host` | `str` |
| `login_kwargs` | `dict` |

