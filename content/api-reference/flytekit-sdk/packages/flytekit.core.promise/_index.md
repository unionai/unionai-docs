---
title: flytekit.core.promise
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.promise

## Directory

### Classes

| Class | Description |
|-|-|
| [`ComparisonExpression`](../flytekit.core.promise/comparisonexpression) | ComparisonExpression refers to an expression of the form (lhs operator rhs), where lhs and rhs are operands. |
| [`ComparisonOps`](../flytekit.core.promise/comparisonops) |  |
| [`ConjunctionExpression`](../flytekit.core.promise/conjunctionexpression) | A Conjunction Expression is an expression of the form either (A and B) or (A or B). |
| [`ConjunctionOps`](../flytekit.core.promise/conjunctionops) |  |
| [`NodeOutput`](../flytekit.core.promise/nodeoutput) |  |
| [`Promise`](../flytekit.core.promise/promise) | This object is a wrapper and exists for three main reasons. |
| [`VoidPromise`](../flytekit.core.promise/voidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |

### Protocols

| Protocol | Description |
|-|-|
| [`HasFlyteInterface`](../flytekit.core.promise/hasflyteinterface) |  |
| [`LocallyExecutable`](../flytekit.core.promise/locallyexecutable) |  |
| [`SupportsNodeCreation`](../flytekit.core.promise/supportsnodecreation) |  |

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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `SupportsNodeCreation` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

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
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `_flyte_context.FlyteContext` | |
| `expected_literal_type` | `_type_models.LiteralType` | |
| `t_value` | `Any` | |
| `t_value_type` | `typing.Type[T]` | |
| `nodes` | `List[Node]` | |

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
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `_flyte_context.FlyteContext` | |
| `var_name` | `str` | |
| `expected_literal_type` | `_type_models.LiteralType` | |
| `t_value` | `Any` | |
| `t_value_type` | `type` | |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `entity` | `SupportsNodeCreation` | RemoteEntity |
| `overridden_interface` | `Optional[Interface]` | utilize this interface instead of the one provided by the entity. This is useful for ArrayNode as there's a mismatch between the underlying interface and inputs |
| `add_node_to_compilation_state` | `bool` | bool that enables for nodes to be created but not linked to the workflow. This is useful when creating nodes nested under other nodes such as ArrayNode |
| `node_id` | `str` | str if provided, this will be used as the node id. |
| `kwargs` | `**kwargs` | Dict[str, Any] default inputs passed from the user to this entity. Can be promises. :return:  Optional[Union[Tuple[Promise], Promise, VoidPromise]] |

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



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `entity` | `HasFlyteInterface` | RemoteEntity |
| `overridden_interface` | `Optional[_interface_models.TypedInterface]` | utilize this interface instead of the one provided by the entity. This is useful for ArrayNode as there's a mismatch between the underlying interface and inputs |
| `add_node_to_compilation_state` | `bool` | bool that enables for nodes to be created but not linked to the workflow. This is useful when creating nodes nested under other nodes such as ArrayNode |
| `node_id` | `str` | str if provided, this will be used as the node id. |
| `_inputs_not_allowed` | `Optional[Set[str]]` | Set of all variable names that should not be provided when using this entity. Useful for Launchplans with `fixed` inputs |
| `_ignorable_inputs` | `Optional[Set[str]]` | Set of all variable names that are optional, but if provided will be overridden. Useful for launchplans with `default` inputs |
| `kwargs` | `**kwargs` | Dict[str, Any] default inputs passed from the user to this entity. Can be promises. :return:  Optional[Union[Tuple[Promise], Promise, VoidPromise]] |

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


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `promises` | `Union[Tuple[Promise], Promise, VoidPromise, None]` | |
| `entity_interface` | `Interface` | |

#### create_task_output()

```python
def create_task_output(
    promises: Optional[Union[List[Promise], Promise]],
    entity_interface: Optional[Interface],
) -> Optional[Union[Tuple[Promise], Promise]]
```
| Parameter | Type | Description |
|-|-|-|
| `promises` | `Optional[Union[List[Promise], Promise]]` | |
| `entity_interface` | `Optional[Interface]` | |

#### extract_obj_name()

```python
def extract_obj_name(
    name: str,
) -> str
```
Generates a shortened name, without the module information. Useful for node-names etc. Only extracts the final
object information often separated by `.` in the python fully qualified notation


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `SupportsNodeCreation` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### get_primitive_val()

```python
def get_primitive_val(
    prim: Primitive,
) -> Any
```
| Parameter | Type | Description |
|-|-|-|
| `prim` | `Primitive` | |

#### resolve_attr_path_in_dict()

```python
def resolve_attr_path_in_dict(
    d: dict,
    attr_path: List[Union[str, int]],
) -> Any
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `dict` | |
| `attr_path` | `List[Union[str, int]]` | |

#### resolve_attr_path_in_pb_struct()

```python
def resolve_attr_path_in_pb_struct(
    st: _struct.Struct,
    attr_path: List[Union[str, int]],
) -> Union[_struct.Struct, _struct.ListValue]
```
Resolves the protobuf struct (e.g. dataclass) with attribute path.

Note that the return type can be google.protobuf.struct_pb2.Struct or google.protobuf.struct_pb2.ListValue.


| Parameter | Type | Description |
|-|-|-|
| `st` | `_struct.Struct` | |
| `attr_path` | `List[Union[str, int]]` | |

#### resolve_attr_path_in_promise()

```python
def resolve_attr_path_in_promise(
    p: Promise,
) -> Promise
```
resolve_attr_path_in_promise resolves the attribute path in a promise and returns a new promise with the resolved value
This is for local execution only. The remote execution will be resolved in flytepropeller.


| Parameter | Type | Description |
|-|-|-|
| `p` | `Promise` | |

#### resolve_attr_path_recursively()

```python
def resolve_attr_path_recursively(
    v: Any,
) -> Any
```
This function resolves the attribute path in a nested structure recursively.


| Parameter | Type | Description |
|-|-|-|
| `v` | `Any` | |

#### to_binding()

```python
def to_binding(
    p: Promise,
) -> _literals_models.Binding
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `Promise` | |

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

    def my_wf(in1: int) -&gt; int:
        a = task_1(in1=in1)
        b = task_2(in1=5, in2=a)
        return b

If this is the case, when task_2 is called in local workflow execution, we'll need to translate the Python native
literal 5 to a Flyte literal.

More interesting is this:

    def my_wf(in1: int, in2: int) -&gt; int:
        a = task_1(in1=in1)
        b = task_2(in1=5, in2=[a, in2])
        return b

Here, in task_2, during execution we'd have a list of Promises. We have to make sure to give task2 a Flyte
LiteralCollection (Flyte's name for list), not a Python list of Flyte literals.

This helper function is used both when sorting out inputs to a task, as well as outputs of a function.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | Context needed in case a non-primitive literal needs to be translated to a Flyte literal (like a file) |
| `incoming_values` | `Dict[str, Any]` | This is a map of your task's input or wf's output kwargs basically |
| `flyte_interface_types` | `Dict[str, _interface_models.Variable]` | One side of an {{&lt; py_class_ref flytekit.models.interface.TypedInterface &gt;}} basically. |
| `native_types` | `Dict[str, type]` | Map to native Python type. |

#### translate_inputs_to_native()

```python
def translate_inputs_to_native(
    ctx: FlyteContext,
    incoming_values: Dict[str, Any],
    flyte_interface_types: Dict[str, _interface_models.Variable],
) -> Dict[str, _literals_models.Literal]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `incoming_values` | `Dict[str, Any]` | |
| `flyte_interface_types` | `Dict[str, _interface_models.Variable]` | |

