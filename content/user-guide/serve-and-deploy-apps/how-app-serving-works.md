---
title: How app serving works
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# How app serving works

Serving is the recommended way to deploy apps during development. It provides a faster feedback loop and allows you to dynamically modify inputs.

## Overview

When you serve an app:

1. **Code bundling**: Your app code is bundled and prepared
2. **Image building**: Container images are built (if needed)
3. **Deployment**: The app is deployed to your Flyte cluster
4. **Activation**: The app is automatically activated and ready to use
5. **URL generation**: A URL is generated for accessing the app

## Using Python SDK

The simplest way to serve an app:

```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-dev-app",
    # ... configuration ...
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.serve(app_env)
    print(f"App served at: {app.url}")
```

This will:
- Bundle your code
- Build any necessary images
- Deploy the app
- Activate it automatically
- Return an `App` object with the URL

## Overriding inputs

One key advantage of serving is the ability to override inputs dynamically:

```python
app = flyte.serve(
    app_env,
    input_values={
        "my-dev-app": {
            "model_path": "s3://bucket/models/test-model.pkl",
            "api_key": "test-key",
        }
    },
)
```

This is useful for:
- Testing different configurations
- Using different models or data sources
- A/B testing during development

## Advanced serving options

Use `with_servecontext()` for more control:

```python
from flyte import with_servecontext

with with_servecontext(
    version="v1.0.0",
    project="my-project",
    domain="development",
    env_vars={"LOG_LEVEL": "DEBUG"},
    input_values={"app-name": {"input": "value"}},
    cluster_pool="dev-pool",
    log_level=logging.INFO,
    log_format="json",
) as ctx:
    app = ctx.serve(app_env)
```

### Serve parameters

#### `version`

Optional version string for the app:

```python
with with_servecontext(version="dev-v1.0.0") as ctx:
    app = ctx.serve(app_env)
```

If not specified, Flyte generates a version automatically.

#### `project` and `domain`

Override the project and domain:

```python
with with_servecontext(
    project="my-project",
    domain="development",
) as ctx:
    app = ctx.serve(app_env)
```

#### `env_vars`

Inject environment variables into the app:

```python
with with_servecontext(
    env_vars={
        "LOG_LEVEL": "DEBUG",
        "API_KEY": "test-key",
    },
) as ctx:
    app = ctx.serve(app_env)
```

#### `input_values`

Override app inputs:

```python
with with_servecontext(
    input_values={
        "app-name": {
            "model_path": "s3://bucket/models/model.pkl",
            "api_key": "key-value",
        }
    },
) as ctx:
    app = ctx.serve(app_env)
```

Input values are keyed by app name, then by input name.

#### `cluster_pool`

Target a specific cluster pool:

```python
with with_servecontext(cluster_pool="gpu-pool") as ctx:
    app = ctx.serve(app_env)
```

#### `log_level` and `log_format`

Control logging:

```python
import logging

with with_servecontext(
    log_level=logging.DEBUG,
    log_format="json",  # or "console"
) as ctx:
    app = ctx.serve(app_env)
```

#### `dry_run`

Preview what would be deployed without actually deploying:

```python
with with_servecontext(dry_run=True) as ctx:
    app = ctx.serve(app_env)  # Doesn't actually deploy
```

## Using CLI

You can also serve apps from the command line:

```bash
flyte serve path/to/app.py app_name
```

With options:

```bash
flyte serve path/to/app.py app_name \
    --version v1.0.0 \
    --project my-project \
    --domain development \
    --env-var LOG_LEVEL=DEBUG \
    --input-value model_path=s3://bucket/model.pkl \
    --cluster-pool gpu-pool
```

## What happens during serve

1. **Code analysis**: Flyte analyzes your app code and dependencies
2. **Code bundling**: Necessary files are bundled (based on `include` or auto-detection)
3. **Image preparation**: Container images are prepared or built
4. **Deployment**: App is deployed to the Flyte cluster
5. **Activation**: App is automatically activated
6. **URL generation**: A URL is generated for the app

## Differences from deploy

| Feature | Serve | Deploy |
|---------|-------|--------|
| **Purpose** | Development | Production |
| **Input overrides** | ✅ Supported | ❌ Fixed at deploy time |
| **Activation** | ✅ Automatic | ❌ Manual |
| **Versioning** | Optional | Recommended |
| **Speed** | Faster iteration | Slower, more thorough |
| **Reproducibility** | Lower | Higher |

## Best practices

1. **Use for development**: Serve is ideal for development and testing.
2. **Override inputs**: Take advantage of input overrides for testing different configurations.
3. **Quick iteration**: Use serve for rapid development cycles.
4. **Switch to deploy**: Use deploy for production deployments.
5. **Version control**: Consider versioning even in development.
6. **Separate environments**: Use different projects/domains for dev/staging/prod.
7. **Logging**: Use appropriate log levels and formats (`log_level`, `log_format`) for your use case.
8. **Cluster pools**: Target appropriate cluster pools for your workload.

## Troubleshooting

**App not activating:**
- Check cluster connectivity
- Verify app configuration is correct
- Review container logs for errors

**Input overrides not working:**
- Verify input names match exactly
- Check that inputs are defined in the app environment
- Ensure you're using the `input_values` parameter correctly

**Slow serving:**
- Images may need to be built (first time is slower).
- Large code bundles can slow down deployment.
- Check network connectivity to the cluster.

## Return value

`flyte.serve()` returns an `App` object with:

- `url`: The app's URL
- `endpoint`: The app's endpoint URL
- `status`: Current status of the app
- `name`: App name

```python
app = flyte.serve(app_env)
print(f"URL: {app.url}")
print(f"Endpoint: {app.endpoint}")
print(f"Status: {app.status}")
```

