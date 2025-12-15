---
title: How app deployment works
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# How app deployment works

Deployment is the recommended way to deploy apps to production. It creates versioned, immutable app deployments.

## Overview

When you deploy an app:

1. **Code bundling**: Your app code is bundled and versioned
2. **Image building**: Container images are built and tagged
3. **Deployment plan**: A deployment plan is created (including dependencies)
4. **Deployment**: Apps are deployed to your Flyte cluster
5. **Version creation**: Each deployment creates a new version
6. **Activation**: Apps need to be explicitly activated (not automatic)

## Using Python SDK

Deploy an app:

```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-prod-app",
    # ... configuration ...
)

if __name__ == "__main__":
    flyte.init_from_config()
    deployments = flyte.deploy(app_env)
    
    for deployment in deployments:
        print(f"Deployed: {deployment.env.name}")
        print(f"URL: {deployment.url}")
```

`flyte.deploy()` returns a list of `DeployedEnvironment` objects, one for each environment deployed (including dependencies).

### Deploy with input overrides

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

### Using deployment context

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

### Deploy parameters

#### `version`

Version string for the deployment:

```python
deployments = flyte.deploy(app_env, version="v1.0.0")
```

If not specified, Flyte generates a version automatically based on code and configuration.

#### `project` and `domain`

Override project and domain:

```python
deployments = flyte.deploy(
    app_env,
    project="my-project",
    domain="production",
)
```

#### `input_values`

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

#### `dry_run`

Preview deployment without actually deploying:

```python
deployments = flyte.deploy(app_env, dry_run=True)
```

This is useful for:

- Validating deployment configuration
- Checking what would be deployed
- Testing deployment logic

## Deployment plan

Flyte automatically creates a deployment plan that includes:

- The app you're deploying
- All dependencies (via `depends_on`)
- Proper deployment order

```python
app1_env = flyte.app.AppEnvironment(name="backend", ...)
app2_env = flyte.app.AppEnvironment(name="frontend", depends_on=[app1_env], ...)

# Deploying app2_env will also deploy app1_env
deployments = flyte.deploy(app2_env)

# deployments contains both app1_env and app2_env
assert len(deployments) == 2
```

## Activation

Unlike serving, deployment does not automatically activate apps. You need to activate them explicitly:

```python
deployments = flyte.deploy(app_env)

# Activate the deployed app
from flyte.remote import App
app = App.get(name=app_env.name)
app.activate()
```

See [Activating and deactivating apps](./activating-and-deactivating-apps) for more details.

## Using CLI

Deploy from the command line:

```bash
flyte deploy path/to/app.py app_name
```

With options:

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

## What happens during deploy

1. **Code analysis**: Flyte analyzes your app code and dependencies
2. **Version generation**: A version is generated (or you provide one)
3. **Code bundling**: Necessary files are bundled and versioned
4. **Image building**: Container images are built and tagged with the version
5. **Deployment plan**: A plan is created including all dependencies
6. **Sequential deployment**: Apps are deployed in the correct order
7. **Status check**: Deployment status is reported

## Differences from serve

| Feature | Deploy | Serve |
|---------|--------|-------|
| **Purpose** | Production | Development |
| **Input overrides** | ❌ Fixed at deploy time | ✅ Supported |
| **Activation** | ❌ Manual | ✅ Automatic |
| **Versioning** | ✅ Required | Optional |
| **Reproducibility** | ✅ High | Lower |
| **Dependencies** | ✅ Explicit handling | Automatic |

## Best practices

1. **Use for production**: Deploy is designed for production use.
2. **Version everything**: Always specify versions for reproducibility.
3. **Test first**: Test with serve before deploying to production.
4. **Manage dependencies**: Use `depends_on` to manage app dependencies.
5. **Activation strategy**: Have a strategy for activating/deactivating apps.
6. **Rollback plan**: Keep old versions available for rollback.
7. **Use dry-run**: Test deployments with `dry_run=True` first.
8. **Separate environments**: Use different projects/domains for different environments.
9. **Input management**: Consider using environment-specific input values.

## Deployment status and return value

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

## Troubleshooting

**Deployment fails:**
- Check that all dependencies are available
- Verify image builds succeed
- Review deployment logs

**App not accessible:**
- Ensure the app is activated
- Check cluster connectivity
- Verify app configuration

**Version conflicts:**
- Use unique versions for each deployment
- Check existing app versions
- Clean up old versions if needed

