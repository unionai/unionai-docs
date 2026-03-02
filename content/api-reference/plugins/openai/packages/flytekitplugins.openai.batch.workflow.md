---
title: flytekitplugins.openai.batch.workflow
version: 1.16.14
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



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The suffix to be added to workflow and task names. |
| `secret` | `flytekit.models.security.Secret` | Secret comprising the OpenAI API key. |
| `openai_organization` | `typing.Optional[str]` | Name of the OpenAI organization. |
| `config` | `typing.Optional[typing.Dict[str, typing.Any]]` | Additional config for batch creation. |
| `is_json_iterator` | `bool` | Set to True if you're sending an iterator/generator; if a JSONL file, set to False. |
| `file_upload_mem` | `str` | Memory to allocate to the upload file task. |
| `file_download_mem` | `str` | Memory to allocate to the download file task. |

