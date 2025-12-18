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

```python
import flyte
from flyte.remote import App

# Deploy the app
deployments = flyte.deploy(app_env)

# Activate the app
app = App.get(name=app_env.name)
app.activate()

print(f"Activated app: {app.name}")
print(f"URL: {app.url}")
```

### Activate an app

When you get an app by name, you get the current app instance:

```python
app = App.get(name="my-app")
app.activate()
```

### Check activation status

Check if an app is active:

```python
app = App.get(name="my-app")
    print(f"Active: {app.is_active()}")
    print(f"Revision: {app.revision}")
```

## Deactivation

Deactivate an app when you no longer need it:

```python
app = App.get(name="my-app")
app.deactivate()

print(f"Deactivated app: {app.name}")
```

## Lifecycle management

### Typical deployment workflow

```python
# 1. Deploy new version
deployments = flyte.deploy(
    app_env,
    version="v2.0.0",
)

    # 2. Get the deployed app
    new_app = App.get(name="my-app")
    # Test endpoints, etc.

    # 3. Activate the new version
    new_app.activate()

    print(f"Deployed and activated version {new_app.revision}")
```

### Blue-green deployment

For zero-downtime deployments:

```python
# Deploy new version without deactivating old
new_deployments = flyte.deploy(
    app_env,
    version="v2.0.0",
)

    new_app = App.get(name="my-app")

    # Test new version
    # ... testing ...

    # Switch traffic to new version
    new_app.activate()

    print(f"Activated revision {new_app.revision}")
```

### Rollback

Roll back to a previous version:

```python
    # Deactivate current version
    current_app = App.get(name="my-app")
    current_app.deactivate()

    print(f"Deactivated revision {current_app.revision}")
```

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
flyte app status my-app
```

## Best practices

1. **Activate after testing**: Test deployed apps before activating
2. **Version management**: Keep track of which version is active
3. **Rollback plan**: Always have a rollback strategy
4. **Blue-green deployments**: Use blue-green for zero-downtime
5. **Monitor**: Monitor apps after activation
6. **Cleanup**: Deactivate and remove old versions periodically

## Automatic activation with serve

Apps served with `flyte.serve()` are automatically activated:

```python
# Automatically activated
app = flyte.serve(app_env)
print(f"Active: {app.is_active()}")  # True
```

This is convenient for development but less suitable for production where you want explicit control over activation.

## Example: Complete deployment and activation

```python
import flyte
import flyte.app
from flyte.remote import App

app_env = flyte.app.AppEnvironment(
    name="my-prod-app",
    # ... configuration ...
)

if __name__ == "__main__":
    flyte.init_from_config()
    
    # Deploy
    deployments = flyte.deploy(
        app_env,
        version="v1.0.0",
        project="my-project",
        domain="production",
    )
    
    # Get the deployed app
    app = App.get(name="my-prod-app")
    
    # Activate
    app.activate()
    
    print(f"Deployed and activated: {app.name}")
    print(f"Revision: {app.revision}")
    print(f"URL: {app.url}")
    print(f"Active: {app.is_active()}")
```

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

