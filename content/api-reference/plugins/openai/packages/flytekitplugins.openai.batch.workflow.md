---
title: flytekitplugins.openai.batch.workflow
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.openai.batch.workflow

## Directory

### Methods

| Method | Description |
|-|-|
| [`create_batch()`](#create_batch) | Uploads JSON data to a JSONL file, creates a batch, waits for it to complete, and downloads the output/error JSON files. |


## Methods

#### create_batch()

```python
def create_batch(
    name: str,
    secret: flytekit.models.security.Secret,
    openai_organization: typing.Optional[str],
    config: typing.Optional[typing.Dict[str, typing.Any]],
    is_json_iterator: bool,
    file_upload_mem: str,
    file_download_mem: str,
) -> flytekit.core.workflow.ImperativeWorkflow
```
Uploads JSON data to a JSONL file, creates a batch, waits for it to complete, and downloads the output/error JSON files.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `secret` | `flytekit.models.security.Secret` |
| `openai_organization` | `typing.Optional[str]` |
| `config` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `is_json_iterator` | `bool` |
| `file_upload_mem` | `str` |
| `file_download_mem` | `str` |

