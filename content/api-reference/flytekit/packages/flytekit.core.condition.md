---
title: flytekit.core.condition
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.condition

## Directory

### Classes

| Class | Description |
|-|-|
| [`Binding`](.././flytekit.core.condition#flytekitcoreconditionbinding) |  |
| [`BindingData`](.././flytekit.core.condition#flytekitcoreconditionbindingdata) |  |
| [`BranchNode`](.././flytekit.core.condition#flytekitcoreconditionbranchnode) |  |
| [`Case`](.././flytekit.core.condition#flytekitcoreconditioncase) |  |
| [`ComparisonExpression`](.././flytekit.core.condition#flytekitcoreconditioncomparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`ComparisonOps`](.././flytekit.core.condition#flytekitcoreconditioncomparisonops) | Create a collection of name/value pairs. |
| [`Condition`](.././flytekit.core.condition#flytekitcoreconditioncondition) |  |
| [`ConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`ConjunctionExpression`](.././flytekit.core.condition#flytekitcoreconditionconjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`ConjunctionOps`](.././flytekit.core.condition#flytekitcoreconditionconjunctionops) | Create a collection of name/value pairs. |
| [`Error`](.././flytekit.core.condition#flytekitcoreconditionerror) |  |
| [`FlyteContextManager`](.././flytekit.core.condition#flytekitcoreconditionflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Literal`](.././flytekit.core.condition#flytekitcoreconditionliteral) |  |
| [`LocalExecutedConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionlocalexecutedconditionalsection) | ConditionalSection is used to denote a condition within a Workflow. |
| [`Node`](.././flytekit.core.condition#flytekitcoreconditionnode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`NodeOutput`](.././flytekit.core.condition#flytekitcoreconditionnodeoutput) |  |
| [`Promise`](.././flytekit.core.condition#flytekitcoreconditionpromise) | This object is a wrapper and exists for three main reasons. |
| [`RetryStrategy`](.././flytekit.core.condition#flytekitcoreconditionretrystrategy) |  |
| [`SkippedConditionalSection`](.././flytekit.core.condition#flytekitcoreconditionskippedconditionalsection) | This ConditionalSection is used for nested conditionals, when the branch has been evaluated to false. |
| [`VoidPromise`](.././flytekit.core.condition#flytekitcoreconditionvoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |

### Methods

| Method | Description |
|-|-|
| [`cast()`](#cast) | Cast a value to a type. |
| [`conditional()`](#conditional) | Use a conditional section to control the flow of a workflow. |
| [`create_branch_node_promise_var()`](#create_branch_node_promise_var) | Generates a globally (wf-level) unique id for a variable. |
| [`create_task_output()`](#create_task_output) |  |
| [`merge_promises()`](#merge_promises) |  |
| [`to_branch_node()`](#to_branch_node) |  |
| [`to_case_block()`](#to_case_block) |  |
| [`to_ifelse_block()`](#to_ifelse_block) |  |
| [`transform_to_boolexpr()`](#transform_to_boolexpr) |  |
| [`transform_to_comp_expr()`](#transform_to_comp_expr) |  |
| [`transform_to_conj_expr()`](#transform_to_conj_expr) |  |
| [`transform_to_operand()`](#transform_to_operand) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |

## Methods

#### cast()

```python
def cast(
    typ,
    val,
)
```
Cast a value to a type.

This returns the value unchanged.  To the type checker this
signals that the return value has the designated type, but at
runtime we intentionally don't check anything (we want this
to be as fast as possible).


| Parameter | Type |
|-|-|
| `typ` |  |
| `val` |  |

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

.. code-block:: python

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


| Parameter | Type |
|-|-|
| `name` | `str` |

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



| Parameter | Type |
|-|-|
| `node_id` | `str` |
| `var` | `str` |

#### create_task_output()

```python
def create_task_output(
    promises: Optional[Union[List[Promise], Promise]],
    entity_interface: Optional[Interface],
) -> Optional[Union[Tuple[Promise], Promise]]
```
| Parameter | Type |
|-|-|
| `promises` | `Optional[Union[List[Promise], Promise]]` |
| `entity_interface` | `Optional[Interface]` |

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

## flytekit.core.condition.Binding

```python
class Binding(
    var,
    binding,
)
```
An input/output binding of a variable to either static value or a node output.



| Parameter | Type |
|-|-|
| `var` |  |
| `binding` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> flytekit.core.models.literals.Binding
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `binding` |  | {{< multiline >}}Data to use to bind this variable.
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}A variable name, must match an input or output variable of the node.
{{< /multiline >}} |

## flytekit.core.condition.BindingData

```python
class BindingData(
    scalar,
    collection,
    promise,
    map,
)
```
Specifies either a simple value or a reference to another output. Only one of the input arguments may be
specified.



| Parameter | Type |
|-|-|
| `scalar` |  |
| `collection` |  |
| `promise` |  |
| `map` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`to_literal_model()`](#to_literal_model) | Converts current binding data into a Literal asserting that there are no promises in the bindings. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### to_literal_model()

```python
def to_literal_model()
```
Converts current binding data into a Literal asserting that there are no promises in the bindings.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}[Optional] A collection of binding data. This allows nesting of binding data to any number of levels.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}[Optional] A map of bindings. The key is always a string.
{{< /multiline >}} |
| `promise` |  | {{< multiline >}}[Optional] References an output promised by another node.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}A simple scalar value.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns whichever value is set
{{< /multiline >}} |

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

## flytekit.core.condition.ComparisonExpression

ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands
and operator can be any comparison expression like <, >, <=, >=, ==, !=


```python
class ComparisonExpression(
    lhs: Union['Promise', Any],
    op: ComparisonOps,
    rhs: Union['Promise', Any],
)
```
| Parameter | Type |
|-|-|
| `lhs` | `Union['Promise', Any]` |
| `op` | `ComparisonOps` |
| `rhs` | `Union['Promise', Any]` |

### Methods

| Method | Description |
|-|-|
| [`eval()`](#eval) |  |


#### eval()

```python
def eval()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `lhs` |  |  |
| `op` |  |  |
| `rhs` |  |  |

## flytekit.core.condition.ComparisonOps

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


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

.. note::

Conditions can only be used within a workflow context.

Usage:

.. code-block:: python

v =  conditional("fractions").if_((my_input > 0.1) & (my_input < 1.0)).then(...)...


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

## flytekit.core.condition.ConjunctionExpression

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
| Parameter | Type |
|-|-|
| `lhs` | `Union[ComparisonExpression, 'ConjunctionExpression']` |
| `op` | `ConjunctionOps` |
| `rhs` | `Union[ComparisonExpression, 'ConjunctionExpression']` |

### Methods

| Method | Description |
|-|-|
| [`eval()`](#eval) |  |


#### eval()

```python
def eval()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `lhs` |  |  |
| `op` |  |  |
| `rhs` |  |  |

## flytekit.core.condition.ConjunctionOps

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.core.condition.Error

```python
class Error(
    failed_node_id: str,
    message: str,
)
```
| Parameter | Type |
|-|-|
| `failed_node_id` | `str` |
| `message` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.types_pb2.Error,
) -> Error
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.types_pb2.Error` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `failed_node_id` |  |  |
| `is_empty` |  |  |
| `message` |  |  |

## flytekit.core.condition.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
) -> traceback.FrameSummary
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
) -> FlyteContext
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.core.condition.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.core.condition.LocalExecutedConditionalSection

ConditionalSection is used to denote a condition within a Workflow. This default conditional section only works
for Compilation mode. It is advised to derive the class and re-implement the `start_branch` and `end_branch` methods
to override the compilation behavior

.. note::

Conditions can only be used within a workflow context.

Usage:

.. code-block:: python

v =  conditional("fractions").if_((my_input > 0.1) & (my_input < 1.0)).then(...)...


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

## flytekit.core.condition.Node

This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like
ID, which from the registration step


```python
class Node(
    id: str,
    metadata: _workflow_model.NodeMetadata,
    bindings: List[_literal_models.Binding],
    upstream_nodes: List[Node],
    flyte_entity: Any,
)
```
| Parameter | Type |
|-|-|
| `id` | `str` |
| `metadata` | `_workflow_model.NodeMetadata` |
| `bindings` | `List[_literal_models.Binding]` |
| `upstream_nodes` | `List[Node]` |
| `flyte_entity` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is typically something we shouldn't do. |
| [`with_overrides()`](#with_overrides) |  |


#### runs_before()

```python
def runs_before(
    other: Node,
)
```
This is typically something we shouldn't do. This modifies an attribute of the other instance rather than
self. But it's done so only because we wanted this English function to be the same as the shift function.
That is, calling node_1.runs_before(node_2) and node_1 >> node_2 are the same. The shift operator going the
other direction is not implemented to further avoid confusion. Right shift was picked rather than left shift
because that's what most users are familiar with.


| Parameter | Type |
|-|-|
| `other` | `Node` |

#### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[bool],
    cache_version: Optional[str],
    cache_serialize: Optional[bool],
    shared_memory: Optional[Union[L[True], str]],
    pod_template: Optional[PodTemplate],
    resources: Optional[Resources],
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `node_name` | `Optional[str]` |
| `aliases` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` |
| `retries` | `Optional[int]` |
| `interruptible` | `Optional[bool]` |
| `name` | `Optional[str]` |
| `task_config` | `Optional[Any]` |
| `container_image` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `cache` | `Optional[bool]` |
| `cache_version` | `Optional[str]` |
| `cache_serialize` | `Optional[bool]` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `pod_template` | `Optional[PodTemplate]` |
| `resources` | `Optional[Resources]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bindings` |  |  |
| `flyte_entity` |  |  |
| `id` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `outputs` |  |  |
| `run_entity` |  |  |
| `upstream_nodes` |  |  |

## flytekit.core.condition.NodeOutput

```python
class NodeOutput(
    node: Node,
    var: str,
    attr_path: Optional[List[Union[str, int]]],
)
```
| Parameter | Type |
|-|-|
| `node` | `Node` |
| `var` | `str` |
| `attr_path` | `Optional[List[Union[str, int]]]` |

### Methods

| Method | Description |
|-|-|
| [`deepcopy()`](#deepcopy) |  |
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |
| [`with_attr()`](#with_attr) |  |


#### deepcopy()

```python
def deepcopy()
```
#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> OutputReference
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
#### with_attr()

```python
def with_attr(
    key,
) -> NodeOutput
```
| Parameter | Type |
|-|-|
| `key` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` |  | {{< multiline >}}The attribute path the promise will be resolved with.
{{< /multiline >}} |
| `is_empty` |  |  |
| `node` |  | {{< multiline >}}Return Node object.
{{< /multiline >}} |
| `node_id` |  | {{< multiline >}}Override the underlying node_id property to refer to the Node's id. This is to make sure that overriding
node IDs from with_overrides gets serialized correctly.
{{< /multiline >}} |
| `var` |  | {{< multiline >}}Variable name must refer to an output variable for the node.
{{< /multiline >}} |

## flytekit.core.condition.Promise

This object is a wrapper and exists for three main reasons. Let's assume we're dealing with a task like ::

@task
def t1() -> (int, str): ...

#. Handling the duality between compilation and local execution - when the task function is run in a local execution
mode inside a workflow function, a Python integer and string are produced. When the task is being compiled as
part of the workflow, the task call creates a Node instead, and the task returns two Promise objects that
point to that Node.
#. One needs to be able to call ::

x = t1().with_overrides(...)

If the task returns an integer or a ``(int, str)`` tuple like ``t1`` above, calling ``with_overrides`` on the
result would throw an error. This Promise object adds that.
#. Assorted handling for conditionals.


```python
class Promise(
    var: str,
    val: Union[NodeOutput, _literals_models.Literal],
    type: typing.Optional[_type_models.LiteralType],
)
```
| Parameter | Type |
|-|-|
| `var` | `str` |
| `val` | `Union[NodeOutput, _literals_models.Literal]` |
| `type` | `typing.Optional[_type_models.LiteralType]` |

### Methods

| Method | Description |
|-|-|
| [`deepcopy()`](#deepcopy) |  |
| [`eval()`](#eval) |  |
| [`is_()`](#is_) |  |
| [`is_false()`](#is_false) |  |
| [`is_none()`](#is_none) |  |
| [`is_true()`](#is_true) |  |
| [`with_overrides()`](#with_overrides) |  |
| [`with_var()`](#with_var) |  |


#### deepcopy()

```python
def deepcopy()
```
#### eval()

```python
def eval()
```
#### is_()

```python
def is_(
    v: bool,
) -> ComparisonExpression
```
| Parameter | Type |
|-|-|
| `v` | `bool` |

#### is_false()

```python
def is_false()
```
#### is_none()

```python
def is_none()
```
#### is_true()

```python
def is_true()
```
#### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[bool],
    cache_version: Optional[str],
    cache_serialize: Optional[bool],
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `node_name` | `Optional[str]` |
| `aliases` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` |
| `retries` | `Optional[int]` |
| `interruptible` | `Optional[bool]` |
| `name` | `Optional[str]` |
| `task_config` | `Optional[Any]` |
| `container_image` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `cache` | `Optional[bool]` |
| `cache_version` | `Optional[str]` |
| `cache_serialize` | `Optional[bool]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### with_var()

```python
def with_var(
    new_var: str,
) -> Promise
```
| Parameter | Type |
|-|-|
| `new_var` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` |  | {{< multiline >}}The attribute path the promise will be resolved with.
{{< /multiline >}} |
| `is_ready` |  | {{< multiline >}}Returns if the Promise is READY (is not a reference and the val is actually ready)

Usage ::

p = Promise(...)
...
if p.is_ready():
print(p.val)
else:
print(p.ref)
{{< /multiline >}} |
| `ref` |  | {{< multiline >}}If the promise is NOT READY / Incomplete, then it maps to the origin node that owns the promise
{{< /multiline >}} |
| `val` |  | {{< multiline >}}If the promise is ready then this holds the actual evaluate value in Flyte's type system
{{< /multiline >}} |
| `var` |  | {{< multiline >}}Name of the variable bound with this promise
{{< /multiline >}} |

## flytekit.core.condition.RetryStrategy

```python
class RetryStrategy(
    retries: int,
)
```
| Parameter | Type |
|-|-|
| `retries` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> RetryStrategy
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `retries` |  | {{< multiline >}}Number of retries to attempt on recoverable failures.  If retries is 0, then only one attempt will be made.
{{< /multiline >}} |

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

## flytekit.core.condition.VoidPromise

This object is returned for tasks that do not return any outputs (declared interface is empty)
VoidPromise cannot be interacted with and does not allow comparisons or any operations


```python
class VoidPromise(
    task_name: str,
    ref: Optional[NodeOutput],
)
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `ref` | `Optional[NodeOutput]` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is a placeholder and should do nothing. |
| [`with_overrides()`](#with_overrides) |  |


#### runs_before()

```python
def runs_before(
    args,
    kwargs,
)
```
This is a placeholder and should do nothing. It is only here to enable local execution of workflows
where a task returns nothing.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### with_overrides()

```python
def with_overrides(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `ref` |  |  |
| `task_name` |  |  |

