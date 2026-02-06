---
title: Experiments
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Experiments

The `@wandb_init` decorator automatically initializes a W&B run when your task executes and finishes it when the task completes. This section covers the different ways to use it.

## Basic usage

Apply `@wandb_init` as the outermost decorator on your task:

```python {hl_lines=1}
@wandb_init
@env.task
async def my_task() -> str:
    run = get_wandb_run()
    run.log({"metric": 42})
    return "done"
```

The decorator:

- Calls `wandb.init()` before your task code runs
- Calls `wandb.finish()` after your task completes (or fails)
- Adds a link to the W&B run in the Flyte UI

You can also use it on synchronous tasks:

```python {hl_lines=[1, 3]}
@wandb_init
@env.task
def my_sync_task() -> str:
    run = get_wandb_run()
    run.log({"metric": 42})
    return "done"
```

## Accessing the run object

Use `get_wandb_run()` to access the current W&B run object:

```python {hl_lines=6}
from flyteplugins.wandb import get_wandb_run

@wandb_init
@env.task
async def train() -> str:
    run = get_wandb_run()

    # Log metrics
    run.log({"loss": 0.5, "accuracy": 0.9})

    # Access run properties
    print(f"Run ID: {run.id}")
    print(f"Run URL: {run.url}")
    print(f"Project: {run.project}")

    # Log configuration
    run.config.update({"learning_rate": 0.001, "batch_size": 32})

    return run.id
```

## Parent-child task relationships

When a parent task calls child tasks, the plugin can share the same W&B run across all of them. This is useful for tracking an entire workflow in a single run.

```python {hl_lines=[1, 9, 16]}
@wandb_init
@env.task
async def child_task(x: int) -> int:
    run = get_wandb_run()
    run.log({"child_metric": x * 2})
    return x * 2


@wandb_init
@env.task
async def parent_task() -> int:
    run = get_wandb_run()
    run.log({"parent_metric": 100})

    # Child task shares the parent's run by default
    result = await child_task(5)

    return result
```

By default (`run_mode="auto"`), child tasks reuse their parent's W&B run. All metrics logged by the parent and children appear in the same run in the W&B UI.

## Run modes

The `run_mode` parameter controls how tasks create or reuse W&B runs. There are three modes:

| Mode             | Behavior                                                                   |
| ---------------- | -------------------------------------------------------------------------- |
| `auto` (default) | Create a new run if no parent run exists, otherwise reuse the parent's run |
| `new`            | Always create a new run, even if a parent run exists                       |
| `shared`         | Always reuse the parent's run (fails if no parent run exists)              |

### Using `run_mode="new"` for independent runs

```python {hl_lines=1}
@wandb_init(run_mode="new")
@env.task
async def independent_child(x: int) -> int:
    run = get_wandb_run()
    # This task gets its own separate run
    run.log({"independent_metric": x})
    return x


@wandb_init
@env.task
async def parent_task() -> str:
    run = get_wandb_run()
    parent_run_id = run.id

    # This child creates its own run
    await independent_child(5)

    # Parent's run is unchanged
    assert run.id == parent_run_id
    return parent_run_id
```

### Using `run_mode="shared"` for explicit sharing

```python {hl_lines=1}
@wandb_init(run_mode="shared")
@env.task
async def must_share_run(x: int) -> int:
    # This task requires a parent run to exist
    # It will fail if called as a top-level task
    run = get_wandb_run()
    run.log({"shared_metric": x})
    return x
```

## Configuration with `wandb_config`

Use `wandb_config()` to configure W&B runs. You can set it at the workflow level or override it for specific tasks, allowing you to provide configuration values at runtime.

### Workflow-level configuration

```python {hl_lines=["5-9"]}
if __name__ == "__main__":
    flyte.init_from_config()

    flyte.with_runcontext(
        custom_context=wandb_config(
            project="my-project",
            entity="my-team",
            tags=["experiment-1", "production"],
            config={"model": "resnet50", "dataset": "imagenet"},
        ),
    ).run(train_task)
```

### Overriding configuration for child tasks

Use `wandb_config()` as a context manager to override settings for specific child task calls:

```python {hl_lines=[8, 12]}
@wandb_init
@env.task
async def parent_task() -> str:
    run = get_wandb_run()
    run.log({"parent_metric": 100})

    # Override tags and config for this child call
    with wandb_config(tags=["special-run"], config={"learning_rate": 0.01}):
        await child_task(10)

    # Override run_mode for this child call
    with wandb_config(run_mode="new"):
        await child_task(20)  # Gets its own run

    return "done"
```

## Using traces with W&B runs

Flyte traces can access the parent task's W&B run without needing the `@wandb_init` decorator. This is useful for helper functions that should log to the same run:

```python {hl_lines=[1, 3]}
@flyte.trace
async def log_validation_metrics(accuracy: float, f1: float):
    run = get_wandb_run()
    if run:
        run.log({"val_accuracy": accuracy, "val_f1": f1})


@wandb_init
@env.task
async def train_and_validate() -> str:
    run = get_wandb_run()

    # Training loop
    for epoch in range(10):
        run.log({"train_loss": 1.0 / (epoch + 1)})

    # Trace logs to the same run
    await log_validation_metrics(accuracy=0.95, f1=0.92)

    return "done"
```

{{< note >}}
Do not apply `@wandb_init` to traces. Traces automatically access the parent task's run via `get_wandb_run()`.
{{< /note >}}
