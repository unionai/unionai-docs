---
title: Downloading logs
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Downloading logs

This integration enables downloading Weights & Biases run data, including metrics history, summary data, and synced files.

## Automatic download

Set `download_logs=True` to automatically download run data after your task completes:

```python {hl_lines=1}
@wandb_init(download_logs=True)
@env.task
async def train_with_download():
    run = get_wandb_run()

    for epoch in range(10):
        run.log({"loss": 1.0 / (epoch + 1)})

    return run.id
```

The downloaded data is traced by Flyte and appears as a `Dir` output in the Flyte UI. Downloaded files include:

- `summary.json`: Final summary metrics
- `metrics_history.json`: Step-by-step metrics history
- Any files synced by W&B (`requirements.txt`, `wandb_metadata.json`, etc.)

You can also set `download_logs=True` in `wandb_config()`:

```python {hl_lines=5}
flyte.with_runcontext(
    custom_context=wandb_config(
        project="my-project",
        entity="my-team",
        download_logs=True,
    ),
).run(train_task)
```

![Logs](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/wandb/logs.png)

For sweeps, set `download_logs=True` on `@wandb_sweep` or `wandb_sweep_config()` to download all trial data:

```python {hl_lines=1}
@wandb_sweep(download_logs=True)
@env.task
async def run_sweep():
    sweep_id = get_wandb_sweep_id()
    wandb.agent(sweep_id, function=objective, count=10)
    return sweep_id
```

![Sweep Logs](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/wandb/sweep_logs.png)

## Accessing run directories during execution

Use `get_wandb_run_dir()` to access the local W&B run directory during task execution. This is useful for writing custom files that get synced to W&B:

```python {hl_lines=[1, 7, "18-19"]}
from flyteplugins.wandb import get_wandb_run_dir

@wandb_init
@env.task
def train_with_artifacts():
    run = get_wandb_run()
    local_dir = get_wandb_run_dir()

    # Train your model
    for epoch in range(10):
        run.log({"loss": 1.0 / (epoch + 1)})

    # Save model checkpoint to the run directory
    model_path = f"{local_dir}/model_checkpoint.pt"
    torch.save(model.state_dict(), model_path)

    # Save custom metrics file
    with open(f"{local_dir}/custom_metrics.json", "w") as f:
        json.dump({"final_accuracy": 0.95}, f)

    return run.id
```

Files written to the run directory are automatically synced to W&B and can be accessed later via the W&B UI or by setting `download_logs=True`.

{{< note >}}
`get_wandb_run_dir()` accesses the local directory without making network calls. Files written here may have a brief delay before appearing in the W&B cloud.
{{< /note >}}
