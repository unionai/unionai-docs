---
title: Deploy command options
weight: 4
variants: +flyte +serverless +byoc +selfmanaged
---

# Deploy command options

This page documents the options available when deploying apps using `flyte.deploy()` or the CLI.

## Basic deploy

The simplest way to deploy:

```python
deployments = flyte.deploy(app_env)
```

## Deploy with input overrides

You can override inputs at deploy time (though less common than with serve):

```python
deployments = flyte.deploy(
    app_env,
    input_values={
        "app-name": {
            "input_name": "input_value",
        }
    },
)
```

Note: Input overrides at deploy time are less flexible than with serve. Consider using `flyte.serve()` for development where you need frequent input changes.

## Using deployment context

For more control, use deployment context (similar to serve context):

```python
from flyte import with_deploycontext

with with_deploycontext(
    version="v1.0.0",
    project="my-project",
    domain="production",
    dry_run=False,
) as ctx:
    deployments = ctx.deploy(app_env)
```

## Parameters

### `version`

Version string for the deployment:

```python
deployments = flyte.deploy(app_env, version="v1.0.0")
```

If not specified, Flyte generates a version automatically based on code and configuration.

### `project` and `domain`

Override project and domain:

```python
deployments = flyte.deploy(
    app_env,
    project="my-project",
    domain="production",
)
```

### `input_values`

Override app inputs at deploy time:

```python
deployments = flyte.deploy(
    app_env,
    input_values={
        "app-name": {
            "model_path": "s3://prod-bucket/models/model.pkl",
        }
    },
)
```

### `dry_run`

Preview deployment without actually deploying:

```python
deployments = flyte.deploy(app_env, dry_run=True)
```

This is useful for:
- Validating deployment configuration
- Checking what would be deployed
- Testing deployment logic

## CLI options

When using the CLI:

```bash
flyte deploy path/to/app.py app_name \
    --version v1.0.0 \
    --project my-project \
    --domain production \
    --dry-run
```

## Example: Full deployment configuration

```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-prod-app",
    # ... configuration ...
)

if __name__ == "__main__":
    flyte.init_from_config()
    
    deployments = flyte.deploy(
        app_env,
        version="v1.0.0",
        project="my-project",
        domain="production",
        input_values={
            "my-prod-app": {
                "model_path": "s3://prod-bucket/models/v1-model.pkl",
            }
        },
        dry_run=False,
    )
    
    for deployment in deployments:
        print(f"Deployed: {deployment.env.name}")
        print(f"Version: {deployment.version}")
        print(f"URL: {deployment.url}")
        
        # Activate the app
        from flyte.remote import App
        app = App.get(name=deployment.env.name)
        app.activate()
        print(f"Activated: {app.name}")
```

## Deployment return value

`flyte.deploy()` returns a list of `DeployedEnvironment` objects:

```python
deployments = flyte.deploy(app_env)

for deployment in deployments:
    # Access deployed environment
    env = deployment.env
    
    # Access deployment info
    print(f"Name: {env.name}")
    print(f"Version: {deployment.version}")
    print(f"URL: {deployment.url}")
    print(f"Status: {deployment.status}")
```

Each `DeployedEnvironment` includes:
- `env`: The `AppEnvironment` that was deployed
- `version`: The version of the deployment
- `url`: The app's URL
- `status`: Current deployment status

## Best practices

1. **Always version**: Use explicit versions for production deployments
2. **Use dry-run**: Test deployments with `dry_run=True` first
3. **Separate environments**: Use different projects/domains for different environments
4. **Input management**: Consider using environment-specific input values
5. **Activation strategy**: Have a clear strategy for activating apps after deployment
6. **Rollback plan**: Keep previous versions available for rollback

## Differences from serve options

Deploy options are more limited than serve options:

- **No dynamic input overrides**: Inputs are fixed at deploy time
- **No automatic activation**: Apps must be activated manually
- **More versioning focus**: Versions are more important for production
- **Dry-run support**: Better support for previewing deployments

## Troubleshooting

**Version conflicts:**
- Use unique versions for each deployment
- Check existing app versions
- Consider using semantic versioning

**Deployment fails:**
- Use `dry_run=True` to preview deployment
- Check that all dependencies are available
- Verify image builds succeed

**Input overrides not working:**
- Remember that deploy-time input overrides are less flexible than serve
- Consider using serve for development/testing with frequent input changes
- Use environment-specific configuration for production

