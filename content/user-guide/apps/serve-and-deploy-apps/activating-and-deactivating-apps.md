---
title: Activating and deactivating apps
description: Turn a deployed app on and off, and what activation means for each deploy method.
icon: toggle-on
weight: 5
variants: +flyte +union
---

# Activating and deactivating apps

Apps deployed with `flyte.deploy()` and apps served with `flyte.serve()` are activated automatically. Use `deactivate()` and `activate()` to turn a deployed app off and on.

## Activation

### Activate an app

When you get an app by name, you get the current app instance:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=activate-app lang=python >}}

### Check activation status

Check if an app is active:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=check-activation-status lang=python >}}

## Deactivation

Deactivate an app when you no longer need it:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=deactivation lang=python >}}

## Lifecycle management

### Typical deployment workflow

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=typical-deployment-workflow lang=python >}}

### Update a live app without downtime

To update a running app, deploy it again. The deploy creates a new revision of the app. The current revision keeps serving requests until the new one is ready, and then all traffic moves to the new revision:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=zero-downtime-update lang=python >}}

- If the new revision never becomes ready, the current revision keeps serving.
- If the app's spec hasn't changed, the deploy does nothing and no new revision is created.

### Test a new version before it takes traffic

Traffic moves to a new revision as soon as it's ready, so you can't check a revision of the live app before users reach it. To test a new version first, deploy it as a separate app next to the live one, then roll it out:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=test-before-switching lang=python >}}

The candidate has its own URL, so the live app's traffic doesn't reach it. It isn't isolated in other ways:

- The candidate keeps the live app's `depends_on`, so deploying it also deploys those environments under their live names. To leave them untouched, pass `depends_on=[]` to `clone_with()`, or point it at test copies.
- The candidate has the same secrets and environment variables as the live app. If your checks write data, point the candidate at test resources.

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

Use `--project` and `--domain` to target a specific [project-domain pair](../../get-started/core-concepts/projects-and-domains).
For all available options, see the [CLI reference](../../../api-reference/flyte-cli).

## Best practices

1. **Test before deploying**: Test with serve or a dry run before deploying
2. **Version management**: Keep track of which version is active
3. **Zero-downtime updates**: Update a running app by redeploying it, and test risky versions as a separate app first
4. **Monitor**: Monitor apps after activation
5. **Cleanup**: Deactivate and remove old versions periodically

## Automatic activation with serve

Apps served with `flyte.serve()` are automatically activated:

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=automatic-activation lang=python >}}

This is convenient for development. For production, use `flyte.deploy()`, which also activates the app, and use `deactivate()` and `activate()` to control it afterwards.

## Example: Complete deployment and activation

{{< code file="/unionai-examples/v2/user-guide/serve-and-deploy-apps/activation_examples.py" fragment=complete-example lang=python >}}

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
