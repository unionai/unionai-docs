---
title: flyte.extras.model_streamer
description: "Stream safetensors model weights from object storage straight onto a device."
icon: box-seam
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# flyte.extras.model_streamer

Stream safetensors model weights from object storage straight onto a device.

Weights are fetched as parallel byte ranges and handed over tensor by tensor
as each one completes. They never touch local disk, and host memory holds only
the tensors in flight, so a model's load time is close to its download time.

- `ModelStreamer`: the streamer itself (async and sync iterators, a
  state dict, or straight into an `nn.Module`).
- `load_hf_model`: a `transformers` model built on `meta` and filled
  on the GPU.
- `flyteplugins.vllm.model_streamer` (in `flyteplugins-vllm`): a vLLM
  `load_format` for `vllm.LLM` / `AsyncLLMEngine`.

Requires `torch`; `load_hf_model` also needs `transformers`, and the
vLLM integration needs `vllm`.
## Directory

### Classes

| Class | Description |
|-|-|
| [`LoadResult`](../flyte.extras.model_streamer/loadresult) | What `ModelStreamer.load_into` did not match. |
| [`ModelStreamer`](../flyte.extras.model_streamer/modelstreamer) | Stream the safetensors weights under a remote prefix, tensor by tensor. |

### Methods

| Method | Description |
|-|-|
| [`empty_weights()`](#empty_weights) | Build modules with their parameters on the `meta` device. |
| [`load_hf_model()`](#load_hf_model) | Build a `transformers` model and stream its weights onto `device`. |
| [`missing_parameters()`](#missing_parameters) | Parameters and buffers still on the `meta` device. |


## Methods

#### empty_weights()

```python
def empty_weights()
```
Build modules with their parameters on the `meta` device.

Unlike `with torch.device("meta")`, buffers are created normally, so
non-persistent buffers computed in `__init__` (rotary `inv_freq`, for
instance), which are never in a checkpoint, keep real values.


#### load_hf_model()

```python
def load_hf_model(
    path: str,
    device: torch.device | str = 'cuda',
    dtype: torch.dtype | None = None,
    model_class: typing.Any = None,
    local_dir: str | pathlib.Path | None = None,
    trust_remote_code: bool = False,
    chunk_size: int | None = None,
    max_concurrency: int | None = None,
) -> tuple[nn.Module, pathlib.Path]
```
Build a `transformers` model and stream its weights onto `device`.

The config, tokenizer and generation config are downloaded to
`local_dir` (a fresh temporary directory by default). The model is built
with its parameters on `meta`, and each weight is then copied onto
`device` as soon as it finishes downloading. Weights never touch local
disk, and host memory holds only the tensors in flight.

`model_class` defaults to `AutoModelForCausalLM`; any `Auto*` class
or concrete `PreTrainedModel` subclass works. `dtype` casts
floating-point weights (`None` keeps the checkpoint's dtype).

Returns the model in eval mode and the local directory, from which the
tokenizer can be loaded with `AutoTokenizer.from_pretrained(local_dir)`.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `device` | `torch.device \| str` | |
| `dtype` | `torch.dtype \| None` | |
| `model_class` | `typing.Any` | |
| `local_dir` | `str \| pathlib.Path \| None` | |
| `trust_remote_code` | `bool` | |
| `chunk_size` | `int \| None` | |
| `max_concurrency` | `int \| None` | |

#### missing_parameters()

```python
def missing_parameters(
    module: nn.Module,
) -> list[str]
```
Parameters and buffers still on the `meta` device.


| Parameter | Type | Description |
|-|-|-|
| `module` | `nn.Module` | |

