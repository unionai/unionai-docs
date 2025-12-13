---
title: App serve options
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# App serve options

This page documents the options available when serving apps using `flyte.serve()` or `with_servecontext()`.

## Basic serve

The simplest way to serve an app:

```python
app = flyte.serve(app_env)
```

## Serve with input overrides

Override app inputs when serving:

```python
app = flyte.serve(
    app_env,
    input_values={
        "app-name": {
            "input_name": "input_value",
            "model_path": "s3://bucket/models/model.pkl",
        }
    },
)
```

## Using servecontext for advanced options

For more control, use `with_servecontext()`:

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

## Parameters

### `version`

Optional version string for the app:

```python
with with_servecontext(version="dev-v1.0.0") as ctx:
    app = ctx.serve(app_env)
```

If not specified, Flyte generates a version automatically.

### `project` and `domain`

Override the project and domain:

```python
with with_servecontext(
    project="my-project",
    domain="development",
) as ctx:
    app = ctx.serve(app_env)
```

### `env_vars`

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

### `input_values`

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

### `cluster_pool`

Target a specific cluster pool:

```python
with with_servecontext(cluster_pool="gpu-pool") as ctx:
    app = ctx.serve(app_env)
```

### `log_level` and `log_format`

Control logging:

```python
import logging

with with_servecontext(
    log_level=logging.DEBUG,
    log_format="json",  # or "console"
) as ctx:
    app = ctx.serve(app_env)
```

### `dry_run`

Preview what would be deployed without actually deploying:

```python
with with_servecontext(dry_run=True) as ctx:
    app = ctx.serve(app_env)  # Doesn't actually deploy
```

## CLI options

When using the CLI, options are passed as flags:

```bash
flyte serve path/to/app.py app_name \
    --version v1.0.0 \
    --project my-project \
    --domain development \
    --env-var LOG_LEVEL=DEBUG \
    --input-value model_path=s3://bucket/model.pkl \
    --cluster-pool gpu-pool
```

## Example: Full serve configuration

```python
import logging
import flyte
from flyte import with_servecontext

app_env = flyte.app.AppEnvironment(
    name="my-app",
    # ... configuration ...
)

if __name__ == "__main__":
    flyte.init_from_config()
    
    with with_servecontext(
        version="dev-1.0.0",
        project="my-project",
        domain="development",
        env_vars={
            "LOG_LEVEL": "DEBUG",
            "ENVIRONMENT": "dev",
        },
        input_values={
            "my-app": {
                "model_path": "s3://dev-bucket/models/dev-model.pkl",
                "debug": "true",
            }
        },
        cluster_pool="development-pool",
        log_level=logging.DEBUG,
        log_format="console",
    ) as ctx:
        app = ctx.serve(app_env)
        print(f"Served app: {app.url}")
        print(f"Status: {app.status}")
```

## Best practices

1. **Use versioning**: Always specify versions for reproducibility
2. **Separate environments**: Use different projects/domains for dev/staging/prod
3. **Input overrides**: Leverage input overrides for testing different configurations
4. **Logging**: Use appropriate log levels and formats for your use case
5. **Cluster pools**: Target appropriate cluster pools for your workload

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

