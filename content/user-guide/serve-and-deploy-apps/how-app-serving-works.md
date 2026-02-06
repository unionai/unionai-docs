---
title: How app serving works
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# How app serving works

Serving is the recommended way to deploy apps during development. It provides a faster feedback loop and allows you to dynamically modify parameters.

## Overview

When you serve an app, the following happens:

1. **Code bundling**: Your app code is bundled and prepared
2. **Image building**: Container images are built (if needed)
3. **Deployment**: The app is deployed to your Flyte cluster
4. **Activation**: The app is automatically activated and ready to use
5. **URL generation**: A URL is generated for accessing the app

## Using the Python SDK

The simplest way to serve an app:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_examples.py" fragment=basic-serve lang=python >}}

## Overriding parameters

One key advantage of serving is the ability to override parameters dynamically:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_examples.py" fragment=override-parameters lang=python >}}

This is useful for:
- Testing different configurations
- Using different models or data sources
- A/B testing during development

## Advanced serving options

Use `with_servecontext()` for more control over the serving process:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_examples.py" fragment=advanced-serving lang=python >}}

## Using CLI

You can also serve apps from the command line:

```bash
flyte serve path/to/app.py app
```

Where `app` is the variable name of the `AppEnvironment` object.

## Return value

`flyte.serve()` returns an `App` object with:

- `url`: The app's URL
- `endpoint`: The app's endpoint URL
- `deployment_status`: Current status of the app
- `name`: App name

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_examples.py" fragment=return-value lang=python >}}

## Best practices

1. **Use for development**: App serving is ideal for development and testing.
2. **Override parameters**: Take advantage of parameter overrides for testing different configurations.
3. **Quick iteration**: Use `serve` for rapid development cycles.
4. **Switch to deploy**: Use [deploy](./how-app-deployment-works) for production deployments.

## Troubleshooting

**App not activating:**
- Check cluster connectivity
- Verify app configuration is correct
- Review container logs for errors

**Parameter overrides not working:**
- Verify parameter names match exactly
- Check that parameters are defined in the app environment
- Ensure you're using the `input_values` parameter correctly

**Slow serving:**
- Images may need to be built (first time is slower).
- Large code bundles can slow down deployment.
- Check network connectivity to the cluster.
