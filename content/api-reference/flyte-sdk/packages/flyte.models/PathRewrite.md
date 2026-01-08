---
title: PathRewrite
version: 2.0.0b47
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PathRewrite

**Package:** `flyte.models`

Configuration for rewriting paths during input loading.


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

