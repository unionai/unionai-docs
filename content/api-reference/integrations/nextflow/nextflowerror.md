---
title: NextflowError
description: "Raised when `nextflow run` exits with a non-zero status."
icon: exclamation-triangle
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# NextflowError

**Package:** `flyteplugins.nextflow`

Raised when `nextflow run` exits with a non-zero status.


## Parameters

```python
class NextflowError(
    exit_code: int,
    output_tail: Sequence[str],
    log_tail: Sequence[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `exit_code` | `int` | |
| `output_tail` | `Sequence[str]` | |
| `log_tail` | `Sequence[str]` | |

