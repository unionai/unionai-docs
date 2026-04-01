---
title: CodeSolution
version: 2.1.2.dev2+g62f55b516
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# CodeSolution

**Package:** `flyteplugins.codegen`

Structured code solution.


## Parameters

```python
class CodeSolution(
    language: str,
    code: str,
    system_packages: list[str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `language` | `str` | Programming language |
| `code` | `str` | Complete executable code including imports and dependencies |
| `system_packages` | `list[str]` | System packages needed (e.g., gcc, build-essential, curl) |

## Methods

| Method | Description |
|-|-|
| [`normalize_language()`](#normalize_language) |  |


### normalize_language()

```python
def normalize_language(
    v: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `v` | `str` | |

