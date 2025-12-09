---
title: SerializationContext
version: 2.0.0b35
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SerializationContext

**Package:** `flyte.models`

This object holds serialization time contextual information, that can be used when serializing the task and
various parameters of a tasktemplate. This is only available when the task is being serialized and can be
during a deployment or runtime.



```python
class SerializationContext(
    version: str,
    project: str | None,
    domain: str | None,
    org: str | None,
    code_bundle: Optional[CodeBundle],
    input_path: str,
    output_path: str,
    interpreter_path: str,
    image_cache: ImageCache | None,
    root_dir: Optional[pathlib.Path],
)
```
| Parameter | Type | Description |
|-|-|-|
| `version` | `str` | The version of the task |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `org` | `str \| None` | |
| `code_bundle` | `Optional[CodeBundle]` | The code bundle for the task. This is used to package the code and the inflation path. |
| `input_path` | `str` | The path to the inputs for the task. This is used to determine where the inputs will be located |
| `output_path` | `str` | The path to the outputs for the task. This is used to determine where the outputs will be located |
| `interpreter_path` | `str` | |
| `image_cache` | `ImageCache \| None` | |
| `root_dir` | `Optional[pathlib.Path]` | |

## Methods

| Method | Description |
|-|-|
| [`get_entrypoint_path()`](#get_entrypoint_path) | Get the entrypoint path for the task. |


### get_entrypoint_path()

```python
def get_entrypoint_path(
    interpreter_path: Optional[str],
) -> str
```
Get the entrypoint path for the task. This is used to determine the entrypoint for the task execution.


| Parameter | Type | Description |
|-|-|-|
| `interpreter_path` | `Optional[str]` | The path to the interpreter (python) |

