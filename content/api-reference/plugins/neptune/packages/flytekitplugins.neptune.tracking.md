---
title: flytekitplugins.neptune.tracking
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.neptune.tracking

## Directory

### Methods

| Method | Description |
|-|-|
| [`neptune_init_run()`](#neptune_init_run) | Neptune plugin. |


### Variables

| Property | Type | Description |
|-|-|-|
| `NEPTUNE_RUN_VALUE` | `str` |  |

## Methods

#### neptune_init_run()

```python
def neptune_init_run(
    project: str,
    secret: typing.Union[flytekit.models.security.Secret, typing.Callable],
    host: str,
    init_run_kwargs: dict,
)
```
Neptune plugin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `secret` | `typing.Union[flytekit.models.security.Secret, typing.Callable]` |
| `host` | `str` |
| `init_run_kwargs` | `dict` |

