---
title: Serve and deploy apps
weight: 12
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Serve and deploy apps

Flyte provides two main ways to deploy apps: **serve** (for development) and **deploy** (for production). This section covers both methods and their differences.

## Serve vs Deploy

### `flyte serve`

Serving is designed for development and iteration:

- **Dynamic input modification**: You can override app inputs when serving
- **Quick iteration**: Faster feedback loop for development
- **Interactive**: Better suited for testing and experimentation

### `flyte deploy`

Deployment is designed for production use:

- **Immutable**: Apps are deployed with fixed configurations
- **Production-ready**: Optimized for stability and reproducibility

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
flyte serve path/to/app.py app_env

# Deploy
flyte deploy path/to/app.py app_env
```

## Next steps

- [**How app serving works**](./how-app-serving-works): Understanding the serve process and configuration options
- [**How app deployment works**](./how-app-deployment-works): Understanding the deploy process and configuration options
- [**Activating and deactivating apps**](./activating-and-deactivating-apps): Managing app lifecycle
- [**Prefetching models**](./prefetching-models): Download and shard HuggingFace models for vLLM and SGLang
