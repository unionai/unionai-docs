---
title: HuggingFaceModelInfo
version: 2.1.0
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# HuggingFaceModelInfo

**Package:** `flyte.prefetch`

Information about a HuggingFace model to store.



## Parameters

```python
class HuggingFaceModelInfo(
    repo: str,
    artifact_name: str | None,
    architecture: str | None,
    task: str,
    modality: tuple[str, ...],
    serial_format: str | None,
    model_type: str | None,
    short_description: str | None,
    shard_config: flyte.prefetch._hf_model.ShardConfig | None,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | The HuggingFace repository ID (e.g., 'meta-llama/Llama-2-7b-hf'). |
| `artifact_name` | `str \| None` | Optional name for the stored artifact. If not provided, the repo name will be used (with '.' replaced by '-'). |
| `architecture` | `str \| None` | Model architecture from HuggingFace config.json. |
| `task` | `str` | Model task (e.g., 'generate', 'classify', 'embed'). |
| `modality` | `tuple[str, ...]` | Modalities supported by the model (e.g., 'text', 'image'). |
| `serial_format` | `str \| None` | Model serialization format (e.g., 'safetensors', 'onnx'). |
| `model_type` | `str \| None` | Model type (e.g., 'transformer', 'custom'). |
| `short_description` | `str \| None` | Short description of the model. |
| `shard_config` | `flyte.prefetch._hf_model.ShardConfig \| None` | Optional configuration for model sharding. |

