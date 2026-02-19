---
title: ProcessResult
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ProcessResult

**Package:** `flytekit.extras.tasks.shell`

Stores a process return code, standard output and standard error.



```python
class ProcessResult(
    returncode: int,
    output: str,
    error: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `returncode` | `int` | int The sub-process return code |
| `output` | `str` | str The sub-process standard output string |
| `error` | `str` | str The sub-process standard error string |

