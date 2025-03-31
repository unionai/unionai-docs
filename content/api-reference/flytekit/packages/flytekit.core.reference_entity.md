---
title: flytekit.core.reference_entity
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.reference_entity

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.core.reference_entity#flytekitcorereference_entityabc) | Helper class that provides a standard way to create an ABC using. |
| [`Any`](.././flytekit.core.reference_entity#flytekitcorereference_entityany) | Special type indicating an unconstrained type. |
| [`BranchEvalMode`](.././flytekit.core.reference_entity#flytekitcorereference_entitybranchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`ExecutionState`](.././flytekit.core.reference_entity#flytekitcorereference_entityexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.reference_entity#flytekitcorereference_entityflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`Interface`](.././flytekit.core.reference_entity#flytekitcorereference_entityinterface) | A Python native interface object, like inspect. |
| [`LaunchPlanReference`](.././flytekit.core.reference_entity#flytekitcorereference_entitylaunchplanreference) | A reference object containing metadata that points to a remote launch plan. |
| [`Promise`](.././flytekit.core.reference_entity#flytekitcorereference_entitypromise) | This object is a wrapper and exists for three main reasons. |
| [`Reference`](.././flytekit.core.reference_entity#flytekitcorereference_entityreference) |  |
| [`ReferenceEntity`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferenceentity) |  |
| [`ReferenceSpec`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferencespec) |  |
| [`ReferenceTemplate`](.././flytekit.core.reference_entity#flytekitcorereference_entityreferencetemplate) |  |
| [`TaskReference`](.././flytekit.core.reference_entity#flytekitcorereference_entitytaskreference) | A reference object containing metadata that points to a remote task. |
| [`TypeEngine`](.././flytekit.core.reference_entity#flytekitcorereference_entitytypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`VoidPromise`](.././flytekit.core.reference_entity#flytekitcorereference_entityvoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |
| [`WorkflowReference`](.././flytekit.core.reference_entity#flytekitcorereference_entityworkflowreference) | A reference object containing metadata that points to a remote workflow. |

### Methods

| Method | Description |
|-|-|
| [`abstractmethod()`](#abstractmethod) | A decorator indicating abstract methods. |
| [`create_and_link_node()`](#create_and_link_node) | This method is used to generate a node with bindings within a flytekit workflow. |
| [`create_task_output()`](#create_task_output) |  |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`extract_obj_name()`](#extract_obj_name) | Generates a shortened name, without the module information. |
| [`transform_interface_to_typed_interface()`](#transform_interface_to_typed_interface) | Transform the given simple python native interface to FlyteIDL's interface. |
| [`translate_inputs_to_literals()`](#translate_inputs_to_literals) | The point of this function is to extract out Literals from a collection of either Python native values (which would. |


### Variables

| Property | Type | Description |
|-|-|-|
| `logger` | `Logger` |  |

## Methods

#### abstractmethod()

```python
def abstractmethod(
    funcobj,
)
```
A decorator indicating abstract methods.

Requires that the metaclass is ABCMeta or derived from it.  A
class that has a metaclass derived from ABCMeta cannot be
instantiated unless all of its abstract methods are overridden.
The abstract methods can be called using any of the normal
'super' call mechanisms.  abstractmethod() may be used to declare
abstract methods for properties and descriptors.

Usage:

class C(metaclass=ABCMeta):
@abstractmethod
def my_abstract_method(self, arg1, arg2, argN):
...


| Parameter | Type |
|-|-|
| `funcobj` |  |

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

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

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

#### transform_interface_to_typed_interface()

```python
def transform_interface_to_typed_interface(
    interface: typing.Optional[Interface],
    allow_partial_artifact_id_binding: bool,
) -> typing.Optional[_interface_models.TypedInterface]
```
Transform the given simple python native interface to FlyteIDL's interface


| Parameter | Type |
|-|-|
| `interface` | `typing.Optional[Interface]` |
| `allow_partial_artifact_id_binding` | `bool` |

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

## flytekit.core.reference_entity.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.core.reference_entity.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.reference_entity.BranchEvalMode

This is a 3-way class, with the None value meaning that we are not within a conditional context. The other two
values are
* Active - This means that the next ``then`` should run
* Skipped - The next ``then`` should not run


## flytekit.core.reference_entity.ExecutionState

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

## flytekit.core.reference_entity.FlyteContext

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

## flytekit.core.reference_entity.Interface

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

## flytekit.core.reference_entity.LaunchPlanReference

A reference object containing metadata that points to a remote launch plan.


```python
class LaunchPlanReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.Promise

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

## flytekit.core.reference_entity.Reference

```python
class Reference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.ReferenceEntity

```python
class ReferenceEntity(
    reference: typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference],
    inputs: typing.Dict[str, typing.Type],
    outputs: typing.Dict[str, typing.Type],
)
```
| Parameter | Type |
|-|-|
| `reference` | `typing.Union[flytekit.core.reference_entity.WorkflowReference, flytekit.core.reference_entity.TaskReference, flytekit.core.reference_entity.LaunchPlanReference]` |
| `inputs` | `typing.Dict[str, typing.Type]` |
| `outputs` | `typing.Dict[str, typing.Type]` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |

## flytekit.core.reference_entity.ReferenceSpec

```python
class ReferenceSpec(
    template: flytekit.core.reference_entity.ReferenceTemplate,
)
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.core.reference_entity.ReferenceTemplate` |

### Properties

| Property | Type | Description |
|-|-|-|
| `template` |  |  |

## flytekit.core.reference_entity.ReferenceTemplate

```python
class ReferenceTemplate(
    id: flytekit.models.core.identifier.Identifier,
    resource_type: int,
)
```
A reference template encapsulates all the information necessary to use reference entities within other
workflows or dynamic tasks.



| Parameter | Type |
|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` |
| `resource_type` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  | {{< multiline >}}User-specified information that uniquely identifies this reference.
{{< /multiline >}} |
| `resource_type` |  | {{< multiline >}}The type of reference.
{{< /multiline >}} |

## flytekit.core.reference_entity.TaskReference

A reference object containing metadata that points to a remote task.


```python
class TaskReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.core.reference_entity.TypeEngine

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

## flytekit.core.reference_entity.VoidPromise

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

## flytekit.core.reference_entity.WorkflowReference

A reference object containing metadata that points to a remote workflow.


```python
class WorkflowReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

