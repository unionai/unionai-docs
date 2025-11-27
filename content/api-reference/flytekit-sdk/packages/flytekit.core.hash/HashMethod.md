---
title: HashMethod
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# HashMethod

**Package:** `flytekit.core.hash`

Flyte-specific object used to wrap the hash function for a specific type


```python
class HashMethod(
    function: typing.Callable[[~T], str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `function` | `typing.Callable[[~T], str]` | |

## Methods

| Method | Description |
|-|-|
| [`calculate()`](#calculate) | Calculate hash for `obj`. |


### calculate()

```python
def calculate(
    obj: ~T,
) -> str
```
Calculate hash for `obj`.


| Parameter | Type | Description |
|-|-|-|
| `obj` | `~T` | |

