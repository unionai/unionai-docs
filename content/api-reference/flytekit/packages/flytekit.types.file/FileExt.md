---
title: FileExt
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FileExt

**Package:** `flytekit.types.file`

Used for annotating file extension types of FlyteFile.
This is useful for extensions that have periods in them, e.g., "tar.gz".

Example:
TAR_GZ = Annotated[str, FileExt("tar.gz")]


```python
def FileExt(
    ext: str,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `ext` | `str` |
## Methods

### check_and_convert_to_str()

```python
def check_and_convert_to_str(
    item: typing.Union[typing.Type, str],
):
```
| Parameter | Type |
|-|-|
| `item` | `typing.Union[typing.Type, str]` |
