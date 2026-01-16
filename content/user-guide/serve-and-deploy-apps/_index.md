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

{{< markdown >}}
```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-app",
    image=flyte.app.Image.from_debian_base().with_pip_packages("streamlit==1.41.1"),
    args=["streamlit", "hello", "--server.port", "8080"],
    port=8080,
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.serve(app_env)
    print(f"Served at: {app.url}")
```
{{< /markdown >}}
{{< /tab >}}

{{< tab "Deploy" >}}

{{< markdown >}}
```python
import flyte
import flyte.app

app_env = flyte.app.AppEnvironment(
    name="my-app",
    image=flyte.app.Image.from_debian_base().with_pip_packages("streamlit==1.41.1"),
    args=["streamlit", "hello", "--server.port", "8080"],
    port=8080,
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)

if __name__ == "__main__":
    flyte.init_from_config()
    deployments = flyte.deploy(app_env)
    # Access deployed app URL from the deployment
    for deployed_env in deployments[0].envs.values():
        print(f"Deployed: {deployed_env.deployed_app.url}")
```
{{< /markdown >}}
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
