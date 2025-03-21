---
title: flytekit.core.gate
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.gate

## Directory

### Classes

| Class | Description |
|-|-|
| [`ExecutionState`](.././flytekit.core.gate#flytekitcoregateexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.gate#flytekitcoregateflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.core.gate#flytekitcoregateflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Gate`](.././flytekit.core.gate#flytekitcoregategate) | A node type that waits for user input before proceeding with a workflow. |
| [`LiteralType`](.././flytekit.core.gate#flytekitcoregateliteraltype) | None. |
| [`Promise`](.././flytekit.core.gate#flytekitcoregatepromise) | This object is a wrapper and exists for three main reasons. |
| [`Scalar`](.././flytekit.core.gate#flytekitcoregatescalar) | None. |
| [`TypeEngine`](.././flytekit.core.gate#flytekitcoregatetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`VoidPromise`](.././flytekit.core.gate#flytekitcoregatevoidpromise) | This object is returned for tasks that do not return any outputs (declared interface is empty). |

### Errors

* [`FlyteDisapprovalException`](.././flytekit.core.gate#flytekitcoregateflytedisapprovalexception)

## flytekit.core.gate.ExecutionState

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
def ExecutionState(
    working_dir: Union[os.PathLike, str],
    mode: Optional[ExecutionState.Mode],
    engine_dir: Optional[Union[os.PathLike, str]],
    branch_eval_mode: Optional[BranchEvalMode],
    user_space_params: Optional[ExecutionParameters],
):
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
| [`branch_complete()`](#branch_complete) | Indicates that we are within a conditional / ifelse block and the active branch is not done |
| [`is_local_execution()`](#is_local_execution) | None |
| [`take_branch()`](#take_branch) | Indicates that we are within an if-else block and the current branch has evaluated to true |
| [`with_params()`](#with_params) | Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values |


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
):
```
Produces a copy of the current execution state and overrides the copy's parameters with passed parameter values.


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |
| `mode` | `Optional[Mode]` |
| `engine_dir` | `Optional[os.PathLike]` |
| `branch_eval_mode` | `Optional[BranchEvalMode]` |
| `user_space_params` | `Optional[ExecutionParameters]` |

## flytekit.core.gate.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
def FlyteContext(
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
):
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
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility |
| [`enter_conditional_section()`](#enter_conditional_section) | None |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) | None |
| [`new_builder()`](#new_builder) | None |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state |
| [`set_stackframe()`](#set_stackframe) | None |
| [`with_client()`](#with_client) | None |
| [`with_compilation_state()`](#with_compilation_state) | None |
| [`with_execution_state()`](#with_execution_state) | None |
| [`with_file_access()`](#with_file_access) | None |
| [`with_new_compilation_state()`](#with_new_compilation_state) | None |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) | None |
| [`with_serialization_settings()`](#with_serialization_settings) | None |
| [`with_worker_queue()`](#with_worker_queue) | None |


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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
):
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
):
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
):
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
):
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
):
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
):
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| user_space_params |  |  |

## flytekit.core.gate.FlyteContextManager

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
| [`add_signal_handler()`](#add_signal_handler) | None |
| [`current_context()`](#current_context) | None |
| [`get_origin_stackframe()`](#get_origin_stackframe) | None |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context |
| [`pop_context()`](#pop_context) | None |
| [`push_context()`](#push_context) | None |
| [`size()`](#size) | None |
| [`with_context()`](#with_context) | None |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.core.gate.FlyteDisapprovalException

Assertion failed.


```python
def FlyteDisapprovalException(
    args,
    timestamp: typing.Optional[float],
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.core.gate.Gate

A node type that waits for user input before proceeding with a workflow.
A gate is a type of node that behaves like a task, but instead of running code, it either needs to wait
for user input to proceed or wait for a timer to complete running.


```python
def Gate(
    name: str,
    input_type: typing.Optional[typing.Type],
    upstream_item: typing.Optional[typing.Any],
    sleep_duration: typing.Optional[datetime.timedelta],
    timeout: typing.Optional[datetime.timedelta],
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `input_type` | `typing.Optional[typing.Type]` |
| `upstream_item` | `typing.Optional[typing.Any]` |
| `sleep_duration` | `typing.Optional[datetime.timedelta]` |
| `timeout` | `typing.Optional[datetime.timedelta]` |

### Methods

| Method | Description |
|-|-|
| [`construct_node_metadata()`](#construct_node_metadata) | None |
| [`local_execute()`](#local_execute) | None |
| [`local_execution_mode()`](#local_execution_mode) | None |


#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| input_type |  |  |
| literal_type |  |  |
| name |  |  |
| python_interface |  |  |
| sleep_duration |  |  |

## flytekit.core.gate.LiteralType

```python
def LiteralType(
    simple,
    schema,
    collection_type,
    map_value_type,
    blob,
    enum_type,
    union_type,
    structured_dataset_type,
    metadata,
    structure,
    annotation,
):
```
This is a oneof message, only one of the kwargs may be set, representing one of the Flyte types.



| Parameter | Type |
|-|-|
| `simple` |  |
| `schema` |  |
| `collection_type` |  |
| `map_value_type` |  |
| `blob` |  |
| `enum_type` |  |
| `union_type` |  |
| `structured_dataset_type` |  |
| `metadata` |  |
| `structure` |  |
| `annotation` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
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
| annotation |  |  |
| blob |  |  |
| collection_type |  |  |
| enum_type |  |  |
| is_empty |  |  |
| map_value_type |  |  |
| metadata |  |  |
| schema |  |  |
| simple |  |  |
| structure |  |  |
| structured_dataset_type |  |  |
| union_type |  |  |

## flytekit.core.gate.Promise

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
def Promise(
    var: str,
    val: Union[NodeOutput, _literals_models.Literal],
    type: typing.Optional[_type_models.LiteralType],
):
```
| Parameter | Type |
|-|-|
| `var` | `str` |
| `val` | `Union[NodeOutput, _literals_models.Literal]` |
| `type` | `typing.Optional[_type_models.LiteralType]` |

### Methods

| Method | Description |
|-|-|
| [`deepcopy()`](#deepcopy) | None |
| [`eval()`](#eval) | None |
| [`is_()`](#is_) | None |
| [`is_false()`](#is_false) | None |
| [`is_none()`](#is_none) | None |
| [`is_true()`](#is_true) | None |
| [`with_overrides()`](#with_overrides) | None |
| [`with_var()`](#with_var) | None |


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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `new_var` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| attr_path |  |  |
| is_ready |  |  |
| ref |  |  |
| val |  |  |
| var |  |  |

## flytekit.core.gate.Scalar

```python
def Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| binary |  |  |
| blob |  |  |
| error |  |  |
| generic |  |  |
| is_empty |  |  |
| none_type |  |  |
| primitive |  |  |
| schema |  |  |
| structured_dataset |  |  |
| union |  |  |
| value |  |  |

## flytekit.core.gate.TypeEngine

Core Extensible TypeEngine of Flytekit. This should be used to extend the capabilities of FlyteKits type system.
Users can implement their own TypeTransformers and register them with the TypeEngine. This will allow special handling
of user objects


### Methods

| Method | Description |
|-|-|
| [`async_to_literal()`](#async_to_literal) | Converts a python value of a given type and expected ``LiteralType`` into a resolved ``Literal`` value |
| [`async_to_python_value()`](#async_to_python_value) | None |
| [`calculate_hash()`](#calculate_hash) | None |
| [`dict_to_literal_map()`](#dict_to_literal_map) | None |
| [`dict_to_literal_map_pb()`](#dict_to_literal_map_pb) | None |
| [`get_available_transformers()`](#get_available_transformers) | Returns all python types for which transformers are available |
| [`get_transformer()`](#get_transformer) | Implements a recursive search for the transformer |
| [`guess_python_type()`](#guess_python_type) | Transforms a flyte-specific ``LiteralType`` to a regular python value |
| [`guess_python_types()`](#guess_python_types) | Transforms a dictionary of flyte-specific ``Variable`` objects to a dictionary of regular python values |
| [`lazy_import_transformers()`](#lazy_import_transformers) | Only load the transformers if needed |
| [`literal_map_to_kwargs()`](#literal_map_to_kwargs) | None |
| [`named_tuple_to_variable_map()`](#named_tuple_to_variable_map) | Converts a python-native ``NamedTuple`` to a flyte-specific VariableMap of named literals |
| [`register()`](#register) | This should be used for all types that respond with the right type annotation when you use type( |
| [`register_additional_type()`](#register_additional_type) | None |
| [`register_restricted_type()`](#register_restricted_type) | None |
| [`to_html()`](#to_html) | None |
| [`to_literal()`](#to_literal) | The current dance is because we are allowing users to call from an async function, this synchronous |
| [`to_literal_checks()`](#to_literal_checks) | None |
| [`to_literal_type()`](#to_literal_type) | Converts a python type into a flyte specific ``LiteralType`` |
| [`to_python_value()`](#to_python_value) | Converts a Literal value with an expected python type into a python value |
| [`unwrap_offloaded_literal()`](#unwrap_offloaded_literal) | None |


#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
):
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
):
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
):
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
):
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
):
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
):
```
Implements a recursive search for the transformer.


| Parameter | Type |
|-|-|
| `python_type` | `Type` |

#### guess_python_type()

```python
def guess_python_type(
    flyte_type: LiteralType,
):
```
Transforms a flyte-specific ``LiteralType`` to a regular python value.


| Parameter | Type |
|-|-|
| `flyte_type` | `LiteralType` |

#### guess_python_types()

```python
def guess_python_types(
    flyte_variable_dict: typing.Dict[str, _interface_models.Variable],
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |

## flytekit.core.gate.VoidPromise

This object is returned for tasks that do not return any outputs (declared interface is empty)
VoidPromise cannot be interacted with and does not allow comparisons or any operations


```python
def VoidPromise(
    task_name: str,
    ref: Optional[NodeOutput],
):
```
| Parameter | Type |
|-|-|
| `task_name` | `str` |
| `ref` | `Optional[NodeOutput]` |

### Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is a placeholder and should do nothing |
| [`with_overrides()`](#with_overrides) | None |


#### runs_before()

```python
def runs_before(
    args,
    kwargs,
):
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
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| ref |  |  |
| task_name |  |  |

