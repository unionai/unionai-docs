---
title: App inputs
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# App inputs

App inputs allow you to pass data to your app at deployment time. This is useful when you want to configure your app based on outputs from tasks, other apps, or external data sources.

## Input types

Apps support several input types:

- **Primitive values**: Strings, numbers, booleans
- **Files**: `flyte.File` objects
- **Directories**: `flyte.Dir` objects
- **Delayed values**: `RunOutput` (from task runs) or `AppEndpoint` (from other apps)

## Basic input syntax

Use the `inputs` parameter when creating your `AppEnvironment`:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=basic-inputs lang=python >}}

## Input types and examples

### String inputs

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=string-inputs lang=python >}}

These inputs are made available to your app via environment variables or through Flyte's input injection mechanism.

### File inputs

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=file-inputs lang=python >}}

The file will be downloaded and mounted at the specified path in the container.

### Directory inputs

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=directory-inputs lang=python >}}

The directory will be downloaded and mounted at the specified path.

### Delayed inputs with RunOutput

You can use outputs from task runs as inputs:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=runoutput-input lang=python >}}

When the app is deployed, it will wait for the specified task run to complete and use its output.

### Delayed inputs with AppEndpoint

You can pass endpoints from other apps:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=appendpoint-input lang=python >}}

The endpoint URL will be injected as the input value when the app starts.

## Overriding inputs at serve/deploy time

You can override input values when serving or deploying:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-examples.py" fragment=override-inputs lang=python >}}

This is particularly useful for:
- Testing different configurations
- Using different models or data sources
- A/B testing different app configurations

## Accessing inputs in your app

How you access inputs depends on the type:

1. **Environment variables**: Some inputs are injected as environment variables
2. **Mounted paths**: File and directory inputs are mounted at specified paths
3. **Flyte SDK**: Use the Flyte SDK to access input values programmatically

For specialized app environments (like vLLM, SGLang), inputs are often handled automatically. Check the documentation for your specific app type.

## Example: FastAPI app with configurable model

```python
from flyte.app.extras import FastAPIAppEnvironment
from fastapi import FastAPI
import os

app = FastAPI()

# Access input via environment variable
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/default.pkl")

app_env = FastAPIAppEnvironment(
    name="model-serving-api",
    app=app,
    inputs=[
        flyte.app.Input(
            name="model_file",
            value=flyte.File("s3://bucket/models/default.pkl"),
            mount="/app/models",
            env_var="MODEL_PATH",
        ),
    ],
    # ...
)

@app.get("/predict")
async def predict(data: dict):
    # Load model from MODEL_PATH
    model = load_model(MODEL_PATH)
    return model.predict(data)
```

## Best practices

1. **Use delayed inputs**: Leverage `RunOutput` and `AppEndpoint` to create app dependencies
2. **Override for testing**: Use `input_values` parameter when serving to test different configurations
3. **Mount paths clearly**: Use descriptive mount paths for file/directory inputs
4. **Document inputs**: Make sure your app documentation explains what inputs it expects
5. **Use environment variables**: For simple values, use `env_var` to inject as environment variables

## Limitations

- Inputs are resolved at deployment time, not at request time
- Large files/directories can slow down app startup
- Input overrides are only available when using `flyte.serve()` or `flyte.deploy()` directly

