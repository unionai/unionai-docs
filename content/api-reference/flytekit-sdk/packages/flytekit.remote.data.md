---
title: flytekit.remote.data
version: 1.16.10
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


| Parameter | Type | Description |
|-|-|-|
| `file_access` | `flytekit.core.data_persistence.FileAccessProvider` | |
| `var` | `str` | |
| `data` | `flytekit.models.literals.Literal` | |
| `download_to` | `typing.Optional[pathlib._local.Path]` | |

