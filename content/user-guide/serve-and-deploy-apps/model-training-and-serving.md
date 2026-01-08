---
title: Model training and serving
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Model training and serving

This guide shows how to build an end-to-end machine learning workflow that trains a model using Flyte tasks and serves it via a FastAPI endpoint. The trained model is automatically passed from the training pipeline to the serving app using Flyte's `RunOutput` parameter.

> [!NOTE]
> For serving pre-trained HuggingFace models (like Llama, Qwen, etc.) without custom training, see [Prefetching models](./prefetching-models).

## Overview

The workflow consists of two main components:

1. **Training pipeline**: Tasks that prepare data and fine-tune a model, saving the result as a file artifact
2. **Serving app**: A FastAPI application that loads the trained model and exposes inference endpoints

The key to connecting these is the `Parameter` with `RunOutput`, which tells the serving app to load its model from a specific training run.

## Training pipeline

The training pipeline uses `TaskEnvironment` to define the compute resources and container image for training tasks.

### Define the training environment

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="training-env" >}}

### Prepare the data

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="prepare-data" >}}

### Fine-tune the model

The fine-tuning task trains the model and saves it as an archive file. The function returns a `File` object that Flyte stores in the object store.

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="fine-tune" >}}

### Orchestrate the pipeline

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="training-pipeline" >}}

### Run training

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/train.py" lang="python" fragment="main" >}}

## Serving app

The serving app uses `FastAPIAppEnvironment` to define a FastAPI application that loads and serves the trained model.

### Define request/response models

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-models" >}}

### Create the FastAPI app

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-app" >}}

### Configure the serving environment

The key configuration is the `parameters` list with a `Parameter` that references the training pipeline output using `RunOutput`:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-env" >}}

**Parameter options:**
- `name`: Identifier for the parameter
- `value`: A `RunOutput` referencing the task that produced the model
- `download`: When `True`, downloads the file to the app container
- `env_var`: Environment variable name where the file path is stored

### Load the model on startup

The `@env.server` decorator defines initialization logic that runs when the app starts:

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-server" >}}

### Deploy the app

{{< code file="/external/unionai-examples/v2/tutorials/model-training-serving/serve.py" lang="python" fragment="serve-main" >}}

## Running the workflow

### Step 1: Train the model

```bash
cd v2/tutorials/model-training-serving
uv run train.py
```

Monitor the training run in the UI using the printed URL.

### Step 2: Deploy the serving app

Once training completes:

```bash
uv run serve.py
```

The app will automatically load the model from the most recent `training_pipeline` run.

### Step 3: Test the API

```bash
curl -X POST "https://<app-url>/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Once upon a time", "max_length": 100}'
```

## Connecting training to serving

The `RunOutput` class is the key to connecting training outputs to serving inputs:

```python
from flyte.app import Parameter, RunOutput

Parameter(
    name="model",
    value=RunOutput(
        task_name="training_pipeline",  # Name of the task that produced the output
        type="file",                     # Type: "file" or "directory"
        run_name="my-specific-run",      # Optional: specific run name
    ),
    download=True,
    env_var="MODEL_PATH",
)
```

**RunOutput options:**
- `task_name`: The task function name that produced the artifact
- `type`: Either `"file"` or `"directory"`
- `run_name`: (Optional) Specific run to use; if omitted, uses the most recent run

## Best practices

1. **Save models as archives**: Use tar.gz archives for models with multiple files (tokenizer, config, weights)
2. **Use environment variables**: Pass file paths via `env_var` for clean separation
3. **Initialize in `@env.server`**: Load models once at startup, not per-request
4. **Store in `app.state`**: Use FastAPI's `app.state` to share loaded models across requests
5. **Handle missing models**: Check if the model loaded successfully and return appropriate errors

## Next steps

- [FastAPI apps](../build-apps/fastapi-app): More details on building FastAPI apps
- [Prefetching models](./prefetching-models): Use pre-trained HuggingFace models
- [Files and directories](../task-programming/files-and-directories): Working with file artifacts
