---
title: flyteplugins.mlflow
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# flyteplugins.mlflow

## Key features:

- Automatic MLflow run management with `@mlflow_run` decorator
- Built-in autologging support via `autolog=True` parameter
- Auto-generated MLflow UI links via `link_host` config and the `Mlflow` link class
- Parent/child task support with run sharing
- Distributed training support (only rank 0 logs to MLflow)
- Configuration management with `mlflow_config()`

## Basic usage:

1. Manual logging with `@mlflow_run`:

   ```python
   from flyteplugins.mlflow import mlflow_run, get_mlflow_run

   @mlflow_run(
       tracking_uri="http://localhost:5000",
       experiment_name="my-experiment",
       tags={"team": "ml"},
   )
   @env.task
   async def train_model(learning_rate: float) -> str:
       import mlflow

       mlflow.log_param("lr", learning_rate)
       mlflow.log_metric("loss", 0.5)

       run = get_mlflow_run()
       return run.info.run_id
   ```

2. Automatic logging with `@mlflow_run(autolog=True)`:

   ```python
   from flyteplugins.mlflow import mlflow_run

   @mlflow_run(
       autolog=True,
       framework="sklearn",
       tracking_uri="http://localhost:5000",
       log_models=True,
       log_datasets=False,
       experiment_id="846992856162999",
   )
   @env.task
   async def train_sklearn_model():
       from sklearn.linear_model import LogisticRegression

       model = LogisticRegression()
       model.fit(X, y)  # Autolog captures parameters, metrics, and model
   ```

3. Workflow-level configuration with `mlflow_config()`:

   ```python
   from flyteplugins.mlflow import mlflow_config

   r = flyte.with_runcontext(
       custom_context=mlflow_config(
           tracking_uri="http://localhost:5000",
           experiment_id="846992856162999",
           tags={"team": "ml"},
       )
   ).run(train_model, learning_rate=0.001)
   ```

4. Per-task config overrides with context manager:

   ```python
   @mlflow_run
   @env.task
   async def parent_task():
       # Override config for a specific child task
       with mlflow_config(run_mode="new", tags={"role": "child"}):
           await child_task()
   ```

5. Run modes — control run creation vs sharing:

   ```python
   @mlflow_run                      # "auto": new run if no parent, else share parent's
   @mlflow_run(run_mode="new")      # Always create a new run
   ```

6. HPO — objective can be a Flyte task with `run_mode="new"`:

   ```python
   @mlflow_run(run_mode="new")
   @env.task
   def objective(params: dict) -> float:
       mlflow.log_params(params)
       loss = train(params)
       mlflow.log_metric("loss", loss)
       return loss
   ```

7. Distributed training (only rank 0 logs):

   ```python
   @mlflow_run  # Auto-detects rank from RANK env var
   @env.task
   async def distributed_train():
       ...
   ```

8. MLflow UI links — auto-generated via `link_host`:

   ```python
   from flyteplugins.mlflow import Mlflow, mlflow_config

   # Set link_host at workflow level — children with Mlflow() link
   # auto-get the URL after the parent creates the run.
   r = flyte.with_runcontext(
       custom_context=mlflow_config(
           tracking_uri="http://localhost:5000",
           link_host="http://localhost:5000",
       )
   ).run(parent_task)

   # Attach the link to child tasks:
   @mlflow_run
   @env.task(links=[Mlflow()])
   async def child_task(): ...

   # Custom URL template (e.g. Databricks):
   mlflow_config(
       link_host="https://dbc-xxx.cloud.databricks.com",
       link_template="{host}/ml/experiments/{experiment_id}/runs/{run_id}",
   )
   ```

Decorator order: `@mlflow_run` must be outermost (before `@env.task`):

```python
@mlflow_run
@env.task
async def my_task(): ...

@mlflow_run(autolog=True, framework="sklearn")
@env.task
async def my_task(): ...
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`Mlflow`](../flyteplugins.mlflow/mlflow) | MLflow UI link for Flyte tasks. |

### Methods

| Method | Description |
|-|-|
| [`get_mlflow_context()`](#get_mlflow_context) | Retrieve current MLflow configuration from Flyte context. |
| [`get_mlflow_run()`](#get_mlflow_run) | Get the current MLflow run if within a `@mlflow_run` decorated task or trace. |
| [`mlflow_config()`](#mlflow_config) | Create MLflow configuration. |
| [`mlflow_run()`](#mlflow_run) | Decorator to manage MLflow runs for Flyte tasks and plain functions. |


## Methods

#### get_mlflow_context()

```python
def get_mlflow_context()
```
Retrieve current MLflow configuration from Flyte context.


#### get_mlflow_run()

```python
def get_mlflow_run()
```
Get the current MLflow run if within a `@mlflow_run` decorated task or trace.

The run is started when the `@mlflow_run` decorator enters.
Returns None if not within an `mlflow_run` context.



**Returns:** `mlflow.ActiveRun` | `None`: The current MLflow active run or None.

#### mlflow_config()

```python
def mlflow_config(
    tracking_uri: typing.Optional[str],
    experiment_name: typing.Optional[str],
    experiment_id: typing.Optional[str],
    run_name: typing.Optional[str],
    run_id: typing.Optional[str],
    tags: typing.Optional[dict[str, str]],
    run_mode: typing.Literal['auto', 'new', 'nested'],
    autolog: bool,
    framework: typing.Optional[str],
    log_models: typing.Optional[bool],
    log_datasets: typing.Optional[bool],
    autolog_kwargs: typing.Optional[dict[str, typing.Any]],
    link_host: typing.Optional[str],
    link_template: typing.Optional[str],
    kwargs: **kwargs,
) -> flyteplugins.mlflow._context._MLflowConfig
```
Create MLflow configuration.

Works in two contexts:
1. With `flyte.with_runcontext()` for global configuration
2. As a context manager to override configuration



| Parameter | Type | Description |
|-|-|-|
| `tracking_uri` | `typing.Optional[str]` | MLflow tracking server URI. |
| `experiment_name` | `typing.Optional[str]` | MLflow experiment name. |
| `experiment_id` | `typing.Optional[str]` | MLflow experiment ID. |
| `run_name` | `typing.Optional[str]` | Human-readable run name. |
| `run_id` | `typing.Optional[str]` | Explicit MLflow run ID. |
| `tags` | `typing.Optional[dict[str, str]]` | MLflow run tags. |
| `run_mode` | `typing.Literal['auto', 'new', 'nested']` | Flyte-specific run mode ("auto", "new", "nested"). |
| `autolog` | `bool` | Enable MLflow autologging. |
| `framework` | `typing.Optional[str]` | Framework-specific autolog (e.g. "sklearn", "pytorch"). |
| `log_models` | `typing.Optional[bool]` | Whether to log models automatically. |
| `log_datasets` | `typing.Optional[bool]` | Whether to log datasets automatically. |
| `autolog_kwargs` | `typing.Optional[dict[str, typing.Any]]` | Extra parameters passed to mlflow.autolog(). |
| `link_host` | `typing.Optional[str]` | MLflow UI host for auto-generating task links. |
| `link_template` | `typing.Optional[str]` | Custom URL template. Defaults to standard MLflow UI format. Available placeholders: `{host}`, `{experiment_id}`, `{run_id}`. |
| `kwargs` | `**kwargs` | |

#### mlflow_run()

```python
def mlflow_run(
    _func: typing.Optional[~F],
    run_mode: typing.Literal['auto', 'new', 'nested'],
    tracking_uri: typing.Optional[str],
    experiment_name: typing.Optional[str],
    experiment_id: typing.Optional[str],
    run_name: typing.Optional[str],
    run_id: typing.Optional[str],
    tags: typing.Optional[dict[str, str]],
    autolog: bool,
    framework: typing.Optional[str],
    log_models: typing.Optional[bool],
    log_datasets: typing.Optional[bool],
    autolog_kwargs: typing.Optional[dict[str, typing.Any]],
    rank: typing.Optional[int],
    kwargs,
) -> ~F
```
Decorator to manage MLflow runs for Flyte tasks and plain functions.

Handles both manual logging and autologging. For autologging, pass
`autolog=True` and optionally `framework` to select a specific
framework (e.g. `"sklearn"`).

Decorator Order:
    @mlflow_run must be the outermost decorator::

        @mlflow_run
        @env.task
        async def my_task():
            ...


| Parameter | Type | Description |
|-|-|-|
| `_func` | `typing.Optional[~F]` | |
| `run_mode` | `typing.Literal['auto', 'new', 'nested']` | "auto" (default), "new", or "nested". - "auto": reuse parent run if available, else create new. - "new": always create a new independent run. - "nested": create a new run nested under the parent via   `mlflow.parentRunId` tag. Works across processes/containers. |
| `tracking_uri` | `typing.Optional[str]` | MLflow tracking server URL. |
| `experiment_name` | `typing.Optional[str]` | MLflow experiment name (exclusive with experiment_id). |
| `experiment_id` | `typing.Optional[str]` | MLflow experiment ID (exclusive with experiment_name). |
| `run_name` | `typing.Optional[str]` | Human-readable run name (exclusive with run_id). |
| `run_id` | `typing.Optional[str]` | MLflow run ID (exclusive with run_name). |
| `tags` | `typing.Optional[dict[str, str]]` | Dictionary of tags for the run. |
| `autolog` | `bool` | Enable MLflow autologging. |
| `framework` | `typing.Optional[str]` | MLflow framework name for autolog (e.g. "sklearn", "pytorch"). |
| `log_models` | `typing.Optional[bool]` | Whether to log models automatically (requires autolog). |
| `log_datasets` | `typing.Optional[bool]` | Whether to log datasets automatically (requires autolog). |
| `autolog_kwargs` | `typing.Optional[dict[str, typing.Any]]` | Extra parameters passed to `mlflow.autolog()`. |
| `rank` | `typing.Optional[int]` | Process rank for distributed training (only rank 0 logs). |
| `kwargs` | `**kwargs` | |

