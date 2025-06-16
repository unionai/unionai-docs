---
title: flytekit.core.condition
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.condition

## Directory

### Classes

| Class | Description |
|-|-|
| [`BranchNode`](.././flytekit.core.condition#flytekitcoreconditionbranchnode) |  |
| [`Case`](.././flytekit.core.condition#flytekitcoreconditioncase) |  |
| [`Condition`](.././flytekit.core.condition#flytekitcoreconditioncondition) |  |
| [`ConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`LocalExecutedConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionlocalexecutedconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`SkippedConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionskippedconditionalsection) | This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |

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


| Parameter | Type |
|-|-|
| `name` | `str` |

#### create_branch_node_promise_var()

```python
def create_branch_node_promise_var(
    node_id: str,
    var: str,
) -> n: The generated unique id of the variable.
```
Generates a globally (wf-level) unique id for a variable.

When building bindings for the branch node, the inputs to the conditions (e.g. (x==5)) need to have variable names
(e.g. x). Because it's currently infeasible to get the name (e.g. x), we resolve to using the referenced node's
output name (e.g. o0, my_out,... etc.). In order to avoid naming collisions (in cases when, for example, the
conditions reference two outputs of two different nodes named the same), we build a variable name composed of the
referenced node name + '.' + the referenced output name. Ideally we use something like
(https://github.com/pwwang/python-varname) to retrieve the assigned variable name (e.g. x). However, because of
https://github.com/pwwang/python-varname/issues/28, this is not currently supported for all AST nodes types.



| Parameter | Type |
|-|-|
| `node_id` | `str` |
| `var` | `str` |

#### merge_promises()

```python
def merge_promises(
    args: `*args`,
) -> typing.List[Promise]
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |

#### to_branch_node()

```python
def to_branch_node(
    name: str,
    cs: ConditionalSection,
) -> Tuple[BranchNode, typing.List[Promise]]
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `cs` | `ConditionalSection` |

#### to_case_block()

```python
def to_case_block(
    c: Case,
) -> Tuple[Union[_core_wf.IfBlock], typing.List[Promise]]
```
| Parameter | Type |
|-|-|
| `c` | `Case` |

#### to_ifelse_block()

```python
def to_ifelse_block(
    node_id: str,
    cs: ConditionalSection,
) -> Tuple[_core_wf.IfElseBlock, typing.List[Binding]]
```
| Parameter | Type |
|-|-|
| `node_id` | `str` |
| `cs` | `ConditionalSection` |

#### transform_to_boolexpr()

```python
def transform_to_boolexpr(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Tuple[_core_cond.BooleanExpression, typing.List[Promise]]
```
| Parameter | Type |
|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` |

#### transform_to_comp_expr()

```python
def transform_to_comp_expr(
    expr: ComparisonExpression,
) -> Tuple[_core_cond.ComparisonExpression, typing.List[Promise]]
```
| Parameter | Type |
|-|-|
| `expr` | `ComparisonExpression` |

#### transform_to_conj_expr()

```python
def transform_to_conj_expr(
    expr: ConjunctionExpression,
) -> Tuple[_core_cond.ConjunctionExpression, typing.List[Promise]]
```
| Parameter | Type |
|-|-|
| `expr` | `ConjunctionExpression` |

#### transform_to_operand()

```python
def transform_to_operand(
    v: Union[Promise, Literal],
) -> Tuple[_core_cond.Operand, Optional[Promise]]
```
| Parameter | Type |
|-|-|
| `v` | `Union[Promise, Literal]` |

## flytekit.core.condition.BranchNode

```python
class BranchNode(
    name: str,
    ifelse_block: _core_wf.IfElseBlock,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `ifelse_block` | `_core_wf.IfElseBlock` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` |  |  |

## flytekit.core.condition.Case

```python
class Case(
    cs: ConditionalSection,
    expr: Optional[Union[ComparisonExpression, ConjunctionExpression]],
    stmt: str,
)
```
| Parameter | Type |
|-|-|
| `cs` | `ConditionalSection` |
| `expr` | `Optional[Union[ComparisonExpression, ConjunctionExpression]]` |
| `stmt` | `str` |

### Methods

| Method | Description |
|-|-|
| [`fail()`](#fail) |  |
| [`then()`](#then) |  |


#### fail()

```python
def fail(
    err: str,
) -> Promise
```
| Parameter | Type |
|-|-|
| `err` | `str` |

#### then()

```python
def then(
    p: Union[Promise, Tuple[Promise]],
) -> Optional[Union[Condition, Promise, Tuple[Promise], VoidPromise]]
```
| Parameter | Type |
|-|-|
| `p` | `Union[Promise, Tuple[Promise]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `err` |  |  |
| `expr` |  |  |
| `output_node` |  |  |
| `output_promise` |  |  |

## flytekit.core.condition.Condition

```python
class Condition(
    cs: ConditionalSection,
)
```
| Parameter | Type |
|-|-|
| `cs` | `ConditionalSection` |

### Methods

| Method | Description |
|-|-|
| [`elif_()`](#elif_) |  |
| [`else_()`](#else_) |  |


#### elif_()

```python
def elif_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type |
|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` |

#### else_()

```python
def else_()
```
## flytekit.core.condition.ConditionalSection

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
class ConditionalSection(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`compute_output_vars()`](#compute_output_vars) | Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have. |
| [`end_branch()`](#end_branch) | This should be invoked after every branch has been visited. |
| [`if_()`](#if_) |  |
| [`start_branch()`](#start_branch) | At the start of an execution of every branch this method should be called. |


#### compute_output_vars()

```python
def compute_output_vars()
```
Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have
been registered


#### end_branch()

```python
def end_branch()
```
This should be invoked after every branch has been visited.
In case this is not local workflow execution then, we should check if this is the last case.
If so then return the promise, else return the condition


#### if_()

```python
def if_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type |
|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` |

#### start_branch()

```python
def start_branch(
    c: Case,
    last_case: bool,
) -> Case
```
At the start of an execution of every branch this method should be called.


| Parameter | Type |
|-|-|
| `c` | `Case` |
| `last_case` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `cases` |  |  |
| `name` |  |  |

## flytekit.core.condition.LocalExecutedConditionalSection

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
| Parameter | Type |
|-|-|
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`compute_output_vars()`](#compute_output_vars) | Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have. |
| [`end_branch()`](#end_branch) | This should be invoked after every branch has been visited. |
| [`if_()`](#if_) |  |
| [`start_branch()`](#start_branch) | At the start of an execution of every branch this method should be called. |


#### compute_output_vars()

```python
def compute_output_vars()
```
Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have
been registered


#### end_branch()

```python
def end_branch()
```
This should be invoked after every branch has been visited
In case of Local workflow execution, we should first mark the branch as complete, then
Then we first check for if this is the last case,
In case this is the last case, we return the output from the selected case - A case should always
be selected (see start_branch)
If this is not the last case, we should return the condition so that further chaining can be done


#### if_()

```python
def if_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type |
|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` |

#### start_branch()

```python
def start_branch(
    c: Case,
    last_case: bool,
) -> Case
```
At the start of an execution of every branch this method should be called.


| Parameter | Type |
|-|-|
| `c` | `Case` |
| `last_case` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `cases` |  |  |
| `name` |  |  |

## flytekit.core.condition.SkippedConditionalSection

This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false.
This ensures that the branch is not evaluated and thus the local tasks are not executed.


```python
class SkippedConditionalSection(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`compute_output_vars()`](#compute_output_vars) | Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have. |
| [`end_branch()`](#end_branch) | This should be invoked after every branch has been visited. |
| [`if_()`](#if_) |  |
| [`start_branch()`](#start_branch) | At the start of an execution of every branch this method should be called. |


#### compute_output_vars()

```python
def compute_output_vars()
```
Computes and returns the minimum set of outputs for this conditional block, based on all the cases that have
been registered


#### end_branch()

```python
def end_branch()
```
This should be invoked after every branch has been visited


#### if_()

```python
def if_(
    expr: Union[ComparisonExpression, ConjunctionExpression],
) -> Case
```
| Parameter | Type |
|-|-|
| `expr` | `Union[ComparisonExpression, ConjunctionExpression]` |

#### start_branch()

```python
def start_branch(
    c: Case,
    last_case: bool,
) -> Case
```
At the start of an execution of every branch this method should be called.


| Parameter | Type |
|-|-|
| `c` | `Case` |
| `last_case` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `cases` |  |  |
| `name` |  |  |

