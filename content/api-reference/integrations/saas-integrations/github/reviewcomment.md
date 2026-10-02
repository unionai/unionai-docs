---
title: ReviewComment
description: "A single inline review comment."
icon: braces
version: 2.10.7
variants: +flyte +union
layout: py_api
---

# ReviewComment

**Package:** `flyteplugins.github`

A single inline review comment.


## Parameters

```python
class ReviewComment(
    path: str,
    line: int | None = None,
    body: str,
    severity: typing.Literal['info', 'warning', 'blocking'] = 'info',
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `line` | `int \| None` | |
| `body` | `str` | |
| `severity` | `typing.Literal['info', 'warning', 'blocking']` | |

