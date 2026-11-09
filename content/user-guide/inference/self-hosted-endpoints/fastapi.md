---
title: FastAPI
description: "Serve any Python model behind a custom REST API on your own compute with FastAPI, for models and request shapes an LLM server doesn't cover."
icon: cpu
weight: 6
variants: +flyte +union
keywords:
  - FastAPI model serving
  - custom inference endpoint
  - self-hosted model API
  - REST API for ML models
---

# FastAPI

[FastAPI](https://fastapi.tiangolo.com/) gives you full control over an endpoint's routes, request schema, and pre- and post-processing. Use it for models an LLM server doesn't cover, such as classifiers, embedding models, and scikit-learn or PyTorch models, or when an LLM needs custom logic around it.

Flyte's [`FastAPIAppEnvironment`](../../apps/native-app-integrations/fastapi-app) runs a FastAPI app with Uvicorn on your compute, so you only write the app. Unlike the vLLM, SGLang, Ollama, llama.cpp, and oMLX endpoints, this endpoint doesn't expose the OpenAI API unless you implement those routes yourself.

## Define the API

This example serves a sentiment classifier from Hugging Face. The `lifespan` handler loads the model once per replica, before the app accepts traffic:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/fastapi_endpoint.py" fragment="api" lang=python >}}

`predict` is a plain `def`, so FastAPI runs it in a thread pool and the blocking model call doesn't hold up the event loop.

## Define the app environment

Pass the FastAPI app to the environment, along with the image and the resources the model needs:

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/fastapi_endpoint.py" fragment="app-env" lang=python >}}

To run on a GPU, add a `gpu` value to `resources` and pass `device=0` to `pipeline`.

## Deploy

{{< code file="/unionai-examples/v2/user-guide/inference/self-hosted-endpoints/fastapi_endpoint.py" fragment="deploy" lang=python >}}

## Call the endpoint

With `requires_auth=True`, the default, callers authenticate with an API key:

```bash
curl -X POST "https://your-app-url/predict" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $FLYTE_API_KEY" \
  -d '{"text": "I love this"}'
```

FastAPI also generates interactive API docs at `/docs`. For app-managed authentication, see [Secret-based authentication](../../apps/build-apps/secret-based-authentication).

## Next steps

- Load your own weights instead of a Hugging Face model: [Deploy trained models](../deploy-trained-models)
- Avoid downloading weights on every cold start: [Prefetching models](../prefetching-models)
- Tune replicas and scale-to-zero: [Autoscaling apps](../../apps/configure-apps/auto-scaling-apps)
- Use a dedicated serving framework: [Other frameworks](./other-frameworks)
