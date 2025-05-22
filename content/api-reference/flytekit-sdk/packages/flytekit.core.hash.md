---
title: flytekit.core.hash
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.hash

## Directory

### Classes

| Class | Description |
|-|-|
| [`HashMethod`](.././flytekit.core.hash#flytekitcorehashhashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`HashOnReferenceMixin`](.././flytekit.core.hash#flytekitcorehashhashonreferencemixin) |  |

### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## flytekit.core.hash.HashMethod

Flyte-specific object used to wrap the hash function for a specific type


```python
class HashMethod(
    function: typing.Callable[[~T], str],
)
```
| Parameter | Type |
|-|-|
| `function` | `typing.Callable[[~T], str]` |

### Methods

| Method | Description |
|-|-|
| [`calculate()`](#calculate) | Calculate hash for `obj`. |


#### calculate()

```python
def calculate(
    obj: ~T,
) -> str
```
Calculate hash for `obj`.


| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.core.hash.HashOnReferenceMixin

