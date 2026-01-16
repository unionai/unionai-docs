---
title: Connecting training to serving
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Connecting training to serving

The key to our project is `RunOutput` - the mechanism that connects training outputs to serving inputs. Let's understand how it works.

## The RunOutput pattern

When you train a model, Flyte stores the output as an artifact. When you serve, you need to load that artifact. `RunOutput` bridges this gap:

```python
from flyte.app import Parameter, RunOutput

Parameter(
    name="model",
    value=RunOutput(
        task_name="training_pipeline",  # Which task produced the output
        type="file",                     # Artifact type
    ),
    download=True,                       # Download to container
    env_var="MODEL_PATH",                # Where to find it
)
```

## How RunOutput works

1. **At training time**: Your task returns a `flyte.File` or `flyte.Directory`. Flyte uploads it to object storage and records metadata.

2. **At serving time**: The app starts and Flyte resolves the `RunOutput`:
   - Finds the specified task's runs
   - Locates the output artifact
   - Downloads it if `download=True`
   - Sets the environment variable to the local path

3. **At runtime**: Your app reads `MODEL_PATH` and loads the model.

## RunOutput options

```python
RunOutput(
    task_name="training_pipeline",  # Required: task function name
    type="file",                     # Required: "file" or "directory"
    run_name="my-specific-run",      # Optional: specific run to use
)
```

**`task_name`**: The name of the task function that produced the artifact. This is the Python function name, not the environment name.

**`type`**: Either `"file"` for single files or `"directory"` for folders.

**`run_name`**: (Optional) A specific run to use. If omitted, Flyte uses the most recent successful run of that task.

## Parameter options

```python
Parameter(
    name="model",                    # Identifier for this parameter
    value=RunOutput(...),            # Where to get the data
    download=True,                   # Download to local filesystem
    env_var="MODEL_PATH",           # Environment variable to set
)
```

**`download`**: When `True`, the artifact is downloaded to the container's filesystem. When `False`, only the remote URL is provided.

**`env_var`**: The environment variable name where the path (or URL) is stored. Your app code reads this to find the artifact.

## Complete example

Here's the full flow:

**Training (train.py):**
```python
@train_env.task
def training_pipeline() -> flyte.File:
    data = prepare_data()
    model = fine_tune(data)
    return model  # Returns flyte.File, stored in object storage
```

**Serving (serve.py):**
```python
env = FastAPIAppEnvironment(
    name="inference",
    parameters=[
        Parameter(
            name="model",
            value=RunOutput(task_name="training_pipeline", type="file"),
            download=True,
            env_var="MODEL_PATH",
        ),
    ],
    ...
)

@env.server
def init_model(app: FastAPI):
    model_path = os.environ["MODEL_PATH"]  # Set by Flyte
    app.state.model = load_model(model_path)
```

## Using a specific run

By default, `RunOutput` uses the most recent successful run. To use a specific run:

```python
RunOutput(
    task_name="training_pipeline",
    type="file",
    run_name="training-run-abc123",  # Specific run ID
)
```

This is useful when you want to:
- Roll back to a previous model version
- A/B test different model versions
- Pin to a known-good training run

## Best practices

1. **Save models as archives**: Use `.tar.gz` for models with multiple files (tokenizer, config, weights).

2. **Use environment variables**: Pass paths via `env_var` for clean separation between configuration and code.

3. **Initialize once in `@env.server`**: Load models at startup, not per-request. This avoids repeated loading overhead.

4. **Store in `app.state`**: FastAPI's `app.state` shares data across request handlers.

5. **Handle missing models gracefully**: Check if the model loaded and return appropriate errors if not.

## Summary

You've built a complete ML system:

- **Training pipeline**: Tasks that prepare data and fine-tune a model
- **Serving app**: FastAPI endpoint that loads and serves the model
- **RunOutput**: The connection between training outputs and serving inputs

This pattern scales to complex systems with multiple models, versions, and environments.

## Next steps

- [Configuring apps](../configure-apps/): More app configuration options
- [Building apps](../build-apps/): Different app types (Streamlit, vLLM, etc.)
- [Files and directories](../task-programming/files-and-directories): Working with file artifacts
