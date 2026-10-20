---
title: Stream model weights
description: Load a model's safetensors weights from object storage onto the GPU inside a task, without writing them to local disk.
weight: 5
variants: +flyte +union
icon: download
---

# Stream model weights

`flyte.extras.model_streamer` loads a model's safetensors weights from object storage tensor by tensor, inside a task.
Use it when a GPU task loads a large model, for example in an `alru_cache`d bootstrap on reusable containers (see [Batch inference](./batch-inference#combining-with-reusable-containers)).
The safetensors weights are not written to local disk.
`load_hf_model()` and the vLLM `engine_args()` download every other file under the model's object-store prefix (config, tokenizer, and any non-safetensors files) to local disk.

Requires `flyte` 2.11.1 or later. The streamer needs `torch`, `load_hf_model()` also needs `transformers`, and the vLLM load format needs `vllm` and `flyteplugins-vllm` 2.11.1 or later.

> [!NOTE] Examples pending
> Tested, runnable examples for this page are pending.
> For runnable code, see `examples/genai/vllm/vllm_task_streamed.py`, `examples/ml/embed_streamed.py`, and `examples/ml/batch_inference_streamed.py` in the [flyte-sdk repository at v2.11.1](https://github.com/flyteorg/flyte-sdk/tree/v2.11.1/examples).
> Those examples have not been verified on GPUs, and neither has loading into GPU memory through vLLM.

## Model location

Every entry point takes `path`, the object-store prefix of a Hugging Face–style model directory, such as `s3://bucket/models/qwen2.5-7b`.
The prefix holds the `*.safetensors` files, optionally a `model.safetensors.index.json`, and the config and tokenizer files.
To copy a Hub model there, use `flyte.prefetch.hf_model()` (see [Prefetching models](../apps/serve-and-deploy-apps/prefetching-models)).
A task that takes the model as a `flyte.io.Dir` passes `model.path`.

A local filesystem path, with or without `file://`, is not supported.

## Load a Hugging Face model

`flyte.extras.model_streamer.load_hf_model()` is async. It builds a `transformers` model with its parameters on the `meta` device, then streams each weight onto `device` as it arrives.
It returns the model in eval mode and the local directory holding the config and tokenizer files, so you can load the tokenizer with `AutoTokenizer.from_pretrained(local_dir)`.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `path` | | Object-store prefix of the model. |
| `device` | `"cuda"` | Device the weights are placed on. |
| `dtype` | `None` | Casts floating-point weights. `None` keeps the checkpoint's dtype. |
| `model_class` | `AutoModelForCausalLM` | Any `Auto*` class or concrete `PreTrainedModel` subclass. |
| `local_dir` | A new temporary directory | Where the config and tokenizer files are downloaded. |
| `trust_remote_code` | `False` | Passed to `transformers`. |
| `chunk_size`, `max_concurrency` | 16 MiB, 32 | Byte-range size and number of ranges fetched in parallel. Set `FLYTE_MODEL_LOADER_CHUNK_SIZE` and `FLYTE_MODEL_LOADER_MAX_CONCURRENCY` in the environment to change the defaults. |

Checkpoint tensors that the model has no parameter for are logged and ignored. A parameter that no tensor fills raises `KeyError`.

## Stream into any module

`ModelStreamer(path, chunk_size=None, max_concurrency=None)` is the streamer underneath, for models that are not `transformers` models.
It uses the same `chunk_size` and `max_concurrency` defaults as `load_hf_model()`.

- `stream(device=None, dtype=None)`: an async iterator of `(name, tensor)` pairs, in the order the tensors finish downloading. With `device`, each tensor is moved there as it arrives. With `dtype`, floating-point tensors are cast.
- `stream_sync(device=None, dtype=None)`: the same, as a regular iterator. It works from any thread, including one with a running event loop.
- `state_dict(device=None, dtype=None)`: collects every tensor into a dict.
- `load_into(module, device=None, dtype=None, strict=True, key_mapping=None)`: streams the weights into a module's parameters and buffers, replacing each entry as it arrives. Build the module with `with empty_weights():` so its parameters are on `meta` and never allocated twice. Then pass `device`: a `meta` entry with no `device` raises `ValueError`. After the stream ends, `load_into()` calls the module's `tie_weights()` if it has one. With `strict=True`, a parameter left on `meta` or an unmatched checkpoint tensor raises `KeyError`. With `strict=False`, it returns a `LoadResult` listing `missing_keys` and `unexpected_keys`.
- `download_metadata(local_dir)`: downloads everything under the prefix except the `*.safetensors` files.

## Load weights into vLLM

`flyteplugins-vllm` registers a vLLM load format, `flyte-streaming`, through vLLM's `vllm.general_plugins` entry point.
`flyteplugins.vllm.model_streamer.engine_args(path)` downloads the non-safetensors files under `path` and returns the `LLM` keyword arguments that select the load format: `model`, `load_format`, and `model_loader_extra_config`.
Pass any other engine arguments alongside them.
It takes the same `local_dir`, `chunk_size`, and `max_concurrency` arguments as `load_hf_model()`.

In an async task, build the engine off the event loop, for example `await asyncio.to_thread(LLM, **args, max_model_len=4096)`, because `LLM()` blocks for the whole load.

`engine_args()` also sets `VLLM_WORKER_MULTIPROC_METHOD=spawn` unless it is already set. Keep it at `spawn`.
obstore's runtime does not survive `fork()`, and vLLM forks its engine-core process by default.
`ModelStreamer` detects a process forked from one that has already streamed or downloaded metadata and raises `RuntimeError` instead of hanging on the first read.

## Gotchas

- A prefix with no `*.safetensors` files raises `ValueError: No files found matching pattern: *.safetensors`.
- Weights in other formats under the prefix, such as `pytorch_model.bin` or an `original/*.pth` directory, are downloaded to local disk with the config and tokenizer. Keep weights in other formats out of the prefix.

## Related pages

To serve a model behind an endpoint instead of loading it inside a task, use `stream_model=True` on a [vLLM app](../apps/native-app-integrations/vllm-app#model-streaming) or an [SGLang app](../apps/native-app-integrations/sglang-app#model-streaming).
