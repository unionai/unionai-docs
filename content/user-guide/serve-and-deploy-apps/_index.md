---
title: Serve and deploy apps
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Serve and deploy apps

Flyte provides two main ways to deploy apps: **serve** (for development) and **deploy** (for production). This section covers both methods and their differences.

## Serve vs Deploy

### `flyte serve` - Development

Serving is designed for development and iteration:

- **Dynamic input modification**: You can override app inputs when serving
- **Quick iteration**: Faster feedback loop for development
- **Interactive**: Better suited for testing and experimentation
- **Auto-activation**: Apps are automatically activated when served

### `flyte deploy` - Production

Deployment is designed for production use:

- **Immutable**: Apps are deployed with fixed configurations
- **Versioned**: Each deployment creates a versioned app
- **Production-ready**: Optimized for stability and reproducibility
- **Manual activation**: Apps need to be explicitly activated/deactivated

## Topics

- [**How app serving works**](./how-app-serving-works): Understanding the serve process
- [**App serve options**](./app-serve-options): Configuration options for serving
- [**How app deployment works**](./how-app-deployment-works): Understanding the deploy process
- [**Deploy command options**](./deploy-command-options): Configuration options for deployment
- [**Activating and deactivating apps**](./activating-and-deactivating-apps): Managing app lifecycle
- [**Prefetching models**](./prefetching-models): Download and shard HuggingFace models for vLLM and SGLang

## Quick start

### Using Python SDK

```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-app",
    # ... configuration ...
)

# Serve (development)
if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.serve(app_env)
    print(f"Served at: {app.url}")

# Deploy (production)
if __name__ == "__main__":
    flyte.init_from_config()
    deployments = flyte.deploy(app_env)
    print(f"Deployed: {deployments[0].url}")
```

### Using CLI

```bash
# Serve
flyte serve path/to/app.py app_name

# Deploy
flyte deploy path/to/app.py app_name
```

## Next steps

- Learn [how serving works](./how-app-serving-works) for development
- Understand [deployment process](./how-app-deployment-works) for production
- Explore [prefetching models](./prefetching-models) for vLLM and SGLang apps

