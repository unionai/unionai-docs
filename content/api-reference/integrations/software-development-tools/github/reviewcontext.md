---
title: ReviewContext
description: "Review metadata collected from a pull request."
icon: braces
version: 2.11.0
variants: +flyte +union
layout: py_api
---

# ReviewContext

**Package:** `flyteplugins.github`

Review metadata collected from a pull request.

This is the payload embedded in the condition prompt, so the reviewer sees
everything needed to decide without leaving the Flyte UI.


## Parameters

```python
class ReviewContext(
    repo: str,
    number: int,
    title: str,
    author: str | None = None,
    body: str = '',
    base: str | None = None,
    head: str | None = None,
    url: str | None = None,
    additions: int | None = None,
    deletions: int | None = None,
    changed_files: int | None = None,
    files: list[dict[str, typing.Any]] = list(),
    prior_reviews: list[dict[str, typing.Any]] = list(),
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `repo` | `str` | |
| `number` | `int` | |
| `title` | `str` | |
| `author` | `str \| None` | |
| `body` | `str` | |
| `base` | `str \| None` | |
| `head` | `str \| None` | |
| `url` | `str \| None` | |
| `additions` | `int \| None` | |
| `deletions` | `int \| None` | |
| `changed_files` | `int \| None` | |
| `files` | `list[dict[str, typing.Any]]` | |
| `prior_reviews` | `list[dict[str, typing.Any]]` | |

## Methods

| Method | Description |
|-|-|
| [`to_json()`](#to_json) | Serialize to JSON for embedding in a prompt. |


### to_json()

```python
def to_json(
    max_file_patches: int = 20,
) -> str
```
Serialize to JSON for embedding in a prompt.

Patches dominate the size of a large diff, so only the first
`max_file_patches` files keep theirs — the rest keep their stats.


| Parameter | Type | Description |
|-|-|-|
| `max_file_patches` | `int` | |

