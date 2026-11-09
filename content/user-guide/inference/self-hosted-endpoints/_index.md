---
title: Self-hosted endpoints
description: "Serve models on your own GPUs or CPUs, with vLLM, SGLang, Ollama, llama.cpp, FastAPI, Ray Serve, LitServe, BentoML, or another framework."
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
  - FastAPI
  - Ray Serve
  - LitServe
  - BentoML
---

# Self-hosted endpoints

Serve a model as an app on your own compute. The vLLM, SGLang, Ollama, and llama.cpp endpoints expose the OpenAI API, so code written against the OpenAI SDK reaches any of them by changing the base URL, the API key, and the model name. FastAPI and other frameworks serve any model behind the API you define.

| You want to | Use |
|---|---|
| Serve an LLM at high throughput | [vLLM endpoint](./vllm) |
| Serve an LLM with structured generation | [SGLang endpoint](./sglang) |
| Serve a small LLM with minimal setup | [Ollama endpoint](./ollama) |
| Serve quantized GGUF weights, a model larger than VRAM, or a model on CPU only | [llama.cpp endpoint](./llamacpp) |
| Serve any model behind your own REST API | [FastAPI endpoint](./fastapi) |
| Serve a model with Ray Serve, LitServe, BentoML, or another framework | [Other frameworks](./other-frameworks) |

{{< subpage-cards >}}
