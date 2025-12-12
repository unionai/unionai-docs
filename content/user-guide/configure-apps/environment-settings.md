---
title: Environment settings
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Environment settings

App environments share many configuration options with task environments, including images, resources, and secrets. However, apps also have unique settings like `type`, `port`, `args`, `command`, and `requires_auth` that are specific to long-running services.

## Shared environment settings

The following settings work the same way for apps as they do for tasks:

- **Images**: See [Container images](../task-configuration/container-images/) for details on creating and using container images
- **Resources**: See [Resources](../task-configuration/resources/) for CPU, memory, GPU, and storage configuration
- **Secrets**: See [Secrets](../task-configuration/secrets/) for injecting secrets into your app
- **Environment variables**: Set via the `env_vars` parameter (same as tasks)
- **Cluster pools**: Specify via `cluster_pool` parameter

## App-specific settings

### `type`

The `type` parameter is an optional string that identifies what kind of app this is. It's used for organizational purposes and may be used by the UI or tooling to display or filter apps.

```python
app_env = flyte.app.AppEnvironment(
    name="my-fastapi-app",
    type="FastAPI",
    # ...
)
```

When using specialized app environments like `FastAPIAppEnvironment`, the type is automatically set. For custom apps, you can set it to any string value.

### `port`

The `port` parameter specifies which port your app listens on. It can be an integer or a `Port` object.

```python
# Using an integer (simple case)
app_env = flyte.app.AppEnvironment(name="my-app", port=8080, ...)

# Using a Port object (more control)
app_env = flyte.app.AppEnvironment(name="my-app", port=flyte.app.Port(port=8080), ...)
```

The default port is `8080`. Your app should listen on this port (or the port you specify).

> [!NOTE]
> Ports 8012, 8022, 8112, 9090, and 9091 are reserved and cannot be used for apps.

### `args`

The `args` parameter specifies arguments to pass to your app's command. This is typically used when you need to pass additional arguments to the command specified in `command`, or when using the default command behavior.

```python
app_env = flyte.app.AppEnvironment(
    name="streamlit-app",
    args="streamlit run main.py --server.port 8080",
    port=8080,
    # ...
)
```

`args` can be either a string (which will be shell-split) or a list of strings:

```python
# String form (will be shell-split)
args="--option1 value1 --option2 value2"

# List form (more explicit)
args=["--option1", "value1", "--option2", "value2"]
```

### `command`

The `command` parameter specifies the full command to run your app. If not specified, Flyte will use a default command that runs your app via `fserve`.

```python
# Explicit command
app_env = flyte.app.AppEnvironment(
    name="streamlit-hello",
    command="streamlit hello --server.port 8080",
    port=8080,
    # ...
)

# Using default command (recommended for most cases)
# When command is None, Flyte generates a command based on your app configuration
app_env = flyte.app.AppEnvironment(name="my-app", ...)  # command=None by default
```

> [!TIP]
> For most apps, especially when using specialized app environments like `FastAPIAppEnvironment`, you don't need to specify `command` as it's automatically configured.

### `requires_auth`

The `requires_auth` parameter controls whether the app requires authentication to access. By default, apps require authentication (`requires_auth=True`).

```python
# Public app (no authentication required)
app_env = flyte.app.AppEnvironment(name="public-dashboard", requires_auth=False, ...)

# Private app (authentication required - default)
app_env = flyte.app.AppEnvironment(name="internal-api", requires_auth=True, ...)  # Default
```

When `requires_auth=True`, users must authenticate with Flyte to access the app. When `requires_auth=False`, the app is publicly accessible (though it may still require API keys or other app-level authentication).

## Complete example

Here's a complete example showing various environment settings:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/environment-settings-example.py" lang=python >}}

This example demonstrates:

- Setting a custom `type` identifier
- Configuring the port
- Specifying compute resources
- Injecting secrets as environment variables
- Setting environment variables
- Making the app publicly accessible
- Targeting a specific cluster pool
- Adding a description

For more details on shared settings like images, resources, and secrets, refer to the [task configuration](../task-configuration/) documentation.

