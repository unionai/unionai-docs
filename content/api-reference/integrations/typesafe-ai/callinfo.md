---
title: CallInfo
description: "What one `system_one` call cost, plus the calibration a plain field dropped."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# CallInfo

**Package:** `flyteplugins.typesafe_ai`

What one `system_one` call cost, plus the calibration a plain field dropped.

`Choice`, `Score` and `Noul` carry their own calibration, so for those the maps
below are redundant. They exist for the shorthand field types -- a `bool` or a
`Literal` -- which hold a plain value: the calibration is dropped from *your
model*, not from the call, and this is where to find it.

Both maps are `dict[str, float]` so that a task can return a `CallInfo`.


## Parameters

```python
class CallInfo(
    model: str = '',
    questions: int = 0,
    input_tokens: int = 0,
    output_tokens: int = 0,
    latency_s: float = 0.0,
    values: dict[str, float] = <factory>,
    confidence: dict[str, float] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | |
| `questions` | `int` | |
| `input_tokens` | `int` | |
| `output_tokens` | `int` | |
| `latency_s` | `float` | |
| `values` | `dict[str, float]` | |
| `confidence` | `dict[str, float]` | |

