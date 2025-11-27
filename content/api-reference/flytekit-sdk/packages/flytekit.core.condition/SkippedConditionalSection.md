---
title: SkippedConditionalSection
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SkippedConditionalSection

**Package:** `flytekit.core.condition`

This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false.
This ensures that the branch is not evaluated and thus the local tasks are not executed.


```python
class SkippedConditionalSection(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`compute_output_vars()`](#compute_output_vars) | Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have. |
| [`end_branch()`](#end_branch) | This should be invoked after every branch has been visited. |
| [`if_()`](#if_) |  |
| [`start_branch()`](#start_branch) | At the start of an execution of every branch this method should be called. |


### compute_output_vars()

```python
def compute_output_vars()
```
Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have
been registered


### end_branch()

```python
def end_branch()
```
This should be invoked after every branch has been visited


### if_()

```python
def if_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type | Description |
|-|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` | |

### start_branch()

```python
def start_branch(
    c: Case,
    last_case: bool,
) -> Case
```
At the start of an execution of every branch this method should be called.


| Parameter | Type | Description |
|-|-|-|
| `c` | `Case` | -&gt; the case that represents this branch |
| `last_case` | `bool` | -&gt; a boolean that indicates if this is the last branch in the ifelseblock |

## Properties

| Property | Type | Description |
|-|-|-|
| `cases` |  |  |
| `name` |  |  |

