---
title: flytekit.tools.repo
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.tools.repo

## Directory

### Classes

| Class | Description |
|-|-|
| [`CopyFileDetection`](.././flytekit.tools.repo#flytekittoolsrepocopyfiledetection) | Create a collection of name/value pairs. |
| [`FastSerializationSettings`](.././flytekit.tools.repo#flytekittoolsrepofastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`FlyteContextManager`](.././flytekit.tools.repo#flytekittoolsrepoflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteRemote`](.././flytekit.tools.repo#flytekittoolsrepoflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`Identifier`](.././flytekit.tools.repo#flytekittoolsrepoidentifier) |  |
| [`ImageConfig`](.././flytekit.tools.repo#flytekittoolsrepoimageconfig) | We recommend you to use ImageConfig. |
| [`Options`](.././flytekit.tools.repo#flytekittoolsrepooptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`Path`](.././flytekit.tools.repo#flytekittoolsrepopath) | PurePath subclass that can make system calls. |
| [`SerializationSettings`](.././flytekit.tools.repo#flytekittoolsreposerializationsettings) | These settings are provided while serializing a workflow and task, before registration. |

### Errors

| Exception | Description |
|-|-|
| [`NoSerializableEntitiesError`](.././flytekit.tools.repo#flytekittoolsreponoserializableentitieserror) | Common base class for all non-exit exceptions. |
| [`RegistrationSkipped`](.././flytekit.tools.repo#flytekittoolsreporegistrationskipped) | RegistrationSkipped error is raised when trying to register an entity that is not registrable. |

### Methods

| Method | Description |
|-|-|
| [`_find_project_root()`](#_find_project_root) | Find the root of the project. |
| [`_get_git_repo_url()`](#_get_git_repo_url) | Get git repo URL from remote. |
| [`find_common_root()`](#find_common_root) | Given an arbitrary list of folders and files, this function will use the script mode function to walk up. |
| [`get_registrable_entities()`](#get_registrable_entities) | Returns all entities that can be serialized and should be sent over to Flyte backend. |
| [`list_packages_and_modules()`](#list_packages_and_modules) | This is a helper function that returns the input list of python packages/modules as a dot delinated list. |
| [`package()`](#package) | Package the given entities and the source code (if fast is enabled) into a package with the given name in output. |
| [`persist_registrable_entities()`](#persist_registrable_entities) | For protobuf serializable list of entities, writes a file with the name if the entity and. |
| [`print_registration_status()`](#print_registration_status) |  |
| [`register()`](#register) | Temporarily, for fast register, specify both the fast arg as well as copy_style. |
| [`rprint()`](#rprint) | Print object(s) supplied via positional arguments. |
| [`serialize_and_package()`](#serialize_and_package) | Fist serialize and then package all entities. |
| [`serialize_get_control_plane_entities()`](#serialize_get_control_plane_entities) | See :py:class:`flytekit. |
| [`serialize_load_only()`](#serialize_load_only) | See :py:class:`flytekit. |
| [`serialize_to_folder()`](#serialize_to_folder) | Serialize the given set of python packages to a folder. |


### Variables

| Property | Type | Description |
|-|-|-|
| `logger` | `Logger` |  |

## Methods

#### _find_project_root()

```python
def _find_project_root(
    source_path,
) -> str
```
Find the root of the project.
The root of the project is considered to be the first ancestor from source_path that does
not contain a __init__.py file.

N.B.: This assumption only holds for regular packages (as opposed to namespace packages)


| Parameter | Type |
|-|-|
| `source_path` |  |

#### _get_git_repo_url()

```python
def _get_git_repo_url(
    source_path: str,
)
```
Get git repo URL from remote.origin.url


| Parameter | Type |
|-|-|
| `source_path` | `str` |

#### find_common_root()

```python
def find_common_root(
    pkgs_or_mods: typing.Union[typing.Tuple[str], typing.List[str]],
) -> pathlib._local.Path
```
Given an arbitrary list of folders and files, this function will use the script mode function to walk up
the filesystem to find the first folder without an init file. If all the folders and files resolve to
the same root folder, then that Path is returned. Otherwise an error is raised.



| Parameter | Type |
|-|-|
| `pkgs_or_mods` | `typing.Union[typing.Tuple[str], typing.List[str]]` |

#### get_registrable_entities()

```python
def get_registrable_entities(
    ctx: flytekit.core.context_manager.FlyteContext,
    options: typing.Optional[flytekit.core.options.Options],
) -> typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]
```
Returns all entities that can be serialized and should be sent over to Flyte backend. This will filter any entities
that are not known to Admin


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |

#### list_packages_and_modules()

```python
def list_packages_and_modules(
    project_root: pathlib._local.Path,
    pkgs_or_mods: typing.List[str],
) -> typing.List[str]
```
This is a helper function that returns the input list of python packages/modules as a dot delinated list
relative to the given project_root.



| Parameter | Type |
|-|-|
| `project_root` | `pathlib._local.Path` |
| `pkgs_or_mods` | `typing.List[str]` |

#### package()

```python
def package(
    serializable_entities: typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]],
    source: str,
    output: str,
    deref_symlinks: bool,
    fast_options: typing.Optional[flytekit.tools.fast_registration.FastPackageOptions],
)
```
Package the given entities and the source code (if fast is enabled) into a package with the given name in output


| Parameter | Type |
|-|-|
| `serializable_entities` | `typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]` |
| `source` | `str` |
| `output` | `str` |
| `deref_symlinks` | `bool` |
| `fast_options` | `typing.Optional[flytekit.tools.fast_registration.FastPackageOptions]` |

#### persist_registrable_entities()

```python
def persist_registrable_entities(
    entities: typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]],
    folder: str,
)
```
For protobuf serializable list of entities, writes a file with the name if the entity and
enumeration order to the specified folder

This function will write to the folder specified the following protobuf types ::
flyteidl.admin.launch_plan_pb2.LaunchPlan
flyteidl.admin.workflow_pb2.WorkflowSpec
flyteidl.admin.task_pb2.TaskSpec

These can be inspected by calling (in the launch plan case) ::
flyte-cli parse-proto -f filename.pb -p flyteidl.admin.launch_plan_pb2.LaunchPlan


| Parameter | Type |
|-|-|
| `entities` | `typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]` |
| `folder` | `str` |

#### print_registration_status()

```python
def print_registration_status(
    i: flytekit.models.core.identifier.Identifier,
    success: bool,
    activation: bool,
    dry_run: bool,
    console_url: str,
    verbosity: int,
)
```
| Parameter | Type |
|-|-|
| `i` | `flytekit.models.core.identifier.Identifier` |
| `success` | `bool` |
| `activation` | `bool` |
| `dry_run` | `bool` |
| `console_url` | `str` |
| `verbosity` | `int` |

#### register()

```python
def register(
    project: str,
    domain: str,
    image_config: flytekit.configuration.ImageConfig,
    output: str,
    destination_dir: str,
    service_account: str,
    raw_data_prefix: str,
    version: typing.Optional[str],
    deref_symlinks: bool,
    package_or_module: typing.Tuple[str],
    remote: flytekit.remote.remote.FlyteRemote,
    copy_style: <enum 'CopyFileDetection'>,
    env: typing.Optional[typing.Dict[str, str]],
    dry_run: bool,
    activate_launchplans: bool,
    skip_errors: bool,
    show_files: bool,
    verbosity: int,
)
```
Temporarily, for fast register, specify both the fast arg as well as copy_style.
fast == True with copy_style == None means use the old fast register tar'ring method.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `image_config` | `flytekit.configuration.ImageConfig` |
| `output` | `str` |
| `destination_dir` | `str` |
| `service_account` | `str` |
| `raw_data_prefix` | `str` |
| `version` | `typing.Optional[str]` |
| `deref_symlinks` | `bool` |
| `package_or_module` | `typing.Tuple[str]` |
| `remote` | `flytekit.remote.remote.FlyteRemote` |
| `copy_style` | `<enum 'CopyFileDetection'>` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `dry_run` | `bool` |
| `activate_launchplans` | `bool` |
| `skip_errors` | `bool` |
| `show_files` | `bool` |
| `verbosity` | `int` |

#### rprint()

```python
def rprint(
    objects: typing.Any,
    sep: str,
    end: str,
    file: typing.Optional[typing.IO[str]],
    flush: bool,
)
```
Print object(s) supplied via positional arguments.
This function has an identical signature to the built-in print.
For more advanced features, see the :class:`~rich.console.Console` class.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `file` | `typing.Optional[typing.IO[str]]` |
| `flush` | `bool` |

#### serialize_and_package()

```python
def serialize_and_package(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    source: str,
    output: str,
    deref_symlinks: bool,
    options: typing.Optional[flytekit.core.options.Options],
    fast_options: typing.Optional[flytekit.tools.fast_registration.FastPackageOptions],
)
```
Fist serialize and then package all entities
Temporarily for fast package, specify both the fast arg as well as copy_style.
fast == True with copy_style == None means use the old fast register tar'ring method.


| Parameter | Type |
|-|-|
| `pkgs` | `typing.List[str]` |
| `settings` | `flytekit.configuration.SerializationSettings` |
| `source` | `str` |
| `output` | `str` |
| `deref_symlinks` | `bool` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |
| `fast_options` | `typing.Optional[flytekit.tools.fast_registration.FastPackageOptions]` |

#### serialize_get_control_plane_entities()

```python
def serialize_get_control_plane_entities(
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
    options: typing.Optional[flytekit.core.options.Options],
    is_registration: bool,
) -> typing.List[typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]]
```
See :py:class:`flytekit.models.core.identifier.ResourceType` to match the trailing index in the file name with the
entity type.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `local_source_root` | `typing.Optional[str]` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |
| `is_registration` | `bool` |

#### serialize_load_only()

```python
def serialize_load_only(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
)
```
See :py:class:`flytekit.models.core.identifier.ResourceType` to match the trailing index in the file name with the
entity type.


| Parameter | Type |
|-|-|
| `pkgs` | `typing.List[str]` |
| `settings` | `flytekit.configuration.SerializationSettings` |
| `local_source_root` | `typing.Optional[str]` |

#### serialize_to_folder()

```python
def serialize_to_folder(
    pkgs: typing.List[str],
    settings: flytekit.configuration.SerializationSettings,
    local_source_root: typing.Optional[str],
    folder: str,
    options: typing.Optional[flytekit.core.options.Options],
)
```
Serialize the given set of python packages to a folder


| Parameter | Type |
|-|-|
| `pkgs` | `typing.List[str]` |
| `settings` | `flytekit.configuration.SerializationSettings` |
| `local_source_root` | `typing.Optional[str]` |
| `folder` | `str` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |

## flytekit.tools.repo.CopyFileDetection

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


## flytekit.tools.repo.FastSerializationSettings

This object hold information about settings necessary to serialize an object so that it can be fast-registered.


```python
class FastSerializationSettings(
    enabled: bool,
    destination_dir: Optional[str],
    distribution_location: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `enabled` | `bool` |
| `destination_dir` | `Optional[str]` |
| `distribution_location` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


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

## flytekit.tools.repo.FlyteContextManager

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

## flytekit.tools.repo.FlyteRemote

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
class FlyteRemote(
    config: Config,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: typing.Optional[bool],
    kwargs,
)
```
Initialize a FlyteRemote object.

:type kwargs: All arguments that can be passed to create the SynchronousFlyteClient. These are usually grpc
parameters, if you want to customize credentials, ssl handling etc.


| Parameter | Type |
|-|-|
| `config` | `Config` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `typing.Optional[bool]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated. |
| [`approve()`](#approve) | . |
| [`auto()`](#auto) |  |
| [`download()`](#download) | Download the data to the specified location. |
| [`execute()`](#execute) | Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity. |
| [`execute_local_launch_plan()`](#execute_local_launch_plan) | Execute a locally defined `LaunchPlan`. |
| [`execute_local_task()`](#execute_local_task) | Execute a @task-decorated function or TaskTemplate task. |
| [`execute_local_workflow()`](#execute_local_workflow) | Execute an @workflow decorated function. |
| [`execute_reference_launch_plan()`](#execute_reference_launch_plan) | Execute a ReferenceLaunchPlan. |
| [`execute_reference_task()`](#execute_reference_task) | Execute a ReferenceTask. |
| [`execute_reference_workflow()`](#execute_reference_workflow) | Execute a ReferenceWorkflow. |
| [`execute_remote_task_lp()`](#execute_remote_task_lp) | Execute a FlyteTask, or FlyteLaunchplan. |
| [`execute_remote_wf()`](#execute_remote_wf) | Execute a FlyteWorkflow. |
| [`fast_package()`](#fast_package) | Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location. |
| [`fast_register_workflow()`](#fast_register_workflow) | Use this method to register a workflow with zip mode. |
| [`fetch_active_launchplan()`](#fetch_active_launchplan) | Returns the active version of the launch plan if it exists or returns None. |
| [`fetch_execution()`](#fetch_execution) | Fetch a workflow execution entity from flyte admin. |
| [`fetch_launch_plan()`](#fetch_launch_plan) | Fetch a launchplan entity from flyte admin. |
| [`fetch_task()`](#fetch_task) | Fetch a task entity from flyte admin. |
| [`fetch_task_lazy()`](#fetch_task_lazy) | Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily. |
| [`fetch_workflow()`](#fetch_workflow) | Fetch a workflow entity from flyte admin. |
| [`fetch_workflow_lazy()`](#fetch_workflow_lazy) | Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily. |
| [`find_launch_plan()`](#find_launch_plan) |  |
| [`find_launch_plan_for_node()`](#find_launch_plan_for_node) |  |
| [`for_endpoint()`](#for_endpoint) |  |
| [`for_sandbox()`](#for_sandbox) |  |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted. |
| [`generate_console_url()`](#generate_console_url) | Generate a Flyteconsole URL for the given Flyte remote endpoint. |
| [`get()`](#get) | General function that works with flyte tiny urls. |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin. |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution. |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) |  |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan. |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin. |
| [`list_signals()`](#list_signals) | . |
| [`list_tasks_by_version()`](#list_tasks_by_version) |  |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities. |
| [`recent_executions()`](#recent_executions) |  |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options. |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode. |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote. |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow. |
| [`reject()`](#reject) | . |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration. |
| [`set_input()`](#set_input) | . |
| [`set_signal()`](#set_signal) | . |
| [`sync()`](#sync) | This function was previously a singledispatchmethod. |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state. |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution. |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state. |
| [`terminate()`](#terminate) | Terminate a workflow execution. |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service. |
| [`wait()`](#wait) | Wait for an execution to finish. |


#### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
)
```
Given a launchplan, activate it, all previous versions are deactivated.


| Parameter | Type |
|-|-|
| `ident` | `Identifier` |

#### approve()

```python
def approve(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    data: typing.Union[LiteralsResolver, Literal, LiteralMap],
    download_to: str,
    recursive: bool,
)
```
Download the data to the specified location. If the data is a LiteralsResolver, LiteralMap and if recursive is
specified, then all file like objects will be recursively downloaded (e.g. FlyteFile/Dir (blob),
StructuredDataset etc).

Note: That it will use your sessions credentials to access the remote location. For sandbox, this should be
automatically configured, assuming you are running sandbox locally. For other environments, you will need to
configure your credentials appropriately.



| Parameter | Type |
|-|-|
| `data` | `typing.Union[LiteralsResolver, Literal, LiteralMap]` |
| `download_to` | `str` |
| `recursive` | `bool` |

#### execute()

```python
def execute(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity.

This method supports:
- ``Flyte{Task, Workflow, LaunchPlan}`` remote module objects.
- ``@task``-decorated functions and ``TaskTemplate`` tasks.
- ``@workflow``-decorated functions.
- ``LaunchPlan`` objects.

For local entities, this code will attempt to find the entity first, and if missing, will compile and register
the object.

Not all arguments are relevant in all circumstances. For example, there's no reason to use the serialization
settings for entities that have already been registered on Admin.



| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_launch_plan()

```python
def execute_local_launch_plan(
    entity: LaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    name: typing.Optional[str],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a locally defined `LaunchPlan`.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `name` | `typing.Optional[str]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_task()

```python
def execute_local_task(
    entity: PythonTask,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a @task-decorated function or TaskTemplate task.



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_workflow()

```python
def execute_local_workflow(
    entity: WorkflowBase,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute an @workflow decorated function.



| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_reference_launch_plan()

```python
def execute_reference_launch_plan(
    entity: ReferenceLaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceLaunchPlan.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceLaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_task()

```python
def execute_reference_task(
    entity: ReferenceTask,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceTask.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_workflow()

```python
def execute_reference_workflow(
    entity: ReferenceWorkflow,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceWorkflow.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_task_lp()

```python
def execute_remote_task_lp(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a FlyteTask, or FlyteLaunchplan.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_wf()

```python
def execute_remote_wf(
    entity: FlyteWorkflow,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a FlyteWorkflow.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `FlyteWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### fast_package()

```python
def fast_package(
    root: os.PathLike,
    deref_symlinks: bool,
    output: str,
    options: typing.Optional[FastPackageOptions],
) -> typing.Tuple[bytes, str]
```
Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location


| Parameter | Type |
|-|-|
| `root` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `output` | `str` |
| `options` | `typing.Optional[FastPackageOptions]` |

#### fast_register_workflow()

```python
def fast_register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
    fast_package_options: typing.Optional[FastPackageOptions],
) -> FlyteWorkflow
```
Use this method to register a workflow with zip mode.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### fetch_active_launchplan()

```python
def fetch_active_launchplan(
    project: str,
    domain: str,
    name: str,
) -> typing.Optional[FlyteLaunchPlan]
```
Returns the active version of the launch plan if it exists or returns None


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_execution()

```python
def fetch_execution(
    project: str,
    domain: str,
    name: str,
) -> FlyteWorkflowExecution
```
Fetch a workflow execution entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_launch_plan()

```python
def fetch_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteLaunchPlan
```
Fetch a launchplan entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task()

```python
def fetch_task(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteTask
```
Fetch a task entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task_lazy()

```python
def fetch_task_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity
```
Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow()

```python
def fetch_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteWorkflow
```
Fetch a workflow entity from flyte admin.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow_lazy()

```python
def fetch_workflow_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity[FlyteWorkflow]
```
Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### find_launch_plan()

```python
def find_launch_plan(
    lp_ref: id_models,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type |
|-|-|
| `lp_ref` | `id_models` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### find_launch_plan_for_node()

```python
def find_launch_plan_for_node(
    node: Node,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type |
|-|-|
| `node` | `Node` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### for_sandbox()

```python
def for_sandbox(
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### generate_console_http_domain()

```python
def generate_console_http_domain()
```
This should generate the domain where console is hosted.

:return:


#### generate_console_url()

```python
def generate_console_url(
    entity: typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan],
)
```
Generate a Flyteconsole URL for the given Flyte remote endpoint.
This will automatically determine if this is an execution or an entity and change the type automatically


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan]` |

#### get()

```python
def get(
    flyte_uri: typing.Optional[str],
) -> typing.Optional[typing.Union[LiteralsResolver, Literal, HTML, bytes]]
```
General function that works with flyte tiny urls. This can return outputs (in the form of LiteralsResolver, or
individual Literals for singular requests), or HTML if passed a deck link, or bytes containing HTML,
if ipython is not available locally.


| Parameter | Type |
|-|-|
| `flyte_uri` | `typing.Optional[str]` |

#### get_domains()

```python
def get_domains()
```
Lists registered domains from flyte admin.

:returns: typing.List[flytekit.models.domain.Domain]


#### get_execution_metrics()

```python
def get_execution_metrics(
    id: WorkflowExecutionIdentifier,
    depth: int,
) -> FlyteExecutionSpan
```
Get the metrics for a given execution.


| Parameter | Type |
|-|-|
| `id` | `WorkflowExecutionIdentifier` |
| `depth` | `int` |

#### get_extra_headers_for_protocol()

```python
def get_extra_headers_for_protocol(
    native_url,
)
```
| Parameter | Type |
|-|-|
| `native_url` |  |

#### launch_backfill()

```python
def launch_backfill(
    project: str,
    domain: str,
    from_date: datetime,
    to_date: datetime,
    launchplan: str,
    launchplan_version: str,
    execution_name: str,
    version: str,
    dry_run: bool,
    execute: bool,
    parallel: bool,
    failure_policy: typing.Optional[WorkflowFailurePolicy],
    overwrite_cache: typing.Optional[bool],
) -> typing.Optional[FlyteWorkflowExecution, FlyteWorkflow, WorkflowBase]
```
Creates and launches a backfill workflow for the given launchplan. If launchplan version is not specified,
then the latest launchplan is retrieved.
The from_date is exclusive and end_date is inclusive and backfill run for all instances in between. ::
-> (start_date - exclusive, end_date inclusive)

If dry_run is specified, the workflow is created and returned.
If execute==False is specified then the workflow is created and registered.
In the last case, the workflow is created, registered and executed.

The `parallel` flag can be used to generate a workflow where all launchplans can be run in parallel. Default
is that execute backfill is run sequentially



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `from_date` | `datetime` |
| `to_date` | `datetime` |
| `launchplan` | `str` |
| `launchplan_version` | `str` |
| `execution_name` | `str` |
| `version` | `str` |
| `dry_run` | `bool` |
| `execute` | `bool` |
| `parallel` | `bool` |
| `failure_policy` | `typing.Optional[WorkflowFailurePolicy]` |
| `overwrite_cache` | `typing.Optional[bool]` |

#### list_projects()

```python
def list_projects(
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
    sort_by: typing.Optional[admin_common_models.Sort],
) -> typing.List[Project]
```
Lists registered projects from flyte admin.



| Parameter | Type |
|-|-|
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |
| `sort_by` | `typing.Optional[admin_common_models.Sort]` |

#### list_signals()

```python
def list_signals(
    execution_name: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: int,
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[Signal]
```
| Parameter | Type |
|-|-|
| `execution_name` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `int` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### list_tasks_by_version()

```python
def list_tasks_by_version(
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
) -> typing.List[FlyteTask]
```
| Parameter | Type |
|-|-|
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |

#### raw_register()

```python
def raw_register(
    cp_entity: FlyteControlPlaneEntity,
    settings: SerializationSettings,
    version: str,
    create_default_launchplan: bool,
    options: Options,
    og_entity: FlyteLocalEntity,
) -> typing.Optional[Identifier]
```
Raw register method, can be used to register control plane entities. Usually if you have a Flyte Entity like a
WorkflowBase, Task, LaunchPlan then use other methods. This should be used only if you have already serialized entities



| Parameter | Type |
|-|-|
| `cp_entity` | `FlyteControlPlaneEntity` |
| `settings` | `SerializationSettings` |
| `version` | `str` |
| `create_default_launchplan` | `bool` |
| `options` | `Options` |
| `og_entity` | `FlyteLocalEntity` |

#### recent_executions()

```python
def recent_executions(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[FlyteWorkflowExecution]
```
| Parameter | Type |
|-|-|
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### register_launch_plan()

```python
def register_launch_plan(
    entity: LaunchPlan,
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteLaunchPlan
```
Register a given launchplan, possibly applying overrides from the provided options. If the underlying workflow
is not already registered, it, along with any underlying entities, will also be registered. If the underlying
workflow does exist (with the given project/domain/version), then only the launchplan will be registered.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### register_script()

```python
def register_script(
    entity: typing.Union[WorkflowBase, PythonTask, LaunchPlan],
    image_config: typing.Optional[ImageConfig],
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    destination_dir: str,
    copy_all: bool,
    default_launch_plan: bool,
    options: typing.Optional[Options],
    source_path: typing.Optional[str],
    module_name: typing.Optional[str],
    envs: typing.Optional[typing.Dict[str, str]],
    fast_package_options: typing.Optional[FastPackageOptions],
) -> typing.Union[FlyteWorkflow, FlyteTask, FlyteLaunchPlan, ReferenceEntity]
```
Use this method to register a workflow via script mode.


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[WorkflowBase, PythonTask, LaunchPlan]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `destination_dir` | `str` |
| `copy_all` | `bool` |
| `default_launch_plan` | `bool` |
| `options` | `typing.Optional[Options]` |
| `source_path` | `typing.Optional[str]` |
| `module_name` | `typing.Optional[str]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### register_task()

```python
def register_task(
    entity: PythonTask,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
) -> FlyteTask
```
Register a qualified task (PythonTask) with Remote
For any conflicting parameters method arguments are regarded as overrides



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |

#### register_workflow()

```python
def register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
) -> FlyteWorkflow
```
Use this method to register a workflow.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |

#### reject()

```python
def reject(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### remote_context()

```python
def remote_context()
```
Context manager with remote-specific configuration.


#### set_input()

```python
def set_input(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project,
    domain,
    python_type,
    literal_type,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` |  |
| `domain` |  |
| `python_type` |  |
| `literal_type` |  |

#### set_signal()

```python
def set_signal(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    python_type: typing.Optional[typing.Type],
    literal_type: typing.Optional[type_models.LiteralType],
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `python_type` | `typing.Optional[typing.Type]` |
| `literal_type` | `typing.Optional[type_models.LiteralType]` |

#### sync()

```python
def sync(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
This function was previously a singledispatchmethod. We've removed that but this function remains
so that we don't break people.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_execution()

```python
def sync_execution(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Sync a FlyteWorkflowExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_node_execution()

```python
def sync_node_execution(
    execution: FlyteNodeExecution,
    node_mapping: typing.Dict[str, FlyteNode],
) -> FlyteNodeExecution
```
Get data backing a node execution. These FlyteNodeExecution objects should've come from Admin with the model
fields already populated correctly. For purposes of the remote experience, we'd like to supplement the object
with some additional fields:
- inputs/outputs
- task/workflow executions, and/or underlying node executions in the case of parent nodes
- TypedInterface (remote wrapper type)

A node can have several different types of executions behind it. That is, the node could've run (perhaps
multiple times because of retries):
- A task
- A static subworkflow
- A dynamic subworkflow (which in turn may have run additional tasks, subwfs, and/or launch plans)
- A launch plan

The data model is complicated, so ascertaining which of these happened is a bit tricky. That logic is
encapsulated in this function.


| Parameter | Type |
|-|-|
| `execution` | `FlyteNodeExecution` |
| `node_mapping` | `typing.Dict[str, FlyteNode]` |

#### sync_task_execution()

```python
def sync_task_execution(
    execution: FlyteTaskExecution,
    entity_interface: typing.Optional[TypedInterface],
) -> FlyteTaskExecution
```
Sync a FlyteTaskExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteTaskExecution` |
| `entity_interface` | `typing.Optional[TypedInterface]` |

#### terminate()

```python
def terminate(
    execution: FlyteWorkflowExecution,
    cause: str,
)
```
Terminate a workflow execution.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `cause` | `str` |

#### upload_file()

```python
def upload_file(
    to_upload: pathlib.Path,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    filename_root: typing.Optional[str],
) -> typing.Tuple[bytes, str]
```
Function will use remote's client to hash and then upload the file using Admin's data proxy service.



| Parameter | Type |
|-|-|
| `to_upload` | `pathlib.Path` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `filename_root` | `typing.Optional[str]` |

#### wait()

```python
def wait(
    execution: FlyteWorkflowExecution,
    timeout: typing.Optional[typing.Union[timedelta, int]],
    poll_interval: typing.Optional[typing.Union[timedelta, int]],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Wait for an execution to finish.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `timeout` | `typing.Optional[typing.Union[timedelta, int]]` |
| `poll_interval` | `typing.Optional[typing.Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `client` |  | {{< multiline >}}Return a SynchronousFlyteClient for additional operations.
{{< /multiline >}} |
| `config` |  | {{< multiline >}}Image config.
{{< /multiline >}} |
| `context` |  |  |
| `default_domain` |  | {{< multiline >}}Default project to use when fetching or executing flyte entities.
{{< /multiline >}} |
| `default_project` |  | {{< multiline >}}Default project to use when fetching or executing flyte entities.
{{< /multiline >}} |
| `file_access` |  | {{< multiline >}}File access provider to use for offloading non-literal inputs/outputs.
{{< /multiline >}} |
| `interactive_mode_enabled` |  | {{< multiline >}}If set to True, the FlyteRemote will pickle the task/workflow.
{{< /multiline >}} |

## flytekit.tools.repo.Identifier

```python
class Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
)
```
| Parameter | Type |
|-|-|
| `resource_type` |  |
| `project` |  |
| `domain` |  |
| `name` |  |
| `version` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> Identifier
```
| Parameter | Type |
|-|-|
| `p` |  |

#### resource_type_name()

```python
def resource_type_name()
```
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
| `domain` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `project` |  |  |
| `resource_type` |  | {{< multiline >}}enum value from ResourceType
{{< /multiline >}} |
| `version` |  |  |

## flytekit.tools.repo.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
default_image (Optional[Image]): The default image to be used as a container for task serialization.
images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
class ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
)
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name. |
| [`auto_default_image()`](#auto_default_image) |  |
| [`create_from()`](#create_from) |  |
| [`find_image()`](#find_image) | Return an image, by name, if it exists. |
| [`from_dict()`](#from_dict) |  |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig. |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
) -> ImageConfig
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
) -> ImageConfig
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
) -> Optional[Image]
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
) -> ~A
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
)
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

#### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
) -> ImageConfig
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

## flytekit.tools.repo.NoSerializableEntitiesError

Common base class for all non-exit exceptions.


## flytekit.tools.repo.Options

These are options that can be configured for a launchplan during registration or overridden during an execution.
For instance two people may want to run the same workflow but have the offloaded data stored in two different
buckets. Or you may want labels or annotations to be different. This object is used when launching an execution
in a Flyte backend, and also when registering launch plans.



```python
class Options(
    labels: typing.Optional[flytekit.models.common.Labels],
    annotations: typing.Optional[flytekit.models.common.Annotations],
    raw_output_data_config: typing.Optional[flytekit.models.common.RawOutputDataConfig],
    security_context: typing.Optional[flytekit.models.security.SecurityContext],
    max_parallelism: typing.Optional[int],
    notifications: typing.Optional[typing.List[flytekit.models.common.Notification]],
    disable_notifications: typing.Optional[bool],
    overwrite_cache: typing.Optional[bool],
)
```
| Parameter | Type |
|-|-|
| `labels` | `typing.Optional[flytekit.models.common.Labels]` |
| `annotations` | `typing.Optional[flytekit.models.common.Annotations]` |
| `raw_output_data_config` | `typing.Optional[flytekit.models.common.RawOutputDataConfig]` |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` |
| `max_parallelism` | `typing.Optional[int]` |
| `notifications` | `typing.Optional[typing.List[flytekit.models.common.Notification]]` |
| `disable_notifications` | `typing.Optional[bool]` |
| `overwrite_cache` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`default_from()`](#default_from) |  |


#### default_from()

```python
def default_from(
    k8s_service_account: typing.Optional[str],
    raw_data_prefix: typing.Optional[str],
) -> Options
```
| Parameter | Type |
|-|-|
| `k8s_service_account` | `typing.Optional[str]` |
| `raw_data_prefix` | `typing.Optional[str]` |

## flytekit.tools.repo.Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.


```python
class Path(
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
| [`absolute()`](#absolute) | Return an absolute version of this path. |
| [`as_posix()`](#as_posix) | Return the string representation of the path with forward (/). |
| [`as_uri()`](#as_uri) | Return the path as a URI. |
| [`chmod()`](#chmod) | Change the permissions of the path, like os. |
| [`cwd()`](#cwd) | Return a new path pointing to the current working directory. |
| [`exists()`](#exists) | Whether this path exists. |
| [`expanduser()`](#expanduser) | Return a new path with expanded ~ and ~user constructs. |
| [`from_uri()`](#from_uri) | Return a new path from the given 'file' URI. |
| [`full_match()`](#full_match) | Return True if this path matches the given glob-style pattern. |
| [`glob()`](#glob) | Iterate over this subtree and yield all existing files (of any. |
| [`group()`](#group) | Return the group name of the file gid. |
| [`hardlink_to()`](#hardlink_to) | Make this path a hard link pointing to the same file as *target*. |
| [`home()`](#home) | Return a new path pointing to expanduser('~'). |
| [`is_absolute()`](#is_absolute) | True if the path is absolute (has both a root and, if applicable,. |
| [`is_block_device()`](#is_block_device) | Whether this path is a block device. |
| [`is_char_device()`](#is_char_device) | Whether this path is a character device. |
| [`is_dir()`](#is_dir) | Whether this path is a directory. |
| [`is_fifo()`](#is_fifo) | Whether this path is a FIFO. |
| [`is_file()`](#is_file) | Whether this path is a regular file (also True for symlinks pointing. |
| [`is_junction()`](#is_junction) | Whether this path is a junction. |
| [`is_mount()`](#is_mount) | Check if this path is a mount point. |
| [`is_relative_to()`](#is_relative_to) | Return True if the path is relative to another path or False. |
| [`is_reserved()`](#is_reserved) | Return True if the path contains one of the special names reserved. |
| [`is_socket()`](#is_socket) | Whether this path is a socket. |
| [`is_symlink()`](#is_symlink) | Whether this path is a symbolic link. |
| [`iterdir()`](#iterdir) | Yield path objects of the directory contents. |
| [`joinpath()`](#joinpath) | Combine this path with one or several arguments, and return a. |
| [`lchmod()`](#lchmod) | Like chmod(), except if the path points to a symlink, the symlink's. |
| [`lstat()`](#lstat) | Like stat(), except if the path points to a symlink, the symlink's. |
| [`match()`](#match) | Return True if this path matches the given pattern. |
| [`mkdir()`](#mkdir) | Create a new directory at this given path. |
| [`open()`](#open) | Open the file pointed to by this path and return a file object, as. |
| [`owner()`](#owner) | Return the login name of the file owner. |
| [`read_bytes()`](#read_bytes) | Open the file in bytes mode, read it, and close the file. |
| [`read_text()`](#read_text) | Open the file in text mode, read it, and close the file. |
| [`readlink()`](#readlink) | Return the path to which the symbolic link points. |
| [`relative_to()`](#relative_to) | Return the relative path to another path identified by the passed. |
| [`rename()`](#rename) | Rename this path to the target path. |
| [`replace()`](#replace) | Rename this path to the target path, overwriting if that path exists. |
| [`resolve()`](#resolve) | Make the path absolute, resolving all symlinks on the way and also. |
| [`rglob()`](#rglob) | Recursively yield all existing files (of any kind, including. |
| [`rmdir()`](#rmdir) | Remove this directory. |
| [`samefile()`](#samefile) | Return whether other_path is the same or not as this file. |
| [`stat()`](#stat) | Return the result of the stat() system call on this path, like. |
| [`symlink_to()`](#symlink_to) | Make this path a symlink pointing to the target path. |
| [`touch()`](#touch) | Create this file with the given access mode, if it doesn't exist. |
| [`unlink()`](#unlink) | Remove this file or link. |
| [`walk()`](#walk) | Walk the directory tree from this directory, similar to os. |
| [`with_name()`](#with_name) | Return a new path with the file name changed. |
| [`with_segments()`](#with_segments) | Construct a new path object from any number of path-like objects. |
| [`with_stem()`](#with_stem) | Return a new path with the stem changed. |
| [`with_suffix()`](#with_suffix) | Return a new path with the file suffix changed. |
| [`write_bytes()`](#write_bytes) | Open the file in bytes mode, write to it, and close the file. |
| [`write_text()`](#write_text) | Open the file in text mode, write to it, and close the file. |


#### absolute()

```python
def absolute()
```
Return an absolute version of this path
No normalization or symlink resolution is performed.

Use resolve() to resolve symlinks and remove '..' segments.


#### as_posix()

```python
def as_posix()
```
Return the string representation of the path with forward (/)
slashes.


#### as_uri()

```python
def as_uri()
```
Return the path as a URI.


#### chmod()

```python
def chmod(
    mode,
    follow_symlinks,
)
```
Change the permissions of the path, like os.chmod().


| Parameter | Type |
|-|-|
| `mode` |  |
| `follow_symlinks` |  |

#### cwd()

```python
def cwd()
```
Return a new path pointing to the current working directory.


#### exists()

```python
def exists(
    follow_symlinks,
)
```
Whether this path exists.

This method normally follows symlinks; to check whether a symlink exists,
add the argument follow_symlinks=False.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### expanduser()

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
(as returned by os.path.expanduser)


#### from_uri()

```python
def from_uri(
    uri,
)
```
Return a new path from the given 'file' URI.


| Parameter | Type |
|-|-|
| `uri` |  |

#### full_match()

```python
def full_match(
    pattern,
    case_sensitive,
)
```
Return True if this path matches the given glob-style pattern. The
pattern is matched against the entire path.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### glob()

```python
def glob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### group()

```python
def group(
    follow_symlinks,
)
```
Return the group name of the file gid.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### hardlink_to()

```python
def hardlink_to(
    target,
)
```
Make this path a hard link pointing to the same file as *target*.

Note the order of arguments (self, target) is the reverse of os.link's.


| Parameter | Type |
|-|-|
| `target` |  |

#### home()

```python
def home()
```
Return a new path pointing to expanduser('~').



#### is_absolute()

```python
def is_absolute()
```
True if the path is absolute (has both a root and, if applicable,
a drive).


#### is_block_device()

```python
def is_block_device()
```
Whether this path is a block device.


#### is_char_device()

```python
def is_char_device()
```
Whether this path is a character device.


#### is_dir()

```python
def is_dir(
    follow_symlinks,
)
```
Whether this path is a directory.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_fifo()

```python
def is_fifo()
```
Whether this path is a FIFO.


#### is_file()

```python
def is_file(
    follow_symlinks,
)
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### is_junction()

```python
def is_junction()
```
Whether this path is a junction.


#### is_mount()

```python
def is_mount()
```
Check if this path is a mount point


#### is_relative_to()

```python
def is_relative_to(
    other,
    _deprecated,
)
```
Return True if the path is relative to another path or False.



| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |

#### is_reserved()

```python
def is_reserved()
```
Return True if the path contains one of the special names reserved
by the system, if any.


#### is_socket()

```python
def is_socket()
```
Whether this path is a socket.


#### is_symlink()

```python
def is_symlink()
```
Whether this path is a symbolic link.


#### iterdir()

```python
def iterdir()
```
Yield path objects of the directory contents.

The children are yielded in arbitrary order, and the
special entries '.' and '..' are not included.


#### joinpath()

```python
def joinpath(
    pathsegments,
)
```
Combine this path with one or several arguments, and return a
new path representing either a subpath (if all arguments are relative
paths) or a totally different path (if one of the arguments is
anchored).


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### lchmod()

```python
def lchmod(
    mode,
)
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.


| Parameter | Type |
|-|-|
| `mode` |  |

#### lstat()

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.


#### match()

```python
def match(
    path_pattern,
    case_sensitive,
)
```
Return True if this path matches the given pattern. If the pattern is
relative, matching is done from the right; otherwise, the entire path
is matched. The recursive wildcard '**' is *not* supported by this
method.


| Parameter | Type |
|-|-|
| `path_pattern` |  |
| `case_sensitive` |  |

#### mkdir()

```python
def mkdir(
    mode,
    parents,
    exist_ok,
)
```
Create a new directory at this given path.


| Parameter | Type |
|-|-|
| `mode` |  |
| `parents` |  |
| `exist_ok` |  |

#### open()

```python
def open(
    mode,
    buffering,
    encoding,
    errors,
    newline,
)
```
Open the file pointed to by this path and return a file object, as
the built-in open() function does.


| Parameter | Type |
|-|-|
| `mode` |  |
| `buffering` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### owner()

```python
def owner(
    follow_symlinks,
)
```
Return the login name of the file owner.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### read_bytes()

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.


#### read_text()

```python
def read_text(
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, read it, and close the file.


| Parameter | Type |
|-|-|
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### readlink()

```python
def readlink()
```
Return the path to which the symbolic link points.


#### relative_to()

```python
def relative_to(
    other,
    _deprecated,
    walk_up,
)
```
Return the relative path to another path identified by the passed
arguments.  If the operation is not possible (because this is not
related to the other path), raise ValueError.

The *walk_up* parameter controls whether `..` may be used to resolve
the path.


| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |
| `walk_up` |  |

#### rename()

```python
def rename(
    target,
)
```
Rename this path to the target path.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### replace()

```python
def replace(
    target,
)
```
Rename this path to the target path, overwriting if that path exists.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### resolve()

```python
def resolve(
    strict,
)
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it.


| Parameter | Type |
|-|-|
| `strict` |  |

#### rglob()

```python
def rglob(
    pattern,
    case_sensitive,
    recurse_symlinks,
)
```
Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |
| `recurse_symlinks` |  |

#### rmdir()

```python
def rmdir()
```
Remove this directory.  The directory must be empty.


#### samefile()

```python
def samefile(
    other_path,
)
```
Return whether other_path is the same or not as this file
(as returned by os.path.samefile()).


| Parameter | Type |
|-|-|
| `other_path` |  |

#### stat()

```python
def stat(
    follow_symlinks,
)
```
Return the result of the stat() system call on this path, like
os.stat() does.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### symlink_to()

```python
def symlink_to(
    target,
    target_is_directory,
)
```
Make this path a symlink pointing to the target path.
Note the order of arguments (link, target) is the reverse of os.symlink.


| Parameter | Type |
|-|-|
| `target` |  |
| `target_is_directory` |  |

#### touch()

```python
def touch(
    mode,
    exist_ok,
)
```
Create this file with the given access mode, if it doesn't exist.


| Parameter | Type |
|-|-|
| `mode` |  |
| `exist_ok` |  |

#### unlink()

```python
def unlink(
    missing_ok,
)
```
Remove this file or link.
If the path is a directory, use rmdir() instead.


| Parameter | Type |
|-|-|
| `missing_ok` |  |

#### walk()

```python
def walk(
    top_down,
    on_error,
    follow_symlinks,
)
```
Walk the directory tree from this directory, similar to os.walk().


| Parameter | Type |
|-|-|
| `top_down` |  |
| `on_error` |  |
| `follow_symlinks` |  |

#### with_name()

```python
def with_name(
    name,
)
```
Return a new path with the file name changed.


| Parameter | Type |
|-|-|
| `name` |  |

#### with_segments()

```python
def with_segments(
    pathsegments,
)
```
Construct a new path object from any number of path-like objects.
Subclasses may override this method to customize how new path objects
are created from methods like `iterdir()`.


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### with_stem()

```python
def with_stem(
    stem,
)
```
Return a new path with the stem changed.


| Parameter | Type |
|-|-|
| `stem` |  |

#### with_suffix()

```python
def with_suffix(
    suffix,
)
```
Return a new path with the file suffix changed.  If the path
has no suffix, add given suffix.  If the given suffix is an empty
string, remove the suffix from the path.


| Parameter | Type |
|-|-|
| `suffix` |  |

#### write_bytes()

```python
def write_bytes(
    data,
)
```
Open the file in bytes mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |

#### write_text()

```python
def write_text(
    data,
    encoding,
    errors,
    newline,
)
```
Open the file in text mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `anchor` |  | {{< multiline >}}The concatenation of the drive and root, or ''.
{{< /multiline >}} |
| `drive` |  | {{< multiline >}}The drive prefix (letter or UNC path), if any.
{{< /multiline >}} |
| `name` |  | {{< multiline >}}The final path component, if any.
{{< /multiline >}} |
| `parent` |  | {{< multiline >}}The logical parent of the path.
{{< /multiline >}} |
| `parents` |  | {{< multiline >}}A sequence of this path's logical parents.
{{< /multiline >}} |
| `parts` |  | {{< multiline >}}An object providing sequence-like access to the
components in the filesystem path.
{{< /multiline >}} |
| `root` |  | {{< multiline >}}The root of the path, if any.
{{< /multiline >}} |
| `stem` |  | {{< multiline >}}The final path component, minus its last suffix.
{{< /multiline >}} |
| `suffix` |  | {{< multiline >}}The final component's last suffix, if any.

This includes the leading period. For example: '.txt'
{{< /multiline >}} |
| `suffixes` |  | {{< multiline >}}A list of the final component's suffixes, if any.

These include the leading periods. For example: ['.tar', '.gz']
{{< /multiline >}} |

## flytekit.tools.repo.RegistrationSkipped

RegistrationSkipped error is raised when trying to register an entity that is not registrable.


## flytekit.tools.repo.SerializationSettings

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

