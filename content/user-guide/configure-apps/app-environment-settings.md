---
title: App environments
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# App environment settings

`[[AppEnvironment]]`s control how your apps run in Flyte, including images, resources, secrets, startup behavior, and autoscaling.

## Shared environment settings

`[[AppEnvironment]]`s share many configuration options with `[[TaskEnvironment]]`s:

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

> [!TIP]
> For most `AppEnvironment`s, use `args` instead of `command` to specify the app startup command
> in the container. This is because `args` will use the `fserve` command to run the app, which
> unlocks features like local code bundling and file/directory mounting via input injection.

### `command`

The `command` parameter specifies the full command to run your app. If not specified, Flyte will use a default command that runs your app via `fserve`, which is the Python executable provided
by `flyte` to run apps.

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
> For most apps, especially when using specialized app environments like `FastAPIAppEnvironment`, you don't need to specify `command` as it's automatically configured. Use `command` when you need
> to specify the raw container command, e.g. when running a non-Python app or when you have all
> of the dependencies and data used by the app available in the container.

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

### `domain`

The `domain` parameter specifies a custom domain or subdomain for your app. Use `flyte.app.Domain` to configure a subdomain or custom domain.

```python
app_env = flyte.app.AppEnvironment(
    name="my-app",
    domain=flyte.app.Domain(subdomain="myapp"),
    # ...
)
```

### `links`

The `links` parameter adds links to the App UI page. Use `flyte.app.Link` objects to specify relative or absolute links with titles.

```python
app_env = flyte.app.AppEnvironment(
    name="my-app",
    links=[
        flyte.app.Link(path="/docs", title="API Documentation", is_relative=True),
        flyte.app.Link(path="/health", title="Health Check", is_relative=True),
        flyte.app.Link(path="https://www.example.com", title="External link", is_relative=False),
    ],
    # ...
)
```

### `include`

The `include` parameter specifies files and directories to include in the app bundle. Use glob patterns or explicit paths to include code files needed by your app.

```python
app_env = flyte.app.AppEnvironment(
    name="my-app",
    include=["*.py", "models/", "utils/", "requirements.txt"],
    # ...
)
```

> [!NOTE]
> Learn more about including additional files in your app deployment [here](./including-additional-files).

### `inputs`

The `inputs` parameter passes inputs to your app at deployment time. Inputs can be primitive values, files, directories, or delayed values like `RunOutput` or `AppEndpoint`.

```python
app_env = flyte.app.AppEnvironment(
    name="my-app",
    inputs=[
        flyte.app.Input(name="config", value="foo", env_var="BAR"),
        flyte.app.Input(name="model", value=flyte.io.File(path="s3://bucket/model.pkl"), mount="/mnt/model"),
        flyte.app.Input(name="data", value=flyte.io.File(path="s3://bucket/data.pkl"), mount="/mnt/data"),
    ],
    # ...
)
```

> [!NOTE]
> Learn more about passing inputs to your app at deployment time [here](./passing-inputs).

### `scaling`

The `scaling` parameter configures autoscaling behavior for your app. Use `flyte.app.Scaling` to set replica ranges and idle TTL.

```python
app_env = flyte.app.AppEnvironment(
    name="my-app",
    scaling=flyte.app.Scaling(
        replicas=(1, 5),
        scaledown_after=300,  # Scale down after 5 minutes of idle time
    ),
    # ...
)
```

> [!NOTE]
> Learn more about autoscaling apps [here](./auto-scaling-apps).

### `depends_on`

The `depends_on` parameter specifies environment dependencies. When you deploy an app, all dependencies are deployed first.

```python
backend_env = flyte.app.AppEnvironment(name="backend-api", ...)

frontend_env = flyte.app.AppEnvironment(
    name="frontend-app",
    depends_on=[backend_env],  # backend-api will be deployed first
    # ...
)
```

> [!NOTE]
> Learn more about app environment dependencies [here](./apps-depending-on-environments).

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
