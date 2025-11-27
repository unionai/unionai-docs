---
title: timeit
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# timeit

**Package:** `flytekit.core.utils`

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
    # your code


```python
class timeit(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | A string that describes the wrapped code block or function being executed. |

