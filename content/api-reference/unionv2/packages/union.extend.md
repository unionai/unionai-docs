---
title: union.extend
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.extend


Extends union with custom functionality.

> [!WARNING] This is not real code yet.
> This can be used to extend the type system and other features of union.

## Directory

### Classes

| Class | Description |
|-|-|
| [`TypeTransformerAPI`](.././union.extend#unionextendtypetransformerapi) | API type to xtend type transformers. |

## union.extend.TypeTransformerAPI

API type to xtend type transformers


```python
class TypeTransformerAPI(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`transform()`](#transform) | Transform the input data to a different format or type. |


#### transform()

```python
def transform(
    data: str,
) -> str
```
Transform the input data to a different format or type.


| Parameter | Type |
|-|-|
| `data` | `str` |

