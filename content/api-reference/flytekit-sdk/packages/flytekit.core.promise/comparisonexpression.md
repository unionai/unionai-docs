---
title: ComparisonExpression
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ComparisonExpression

**Package:** `flytekit.core.promise`

ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands
and operator can be any comparison expression like &lt;, &gt;, &lt;=, &gt;=, ==, !=



```python
class ComparisonExpression(
    lhs: Union['Promise', Any],
    op: ComparisonOps,
    rhs: Union['Promise', Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `lhs` | `Union['Promise', Any]` | |
| `op` | `ComparisonOps` | |
| `rhs` | `Union['Promise', Any]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `lhs` | `None` |  |
| `op` | `None` |  |
| `rhs` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`eval()`](#eval) |  |


### eval()

```python
def eval()
```
