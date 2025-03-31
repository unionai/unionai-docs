---
title: flytekit.extend.backend.base_agent
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extend.backend.base_agent

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentabc) | Helper class that provides a standard way to create an ABC using. |
| [`Agent`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentagent) | A ProtocolMessage. |
| [`AgentBase`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentagentbase) | Helper class that provides a standard way to create an ABC using. |
| [`AgentRegistry`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentagentregistry) | This is the registry for all agents. |
| [`Any`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentany) | Special type indicating an unconstrained type. |
| [`AsyncAgentBase`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentasyncagentbase) | This is the base class for all async agents. |
| [`AsyncAgentExecutorMixin`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentasyncagentexecutormixin) | This mixin class is used to run the async task locally, and it's only used for local execution. |
| [`ExecutionState`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FlyteContext`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FrameType`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentframetype) | None. |
| [`ImageConfig`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentimageconfig) | We recommend you to use ImageConfig. |
| [`LiteralMap`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentliteralmap) | None. |
| [`OrderedDict`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentordereddict) | Dictionary that remembers insertion order. |
| [`Progress`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentprogress) | Renders an auto-updating progress bar(s). |
| [`PythonFunctionTask`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentpythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`PythonTask`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`Resource`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentresource) | This is the output resource of the job. |
| [`ResourceMeta`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentresourcemeta) | This is the metadata for the job. |
| [`RichHandler`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentrichhandler) | A logging handler that renders output with Rich. |
| [`SerializationSettings`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`Struct`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentstruct) | A ProtocolMessage. |
| [`SyncAgentBase`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentsyncagentbase) | This is the base class for all sync agents. |
| [`SyncAgentExecutorMixin`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentsyncagentexecutormixin) | This mixin class is used to run the sync task locally, and it's only used for local execution. |
| [`TaskCategory`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttaskcategory) | None. |
| [`TaskExecution`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttaskexecution) | A ProtocolMessage. |
| [`TaskExecutionMetadata`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttaskexecutionmetadata) | None. |
| [`TaskLog`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttasklog) | A ProtocolMessage. |
| [`TaskTemplate`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttasktemplate) | None. |
| [`TypeEngine`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agenttypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`partial`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentpartial) | partial(func, *args, **keywords) - new function with partial application. |

### Errors

* [`FlyteAgentNotFound`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentflyteagentnotfound)
* [`FlyteUserException`](.././flytekit.extend.backend.base_agent#flytekitextendbackendbase_agentflyteuserexception)

## flytekit.extend.backend.base_agent.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.extend.backend.base_agent.Agent

A ProtocolMessage


## flytekit.extend.backend.base_agent.AgentBase

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def AgentBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| task_category |  |  |

## flytekit.extend.backend.base_agent.AgentRegistry

This is the registry for all agents.
The agent service will look up the agent registry based on the task type.
The agent metadata service will look up the agent metadata based on the agent name.


### Methods

| Method | Description |
|-|-|
| [`get_agent()`](#get_agent) | None |
| [`get_agent_metadata()`](#get_agent_metadata) | None |
| [`list_agents()`](#list_agents) | None |
| [`register()`](#register) | None |


#### get_agent()

```python
def get_agent(
    task_type_name: str,
    task_type_version: int,
):
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |

#### get_agent_metadata()

```python
def get_agent_metadata(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |

#### list_agents()

```python
def list_agents()
```
#### register()

```python
def register(
    agent: typing.Union[flytekit.extend.backend.base_agent.AsyncAgentBase, flytekit.extend.backend.base_agent.SyncAgentBase],
    override: bool,
):
```
| Parameter | Type |
|-|-|
| `agent` | `typing.Union[flytekit.extend.backend.base_agent.AsyncAgentBase, flytekit.extend.backend.base_agent.SyncAgentBase]` |
| `override` | `bool` |

## flytekit.extend.backend.base_agent.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.extend.backend.base_agent.AsyncAgentBase

This is the base class for all async agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents. The propeller will communicate with the agent service
to create tasks, get the status of tasks, and delete tasks.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def AsyncAgentBase(
    metadata_type: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `metadata_type` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task |
| [`delete()`](#delete) | Delete the task |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    task_execution_metadata: typing.Optional[flytekit.models.task.TaskExecutionMetadata],
    kwargs,
):
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `task_execution_metadata` | `typing.Optional[flytekit.models.task.TaskExecutionMetadata]` |
| `kwargs` | ``**kwargs`` |

#### delete()

```python
def delete(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    kwargs,
):
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| metadata_type |  |  |
| task_category |  |  |

## flytekit.extend.backend.base_agent.AsyncAgentExecutorMixin

This mixin class is used to run the async task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the agent.

Asynchronous tasks are tasks that take a long time to complete, such as running a query.


### Methods

| Method | Description |
|-|-|
| [`agent_signal_handler()`](#agent_signal_handler) | None |
| [`execute()`](#execute) | None |


#### agent_signal_handler()

```python
def agent_signal_handler(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    signum: int,
    frame: frame,
):
```
| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `signum` | `int` |
| `frame` | `frame` |

#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.extend.backend.base_agent.ExecutionState

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

## flytekit.extend.backend.base_agent.FlyteAgentNotFound

Assertion failed.


```python
def FlyteAgentNotFound(
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

## flytekit.extend.backend.base_agent.FlyteContext

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

## flytekit.extend.backend.base_agent.FlyteContextManager

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

## flytekit.extend.backend.base_agent.FlyteUserException

Common base class for all non-exit exceptions.


```python
def FlyteUserException(
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

## flytekit.extend.backend.base_agent.FrameType

## flytekit.extend.backend.base_agent.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
default_image (Optional[Image]): The default image to be used as a container for task serialization.
images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
def ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name |
| [`auto_default_image()`](#auto_default_image) | None |
| [`create_from()`](#create_from) | None |
| [`find_image()`](#find_image) | Return an image, by name, if it exists |
| [`from_dict()`](#from_dict) | None |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
):
```
Reads from config file or from img_name
Note that this function does not take into account the flytekit default images (see the Dockerfiles at the
base of this repo). To pick those up, see the auto_default_image function..



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |
| `img_name` | `Optional[str]` |

#### auto_default_image()

```python
def auto_default_image()
```
#### create_from()

```python
def create_from(
    default_image: Optional[Image],
    other_images: typing.Optional[typing.List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
):
```
Return an image, by name, if it exists.


| Parameter | Type |
|-|-|
| `name` |  |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_images()

```python
def from_images(
    default_image: str,
    m: typing.Optional[typing.Dict[str, str]],
):
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

.. code:: python

ImageConfig.from_dict(
"ghcr.io/flyteorg/flytecookbook:v1.0.0",
{
"spark": "ghcr.io/flyteorg/myspark:...",
"other": "...",
}
)

urn:


| Parameter | Type |
|-|-|
| `default_image` | `str` |
| `m` | `typing.Optional[typing.Dict[str, str]]` |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
):
```
Validates the image to match the standard format. Also validates that only one default image
is provided. a default image, is one that is specified as ``default=<image_uri>`` or just ``<image_uri>``. All
other images should be provided with a name, in the format ``name=<image_uri>`` This method can be used with the
CLI



| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `tuple` |

## flytekit.extend.backend.base_agent.LiteralMap

```python
def LiteralMap(
    literals,
):
```
| Parameter | Type |
|-|-|
| `literals` |  |

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
| is_empty |  |  |
| literals |  |  |

## flytekit.extend.backend.base_agent.OrderedDict

Dictionary that remembers insertion order


## flytekit.extend.backend.base_agent.Progress

Renders an auto-updating progress bar(s).



```python
def Progress(
    columns: typing.Union[str, rich.progress.ProgressColumn],
    console: typing.Optional[rich.console.Console],
    auto_refresh: bool,
    refresh_per_second: float,
    speed_estimate_period: float,
    transient: bool,
    redirect_stdout: bool,
    redirect_stderr: bool,
    get_time: typing.Optional[typing.Callable[[], float]],
    disable: bool,
    expand: bool,
):
```
| Parameter | Type |
|-|-|
| `columns` | `typing.Union[str, rich.progress.ProgressColumn]` |
| `console` | `typing.Optional[rich.console.Console]` |
| `auto_refresh` | `bool` |
| `refresh_per_second` | `float` |
| `speed_estimate_period` | `float` |
| `transient` | `bool` |
| `redirect_stdout` | `bool` |
| `redirect_stderr` | `bool` |
| `get_time` | `typing.Optional[typing.Callable[[], float]]` |
| `disable` | `bool` |
| `expand` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_task()`](#add_task) | Add a new 'task' to the Progress display |
| [`advance()`](#advance) | Advance task by a number of steps |
| [`get_default_columns()`](#get_default_columns) | Get the default columns used for a new Progress instance: |
| [`get_renderable()`](#get_renderable) | Get a renderable for the progress display |
| [`get_renderables()`](#get_renderables) | Get a number of renderables for the progress display |
| [`make_tasks_table()`](#make_tasks_table) | Get a table to render the Progress display |
| [`open()`](#open) | Track progress while reading from a binary file |
| [`refresh()`](#refresh) | Refresh (render) the progress information |
| [`remove_task()`](#remove_task) | Delete a task if it exists |
| [`reset()`](#reset) | Reset a task so completed is 0 and the clock is reset |
| [`start()`](#start) | Start the progress display |
| [`start_task()`](#start_task) | Start a task |
| [`stop()`](#stop) | Stop the progress display |
| [`stop_task()`](#stop_task) | Stop a task |
| [`track()`](#track) | Track progress by iterating over a sequence |
| [`update()`](#update) | Update information associated with a task |
| [`wrap_file()`](#wrap_file) | Track progress file reading from a binary file |


#### add_task()

```python
def add_task(
    description: str,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: bool,
    fields: typing.Any,
):
```
Add a new 'task' to the Progress display.



| Parameter | Type |
|-|-|
| `description` | `str` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `bool` |
| `fields` | `typing.Any` |

#### advance()

```python
def advance(
    task_id: rich.progress.TaskID,
    advance: float,
):
```
Advance task by a number of steps.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `advance` | `float` |

#### get_default_columns()

```python
def get_default_columns()
```
Get the default columns used for a new Progress instance:
- a text column for the description (TextColumn)
- the bar itself (BarColumn)
- a text column showing completion percentage (TextColumn)
- an estimated-time-remaining column (TimeRemainingColumn)
If the Progress instance is created without passing a columns argument,
the default columns defined here will be used.

You can also create a Progress instance using custom columns before
and/or after the defaults, as in this example:

progress = Progress(
SpinnerColumn(),
*Progress.get_default_columns(),
"Elapsed:",
TimeElapsedColumn(),
)

This code shows the creation of a Progress display, containing
a spinner to the left, the default columns, and a labeled elapsed
time column.


#### get_renderable()

```python
def get_renderable()
```
Get a renderable for the progress display.


#### get_renderables()

```python
def get_renderables()
```
Get a number of renderables for the progress display.


#### make_tasks_table()

```python
def make_tasks_table(
    tasks: typing.Iterable[rich.progress.Task],
):
```
Get a table to render the Progress display.



| Parameter | Type |
|-|-|
| `tasks` | `typing.Iterable[rich.progress.Task]` |

#### open()

```python
def open(
    file: typing.Union[str, ForwardRef('PathLike[str]'), bytes],
    mode: typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']],
    buffering: int,
    encoding: typing.Optional[str],
    errors: typing.Optional[str],
    newline: typing.Optional[str],
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
):
```
Track progress while reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.Union[str, ForwardRef('PathLike[str]'), bytes]` |
| `mode` | `typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']]` |
| `buffering` | `int` |
| `encoding` | `typing.Optional[str]` |
| `errors` | `typing.Optional[str]` |
| `newline` | `typing.Optional[str]` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

#### refresh()

```python
def refresh()
```
Refresh (render) the progress information.


#### remove_task()

```python
def remove_task(
    task_id: rich.progress.TaskID,
):
```
Delete a task if it exists.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### reset()

```python
def reset(
    task_id: rich.progress.TaskID,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: typing.Optional[bool],
    description: typing.Optional[str],
    fields: typing.Any,
):
```
Reset a task so completed is 0 and the clock is reset.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `typing.Optional[bool]` |
| `description` | `typing.Optional[str]` |
| `fields` | `typing.Any` |

#### start()

```python
def start()
```
Start the progress display.


#### start_task()

```python
def start_task(
    task_id: rich.progress.TaskID,
):
```
Start a task.

Starts a task (used when calculating elapsed time). You may need to call this manually,
if you called ``add_task`` with ``start=False``.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### stop()

```python
def stop()
```
Stop the progress display.


#### stop_task()

```python
def stop_task(
    task_id: rich.progress.TaskID,
):
```
Stop a task.

This will freeze the elapsed time on the task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### track()

```python
def track(
    sequence: typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]],
    total: typing.Optional[float],
    completed: int,
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
    update_period: float,
):
```
Track progress by iterating over a sequence.



| Parameter | Type |
|-|-|
| `sequence` | `typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]]` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |
| `update_period` | `float` |

#### update()

```python
def update(
    task_id: rich.progress.TaskID,
    total: typing.Optional[float],
    completed: typing.Optional[float],
    advance: typing.Optional[float],
    description: typing.Optional[str],
    visible: typing.Optional[bool],
    refresh: bool,
    fields: typing.Any,
):
```
Update information associated with a task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `total` | `typing.Optional[float]` |
| `completed` | `typing.Optional[float]` |
| `advance` | `typing.Optional[float]` |
| `description` | `typing.Optional[str]` |
| `visible` | `typing.Optional[bool]` |
| `refresh` | `bool` |
| `fields` | `typing.Any` |

#### wrap_file()

```python
def wrap_file(
    file: typing.BinaryIO,
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
):
```
Track progress file reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.BinaryIO` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| console |  |  |
| finished |  |  |
| task_ids |  |  |
| tasks |  |  |

## flytekit.extend.backend.base_agent.PythonFunctionTask

A Python Function task should be used as the base for all extensions that have a python function. It will
automatically detect interface of the python function and when serialized on the hosted Flyte platform handles the
writing execution command to execute the function

It is advised this task is used using the @task decorator as follows

.. code-block: python

@task
def my_func(a: int) -> str:
...

In the above code, the name of the function, the module, and the interface (inputs = int and outputs = str) will be
auto detected.


```python
def PythonFunctionTask(
    task_config: T,
    task_function: Callable,
    task_type,
    ignore_input_vars: Optional[List[str]],
    execution_mode: ExecutionBehavior,
    task_resolver: Optional[TaskResolverMixin],
    node_dependency_hints: Optional[Iterable[Union['PythonFunctionTask', '_annotated_launch_plan.LaunchPlan', WorkflowBase]]],
    pickle_untyped: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_config` | `T` |
| `task_function` | `Callable` |
| `task_type` |  |
| `ignore_input_vars` | `Optional[List[str]]` |
| `execution_mode` | `ExecutionBehavior` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `node_dependency_hints` | `Optional[Iterable[Union['PythonFunctionTask', '_annotated_launch_plan.LaunchPlan', WorkflowBase]]]` |
| `pickle_untyped` | `bool` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`compile_into_workflow()`](#compile_into_workflow) | In the case of dynamic workflows, this function will produce a workflow definition at execution time which will |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`dynamic_execute()`](#dynamic_execute) | By the time this function is invoked, the local_execute function should have unwrapped the Promises and Flyte |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### compile_into_workflow()

```python
def compile_into_workflow(
    ctx: FlyteContext,
    task_function: Callable,
    kwargs,
):
```
In the case of dynamic workflows, this function will produce a workflow definition at execution time which will
then proceed to be executed.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `task_function` | `Callable` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### dynamic_execute()

```python
def dynamic_execute(
    task_function: Callable,
    kwargs,
):
```
By the time this function is invoked, the local_execute function should have unwrapped the Promises and Flyte
literal wrappers so that the kwargs we are working with here are now Python native literal values. This
function is also expected to return Python native literal values.

Since the user code within a dynamic task constitute a workflow, we have to first compile the workflow, and
then execute that workflow.

When running for real in production, the task would stop after the compilation step, and then create a file
representing that newly generated workflow, instead of executing it.


| Parameter | Type |
|-|-|
| `task_function` | `Callable` |
| `kwargs` | ``**kwargs`` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task. If you do decide to override this method you must also
handle dynamic tasks or you will no longer be able to use the task as a dynamic task generator.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
):
```
Returns the command which should be used in the container definition for the serialized version of this task
registered on a hosted Flyte platform.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
):
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
):
```
Update image spec based on fast registration usage, and return string representing the image


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### reset_command_fn()

```python
def reset_command_fn()
```
Resets the command which should be used in the container definition of this task to the default arguments.
This is useful when the command line is overridden at serialization time.


#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### set_command_fn()

```python
def set_command_fn(
    get_command_fn: Optional[Callable[[SerializationSettings], List[str]]],
):
```
By default, the task will run on the Flyte platform using the pyflyte-execute command.
However, it can be useful to update the command with which the task is serialized for specific cases like
running map tasks ("pyflyte-map-execute") or for fast-executed tasks.


| Parameter | Type |
|-|-|
| `get_command_fn` | `Optional[Callable[[SerializationSettings], List[str]]]` |

#### set_resolver()

```python
def set_resolver(
    resolver: TaskResolverMixin,
):
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

### Properties

| Property | Type | Description |
|-|-|-|
| container_image |  |  |
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| execution_mode |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| node_dependency_hints |  |  |
| python_interface |  |  |
| resources |  |  |
| security_context |  |  |
| task_config |  |  |
| task_function |  |  |
| task_resolver |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.extend.backend.base_agent.PythonTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
def PythonTask(
    task_type: str,
    name: str,
    task_config: typing.Optional[~T],
    interface: typing.Optional[flytekit.core.interface.Interface],
    environment: typing.Optional[typing.Dict[str, str]],
    disable_deck: typing.Optional[bool],
    enable_deck: typing.Optional[bool],
    deck_fields: typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type` | `str` |
| `name` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `interface` | `typing.Optional[flytekit.core.interface.Interface]` |
| `environment` | `typing.Optional[typing.Dict[str, str]]` |
| `disable_deck` | `typing.Optional[bool]` |
| `enable_deck` | `typing.Optional[bool]` |
| `deck_fields` | `typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| security_context |  |  |
| task_config |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.extend.backend.base_agent.Resource

This is the output resource of the job.



```python
def Resource(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1060829f0>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]],
    outputs: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
):
```
| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1060829f0>` |
| `message` | `typing.Optional[str]` |
| `log_links` | `typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]]` |
| `outputs` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType]` |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`to_flyte_idl()`](#to_flyte_idl) | This function is async to call the async type engine functions |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.agent_pb2.Resource,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.agent_pb2.Resource` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
This function is async to call the async type engine functions. This is okay to do because this is not a
normal model class that inherits from FlyteIdlEntity


## flytekit.extend.backend.base_agent.ResourceMeta

This is the metadata for the job. For example, the id of the job.


```python
def ResourceMeta()
```
### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes |
| [`encode()`](#encode) | Encode the resource meta to bytes |


#### decode()

```python
def decode(
    data: bytes,
):
```
Decode the resource meta from bytes.


| Parameter | Type |
|-|-|
| `data` | `bytes` |

#### encode()

```python
def encode()
```
Encode the resource meta to bytes.


## flytekit.extend.backend.base_agent.RichHandler

A logging handler that renders output with Rich. The time / level / message and file are displayed in columns.
The level is color coded, and the message is syntax highlighted.

Note:
Be careful when enabling console markup in log messages if you have configured logging for libraries not
under your control. If a dependency writes messages containing square brackets, it may not produce the intended output.



```python
def RichHandler(
    level: typing.Union[int, str],
    console: typing.Optional[rich.console.Console],
    show_time: bool,
    omit_repeated_times: bool,
    show_level: bool,
    show_path: bool,
    enable_link_path: bool,
    highlighter: typing.Optional[rich.highlighter.Highlighter],
    markup: bool,
    rich_tracebacks: bool,
    tracebacks_width: typing.Optional[int],
    tracebacks_code_width: int,
    tracebacks_extra_lines: int,
    tracebacks_theme: typing.Optional[str],
    tracebacks_word_wrap: bool,
    tracebacks_show_locals: bool,
    tracebacks_suppress: typing.Iterable[typing.Union[str, module]],
    tracebacks_max_frames: int,
    locals_max_length: int,
    locals_max_string: int,
    log_time_format: typing.Union[str, typing.Callable[[datetime.datetime], rich.text.Text]],
    keywords: typing.Optional[typing.List[str]],
):
```
Initializes the instance - basically setting the formatter to None
and the filter list to empty.


| Parameter | Type |
|-|-|
| `level` | `typing.Union[int, str]` |
| `console` | `typing.Optional[rich.console.Console]` |
| `show_time` | `bool` |
| `omit_repeated_times` | `bool` |
| `show_level` | `bool` |
| `show_path` | `bool` |
| `enable_link_path` | `bool` |
| `highlighter` | `typing.Optional[rich.highlighter.Highlighter]` |
| `markup` | `bool` |
| `rich_tracebacks` | `bool` |
| `tracebacks_width` | `typing.Optional[int]` |
| `tracebacks_code_width` | `int` |
| `tracebacks_extra_lines` | `int` |
| `tracebacks_theme` | `typing.Optional[str]` |
| `tracebacks_word_wrap` | `bool` |
| `tracebacks_show_locals` | `bool` |
| `tracebacks_suppress` | `typing.Iterable[typing.Union[str, module]]` |
| `tracebacks_max_frames` | `int` |
| `locals_max_length` | `int` |
| `locals_max_string` | `int` |
| `log_time_format` | `typing.Union[str, typing.Callable[[datetime.datetime], rich.text.Text]]` |
| `keywords` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`acquire()`](#acquire) | Acquire the I/O thread lock |
| [`addFilter()`](#addfilter) | Add the specified filter to this handler |
| [`close()`](#close) | Tidy up any resources used by the handler |
| [`createLock()`](#createlock) | Acquire a thread lock for serializing access to the underlying I/O |
| [`emit()`](#emit) | Invoked by logging |
| [`filter()`](#filter) | Determine if a record is loggable by consulting all the filters |
| [`flush()`](#flush) | Ensure all logging output has been flushed |
| [`format()`](#format) | Format the specified record |
| [`get_level_text()`](#get_level_text) | Get the level name from the record |
| [`get_name()`](#get_name) | None |
| [`handle()`](#handle) | Conditionally emit the specified logging record |
| [`handleError()`](#handleerror) | Handle errors which occur during an emit() call |
| [`release()`](#release) | Release the I/O thread lock |
| [`removeFilter()`](#removefilter) | Remove the specified filter from this handler |
| [`render()`](#render) | Render log for display |
| [`render_message()`](#render_message) | Render message text in to Text |
| [`setFormatter()`](#setformatter) | Set the formatter for this handler |
| [`setLevel()`](#setlevel) | Set the logging level of this handler |
| [`set_name()`](#set_name) | None |


#### acquire()

```python
def acquire()
```
Acquire the I/O thread lock.


#### addFilter()

```python
def addFilter(
    filter,
):
```
Add the specified filter to this handler.


| Parameter | Type |
|-|-|
| `filter` |  |

#### close()

```python
def close()
```
Tidy up any resources used by the handler.

This version removes the handler from an internal map of handlers,
_handlers, which is used for handler lookup by name. Subclasses
should ensure that this gets called from overridden close()
methods.


#### createLock()

```python
def createLock()
```
Acquire a thread lock for serializing access to the underlying I/O.


#### emit()

```python
def emit(
    record: logging.LogRecord,
):
```
Invoked by logging.


| Parameter | Type |
|-|-|
| `record` | `logging.LogRecord` |

#### filter()

```python
def filter(
    record,
):
```
Determine if a record is loggable by consulting all the filters.

The default is to allow the record to be logged; any filter can veto
this by returning a false value.
If a filter attached to a handler returns a log record instance,
then that instance is used in place of the original log record in
any further processing of the event by that handler.
If a filter returns any other true value, the original log record
is used in any further processing of the event by that handler.

If none of the filters return false values, this method returns
a log record.
If any of the filters return a false value, this method returns
a false value.

.. versionchanged:: 3.2

Allow filters to be just callables.

.. versionchanged:: 3.12
Allow filters to return a LogRecord instead of
modifying it in place.


| Parameter | Type |
|-|-|
| `record` |  |

#### flush()

```python
def flush()
```
Ensure all logging output has been flushed.

This version does nothing and is intended to be implemented by
subclasses.


#### format()

```python
def format(
    record,
):
```
Format the specified record.

If a formatter is set, use it. Otherwise, use the default formatter
for the module.


| Parameter | Type |
|-|-|
| `record` |  |

#### get_level_text()

```python
def get_level_text(
    record: logging.LogRecord,
):
```
Get the level name from the record.



| Parameter | Type |
|-|-|
| `record` | `logging.LogRecord` |

#### get_name()

```python
def get_name()
```
#### handle()

```python
def handle(
    record,
):
```
Conditionally emit the specified logging record.

Emission depends on filters which may have been added to the handler.
Wrap the actual emission of the record with acquisition/release of
the I/O thread lock.

Returns an instance of the log record that was emitted
if it passed all filters, otherwise a false value is returned.


| Parameter | Type |
|-|-|
| `record` |  |

#### handleError()

```python
def handleError(
    record,
):
```
Handle errors which occur during an emit() call.

This method should be called from handlers when an exception is
encountered during an emit() call. If raiseExceptions is false,
exceptions get silently ignored. This is what is mostly wanted
for a logging system - most users will not care about errors in
the logging system, they are more interested in application errors.
You could, however, replace this with a custom handler if you wish.
The record which was being processed is passed in to this method.


| Parameter | Type |
|-|-|
| `record` |  |

#### release()

```python
def release()
```
Release the I/O thread lock.


#### removeFilter()

```python
def removeFilter(
    filter,
):
```
Remove the specified filter from this handler.


| Parameter | Type |
|-|-|
| `filter` |  |

#### render()

```python
def render(
    record: logging.LogRecord,
    traceback: typing.Optional[rich.traceback.Traceback],
    message_renderable: ConsoleRenderable,
):
```
Render log for display.



| Parameter | Type |
|-|-|
| `record` | `logging.LogRecord` |
| `traceback` | `typing.Optional[rich.traceback.Traceback]` |
| `message_renderable` | `ConsoleRenderable` |

#### render_message()

```python
def render_message(
    record: logging.LogRecord,
    message: str,
):
```
Render message text in to Text.



| Parameter | Type |
|-|-|
| `record` | `logging.LogRecord` |
| `message` | `str` |

#### setFormatter()

```python
def setFormatter(
    fmt,
):
```
Set the formatter for this handler.


| Parameter | Type |
|-|-|
| `fmt` |  |

#### setLevel()

```python
def setLevel(
    level,
):
```
Set the logging level of this handler.  level must be an int or a str.


| Parameter | Type |
|-|-|
| `level` |  |

#### set_name()

```python
def set_name(
    name,
):
```
| Parameter | Type |
|-|-|
| `name` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| name |  |  |

## flytekit.extend.backend.base_agent.SerializationSettings

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
project (str): The project (if any) with which to register entities under.
domain (str): The domain (if any) with which to register entities under.
version (str): The version (if any) with which to register entities under.
image_config (ImageConfig): The image config used to define task container images.
env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
virtualenv at serialization time won't match the in-container value at execution time. This optional value
is used to provide the in-container virtualenv path
python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
container execution.
entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
entrypoint program.
fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
can be fast registered (and thus omit building a Docker image) this object contains additional parameters
for serialization.
source_root (Optional[str]): The root directory of the source code.


```python
def SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `image_config` | `ImageConfig` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `version` | `typing.Optional[str]` |
| `env` | `Optional[Dict[str, str]]` |
| `git_repo` | `Optional[str]` |
| `python_interpreter` | `str` |
| `flytekit_virtualenv_root` | `Optional[str]` |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` |
| `source_root` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is |
| [`for_image()`](#for_image) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_transport()`](#from_transport) | None |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings |
| [`schema()`](#schema) | None |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
):
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
):
```
| Parameter | Type |
|-|-|
| `image` | `str` |
| `version` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `python_interpreter_path` | `str` |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_transport()

```python
def from_transport(
    s: str,
):
```
| Parameter | Type |
|-|-|
| `s` | `str` |

#### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


#### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
):
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -> /opt/venv


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


### Properties

| Property | Type | Description |
|-|-|-|
| entrypoint_settings |  |  |
| serialized_context |  |  |

## flytekit.extend.backend.base_agent.Struct

A ProtocolMessage


### Methods

| Method | Description |
|-|-|
| [`get_or_create_list()`](#get_or_create_list) | Returns a list for this key, creating if it didn't exist already |
| [`get_or_create_struct()`](#get_or_create_struct) | Returns a struct for this key, creating if it didn't exist already |
| [`items()`](#items) | None |
| [`keys()`](#keys) | None |
| [`update()`](#update) | None |
| [`values()`](#values) | None |


#### get_or_create_list()

```python
def get_or_create_list(
    key,
):
```
Returns a list for this key, creating if it didn't exist already.


| Parameter | Type |
|-|-|
| `key` |  |

#### get_or_create_struct()

```python
def get_or_create_struct(
    key,
):
```
Returns a struct for this key, creating if it didn't exist already.


| Parameter | Type |
|-|-|
| `key` |  |

#### items()

```python
def items()
```
#### keys()

```python
def keys()
```
#### update()

```python
def update(
    dictionary,
):
```
| Parameter | Type |
|-|-|
| `dictionary` |  |

#### values()

```python
def values()
```
## flytekit.extend.backend.base_agent.SyncAgentBase

This is the base class for all sync agents. It defines the interface that all agents must implement.
The agent service is responsible for invoking agents.
Propeller sends a request to agent service, and gets a response in the same call.

All the agents should be registered in the AgentRegistry. Agent Service
will look up the agent based on the task type. Every task type can only have one agent.


```python
def SyncAgentBase(
    task_type_name: str,
    task_type_version: int,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type_name` | `str` |
| `task_type_version` | `int` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`do()`](#do) | This is the method that the agent will run |


#### do()

```python
def do(
    task_template: flytekit.models.task.TaskTemplate,
    output_prefix: str,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwargs,
):
```
This is the method that the agent will run.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `output_prefix` | `str` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| task_category |  |  |

## flytekit.extend.backend.base_agent.SyncAgentExecutorMixin

This mixin class is used to run the sync task locally, and it's only used for local execution.
Task should inherit from this class if the task can be run in the agent.

Synchronous tasks run quickly and can return their results instantly.
Sending a prompt to ChatGPT and getting a response, or retrieving some metadata from a backend system.


### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | None |


#### execute()

```python
def execute(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.extend.backend.base_agent.TaskCategory

```python
def TaskCategory(
    name: str,
    version: int,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `version` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| name |  |  |
| version |  |  |

## flytekit.extend.backend.base_agent.TaskExecution

A ProtocolMessage


## flytekit.extend.backend.base_agent.TaskExecutionMetadata

```python
def TaskExecutionMetadata(
    task_execution_id,
    namespace,
    labels,
    annotations,
    k8s_service_account,
    environment_variables,
    identity,
):
```
Runtime task execution metadata.



| Parameter | Type |
|-|-|
| `task_execution_id` |  |
| `namespace` |  |
| `labels` |  |
| `annotations` |  |
| `k8s_service_account` |  |
| `environment_variables` |  |
| `identity` |  |

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
| annotations |  |  |
| environment_variables |  |  |
| identity |  |  |
| is_empty |  |  |
| k8s_service_account |  |  |
| labels |  |  |
| namespace |  |  |
| task_execution_id |  |  |

## flytekit.extend.backend.base_agent.TaskLog

A ProtocolMessage


## flytekit.extend.backend.base_agent.TaskTemplate

```python
def TaskTemplate(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
):
```
A task template represents the full set of information necessary to perform a unit of work in the Flyte system.
It contains the metadata about what inputs and outputs are consumed or produced.  It also contains the metadata
necessary for Flyte Propeller to do the appropriate work.



| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` |  |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |

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
| config |  |  |
| container |  |  |
| custom |  |  |
| extended_resources |  |  |
| id |  |  |
| interface |  |  |
| is_empty |  |  |
| k8s_pod |  |  |
| metadata |  |  |
| security_context |  |  |
| sql |  |  |
| task_type_version |  |  |
| type |  |  |

## flytekit.extend.backend.base_agent.TypeEngine

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

## flytekit.extend.backend.base_agent.partial

partial(func, *args, **keywords) - new function with partial application
of the given arguments and keywords.


