---
title: Serve and deploy apps
weight: 14
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Serve and deploy apps

Flyte provides two main ways to deploy apps: **serve** (for development) and **deploy** (for production). This section covers both methods and their differences.

## Serve vs Deploy

### `flyte serve`

Serving is designed for development and iteration:

- **Dynamic parameter modification**: You can override app parameters when serving
- **Quick iteration**: Faster feedback loop for development
- **Interactive**: Better suited for testing and experimentation

### `flyte deploy`

Deployment is designed for production use:

- **Immutable**: Apps are deployed with fixed configurations
- **Production-ready**: Optimized for stability and reproducibility

## Using Python SDK

{{< tabs "serve-vs-deploy" >}}
{{< tab "Serve" >}}

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_and_deploy_examples.py" fragment=serve-example lang=python >}}
{{< /tab >}}

{{< tab "Deploy" >}}

{{< code file="/external/unionai-examples/v2/user-guide/serve-and-deploy-apps/serve_and_deploy_examples.py" fragment=deploy-example lang=python >}}
{{< /tab >}}
{{< /tabs >}}

## Using the CLI


{{< tabs >}}
{{< tab "Serve" >}}

{{< markdown >}}
```bash
flyte serve path/to/app.py app_env
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Deploy" >}}

{{< markdown >}}
```bash
flyte deploy path/to/app.py app_env
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Next steps

- [**How app serving works**](./how-app-serving-works): Understanding the serve process and configuration options
- [**How app deployment works**](./how-app-deployment-works): Understanding the deploy process and configuration options
- [**Activating and deactivating apps**](./activating-and-deactivating-apps): Managing app lifecycle
- [**Model training and serving**](../first-project/): Train a model with tasks and serve it via FastAPI
- [**Prefetching models**](./prefetching-models): Download and shard HuggingFace models for vLLM and SGLang
