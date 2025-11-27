---
title: FileExt
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FileExt

**Package:** `flytekit.types.file`

Used for annotating file extension types of FlyteFile.
This is useful for extensions that have periods in them, e.g., "tar.gz".

Example:
TAR_GZ = Annotated[str, FileExt("tar.gz")]


```python
class FileExt(
    ext: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ext` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`check_and_convert_to_str()`](#check_and_convert_to_str) |  |


### check_and_convert_to_str()

```python
def check_and_convert_to_str(
    item: typing.Union[typing.Type, str],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `item` | `typing.Union[typing.Type, str]` | |

