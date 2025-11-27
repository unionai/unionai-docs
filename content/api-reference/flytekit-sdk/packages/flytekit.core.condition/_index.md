---
title: flytekit.core.condition
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.condition

## Directory

### Classes

| Class | Description |
|-|-|
| [`BranchNode`](../flytekit.core.condition/branchnode) |  |
| [`Case`](../flytekit.core.condition/case) |  |
| [`Condition`](../flytekit.core.condition/condition) |  |
| [`ConditionalSection`](../flytekit.core.condition/conditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`LocalExecutedConditionalSection`](../flytekit.core.condition/localexecutedconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`SkippedConditionalSection`](../flytekit.core.condition/skippedconditionalsection) | This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |

### Methods

| Method | Description |
|-|-|
| [`conditional()`](#conditional) | Use a conditional section to control the flow of a workflow. |
| [`create_branch_node_promise_var()`](#create_branch_node_promise_var) | Generates a globally (wf-level) unique id for a variable. |
| [`merge_promises()`](#merge_promises) |  |
| [`to_branch_node()`](#to_branch_node) |  |
| [`to_case_block()`](#to_case_block) |  |
| [`to_ifelse_block()`](#to_ifelse_block) |  |
| [`transform_to_boolexpr()`](#transform_to_boolexpr) |  |
| [`transform_to_comp_expr()`](#transform_to_comp_expr) |  |
| [`transform_to_conj_expr()`](#transform_to_conj_expr) |  |
| [`transform_to_operand()`](#transform_to_operand) |  |


## Methods

#### conditional()

```python
def conditional(
    name: str,
) -> ConditionalSection
```
Use a conditional section to control the flow of a workflow. Conditional sections can only be used inside a workflow
context. Outside of a workflow they will raise an Assertion.

The ``conditional`` method returns a new conditional section, that allows to create a - ternary operator like
if-else clauses. The reason why it is called ternary-like is because, it returns the output of the branch result.
So in-effect it is a functional style condition.

Example of a condition usage. Note the nesting and the assignment to a LHS variable

```python
v = (
conditional("fractions")
.if_((my_input > 0.1) & (my_input < 1.0))
.then(
    conditional("inner_fractions")
    .if_(my_input < 0.5)
    .then(double(n=my_input))
    .elif_((my_input > 0.5) & (my_input < 0.7))
    .then(square(n=my_input))
    .else_()
    .fail("Only <0.7 allowed")
)
.elif_((my_input > 1.0) & (my_input < 10.0))
.then(square(n=my_input))
.else_()
.then(double(n=my_input))
)
```


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

#### create_branch_node_promise_var()

```python
def create_branch_node_promise_var(
    node_id: str,
    var: str,
) -> str
```
Generates a globally (wf-level) unique id for a variable.

When building bindings for the branch node, the inputs to the conditions (e.g. (x==5)) need to have variable names
(e.g. x). Because it's currently infeasible to get the name (e.g. x), we resolve to using the referenced node's
output name (e.g. o0, my_out,... etc.). In order to avoid naming collisions (in cases when, for example, the
conditions reference two outputs of two different nodes named the same), we build a variable name composed of the
referenced node name + '.' + the referenced output name. Ideally we use something like
(https://github.com/pwwang/python-varname) to retrieve the assigned variable name (e.g. x). However, because of
https://github.com/pwwang/python-varname/issues/28, this is not currently supported for all AST nodes types.



| Parameter | Type | Description |
|-|-|-|
| `node_id` | `str` | |
| `var` | `str` | |

#### merge_promises()

```python
def merge_promises(
    args: *args,
) -> typing.List[Promise]
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |

#### to_branch_node()

```python
def to_branch_node(
    name: str,
    cs: ConditionalSection,
) -> Tuple[BranchNode, typing.List[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `cs` | `ConditionalSection` | |

#### to_case_block()

```python
def to_case_block(
    c: Case,
) -> Tuple[Union[_core_wf.IfBlock], typing.List[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `c` | `Case` | |

#### to_ifelse_block()

```python
def to_ifelse_block(
    node_id: str,
    cs: ConditionalSection,
) -> Tuple[_core_wf.IfElseBlock, typing.List[Binding]]
```
| Parameter | Type | Description |
|-|-|-|
| `node_id` | `str` | |
| `cs` | `ConditionalSection` | |

#### transform_to_boolexpr()

```python
def transform_to_boolexpr(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Tuple[_core_cond.BooleanExpression, typing.List[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` | |

#### transform_to_comp_expr()

```python
def transform_to_comp_expr(
    expr: ComparisonExpression,
) -> Tuple[_core_cond.ComparisonExpression, typing.List[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `expr` | `ComparisonExpression` | |

#### transform_to_conj_expr()

```python
def transform_to_conj_expr(
    expr: ConjunctionExpression,
) -> Tuple[_core_cond.ConjunctionExpression, typing.List[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `expr` | `ConjunctionExpression` | |

#### transform_to_operand()

```python
def transform_to_operand(
    v: Union[Promise, Literal],
) -> Tuple[_core_cond.Operand, Optional[Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `v` | `Union[Promise, Literal]` | |

