---
title: App environments
weight: 1
variants: +flyte +union
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

For complete parameter documentation, type signatures, and defaults, see the [`AppEnvironment` API reference](../../api-reference/flyte-sdk/packages/flyte.app/appenvironment).

Key app-specific parameters include `type`, `port`, `args`, `command`, `requires_auth`, `scaling`, `domain`, `links`, `include`, `parameters`, `cluster_pool`, and `timeouts`. See also:

- [Including additional files](./including-additional-files) in your app deployment
- [Passing parameters](./passing-parameters) to your app
- [Auto-scaling apps](./auto-scaling-apps)
- [App environment dependencies](./apps-depending-on-environments)

### Environment variable substitution in `args`

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
> unlocks features like local code bundling and file/directory mounting via parameter injection.

## App startup

There are two ways to start up an app in Flyte:
1. With a server function using `@app_env.server`
2. As a container command using `command` or `args`

### Server decorator via `@app_env.server`

The server function is a Python function that runs the app. It is defined using the `@app_env.server` decorator.

{{< code file="/unionai-examples/v2/user-guide/configure-apps/fastapi-server-example.py" fragment=fastapi-app lang=python >}}

The `@app_env.server` decorator allows you to define a synchronous or asynchronous function that runs the app, either
with a server start command like `uvicorn.run`, [`HTTPServer.serve_forever`](https://docs.python.org/3/library/http.server.html), etc.

> [!NOTE]
> Generally the `[[FastAPIAppEnvironment]]` handles serving automatically under the hood,
> the example above just shows how the `@app_env.server` decorator can be used to define a server function
> that runs the app.

#### Startup hook

The server function is called after the app is started up, and before the app is shut down. It is defined using the `@app_env.on_startup` decorator. This is useful if you need to load any state or external connections needed to run the
app before it starts.

{{< code file="/unionai-examples/v2/user-guide/configure-apps/fastapi-server-example.py" fragment=on-startup-decorator lang=python >}}

#### Shutdown hook

The server function is called before the app instance shuts down during scale down. It is defined using the
`@app_env.on_shutdown` decorator. This is useful if you need to clean up any state or external connections in the
container running the app.

{{< code file="/unionai-examples/v2/user-guide/configure-apps/fastapi-server-example.py" fragment=on-shutdown-decorator lang=python >}}

### Container command via `command` vs `args`

The difference between `args` and `command` is crucial for properly configuring how your app starts.

- **`command`**: The full command to run your app, for example, `"streamlit hello --server.port 8080"`. For most use
  cases, you don't need to specify `command` as it's automatically configured, and uses the `fserve` executable to
  run the app. `fserve` does additional setup for you, like setting up the code bundle and loading [parameters](./passing-parameters) if provided, so it's highly recommended to use the default command.
- **`args`**: Arguments to pass to your app's command (used with the default Flyte command or your custom command). The
  `fserve` executable takes in additional arguments, which you can specify as the arguments needed to run your app, e.g.
  `uvicorn run main.py --server.port 8080`.

#### Default startup behavior

When you don't specify a `command`, Flyte generates a default command that uses `fserve` to run your app. This default command handles:

- Setting up the code bundle
- Configuring the version
- Setting up project/domain context
- Injecting parameters if provided

The default command looks like:

```bash
fserve --version <version> --project <project> --domain <domain> -- <args>
```

So if you specify `args`, they'll be appended after the `--` separator.

#### Using args with the default command

When you use `args` without specifying `command`, the args are passed to the default Flyte command:

{{< code file="/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=args-with-default-command lang=python >}}

This effectively runs:

```bash
fserve --version ... --project ... --domain ... -- streamlit run main.py --server.port 8080
```

#### Using an explicit command

When you specify a `command`, it completely replaces the default command:

{{< code file="/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=explicit-command lang=python >}}

This runs exactly:

```bash
streamlit hello --server.port 8080
```

#### Using a command with args

You can combine both, though this is less common:

{{< code file="/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=command-with-args lang=python >}}

#### FastAPIAppEnvironment example

When using `FastAPIAppEnvironment`, the command is automatically configured to run uvicorn:

{{< code file="/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=fastapi-auto-command lang=python >}}

The `FastAPIAppEnvironment` automatically:

1. Detects the module and variable name of your FastAPI app
2. Uses an internal server function to start the app via `uvicorn.run`.
3. Handles all the startup configuration for you

## Shared settings

For more details on shared settings like images, resources, and secrets, refer to the [task configuration](../task-configuration/_index) documentation.
