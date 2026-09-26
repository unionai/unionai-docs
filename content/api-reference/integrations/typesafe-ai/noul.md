---
title: Noul
description: "Truthfulness in 0..1."
icon: braces
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# Noul

**Package:** `flyteplugins.typesafe_ai`

Truthfulness in 0..1.

Deliberately no `__bool__`: `if noul:` would make 0.02 and 0.98 alike,
and choosing the threshold is the part you want in code where it can be read,
reviewed and changed.


## Parameters

```python
class Noul(
    value: float = 0.0,
)
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `float` | |

## Methods

| Method | Description |
|-|-|
| [`at()`](#at) |  |


### at()

```python
def at(
    threshold: float,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `threshold` | `float` | |

