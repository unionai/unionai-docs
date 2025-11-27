---
title: Condition
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Condition

**Package:** `flytekit.core.condition`

```python
class Condition(
    cs: ConditionalSection,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cs` | `ConditionalSection` | |

## Methods

| Method | Description |
|-|-|
| [`elif_()`](#elif_) |  |
| [`else_()`](#else_) |  |


### elif_()

```python
def elif_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type | Description |
|-|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` | |

### else_()

```python
def else_()
```
