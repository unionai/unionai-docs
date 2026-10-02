---
title: ReviewDecision
description: "Structured decision parsed from a reviewer's condition response."
icon: braces
version: 2.10.6
variants: +flyte +union
layout: py_api
---

# ReviewDecision

**Package:** `flyteplugins.github`

Structured decision parsed from a reviewer's condition response.


## Parameters

```python
class ReviewDecision(
    verdict: typing.Literal['approve', 'request_changes', 'comment'],
    summary: str = '',
    comments: list[flyteplugins.github._review.ReviewComment] = list(),
    reviewer: str | None = None,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `verdict` | `typing.Literal['approve', 'request_changes', 'comment']` | |
| `summary` | `str` | |
| `comments` | `list[flyteplugins.github._review.ReviewComment]` | |
| `reviewer` | `str \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `blocking_comments` | `list[ReviewComment]` | Comments the reviewer flagged as blocking. |
| `is_approved` | `bool` | True when the reviewer approved the change. |

