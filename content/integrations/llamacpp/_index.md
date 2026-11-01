---
title: llama.cpp
description: Serve quantized GGUF models with llama-server as a Flyte app, on GPU or CPU, behind an OpenAI-compatible API.
icon: cpu
weight: 3
variants: +flyte +union
---

# llama.cpp

The `flyteplugins-llamacpp` plugin serves GGUF models with [llama.cpp](https://github.com/ggml-org/llama.cpp)'s `llama-server` as a Flyte app. `LlamaCppAppEnvironment` exposes an OpenAI-compatible API under `/v1` and the llama.cpp Web UI at `/`.

Use it for quantized GGUF weights, for models larger than your GPU's VRAM, and for CPU-only serving. For high-throughput serving of full-precision weights, use [vLLM](../../user-guide/inference/vllm-app) or [SGLang](../../user-guide/inference/sglang-app).

## Installation

```bash
pip install flyteplugins-llamacpp
```

## Quickstart

Set `model_hf_path` to a GGUF repo, with an optional quantization tag. `llama-server` downloads the weights when the app starts:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="hugging-face" lang="python" >}}

Serve the app:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="deploy" lang="python" >}}

## Next steps

The [llama.cpp app](../../user-guide/inference/llamacpp-app) guide covers object storage, calling the app, choosing an image, `llama-server` arguments, and speculative decoding.

## API reference

See the [llama.cpp API reference](../../api-reference/integrations/llamacpp/_index).
