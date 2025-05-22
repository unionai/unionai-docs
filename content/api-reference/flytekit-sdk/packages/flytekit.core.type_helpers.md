---
title: flytekit.core.type_helpers
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.type_helpers

## Directory

### Methods

| Method | Description |
|-|-|
| [`load_type_from_tag()`](#load_type_from_tag) | Loads python type from tag. |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## Methods

#### load_type_from_tag()

```python
def load_type_from_tag(
    tag: str,
) -> typing.Type[~T]
```
Loads python type from tag


| Parameter | Type |
|-|-|
| `tag` | `str` |

