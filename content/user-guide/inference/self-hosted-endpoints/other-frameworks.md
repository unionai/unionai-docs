---
title: Other frameworks
description: "Serve models with Ray Serve, LitServe, BentoML, or any other ML serving framework by running its server in a generic AppEnvironment."
icon: cpu
weight: 6
variants: +flyte +union
keywords:
  - Ray Serve
  - LitServe
  - BentoML
  - MLServer
  - model serving frameworks
  - custom model server
---

# Other frameworks

Any framework that runs an HTTP server can serve a model on your compute. Flyte doesn't need a dedicated integration: a generic [`AppEnvironment`](../../apps/build-apps/single-script-apps) runs the server and routes traffic to it.

Every framework follows the same three steps:

1. **Install the framework in the image**, with `flyte.Image` and `with_pip_packages`.
2. **Start the server with `args`**, using either the framework's CLI or a Python entrypoint.
3. **Bind the server to `0.0.0.0` on the app's `port`**, so the platform can reach it. The default port is `8080`.

The examples below serve the same sentiment classifier, so you can compare the frameworks directly.

| Framework | Good fit for |
|---|---|
| [LitServe](#litserve) | A small `LitAPI` class with built-in batching and GPU handling |
| [Ray Serve](#ray-serve) | Multiple replicas or multi-model pipelines inside one app, using Ray's programming model |
| [BentoML](#bentoml) | Typed service classes with generated API schemas, or an existing Bento service |
| [Any other server](#any-other-server) | A framework you already use |

## LitServe

[LitServe](https://lightning.ai/docs/litserve) serves a `LitAPI` class. Start it through a `--server` entrypoint in the script:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/litserve_endpoint.py" fragment="app-env" lang=python >}}

The `--server` entrypoint starts LitServe on the app port:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/litserve_endpoint.py" fragment="server" lang=python >}}

Deploy with `flyte.serve`, and run the server when the container passes `--server`:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/litserve_endpoint.py" fragment="deploy" lang=python >}}

LitServe serves `POST /predict` by default.

## Ray Serve

[Ray Serve](https://docs.ray.io/en/latest/serve/) runs deployments on a Ray cluster. In this pattern, Ray runs inside a single app replica, so size `resources` for all of the Ray Serve replicas plus Ray's own processes:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/ray_serve_endpoint.py" fragment="app-env" lang=python >}}

`serve.start` binds the Ray Serve proxy to the app port. `serve.run` returns once the deployment is ready, so the entrypoint then blocks to keep the container running:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/ray_serve_endpoint.py" fragment="server" lang=python >}}

Keep the app at one replica, as in `replicas=(0, 1)`, and scale with `num_replicas` in the Ray deployment. Each app replica would otherwise start its own independent Ray instance.

## BentoML

[BentoML](https://docs.bentoml.com/) defines a service as a class. Each `@bentoml.api` method becomes a `POST` route named after the method:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/bentoml_endpoint.py" fragment="service" lang=python >}}

BentoML has its own CLI, so `args` can start the server directly:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/bentoml_endpoint.py" fragment="app-env" lang=python >}}

## Any other server

The same pattern works for other servers. Point `args` at the command that starts the server and make sure it listens on `0.0.0.0` and the app's `port`:

| Framework | What it serves | Notes |
|---|---|---|
| [MLServer](https://mlserver.readthedocs.io/) | Scikit-learn, XGBoost, LightGBM, and MLflow models | Started with `mlserver start`. Set the port in `settings.json`. |
| [MLflow](https://mlflow.org/docs/latest/) | Models in the MLflow format | Started with `mlflow models serve`, which takes `--host` and `--port`. |
| [Gradio](https://www.gradio.app/) | A browser demo with an HTTP API | Set `GRADIO_SERVER_NAME` to `0.0.0.0` and `GRADIO_SERVER_PORT` to the app port. |

> [!NOTE]
> [TorchServe](https://docs.pytorch.org/serve/) is no longer maintained, and its repository was archived in August 2025. For new PyTorch endpoints, use one of the frameworks on this page or a [FastAPI endpoint](./fastapi).

For an LLM, start with the [vLLM](./vllm), [SGLang](./sglang), [Ollama](./ollama), or [llama.cpp](./llamacpp) endpoints.

## Deploy, call, and scale

All of these run as ordinary apps, so the rest of the app documentation applies:

- **Authentication**: `requires_auth=True` is the default and sits in front of the framework's own server. See [Secret-based authentication](../../apps/build-apps/secret-based-authentication) for app-managed auth.
- **Scaling**: See [Autoscaling apps](../../apps/configure-apps/auto-scaling-apps).
- **Weights**: See [Prefetching models](../prefetching-models) and [Deploy trained models](../deploy-trained-models).

## Troubleshooting

**The app never becomes ready:**

- Confirm the server binds `0.0.0.0` rather than `localhost`. Many frameworks default to `localhost` or use their own default port, such as 3000 for BentoML and 8000 for Ray Serve.
- Check that the server's port matches `port` on the `AppEnvironment`.
- Avoid the reserved ports 8012, 8022, 8112, and 9090.

**The server starts, then the container exits:**

- The `args` command must stay in the foreground. If the entrypoint only starts a background server, as Ray Serve's does, block afterward.

**Slow first response:**

- The model loads at startup, so a replica scaling up from zero takes that long to respond. Raise `scaledown_after`, keep a minimum replica, or [prefetch the weights](../prefetching-models).
