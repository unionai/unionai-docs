---
title: ModelStreamer
description: "Stream the safetensors weights under a remote prefix, tensor by tensor."
icon: braces
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# ModelStreamer

**Package:** `flyte.extras.model_streamer`

Stream the safetensors weights under a remote prefix, tensor by tensor.

`path` is the object-store prefix of a Hugging Face style model directory
(`s3://bucket/models/qwen2.5-7b`) holding `*.safetensors` files and,
optionally, a `model.safetensors.index.json`. When the index is present it
decides which file each tensor is read from; otherwise every
`*.safetensors` file directly under the prefix is read and the first copy
of a duplicated tensor name wins.

Each tensor is fetched as `chunk_size` byte ranges, `max_concurrency`
at a time, and yielded as soon as its last range lands, so loading overlaps
the download instead of waiting for it. Peak host memory is roughly the
tensors in flight, not the model.

Credentials come from the task's storage configuration (or the ambient
cloud environment outside a task), the same way `flyte.io.File` reads.


## Parameters

```python
class ModelStreamer(
    path: str,
    chunk_size: int | None = None,
    max_concurrency: int | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `chunk_size` | `int \| None` | |
| `max_concurrency` | `int \| None` | |

## Methods

| Method | Description |
|-|-|
| [`download_metadata()`](#download_metadata) | Download everything under the prefix except the weights. |
| [`load_into()`](#load_into) | Stream the weights straight into `module`'s parameters and buffers. |
| [`state_dict()`](#state_dict) | Collect every tensor into a dict, each placed on `device` as it lands. |
| [`stream()`](#stream) | Yield `(name, tensor)` pairs in completion order, not file order. |
| [`stream_sync()`](#stream_sync) | Synchronous `stream`, safe to call from any thread. |


### download_metadata()

```python
def download_metadata(
    local_dir: str | pathlib.Path,
) -> pathlib.Path
```
Download everything under the prefix except the weights.

Config, tokenizer and generation-config files are small and the
libraries that read them want a local directory; the `*.safetensors`
files are skipped because `stream` reads them directly.


| Parameter | Type | Description |
|-|-|-|
| `local_dir` | `str \| pathlib.Path` | |

### load_into()

```python
def load_into(
    module: nn.Module,
    device: torch.device | str | None = None,
    dtype: torch.dtype | None = None,
    strict: bool = True,
    key_mapping: typing.Callable[[str], str | None] | None = None,
) -> LoadResult
```
Stream the weights straight into `module`'s parameters and buffers.

Each tensor replaces the module's entry as it arrives (`assign`
semantics, as in `load_state_dict(assign=True)`), so the module can be
built on the `meta` device with `empty_weights` and never
allocate its weights twice. Tensors go to `device` when given,
otherwise to the device of the entry they replace (`meta` entries
need an explicit `device`).

`key_mapping` renames a checkpoint key to a module key, or returns
`None` to skip it. Checkpoints usually store a tied weight once (an
embedding shared with the output head), so when the module has a
`tie_weights()` method, as Hugging Face models do, it is called once
the stream ends. With `strict` (the default), any parameter still on
`meta` after that, or any checkpoint key left unmatched, raises
`KeyError`.


| Parameter | Type | Description |
|-|-|-|
| `module` | `nn.Module` | |
| `device` | `torch.device \| str \| None` | |
| `dtype` | `torch.dtype \| None` | |
| `strict` | `bool` | |
| `key_mapping` | `typing.Callable[[str], str \| None] \| None` | |

### state_dict()

```python
def state_dict(
    device: torch.device | str | None = None,
    dtype: torch.dtype | None = None,
) -> dict[str, torch.Tensor]
```
Collect every tensor into a dict, each placed on `device` as it lands.


| Parameter | Type | Description |
|-|-|-|
| `device` | `torch.device \| str \| None` | |
| `dtype` | `torch.dtype \| None` | |

### stream()

```python
def stream(
    device: torch.device | str | None = None,
    dtype: torch.dtype | None = None,
) -> typing.AsyncIterator[tuple[str, torch.Tensor]]
```
Yield `(name, tensor)` pairs in completion order, not file order.

With `device` set, each tensor is copied there as it arrives and its
host buffer is released; with `dtype` set, floating-point tensors are
cast (integer and boolean tensors are left alone).

Raises `RuntimeError` in a process forked from one that already
streamed: object-storage reads cannot work across `fork()`.


| Parameter | Type | Description |
|-|-|-|
| `device` | `torch.device \| str \| None` | |
| `dtype` | `torch.dtype \| None` | |

### stream_sync()

```python
def stream_sync(
    device: torch.device | str | None = None,
    dtype: torch.dtype | None = None,
) -> typing.Iterator[tuple[str, torch.Tensor]]
```
Synchronous `stream`, safe to call from any thread.

The download runs on its own event loop in a background thread, so this
works both from plain synchronous code and from a thread that already
has a loop running (where flyte's own `get_tensors()` raises). The
hand-off queue is bounded: a slow consumer pauses the download rather
than letting finished tensors pile up in host memory.


| Parameter | Type | Description |
|-|-|-|
| `device` | `torch.device \| str \| None` | |
| `dtype` | `torch.dtype \| None` | |

