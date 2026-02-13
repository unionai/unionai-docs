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

## Using the Python SDK

Deploy an app:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=basic-deploy lang=python >}}

`flyte.deploy()` returns a list of `Deployment` objects. Each `Deployment` contains a dictionary of `DeployedEnvironment` objects (one for each environment deployed, including environment dependencies). For apps, the `DeployedEnvironment` is a `DeployedAppEnvironment` which has a `deployed_app` property of type `App`.


## Deployment plan

Flyte automatically creates a deployment plan that includes:

- The app you're deploying
- All [app environment dependencies](../configure-apps/apps-depending-on-environments) (via `depends_on`)
- Proper deployment order

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=deployment-plan lang=python >}}

## Overriding App configuration at deployment time

If you need to override the app configuration at deployment time, you can use the `clone_with` method to create a new
app environment with the desired overrides.

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=clone-with lang=python >}}

## Activation/deactivation

Unlike serving, deployment does not automatically activate apps. You need to activate them explicitly:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=activation-deactivation lang=python >}}

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

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=full-deployment lang=python >}}

## Best practices

1. **Use for production**: Deploy is designed for production use.
2. **Version everything**: Always specify versions for reproducibility.
3. **Test first**: Test with serve before deploying to production.
4. **Manage dependencies**: Use `depends_on` to manage app dependencies.
5. **Activation strategy**: Have a strategy for activating/deactivating apps.
7. **Use dry-run**: Test deployments with `dry_run=True` first.
8. **Separate environments**: Use different projects/domains for different environments.
9. **Parameter management**: Consider using environment-specific parameter values.

## Deployment status and return value

`flyte.deploy()` returns a list of `Deployment` objects. Each `Deployment` contains a dictionary of `DeployedEnvironment` objects:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/deploy_examples.py" fragment=deployment-status lang=python >}}

For apps, each `DeployedAppEnvironment` includes:

- `env`: The `AppEnvironment` that was deployed
- `deployed_app`: The `App` object with properties like `url`, `endpoint`, `name`, and `deployment_status`

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

