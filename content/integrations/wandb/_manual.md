---
title: Manual integration
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Manual integration

If you need more control over W&B initialization, you can use the `Wandb` and `WandbSweep` link classes directly instead of the decorators. This lets you call `wandb.init()` and `wandb.finish()` yourself while still getting automatic links in the Flyte UI.

## Using the Wandb link class

Add a `Wandb` link to your task to generate a link to the W&B run in the Flyte UI:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/wandb/init_manual.py" lang=python highlight="3 15-22 31-36 44" >}}

### With a custom run ID

If you want to use your own run ID, specify it in both the link and the `wandb.init()` call:

```python {hl_lines=[6, 14]}
@env.task(
    links=(
        Wandb(
            project="my-project",
            entity="my-team",
            id="my-custom-run-id",
        ),
    )
)
async def train_with_custom_id() -> str:
    run = wandb.init(
        project="my-project",
        entity="my-team",
        id="my-custom-run-id",  # Must match the link's ID
        resume="allow",
    )

    # Training code...
    run.finish()
    return run.id
```

### Adding links at runtime with override

You can also add links when calling a task using `.override()`:

```python {hl_lines=9}
@env.task
async def train_model(learning_rate: float) -> str:
    # ... training code with manual wandb.init() ...
    return run.id


# Add link when running the task
result = await train_model.override(
    links=(Wandb(project="my-project", entity="my-team", run_mode="new"),)
)(learning_rate=0.01)
```

## Using the `WandbSweep` link class

Use `WandbSweep` to add a link to a W&B sweep:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/wandb/sweep_manual.py" lang=python highlight="3 25-30 43" >}}

The link will point to the project's sweeps page. If you have the sweep ID, you can specify it in the link:

```python {hl_lines=6}
@env.task(
    links=(
        WandbSweep(
            project="my-project",
            entity="my-team",
            id="known-sweep-id",
        ),
    )
)
async def resume_sweep() -> str:
    # Resume an existing sweep
    wandb.agent("known-sweep-id", function=objective, count=10)
    return "known-sweep-id"
```
