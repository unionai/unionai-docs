---
title: Choice
description: "One pick from a fixed vocabulary, carrying the calibration it came with."
icon: braces
version: 2.9.0
variants: +flyte +union
layout: py_api
---

# Choice

**Package:** `flyteplugins.typesafe_ai`

One pick from a fixed vocabulary, carrying the calibration it came with.


## Parameters

```python
class Choice(
    value: C,
    confidence: float = 0.0,
    probabilities: dict[str, float] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `C` | |
| `confidence` | `float` | |
| `probabilities` | `dict[str, float]` | |

## Methods

| Method | Description |
|-|-|
| [`certain()`](#certain) | Is this pick confident enough to act on without a human? |
| [`runner_up()`](#runner_up) | The second-most-likely option, which is what you show a reviewer. |


### certain()

```python
def certain(
    threshold: float,
) -> bool
```
Is this pick confident enough to act on without a human?


| Parameter | Type | Description |
|-|-|-|
| `threshold` | `float` | |

### runner_up()

```python
def runner_up()
```
The second-most-likely option, which is what you show a reviewer.


