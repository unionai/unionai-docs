---
title: ImageChecker
version: 2.0.0
variants: +flyte +byoc +selfmanaged +serverless
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
| [`image_exists()`](#image_exists) |  |


### image_exists()

```python
def image_exists(
    repository: str,
    tag: str,
    arch: Tuple[Architecture, ...],
) -> Optional[str]
```
| Parameter | Type | Description |
|-|-|-|
| `repository` | `str` | |
| `tag` | `str` | |
| `arch` | `Tuple[Architecture, ...]` | |

