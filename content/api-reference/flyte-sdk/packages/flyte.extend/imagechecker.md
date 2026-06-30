---
title: ImageChecker
version: 2.5.6
variants: +flyte +union
layout: py_api
---

# ImageChecker

**Package:** `flyte.extend`

```python
protocol ImageChecker()
```
## Methods

| Method | Description |
|-|-|
| [`image_exists()`](#image_exists) | Check whether an image exists in a registry or cache. |


### image_exists()

```python
def image_exists(
    repository: str,
    tag: str,
    arch: Tuple[Architecture, ...],
) -> Optional[str]
```
Check whether an image exists in a registry or cache.

Returns the image URI if found, or None if the image definitively does not exist.
Raise an exception if existence cannot be determined (e.g. cache miss, network failure)
so the next checker in the chain gets a chance.


| Parameter | Type | Description |
|-|-|-|
| `repository` | `str` | |
| `tag` | `str` | |
| `arch` | `Tuple[Architecture, ...]` | |

