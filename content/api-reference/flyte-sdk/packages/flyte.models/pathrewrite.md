---
title: PathRewrite
version: 2.1.2.dev2+g62f55b516
variants: +flyte +union
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

