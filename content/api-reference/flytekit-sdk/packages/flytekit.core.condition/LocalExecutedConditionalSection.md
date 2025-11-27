---
title: LocalExecutedConditionalSection
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LocalExecutedConditionalSection

**Package:** `flytekit.core.condition`

ConditionalSection is used to denote a condition within a Workflow. This default conditional section only works
for Compilation mode. It is advised to derive the class and re-implement the `start_branch` and `end_branch` methods
to override the compilation behavior

> [!NOTE]
> Conditions can only be used within a workflow context.

Usage:

```python
v =  conditional("fractions").if_((my_input > 0.1) & (my_input < 1.0)).then(...)...
```


```python
class LocalExecutedConditionalSection(
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

## Properties

| Property | Type | Description |
|-|-|-|
| `cases` |  |  |
| `name` |  |  |

