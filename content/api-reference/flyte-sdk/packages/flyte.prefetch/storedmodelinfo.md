---
title: StoredModelInfo
version: 2.0.9
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# StoredModelInfo

**Package:** `flyte.prefetch`

Information about a stored model.



## Parameters

```python
class StoredModelInfo(
    artifact_name: str,
    path: str,
    metadata: dict[str, str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `artifact_name` | `str` | Name of the stored artifact. |
| `path` | `str` | Path to the stored model directory. |
| `metadata` | `dict[str, str]` | Metadata about the stored model. |

