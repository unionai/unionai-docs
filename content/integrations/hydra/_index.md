---
title: Hydra
weight: 1
variants: +flyte +union
---

# Hydra

[Hydra](https://hydra.cc) is a framework for composing and overriding configuration trees from YAML files, dataclasses and the command line. The `flyteplugins-hydra` plugin makes Hydra a first-class submission layer for Flyte, so you can compose a config exactly as you would in any other Hydra app and have each composed run executed as a Flyte task, locally or as a remote execution on a {{< key product_name >}} cluster.

The plugin offers three complementary entry points that share a single launcher implementation:

| Entry point                                    | Use it when                                                                                                                              |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `hydra/launcher=flyte` (Hydra Launcher plugin) | You already have a `@hydra.main` script and want standard Hydra CLI ergonomics, including `--multirun` and custom sweepers.              |
| `flyte hydra run` (Flyte CLI extension)        | You want a Flyte-style CLI that imports a task from a Python file and composes a Hydra config without requiring a `@hydra.main` wrapper. |
| `hydra_run` / `hydra_sweep` (Python SDK)       | You want to submit runs directly from Python -- notebooks, tests, examples or another orchestration script.                              |

All three paths converge on the same `FlyteLauncher`.

## Installation

```bash
pip install flyteplugins-hydra
```

The plugin depends on `flyteplugins-omegaconf`, which is installed automatically and provides the `DictConfig`/`ListConfig` type transformers that allow Hydra-composed configs to flow into Flyte tasks. Both packages must be available in the same environment as `flyte`.

If you call `apply_task_env` for child tasks (see [Task environment overrides](#task-environment-overrides)), include `flyteplugins-hydra` in the task image as well.

## Requirements on tasks

Every task launched through this plugin must accept an OmegaConf `DictConfig` input. Any other parameters are passed through as ordinary task arguments.

```python{hl_lines=[1, 5]}
from omegaconf import DictConfig


@env.task
async def pipeline(cfg: DictConfig, dataset: str) -> float:
    ...
```

The plugin auto-detects the `DictConfig` parameter name. If your parameter is `cfg`, app-level overrides are passed through `--cfg` on the CLI; if it is `config`, they are passed through `--config`; and so on.

## A walkthrough config

The examples in this page assume a small project layout:

```
project/
├── train.py
└── conf/
    ├── training.yaml
    ├── model/
    │   ├── resnet.yaml
    │   └── vit.yaml
    ├── optimizer/
    │   ├── adam.yaml
    │   └── sgd.yaml
    └── task_env/
        ├── a100.yaml
        └── prebuilt_image.yaml
```

`conf/training.yaml`:

```yaml
defaults:
  - optimizer: adam
  - model: resnet
  - _self_

data:
  path: s3://my-bucket/imagenet
  dataset: imagenet

training:
  epochs: 30
  batch_size: 64
```

`train.py` (abbreviated):

```python
import flyte
from omegaconf import DictConfig
from flyteplugins.hydra import apply_task_env

env = flyte.TaskEnvironment(name="training", image=...)


@env.task
async def preprocess(cfg: DictConfig) -> flyte.io.Dir: ...


@env.task
async def train_model(cfg: DictConfig, data: flyte.io.Dir) -> tuple[flyte.io.Dir, float]: ...


@env.task
async def pipeline(cfg: DictConfig, dataset: str) -> float:
    data = await preprocess(cfg)
    train_task = apply_task_env(train_model, cfg)
    _, val_loss = await train_task(cfg, data)
    return val_loss
```

The same `pipeline` task is the target of every example below.

{{< note >}}
`config_path` is resolved relative to the current working directory. If you submit runs from a directory other than `project/`, pass an absolute path (or an absolute path on the CLI via `--config-path /abs/path/to/conf`). For structured-config-only setups (no YAML files), omit `config_path` / `--config-path` entirely.
{{< /note >}}

## Execution mode

Remote execution is the default. Every entry point exposes an explicit knob:

| Surface                | Local                       | Remote                                 |
| ---------------------- | --------------------------- | -------------------------------------- |
| `@hydra.main` launcher | `hydra.launcher.mode=local` | `hydra.launcher.mode=remote` (default) |
| `flyte hydra run`      | `--local`                   | `--mode remote` (default)              |
| Python SDK             | `mode="local"`              | `mode="remote"` (default)              |

For the `@hydra.main` launcher, the default applies as soon as `hydra/launcher=flyte` is selected.

Remote runs print the Flyte run URL immediately after submission, before any waiting. By default the plugin then waits for every submitted run to reach a terminal phase, capped at 32 worker threads. To tune or disable waiting:

| Surface                | Tune wait threads                    | Fire and forget             |
| ---------------------- | ------------------------------------ | --------------------------- |
| `@hydra.main` launcher | `hydra.launcher.wait_max_workers=64` | `hydra.launcher.wait=false` |
| `flyte hydra run`      | `--wait-max-workers 64`              | `--no-wait`                 |
| Python SDK             | `wait_max_workers=64`                | `wait=False`                |

For a sweep, every job is submitted first and waits run concurrently. Submission is not blocked by earlier runs reaching a terminal phase.

## Hydra launcher (`@hydra.main` scripts)

Use this path when your script already has a `@hydra.main` entry point. Selecting `hydra/launcher=flyte` swaps Hydra's built-in `BasicLauncher` for `FlyteLauncher`.

Single remote run:

```bash
python train.py hydra/launcher=flyte hydra.launcher.mode=remote
```

Single local run:

```bash
python train.py hydra/launcher=flyte hydra.launcher.mode=local
```

Remote grid sweep submission: Each comma-separated value expands into a separate Flyte execution; six executions in this example:

```bash{hl_lines=[4]}
python train.py --multirun \
  hydra/launcher=flyte hydra.launcher.mode=remote \
  hydra.launcher.wait_max_workers=64 \
  optimizer.lr=0.001,0.01,0.1 training.epochs=10,20
```

Fire-and-forget sweep submission:

```bash{hl_lines=[2]}
python train.py --multirun \
  hydra/launcher=flyte hydra.launcher.wait=false \
  optimizer.lr=0.001,0.01,0.1
```

Custom sweepers (Optuna) work exactly as they do with the BasicLauncher. Selecting `hydra/sweeper=...` activates the sweeper and `FlyteLauncher` runs each trial as a Flyte execution:

```bash{hl_lines=["3-5"]}
python train.py --multirun \
  hydra/launcher=flyte hydra.launcher.mode=remote \
  hydra/sweeper=optuna hydra.sweeper.n_trials=20 \
  hydra.sweeper.n_jobs=4 \
  "optimizer.lr=interval(1e-4,1e-1)"
```

Inside `@hydra.main`, the standard pattern is:

```python{hl_lines=[7]}
import flyte
import hydra
from omegaconf import DictConfig
from flyteplugins.hydra import apply_task_env


@hydra.main(version_base=None, config_path="conf", config_name="training")
def main(cfg: DictConfig):
    flyte.init_from_config()
    entry_task = apply_task_env(pipeline, cfg)
    return flyte.run(entry_task, cfg=cfg, dataset=cfg.data.dataset)


if __name__ == "__main__":
    main()
```

## Python SDK

`hydra_run` composes one config and runs the task once. `hydra_sweep` expands sweep overrides and runs the task once per combination.

### Single run

```python{hl_lines=[1, 3, 7]}
from flyteplugins.hydra import hydra_run

run = hydra_run(
    pipeline,
    config_path="conf",
    config_name="training",
    overrides=["optimizer.lr=0.01"],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
    wait=True,
    wait_max_workers=64,
)
```

For a remote run with `wait=True`, the return value is a wrapper exposing both `run.url` and `run.value` (the resolved task output). The wrapper is `float()`-castable so Hydra sweepers such as Optuna can consume scalar objectives directly. With `wait=False`, the return value is the underlying `flyte.remote.Run`.

### Grid sweep

```python{hl_lines=[7]}
from flyteplugins.hydra import hydra_sweep

runs = hydra_sweep(
    pipeline,
    config_path="conf",
    config_name="training",
    overrides=["optimizer.lr=0.001,0.01,0.1", "training.epochs=10,20"],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
)
```

Six executions are submitted (3 × 2). `runs` is a list aligned with the Cartesian-product order Hydra's `BasicSweeper` produces.

### Custom sweepers

Custom sweeper plugins are activated by passing their selection in `overrides`:

```python{hl_lines=["5-10"]}
runs = hydra_sweep(
    pipeline,
    config_path="conf",
    config_name="training",
    overrides=[
        "hydra/sweeper=optuna",
        "hydra.sweeper.n_trials=20",
        "hydra.sweeper.n_jobs=4",
        "optimizer.lr=interval(1e-4,1e-1)",
    ],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
)
```

Whenever an override starts with `hydra/`, the plugin invokes the full Hydra runtime so plugin discovery (sweepers, launchers, callbacks) can run. Pure value overrides on the `hydra.*` namespace (for example `hydra.run.dir=...`) do not need the full runtime and are applied per-job by the launcher directly.

### Forwarding `flyte.with_runcontext` options

Use `run_options` to pass Flyte runtime options through to every job:

```python{hl_lines=["8-14"]}
runs = hydra_sweep(
    pipeline,
    config_path="conf",
    config_name="training",
    overrides=["optimizer.lr=0.001,0.01,0.1"],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
    run_options={
        "name": "my-training-sweep",
        "service_account": "default",
        "copy_style": "all",
        "raw_data_path": "s3://my-bucket/raw-data",
        "debug": True,
    },
)
```

## Flyte CLI (`flyte hydra run`)

`flyte hydra run` is registered through the `flyte.plugins.cli.commands` entry point. It loads a task from a Python file, composes a Hydra config, and runs the task without requiring the script to have its own `@hydra.main` function. It also inherits the relevant flags from `flyte run` (`--project`, `--domain`, `--image`, `--name`, `--service-account`, `--raw-data-path`, `--copy-style`, `--debug`, `--local`, `--follow`).

### Single run

Remote (default):

```bash
flyte hydra run --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet
```

Forced local:

```bash{hl_lines=[1]}
flyte hydra run --local --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet
```

### Grid sweep

```bash{hl_lines=[4]}
flyte hydra run --multirun --config-path conf --config-name training \
  --wait-max-workers 64 \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --cfg "optimizer.lr=0.001,0.01,0.1" --cfg "training.epochs=10,20"
```

### App-level vs Hydra-namespace overrides

The CLI keeps app-level overrides separate from Hydra runtime overrides so they do not collide with ordinary Flyte task arguments.

App-level overrides target the composed config and are passed through the **task's `DictConfig` parameter name**. For `pipeline(cfg: DictConfig, ...)`, use `--cfg`. For `pipeline_with_config(config: DictConfig, ...)`, use `--config`:

```bash{hl_lines=["3-4", 8]}
flyte hydra run --config-path conf --config-name training \
  train.py pipeline \
  --cfg optimizer.lr=0.01 \
  --cfg training.epochs=20

flyte hydra run --config-path conf --config-name training \
  train.py pipeline_with_config \
  --config optimizer.lr=0.01
```

Hydra runtime overrides: Anything in the `hydra.*` or `hydra/*` namespace go through `--hydra-override`:

```bash{hl_lines=[3, 4]}
flyte hydra run --config-path conf --config-name training \
  train.py pipeline \
  --hydra-override hydra.run.dir=./outputs/exp1 \
  --hydra-override hydra/launcher=flyte
```

Custom sweepers combine the two:

```bash{hl_lines=["3-7"]}
flyte hydra run --multirun --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --hydra-override hydra/sweeper=optuna \
  --hydra-override hydra.sweeper.n_trials=20 \
  --hydra-override hydra.sweeper.n_jobs=4 \
  --cfg "optimizer.lr=interval(1e-4,1e-1)" \
  --cfg "training.epochs=choice(10,20,50)"
```

### `--follow` and `--no-wait`

`--follow` streams logs from the launched run after submission; it implies waiting and cannot be combined with `--no-wait`. `--no-wait` returns immediately after submission and skips log streaming.

### Shell completion

Install Click's completion hook for the `flyte` executable. For zsh:

```zsh
eval "$(_FLYTE_COMPLETE=zsh_source flyte)"
```

For bash:

```bash
eval "$(_FLYTE_COMPLETE=bash_source flyte)"
```

Once installed, `flyte hydra run` adds Hydra-aware completion after `SCRIPT TASK_NAME`. The command imports the script, inspects the task signature, and suggests:

- The app override flag matching the task's `DictConfig` parameter (`--cfg`, `--config`, ...).
- Override values for that flag and `--hydra-override` via Hydra's own completion engine, including config keys, config-group selections and sweep functions.

```bash{hl_lines=["2-3", "6-7"]}
flyte hydra run --config-path conf --config-name training \
  train.py pipeline --cfg optimizer.<TAB>
# suggests optimizer.lr=, optimizer.weight_decay=, ...

flyte hydra run --config-path conf --config-name training \
  train.py pipeline --hydra-override hydra/launcher=<TAB>
# suggests hydra launcher choices
```

Because completion has to import the target script, keep task definitions and `ConfigStore` registration import-safe, and avoid expensive top-level work in scripts you reach via `flyte hydra run`.

![Auto Completion](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/hydra/auto_complete.gif)

## Override grammar

The override grammar is identical to standard Hydra; what differs is only how you pass the strings (positional in `python train.py ...`, list entries in `overrides=[...]`, repeated `--cfg`/`--hydra-override` on the Flyte CLI).

| Form                               | Meaning                                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------------------- |
| `optimizer.lr=0.01`                | Set an existing key.                                                                     |
| `optimizer=sgd`                    | Select a config group (replaces the `optimizer` subtree with `conf/optimizer/sgd.yaml`). |
| `+task_env=a100`                   | Append a config group whose key is not currently in the config.                          |
| `+training.grad_clip=1.0`          | Append a key that does not exist.                                                        |
| `++optimizer.lr=0.05`              | Force-set a key, creating it if missing and overriding strict-schema errors.             |
| `~training.warmup_steps`           | Delete a key from the composed config.                                                   |
| `optimizer.lr=0.001,0.01,0.1`      | Sweep value (with `--multirun`); expanded into one job per element.                      |
| `optimizer.lr=interval(1e-4,1e-1)` | Continuous sweep range; consumed by samplers like Optuna.                                |
| `optimizer=choice(adam,sgd)`       | Categorical sweep; consumed by samplers.                                                 |
| `hydra.run.dir=./outputs/exp1`     | Hydra-namespace value override (single run output dir).                                  |
| `hydra.sweep.dir=./outputs/sweep1` | Hydra-namespace sweep output dir.                                                        |
| `hydra/sweeper=optuna`             | Hydra-namespace config group selection (activates the Optuna sweeper plugin).            |

## Sweeps

### Grid sweeps (BasicSweeper)

Comma-separated overrides expand into a Cartesian product. The plugin uses Hydra's `BasicSweeper` to expand them, then submits one Flyte execution per combination.

```python{hl_lines=[1, 4, 7]}
from flyteplugins.hydra import hydra_sweep


runs = hydra_sweep(
    pipeline,
    config_path="conf", config_name="training",
    overrides=["model=resnet,vit", "optimizer.lr=0.001,0.01,0.1"],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
)  # 6 executions
```

```bash{hl_lines=[3]}
flyte hydra run --multirun --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --cfg "model=resnet,vit" --cfg "optimizer.lr=0.001,0.01,0.1"
```

Hardware presets can sweep alongside hyperparameters:

```bash{hl_lines=[3]}
flyte hydra run --multirun --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --cfg "+task_env=a10g,a100" --cfg "optimizer.lr=0.001,0.01,0.1"
```

### Bayesian / TPE sweeps (Optuna)

Install the sweeper, then activate it via `hydra/sweeper=optuna`. Continuous parameters use `interval(...)`; categorical parameters use `choice(...)`.

```bash
pip install hydra-optuna-sweeper
```

```bash{hl_lines=["3-8"]}
flyte hydra run --multirun --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --hydra-override "hydra/sweeper=optuna" \
  --hydra-override "hydra.sweeper.n_trials=30" \
  --hydra-override "hydra.sweeper.n_jobs=5" \
  --cfg "optimizer.lr=interval(1e-4,1e-1)" \
  --cfg "optimizer.weight_decay=interval(1e-6,1e-2)" \
  --cfg "model=choice(resnet,vit)"
```

When `wait=True`, each remote run's wrapped result exposes the task output as a float (via `__float__`), so Optuna can use it directly as the trial objective. With `wait=False`, the sweeper sees the run URL but cannot read objective values; use this only for fire-and-forget submission.

Other sweepers that respect Hydra's plugin protocol are activated the same way: install the package, select `hydra/sweeper=<name>`, and set the sweeper's parameters under `hydra.sweeper.*`.

### Sweep output directories

Hydra-namespace overrides redirect where Hydra writes per-job logs and config snapshots:

```bash{hl_lines=[3, 4]}
flyte hydra run --multirun --config-path conf --config-name training \
  train.py pipeline --dataset s3://my-bucket/imagenet \
  --hydra-override "hydra.sweep.dir=./outputs/sweep1" \
  --hydra-override "hydra.sweep.subdir=\${hydra.job.num}" \
  --cfg "optimizer.lr=0.001,0.01,0.1"
```

## Task environment overrides

Hydra is good at composing flat YAML; Flyte tasks need richer settings such as resources and container images. The plugin reserves a config key named `task_env` by default that maps task names to `task.override` kwargs.

```yaml
task_env:
  pipeline:
    resources:
      cpu: "2"
      memory: 8Gi
  train_model:
    resources:
      cpu: "16"
      memory: 64Gi
      gpu: "A100:1"
```

When the plugin launches a task, it looks up `task_env[<entry-task-name>]` (`pipeline` in this example) and applies the values via `task.override(...)`. Resource mappings are converted into `flyte.Resources(**values)` automatically.

### Prebuilt images

To run a task in a prebuilt container image, set `image` (and optionally `primary_container_name`):

```yaml{hl_lines=[3]}
task_env:
  pipeline:
    image: ghcr.io/acme/flyte-training:latest
    primary_container_name: main
    resources:
      cpu: "4"
      memory: 16Gi
```

`task.override` does not accept `image` directly. The task image is part of the task definition. Instead, the plugin lowers the override to a `flyte.PodTemplate` whose primary container uses the requested image:

- If the task has no inline pod template, a new one is created.
- If the task already has an inline `flyte.PodTemplate`, the plugin deep-copies it and sets only the image on the primary container.
- If the task references a pod template by name (a string), the plugin raises an error. You must patch a string-named template by editing it in cluster config rather than at submission time.

### Applying overrides to child tasks

The launcher only controls the entry task it submits. Child tasks called from within the entry task are not patched automatically. Use `apply_task_env` to apply the same `resources`/`image` handling to a child task before invoking it:

```python{hl_lines=[1, 7]}
from flyteplugins.hydra import apply_task_env


@env.task
async def pipeline(cfg: DictConfig, dataset: str) -> float:
    data = await preprocess(cfg)
    train_task = apply_task_env(train_model, cfg)
    _, val_loss = await train_task(cfg, data)
    return val_loss
```

This keeps the override knobs in YAML/CLI surfaces while leaving each task in control of which children it patches.

### Renaming the task-env key

If your config uses a different name for the task-env subtree, pass it explicitly:

```python
hydra_run(..., task_env_key="task_environment")
```

```bash
flyte hydra run --task-env-key task_environment ...
```

### What `task_env` should not model

The YAML schema intentionally omits the full Kubernetes `V1PodSpec`. Keep advanced pod configuration (volumes, init containers, node selectors, etc.) in Python task/environment code where you have a real type. Use Hydra `task_env` presets for the common knobs only: image, primary container name and resources.

## Structured configs (without YAML)

Structured configs work with this plugin as long as they are registered before the launcher composes the config. `flyte hydra run` imports the script first, so top-level `ConfigStore.instance().store(...)` calls run before composition.

```python{hl_lines=[17]}
from dataclasses import dataclass, field
from hydra.core.config_store import ConfigStore
from omegaconf import DictConfig


@dataclass
class TrainingConf:
    epochs: int = 30
    batch_size: int = 64


@dataclass
class RootConf:
    training: TrainingConf = field(default_factory=TrainingConf)


ConfigStore.instance().store(name="structured_training", node=RootConf)
```

Run a fully-structured config without YAML:

```bash{hl_lines=[1]}
flyte hydra run --config-name structured_training \
  train.py pipeline --dataset s3://my-bucket/imagenet
```

The same config also works through `@hydra.main`:

```bash
python train.py --config-name structured_training
```

If the structured config still references YAML config groups, keep `--config-path conf`. If everything is registered in `ConfigStore`, omit `--config-path`.

{{< warning >}}
Do not register structured configs only inside `if __name__ == "__main__":` or inside the `@hydra.main` function body. `flyte hydra run` and shell completion inspect the script at import time, before either of those blocks runs, and registrations placed there will not be visible.
{{< /warning >}}

Structured configs sweep just like YAML configs:

```python{hl_lines=[4, 5]}
runs = hydra_sweep(
    pipeline,
    config_path=None,
    config_name="structured_training",
    overrides=["training.epochs=10,20", "training.batch_size=32,64"],
    dataset="s3://my-bucket/imagenet",
    mode="remote",
)
```
