---
title: HuggingFaceModelInfo
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# HuggingFaceModelInfo

**Package:** `union.remote`

Captures information about a Hugging Face model. Only repo is required, all other fields are optional, and are
automatically determined from the model's config.json file. If not found, the fields are initialized to defaults.



```python
class HuggingFaceModelInfo(
    repo: str,
    artifact_name: str | None,
    model_type: str | None,
    architecture: str | None,
    task: str,
    modality: typing.List[str] | None,
    serial_format: str,
    short_description: str | None,
    shard_config: ShardConfig | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `artifact_name` | `str \| None` | |
| `model_type` | `str \| None` | |
| `architecture` | `str \| None` | |
| `task` | `str` | |
| `modality` | `typing.List[str] \| None` | |
| `serial_format` | `str` | |
| `short_description` | `str \| None` | |
| `shard_config` | `ShardConfig \| None` | |

