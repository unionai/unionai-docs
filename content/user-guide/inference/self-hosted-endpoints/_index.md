---
title: Self-hosted endpoints
description: "Serve open-weight LLMs on your own GPUs or CPUs behind an OpenAI-compatible endpoint, with vLLM, SGLang, Ollama, or llama.cpp."
icon: cpu
weight: 2
variants: +flyte +union
keywords:
  - self-hosted LLM
  - model serving
  - OpenAI-compatible endpoint
  - vLLM
  - SGLang
  - Ollama
  - llama.cpp
---

# Self-hosted endpoints

Serve an open-weight model as an app on your own compute, behind an endpoint that exposes the OpenAI API. Code written against the OpenAI SDK reaches any of them by changing the base URL, the API key, and the model name.

| You want to | Use |
|---|---|
| Serve an LLM at high throughput | [vLLM endpoint](./vllm) |
| Serve an LLM with structured generation | [SGLang endpoint](./sglang) |
| Serve a small LLM with minimal setup | [Ollama endpoint](./ollama) |
| Serve quantized GGUF weights, a model larger than VRAM, or a model on CPU only | [llama.cpp endpoint](./llamacpp) |

{{< subpage-cards >}}
