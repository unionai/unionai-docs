---
title: VLLMShardArgs
version: 2.1.5
variants: +flyte +union
layout: py_api
---

# VLLMShardArgs

**Package:** `flyte.prefetch`

Arguments for sharding a model using vLLM.



## Parameters

```python
class VLLMShardArgs(
    tensor_parallel_size: int,
    dtype: str,
    trust_remote_code: bool,
    max_model_len: int | None,
    file_pattern: str | None,
    max_file_size: int,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `tensor_parallel_size` | `int` | Number of tensor parallel workers. |
| `dtype` | `str` | Data type for model weights. |
| `trust_remote_code` | `bool` | Whether to trust remote code from HuggingFace. |
| `max_model_len` | `int \| None` | Maximum model context length. |
| `file_pattern` | `str \| None` | Pattern for sharded weight files. |
| `max_file_size` | `int` | Maximum size for each sharded file. |

## Methods

| Method | Description |
|-|-|
| [`get_vllm_args()`](#get_vllm_args) | Get arguments dict for vLLM LLM constructor. |


### get_vllm_args()

```python
def get_vllm_args(
    model_path: str,
) -> dict[str, Any]
```
Get arguments dict for vLLM LLM constructor.


| Parameter | Type | Description |
|-|-|-|
| `model_path` | `str` | |

