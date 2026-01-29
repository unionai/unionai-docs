---
title: Activating and deactivating apps
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Activating and deactivating apps

Apps deployed with `flyte.deploy()` need to be explicitly activated before they can serve traffic. Apps served with `flyte.serve()` are automatically activated.

## Activation

### Activate after deployment

After deploying an app, activate it:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=activate-after-deployment lang=python >}}

### Activate an app

When you get an app by name, you get the current app instance:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=activate-app lang=python >}}

### Check activation status

Check if an app is active:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=check-activation-status lang=python >}}

## Deactivation

Deactivate an app when you no longer need it:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=deactivation lang=python >}}

## Lifecycle management

### Typical deployment workflow

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=typical-deployment-workflow lang=python >}}

### Blue-green deployment

For zero-downtime deployments:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=blue-green-deployment lang=python >}}

## Using CLI

### Activate

```bash
flyte update app --activate my-app
```

### Deactivate

```bash
flyte update app --deactivate my-app
```

### Check status

```bash
flyte get app my-app
```

## Best practices

1. **Activate after testing**: Test deployed apps before activating
2. **Version management**: Keep track of which version is active
4. **Blue-green deployments**: Use blue-green for zero-downtime
5. **Monitor**: Monitor apps after activation
6. **Cleanup**: Deactivate and remove old versions periodically

## Automatic activation with serve

Apps served with `flyte.serve()` are automatically activated:

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=automatic-activation lang=python >}}

This is convenient for development but less suitable for production where you want explicit control over activation.

## Example: Complete deployment and activation

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=complete-example lang=python >}}

## Troubleshooting

**App not accessible after activation:**
- Verify activation succeeded
- Check app logs for startup errors
- Verify cluster connectivity
- Check that the app is listening on the correct port

**Activation fails:**
- Check that the app was deployed successfully
- Verify app configuration is correct
- Check cluster resources
- Review deployment logs

**Cannot deactivate:**
- Ensure you have proper permissions
- Check if there are dependencies preventing deactivation
- Verify the app name and version

