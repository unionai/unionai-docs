---
title: VLLMShardArgs
version: 0.1.201
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# VLLMShardArgs

**Package:** `union.remote`

```python
class VLLMShardArgs(
    model: str,
    tensor_parallel_size: int,
    trust_remote_code: bool,
    revision: str | None,
    file_pattern: str | None,
    max_file_size: int | None,
    gpu_memory_utilization: float,
    extra_args: dict[str, typing.Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | |
| `tensor_parallel_size` | `int` | |
| `trust_remote_code` | `bool` | |
| `revision` | `str \| None` | |
| `file_pattern` | `str \| None` | |
| `max_file_size` | `int \| None` | |
| `gpu_memory_utilization` | `float` | |
| `extra_args` | `dict[str, typing.Any]` | |

## Methods

| Method | Description |
|-|-|
| [`get_vllm_args()`](#get_vllm_args) |  |


### get_vllm_args()

```python
def get_vllm_args(
    model_path: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model_path` | `str` | |

