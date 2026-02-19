---
title: FlyteIterator
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteIterator

**Package:** `flytekit.types.iterator.iterator`

```python
class FlyteIterator(
    ctx: flytekit.core.context_manager.FlyteContext,
    lv: flytekit.models.literals.Literal,
    expected_python_type: typing.Type[~T],
    length: int,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `lv` | `flytekit.models.literals.Literal` | |
| `expected_python_type` | `typing.Type[~T]` | |
| `length` | `int` | |

