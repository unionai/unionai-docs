---
title: Prompt
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Prompt

**Package:** `flyte.extras`

Simple prompt record with built-in token estimation.

This is a convenience type for common LLM use cases.  For richer
prompt types (e.g. with system messages, metadata), define your own
dataclass implementing `TokenEstimator`.



## Parameters

```python
class Prompt(
    text: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `text` | `str` | The prompt text. |

## Methods

| Method | Description |
|-|-|
| [`estimate_tokens()`](#estimate_tokens) | Rough token estimate (~4 chars per token). |


### estimate_tokens()

```python
def estimate_tokens()
```
Rough token estimate (~4 chars per token).


