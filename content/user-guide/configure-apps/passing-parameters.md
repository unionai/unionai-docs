---
title: Passing parameters into app environments
weight: 4
variants: +flyte +union
---

# Passing parameters into app environments

`[[AppEnvironment]]`s support various parameter types that can be passed at deployment time. This includes primitive values, files, directories, and delayed values like `RunOutput` and `AppEndpoint`.

## Parameter types overview

There are several parameter types:

- **Primitive values**: Strings, numbers, booleans
- **Files**: `flyte.io.File` objects (use `flyte.io.File.from_existing_remote(...)` for remote files)
- **Directories**: `flyte.io.Dir` objects (use `flyte.io.Dir.from_existing_remote(...)` for remote directories)
- **Delayed values**: `RunOutput` (from task runs) or `AppEndpoint` (inject endpoint urls of other apps)

## Basic parameter types

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=basic-parameter-types lang=python >}}

> [!WARNING]
> Do not use `flyte.io.File(...)` or `flyte.io.Dir(...)` directly as parameter values.
> Use `flyte.io.File.from_existing_remote(...)` and `flyte.io.Dir.from_existing_remote(...)` to
> reference existing remote files and directories.

## Accessing parameters in your app

There are three ways to access parameter values at runtime: **mount paths**, **environment variables**, and the **`get_parameter` helper function**.

### `mount`

When `mount` is specified on a `Parameter`, the file or directory is downloaded to the given path.
If the mount path ends with a `/`, the file is placed inside that directory with its original
name. Otherwise, the file is downloaded to the exact path specified.

Your app reads directly from the mount path:

```python
with open("/tmp/data_file.txt", "rb") as fh:
    contents = fh.read()
```

### `env_var`

When `env_var` is specified, an environment variable is set containing the path to the downloaded
file or directory. This is useful when you want your app code to be decoupled from specific mount
paths:

```python
import os

data_path = os.environ["DATA_FILE_PATH"]
with open(data_path, "rb") as fh:
    contents = fh.read()
```

### `get_parameter`

The `get_parameter(name)` helper function from `flyte.app` returns the path to the downloaded
file or the string value of the parameter. This works regardless of whether `mount` or `env_var`
are specified and is the most flexible access method:

```python
from flyte.app import get_parameter

data_path = get_parameter("data")
with open(data_path, "rb") as fh:
    contents = fh.read()
```

When a parameter has no `mount` or `env_var` configured, `get_parameter` is the only way to
access its value at runtime.

### Full example

The following example defines a FastAPI app with parameters using all three access methods:

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=parameter-access-methods lang=python >}}

## Delayed values

Delayed values are parameters whose actual values are materialized at deployment time.

### RunOutput

Use `RunOutput` to pass outputs from task runs as app parameters:

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=runoutput-example lang=python >}}

The `type` argument is required and must be one of `string`, `file`, or `directory`.
When the app is deployed, it will make the remote calls needed to figure out the
actual value of the parameter.

### AppEndpoint

Use `AppEndpoint` to pass endpoints from other apps:

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=appendpoint-example lang=python >}}

The endpoint URL will be injected as the parameter value when the app starts.

This is particularly useful when you want to chain apps together (for example, a frontend app calling a backend app), without hardcoding URLs.

## Overriding parameters at serve time

You can override parameter values when serving apps using `parameter_values` in
`flyte.with_servecontext`. File and directory values must use `from_existing_remote`:

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=parameter-serve-override lang=python >}}

> [!NOTE]
> Parameter overrides are only available when using `flyte.with_servecontext().serve()`.
> The `flyte.deploy()` function does not support parameter overrides — parameters must be specified in the `AppEnvironment` definition.

This is useful for:
- Testing different configurations during development
- Using different models or data sources for testing
- A/B testing different app configurations

## Example: FastAPI app with configurable model

Here's a complete example showing how to use parameters in a FastAPI app:

{{< code file="/unionai-examples/v2/user-guide/configure-apps/app-parameters-fastapi-example.py" lang=python >}}

## Example: Using RunOutput for model serving

{{< code file="/unionai-examples/v2/user-guide/build-apps/passing-parameters-examples.py" fragment=runoutput-serving-example lang=python >}}

## Best practices

1. **Use `from_existing_remote`**: Always use `flyte.io.File.from_existing_remote(...)` or `flyte.io.Dir.from_existing_remote(...)` to reference remote files and directories as parameter values.
2. **Use delayed parameters**: Leverage `RunOutput` and `AppEndpoint` to create app dependencies between tasks and apps, or app-to-app chains.
3. **Override for testing**: Use the `parameter_values` argument in `flyte.with_servecontext()` to test different configurations without changing code.
4. **Mount paths clearly**: Use descriptive mount paths for file/directory parameters so your app code is easy to understand.
5. **Use environment variables**: For paths that your app needs to reference dynamically, use `env_var` to inject values as environment variables.
6. **Use `get_parameter` for flexibility**: When you want to keep your parameter access decoupled from specific mount paths or env var names, use `get_parameter(name)`.

## Limitations

- Large files/directories can slow down app startup.
- Parameter overrides are only available when using `flyte.with_servecontext(...).serve(...)`.
