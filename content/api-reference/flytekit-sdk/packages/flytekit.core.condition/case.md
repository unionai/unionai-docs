---
title: Case
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Case

**Package:** `flytekit.core.condition`

```python
class Case(
    cs: ConditionalSection,
    expr: Optional[Union[ComparisonExpression, ConjunctionExpression]],
    stmt: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cs` | `ConditionalSection` | |
| `expr` | `Optional[Union[ComparisonExpression, ConjunctionExpression]]` | |
| `stmt` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `err` | `None` |  |
| `expr` | `None` |  |
| `output_node` | `None` |  |
| `output_promise` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`fail()`](#fail) |  |
| [`then()`](#then) |  |


### fail()

```python
def fail(
    err: str,
) -> Promise
```
| Parameter | Type | Description |
|-|-|-|
| `err` | `str` | |

### then()

```python
def then(
    p: Union[Promise, Tuple[Promise]],
) -> Optional[Union[Condition, Promise, Tuple[Promise], VoidPromise]]
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `Union[Promise, Tuple[Promise]]` | |

