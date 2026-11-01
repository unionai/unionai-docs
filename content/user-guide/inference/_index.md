---
title: Inference
description: Run models from Flyte by calling a hosted provider, serving open-weight models on your own GPUs, or deploying the models your tasks train.
icon: cpu
weight: 4
variants: +flyte +union
---

# Inference

Choose how to run a model based on where it lives and how you call it:

| You want to | Use |
|---|---|
| Call a hosted model such as Fireworks, OpenAI, or Anthropic from a task or app | [Providers](./providers) |
| Serve an open-weight LLM on your own GPUs at high throughput | [vLLM app](./vllm-app) or [SGLang app](./sglang-app) |
| Serve a small LLM with minimal setup | [Ollama app](./ollama-app) |
| Serve quantized GGUF weights, a model larger than VRAM, or a model on CPU only | [llama.cpp](../../integrations/llamacpp/_index) |
| Copy Hugging Face weights into your storage before serving them | [Prefetching models](./prefetching-models) |
| Serve a model you trained in a task | [Deploy trained models](./deploy-trained-models) |
| Score a dataset on GPUs as a job, with no endpoint | [Batch inference](../run-scaling/batch-inference) |
| Load weights inside a task from object storage | [Stream model weights](../run-scaling/stream-model-weights) |

Most hosted providers, and the vLLM, SGLang, Ollama, and llama.cpp apps, expose the OpenAI API or an endpoint compatible with it. Code written against the OpenAI SDK moves between them by changing the base URL, the API key, and the model name. Some providers, such as Anthropic, need their own SDK. See [Providers](./providers#providers-with-their-own-sdk).

{{< variant union >}}
{{< markdown >}}

## Route calls through the LLM Gateway

The [LLM Gateway](../llm-gateway/_index) puts one endpoint in front of hosted providers, including Fireworks, and the models you serve with vLLM or SGLang. It adds budgets, fallbacks between providers, and guardrails. See [Choose direct calls or the gateway](./providers#choose-direct-calls-or-the-gateway).

{{< /markdown >}}
{{< /variant >}}

{{< subpage-cards >}}
