---
title: ConditionalSection
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConditionalSection

**Package:** `flytekit.core.condition`

ConditionalSection is used to denote a condition within a Workflow. This default conditional section only works
for Compilation mode. It is advised to derive the class and re-implement the `start_branch` and `end_branch` methods
to override the compilation behavior

&gt; [!NOTE]
&gt; Conditions can only be used within a workflow context.

Usage:

```python
v =  conditional("fractions").if_((my_input > 0.1) & (my_input < 1.0)).then(...)...
```



```python
class ConditionalSection(
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
This should be invoked after every branch has been visited.
In case this is not local workflow execution then, we should check if this is the last case.
If so then return the promise, else return the condition


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

