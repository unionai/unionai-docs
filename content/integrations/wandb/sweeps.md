---
title: Sweeps
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Sweeps

W&B sweeps automate hyperparameter optimization by running multiple trials with different parameter combinations. The `@wandb_sweep` decorator creates a sweep and makes it easy to run trials in parallel using Flyte's distributed execution.

## Creating a sweep

Use `@wandb_sweep` to create a W&B sweep when the task executes:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/wandb/sweep.py" lang=python highlight="3-9 14 16 20 32 35 47-58" >}}

The `@wandb_sweep` decorator:

- Creates a W&B sweep when the task starts
- Makes the sweep ID available via `get_wandb_sweep_id()`
- Adds a link to the main sweeps page in the Flyte UI

Use `wandb_sweep_config()` to define the sweep parameters. This is passed to W&B's sweep API.

{{< note >}}
Random and Bayesian searches run indefinitely, and the sweep remains in the `Running` state until you stop it.
You can stop a running sweep from the Weights & Biases UI or from the command line.
{{< /note >}}

## Running parallel agents

Flyte's distributed execution makes it easy to run multiple sweep agents in parallel, each on its own compute resources:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/wandb/parallel_sweep.py" lang=python highlight="51-55 59" >}}

This pattern provides:

- **Distributed execution**: Each agent runs on separate compute nodes
- **Resource allocation**: Specify CPU, memory, and GPU per agent
- **Fault tolerance**: Failed agents can retry without affecting others
- **Timeout protection**: Prevent runaway trials

{{< note >}}
`run_parallel_sweep` links to the main Weights & Biases sweeps page and `sweep_agent` links to the specific sweep URL because we cannot determine the sweep ID at link rendering time.
{{< /note >}}

![Sweep](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/wandb/sweep.png)

## Writing objective functions

The objective function is called by `wandb.agent()` for each trial. It must be a regular Python function decorated with `@wandb_init`:

```python {hl_lines=["1-2", "5-6"]}
@wandb_init
def objective():
    """Objective function for sweep trials."""
    # Access hyperparameters from wandb.run.config
    run = wandb.run
    config = run.config

    # Your training code
    model = create_model(
        learning_rate=config.learning_rate,
        hidden_size=config.hidden_size,
    )

    for epoch in range(config.epochs):
        train_loss = train_epoch(model)
        val_loss = validate(model)

        # Log metrics - W&B tracks these for the sweep
        run.log({
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
        })

    # The final val_loss is used by the sweep to rank trials
```

Key points:

- Use `@wandb_init` on the objective function (not `@env.task`)
- Access hyperparameters via `wandb.run.config` (not `get_wandb_run()` since this is outside Flyte context)
- Log the metric specified in `wandb_sweep_config(metric=...)` so the sweep can optimize it
- The function is called multiple times by `wandb.agent()`, once per trial
