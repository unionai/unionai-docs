---
title: ConjunctionExpression
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConjunctionExpression

**Package:** `flytekit.core.promise`

A Conjunction Expression is an expression of the form either (A and B) or (A or B).
where A, B are two expressions (comparison or conjunctions) and (and, or) are logical truth operators.

A conjunctionExpression evaluates to True or False depending on the logical operator and the truth values of
each of the expressions A & B



```python
class ConjunctionExpression(
    lhs: Union[ComparisonExpression, 'ConjunctionExpression'],
    op: ConjunctionOps,
    rhs: Union[ComparisonExpression, 'ConjunctionExpression'],
)
```
| Parameter | Type | Description |
|-|-|-|
| `lhs` | `Union[ComparisonExpression, 'ConjunctionExpression']` | |
| `op` | `ConjunctionOps` | |
| `rhs` | `Union[ComparisonExpression, 'ConjunctionExpression']` | |

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
