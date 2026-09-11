---
title: Constraints and best practices
description: Decorator ordering rules and the practices that keep W&B logging correct inside tasks and traces.
icon: exclamation-triangle
weight: 4
variants: +flyte +union
---

# Constraints and best practices

## Decorator ordering

`@wandb_init` and `@wandb_sweep` must be the **outermost decorators**, applied after `@env.task`:

```python
# Correct
@wandb_init
@env.task
async def my_task():
    ...

# Incorrect - will not work
@env.task
@wandb_init
async def my_task():
    ...
```

## Traces cannot use decorators

Do not apply `@wandb_init` to traces. Traces automatically access the parent task's run via `get_wandb_run()`:

```python
# Correct
@flyte.trace
async def my_trace():
    run = get_wandb_run()
    if run:
        run.log({"metric": 42})

# Incorrect - don't decorate traces
@wandb_init
@flyte.trace
async def my_trace():
    ...
```

## Maximum sweep agents

[W&B limits sweeps to a maximum of 20 concurrent agents](https://docs.wandb.ai/models/sweeps/existing-project#3-launch-agents).

## Configuration priority

Configuration is merged with the following priority (highest to lowest):

1. Decorator parameters (`@wandb_init(project="...")`)
2. Context manager (`with wandb_config(...)`)
3. Workflow-level context (`flyte.with_runcontext(custom_context=wandb_config(...))`)
4. Auto-generated values (run ID from Flyte context)

## Run ID generation

When no explicit `id` is provided, the plugin generates run IDs using the pattern:

```
{run_name}-{action_name}
```

This ensures unique, predictable IDs that can be matched between the `Wandb` link class and manual `wandb.init()` calls.

## Sync delay for local files

Files written to the run directory (via `get_wandb_run_dir()`) are synced to W&B asynchronously. There may be a brief delay before they appear in the W&B cloud or can be downloaded via `download_wandb_run_dir()`.

## Shared run mode requirements

When using `run_mode="shared"`, the task requires a parent task to have already created a W&B run. Calling a task with `run_mode="shared"` as a top-level task will fail.

## Objective functions for sweeps

Objective functions passed to `wandb.agent()` should:

- Be regular Python functions (not Flyte tasks)
- Be decorated with `@wandb_init`
- Access hyperparameters via `wandb.run.config` (not `get_wandb_run()`)
- Log the metric specified in `wandb_sweep_config(metric=...)` so the sweep can optimize it

## Error handling

`download_wandb_run_dir()` and `download_wandb_sweep_dirs()` raise `RuntimeError` when they fail, with the underlying W&B error as its cause where there is one. This includes when:

- No run or sweep ID is given and there is no active run or sweep
- `download_wandb_sweep_dirs()` has no entity and project to query (set them with `wandb_config()`)
- Authentication fails because `WANDB_API_KEY` is not set or is invalid
- The run or sweep can't be found in the W&B cloud, or you don't have access to it
- Every run in a sweep fails to download. If only some fail, `download_wandb_sweep_dirs()` logs a warning and returns the paths that succeeded

Errors from `wandb.init()` when a `@wandb_init` task starts, such as an authentication failure, are raised by `wandb` itself and are not wrapped.
