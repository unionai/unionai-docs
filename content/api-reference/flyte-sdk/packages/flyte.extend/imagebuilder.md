---
title: ImageBuilder
version: 2.0.0b56
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageBuilder

**Package:** `flyte.extend`

```python
protocol ImageBuilder()
```
## Methods

| Method | Description |
|-|-|
| [`build_image()`](#build_image) |  |
| [`get_checkers()`](#get_checkers) | Returns ImageCheckers that can be used to check if the image exists in the registry. |


### build_image()

```python
def build_image(
    image: Image,
    dry_run: bool,
    wait: bool,
) -> 'ImageBuild'
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `dry_run` | `bool` | |
| `wait` | `bool` | |

### get_checkers()

```python
def get_checkers()
```
Returns ImageCheckers that can be used to check if the image exists in the registry.
If None, then use the default checkers.


