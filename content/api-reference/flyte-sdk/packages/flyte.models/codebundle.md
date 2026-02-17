---
title: CodeBundle
version: 2.0.0b58
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CodeBundle

**Package:** `flyte.models`

A class representing a code bundle for a task. This is used to package the code and the inflation path.
The code bundle computes the version of the code using the hash of the code.



```python
class CodeBundle(
    computed_version: str,
    destination: str,
    tgz: str | None,
    pkl: str | None,
    downloaded_path: pathlib.Path | None,
    files: List[str] | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `computed_version` | `str` | The version of the code bundle. This is the hash of the code. |
| `destination` | `str` | The destination path for the code bundle to be inflated to. |
| `tgz` | `str \| None` | Optional path to the tgz file. |
| `pkl` | `str \| None` | Optional path to the pkl file. |
| `downloaded_path` | `pathlib.Path \| None` | The path to the downloaded code bundle. This is only available during runtime, when the code bundle has been downloaded and inflated. |
| `files` | `List[str] \| None` | |

## Methods

| Method | Description |
|-|-|
| [`with_downloaded_path()`](#with_downloaded_path) | Create a new CodeBundle with the given downloaded path. |


### with_downloaded_path()

```python
def with_downloaded_path(
    path: pathlib.Path,
) -> CodeBundle
```
Create a new CodeBundle with the given downloaded path.


| Parameter | Type | Description |
|-|-|-|
| `path` | `pathlib.Path` | |

