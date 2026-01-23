---
title: Constraints and best practices
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
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

## UI reruns with `with_runcontext`

Reruns triggered from the UI do not currently work when `wandb_config` is provided via the `with_runcontext` context manager. This is because the UI launch form does not yet support supplying `custom_context` values alongside inputs.

Support for providing this configuration in the UI is planned. In the meantime, you can either:

- use the `wandb_config` context manager instead of providing it via `with_runcontext`, or
- trigger runs from the command line.

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

The plugin raises standard exceptions:

- `RuntimeError`: When `download_wandb_run_dir()` is called without a run ID and no active run exists
- `wandb.errors.AuthenticationError`: When `WANDB_API_KEY` is not set or invalid
- `wandb.errors.CommError`: When a run cannot be found in the W&B cloud
