---
title: App startup
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# App startup

Understanding the difference between `args` and `command` is crucial for properly configuring how your app starts.

## Command vs Args

In container terminology:
- **`command`**: The executable or entrypoint that runs
- **`args`**: Arguments passed to that command

In Flyte apps:
- **`command`**: The full command to run your app (e.g., `"streamlit hello --server.port 8080"`)
- **`args`**: Arguments to pass to your app's command (used with the default Flyte command or your custom command)

## Default behavior

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

## Examples

### Using args with default command

When you use `args` without specifying `command`, the args are passed to the default Flyte command:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=args-with-default-command lang=python >}}

This effectively runs:
```bash
fserve --version ... --project ... --domain ... -- streamlit run main.py --server.port 8080
```

### Using explicit command

When you specify a `command`, it completely replaces the default command:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=explicit-command lang=python >}}

This runs exactly:
```bash
streamlit hello --server.port 8080
```

### Using command with args

You can combine both, though this is less common:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=command-with-args lang=python >}}

## When to use each

### Use `args` (and default `command`) when:

- You're using Flyte's code bundling and input injection features
- You want Flyte to handle versioning and context setup
- You're including files with the `include` parameter
- You want to pass inputs to your app

### Use `command` when:

- You're using a simple, self-contained command (like Streamlit's built-in hello app)
- You don't need Flyte's code bundling features
- You want complete control over the startup command
- You're using specialized app environments (like `FastAPIAppEnvironment`) which set `command` automatically

## FastAPIAppEnvironment example

When using `FastAPIAppEnvironment`, the command is automatically configured to run uvicorn:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/app-startup-examples.py" fragment=fastapi-auto-command lang=python >}}

The `FastAPIAppEnvironment` automatically:
1. Detects the module and variable name of your FastAPI app
2. Sets the command to run `uvicorn <module>:<app_var> --port <port>`
3. Handles all the startup configuration for you

## Best practices

1. **Use specialized app environments** when available (e.g., `FastAPIAppEnvironment`) - they handle command setup automatically
2. **Use `args`** when you need code bundling and input injection
3. **Use `command`** for simple, standalone apps that don't need code bundling
4. **Always set `port`** to match what your app actually listens on
5. **Use `include`** with `args` to bundle your app code files

## Troubleshooting

If your app isn't starting correctly:

1. **Check the port**: Make sure your app listens on the port specified in the `port` parameter
2. **Verify command/args**: Check the logs to see what command is actually being run
3. **Test locally**: Try running the command/args locally to ensure they work
4. **Check include files**: If using `args` with `include`, verify the files are being included correctly

