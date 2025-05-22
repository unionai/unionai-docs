---
title: flytekit.core.promise
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.promise

## Directory

### Classes

| Class | Description |
|-|-|
| [`ComparisonExpression`](.././flytekit.core.promise#flytekitcorepromisecomparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`ConjunctionExpression`](.././flytekit.core.promise#flytekitcorepromiseconjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`HasFlyteInterface`](.././flytekit.core.promise#flytekitcorepromisehasflyteinterface) | Base class for protocol classes. |
| [`LocallyExecutable`](.././flytekit.core.promise#flytekitcorepromiselocallyexecutable) | Base class for protocol classes. |
| [`NodeOutput`](.././flytekit.core.promise#flytekitcorepromisenodeoutput) |  |
| [`Promise`](.././flytekit.core.promise#flytekitcorepromisepromise) | This object is a wrapper and exists for three main reasons. |
| [`SupportsNodeCreation`](.././flytekit.core.promise#flytekitcorepromisesupportsnodecreation) | Base class for protocol classes. |
| [`VoidPromise`](.././flytekit.core.promise#flytekitcorepromisevoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |

### Methods

| Method | Description |
|-|-|
| [`async_flyte_entity_call_handler()`](#async_flyte_entity_call_handler) | This is a limited async version of the main call handler. |
| [`binding_data_from_python_std()`](#binding_data_from_python_std) |  |
| [`binding_from_python_std()`](#binding_from_python_std) |  |
| [`create_and_link_node()`](#create_and_link_node) | This method is used to generate a node with bindings within a flytekit workflow. |
| [`create_and_link_node_from_remote()`](#create_and_link_node_from_remote) | This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,. |
| [`create_native_named_tuple()`](#create_native_named_tuple) | Creates and returns a Named tuple with all variables that match the expected named outputs. |
| [`create_task_output()`](#create_task_output) |  |
| [`extract_obj_name()`](#extract_obj_name) | Generates a shortened name, without the module information. |
| [`flyte_entity_call_handler()`](#flyte_entity_call_handler) | This function is the call handler for tasks, workflows, and launch plans (which redirects to the underlying. |
| [`get_primitive_val()`](#get_primitive_val) |  |
| [`resolve_attr_path_in_dict()`](#resolve_attr_path_in_dict) |  |
| [`resolve_attr_path_in_pb_struct()`](#resolve_attr_path_in_pb_struct) | Resolves the protobuf struct (e. |
| [`resolve_attr_path_in_promise()`](#resolve_attr_path_in_promise) | resolve_attr_path_in_promise resolves the attribute path in a promise and returns a new promise with the resolved value. |
| [`resolve_attr_path_recursively()`](#resolve_attr_path_recursively) | This function resolves the attribute path in a nested structure recursively. |
| [`to_binding()`](#to_binding) |  |
| [`translate_inputs_to_literals()`](#translate_inputs_to_literals) | The point of this function is to extract out Literals from a collection of either Python native values (which would. |
| [`translate_inputs_to_native()`](#translate_inputs_to_native) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## Methods

#### async_flyte_entity_call_handler()

```python
def async_flyte_entity_call_handler(
    entity: SupportsNodeCreation,
    args,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, Tuple, None]
```
This is a limited async version of the main call handler.


| Parameter | Type |
|-|-|
| `entity` | `SupportsNodeCreation` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### binding_data_from_python_std()

```python
def binding_data_from_python_std(
    ctx: _flyte_context.FlyteContext,
    expected_literal_type: _type_models.LiteralType,
    t_value: Any,
    t_value_type: typing.Type[T],
    nodes: List[Node],
) -> _literals_models.BindingData
```
| Parameter | Type |
|-|-|
| `ctx` | `_flyte_context.FlyteContext` |
| `expected_literal_type` | `_type_models.LiteralType` |
| `t_value` | `Any` |
| `t_value_type` | `typing.Type[T]` |
| `nodes` | `List[Node]` |

#### binding_from_python_std()

```python
def binding_from_python_std(
    ctx: _flyte_context.FlyteContext,
    var_name: str,
    expected_literal_type: _type_models.LiteralType,
    t_value: Any,
    t_value_type: type,
) -> Tuple[_literals_models.Binding, List[Node]]
```
| Parameter | Type |
|-|-|
| `ctx` | `_flyte_context.FlyteContext` |
| `var_name` | `str` |
| `expected_literal_type` | `_type_models.LiteralType` |
| `t_value` | `Any` |
| `t_value_type` | `type` |

#### create_and_link_node()

```python
def create_and_link_node(
    ctx: FlyteContext,
    entity: SupportsNodeCreation,
    overridden_interface: Optional[Interface],
    add_node_to_compilation_state: bool,
    node_id: str,
    kwargs,
) -> n:  Optional[Union[Tuple[Promise], Promise, VoidPromise]]
```
This method is used to generate a node with bindings within a flytekit workflow. this is useful to traverse the
workflow using regular python interpreter and generate nodes and promises whenever an execution is encountered



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `entity` | `SupportsNodeCreation` |
| `overridden_interface` | `Optional[Interface]` |
| `add_node_to_compilation_state` | `bool` |
| `node_id` | `str` |
| `kwargs` | ``**kwargs`` |

#### create_and_link_node_from_remote()

```python
def create_and_link_node_from_remote(
    ctx: FlyteContext,
    entity: HasFlyteInterface,
    overridden_interface: Optional[_interface_models.TypedInterface],
    add_node_to_compilation_state: bool,
    node_id: str,
    _inputs_not_allowed: Optional[Set[str]],
    _ignorable_inputs: Optional[Set[str]],
    kwargs,
) -> n:  Optional[Union[Tuple[Promise], Promise, VoidPromise]]
```
This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,
FlyteTask and FlyteLaunchplan.

This method is kept separate from the similar named method `create_and_link_node` as remote entities have to be
handled differently. The major difference arises from the fact that the remote entities do not have a python
interface, so all comparisons need to happen using the Literals.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `entity` | `HasFlyteInterface` |
| `overridden_interface` | `Optional[_interface_models.TypedInterface]` |
| `add_node_to_compilation_state` | `bool` |
| `node_id` | `str` |
| `_inputs_not_allowed` | `Optional[Set[str]]` |
| `_ignorable_inputs` | `Optional[Set[str]]` |
| `kwargs` | ``**kwargs`` |

#### create_native_named_tuple()

```python
def create_native_named_tuple(
    ctx: FlyteContext,
    promises: Union[Tuple[Promise], Promise, VoidPromise, None],
    entity_interface: Interface,
) -> Optional[Tuple]
```
Creates and returns a Named tuple with all variables that match the expected named outputs. this makes
it possible to run things locally and expect a more native behavior, i.e. address elements of a named tuple
by name.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `promises` | `Union[Tuple[Promise], Promise, VoidPromise, None]` |
| `entity_interface` | `Interface` |

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

#### extract_obj_name()

```python
def extract_obj_name(
    name: str,
) -> str
```
Generates a shortened name, without the module information. Useful for node-names etc. Only extracts the final
object information often separated by `.` in the python fully qualified notation


| Parameter | Type |
|-|-|
| `name` | `str` |

#### flyte_entity_call_handler()

```python
def flyte_entity_call_handler(
    entity: SupportsNodeCreation,
    args,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, Tuple, None]
```
This function is the call handler for tasks, workflows, and launch plans (which redirects to the underlying
workflow). The logic is the same for all three, but we did not want to create base class, hence this separate
method. When one of these entities is () aka __called__, there are three things we may do:
#. Compilation Mode - this happens when the function is called as part of a workflow (potentially
   dynamic task?). Instead of running the user function, produce promise objects and create a node.
#. Workflow Execution Mode - when a workflow is being run locally. Even though workflows are functions
   and everything should be able to be passed through naturally, we'll want to wrap output values of the
   function into objects, so that potential .with_cpu or other ancillary functions can be attached to do
   nothing. Subsequent tasks will have to know how to unwrap these. If by chance a non-Flyte task uses a
   task output as an input, things probably will fail pretty obviously.
#. Start a local execution - This means that we're not already in a local workflow execution, which means that
   we should expect inputs to be native Python values and that we should return Python native values.


| Parameter | Type |
|-|-|
| `entity` | `SupportsNodeCreation` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### get_primitive_val()

```python
def get_primitive_val(
    prim: Primitive,
) -> Any
```
| Parameter | Type |
|-|-|
| `prim` | `Primitive` |

#### resolve_attr_path_in_dict()

```python
def resolve_attr_path_in_dict(
    d: dict,
    attr_path: List[Union[str, int]],
) -> Any
```
| Parameter | Type |
|-|-|
| `d` | `dict` |
| `attr_path` | `List[Union[str, int]]` |

#### resolve_attr_path_in_pb_struct()

```python
def resolve_attr_path_in_pb_struct(
    st: _struct.Struct,
    attr_path: List[Union[str, int]],
) -> Union[_struct.Struct, _struct.ListValue]
```
Resolves the protobuf struct (e.g. dataclass) with attribute path.

Note that the return type can be google.protobuf.struct_pb2.Struct or google.protobuf.struct_pb2.ListValue.


| Parameter | Type |
|-|-|
| `st` | `_struct.Struct` |
| `attr_path` | `List[Union[str, int]]` |

#### resolve_attr_path_in_promise()

```python
def resolve_attr_path_in_promise(
    p: Promise,
) -> Promise
```
resolve_attr_path_in_promise resolves the attribute path in a promise and returns a new promise with the resolved value
This is for local execution only. The remote execution will be resolved in flytepropeller.


| Parameter | Type |
|-|-|
| `p` | `Promise` |

#### resolve_attr_path_recursively()

```python
def resolve_attr_path_recursively(
    v: Any,
) -> Any
```
This function resolves the attribute path in a nested structure recursively.


| Parameter | Type |
|-|-|
| `v` | `Any` |

#### to_binding()

```python
def to_binding(
    p: Promise,
) -> _literals_models.Binding
```
| Parameter | Type |
|-|-|
| `p` | `Promise` |

#### translate_inputs_to_literals()

```python
def translate_inputs_to_literals(
    ctx: FlyteContext,
    incoming_values: Dict[str, Any],
    flyte_interface_types: Dict[str, _interface_models.Variable],
    native_types: Dict[str, type],
) -> Dict[str, _literals_models.Literal]
```
The point of this function is to extract out Literals from a collection of either Python native values (which would
be converted into Flyte literals) or Promises (the literals in which would just get extracted).

When calling a task inside a workflow, a user might do something like this.

    def my_wf(in1: int) -> int:
        a = task_1(in1=in1)
        b = task_2(in1=5, in2=a)
        return b

If this is the case, when task_2 is called in local workflow execution, we'll need to translate the Python native
literal 5 to a Flyte literal.

More interesting is this:

    def my_wf(in1: int, in2: int) -> int:
        a = task_1(in1=in1)
        b = task_2(in1=5, in2=[a, in2])
        return b

Here, in task_2, during execution we'd have a list of Promises. We have to make sure to give task2 a Flyte
LiteralCollection (Flyte's name for list), not a Python list of Flyte literals.

This helper function is used both when sorting out inputs to a task, as well as outputs of a function.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `incoming_values` | `Dict[str, Any]` |
| `flyte_interface_types` | `Dict[str, _interface_models.Variable]` |
| `native_types` | `Dict[str, type]` |

#### translate_inputs_to_native()

```python
def translate_inputs_to_native(
    ctx: FlyteContext,
    incoming_values: Dict[str, Any],
    flyte_interface_types: Dict[str, _interface_models.Variable],
) -> Dict[str, _literals_models.Literal]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `incoming_values` | `Dict[str, Any]` |
| `flyte_interface_types` | `Dict[str, _interface_models.Variable]` |

## flytekit.core.promise.ComparisonExpression

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

## flytekit.core.promise.ConjunctionExpression

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

## flytekit.core.promise.HasFlyteInterface

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...


```python
class HasFlyteInterface(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |


#### construct_node_metadata()

```python
def construct_node_metadata()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `interface` |  |  |
| `name` |  |  |

## flytekit.core.promise.LocallyExecutable

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...


```python
class LocallyExecutable(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
## flytekit.core.promise.NodeOutput

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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |
| [`with_attr()`](#with_attr) |  |


#### deepcopy()

```python
def deepcopy()
```
#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: OutputReference
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.types.OutputReference


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
:rtype: list[union[str, int]]
{{< /multiline >}} |
| `is_empty` |  |  |
| `node` |  | {{< multiline >}}Return Node object.
{{< /multiline >}} |
| `node_id` |  | {{< multiline >}}Override the underlying node_id property to refer to the Node's id. This is to make sure that overriding
node IDs from with_overrides gets serialized correctly.
:rtype: Text
{{< /multiline >}} |
| `var` |  | {{< multiline >}}Variable name must refer to an output variable for the node.
:rtype: Text
{{< /multiline >}} |

## flytekit.core.promise.Promise

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
:rtype: List[Union[str, int]]
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

## flytekit.core.promise.SupportsNodeCreation

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...


```python
class SupportsNodeCreation(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) |  |


#### construct_node_metadata()

```python
def construct_node_metadata()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `name` |  |  |
| `python_interface` |  |  |

## flytekit.core.promise.VoidPromise

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

