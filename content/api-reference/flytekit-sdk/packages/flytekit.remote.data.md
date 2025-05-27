---
title: flytekit.remote.data
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.data

## Directory

### Methods

| Method | Description |
|-|-|
| [`download_literal()`](#download_literal) | Download a single literal to a file, if it is a blob or structured dataset. |


## Methods

#### download_literal()

```python
def download_literal(
    file_access: flytekit.core.data_persistence.FileAccessProvider,
    var: str,
    data: flytekit.models.literals.Literal,
    download_to: typing.Optional[pathlib._local.Path],
)
```
Download a single literal to a file, if it is a blob or structured dataset.


| Parameter | Type |
|-|-|
| `file_access` | `flytekit.core.data_persistence.FileAccessProvider` |
| `var` | `str` |
| `data` | `flytekit.models.literals.Literal` |
| `download_to` | `typing.Optional[pathlib._local.Path]` |

