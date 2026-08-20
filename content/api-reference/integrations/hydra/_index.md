---
title: Hydra
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# Hydra



flyteplugins-hydra — Hydra launcher plugin for Flyte.

Provides three entry points for running Flyte tasks via Hydra:

1. **`@hydra.main` + `--multirun`** (standard Hydra CLI pattern):

```bash
python train.py hydra/launcher=flyte hydra.launcher.mode=remote
python train.py --multirun hydra/launcher=flyte hydra.launcher.mode=remote \
    optimizer.lr=0.001,0.01,0.1
```

2. **`flyte hydra run`** (Flyte CLI extension, no `@hydra.main` required):

```bash
flyte hydra run --config-path conf --config-name training --mode remote \
    train.py pipeline --cfg optimizer.lr=0.01
```

3. **`hydra_run` / `hydra_sweep`** (Python SDK):

```python
from flyteplugins.hydra import hydra_run, hydra_sweep

hydra_run(pipeline, config_path="conf", config_name="training",
          overrides=["optimizer.lr=0.01"], mode="remote")

runs = hydra_sweep(pipeline, config_path="conf", config_name="training",
                   overrides=["optimizer.lr=0.001,0.01,0.1"], mode="remote")
```
## Directory

### Methods

| Method | Description |
|-|-|
| [`apply_task_env()`](#apply_task_env) | Return task with Hydra task-env overrides applied. |
| [`hydra_run()`](#hydra_run) | Run a single Flyte task with a Hydra-composed config. |
| [`hydra_sweep()`](#hydra_sweep) | Run a Hydra sweep, one Flyte execution per override combination. |


## Methods

#### apply_task_env()

```python
def apply_task_env(
    task: Callable,
    cfg: DictConfig | Mapping[str, Any],
    task_env_key: str = 'task_env',
    task_name: str | None = None,
) -> Callable
```
Return task with Hydra task-env overrides applied.

The launcher calls this for the entry task automatically. User code can call
it for child tasks to get the same resources and prebuilt-image handling
before invoking the task.


| Parameter | Type | Description |
|-|-|-|
| `task` | `Callable` | |
| `cfg` | `DictConfig \| Mapping[str, Any]` | |
| `task_env_key` | `str` | |
| `task_name` | `str \| None` | |

#### hydra_run()

```python
def hydra_run(
    task: Callable,
    config_path: str | Path | None = None,
    config_name: str = 'config',
    overrides: list[str] | None = None,
    mode: str = 'remote',
    wait: bool = True,
    wait_max_workers: int | None = 32,
    run_options: dict[str, Any] | None = None,
    task_env_key: str = 'task_env',
    **kwargs: Any,
) -> Any
```
Run a single Flyte task with a Hydra-composed config.



| Parameter | Type | Description |
|-|-|-|
| `task` | `Callable` | Flyte task that accepts a `cfg: DictConfig` parameter. |
| `config_path` | `str \| Path \| None` | Path to the config directory. `None` for structured-config-only use. |
| `config_name` | `str` | Top-level config file name (without `.yaml`). |
| `overrides` | `list[str] \| None` | Hydra override strings, e.g. `["optimizer.lr=0.01"]`. |
| `mode` | `str` | `"remote"` (default) or `"local"`. |
| `wait` | `bool` | Whether to wait for remote Flyte runs to reach a terminal phase. |
| `wait_max_workers` | `int \| None` | Max worker threads used to wait for remote runs. |
| `run_options` | `dict[str, Any] \| None` | Optional dict of kwargs forwarded to `flyte.with_runcontext` (e.g. `service_account`, `name`, `copy_style`, `raw_data_path`). |
| `task_env_key` | `str` | Config key containing entry-task `task.override` kwargs, nested under the launched task's name. Child task overrides must be applied by user code. |
| `**kwargs` | `Any` | |

**Returns**

The task result. Waited remote runs return a wrapper with `url` and
the resolved task output.

#### hydra_sweep()

```python
def hydra_sweep(
    task: Callable,
    config_path: str | Path | None = None,
    config_name: str = 'config',
    overrides: list[str] | None = None,
    mode: str = 'remote',
    wait: bool = True,
    wait_max_workers: int | None = 32,
    run_options: dict[str, Any] | None = None,
    task_env_key: str = 'task_env',
    **kwargs: Any,
) -> list[Any]
```
Run a Hydra sweep, one Flyte execution per override combination.

Comma-separated values in `overrides` are expanded into a Cartesian
product. For example:

```python
overrides=["optimizer.lr=0.001,0.01,0.1", "training.epochs=10,20"]
```

produces six executions.

Custom sweepers (e.g. Optuna) are supported — include sweeper overrides
directly in the `overrides` list:

```python
overrides=[
    "hydra/sweeper=optuna", "hydra.sweeper.n_trials=20",
    "hydra.sweeper.n_jobs=4",
    "optimizer.lr=interval(1e-4,1e-1)",
]
```

When a custom sweeper is detected, the full Hydra runtime is used so the
sweeper plugin is properly discovered and invoked.



| Parameter | Type | Description |
|-|-|-|
| `task` | `Callable` | Flyte task that accepts a `cfg: DictConfig` parameter. |
| `config_path` | `str \| Path \| None` | Path to the config directory. |
| `config_name` | `str` | Top-level config file name (without `.yaml`). |
| `overrides` | `list[str] \| None` | Hydra sweep override strings (app-level and/or hydra-namespace). |
| `mode` | `str` | `"remote"` (default) or `"local"`. |
| `wait` | `bool` | Whether to wait for remote Flyte runs to reach a terminal phase. |
| `wait_max_workers` | `int \| None` | Max worker threads used to wait for remote runs. |
| `run_options` | `dict[str, Any] \| None` | Optional dict of kwargs forwarded to `flyte.with_runcontext` (e.g. `service_account`, `name`, `copy_style`, `raw_data_path`). |
| `task_env_key` | `str` | Config key containing entry-task `task.override` kwargs, nested under the launched task's name. Child task overrides must be applied by user code. |
| `**kwargs` | `Any` | |

**Returns**

List of job results. Waited remote runs return wrappers with `url`
and the resolved task outputs.

