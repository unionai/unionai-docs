---
title: Passing parameters into app environments
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Passing parameters into app environments

`[[AppEnvironment]]`s support various parameter types that can be passed at deployment time. This includes primitive values, files, directories, and delayed values like `RunOutput` and `AppEndpoint`.

## Parameter types overview

There are several parameter types:

- **Primitive values**: Strings, numbers, booleans
- **Files**: `flyte.io.File` objects
- **Directories**: `flyte.io.Dir` objects
- **Delayed values**: `RunOutput` (from task runs) or `AppEndpoint` (inject endpoint urls of other apps)

## Basic parameter types

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=basic-parameter-types lang=python >}}

## Delayed values

Delayed values are parameters whose actual values are materialized at deployment time.

### RunOutput

Use `RunOutput` to pass outputs from task runs as app parameters:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=runoutput-example lang=python >}}

The `type` argument is required and must be one of `string`, `file`, or `directory`.
When the app is deployed, it will make the remote calls needed to figure out the
actual value of the parameter.

### AppEndpoint

Use `AppEndpoint` to pass endpoints from other apps:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=appendpoint-example lang=python >}}

The endpoint URL will be injected as the parameter value when the app starts.

This is particularly useful when you want to chain apps together (for example, a frontend app calling a backend app), without hardcoding URLs.

## Overriding parameters at serve time

You can override parameter values when serving apps (this is not supported for deployment):

```python
# Override parameters when serving
app = flyte.with_servecontext(
    input_values={"my-app": {"model_path": "s3://bucket/new-model.pkl"}}
).serve(app_env)
```

> [!NOTE]
> Parameter overrides are only available when using `flyte.serve()` or `flyte.with_servecontext().serve()`. 
> The `flyte.deploy()` function does not support parameter overrides - parameters must be specified in the `AppEnvironment` definition.

This is useful for:
- Testing different configurations during development
- Using different models or data sources for testing
- A/B testing different app configurations

## Example: FastAPI app with configurable model

Here's a complete example showing how to use parameters in a FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-inputs-fastapi-example.py" lang=python >}}

## Example: Using RunOutput for model serving

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=runoutput-serving-example lang=python >}}

## Accessing parameters in your app

How you access parameters depends on how they're configured:

1. **Environment variables**: If `env_var` is specified, the parameter is available as an environment variable
2. **Mounted paths**: File and directory parameters are mounted at the specified path
3. **Flyte SDK**: Use the Flyte SDK to access parameter values programmatically

```python
import os

# Parameter with env_var specified
env = flyte.app.AppEnvironment(
    name="my-app",
    parameters=[
        flyte.app.Parameter(
            name="model_file",
            value=flyte.io.File("s3://bucket/model.pkl"),
            mount="/app/models/model.pkl",
            env_var="MODEL_PATH",
        ),
    ],
    # ...
)

# Access in the app via the environment variable
API_KEY = os.getenv("API_KEY")

# Access in the app via the mounted path
with open("/app/models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Access in the app via the Flyte SDK (for string parameters)
parameter_value = flyte.app.get_parameter("model_file")  # Returns string value
```

## Best practices

1. **Use delayed parameters**: Leverage `RunOutput` and `AppEndpoint` to create app dependencies between tasks and apps, or app-to-app chains.
2. **Override for testing**: Use the `input_values` parameter when serving to test different configurations without changing code.
3. **Mount paths clearly**: Use descriptive mount paths for file/directory parameters so your app code is easy to understand.
4. **Use environment variables**: For simple constants that you can hard-code, use `env_var` to inject values as environment variables.
5. **Production deployments**: For production, define parameters in the `AppEnvironment` rather than overriding them at deploy time.

## Limitations

- Large files/directories can slow down app startup.
- Parameter overrides are only available when using `flyte.with_servecontext(...).serve(...)`.
