---
title: flytekit.types.file
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.file


Flytekit File Type
==========================================================
.. currentmodule:: flytekit.types.file

This list also contains a bunch of pre-formatted {{< py_class_ref flytekit.types.file.FlyteFile >}} types.

.. autosummary::
   :toctree: generated/
   :template: file_types.rst

   FlyteFile
   HDF5EncodedFile
   HTMLPage
   JoblibSerializedFile
   JPEGImageFile
   PDFFile
   PNGImageFile
   PythonPickledFile
   PythonNotebook
   SVGImageFile

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

