---
title: flytekit.core.context_manager
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.context_manager



.. autoclass:: flytekit.core.context_manager::ExecutionState.Mode
   :noindex:
.. autoclass:: flytekit.core.context_manager::ExecutionState.Mode.TASK_EXECUTION
   :noindex:
.. autoclass:: flytekit.core.context_manager::ExecutionState.Mode.LOCAL_WORKFLOW_EXECUTION
   :noindex:
.. autoclass:: flytekit.core.context_manager::ExecutionState.Mode.LOCAL_TASK_EXECUTION
   :noindex:


## Directory

### Classes

| Class | Description |
|-|-|
| [`CompilationState`](.././flytekit.core.context_manager#flytekitcorecontext_managercompilationstate) | Compilation state is used during the compilation of a workflow or task. |
| [`ExecutionParameters`](.././flytekit.core.context_manager#flytekitcorecontext_managerexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`ExecutionState`](.././flytekit.core.context_manager#flytekitcorecontext_managerexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.core.context_manager#flytekitcorecontext_managerflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.core.context_manager#flytekitcorecontext_managerflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteEntities`](.././flytekit.core.context_manager#flytekitcorecontext_managerflyteentities) | This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`OutputMetadata`](.././flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadata) |  |
| [`OutputMetadataTracker`](.././flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`SecretsManager`](.././flytekit.core.context_manager#flytekitcorecontext_managersecretsmanager) | This provides a secrets resolution logic at runtime. |
| [`SerializableToString`](.././flytekit.core.context_manager#flytekitcorecontext_managerserializabletostring) | This protocol is used by the Artifact create_from function. |

### Variables

| Property | Type | Description |
|-|-|-|
| `flyte_context_Var` | `ContextVar` |  |

## flytekit.core.context_manager.CompilationState

Compilation state is used during the compilation of a workflow or task. It stores the nodes that were
created when walking through the workflow graph.

Attributes:
    prefix (str): This is because we may one day want to be able to have subworkflows inside other workflows. If
        users choose to not specify their node names, then we can end up with multiple "n0"s. This prefix allows
        us to give those nested nodes a distinct name, as well as properly identify them in the workflow.
    mode (int): refer to `flytekit.extend.ExecutionState.Mode`
    task_resolver (Optional[TaskResolverMixin]): Please see `flytekit.extend.TaskResolverMixin`
    nodes (Optional[List]): Stores currently compiled nodes so far.


```python
class CompilationState(
    prefix: str,
    mode: int,
    task_resolver: Optional[TaskResolverMixin],
    nodes: List,
)
```
| Parameter | Type |
|-|-|
| `prefix` | `str` |
| `mode` | `int` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `nodes` | `List` |

### Methods

| Method | Description |
|-|-|
| [`add_node()`](#add_node) |  |
| [`with_params()`](#with_params) | Create a new CompilationState where the mode and task resolver are defaulted to the current object, but they. |


#### add_node()

```python
def add_node(
    n: Node,
)
```
| Parameter | Type |
|-|-|
| `n` | `Node` |

#### with_params()

```python
def with_params(
    prefix: str,
    mode: Optional[int],
    resolver: Optional[TaskResolverMixin],
    nodes: Optional[List],
) -> CompilationState
```
Create a new CompilationState where the mode and task resolver are defaulted to the current object, but they
and all other args are taken if explicitly provided as an argument.

Usage:
    s.with_params("p", nodes=[])


| Parameter | Type |
|-|-|
| `prefix` | `str` |
| `mode` | `Optional[int]` |
| `resolver` | `Optional[TaskResolverMixin]` |
| `nodes` | `Optional[List]` |

## flytekit.core.context_manager.ExecutionParameters

This is a run-time user-centric context object that is accessible to every @task method. It can be accessed using


```python
flytekit.current_context()
```

This object provides the following objections
* a statsd handler
* a logging handler
* the execution ID as an `flytekit.models.core.identifier.WorkflowExecutionIdentifier` object
* a working directory for the user to write arbitrary files to

Please do not confuse this object with the `flytekit.FlyteContext` object.


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

> [!NOTE]
> Do NOT use this execution_date to drive any production logic.  It might be useful as a tag for data to help
    in debugging.
{{< /multiline >}} |
| `execution_id` |  | {{< multiline >}}This is the identifier of the workflow execution within the underlying engine.  It will be consistent across all
task executions in a workflow or sub-workflow execution.

> [!NOTE]
> Do NOT use this execution_id to drive any production logic.  This execution ID should only be used as a tag
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

## flytekit.core.context_manager.ExecutionState

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

## flytekit.core.context_manager.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the `flytekit.ExecutionParameters` object.


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
with {{< py_func_ref flytekit.current_context >}}


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

```python
with flytekit.new_context() as ctx:
    my_task(...)
ctx.get_deck()
```

OR if you wish to explicitly display

```python
from IPython import display
display(ctx.get_deck())
```


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

## flytekit.core.context_manager.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

```python
FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
    pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()
```


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

## flytekit.core.context_manager.FlyteEntities

This is a global Object that tracks various tasks and workflows that are declared within a VM during the
 registration process


## flytekit.core.context_manager.OutputMetadata

```python
class OutputMetadata(
    artifact: 'Artifact',
    dynamic_partitions: Optional[typing.Dict[str, str]],
    time_partition: Optional[datetime],
    additional_items: Optional[typing.List[SerializableToString]],
)
```
| Parameter | Type |
|-|-|
| `artifact` | `'Artifact'` |
| `dynamic_partitions` | `Optional[typing.Dict[str, str]]` |
| `time_partition` | `Optional[datetime]` |
| `additional_items` | `Optional[typing.List[SerializableToString]]` |

## flytekit.core.context_manager.OutputMetadataTracker

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

## flytekit.core.context_manager.SecretsManager

This provides a secrets resolution logic at runtime.
The resolution order is
  - Try env var first. The env var should have the configuration.SECRETS_ENV_PREFIX. The env var will be all upper
     cased
  - If not then try the file where the name matches lower case
    ``configuration.SECRETS_DEFAULT_DIR/<group>/configuration.SECRETS_FILE_PREFIX<key>``

All configuration values can always be overridden by injecting an environment variable


```python
class SecretsManager(
    secrets_cfg: typing.Optional[SecretsConfig],
)
```
| Parameter | Type |
|-|-|
| `secrets_cfg` | `typing.Optional[SecretsConfig]` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Retrieves a secret using the resolution order -> Env followed by file. |
| [`get_secrets_env_var()`](#get_secrets_env_var) | Returns a string that matches the ENV Variable to look for the secrets. |
| [`get_secrets_file()`](#get_secrets_file) | Returns a path that matches the file to look for the secrets. |


#### get()

```python
def get(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
    encode_mode: str,
) -> str
```
Retrieves a secret using the resolution order -> Env followed by file. If not found raises a ValueError
param encode_mode, defines the mode to open files, it can either be "r" to read file, or "rb" to read binary file


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |
| `encode_mode` | `str` |

#### get_secrets_env_var()

```python
def get_secrets_env_var(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a string that matches the ENV Variable to look for the secrets


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |

#### get_secrets_file()

```python
def get_secrets_file(
    group: Optional[str],
    key: Optional[str],
    group_version: Optional[str],
) -> str
```
Returns a path that matches the file to look for the secrets


| Parameter | Type |
|-|-|
| `group` | `Optional[str]` |
| `key` | `Optional[str]` |
| `group_version` | `Optional[str]` |

## flytekit.core.context_manager.SerializableToString

This protocol is used by the Artifact create_from function. Basically these objects are serialized when running,
and then added to a literal's metadata.


```python
class SerializableToString(
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
| [`serialize_to_string()`](#serialize_to_string) |  |


#### serialize_to_string()

```python
def serialize_to_string(
    ctx: FlyteContext,
    variable_name: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `variable_name` | `str` |

