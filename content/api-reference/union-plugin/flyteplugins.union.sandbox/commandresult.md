---
title: CommandResult
description: "A finished command: what `Sandbox.run` returns."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# CommandResult

**Package:** `flyteplugins.union.sandbox`

A finished command: what `Sandbox.run` returns.


## Parameters

```python
class CommandResult(
    command: str,
    exit_code: int,
    stdout: str,
    stderr: str,
    duration: float,
    reason: str = '',
    timed_out: bool = False,
    truncated: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `command` | `str` | |
| `exit_code` | `int` | |
| `stdout` | `str` | |
| `stderr` | `str` | |
| `duration` | `float` | |
| `reason` | `str` | |
| `timed_out` | `bool` | |
| `truncated` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `ok` | `bool` |  |

