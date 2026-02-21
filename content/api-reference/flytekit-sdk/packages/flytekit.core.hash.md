---
title: flytekit.core.hash
version: 1.16.14
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
| Parameter | Type | Description |
|-|-|-|
| `function` | `typing.Callable[[~T], str]` | |

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


| Parameter | Type | Description |
|-|-|-|
| `obj` | `~T` | |

## flytekit.core.hash.HashOnReferenceMixin

