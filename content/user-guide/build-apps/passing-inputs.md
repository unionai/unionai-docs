---
title: Passing inputs into apps
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Passing inputs into apps

Apps support various input types that can be passed at deployment time. This includes primitive values, files, directories, and delayed values like `RunOutput` and `AppEndpoint`.

## Input types overview

Apps support several input types:

- **Primitive values**: Strings, numbers, booleans
- **Files**: `flyte.File` objects
- **Directories**: `flyte.Dir` objects
- **Delayed values**: `RunOutput` (from task runs) or `AppEndpoint` (from other apps)

## Basic input types

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-inputs-examples.py" fragment=basic-input-types lang=python >}}

## Delayed inputs

### RunOutput

Use `RunOutput` to pass outputs from task runs as app inputs:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-inputs-examples.py" fragment=runoutput-example lang=python >}}

When the app is deployed, it will wait for the specified task run to complete and use its output.

### AppEndpoint

Use `AppEndpoint` to pass endpoints from other apps:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-inputs-examples.py" fragment=appendpoint-example lang=python >}}

The endpoint URL will be injected as the input value when the app starts.

This is particularly useful when you want to chain apps together (for example, a frontend app calling a backend app), without hardcoding URLs.

## Overriding inputs at serve or deploy time

You can override input values when serving or deploying apps:

```python
# Override inputs when serving
app = flyte.serve(app_env, input_values={"my-app": {"model_path": "s3://bucket/new-model.pkl"}})

# Override inputs when deploying
app = flyte.deploy(app_env, input_values={"my-app": {"model_path": "s3://bucket/new-model.pkl"}})
```

This is useful for:
- Testing different configurations
- Using different models or data sources
- A/B testing different app configurations

## Example: FastAPI app with configurable model

Here's a complete example showing how to use inputs in a FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-fastapi-example.py" lang=python >}}

## Example: Using RunOutput for model serving

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-inputs-examples.py" fragment=runoutput-serving-example lang=python >}}

## Accessing inputs in your app

How you access inputs depends on how they're configured:

1. **Environment variables**: If `env_var` is specified, the input is available as an environment variable
2. **Mounted paths**: File and directory inputs are mounted at the specified path
3. **Flyte SDK**: Use the Flyte SDK to access input values programmatically

### Environment variables

```python
import os

# Input with env_var specified
flyte.app.Input(name="api_key", value="secret-key", env_var="API_KEY")

# Access in app
API_KEY = os.getenv("API_KEY")
```

### Mounted paths

```python
# File input with mount
flyte.app.Input(
    name="model_file",
    value=flyte.File("s3://bucket/model.pkl"),
    mount="/app/models/model.pkl",  # Mounted at this path
)

# Access in app
with open("/app/models/model.pkl", "rb") as f:
    model = pickle.load(f)
```

## Best practices

1. **Use delayed inputs**: Leverage `RunOutput` and `AppEndpoint` to create app dependencies between tasks and apps, or app-to-app chains.
2. **Override for testing**: Use the `input_values` parameter when serving or deploying to test different configurations without changing code.
3. **Mount paths clearly**: Use descriptive mount paths for file/directory inputs so your app code is easy to understand.
4. **Document inputs**: Make sure your app documentation explains what inputs it expects and how they’re used.
5. **Use environment variables**: For simple values, use `env_var` to inject as environment variables.
6. **Type safety**: Specify input types clearly in your app code.

## Limitations

- Inputs are resolved at deployment/serve time, not at request time.
- Large files/directories can slow down app startup.
- Input overrides are only available when using `flyte.serve()` or `flyte.deploy()` directly.
- Delayed inputs (`RunOutput`, `AppEndpoint`) must be resolved before the app can start.

