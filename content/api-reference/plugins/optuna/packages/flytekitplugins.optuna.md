---
title: flytekitplugins.optuna
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.optuna

## Directory

### Classes

| Class | Description |
|-|-|
| [`Optimizer`](.././flytekitplugins.optuna#flytekitpluginsoptunaoptimizer) |  |

### Methods

| Method | Description |
|-|-|
| [`optimize()`](#optimize) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `suggest` | `SimpleNamespace` |  |

## Methods

#### optimize()

```python
def optimize(
    objective: typing.Union[typing.Callable[typing.Concatenate[optuna.trial._trial.Trial, ~P], typing.Union[typing.Awaitable[typing.Union[float, tuple[float, ...]]], float, tuple[float, ...]]], flytekit.core.python_function_task.AsyncPythonFunctionTask, NoneType],
    concurrency: int,
    n_trials: int,
    study: typing.Optional[optuna.study.study.Study],
)
```
| Parameter | Type |
|-|-|
| `objective` | `typing.Union[typing.Callable[typing.Concatenate[optuna.trial._trial.Trial, ~P], typing.Union[typing.Awaitable[typing.Union[float, tuple[float, ...]]], float, tuple[float, ...]]], flytekit.core.python_function_task.AsyncPythonFunctionTask, NoneType]` |
| `concurrency` | `int` |
| `n_trials` | `int` |
| `study` | `typing.Optional[optuna.study.study.Study]` |

## flytekitplugins.optuna.Optimizer

```python
class Optimizer(
    objective: typing.Union[typing.Callable[typing.Concatenate[optuna.trial._trial.Trial, ~P], typing.Union[typing.Awaitable[typing.Union[float, tuple[float, ...]]], float, tuple[float, ...]]], flytekit.core.python_function_task.AsyncPythonFunctionTask],
    concurrency: int,
    n_trials: int,
    study: typing.Optional[optuna.study.study.Study],
    delay: int,
)
```
| Parameter | Type |
|-|-|
| `objective` | `typing.Union[typing.Callable[typing.Concatenate[optuna.trial._trial.Trial, ~P], typing.Union[typing.Awaitable[typing.Union[float, tuple[float, ...]]], float, tuple[float, ...]]], flytekit.core.python_function_task.AsyncPythonFunctionTask]` |
| `concurrency` | `int` |
| `n_trials` | `int` |
| `study` | `typing.Optional[optuna.study.study.Study]` |
| `delay` | `int` |

### Methods

| Method | Description |
|-|-|
| [`spawn()`](#spawn) |  |


#### spawn()

```python
def spawn(
    semaphore: asyncio.locks.Semaphore,
    inputs: dict[str, typing.Any],
)
```
| Parameter | Type |
|-|-|
| `semaphore` | `asyncio.locks.Semaphore` |
| `inputs` | `dict[str, typing.Any]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_imperative` |  |  |

