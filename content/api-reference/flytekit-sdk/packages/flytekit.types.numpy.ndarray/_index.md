---
title: flytekit.types.numpy.ndarray
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.numpy.ndarray

## Directory

### Classes

| Class | Description |
|-|-|
| [`NumpyArrayTransformer`](../flytekit.types.numpy.ndarray/numpyarraytransformer) | TypeTransformer that supports np. |

### Methods

| Method | Description |
|-|-|
| [`extract_metadata()`](#extract_metadata) |  |


## Methods

#### extract_metadata()

```python
def extract_metadata(
    t: typing.Type[numpy.ndarray],
) -> typing.Tuple[typing.Type[numpy.ndarray], typing.Dict[str, bool]]
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Type[numpy.ndarray]` | |

