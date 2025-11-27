---
title: ComparisonExpression
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ComparisonExpression

**Package:** `flytekit.core.promise`

ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands
and operator can be any comparison expression like <, >, <=, >=, ==, !=


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

## Methods

| Method | Description |
|-|-|
| [`eval()`](#eval) |  |


### eval()

```python
def eval()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `lhs` |  |  |
| `op` |  |  |
| `rhs` |  |  |

