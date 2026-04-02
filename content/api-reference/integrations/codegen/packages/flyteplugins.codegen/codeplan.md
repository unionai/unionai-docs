---
title: CodePlan
version: 2.1.0
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# CodePlan

**Package:** `flyteplugins.codegen`

Structured plan for the code solution.


## Parameters

```python
class CodePlan(
    description: str,
    approach: str,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `description` | `str` | Overall description of the solution |
| `approach` | `str` | High-level approach and algorithm to solve the problem |

