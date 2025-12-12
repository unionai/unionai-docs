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
    version="dev-v1",
    project="my-project",
    domain="development",
    env_vars={"LOG_LEVEL": "DEBUG"},
    input_values={
        "my-dev-app": {"model_path": "s3://test/model.pkl"}
    },
) as ctx:
    app = ctx.serve(app_env)
    print(f"Served: {app.url}")
```

## Using CLI

You can also serve apps from the command line:

```bash
flyte serve path/to/app.py app_name
```

With options:

```bash
flyte serve path/to/app.py app_name \
    --project my-project \
    --domain development \
    --version dev-v1 \
    --input-values model_path=s3://bucket/model.pkl
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

1. **Use for development**: Serve is ideal for development and testing
2. **Override inputs**: Take advantage of input overrides for testing
3. **Quick iteration**: Use serve for rapid development cycles
4. **Switch to deploy**: Use deploy for production deployments
5. **Version control**: Consider versioning even in development

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
- Images may need to be built (first time is slower)
- Large code bundles can slow down deployment
- Check network connectivity to the cluster

