---
title: flytekit.extras.sqlite3.task
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extras.sqlite3.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`DefaultImages`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3taskdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`FlyteContext`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3taskflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`PythonCustomizedContainerTask`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3taskpythoncustomizedcontainertask) | Please take a look at the comments for :py:class`flytekit. |
| [`SQLTask`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqltask) | Base task types for all SQL tasks. |
| [`SQLite3Config`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3config) | Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`SQLite3Task`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3task) | Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`SQLite3TaskExecutor`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3tasksqlite3taskexecutor) | Please see the notes for the metaclass above first. |
| [`SerializationSettings`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3taskserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`ShimTaskExecutor`](.././flytekit.extras.sqlite3.task#flytekitextrassqlite3taskshimtaskexecutor) | Please see the notes for the metaclass above first. |

### Methods

| Method | Description |
|-|-|
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`kwtypes()`](#kwtypes) | This is a small helper function to convert the keyword arguments to an OrderedDict of types. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |
| [`unarchive_file()`](#unarchive_file) | Unarchive given archive and returns the unarchived file name. |


## Methods

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

#### kwtypes()

```python
def kwtypes(
    kwargs,
) -> typing.OrderedDict[str, typing.Type]
```
This is a small helper function to convert the keyword arguments to an OrderedDict of types.

.. code-block:: python

kwtypes(a=int, b=str)


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:
.. code-block:: python
from flytekit.lazy_import import lazy_module
sklearn = lazy_module("sklearn")
sklearn.svm.SVC()


| Parameter | Type |
|-|-|
| `fullname` |  |

#### unarchive_file()

```python
def unarchive_file(
    local_path: str,
    to_dir: str,
)
```
Unarchive given archive and returns the unarchived file name. It is expected that only one file is unarchived.
More than one file or 0 files will result in a ``RuntimeError``


| Parameter | Type |
|-|-|
| `local_path` | `str` |
| `to_dir` | `str` |

## flytekit.extras.sqlite3.task.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) |  |
| [`find_image_for()`](#find_image_for) |  |
| [`get_version_suffix()`](#get_version_suffix) |  |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
) -> str
```
| Parameter | Type |
|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` |
| `flytekit_version` | `typing.Optional[str]` |

#### get_version_suffix()

```python
def get_version_suffix()
```
## flytekit.extras.sqlite3.task.FlyteContext

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

## flytekit.extras.sqlite3.task.PythonCustomizedContainerTask

Please take a look at the comments for :py:class`flytekit.extend.ExecutableTemplateShimTask` as well. This class
should be subclassed and a custom Executor provided as a default to this parent class constructor
when building a new external-container flytekit-only plugin.

This class provides authors of new task types the basic scaffolding to create task-template based tasks. In order
to write such a task, authors need to

* subclass the ``ShimTaskExecutor`` class  and override the ``execute_from_model`` function. This function is
where all the business logic should go. Keep in mind though that you, the plugin author, will not have access
to anything that's not serialized within the ``TaskTemplate`` which is why you'll also need to
* subclass this class, and override the ``get_custom`` function to include all the information the executor
will need to run.
* Also pass the executor you created as the ``executor_type`` argument of this class's constructor.

Keep in mind that the total size of the ``TaskTemplate`` still needs to be small, since these will be accessed
frequently by the Flyte engine.


```python
class PythonCustomizedContainerTask(
    name: str,
    task_config: TC,
    container_image: str,
    executor_type: Type[ShimTaskExecutor],
    task_resolver: Optional[TaskTemplateResolver],
    task_type,
    requests: Optional[Resources],
    limits: Optional[Resources],
    environment: Optional[Dict[str, str]],
    secret_requests: Optional[List[Secret]],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `task_config` | `TC` |
| `container_image` | `str` |
| `executor_type` | `Type[ShimTaskExecutor]` |
| `task_resolver` | `Optional[TaskTemplateResolver]` |
| `task_type` |  |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `environment` | `Optional[Dict[str, str]]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) |  |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`serialize_to_model()`](#serialize_to_model) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
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

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Dict[str, str]
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
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: SerializationSettings,
) -> Dict[str, Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
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
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
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
) -> typing.Type[typing.Any]
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
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, typing.Coroutine, NoneType]
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

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### serialize_to_model()

```python
def serialize_to_model(
    settings: SerializationSettings,
) -> _task_model.TaskTemplate
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `executor` |  |  |
| `executor_type` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  | {{< multiline >}}Return the name of the underlying task.
{{< /multiline >}} |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_resolver` |  |  |
| `task_template` |  | {{< multiline >}}Override the base class implementation to serialize on first call.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.extras.sqlite3.task.SQLTask

Base task types for all SQL tasks. See :py:class:`flytekit.extras.sqlite3.task.SQLite3Task`
and :py:class:`flytekitplugins.athena.task.AthenaTask` for examples of how to use it as a base class.

.. autoclass:: flytekit.extras.sqlite3.task.SQLite3Task
:noindex:


```python
class SQLTask(
    name: str,
    query_template: str,
    task_config: typing.Optional[~T],
    task_type,
    inputs: typing.Optional[typing.Dict[str, typing.Tuple[typing.Type, typing.Any]]],
    metadata: typing.Optional[flytekit.core.base_task.TaskMetadata],
    outputs: typing.Optional[typing.Dict[str, typing.Type]],
    kwargs,
)
```
This SQLTask should mostly just be used as a base class for other SQL task types and should not be used
directly. See :py:class:`flytekit.extras.sqlite3.task.SQLite3Task`


| Parameter | Type |
|-|-|
| `name` | `str` |
| `query_template` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `task_type` |  |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Tuple[typing.Type, typing.Any]]]` |
| `metadata` | `typing.Optional[flytekit.core.base_task.TaskMetadata]` |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_query()`](#get_query) |  |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`interpolate_query()`](#interpolate_query) | This function will fill in the query template with the provided kwargs and return the interpolated query. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
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
) -> typing.Union[flytekit.models.literals.LiteralMap, flytekit.models.dynamic_job.DynamicJobSpec, typing.Coroutine]
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
) -> typing.Any
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
) -> typing.Optional[typing.Dict[str, str]]
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
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
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
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_query()

```python
def get_query(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
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
) -> typing.Type[typing.Any]
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### interpolate_query()

```python
def interpolate_query(
    query_template,
    kwargs,
) -> typing.Any
```
This function will fill in the query template with the provided kwargs and return the interpolated query.
Please note that when SQL tasks run in Flyte, this step is done by the task executor.


| Parameter | Type |
|-|-|
| `query_template` |  |
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, typing.Coroutine, NoneType]
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
) -> typing.Any
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
) -> typing.Optional[flytekit.core.context_manager.ExecutionParameters]
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
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `query_template` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.extras.sqlite3.task.SQLite3Config

Use this configuration to configure if sqlite3 files that should be loaded by the task. The file itself is
considered as a database and hence is treated like a configuration
The path to a static sqlite3 compatible database file can be

-  within the container
- or from a publicly downloadable source



```python
class SQLite3Config(
    uri: str,
    compressed: bool,
)
```
| Parameter | Type |
|-|-|
| `uri` | `str` |
| `compressed` | `bool` |

## flytekit.extras.sqlite3.task.SQLite3Task

Run client side SQLite3 queries that optionally return a FlyteSchema object.

.. note::

This is a pre-built container task. That is, your user container will not be used at task execution time.
Instead the image defined in this task definition will be used instead.

.. literalinclude:: ../../../tests/flytekit/unit/extras/sqlite3/test_task.py
:start-after: # sqlite3_start
:end-before: # sqlite3_end
:language: python
:dedent: 4

See the :ref:`integrations guide <cookbook:integrations_sql_sqlite3>` for additional usage examples and
the base class :py:class:`flytekit.extend.PythonCustomizedContainerTask` as well.


```python
class SQLite3Task(
    name: str,
    query_template: str,
    inputs: typing.Optional[typing.Dict[str, typing.Type]],
    task_config: typing.Optional[flytekit.extras.sqlite3.task.SQLite3Config],
    output_schema_type: typing.Optional[typing.Type[ForwardRef('FlyteSchema')]],
    container_image: typing.Optional[str],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `query_template` | `str` |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `task_config` | `typing.Optional[flytekit.extras.sqlite3.task.SQLite3Config]` |
| `output_schema_type` | `typing.Optional[typing.Type[ForwardRef('FlyteSchema')]]` |
| `container_image` | `typing.Optional[str]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) |  |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_query()`](#get_query) |  |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`interpolate_query()`](#interpolate_query) | This function will fill in the query template with the provided kwargs and return the interpolated query. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`serialize_to_model()`](#serialize_to_model) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
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

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Dict[str, str]
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
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Dict[str, typing.Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
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
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_query()

```python
def get_query(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
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
) -> typing.Type[typing.Any]
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### interpolate_query()

```python
def interpolate_query(
    query_template,
    kwargs,
) -> typing.Any
```
This function will fill in the query template with the provided kwargs and return the interpolated query.
Please note that when SQL tasks run in Flyte, this step is done by the task executor.


| Parameter | Type |
|-|-|
| `query_template` |  |
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, typing.Coroutine, NoneType]
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

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### serialize_to_model()

```python
def serialize_to_model(
    settings: SerializationSettings,
) -> _task_model.TaskTemplate
```
| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `executor` |  |  |
| `executor_type` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  | {{< multiline >}}Return the name of the underlying task.
{{< /multiline >}} |
| `output_columns` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `query_template` |  |  |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_resolver` |  |  |
| `task_template` |  | {{< multiline >}}Override the base class implementation to serialize on first call.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.extras.sqlite3.task.SQLite3TaskExecutor

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
class SQLite3TaskExecutor(
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
    tt: flytekit.models.task.TaskTemplate,
    kwargs,
) -> typing.Any
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type |
|-|-|
| `tt` | `flytekit.models.task.TaskTemplate` |
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

## flytekit.extras.sqlite3.task.SerializationSettings

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
class SerializationSettings(
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
)
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
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is. |
| [`for_image()`](#for_image) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_transport()`](#from_transport) |  |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings. |
| [`schema()`](#schema) |  |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path. |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext. |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
) -> EntrypointSettings
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
) -> SerializationSettings
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
) -> ~A
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
) -> ~A
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
) -> SerializationSettings
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
) -> SchemaType[A]
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
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
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
) -> str
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
) -> str
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
| `entrypoint_settings` |  |  |
| `serialized_context` |  | {{< multiline >}}:return: returns the serialization context as a base64encoded, gzip compressed, json strinnn
{{< /multiline >}} |

## flytekit.extras.sqlite3.task.ShimTaskExecutor

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

