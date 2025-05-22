---
title: flytekitplugins.optuna.optimizer
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.optuna.optimizer

## Directory

### Classes

| Class | Description |
|-|-|
| [`Category`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizercategory) |  |
| [`Float`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizerfloat) |  |
| [`Integer`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizerinteger) |  |
| [`Number`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizernumber) |  |
| [`Optimizer`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizeroptimizer) |  |
| [`Suggestion`](.././flytekitplugins.optuna.optimizer#flytekitpluginsoptunaoptimizersuggestion) |  |

### Methods

| Method | Description |
|-|-|
| [`optimize()`](#optimize) |  |
| [`process()`](#process) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `P` | `ParamSpec` |  |
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

#### process()

```python
def process(
    trial: optuna.trial._trial.Trial,
    inputs: dict[str, typing.Any],
    root: typing.Optional[list[str]],
) -> dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `trial` | `optuna.trial._trial.Trial` |
| `inputs` | `dict[str, typing.Any]` |
| `root` | `typing.Optional[list[str]]` |

## flytekitplugins.optuna.optimizer.Category

```python
class Category(
    choices: list[typing.Any],
)
```
| Parameter | Type |
|-|-|
| `choices` | `list[typing.Any]` |

## flytekitplugins.optuna.optimizer.Float

```python
class Float(
    low: float,
    high: float,
    step: typing.Optional[float],
    log: bool,
)
```
| Parameter | Type |
|-|-|
| `low` | `float` |
| `high` | `float` |
| `step` | `typing.Optional[float]` |
| `log` | `bool` |

## flytekitplugins.optuna.optimizer.Integer

```python
class Integer(
    low: int,
    high: int,
    step: int,
    log: bool,
)
```
| Parameter | Type |
|-|-|
| `low` | `int` |
| `high` | `int` |
| `step` | `int` |
| `log` | `bool` |

## flytekitplugins.optuna.optimizer.Number

## flytekitplugins.optuna.optimizer.Optimizer

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

## flytekitplugins.optuna.optimizer.Suggestion

