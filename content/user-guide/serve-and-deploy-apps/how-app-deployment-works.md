---
title: How app deployment works
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# How app deployment works

Deployment is the recommended way to deploy apps to production. It creates versioned, immutable app deployments.

## Overview

When you deploy an app, the following happens:

1. **Code bundling**: Your app code is bundled and prepared
2. **Image building**: Container images are built (if needed)
3. **Deployment**: The app is deployed to your Flyte cluster
4. **Activation**: The app is automatically activated and ready to use

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

`flyte.deploy()` returns a list of `DeployedEnvironment` objects, one for each environment deployed (including environment dependencies).


## Deployment plan

Flyte automatically creates a deployment plan that includes:

- The app you're deploying
- All [app environment dependencies](../configure-apps/apps-depending-on-environments) (via `depends_on`)
- Proper deployment order

```python
app1_env = flyte.app.AppEnvironment(name="backend", ...)
app2_env = flyte.app.AppEnvironment(name="frontend", depends_on=[app1_env], ...)

# Deploying app2_env will also deploy app1_env
deployments = flyte.deploy(app2_env)

# deployments contains both app1_env and app2_env
assert len(deployments) == 2
```

## Activation/deactivation

Unlike serving, deployment does not automatically activate apps. You need to activate them explicitly:

```python
deployments = flyte.deploy(app_env)

from flyte.remote import App
app = App.get(name=app_env.name)

# deactivate the app
app.deactivate()

# activate the app
app.activate()
```

See [Activating and deactivating apps](./activating-and-deactivating-apps) for more details.

## Using the CLI

Deploy from the command line:

```bash
flyte deploy path/to/app.py app
```

Where `app` is the variable name of the `AppEnvironment` object.

You can also specify the following options:

```bash
flyte deploy path/to/app.py app \
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
        dryrun=False,
        version="v1.0.0",
        interactive_mode=False,
        copy_style="loaded_modules",
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

