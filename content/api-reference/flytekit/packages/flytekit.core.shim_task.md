---
title: flytekit.core.shim_task
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.shim_task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.shim_task#flytekitcoreshim_taskany) | Special type indicating an unconstrained type. |
| [`ExecutableTemplateShimTask`](.././flytekit.core.shim_task#flytekitcoreshim_taskexecutabletemplateshimtask) | The canonical ``@task`` decorated Python function task is pretty simple to reason about. |
| [`ExecutionParameters`](.././flytekit.core.shim_task#flytekitcoreshim_taskexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`ExecutionState`](.././flytekit.core.shim_task#flytekitcoreshim_taskexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.shim_task#flytekitcoreshim_taskflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.core.shim_task#flytekitcoreshim_taskflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`Generic`](.././flytekit.core.shim_task#flytekitcoreshim_taskgeneric) | Abstract base class for generic types. |
| [`ShimTaskExecutor`](.././flytekit.core.shim_task#flytekitcoreshim_taskshimtaskexecutor) | Please see the notes for the metaclass above first. |
| [`TrackedInstance`](.././flytekit.core.shim_task#flytekitcoreshim_tasktrackedinstance) | Please see the notes for the metaclass above first. |
| [`TypeEngine`](.././flytekit.core.shim_task#flytekitcoreshim_tasktypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeVar`](.././flytekit.core.shim_task#flytekitcoreshim_tasktypevar) | Type variable. |

### Methods

| Method | Description |
|-|-|
| [`cast()`](#cast) | Cast a value to a type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |

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

## flytekit.core.shim_task.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.shim_task.ExecutableTemplateShimTask

The canonical ``@task`` decorated Python function task is pretty simple to reason about. At execution time (either
locally or on a Flyte cluster), the function runs.

This class, along with the ``ShimTaskExecutor`` class below, represents another execution pattern. This pattern,
has two components:

* The ``TaskTemplate``, or something like it like a ``FlyteTask``.
* An executor, which can use information from the task template (including the ``custom`` field)

Basically at execution time (both locally and on a Flyte cluster), the task template is given to the executor,
which is responsible for computing and returning the results.

.. note::

The interface at execution time will have to derived from the Flyte IDL interface, which means it may be lossy.
This is because when a task is serialized from Python into the ``TaskTemplate`` some information is lost because
Flyte IDL can't keep track of every single Python type (or Java type if writing in the Java flytekit).

This class also implements the ``dispatch_execute`` and ``execute`` functions to make it look like a ``PythonTask``
that the ``entrypoint.py`` can execute, even though this class doesn't inherit from ``PythonTask``.


```python
class ExecutableTemplateShimTask(
    tt: _task_model.TaskTemplate,
    executor_type: Type[ShimTaskExecutor],
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `tt` | `_task_model.TaskTemplate` |
| `executor_type` | `Type[ShimTaskExecutor]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: FlyteContext,
    input_literal_map: _literal_models.LiteralMap,
) -> Union[_literal_models.LiteralMap, _dynamic_job.DynamicJobSpec]
```
This function is largely similar to the base PythonTask, with the exception that we have to infer the Python
interface before executing. Also, we refer to ``self.task_template`` rather than just ``self`` similar to task
classes that derive from the base ``PythonTask``.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `input_literal_map` | `_literal_models.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
) -> Any
```
Rather than running here, send everything to the executor.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### post_execute()

```python
def post_execute(
    _: Optional[ExecutionParameters],
    rval: Any,
) -> Any
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type |
|-|-|
| `_` | `Optional[ExecutionParameters]` |
| `rval` | `Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: Optional[ExecutionParameters],
) -> Optional[ExecutionParameters]
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type |
|-|-|
| `user_params` | `Optional[ExecutionParameters]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `executor` |  |  |
| `executor_type` |  |  |
| `name` |  | {{< multiline >}}Return the name of the underlying task.
{{< /multiline >}} |
| `task_template` |  |  |

## flytekit.core.shim_task.ExecutionParameters

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

## flytekit.core.shim_task.ExecutionState

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

## flytekit.core.shim_task.FlyteContext

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

## flytekit.core.shim_task.FlyteContextManager

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

## flytekit.core.shim_task.Generic

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

class Mapping[KT, VT]:
def __getitem__(self, key: KT) -> VT:
...
# Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
try:
return mapping[key]
except KeyError:
return default


## flytekit.core.shim_task.ShimTaskExecutor

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
class ShimTaskExecutor(
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
| [`execute_from_model()`](#execute_from_model) | This function must be overridden and is where all the business logic for running a task should live. |
| [`find_lhs()`](#find_lhs) |  |


#### execute_from_model()

```python
def execute_from_model(
    tt: _task_model.TaskTemplate,
    kwargs,
) -> Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type |
|-|-|
| `tt` | `_task_model.TaskTemplate` |
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

## flytekit.core.shim_task.TrackedInstance

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
class TrackedInstance(
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
| [`find_lhs()`](#find_lhs) |  |


#### find_lhs()

```python
def find_lhs()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

## flytekit.core.shim_task.TypeEngine

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

## flytekit.core.shim_task.TypeVar

Type variable.

The preferred way to construct a type variable is via the dedicated
syntax for generic functions, classes, and type aliases::

class Sequence[T]:  # T is a TypeVar
...

This syntax can also be used to create bound and constrained type
variables::

# S is a TypeVar bound to str
class StrSequence[S: str]:
...

# A is a TypeVar constrained to str or bytes
class StrOrBytesSequence[A: (str, bytes)]:
...

Type variables can also have defaults:

class IntDefault[T = int]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
D = TypeVar('D', default=int)  # Defaults to int

Type variables exist primarily for the benefit of static type
checkers.  They serve as the parameters for generic types as well
as for generic function and type alias definitions.

The variance of type variables is inferred by type checkers when they
are created through the type parameter syntax and when
``infer_variance=True`` is passed. Manually created type variables may
be explicitly marked covariant or contravariant by passing
``covariant=True`` or ``contravariant=True``. By default, manually
created type variables are invariant. See PEP 484 and PEP 695 for more
details.


