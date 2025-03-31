---
title: flytekit.core.promise
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.promise

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.promise#flytekitcorepromiseany) | Special type indicating an unconstrained type. |
| [`AsyncTypeTransformer`](.././flytekit.core.promise#flytekitcorepromiseasynctypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`BaseAccelerator`](.././flytekit.core.promise#flytekitcorepromisebaseaccelerator) | Base class for all accelerator types. |
| [`Binary`](.././flytekit.core.promise#flytekitcorepromisebinary) |  |
| [`BranchEvalMode`](.././flytekit.core.promise#flytekitcorepromisebranchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`ComparisonExpression`](.././flytekit.core.promise#flytekitcorepromisecomparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`ComparisonOps`](.././flytekit.core.promise#flytekitcorepromisecomparisonops) | Create a collection of name/value pairs. |
| [`ConjunctionExpression`](.././flytekit.core.promise#flytekitcorepromiseconjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`ConjunctionOps`](.././flytekit.core.promise#flytekitcorepromiseconjunctionops) | Create a collection of name/value pairs. |
| [`DictTransformer`](.././flytekit.core.promise#flytekitcorepromisedicttransformer) | Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or. |
| [`Enum`](.././flytekit.core.promise#flytekitcorepromiseenum) | Create a collection of name/value pairs. |
| [`ExecutionParameters`](.././flytekit.core.promise#flytekitcorepromiseexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`ExecutionState`](.././flytekit.core.promise#flytekitcorepromiseexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.promise#flytekitcorepromiseflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.core.promise#flytekitcorepromiseflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`HasFlyteInterface`](.././flytekit.core.promise#flytekitcorepromisehasflyteinterface) | Base class for protocol classes. |
| [`Interface`](.././flytekit.core.promise#flytekitcorepromiseinterface) | A Python native interface object, like inspect. |
| [`Iterable`](.././flytekit.core.promise#flytekitcorepromiseiterable) |  |
| [`ListTransformer`](.././flytekit.core.promise#flytekitcorepromiselisttransformer) | Transformer that handles a univariate typing. |
| [`Literal`](.././flytekit.core.promise#flytekitcorepromiseliteral) |  |
| [`LocallyExecutable`](.././flytekit.core.promise#flytekitcorepromiselocallyexecutable) | Base class for protocol classes. |
| [`Node`](.././flytekit.core.promise#flytekitcorepromisenode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`NodeOutput`](.././flytekit.core.promise#flytekitcorepromisenodeoutput) |  |
| [`OutputMetadataTracker`](.././flytekit.core.promise#flytekitcorepromiseoutputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`Primitive`](.././flytekit.core.promise#flytekitcorepromiseprimitive) |  |
| [`Promise`](.././flytekit.core.promise#flytekitcorepromisepromise) | This object is a wrapper and exists for three main reasons. |
| [`Protocol`](.././flytekit.core.promise#flytekitcorepromiseprotocol) | Base class for protocol classes. |
| [`Resources`](.././flytekit.core.promise#flytekitcorepromiseresources) |  |
| [`Scalar`](.././flytekit.core.promise#flytekitcorepromisescalar) |  |
| [`SimpleType`](.././flytekit.core.promise#flytekitcorepromisesimpletype) |  |
| [`SupportsNodeCreation`](.././flytekit.core.promise#flytekitcorepromisesupportsnodecreation) | Base class for protocol classes. |
| [`TypeEngine`](.././flytekit.core.promise#flytekitcorepromisetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeTransformer`](.././flytekit.core.promise#flytekitcorepromisetypetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |
| [`UnionTransformer`](.././flytekit.core.promise#flytekitcorepromiseuniontransformer) | Transformer that handles a typing. |
| [`VoidPromise`](.././flytekit.core.promise#flytekitcorepromisevoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |

### Errors

| Exception | Description |
|-|-|
| [`FlytePromiseAttributeResolveException`](.././flytekit.core.promise#flytekitcorepromiseflytepromiseattributeresolveexception) | Assertion failed. |
| [`TypeTransformerFailedError`](.././flytekit.core.promise#flytekitcorepromisetypetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`_translate_inputs_to_literals()`](#_translate_inputs_to_literals) | The point of this function is to extract out Literals from a collection of either Python native values (which would. |
| [`_translate_inputs_to_native()`](#_translate_inputs_to_native) |  |
| [`async_flyte_entity_call_handler()`](#async_flyte_entity_call_handler) | This is a limited async version of the main call handler. |
| [`binding_data_from_python_std()`](#binding_data_from_python_std) |  |
| [`binding_from_python_std()`](#binding_from_python_std) |  |
| [`cast()`](#cast) | Cast a value to a type. |
| [`create_and_link_node()`](#create_and_link_node) | This method is used to generate a node with bindings within a flytekit workflow. |
| [`create_and_link_node_from_remote()`](#create_and_link_node_from_remote) | This method is used to generate a node with bindings especially when using remote entities, like FlyteWorkflow,. |
| [`create_native_named_tuple()`](#create_native_named_tuple) | Creates and returns a Named tuple with all variables that match the expected named outputs. |
| [`create_task_output()`](#create_task_output) |  |
| [`deepcopy()`](#deepcopy) | Deep copy operation on arbitrary Python objects. |
| [`extract_obj_name()`](#extract_obj_name) | Generates a shortened name, without the module information. |
| [`flyte_entity_call_handler()`](#flyte_entity_call_handler) | This function is the call handler for tasks, workflows, and launch plans (which redirects to the underlying. |
| [`get_args()`](#get_args) | Get type arguments with all substitutions performed. |
| [`get_origin()`](#get_origin) | Get the unsubscripted version of a type. |
| [`get_primitive_val()`](#get_primitive_val) |  |
| [`resolve_attr_path_in_dict()`](#resolve_attr_path_in_dict) |  |
| [`resolve_attr_path_in_pb_struct()`](#resolve_attr_path_in_pb_struct) | Resolves the protobuf struct (e. |
| [`resolve_attr_path_in_promise()`](#resolve_attr_path_in_promise) | resolve_attr_path_in_promise resolves the attribute path in a promise and returns a new promise with the resolved value. |
| [`resolve_attr_path_recursively()`](#resolve_attr_path_recursively) | This function resolves the attribute path in a nested structure recursively. |
| [`run_sync()`](#run_sync) | This should be called from synchronous functions to run an async function. |
| [`to_binding()`](#to_binding) |  |
| [`translate_inputs_to_literals()`](#translate_inputs_to_literals) | The point of this function is to extract out Literals from a collection of either Python native values (which would. |
| [`translate_inputs_to_native()`](#translate_inputs_to_native) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |
| `loop_manager` | `_AsyncLoopManager` |  |

## Methods

#### _translate_inputs_to_literals()

```python
def _translate_inputs_to_literals(
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

#### _translate_inputs_to_native()

```python
def _translate_inputs_to_native(
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

#### create_and_link_node()

```python
def create_and_link_node(
    ctx: FlyteContext,
    entity: SupportsNodeCreation,
    overridden_interface: Optional[Interface],
    add_node_to_compilation_state: bool,
    node_id: str,
    kwargs,
) -> Optional[Union[Tuple[Promise], Promise, VoidPromise]]
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
) -> Optional[Union[Tuple[Promise], Promise, VoidPromise]]
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

#### deepcopy()

```python
def deepcopy(
    x,
    memo,
    _nil,
)
```
Deep copy operation on arbitrary Python objects.

See the module's __doc__ string for more info.


| Parameter | Type |
|-|-|
| `x` |  |
| `memo` |  |
| `_nil` |  |

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

#### get_args()

```python
def get_args(
    tp,
)
```
Get type arguments with all substitutions performed.

For unions, basic simplifications used by Union constructor are performed.

Examples::

>>> T = TypeVar('T')
>>> assert get_args(Dict[str, int]) == (str, int)
>>> assert get_args(int) == ()
>>> assert get_args(Union[int, Union[T, int], str][int]) == (int, str)
>>> assert get_args(Union[int, Tuple[T, int]][str]) == (int, Tuple[str, int])
>>> assert get_args(Callable[[], T][int]) == ([], int)


| Parameter | Type |
|-|-|
| `tp` |  |

#### get_origin()

```python
def get_origin(
    tp,
)
```
Get the unsubscripted version of a type.

This supports generic types, Callable, Tuple, Union, Literal, Final, ClassVar,
Annotated, and others. Return None for unsupported types.

Examples::

>>> P = ParamSpec('P')
>>> assert get_origin(Literal[42]) is Literal
>>> assert get_origin(int) is None
>>> assert get_origin(ClassVar[int]) is ClassVar
>>> assert get_origin(Generic) is Generic
>>> assert get_origin(Generic[T]) is Generic
>>> assert get_origin(Union[T, int]) is Union
>>> assert get_origin(List[Tuple[T, T]][int]) is list
>>> assert get_origin(P.args) is P


| Parameter | Type |
|-|-|
| `tp` |  |

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

#### run_sync()

```python
def run_sync(
    coro_func: typing.Callable[..., typing.Awaitable[~T]],
    args,
    kwargs,
) -> ~T
```
This should be called from synchronous functions to run an async function.


| Parameter | Type |
|-|-|
| `coro_func` | `typing.Callable[..., typing.Awaitable[~T]]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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

## flytekit.core.promise.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.promise.AsyncTypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
class AsyncTypeTransformer(
    name: str,
    t: Type[T],
    enable_type_assertions: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |
| `enable_type_assertions` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.promise.BaseAccelerator

Base class for all accelerator types. This class is not meant to be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.core.promise.Binary

```python
class Binary(
    value,
    tag,
)
```
| Parameter | Type |
|-|-|
| `value` |  |
| `tag` |  |

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
) -> Binary
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
| `tag` |  |  |
| `value` |  |  |

## flytekit.core.promise.BranchEvalMode

This is a 3-way class, with the None value meaning that we are not within a conditional context. The other two
values are
* Active - This means that the next ``then`` should run
* Skipped - The next ``then`` should not run


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

## flytekit.core.promise.ComparisonOps

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

## flytekit.core.promise.ConjunctionOps

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


## flytekit.core.promise.DictTransformer

Transformer that transforms an univariate dictionary Dict[str, T] to a Literal Map or
transforms an untyped dictionary to a Binary Scalar Literal with a Struct Literal Type.


```python
def DictTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`dict_to_binary_literal()`](#dict_to_binary_literal) | Converts a Python dictionary to a Flyte-specific ``Literal`` using MessagePack encoding. |
| [`dict_to_generic_literal()`](#dict_to_generic_literal) | This is deprecated from flytekit 1. |
| [`extract_types()`](#extract_types) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Transforms a native python dictionary to a flyte-specific ``LiteralType``. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`is_pickle()`](#is_pickle) |  |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[dict],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[dict]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[dict],
) -> dict
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[dict]` |

#### dict_to_binary_literal()

```python
def dict_to_binary_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
) -> Literal
```
Converts a Python dictionary to a Flyte-specific ``Literal`` using MessagePack encoding.
Falls back to Pickle if encoding fails and `allow_pickle` is True.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `v` | `dict` |
| `python_type` | `Type[dict]` |
| `allow_pickle` | `bool` |

#### dict_to_generic_literal()

```python
def dict_to_generic_literal(
    ctx: FlyteContext,
    v: dict,
    python_type: Type[dict],
    allow_pickle: bool,
) -> Literal
```
This is deprecated from flytekit 1.14.0.
Creates a flyte-specific ``Literal`` value from a native python dictionary.
Note: This is deprecated and will be removed in the future.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `v` | `dict` |
| `python_type` | `Type[dict]` |
| `allow_pickle` | `bool` |

#### extract_types()

```python
def extract_types(
    t: Optional[Type[dict]],
) -> typing.Tuple
```
| Parameter | Type |
|-|-|
| `t` | `Optional[Type[dict]]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[dict],
) -> LiteralType
```
Transforms a native python dictionary to a flyte-specific ``LiteralType``


| Parameter | Type |
|-|-|
| `t` | `Type[dict]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Union[Type[dict], typing.Dict[Type, Type]]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_pickle()

```python
def is_pickle(
    python_type: Type[dict],
) -> bool
```
| Parameter | Type |
|-|-|
| `python_type` | `Type[dict]` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.promise.Enum

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


## flytekit.core.promise.ExecutionParameters

This is a run-time user-centric context object that is accessible to every @task method. It can be accessed using

.. code-block:: python

flytekit.current_context()

This object provides the following
* a statsd handler
* a logging handler
* the execution ID as an :py:class:`flytekit.models.core.identifier.WorkflowExecutionIdentifier` object
* a working directory for the user to write arbitrary files to

Please do not confuse this object with the :py:class:`flytekit.FlyteContext` object.


```python
class ExecutionParameters(
    execution_date,
    tmp_dir,
    stats,
    execution_id: typing.Optional[_identifier.WorkflowExecutionIdentifier],
    logging,
    raw_output_prefix,
    output_metadata_prefix,
    checkpoint,
    decks,
    task_id: typing.Optional[_identifier.Identifier],
    enable_deck: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `execution_date` |  |
| `tmp_dir` |  |
| `stats` |  |
| `execution_id` | `typing.Optional[_identifier.WorkflowExecutionIdentifier]` |
| `logging` |  |
| `raw_output_prefix` |  |
| `output_metadata_prefix` |  |
| `checkpoint` |  |
| `decks` |  |
| `task_id` | `typing.Optional[_identifier.Identifier]` |
| `enable_deck` | `bool` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`builder()`](#builder) |  |
| [`get()`](#get) | Returns task specific context if present else raise an error. |
| [`has_attr()`](#has_attr) |  |
| [`new_builder()`](#new_builder) |  |
| [`with_enable_deck()`](#with_enable_deck) |  |
| [`with_task_sandbox()`](#with_task_sandbox) |  |


#### builder()

```python
def builder()
```
#### get()

```python
def get(
    key: str,
) -> typing.Any
```
Returns task specific context if present else raise an error. The returned context will match the key


| Parameter | Type |
|-|-|
| `key` | `str` |

#### has_attr()

```python
def has_attr(
    attr_name: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `attr_name` | `str` |

#### new_builder()

```python
def new_builder(
    current: Optional[ExecutionParameters],
) -> Builder
```
| Parameter | Type |
|-|-|
| `current` | `Optional[ExecutionParameters]` |

#### with_enable_deck()

```python
def with_enable_deck(
    enable_deck: bool,
) -> Builder
```
| Parameter | Type |
|-|-|
| `enable_deck` | `bool` |

#### with_task_sandbox()

```python
def with_task_sandbox()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `checkpoint` |  |  |
| `decks` |  | {{< multiline >}}A list of decks of the tasks, and it will be rendered to a html at the end of the task execution.
{{< /multiline >}} |
| `default_deck` |  |  |
| `enable_deck` |  | {{< multiline >}}Returns whether deck is enabled or not
{{< /multiline >}} |
| `execution_date` |  | {{< multiline >}}This is a datetime representing the time at which a workflow was started.  This is consistent across all tasks
executed in a workflow or sub-workflow.

.. note::

Do NOT use this execution_date to drive any production logic.  It might be useful as a tag for data to help
in debugging.
{{< /multiline >}} |
| `execution_id` |  | {{< multiline >}}This is the identifier of the workflow execution within the underlying engine.  It will be consistent across all
task executions in a workflow or sub-workflow execution.

.. note::

Do NOT use this execution_id to drive any production logic.  This execution ID should only be used as a tag
on output data to link back to the workflow run that created it.
{{< /multiline >}} |
| `logging` |  | {{< multiline >}}A handle to a useful logging object.
TODO: Usage examples
{{< /multiline >}} |
| `output_metadata_prefix` |  |  |
| `raw_output_prefix` |  |  |
| `secrets` |  |  |
| `stats` |  | {{< multiline >}}A handle to a special statsd object that provides usefully tagged stats.
TODO: Usage examples and better comments
{{< /multiline >}} |
| `task_id` |  | {{< multiline >}}At production run-time, this will be generated by reading environment variables that are set
by the backend.
{{< /multiline >}} |
| `timeline_deck` |  |  |
| `working_directory` |  | {{< multiline >}}A handle to a special working directory for easily producing temporary files.
TODO: Usage examples
{{< /multiline >}} |

## flytekit.core.promise.ExecutionState

This is the context that is active when executing a task or a local workflow. This carries the necessary state to
execute.
Some required things during execution deal with temporary directories, ExecutionParameters that are passed to the
user etc.

Attributes:
mode (ExecutionState.Mode): Defines the context in which the task is executed (local, hosted, etc).
working_dir (os.PathLike): Specifies the remote, external directory where inputs, outputs and other protobufs
are uploaded
engine_dir (os.PathLike):
branch_eval_mode Optional[BranchEvalMode]: Used to determine whether a branch node should execute.
user_space_params Optional[ExecutionParameters]: Provides run-time, user-centric context such as a statsd
handler, a logging handler, the current execution id and a working directory.


```python
class ExecutionState(
    working_dir: Union[os.PathLike, str],
    mode: Optional[ExecutionState.Mode],
    engine_dir: Optional[Union[os.PathLike, str]],
    branch_eval_mode: Optional[BranchEvalMode],
    user_space_params: Optional[ExecutionParameters],
)
```
| Parameter | Type |
|-|-|
| `working_dir` | `Union[os.PathLike, str]` |
| `mode` | `Optional[ExecutionState.Mode]` |
| `engine_dir` | `Optional[Union[os.PathLike, str]]` |
| `branch_eval_mode` | `Optional[BranchEvalMode]` |
| `user_space_params` | `Optional[ExecutionParameters]` |

### Methods

| Method | Description |
|-|-|
| [`branch_complete()`](#branch_complete) | Indicates that we are within a conditional / ifelse block and the active branch is not done. |
| [`is_local_execution()`](#is_local_execution) |  |
| [`take_branch()`](#take_branch) | Indicates that we are within an if-else block and the current branch has evaluated to true. |
| [`with_params()`](#with_params) | Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values. |


#### branch_complete()

```python
def branch_complete()
```
Indicates that we are within a conditional / ifelse block and the active branch is not done.
Default to SKIPPED


#### is_local_execution()

```python
def is_local_execution()
```
#### take_branch()

```python
def take_branch()
```
Indicates that we are within an if-else block and the current branch has evaluated to true.
Useful only in local execution mode


#### with_params()

```python
def with_params(
    working_dir: Optional[os.PathLike],
    mode: Optional[Mode],
    engine_dir: Optional[os.PathLike],
    branch_eval_mode: Optional[BranchEvalMode],
    user_space_params: Optional[ExecutionParameters],
) -> ExecutionState
```
Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values.


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |
| `mode` | `Optional[Mode]` |
| `engine_dir` | `Optional[os.PathLike]` |
| `branch_eval_mode` | `Optional[BranchEvalMode]` |
| `user_space_params` | `Optional[ExecutionParameters]` |

## flytekit.core.promise.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

## flytekit.core.promise.FlyteContextManager

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

## flytekit.core.promise.FlytePromiseAttributeResolveException

Assertion failed.


```python
class FlytePromiseAttributeResolveException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

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

## flytekit.core.promise.Interface

A Python native interface object, like inspect.signature but simpler.


```python
class Interface(
    inputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]],
    outputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]],
    output_tuple_name: Optional[str],
    docstring: Optional[Docstring],
)
```
| Parameter | Type |
|-|-|
| `inputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]]` |
| `outputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]]` |
| `output_tuple_name` | `Optional[str]` |
| `docstring` | `Optional[Docstring]` |

### Methods

| Method | Description |
|-|-|
| [`remove_inputs()`](#remove_inputs) | This method is useful in removing some variables from the Flyte backend inputs specification, as these are. |
| [`with_inputs()`](#with_inputs) | Use this to add additional inputs to the interface. |
| [`with_outputs()`](#with_outputs) | This method allows addition of extra outputs are expected from a task specification. |


#### remove_inputs()

```python
def remove_inputs(
    vars: Optional[List[str]],
) -> Interface
```
This method is useful in removing some variables from the Flyte backend inputs specification, as these are
implicit local only inputs or will be supplied by the library at runtime. For example, spark-session etc
It creates a new instance of interface with the requested variables removed


| Parameter | Type |
|-|-|
| `vars` | `Optional[List[str]]` |

#### with_inputs()

```python
def with_inputs(
    extra_inputs: Dict[str, Type],
) -> Interface
```
Use this to add additional inputs to the interface. This is useful for adding additional implicit inputs that
are added without the user requesting for them


| Parameter | Type |
|-|-|
| `extra_inputs` | `Dict[str, Type]` |

#### with_outputs()

```python
def with_outputs(
    extra_outputs: Dict[str, Type],
) -> Interface
```
This method allows addition of extra outputs are expected from a task specification


| Parameter | Type |
|-|-|
| `extra_outputs` | `Dict[str, Type]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_inputs_as_kwargs` |  |  |
| `docstring` |  |  |
| `inputs` |  |  |
| `inputs_with_defaults` |  |  |
| `output_names` |  |  |
| `output_tuple` |  |  |
| `output_tuple_name` |  |  |
| `outputs` |  |  |

## flytekit.core.promise.Iterable

## flytekit.core.promise.ListTransformer

Transformer that handles a univariate typing.List[T]


```python
def ListTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Only univariate Lists are supported in Flyte. |
| [`get_sub_type()`](#get_sub_type) | Return the generic Type T of the List. |
| [`get_sub_type_or_none()`](#get_sub_type_or_none) | Return the generic Type T of the List, or None if the generic type cannot be inferred. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> typing.Optional[typing.List[T]]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> Optional[LiteralType]
```
Only univariate Lists are supported in Flyte


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type()

```python
def get_sub_type(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the List


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_or_none()

```python
def get_sub_type_or_none(
    t: Type[T],
) -> Optional[Type[T]]
```
Return the generic Type T of the List, or None if the generic type cannot be inferred


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> list
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.promise.Literal

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
## flytekit.core.promise.Node

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

## flytekit.core.promise.OutputMetadataTracker

This class is for the users to set arbitrary metadata on output literals.

Attributes:
output_metadata Optional[TaskOutputMetadata]: is a sparse dictionary of metadata that the user wants to attach
to each output of a task. The key is the output value (object) and the value is an OutputMetadata object.


```python
class OutputMetadataTracker(
    output_metadata: typing.Dict[typing.Any, OutputMetadata],
)
```
| Parameter | Type |
|-|-|
| `output_metadata` | `typing.Dict[typing.Any, OutputMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`get()`](#get) |  |
| [`with_params()`](#with_params) | Produces a copy of the current object and set new things. |


#### add()

```python
def add(
    obj: typing.Any,
    metadata: OutputMetadata,
)
```
| Parameter | Type |
|-|-|
| `obj` | `typing.Any` |
| `metadata` | `OutputMetadata` |

#### get()

```python
def get(
    obj: typing.Any,
) -> Optional[OutputMetadata]
```
| Parameter | Type |
|-|-|
| `obj` | `typing.Any` |

#### with_params()

```python
def with_params(
    output_metadata: Optional[TaskOutputMetadata],
) -> OutputMetadataTracker
```
Produces a copy of the current object and set new things


| Parameter | Type |
|-|-|
| `output_metadata` | `Optional[TaskOutputMetadata]` |

## flytekit.core.promise.Primitive

```python
class Primitive(
    integer: typing.Optional[int],
    float_value: typing.Optional[float],
    string_value: typing.Optional[str],
    boolean: typing.Optional[bool],
    datetime: typing.Optional[datetime.datetime],
    duration: typing.Optional[datetime.timedelta],
)
```
This object proxies the primitives supported by the Flyte IDL system.  Only one value can be set.


| Parameter | Type |
|-|-|
| `integer` | `typing.Optional[int]` |
| `float_value` | `typing.Optional[float]` |
| `string_value` | `typing.Optional[str]` |
| `boolean` | `typing.Optional[bool]` |
| `datetime` | `typing.Optional[datetime.datetime]` |
| `duration` | `typing.Optional[datetime.timedelta]` |

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
    proto,
) -> Primitive
```
| Parameter | Type |
|-|-|
| `proto` |  |

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
| `boolean` |  |  |
| `datetime` |  |  |
| `duration` |  |  |
| `float_value` |  |  |
| `integer` |  |  |
| `is_empty` |  |  |
| `string_value` |  |  |
| `value` |  | {{< multiline >}}This returns whichever field is set.
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

## flytekit.core.promise.Protocol

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


## flytekit.core.promise.Resources

```python
class Resources(
    requests,
    limits,
)
```
| Parameter | Type |
|-|-|
| `requests` |  |
| `limits` |  |

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
) -> Resources
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
| `limits` |  | {{< multiline >}}These are the limits required.  These are guaranteed to be satisfied.
{{< /multiline >}} |
| `requests` |  | {{< multiline >}}The desired resources for execution.  This is given on a best effort basis.
{{< /multiline >}} |

## flytekit.core.promise.Scalar

```python
class Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
)
```
Scalar wrapper around Flyte types.  Only one can be specified.



| Parameter | Type |
|-|-|
| `primitive` | `typing.Optional[flytekit.models.literals.Primitive]` |
| `blob` | `typing.Optional[flytekit.models.literals.Blob]` |
| `binary` | `typing.Optional[flytekit.models.literals.Binary]` |
| `schema` | `typing.Optional[flytekit.models.literals.Schema]` |
| `union` | `typing.Optional[flytekit.models.literals.Union]` |
| `none_type` | `typing.Optional[flytekit.models.literals.Void]` |
| `error` | `typing.Optional[flytekit.models.types.Error]` |
| `generic` | `typing.Optional[google.protobuf.struct_pb2.Struct]` |
| `structured_dataset` | `typing.Optional[flytekit.models.literals.StructuredDataset]` |

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
) -> flytekit.models.literals.Scalar
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
| `binary` |  |  |
| `blob` |  |  |
| `error` |  |  |
| `generic` |  |  |
| `is_empty` |  |  |
| `none_type` |  |  |
| `primitive` |  |  |
| `schema` |  |  |
| `structured_dataset` |  |  |
| `union` |  |  |
| `value` |  | {{< multiline >}}Returns whichever value is set
{{< /multiline >}} |

## flytekit.core.promise.SimpleType

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

## flytekit.core.promise.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value. |
| [`async_to_python_value()`](#async_to_python_value) |  |
| [`calculate_hash()`](#calculate_hash) |  |
| [`dict_to_literal_map()`](#dict_to_literal_map) |  |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) |  |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available. |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer. |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value. |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values. |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed. |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) |  |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals. |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type(. |
| [`register_additional_type()`](#register_additional_type) |  |
| [`register_restricted_type()`](#register_restricted_type) |  |
| [`to_html()`](#to_html) |  |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous. |
| [`to_literal_checks()`](#to_literal_checks) |  |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType``. |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value. |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) |  |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### calculate_hash()

```python
def calculate_hash(
    python_val: typing.Any,
    python_type: Type[T],
) -> Optional[str]
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |

#### dict_to_literal_map()

```python
def dict_to_literal_map(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> LiteralMap
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### dict_to_literal_map_pb()

```python
def dict_to_literal_map_pb(
    ctx: FlyteContext,
    d: typing.Dict[str, typing.Any],
    type_hints: Optional[typing.Dict[str, type]],
) -> Optional[literals_pb2.LiteralMap]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `d` | `typing.Dict[str, typing.Any]` |
| `type_hints` | `Optional[typing.Dict[str, type]]` |

#### get_available_transformers()

```python
def get_available_transformers()
```
Returns all python types for which transformers are available


#### get_transformer()

```python
def get_transformer(
    python_type: Type,
) -> TypeTransformer[T]
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
) -> Type[T]
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
) -> typing.Dict[str, type]
```
Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values.


| Parameter | Type |
|-|-|
| `flyte_variable_dict` | `typing.Dict[str, _interface_models.Variable]` |

#### lazy_import_transformers()

```python
def lazy_import_transformers()
```
Only load the transformers if needed.


#### literal_map_to_kwargs()

```python
def literal_map_to_kwargs(
    ctx: FlyteContext,
    lm: LiteralMap,
    python_types: typing.Optional[typing.Dict[str, type]],
    literal_types: typing.Optional[typing.Dict[str, _interface_models.Variable]],
) -> typing.Dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lm` | `LiteralMap` |
| `python_types` | `typing.Optional[typing.Dict[str, type]]` |
| `literal_types` | `typing.Optional[typing.Dict[str, _interface_models.Variable]]` |

#### named_tuple_to_variable_map()

```python
def named_tuple_to_variable_map(
    t: typing.NamedTuple,
) -> _interface_models.VariableMap
```
Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals.


| Parameter | Type |
|-|-|
| `t` | `typing.NamedTuple` |

#### register()

```python
def register(
    transformer: TypeTransformer,
    additional_types: Optional[typing.List[Type]],
)
```
This should be used for all types that respond with the right type annotation when you use type(...) function


| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer` |
| `additional_types` | `Optional[typing.List[Type]]` |

#### register_additional_type()

```python
def register_additional_type(
    transformer: TypeTransformer[T],
    additional_type: Type[T],
    override,
)
```
| Parameter | Type |
|-|-|
| `transformer` | `TypeTransformer[T]` |
| `additional_type` | `Type[T]` |
| `override` |  |

#### register_restricted_type()

```python
def register_restricted_type(
    name: str,
    type: Type[T],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `type` | `Type[T]` |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[typing.Any],
) -> str
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[typing.Any]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
The current dance is because we are allowing users to call from an async function, this synchronous
to_literal function, and allowing this to_literal function, to then invoke yet another async function,
namely an async transformer.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_checks()

```python
def to_literal_checks(
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
)
```
| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_literal_type()

```python
def to_literal_type(
    python_type: Type[T],
) -> LiteralType
```
Converts a python type into a flyte specific ``LiteralType``


| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type,
) -> typing.Any
```
Converts a Literal value with an expected python type into a python value.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type` |

#### unwrap_offloaded_literal()

```python
def unwrap_offloaded_literal(
    ctx: FlyteContext,
    lv: Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |

## flytekit.core.promise.TypeTransformer

Base transformer type that should be implemented for every python native type that can be handled by flytekit


```python
class TypeTransformer(
    name: str,
    t: Type[T],
    enable_type_assertions: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `t` | `Type[T]` |
| `enable_type_assertions` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> LiteralType
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[T]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.core.promise.TypeTransformerFailedError

Inappropriate argument type.


## flytekit.core.promise.UnionTransformer

Transformer that handles a typing.Union[T1, T2, ...]


```python
def UnionTransformer()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | Converts the given Literal to a Python Type. |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access. |
| [`from_generic_idl()`](#from_generic_idl) | TODO: Support all Flyte Types. |
| [`get_literal_type()`](#get_literal_type) | Converts the python type to a Flyte LiteralType. |
| [`get_sub_type_in_optional()`](#get_sub_type_in_optional) | Return the generic Type T of the Optional type. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`is_optional_type()`](#is_optional_type) |  |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[T],
    v: T,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[T]` |
| `v` | `T` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: T,
    python_type: Type[T],
    expected: LiteralType,
) -> typing.Union[Literal, asyncio.Future]
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[typing.Any]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and attribute access.｀

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
python val -> msgpack bytes -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
python val -> msgpack bytes -> binary literal scalar -> resolved golang value -> binary literal scalar -> msgpack bytes -> python val
(to_literal)                            (propeller attribute access)                       (from_binary_idl)


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T]` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T],
) -> Optional[T]
```
TODO: Support all Flyte Types.
This is for dataclass attribute access from input created from the Flyte Console.

Note:
- This can be removed in the future when the Flyte Console support generate Binary IDL Scalar as input.


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T]` |

#### get_literal_type()

```python
def get_literal_type(
    t: Type[T],
) -> Optional[LiteralType]
```
Converts the python type to a Flyte LiteralType


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### get_sub_type_in_optional()

```python
def get_sub_type_in_optional(
    t: Type[T],
) -> Type[T]
```
Return the generic Type T of the Optional type


| Parameter | Type |
|-|-|
| `t` | `Type[T]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> type
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### is_optional_type()

```python
def is_optional_type(
    t: Type,
) -> bool
```
| Parameter | Type |
|-|-|
| `t` | `Type` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: T,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `T` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

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

