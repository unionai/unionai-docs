---
title: LocalExecutedConditionalSection
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocalExecutedConditionalSection

**Package:** `flytekit.core.condition`

```python
class LocalExecutedConditionalSection(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `cases` | `None` |  |
| `name` | `None` |  |

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
In case of Local workflow execution, we should first mark the branch as complete, then
Then we first check for if this is the last case,
In case this is the last case, we return the output from the selected case - A case should always
be selected (see start_branch)
If this is not the last case, we should return the condition so that further chaining can be done


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

