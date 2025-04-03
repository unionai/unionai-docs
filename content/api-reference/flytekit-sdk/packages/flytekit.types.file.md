---
title: flytekit.types.file
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.file


## Flytekit File Type

This list also contains a bunch of pre-formatted :py:class:`flytekit.types.file.FlyteFile` types.


## Directory

### Classes

| Class | Description |
|-|-|
| [`FileExt`](.././flytekit.types.file#flytekittypesfilefileext) | Used for annotating file extension types of FlyteFile. |

## flytekit.types.file.FileExt

Used for annotating file extension types of FlyteFile.
This is useful for extensions that have periods in them, e.g., "tar.gz".

Example:
TAR_GZ = Annotated[str, FileExt("tar.gz")]


```python
class FileExt(
    ext: str,
)
```
| Parameter | Type |
|-|-|
| `ext` | `str` |

### Methods

| Method | Description |
|-|-|
| [`check_and_convert_to_str()`](#check_and_convert_to_str) |  |


#### check_and_convert_to_str()

```python
def check_and_convert_to_str(
    item: typing.Union[typing.Type, str],
) -> str
```
| Parameter | Type |
|-|-|
| `item` | `typing.Union[typing.Type, str]` |

