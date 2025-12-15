---
title: App environments
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# App environments

App environments control how your apps run in Flyte, including images, resources, secrets, startup behavior, and autoscaling. This page combines the previous **Environment settings**, **App startup**, and **Autoscaling apps** docs into a single guide.

## Shared environment settings

App environments share many configuration options with task environments:

- **Images**: See [Container images](../task-configuration/container-images/) for details on creating and using container images
- **Resources**: See [Resources](../task-configuration/resources/) for CPU, memory, GPU, and storage configuration
- **Secrets**: See [Secrets](../task-configuration/secrets/) for injecting secrets into your app
- **Environment variables**: Set via the `env_vars` parameter (same as tasks)
- **Cluster pools**: Specify via the `cluster_pool` parameter

## App-specific environment settings

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
app_env = flyte.app.AppEnvironment(
    name="my-app",
    port=flyte.app.Port(port=8080),
    # ...
)
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

#### Environment variable substitution

Environment variables are automatically substituted in `args` strings when they start with the `$` character. This works for both:

- Values from `env_vars`
- Secrets that are specified as environment variables (via `as_env_var` in `flyte.Secret`)

The `$VARIABLE_NAME` syntax will be replaced with the actual environment variable value at runtime:

```python
# Using env_vars
app_env = flyte.app.AppEnvironment(
    name="my-app",
    env_vars={"API_KEY": "secret-key-123"},
    args="--api-key $API_KEY",  # $API_KEY will be replaced with "secret-key-123"
    # ...
)

# Using secrets
app_env = flyte.app.AppEnvironment(
    name="my-app",
    secrets=flyte.Secret(key="AUTH_SECRET", as_env_var="AUTH_SECRET"),
    args=["--api-key", "$AUTH_SECRET"],  # $AUTH_SECRET will be replaced with the secret value
    # ...
)
```

This is particularly useful for passing API keys or other sensitive values to command-line arguments without hardcoding them in your code. The substitution happens at runtime, ensuring secrets are never exposed in your code or configuration files.

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
app_env = flyte.app.AppEnvironment(
    name="public-dashboard",
    requires_auth=False,
    # ...
)

# Private app (authentication required - default)
app_env = flyte.app.AppEnvironment(
    name="internal-api",
    requires_auth=True,
    # ...
)  # Default
```

When `requires_auth=True`, users must authenticate with Flyte to access the app. When `requires_auth=False`, the app is publicly accessible (though it may still require API keys or other app-level authentication).

## App startup

Understanding the difference between `args` and `command` is crucial for properly configuring how your app starts.

### Command vs args

In container terminology:

- **`command`**: The executable or entrypoint that runs
- **`args`**: Arguments passed to that command

In Flyte apps:

- **`command`**: The full command to run your app (for example, `"streamlit hello --server.port 8080"`)
- **`args`**: Arguments to pass to your app's command (used with the default Flyte command or your custom command)

### Default startup behavior

When you don't specify a `command`, Flyte generates a default command that uses `fserve` to run your app. This default command handles:

- Setting up the code bundle
- Configuring the version
- Setting up project/domain context
- Injecting inputs if provided

The default command looks like:

```bash
fserve --version <version> --project <project> --domain <domain> -- <args>
```

So if you specify `args`, they'll be appended after the `--` separator.

### Startup examples

#### Using args with default command

When you use `args` without specifying `command`, the args are passed to the default Flyte command:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=args-with-default-command lang=python >}}

This effectively runs:

```bash
fserve --version ... --project ... --domain ... -- streamlit run main.py --server.port 8080
```

#### Using explicit command

When you specify a `command`, it completely replaces the default command:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=explicit-command lang=python >}}

This runs exactly:

```bash
streamlit hello --server.port 8080
```

#### Using command with args

You can combine both, though this is less common:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=command-with-args lang=python >}}

#### FastAPIAppEnvironment example

When using `FastAPIAppEnvironment`, the command is automatically configured to run uvicorn:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=fastapi-auto-command lang=python >}}

The `FastAPIAppEnvironment` automatically:

1. Detects the module and variable name of your FastAPI app
2. Sets the command to run `uvicorn <module>:<app_var> --port <port>`
3. Handles all the startup configuration for you

### Startup best practices

1. **Use specialized app environments** when available (for example, `FastAPIAppEnvironment`) – they handle command setup automatically.
2. **Use `args`** when you need code bundling and input injection.
3. **Use `command`** for simple, standalone apps that don't need code bundling.
4. **Always set `port`** to match what your app actually listens on.
5. **Use `include`** with `args` to bundle your app code files.

## Autoscaling apps

Flyte apps support autoscaling, allowing them to scale up and down based on traffic. This helps optimize costs by scaling down when there's no traffic and scaling up when needed.

### Scaling configuration

The `scaling` parameter uses a `Scaling` object to configure autoscaling behavior:

```python
scaling=flyte.app.Scaling(
    replicas=(min_replicas, max_replicas),
    scaledown_after=idle_ttl_seconds,
)
```

#### Parameters

- **`replicas`**: A tuple `(min_replicas, max_replicas)` specifying the minimum and maximum number of replicas.
- **`scaledown_after`**: Time in seconds to wait before scaling down when idle (idle TTL).

### Basic scaling example

Here's a simple example with scaling from 0 to 1 replica:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=basic-scaling lang=python >}}

This configuration:

- Starts with 0 replicas (no running instances)
- Scales up to 1 replica when there's traffic
- Scales back down to 0 after 5 minutes (300 seconds) of no traffic

### Scaling patterns

#### Always-on app

For apps that need to always be running:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=always-on lang=python >}}

#### Scale-to-zero app

For apps that can scale to zero when idle:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=scale-to-zero lang=python >}}

#### High-availability app

For apps that need multiple replicas for availability:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=high-availability lang=python >}}

#### Burstable app

For apps with variable load:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/autoscaling-examples.py" fragment=burstable lang=python >}}

### Idle TTL (Time To Live)

The `scaledown_after` parameter (idle TTL) determines how long an app instance can be idle before it's scaled down. 

#### Considerations

- **Too short**: May cause frequent scale up/down cycles, leading to cold starts.
- **Too long**: Keeps resources running unnecessarily, increasing costs.
- **Optimal**: Balance between cost and user experience.

#### Common idle TTL values

- **Development/Testing**: 60-180 seconds (1-3 minutes) - quick scale down for cost savings.
- **Production APIs**: 300-600 seconds (5-10 minutes) - balance cost and responsiveness.
- **Batch processing**: 900-1800 seconds (15-30 minutes) - longer to handle bursts.
- **Always-on**: Set `min_replicas > 0` - never scale down.

### Autoscaling best practices

1. **Start conservative**: Begin with longer idle TTL values and adjust based on usage.
2. **Monitor cold starts**: Track how long it takes for your app to become ready after scaling up.
3. **Consider costs**: Balance idle TTL between cost savings and user experience.
4. **Use appropriate min replicas**: Set `min_replicas > 0` for critical apps that need to be always available.
5. **Test scaling behavior**: Verify your app handles scale up/down correctly (for example, state management and connections).

### Autoscaling limitations

- Scaling is based on traffic/request patterns, not CPU/memory utilization.
- Cold starts may occur when scaling from zero.
- Stateful apps need careful design to handle scaling (use external state stores).
- Maximum replicas are limited by your cluster capacity.

### Autoscaling troubleshooting

**App scales down too quickly:**

- Increase `scaledown_after` value.
- Set `min_replicas > 0` if the app needs to stay warm.

**App doesn't scale up fast enough:**

- Ensure your cluster has capacity.
- Check if there are resource constraints.

**Cold starts are too slow:**

- Pre-warm with `min_replicas = 1`.
- Optimize app startup time.
- Consider using faster storage for model loading.

## Complete example

Here's a complete example showing various environment, startup, and scaling settings:

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
- Configuring autoscaling behavior

For more details on shared settings like images, resources, and secrets, refer to the [task configuration](../task-configuration/) documentation.
