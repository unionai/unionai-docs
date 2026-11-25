---
title: Inference
description: Run models from Flyte by calling a hosted provider, serving open-weight models on your own GPUs, deploying the models your tasks train, or making typed model calls.
icon: cpu
weight: 7
variants: +flyte +union
---

# Inference

Choose how to run a model based on where it lives and how you call it:

| You want to | Use |
|---|---|
| Call a hosted model such as Fireworks, OpenAI, or Anthropic from a task or app | [Providers](./providers/_index) |
| Serve an open-weight LLM on your own GPUs at high throughput | [vLLM endpoint](./self-hosted-endpoints/vllm) or [SGLang endpoint](./self-hosted-endpoints/sglang) |
| Serve a small LLM with minimal setup | [Ollama endpoint](./self-hosted-endpoints/ollama) |
| Serve quantized GGUF weights, a model larger than VRAM, or a model on CPU only | [llama.cpp endpoint](./self-hosted-endpoints/llamacpp) |
| Serve any model behind your own API | [FastAPI endpoint](./self-hosted-endpoints/fastapi) or [Other frameworks](./self-hosted-endpoints/other-frameworks) such as Ray Serve, LitServe, and BentoML |
| Copy Hugging Face weights into your storage before serving them | [Prefetching models](./prefetching-models) |
| Serve a model you trained in a task | [Deploy trained models](./deploy-trained-models) |
| Score a dataset on GPUs as a job, with no endpoint | [Batch inference](./batch-inference) |
| Load weights inside a task from object storage | [Stream model weights](./stream-model-weights) |
| Ask a model many typed questions in one call and branch on calibrated answers | [Decision models](./decision-models/_index) |

Most hosted providers, and vLLM, SGLang, Ollama, and llama.cpp endpoints, expose the OpenAI API or an API compatible with it. Code written against the OpenAI SDK moves between them by changing the base URL, the API key, and the model name. Some providers, such as Anthropic, need their own SDK. See [Providers](./providers/_index#providers-with-their-own-sdk).

{{< variant union >}}
{{< markdown >}}

## Route calls through the Inference Gateway

The [Inference Gateway](./inference-gateway/_index) puts one endpoint in front of hosted providers, including Fireworks, and the models you serve with vLLM or SGLang. It adds budgets, fallbacks between providers, and guardrails. See [Choose direct calls or the gateway](./providers/_index#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}

{{< subpage-cards >}}
