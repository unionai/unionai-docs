---
title: CallInfo
description: "What one `system_one` call cost, for the report and for cost accounting."
icon: braces
version: 2.9.0
variants: +flyte +union
layout: py_api
---

# CallInfo

**Package:** `flyteplugins.typesafe_ai`

What one `system_one` call cost, for the report and for cost accounting.


## Parameters

```python
class CallInfo(
    model: str = '',
    questions: int = 0,
    input_tokens: int = 0,
    output_tokens: int = 0,
    latency_s: float = 0.0,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` | `str` | |
| `questions` | `int` | |
| `input_tokens` | `int` | |
| `output_tokens` | `int` | |
| `latency_s` | `float` | |

