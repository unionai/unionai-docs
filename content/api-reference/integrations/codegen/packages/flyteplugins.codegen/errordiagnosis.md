---
title: ErrorDiagnosis
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# ErrorDiagnosis

**Package:** `flyteplugins.codegen`

Structured diagnosis of execution errors.


## Parameters

```python
class ErrorDiagnosis(
    failures: list[flyteplugins.codegen.core.types.TestFailure],
    needs_system_packages: list[str],
    needs_language_packages: list[str],
    needs_additional_commands: list[str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `failures` | `list[flyteplugins.codegen.core.types.TestFailure]` | Individual test failures with their diagnoses |
| `needs_system_packages` | `list[str]` | System packages needed (e.g., gcc, pkg-config). |
| `needs_language_packages` | `list[str]` | Language packages needed. |
| `needs_additional_commands` | `list[str]` | Additional RUN commands (e.g., apt-get update, mkdir /data, wget files). |

