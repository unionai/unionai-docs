---
title: llama.cpp endpoint
description: Serve quantized GGUF models with llama-server as a Flyte app, on GPU or CPU, behind an OpenAI-compatible API.
icon: cpu
weight: 5
variants: +flyte +union
---

# llama.cpp endpoint

The `flyteplugins-llamacpp` plugin serves GGUF models with [llama.cpp](https://github.com/ggml-org/llama.cpp)'s `llama-server` as a Flyte app. `LlamaCppAppEnvironment` exposes an OpenAI-compatible API under `/v1` and the llama.cpp Web UI at `/`.

Use it for quantized GGUF weights, for models larger than your GPU's VRAM, and for CPU-only serving. For high-throughput serving of full-precision weights, use [vLLM](./vllm-app) or [SGLang](./sglang-app).

## Installation

```bash
pip install flyteplugins-llamacpp
```

## Serve a model from Hugging Face

Set `model_hf_path` to a GGUF repo, with an optional quantization tag. `llama-server` downloads the weights when the app starts:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="hugging-face" lang="python" >}}

Serve the app:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="deploy" lang="python" >}}

## Serve a model from object storage

Set `model_path` to a directory of GGUF weights, or to one `.gguf` file:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="object-storage" lang="python" >}}

The weights are downloaded into the container, so set `disk` to fit them. If the directory holds a sharded model, the app selects the `-00001-of-` shard and `llama-server` finds the rest. If it holds several unrelated `.gguf` files, the app serves the first one by sorted path.

`model_path` also accepts a `flyte.app.RunOutput`, to serve the output of a task. See [Deploy trained models](./deploy-trained-models).

{{< variant union >}}
{{< markdown >}}

It accepts a `flyte.app.ArtifactValue` too, to serve a [model artifact](../artifacts/artifacts-in-apps).

{{< /markdown >}}
{{< /variant >}}

Set `model_path` or `model_hf_path`, not both. `model_id` is required, and it's the name callers pass as `model`.

## Call the app

Use any OpenAI client:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/call_app.py" fragment="client" lang="python" >}}

`llama-server` checks no key of its own unless you pass `--api-key` in `extra_args`.

{{< variant union >}}
{{< markdown >}}

With `requires_auth=True` (the default), pass a Union API key as `api_key`. See [Calling an authenticated app](./ollama-app#calling-an-authenticated-app).

{{< /markdown >}}
{{< /variant >}}

## Choose an image

The default image compiles `llama-server` from source with CUDA for L4 and L40S GPUs (compute capability 8.9). The source build makes the first image build slow.

To target other GPUs, or to pin a llama.cpp release for reproducible builds, use `build_llama_cpp_image()`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="custom-image" lang="python" >}}

To serve small models without a GPU, build a CPU-only image:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="cpu-only" lang="python" >}}

> [!WARNING] Match the image to the GPU
> The default image targets only compute capability 8.9. On another GPU, such as an A100 or H100, set `cuda_arch` to include it.

## Pass arguments to llama-server

`extra_args` is appended to the `llama-server` command, as a string or a list:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="extra-args" lang="python" >}}

| Flag | Purpose |
|---|---|
| `--ctx-size` | Context length |
| `--parallel` | Concurrent request slots |
| `--jinja` | Use the model's chat template, which tool calling needs |
| `--n-gpu-layers` | Limit GPU offload for a model larger than VRAM |
| `--cache-type-k`, `--cache-type-v` | Quantize the KV cache |
| `--flash-attn` | Enable flash attention |

Values with spaces or JSON are quoted for you. An argument of the form `$MY_VAR` isn't quoted, and Flyte expands it from the app's environment.

See the [llama-server docs](https://github.com/ggml-org/llama.cpp/tree/master/tools/server) for all flags.

## Use speculative decoding

Set `draft_model_path` or `draft_model_hf_path` to a small draft GGUF, and tune it with `extra_args`:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/llamacpp/llamacpp_apps.py" fragment="speculative" lang="python" >}}

## Limitations

`LlamaCppAppEnvironment` sets its own command and parameters. Passing `args` or `parameters` raises a `ValueError`, so use `extra_args` and `model_path` instead.

## API reference

See the [llama.cpp API reference](../../api-reference/integrations/llamacpp/_index).
