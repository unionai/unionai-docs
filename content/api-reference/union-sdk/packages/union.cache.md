---
title: union.cache
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.cache

## Directory

### Classes

| Class | Description |
|-|-|
| [`CacheFunctionBody`](.././union.cache#unioncachecachefunctionbody) | A class that implements a versioning mechanism for functions by generating. |

## union.cache.CacheFunctionBody

A class that implements a versioning mechanism for functions by generating
a SHA-256 hash of the function's source code combined with a salt.


### Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) | This method generates a version string for a function by hashing the function's source code. |


#### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
) -> str
```
This method generates a version string for a function by hashing the function's source code
combined with a salt.



| Parameter | Type | Description |
|-|-|-|
| `salt` | `str` | A string that is used to salt the hash. |
| `params` | `flytekit.core.cache.VersionParameters` | VersionParameters object that contains the parameters (e.g. function, ImageSpec, etc.) that are used to generate the version.  :return: A string that represents the version of the function. |

