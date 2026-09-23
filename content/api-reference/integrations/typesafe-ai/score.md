---
title: Score
description: "A position on a rubric."
icon: braces
version: 2.10.0
variants: +flyte +union
layout: py_api
---

# Score

**Package:** `flyteplugins.typesafe_ai`

A position on a rubric.

Two representations, because both are useful: `value` is the rung that was
picked (an `IntEnum` member, so it compares and orders), and `position`
is the unrounded place on the scale that Jev actually returned. Branch on the
first, sort and threshold on the second.


## Parameters

```python
class Score(
    value: S,
    position: float = 0.0,
    confidence: float = 0.0,
    probabilities: dict[str, float] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `S` | |
| `position` | `float` | |
| `confidence` | `float` | |
| `probabilities` | `dict[str, float]` | |

## Methods

| Method | Description |
|-|-|
| [`at_least()`](#at_least) |  |


### at_least()

```python
def at_least(
    rung: S,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `rung` | `S` | |

