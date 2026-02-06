---
title: flyteplugins.wandb
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.wandb


## Key features:

- Automatic W&B run initialization with `@wandb_init` decorator
- Automatic W&B links in Flyte UI pointing to runs and sweeps
- Parent/child task support with automatic run reuse
- W&B sweep creation and management with `@wandb_sweep` decorator
- Configuration management with `wandb_config()` and `wandb_sweep_config()`

## Basic usage:

1. Simple task with W&B logging:

   ```python
   from flyteplugins.wandb import wandb_init, get_wandb_run

   @wandb_init(project="my-project", entity="my-team")
   @env.task
   async def train_model(learning_rate: float) -> str:
       wandb_run = get_wandb_run()
       wandb_run.log({"loss": 0.5, "learning_rate": learning_rate})
       return wandb_run.id
   ```

2. Parent/Child Tasks with Run Reuse:

   ```python
   @wandb_init  # Automatically reuses parent's run ID
   @env.task
   async def child_task(x: int) -> str:
       wandb_run = get_wandb_run()
       wandb_run.log({"child_metric": x * 2})
       return wandb_run.id

   @wandb_init(project="my-project", entity="my-team")
   @env.task
   async def parent_task() -> str:
       wandb_run = get_wandb_run()
       wandb_run.log({"parent_metric": 100})

       # Child reuses parent's run by default (run_mode="auto")
       await child_task(5)
       return wandb_run.id
   ```

3. Configuration with context manager:

   ```python
   from flyteplugins.wandb import wandb_config

   r = flyte.with_runcontext(
       custom_context=wandb_config(
           project="my-project",
           entity="my-team",
           tags=["experiment-1"]
       )
   ).run(train_model, learning_rate=0.001)
   ```

4. Creating new runs for child tasks:

   ```python
   @wandb_init(run_mode="new")  # Always creates a new run
   @env.task
   async def independent_child() -> str:
       wandb_run = get_wandb_run()
       wandb_run.log({"independent_metric": 42})
       return wandb_run.id
   ```

5. Running sweep agents in parallel:

   ```python
   import asyncio
   from flyteplugins.wandb import wandb_sweep, get_wandb_sweep_id, get_wandb_context

   @wandb_init
   async def objective():
       wandb_run = wandb.run
       config = wandb_run.config
       ...

       wandb_run.log({"loss": loss_value})

   @wandb_sweep
   @env.task
   async def sweep_agent(agent_id: int, sweep_id: str, count: int = 5) -> int:
       wandb.agent(sweep_id, function=objective, count=count, project=get_wandb_context().project)
       return agent_id

   @wandb_sweep
   @env.task
   async def run_parallel_sweep(num_agents: int = 2, trials_per_agent: int = 5) -> str:
       sweep_id = get_wandb_sweep_id()

       # Launch agents in parallel
       agent_tasks = [
           sweep_agent(agent_id=i + 1, sweep_id=sweep_id, count=trials_per_agent)
           for i in range(num_agents)
       ]

       # Wait for all agents to complete
       await asyncio.gather(*agent_tasks)
       return sweep_id

   # Run with 2 parallel agents
   r = flyte.with_runcontext(
       custom_context={
           **wandb_config(project="my-project", entity="my-team"),
           **wandb_sweep_config(
               method="random",
               metric={"name": "loss", "goal": "minimize"},
               parameters={
                   "learning_rate": {"min": 0.0001, "max": 0.1},
                   "batch_size": {"values": [16, 32, 64]},
               }
           )
       }
   ).run(run_parallel_sweep, num_agents=2, trials_per_agent=5)
   ```

Decorator order: `@wandb_init` or `@wandb_sweep` must be the outermost decorator:

```python
@wandb_init
@env.task
async def my_task():
    ...
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`Wandb`](../flyteplugins.wandb/wandb) | Generates a Weights & Biases run link. |
| [`WandbSweep`](../flyteplugins.wandb/wandbsweep) | Generates a Weights & Biases Sweep link. |

### Methods

| Method | Description |
|-|-|
| [`download_wandb_run_dir()`](#download_wandb_run_dir) | Download wandb run data from wandb cloud. |
| [`download_wandb_run_logs()`](#download_wandb_run_logs) | Traced function to download wandb run logs after task completion. |
| [`download_wandb_sweep_dirs()`](#download_wandb_sweep_dirs) | Download all run data for a wandb sweep. |
| [`download_wandb_sweep_logs()`](#download_wandb_sweep_logs) | Traced function to download wandb sweep logs after task completion. |
| [`get_wandb_context()`](#get_wandb_context) | Get wandb config from current Flyte context. |
| [`get_wandb_run()`](#get_wandb_run) | Get the current wandb run if within a `@wandb_init` decorated task or trace. |
| [`get_wandb_run_dir()`](#get_wandb_run_dir) | Get the local directory path for the current wandb run. |
| [`get_wandb_sweep_context()`](#get_wandb_sweep_context) | Get wandb sweep config from current Flyte context. |
| [`get_wandb_sweep_id()`](#get_wandb_sweep_id) | Get the current wandb `sweep_id` if within a `@wandb_sweep` decorated task. |
| [`wandb_config()`](#wandb_config) | Create wandb configuration. |
| [`wandb_init()`](#wandb_init) | Decorator to automatically initialize wandb for Flyte tasks and wandb sweep objectives. |
| [`wandb_sweep()`](#wandb_sweep) | Decorator to create a wandb sweep and make `sweep_id` available. |
| [`wandb_sweep_config()`](#wandb_sweep_config) | Create wandb sweep configuration for hyperparameter optimization. |


## Methods

#### download_wandb_run_dir()

```python
def download_wandb_run_dir(
    run_id: typing.Optional[str],
    path: typing.Optional[str],
    include_history: bool,
) -> str
```
Download wandb run data from wandb cloud.

Downloads all run files and optionally exports metrics history to JSON.
This enables access to wandb data from any task or after workflow completion.

Downloaded contents:

    - summary.json - final summary metrics (always exported)
    - metrics_history.json - step-by-step metrics (if include_history=True)
    - Plus any files synced by wandb (requirements.txt, wandb_metadata.json, etc.)



| Parameter | Type | Description |
|-|-|-|
| `run_id` | `typing.Optional[str]` | The wandb run ID to download. If `None`, uses the current run's ID from context (useful for shared runs across tasks). |
| `path` | `typing.Optional[str]` | Local directory to download files to. If `None`, downloads to `/tmp/wandb_runs/{run_id}`. |
| `include_history` | `bool` | If `True`, exports the step-by-step metrics history to `metrics_history.json`. Defaults to `True`. |

#### download_wandb_run_logs()

```python
def download_wandb_run_logs(
    run_id: str,
) -> flyte.io._dir.Dir
```
Traced function to download wandb run logs after task completion.

This function is called automatically when `download_logs=True` is set
in `@wandb_init` or `wandb_config()`. The downloaded files appear as a
trace output in the Flyte UI.



| Parameter | Type | Description |
|-|-|-|
| `run_id` | `str` | The wandb run ID to download. |

#### download_wandb_sweep_dirs()

```python
def download_wandb_sweep_dirs(
    sweep_id: typing.Optional[str],
    base_path: typing.Optional[str],
    include_history: bool,
) -> list[str]
```
Download all run data for a wandb sweep.

Queries the wandb API for all runs in the sweep and downloads their files
and metrics history. This is useful for collecting results from all sweep
trials after completion.



| Parameter | Type | Description |
|-|-|-|
| `sweep_id` | `typing.Optional[str]` | The wandb sweep ID. If `None`, uses the current sweep's ID from context (set by `@wandb_sweep` decorator). |
| `base_path` | `typing.Optional[str]` | Base directory to download files to. Each run's files will be in a subdirectory named by run_id. If `None`, uses `/tmp/wandb_runs/`. |
| `include_history` | `bool` | If `True`, exports the step-by-step metrics history to metrics_history.json for each run. Defaults to `True`. |

#### download_wandb_sweep_logs()

```python
def download_wandb_sweep_logs(
    sweep_id: str,
) -> flyte.io._dir.Dir
```
Traced function to download wandb sweep logs after task completion.

This function is called automatically when `download_logs=True` is set
in `@wandb_sweep` or `wandb_sweep_config()`. The downloaded files appear as a
trace output in the Flyte UI.



| Parameter | Type | Description |
|-|-|-|
| `sweep_id` | `str` | The wandb sweep ID to download. |

#### get_wandb_context()

```python
def get_wandb_context()
```
Get wandb config from current Flyte context.


#### get_wandb_run()

```python
def get_wandb_run()
```
Get the current wandb run if within a `@wandb_init` decorated task or trace.

The run is initialized when the `@wandb_init` context manager is entered.
Returns None if not within a `wandb_init` context.

Returns:
    `wandb.sdk.wandb_run.Run` | `None`: The current wandb run object or None.


#### get_wandb_run_dir()

```python
def get_wandb_run_dir()
```
Get the local directory path for the current wandb run.

Use this for accessing files written by the current task without any
network calls. For accessing files from other tasks (or after a task
completes), use `download_wandb_run_dir()` instead.

Returns:
    Local path to wandb run directory (`wandb.run.dir`) or `None` if no
    active run.


#### get_wandb_sweep_context()

```python
def get_wandb_sweep_context()
```
Get wandb sweep config from current Flyte context.


#### get_wandb_sweep_id()

```python
def get_wandb_sweep_id()
```
Get the current wandb `sweep_id` if within a `@wandb_sweep` decorated task.

Returns `None` if not within a `wandb_sweep` context.

Returns:
    `str` | `None`: The sweep ID or None.


#### wandb_config()

```python
def wandb_config(
    project: typing.Optional[str],
    entity: typing.Optional[str],
    id: typing.Optional[str],
    name: typing.Optional[str],
    tags: typing.Optional[list[str]],
    config: typing.Optional[dict[str, typing.Any]],
    mode: typing.Optional[str],
    group: typing.Optional[str],
    run_mode: typing.Literal['auto', 'new', 'shared'],
    download_logs: bool,
    kwargs: **kwargs,
) -> flyteplugins.wandb._context._WandBConfig
```
Create wandb configuration.

This function works in two contexts:
1. With `flyte.with_runcontext()` - sets global wandb config
2. As a context manager - overrides config for specific tasks



| Parameter | Type | Description |
|-|-|-|
| `project` | `typing.Optional[str]` | W&B project name |
| `entity` | `typing.Optional[str]` | W&B entity (team or username) |
| `id` | `typing.Optional[str]` | Unique run id (auto-generated if not provided) |
| `name` | `typing.Optional[str]` | Human-readable run name |
| `tags` | `typing.Optional[list[str]]` | List of tags for organizing runs |
| `config` | `typing.Optional[dict[str, typing.Any]]` | Dictionary of hyperparameters |
| `mode` | `typing.Optional[str]` | "online", "offline" or "disabled" |
| `group` | `typing.Optional[str]` | Group name for related runs |
| `run_mode` | `typing.Literal['auto', 'new', 'shared']` | Flyte-specific run mode - "auto", "new" or "shared". Controls whether tasks create new W&B runs or share existing ones |
| `download_logs` | `bool` | If `True`, downloads wandb run files after task completes and shows them as a trace output in the Flyte UI |
| `kwargs` | `**kwargs` | |

#### wandb_init()

```python
def wandb_init(
    _func: typing.Optional[~F],
    run_mode: typing.Literal['auto', 'new', 'shared'],
    download_logs: typing.Optional[bool],
    project: typing.Optional[str],
    entity: typing.Optional[str],
    kwargs,
) -> ~F
```
Decorator to automatically initialize wandb for Flyte tasks and wandb sweep objectives.



| Parameter | Type | Description |
|-|-|-|
| `_func` | `typing.Optional[~F]` | |
| `run_mode` | `typing.Literal['auto', 'new', 'shared']` | |
| `download_logs` | `typing.Optional[bool]` | If `True`, downloads wandb run files after task completes and shows them as a trace output in the Flyte UI. If None, uses the value from `wandb_config()` context if set. |
| `project` | `typing.Optional[str]` | W&B project name (overrides context config if provided) |
| `entity` | `typing.Optional[str]` | W&B entity/team name (overrides context config if provided) |
| `kwargs` | `**kwargs` | |

#### wandb_sweep()

```python
def wandb_sweep(
    _func: typing.Optional[~F],
    project: typing.Optional[str],
    entity: typing.Optional[str],
    download_logs: typing.Optional[bool],
    kwargs,
) -> ~F
```
Decorator to create a wandb sweep and make `sweep_id` available.

This decorator:
1. Creates a wandb sweep using config from context
2. Makes `sweep_id` available via `get_wandb_sweep_id()`
3. Automatically adds a W&B sweep link to the task
4. Optionally downloads all sweep run logs as a trace output (if `download_logs=True`)



| Parameter | Type | Description |
|-|-|-|
| `_func` | `typing.Optional[~F]` | |
| `project` | `typing.Optional[str]` | W&B project name (overrides context config if provided) |
| `entity` | `typing.Optional[str]` | W&B entity/team name (overrides context config if provided) |
| `download_logs` | `typing.Optional[bool]` | if `True`, downloads all sweep run files after task completes and shows them as a trace output in the Flyte UI. If None, uses the value from wandb_sweep_config() context if set. |
| `kwargs` | `**kwargs` | |

#### wandb_sweep_config()

```python
def wandb_sweep_config(
    method: typing.Optional[str],
    metric: typing.Optional[dict[str, typing.Any]],
    parameters: typing.Optional[dict[str, typing.Any]],
    project: typing.Optional[str],
    entity: typing.Optional[str],
    prior_runs: typing.Optional[list[str]],
    name: typing.Optional[str],
    download_logs: bool,
    kwargs: **kwargs,
) -> flyteplugins.wandb._context._WandBSweepConfig
```
Create wandb sweep configuration for hyperparameter optimization.



| Parameter | Type | Description |
|-|-|-|
| `method` | `typing.Optional[str]` | Sweep method (e.g., "random", "grid", "bayes") |
| `metric` | `typing.Optional[dict[str, typing.Any]]` | |
| `parameters` | `typing.Optional[dict[str, typing.Any]]` | Parameter definitions for the sweep |
| `project` | `typing.Optional[str]` | W&B project for the sweep |
| `entity` | `typing.Optional[str]` | W&B entity for the sweep |
| `prior_runs` | `typing.Optional[list[str]]` | List of prior run IDs to include in the sweep analysis |
| `name` | `typing.Optional[str]` | Sweep name (auto-generated as `{run_name}-{action_name}` if not provided) |
| `download_logs` | `bool` | If `True`, downloads all sweep run files after task completes and shows them as a trace output in the Flyte UI |
| `kwargs` | `**kwargs` | |

