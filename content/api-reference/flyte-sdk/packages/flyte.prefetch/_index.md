---
title: flyte.prefetch
version: 2.0.0b50
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.prefetch


Prefetch utilities for Flyte.

This module provides functionality to prefetch various artifacts from remote registries,
such as HuggingFace models.

## Directory

### Classes

| Class | Description |
|-|-|
| [`HuggingFaceModelInfo`](../flyte.prefetch/huggingfacemodelinfo) | Information about a HuggingFace model to store. |
| [`ShardConfig`](../flyte.prefetch/shardconfig) | Configuration for model sharding. |
| [`StoredModelInfo`](../flyte.prefetch/storedmodelinfo) | Information about a stored model. |
| [`VLLMShardArgs`](../flyte.prefetch/vllmshardargs) | Arguments for sharding a model using vLLM. |

### Methods

| Method | Description |
|-|-|
| [`hf_model()`](#hf_model) | Store a HuggingFace model to remote storage. |


## Methods

#### hf_model()

```python
def hf_model(
    repo: str,
    raw_data_path: str | None,
    artifact_name: str | None,
    architecture: str | None,
    task: str,
    modality: tuple[str, ...],
    serial_format: str | None,
    model_type: str | None,
    short_description: str | None,
    shard_config: ShardConfig | None,
    hf_token_key: str,
    resources: Resources,
    force: int,
) -> Run
```
Store a HuggingFace model to remote storage.

This function downloads a model from the HuggingFace Hub and prefetches it to
remote storage. It supports optional sharding using vLLM for large models.

The prefetch behavior follows this priority:
1. If the model isn't being sharded, stream files directly to remote storage.
2. If streaming fails, fall back to downloading a snapshot and uploading.
3. If sharding is configured, download locally, shard with vLLM, then upload.

Example usage:

```python
import flyte

flyte.init(endpoint="my-flyte-endpoint")

# Store a model without sharding
run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-7b-hf",
    hf_token_key="HF_TOKEN",
)
run.wait()

# Prefetch and shard a model
from flyte.prefetch import ShardConfig, VLLMShardArgs

run = flyte.prefetch.hf_model(
    repo="meta-llama/Llama-2-70b-hf",
    shard_config=ShardConfig(
        engine="vllm",
        args=VLLMShardArgs(tensor_parallel_size=8),
    ),
    accelerator="A100:8",
    hf_token_key="HF_TOKEN",
)
run.wait()
```



| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | The HuggingFace repository ID (e.g., 'meta-llama/Llama-2-7b-hf'). |
| `raw_data_path` | `str \| None` | |
| `artifact_name` | `str \| None` | Optional name for the stored artifact. If not provided, the repo name will be used (with '.' replaced by '-'). |
| `architecture` | `str \| None` | Model architecture from HuggingFace config.json. |
| `task` | `str` | Model task (e.g., 'generate', 'classify', 'embed'). Default |
| `modality` | `tuple[str, ...]` | Modalities supported by the model. Default |
| `serial_format` | `str \| None` | Model serialization format (e.g., 'safetensors', 'onnx'). |
| `model_type` | `str \| None` | Model type (e.g., 'transformer', 'custom'). |
| `short_description` | `str \| None` | Short description of the model. |
| `shard_config` | `ShardConfig \| None` | Optional configuration for model sharding with vLLM. |
| `hf_token_key` | `str` | Name of the secret containing the HuggingFace token. Default |
| `resources` | `Resources` | |
| `force` | `int` | Force re-prefetch. Increment to force a new prefetch. Default  :return: A Run object representing the prefetch task execution. |

