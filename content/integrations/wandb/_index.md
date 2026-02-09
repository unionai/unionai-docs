---
title: Weights & Biases
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Weights & Biases

[Weights & Biases](https://wandb.ai) (W&B) is a platform for tracking machine learning experiments, visualizing metrics and optimizing hyperparameters. This plugin integrates W&B with Flyte, enabling you to:

- Automatically initialize W&B runs in your tasks without boilerplate
- Link directly from the Flyte UI to your W&B runs and sweeps
- Share W&B runs across parent and child tasks
- Track distributed training jobs across multiple GPUs and nodes
- Run hyperparameter sweeps with parallel agents

## Installation

```shell
pip install flyteplugins-wandb
```

You also need a W&B API key. Store it as a Flyte secret so your tasks can authenticate with W&B.

## Quick start

Here's a minimal example that logs metrics to W&B from a Flyte task:

{{< code file="/external/unionai-examples/v2/integrations/flyte-plugins/wandb/quick_start.py" lang=python highlight="3 8 10 14 17 31-33" >}}

This example demonstrates the core pattern:

1. **Define a task environment** with the plugin installed and your W&B API key as a secret
2. **Decorate your task** with `@wandb_init` (must be the outermost decorator, above `@env.task`)
3. **Access the run** with `get_wandb_run()` to log metrics
4. **Provide configuration** via `wandb_config()` when running the task

The plugin handles calling `wandb.init()` and `wandb.finish()` for you, and automatically adds a link to the W&B run in the Flyte UI.

![UI](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/integrations/wandb/ui.png)

## What's next

This integration guide is split into focused sections, depending on how you want to use Weights & Biases with Flyte:

- **[Experiments](experiments)**: Create and manage W&B runs from Flyte tasks.
- **[Distributed training](distributed_training)**: Track experiments across multi-GPU and multi-node training jobs.
- **[Sweeps](sweeps)**: Run hyperparameter searches and manage sweep execution from Flyte tasks.
- **[Downloading logs](downloading_logs)**: Download logs and execution metadata from Weights & Biases.
- **[Constraints and best practices](constraints_and_best_practices)**: Learn about limitations, edge cases and recommended patterns.
- **[Manual integration](manual)**: Use Weights & Biases directly in Flyte tasks without decorators or helpers.

{{< note >}}
We've included additional examples developed while testing edge cases of the plugin [here](https://github.com/flyteorg/flyte-sdk/tree/main/plugins/wandb/examples).
{{< /note >}}
