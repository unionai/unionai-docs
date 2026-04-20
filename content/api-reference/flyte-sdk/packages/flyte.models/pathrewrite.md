---
title: PathRewrite
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
layout: py_api
---

# PathRewrite

**Package:** `flyte.models`

Configuration for rewriting paths during input loading.


## Parameters

```python
class PathRewrite(
    old_prefix: str,
    new_prefix: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `old_prefix` | `str` | |
| `new_prefix` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`from_str()`](#from_str) | Create a PathRewrite from a string pattern of the form `old_prefix->new_prefix`. |


### from_str()

```python
def from_str(
    pattern: str,
) -> PathRewrite
```
Create a PathRewrite from a string pattern of the form `old_prefix-&gt;new_prefix`.


| Parameter | Type | Description |
|-|-|-|
| `pattern` | `str` | |

