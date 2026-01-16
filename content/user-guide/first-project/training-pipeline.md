---
title: Training pipeline
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Training pipeline

Now let's build the training pipeline. This will be a series of tasks that prepare data, fine-tune a model, and save it as a file artifact.

## Define the training environment

First, we set up a `TaskEnvironment` with the resources and dependencies needed for training:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="training-env" >}}

This environment includes:
- GPU resources for training
- Python packages for ML (transformers, torch, etc.)
- Enough memory for model weights

## Prepare the data

The first task prepares training data. This is a lightweight operation that doesn't need GPU:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="prepare-data" >}}

## Fine-tune the model

The core training task loads a base model, fine-tunes it on our data, and saves the result:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="fine-tune" >}}

Key points:
- The function returns a `flyte.File` object
- Flyte automatically uploads this file to object storage
- The file becomes available as an artifact for other tasks or apps

## Orchestrate the pipeline

The top-level task connects data preparation and training:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="training-pipeline" >}}

This is our "workflow" - it's just a task that calls other tasks. The pipeline:
1. Prepares the training data
2. Fine-tunes the model with that data
3. Returns the model file artifact

## Run the training

Add a main block to execute the pipeline:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="main" >}}

Run the training:

```bash
uv run train.py
```

You'll see a URL printed. Click it to monitor the training run in the UI.

## What happens during training

When you run the pipeline:

1. **Code is packaged** and sent to your Flyte backend
2. **Containers spin up** with the specified resources and image
3. **Tasks execute** in sequence: prepare_data → fine_tune
4. **The model file is saved** to object storage
5. **Metadata is recorded** so the app can find the model later

The run completes with a trained model stored as an artifact. In the next section, we'll create an app that loads and serves this model.

## Next steps

With the training pipeline complete, let's build the [serving app](./serving-the-model) that will load and serve our trained model.
