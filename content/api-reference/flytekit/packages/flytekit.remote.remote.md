---
title: flytekit.remote.remote
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.remote


This module provides the ``FlyteRemote`` object, which is the end-user's main starting point for interacting
with a Flyte backend in an interactive and programmatic way. This of this experience as kind of like the web UI
but in Python object form.

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrayNodeMapTask`](.././flytekit.remote.remote#flytekitremoteremotearraynodemaptask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`Artifact`](.././flytekit.remote.remote#flytekitremoteremoteartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`BranchNode`](.././flytekit.remote.remote#flytekitremoteremotebranchnode) |  |
| [`ClusterAssignment`](.././flytekit.remote.remote#flytekitremoteremoteclusterassignment) |  |
| [`Config`](.././flytekit.remote.remote#flytekitremoteremoteconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`ConfigFile`](.././flytekit.remote.remote#flytekitremoteremoteconfigfile) |  |
| [`CopyFileDetection`](.././flytekit.remote.remote#flytekitremoteremotecopyfiledetection) | Create a collection of name/value pairs. |
| [`CoreNode`](.././flytekit.remote.remote#flytekitremoteremotecorenode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`DataConfig`](.././flytekit.remote.remote#flytekitremoteremotedataconfig) | Any data storage specific configuration. |
| [`Domain`](.././flytekit.remote.remote#flytekitremoteremotedomain) | Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |
| [`ExecutionClusterLabel`](.././flytekit.remote.remote#flytekitremoteremoteexecutionclusterlabel) |  |
| [`ExecutionMetadata`](.././flytekit.remote.remote#flytekitremoteremoteexecutionmetadata) |  |
| [`ExecutionSpec`](.././flytekit.remote.remote#flytekitremoteremoteexecutionspec) |  |
| [`FastPackageOptions`](.././flytekit.remote.remote#flytekitremoteremotefastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |
| [`FastSerializationSettings`](.././flytekit.remote.remote#flytekitremoteremotefastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`FileAccessProvider`](.././flytekit.remote.remote#flytekitremoteremotefileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`FlyteContext`](.././flytekit.remote.remote#flytekitremoteremoteflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.remote.remote#flytekitremoteremoteflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteExecutionSpan`](.././flytekit.remote.remote#flytekitremoteremoteflyteexecutionspan) |  |
| [`FlyteLaunchPlan`](.././flytekit.remote.remote#flytekitremoteremoteflytelaunchplan) | A class encapsulating a remote Flyte launch plan. |
| [`FlyteNode`](.././flytekit.remote.remote#flytekitremoteremoteflytenode) | A class encapsulating a remote Flyte node. |
| [`FlyteNodeExecution`](.././flytekit.remote.remote#flytekitremoteremoteflytenodeexecution) | A class encapsulating a node execution being run on a Flyte remote backend. |
| [`FlyteRemote`](.././flytekit.remote.remote#flytekitremoteremoteflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`FlyteTask`](.././flytekit.remote.remote#flytekitremoteremoteflytetask) | A class encapsulating a remote Flyte task. |
| [`FlyteTaskExecution`](.././flytekit.remote.remote#flytekitremoteremoteflytetaskexecution) | A class encapsulating a task execution being run on a Flyte remote backend. |
| [`FlyteTaskNode`](.././flytekit.remote.remote#flytekitremoteremoteflytetasknode) | A class encapsulating a task that a Flyte node needs to execute. |
| [`FlyteWorkflow`](.././flytekit.remote.remote#flytekitremoteremoteflyteworkflow) | A class encapsulating a remote Flyte workflow. |
| [`FlyteWorkflowExecution`](.././flytekit.remote.remote#flytekitremoteremoteflyteworkflowexecution) | A class encapsulating a workflow execution being run on a Flyte remote backend. |
| [`Identifier`](.././flytekit.remote.remote#flytekitremoteremoteidentifier) |  |
| [`ImageConfig`](.././flytekit.remote.remote#flytekitremoteremoteimageconfig) | We recommend you to use ImageConfig. |
| [`ImageSpec`](.././flytekit.remote.remote#flytekitremoteremoteimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`LaunchPlan`](.././flytekit.remote.remote#flytekitremoteremotelaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`LaunchPlanState`](.././flytekit.remote.remote#flytekitremoteremotelaunchplanstate) |  |
| [`LazyEntity`](.././flytekit.remote.remote#flytekitremoteremotelazyentity) | Fetches the entity when the entity is called or when the entity is retrieved. |
| [`Literal`](.././flytekit.remote.remote#flytekitremoteremoteliteral) |  |
| [`LiteralMap`](.././flytekit.remote.remote#flytekitremoteremoteliteralmap) |  |
| [`LiteralsResolver`](.././flytekit.remote.remote#flytekitremoteremoteliteralsresolver) | LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation. |
| [`NamedEntityIdentifier`](.././flytekit.remote.remote#flytekitremoteremotenamedentityidentifier) |  |
| [`Node`](.././flytekit.remote.remote#flytekitremoteremotenode) |  |
| [`NodeExecutionGetDataResponse`](.././flytekit.remote.remote#flytekitremoteremotenodeexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`NodeMetadata`](.././flytekit.remote.remote#flytekitremoteremotenodemetadata) |  |
| [`NotificationList`](.././flytekit.remote.remote#flytekitremoteremotenotificationlist) |  |
| [`Options`](.././flytekit.remote.remote#flytekitremoteremoteoptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`OrderedDict`](.././flytekit.remote.remote#flytekitremoteremoteordereddict) | Dictionary that remembers insertion order. |
| [`PickledEntity`](.././flytekit.remote.remote#flytekitremoteremotepickledentity) | Represents the structure of the pickled object stored in the . |
| [`PickledEntityMetadata`](.././flytekit.remote.remote#flytekitremoteremotepickledentitymetadata) | Metadata for a pickled entity containing version information. |
| [`Progress`](.././flytekit.remote.remote#flytekitremoteremoteprogress) | Renders an auto-updating progress bar(s). |
| [`Project`](.././flytekit.remote.remote#flytekitremoteremoteproject) |  |
| [`PythonAutoContainerTask`](.././flytekit.remote.remote#flytekitremoteremotepythonautocontainertask) | A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`PythonFunctionTask`](.././flytekit.remote.remote#flytekitremoteremotepythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`PythonFunctionWorkflow`](.././flytekit.remote.remote#flytekitremoteremotepythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`PythonTask`](.././flytekit.remote.remote#flytekitremoteremotepythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`ReferenceEntity`](.././flytekit.remote.remote#flytekitremoteremotereferenceentity) |  |
| [`ReferenceLaunchPlan`](.././flytekit.remote.remote#flytekitremoteremotereferencelaunchplan) | A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. |
| [`ReferenceSpec`](.././flytekit.remote.remote#flytekitremoteremotereferencespec) |  |
| [`ReferenceTask`](.././flytekit.remote.remote#flytekitremoteremotereferencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`ReferenceWorkflow`](.././flytekit.remote.remote#flytekitremoteremotereferenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`RemoteEntity`](.././flytekit.remote.remote#flytekitremoteremoteremoteentity) | Helper class that provides a standard way to create an ABC using. |
| [`ResolvedIdentifiers`](.././flytekit.remote.remote#flytekitremoteremoteresolvedidentifiers) |  |
| [`ResourceType`](.././flytekit.remote.remote#flytekitremoteremoteresourcetype) |  |
| [`SerializationSettings`](.././flytekit.remote.remote#flytekitremoteremoteserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`Signal`](.././flytekit.remote.remote#flytekitremoteremotesignal) | A ProtocolMessage. |
| [`SignalIdentifier`](.././flytekit.remote.remote#flytekitremoteremotesignalidentifier) |  |
| [`SignalListRequest`](.././flytekit.remote.remote#flytekitremoteremotesignallistrequest) | A ProtocolMessage. |
| [`SignalSetRequest`](.././flytekit.remote.remote#flytekitremoteremotesignalsetrequest) | A ProtocolMessage. |
| [`Sort`](.././flytekit.remote.remote#flytekitremoteremotesort) |  |
| [`SynchronousFlyteClient`](.././flytekit.remote.remote#flytekitremoteremotesynchronousflyteclient) | This is a low-level client that users can use to make direct gRPC service calls to the control plane. |
| [`TextColumn`](.././flytekit.remote.remote#flytekitremoteremotetextcolumn) | A column containing text. |
| [`TimeElapsedColumn`](.././flytekit.remote.remote#flytekitremoteremotetimeelapsedcolumn) | Renders time elapsed. |
| [`TypeEngine`](.././flytekit.remote.remote#flytekitremoteremotetypeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypedInterface`](.././flytekit.remote.remote#flytekitremoteremotetypedinterface) |  |
| [`WorkflowBase`](.././flytekit.remote.remote#flytekitremoteremoteworkflowbase) |  |
| [`WorkflowExecutionGetDataResponse`](.././flytekit.remote.remote#flytekitremoteremoteworkflowexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`WorkflowExecutionIdentifier`](.././flytekit.remote.remote#flytekitremoteremoteworkflowexecutionidentifier) |  |
| [`WorkflowFailurePolicy`](.././flytekit.remote.remote#flytekitremoteremoteworkflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`datetime`](.././flytekit.remote.remote#flytekitremoteremotedatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timedelta`](.././flytekit.remote.remote#flytekitremoteremotetimedelta) | Difference between two datetime values. |

### Errors

| Exception | Description |
|-|-|
| [`FlyteAssertion`](.././flytekit.remote.remote#flytekitremoteremoteflyteassertion) | Assertion failed. |
| [`FlyteEntityAlreadyExistsException`](.././flytekit.remote.remote#flytekitremoteremoteflyteentityalreadyexistsexception) | Assertion failed. |
| [`FlyteEntityNotExistException`](.././flytekit.remote.remote#flytekitremoteremoteflyteentitynotexistexception) | Assertion failed. |
| [`FlyteValueException`](.././flytekit.remote.remote#flytekitremoteremoteflytevalueexception) | Inappropriate argument value (of correct type). |
| [`RegistrationSkipped`](.././flytekit.remote.remote#flytekitremoteremoteregistrationskipped) | RegistrationSkipped error is raised when trying to register an entity that is not registrable. |

### Methods

| Method | Description |
|-|-|
| [`_find_project_root()`](#_find_project_root) | Find the root of the project. |
| [`_get_entity_identifier()`](#_get_entity_identifier) |  |
| [`_get_git_repo_url()`](#_get_git_repo_url) | Get git repo URL from remote. |
| [`_get_latest_version()`](#_get_latest_version) |  |
| [`_get_pickled_target_dict()`](#_get_pickled_target_dict) | Get the pickled target dictionary for the entity. |
| [`asdict()`](#asdict) | Return the fields of a dataclass instance as a new dictionary mapping. |
| [`b64encode()`](#b64encode) | Encode the bytes-like object s using Base64 and return a bytes object. |
| [`compress_scripts()`](#compress_scripts) | Compresses the single script while maintaining the folder structure for that file. |
| [`create_backfill_workflow()`](#create_backfill_workflow) | Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`dc_replace()`](#dc_replace) | Return a new object replacing specified fields with new values. |
| [`download_literal()`](#download_literal) | Download a single literal to a file, if it is a blob or structured dataset. |
| [`extract_task_module()`](#extract_task_module) | Returns the task-name, absolute module and the string name of the callable. |
| [`fast_package()`](#fast_package) | Takes a source directory and packages everything not covered by common ignores into a tarball. |
| [`get_all_modules()`](#get_all_modules) | Import python file with module_name in source_path and return all modules. |
| [`get_flyte_fs()`](#get_flyte_fs) |  |
| [`get_serializable()`](#get_serializable) | The flytekit authoring code produces objects representing Flyte entities (tasks, workflows, etc. |
| [`get_serializable_launch_plan()`](#get_serializable_launch_plan) | . |
| [`ipython_check()`](#ipython_check) | Check if interface is launching from iPython (not colab). |
| [`is_display_progress_enabled()`](#is_display_progress_enabled) |  |
| [`iterate_node_executions()`](#iterate_node_executions) | This returns a generator for node executions. |
| [`iterate_task_executions()`](#iterate_task_executions) | This returns a generator for task executions, given a node execution identifier. |
| [`run_sync()`](#run_sync) | This should be called from synchronous functions to run an async function. |
| [`strict_type_hint_matching()`](#strict_type_hint_matching) | Try to be smarter about guessing the type of the input (and hence the transformer). |


### Variables

| Property | Type | Description |
|-|-|-|
| `LATEST_VERSION_STR` | `str` |  |
| `MOST_RECENT_FIRST` | `Sort` |  |
| `PICKLE_FILE_PATH` | `str` |  |
| `annotations` | `_Feature` |  |
| `default_notebook_task_resolver` | `DefaultNotebookTaskResolver` |  |
| `developer_logger` | `Logger` |  |
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

#### _get_entity_identifier()

```python
def _get_entity_identifier(
    list_entities_method: typing.Callable,
    resource_type: int,
    project: str,
    domain: str,
    name: str,
    version: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `list_entities_method` | `typing.Callable` |
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `typing.Optional[str]` |

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

#### _get_latest_version()

```python
def _get_latest_version(
    list_entities_method: typing.Callable,
    project: str,
    domain: str,
    name: str,
)
```
| Parameter | Type |
|-|-|
| `list_entities_method` | `typing.Callable` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### _get_pickled_target_dict()

```python
def _get_pickled_target_dict(
    root_entity: typing.Union[WorkflowBase, PythonTask],
) -> typing.Tuple[bytes, PickledEntity]
```
Get the pickled target dictionary for the entity.


| Parameter | Type |
|-|-|
| `root_entity` | `typing.Union[WorkflowBase, PythonTask]` |

#### asdict()

```python
def asdict(
    obj,
    dict_factory,
)
```
Return the fields of a dataclass instance as a new dictionary mapping
field names to field values.

Example usage::

@dataclass
class C:
x: int
y: int

c = C(1, 2)
assert asdict(c) == {'x': 1, 'y': 2}

If given, 'dict_factory' will be used instead of built-in dict.
The function applies recursively to field values that are
dataclass instances. This will also look into built-in containers:
tuples, lists, and dicts. Other objects are copied with 'copy.deepcopy()'.


| Parameter | Type |
|-|-|
| `obj` |  |
| `dict_factory` |  |

#### b64encode()

```python
def b64encode(
    s,
    altchars,
)
```
Encode the bytes-like object s using Base64 and return a bytes object.

Optional altchars should be a byte string of length 2 which specifies an
alternative alphabet for the '+' and '/' characters.  This allows an
application to e.g. generate url or filesystem safe Base64 strings.


| Parameter | Type |
|-|-|
| `s` |  |
| `altchars` |  |

#### compress_scripts()

```python
def compress_scripts(
    source_path: str,
    destination: str,
    modules: List[ModuleType],
)
```
Compresses the single script while maintaining the folder structure for that file.

For example, given the follow file structure:
.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       ├── unused_example.py
│       └── __init__.py

Let's say you want to compress `example.py` imports `another_example.py`. And `another_example.py`
imports on `yet_another_example.py`. This will  produce a tar file that contains only that
file alongside with the folder structure, i.e.:

.
├── flyte
│   ├── __init__.py
│   └── workflows
│       ├── example.py
│       ├── another_example.py
│       ├── yet_another_example.py
│       └── __init__.py


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `destination` | `str` |
| `modules` | `List[ModuleType]` |

#### create_backfill_workflow()

```python
def create_backfill_workflow(
    start_date: datetime.datetime,
    end_date: datetime.datetime,
    for_lp: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan],
    parallel: bool,
    per_node_timeout: datetime.timedelta,
    per_node_retries: int,
    failure_policy: typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy],
) -> typing.Tuple[flytekit.core.workflow.WorkflowBase, datetime.datetime, datetime.datetime]
```
Generates a new imperative workflow for the launchplan that can be used to backfill the given launchplan.
This can only be used to generate  backfilling workflow only for schedulable launchplans

the Backfill plan is generated as (start_date - exclusive, end_date inclusive)

.. code-block:: python
:caption: Correct usage for dates example

lp = Launchplan.get_or_create(...)
start_date = datetime.datetime(2023, 1, 1)
end_date =  start_date + datetime.timedelta(days=10)
wf = create_backfill_workflow(start_date, end_date, for_lp=lp)


.. code-block:: python
:caption: Incorrect date example

wf = create_backfill_workflow(end_date, start_date, for_lp=lp) # end_date is before start_date
# OR
wf = create_backfill_workflow(start_date, start_date, for_lp=lp) # start and end date are same




| Parameter | Type |
|-|-|
| `start_date` | `datetime.datetime` |
| `end_date` | `datetime.datetime` |
| `for_lp` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.remote.entities.FlyteLaunchPlan]` |
| `parallel` | `bool` |
| `per_node_timeout` | `datetime.timedelta` |
| `per_node_retries` | `int` |
| `failure_policy` | `typing.Optional[flytekit.core.workflow.WorkflowFailurePolicy]` |

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

#### dc_replace()

```python
def dc_replace(
    obj,
    changes,
)
```
Return a new object replacing specified fields with new values.

This is especially useful for frozen classes.  Example usage::

@dataclass(frozen=True)
class C:
x: int
y: int

c = C(1, 2)
c1 = replace(c, x=3)
assert c1.x == 3 and c1.y == 2


| Parameter | Type |
|-|-|
| `obj` |  |
| `changes` |  |

#### download_literal()

```python
def download_literal(
    file_access: flytekit.core.data_persistence.FileAccessProvider,
    var: str,
    data: flytekit.models.literals.Literal,
    download_to: typing.Optional[pathlib._local.Path],
)
```
Download a single literal to a file, if it is a blob or structured dataset.


| Parameter | Type |
|-|-|
| `file_access` | `flytekit.core.data_persistence.FileAccessProvider` |
| `var` | `str` |
| `data` | `flytekit.models.literals.Literal` |
| `download_to` | `typing.Optional[pathlib._local.Path]` |

#### extract_task_module()

```python
def extract_task_module(
    f: typing.Union[typing.Callable, flytekit.core.tracker.TrackedInstance],
) -> typing.Tuple[str, str, str, str]
```
Returns the task-name, absolute module and the string name of the callable.


| Parameter | Type |
|-|-|
| `f` | `typing.Union[typing.Callable, flytekit.core.tracker.TrackedInstance]` |

#### fast_package()

```python
def fast_package(
    source: os.PathLike,
    output_dir: os.PathLike,
    deref_symlinks: bool,
    options: Optional[FastPackageOptions],
) -> os.PathLike
```
Takes a source directory and packages everything not covered by common ignores into a tarball
named after a hexdigest of the included files.


| Parameter | Type |
|-|-|
| `source` | `os.PathLike` |
| `output_dir` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `options` | `Optional[FastPackageOptions]` |

#### get_all_modules()

```python
def get_all_modules(
    source_path: str,
    module_name: Optional[str],
) -> List[ModuleType]
```
Import python file with module_name in source_path and return all modules.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `module_name` | `Optional[str]` |

#### get_flyte_fs()

```python
def get_flyte_fs(
    remote: FlyteRemote,
) -> typing.Type[FlyteFS]
```
| Parameter | Type |
|-|-|
| `remote` | `FlyteRemote` |

#### get_serializable()

```python
def get_serializable(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode],
    options: typing.Optional[flytekit.core.options.Options],
) -> typing.Union[flytekit.models.task.TaskSpec, flytekit.models.launch_plan.LaunchPlan, flytekit.models.admin.workflow.WorkflowSpec, flytekit.models.core.workflow.Node, flytekit.models.core.workflow.BranchNode, flytekit.models.core.workflow.ArrayNode]
```
The flytekit authoring code produces objects representing Flyte entities (tasks, workflows, etc.). In order to
register these, they need to be converted into objects that Flyte Admin understands (the IDL objects basically, but
this function currently translates to the layer above (e.g. SdkTask) - this will be changed to the IDL objects
directly in the future).



| Parameter | Type |
|-|-|
| `entity_mapping` | `collections.OrderedDict` |
| `settings` | `flytekit.configuration.SerializationSettings` |
| `entity` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.condition.BranchNode, flytekit.core.node.Node, flytekit.core.launch_plan.LaunchPlan, flytekit.core.workflow.WorkflowBase, flytekit.core.workflow.ReferenceWorkflow, flytekit.core.task.ReferenceTask, flytekit.core.launch_plan.ReferenceLaunchPlan, flytekit.core.reference_entity.ReferenceEntity, flytekit.core.array_node.ArrayNode]` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |

#### get_serializable_launch_plan()

```python
def get_serializable_launch_plan(
    entity_mapping: collections.OrderedDict,
    settings: flytekit.configuration.SerializationSettings,
    entity: flytekit.core.launch_plan.LaunchPlan,
    recurse_downstream: bool,
    options: typing.Optional[flytekit.core.options.Options],
) -> flytekit.models.launch_plan.LaunchPlan
```
| Parameter | Type |
|-|-|
| `entity_mapping` | `collections.OrderedDict` |
| `settings` | `flytekit.configuration.SerializationSettings` |
| `entity` | `flytekit.core.launch_plan.LaunchPlan` |
| `recurse_downstream` | `bool` |
| `options` | `typing.Optional[flytekit.core.options.Options]` |

#### ipython_check()

```python
def ipython_check()
```
Check if interface is launching from iPython (not colab)
:return is_ipython (bool): True or False


#### is_display_progress_enabled()

```python
def is_display_progress_enabled()
```
#### iterate_node_executions()

```python
def iterate_node_executions(
    client,
    workflow_execution_identifier,
    task_execution_identifier,
    limit,
    filters,
    unique_parent_id,
) -> Iterator[flytekit.models.node_execution.NodeExecution]
```
This returns a generator for node executions.


| Parameter | Type |
|-|-|
| `client` |  |
| `workflow_execution_identifier` |  |
| `task_execution_identifier` |  |
| `limit` |  |
| `filters` |  |
| `unique_parent_id` |  |

#### iterate_task_executions()

```python
def iterate_task_executions(
    client,
    node_execution_identifier,
    limit,
    filters,
) -> Iterator[flytekit.models.admin.task_execution.TaskExecution]
```
This returns a generator for task executions, given a node execution identifier


| Parameter | Type |
|-|-|
| `client` |  |
| `node_execution_identifier` |  |
| `limit` |  |
| `filters` |  |

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

#### strict_type_hint_matching()

```python
def strict_type_hint_matching(
    input_val: typing.Any,
    target_literal_type: LiteralType,
) -> typing.Type
```
Try to be smarter about guessing the type of the input (and hence the transformer).
If the literal type from the transformer for type(v), matches the literal type of the interface, then we
can use type(). Otherwise, fall back to guess python type from the literal type.
Raises ValueError, like in case of [1,2,3] type() will just give `list`, which won't work.
Raises ValueError also if the transformer found for the raw type doesn't have a literal type match.


| Parameter | Type |
|-|-|
| `input_val` | `typing.Any` |
| `target_literal_type` | `LiteralType` |

## flytekit.remote.remote.ArrayNodeMapTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
class ArrayNodeMapTask(
    python_function_task: typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: typing.Optional[float],
    bound_inputs: typing.Optional[typing.Set[str]],
    bound_inputs_values: typing.Optional[typing.Dict[str, typing.Any]],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `python_function_task` | `typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial]` |
| `concurrency` | `typing.Optional[int]` |
| `min_successes` | `typing.Optional[int]` |
| `min_success_ratio` | `typing.Optional[float]` |
| `bound_inputs` | `typing.Optional[typing.Set[str]]` |
| `bound_inputs_values` | `typing.Optional[typing.Dict[str, typing.Any]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | This returns metadata for the parent ArrayNode, not the sub-node getting mapped over. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | TODO ADD bound variables to the resolver. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | We override this method from flytekit. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`prepare_target()`](#prepare_target) | Alters the underlying run_task command to modify it for map task execution and then resets it after. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_prefix()`](#set_command_prefix) |  |


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
This returns metadata for the parent ArrayNode, not the sub-node getting mapped over


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
#### get_command()

```python
def get_command(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.List[str]
```
TODO ADD bound variables to the resolver. Maybe we need a different resolver?


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

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
) -> flytekit.models.task.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

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

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.Sql
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
) -> type
```
We override this method from flytekit.core.base_task Task because the dispatch_execute method uses this
interface to construct outputs. Each instance of an container_array task will however produce outputs
according to the underlying run_task interface and the array plugin handler will actually create a collection
from these individual outputs as the final output value.


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

#### prepare_target()

```python
def prepare_target()
```
Alters the underlying run_task command to modify it for map task execution and then resets it after.


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

#### set_command_prefix()

```python
def set_command_prefix(
    cmd: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `cmd` | `typing.Optional[typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bound_inputs` |  |  |
| `concurrency` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `execution_mode` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `is_original_sub_node_interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `min_success_ratio` |  |  |
| `min_successes` |  |  |
| `name` |  |  |
| `python_function_task` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.remote.remote.Artifact

An Artifact is effectively just a metadata layer on top of data that exists in Flyte. Most data of interest
will be the output of tasks and workflows. The other category is user uploads.

This Python class has limited purpose, as a way for users to specify that tasks/workflows create Artifacts
and the manner (i.e. name, partitions) in which they are created.

Control creation parameters at task/workflow execution time ::

@task
def t1() -> Annotated[nn.Module, Artifact(name="my.artifact.name")]:
...


```python
class Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
)
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `name` | `Optional[str]` |
| `version` | `Optional[str]` |
| `time_partitioned` | `bool` |
| `time_partition` | `Optional[TimePartition]` |
| `time_partition_granularity` | `Optional[Granularity]` |
| `partition_keys` | `Optional[typing.List[str]]` |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` |

### Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`query()`](#query) |  |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation. |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
) -> O
```
This function allows users to declare partition values dynamically from the body of a task. Note that you'll
still need to annotate your task function output with the relevant Artifact object. Below, one of the partition
values is bound to an input, and the other is set at runtime. Note that since tasks are not run at compile
time, flytekit cannot check that you've bound all the partition values. It's up to you to ensure that you've
done so.

Pricing = Artifact(name="pricing", partition_keys=["region"])
EstError = Artifact(name="estimation_error", partition_keys=["dataset"], time_partitioned=True)

@task
def t1() -> Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
df = get_pricing_results()
dt = get_time()
return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

@task
def my_task() -> Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
...
return RideCountData.create_from(df, time_partition=datetime.datetime.now())


| Parameter | Type |
|-|-|
| `o` | `O` |
| `card` | `Optional[SerializableToString]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### embed_as_query()

```python
def embed_as_query(
    partition: Optional[str],
    bind_to_time_partition: Optional[bool],
    expr: Optional[str],
    op: Optional[Op],
) -> art_id.ArtifactQuery
```
This should only be called in the context of a Trigger. The type of query this returns is different from the
query() function. This type of query is used to reference the triggering artifact, rather than running a query.


| Parameter | Type |
|-|-|
| `partition` | `Optional[str]` |
| `bind_to_time_partition` | `Optional[bool]` |
| `expr` | `Optional[str]` |
| `op` | `Optional[Op]` |

#### query()

```python
def query(
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]],
    partitions: Optional[Union[typing.Dict[str, str], Partitions]],
    kwargs,
) -> ArtifactQuery
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]]` |
| `partitions` | `Optional[Union[typing.Dict[str, str], Partitions]]` |
| `kwargs` | ``**kwargs`` |

#### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


### Properties

| Property | Type | Description |
|-|-|-|
| `concrete_artifact_id` |  |  |
| `partitions` |  |  |
| `time_partition` |  |  |

## flytekit.remote.remote.BranchNode

```python
class BranchNode(
    if_else: flytekit.models.core.workflow.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type |
|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_objct,
)
```
| Parameter | Type |
|-|-|
| `pb2_objct` |  |

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
| `if_else` |  |  |
| `is_empty` |  |  |

## flytekit.remote.remote.ClusterAssignment

```python
class ClusterAssignment(
    cluster_pool,
)
```
| Parameter | Type |
|-|-|
| `cluster_pool` |  |

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
    p,
) -> flyteidl.admin.ClusterAssignment
```
| Parameter | Type |
|-|-|
| `p` |  |

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
| `cluster_pool` |  |  |
| `is_empty` |  |  |

## flytekit.remote.remote.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task



```python
class Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
)
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default. |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`. |
| [`with_params()`](#with_params) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
) -> Config
```
Automatically constructs the Config Object. The order of precedence is as follows
1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
2. If not found in environment then values ar read from the config file
3. If not found in the file, then the default values are used.



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
) -> Config
```
Creates an automatic config for the given endpoint and uses the config_file or environment variable for default.
Refer to `Config.auto()` to understand the default bootstrap behavior.

data_config can be used to configure how data is downloaded or uploaded to a specific Blob storage like S3 / GCS etc.
But, for permissions to a specific backend just use Cloud providers reqcommendation. If using fsspec, then
refer to fsspec documentation


| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |

#### for_sandbox()

```python
def for_sandbox()
```
Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`.
If you are using a hosted Sandbox like environment, then you may need to use port-forward or ingress urls
:return: Config


#### with_params()

```python
def with_params(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
) -> Config
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

## flytekit.remote.remote.ConfigFile

```python
class ConfigFile(
    location: str,
)
```
Load the config from this location


| Parameter | Type |
|-|-|
| `location` | `str` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) |  |


#### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `legacy_config` |  |  |
| `yaml_config` |  |  |

## flytekit.remote.remote.CopyFileDetection

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


## flytekit.remote.remote.CoreNode

This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like
ID, which from the registration step


```python
class CoreNode(
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

## flytekit.remote.remote.DataConfig

Any data storage specific configuration. Please do not use this to store secrets, in S3 case, as it is used in
Flyte sandbox environment we store the access key id and secret.
All DataPersistence plugins are passed all DataConfig and the plugin should correctly use the right config


```python
class DataConfig(
    s3: S3Config,
    gcs: GCSConfig,
    azure: AzureBlobStorageConfig,
    generic: GenericPersistenceConfig,
)
```
| Parameter | Type |
|-|-|
| `s3` | `S3Config` |
| `gcs` | `GCSConfig` |
| `azure` | `AzureBlobStorageConfig` |
| `generic` | `GenericPersistenceConfig` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> DataConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.remote.remote.Domain

Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments.



```python
class Domain(
    id,
    name,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |

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
) -> Domain
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
| `id` |  | {{< multiline >}}A globally unique identifier associated with this domain.
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}A human-readable name for this domain.
{{< /multiline >}} |

## flytekit.remote.remote.ExecutionClusterLabel

```python
class ExecutionClusterLabel(
    value,
)
```
Label value to determine where the execution will be run



| Parameter | Type |
|-|-|
| `value` |  |

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
) -> ExecutionClusterLabel
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
| `value` |  |  |

## flytekit.remote.remote.ExecutionMetadata

```python
class ExecutionMetadata(
    mode: int,
    principal: str,
    nesting: int,
    scheduled_at: Optional[datetime.datetime],
    parent_node_execution: Optional[_identifier.NodeExecutionIdentifier],
    reference_execution: Optional[_identifier.WorkflowExecutionIdentifier],
    system_metadata: Optional[SystemMetadata],
)
```
| Parameter | Type |
|-|-|
| `mode` | `int` |
| `principal` | `str` |
| `nesting` | `int` |
| `scheduled_at` | `Optional[datetime.datetime]` |
| `parent_node_execution` | `Optional[_identifier.NodeExecutionIdentifier]` |
| `reference_execution` | `Optional[_identifier.WorkflowExecutionIdentifier]` |
| `system_metadata` | `Optional[SystemMetadata]` |

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
)
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
| `mode` |  | {{< multiline >}}An enum value from ExecutionMetadata.ExecutionMode which specifies how the job started.
{{< /multiline >}} |
| `nesting` |  | {{< multiline >}}An integer representing how deeply nested the workflow is (i.e. was it triggered by a parent workflow)
{{< /multiline >}} |
| `parent_node_execution` |  | {{< multiline >}}Which subworkflow node (if any) launched this execution
{{< /multiline >}} |
| `principal` |  | {{< multiline >}}The entity that triggered the execution
{{< /multiline >}} |
| `reference_execution` |  | {{< multiline >}}Optional, reference workflow execution related to this execution
{{< /multiline >}} |
| `scheduled_at` |  | {{< multiline >}}For scheduled executions, the requested time for execution for this specific schedule invocation.
{{< /multiline >}} |
| `system_metadata` |  | {{< multiline >}}Optional, platform-specific metadata about the execution.
{{< /multiline >}} |

## flytekit.remote.remote.ExecutionSpec

```python
class ExecutionSpec(
    launch_plan,
    metadata,
    notifications,
    disable_all,
    labels,
    annotations,
    auth_role,
    raw_output_data_config,
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    overwrite_cache: Optional[bool],
    interruptible: Optional[bool],
    envs: Optional[_common_models.Envs],
    tags: Optional[typing.List[str]],
    cluster_assignment: Optional[ClusterAssignment],
    execution_cluster_label: Optional[ExecutionClusterLabel],
)
```
| Parameter | Type |
|-|-|
| `launch_plan` |  |
| `metadata` |  |
| `notifications` |  |
| `disable_all` |  |
| `labels` |  |
| `annotations` |  |
| `auth_role` |  |
| `raw_output_data_config` |  |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `overwrite_cache` | `Optional[bool]` |
| `interruptible` | `Optional[bool]` |
| `envs` | `Optional[_common_models.Envs]` |
| `tags` | `Optional[typing.List[str]]` |
| `cluster_assignment` | `Optional[ClusterAssignment]` |
| `execution_cluster_label` | `Optional[ExecutionClusterLabel]` |

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
    p,
)
```
| Parameter | Type |
|-|-|
| `p` |  |

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
| `annotations` |  |  |
| `auth_role` |  |  |
| `cluster_assignment` |  |  |
| `disable_all` |  |  |
| `envs` |  |  |
| `execution_cluster_label` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `labels` |  |  |
| `launch_plan` |  | {{< multiline >}}If the values were too large, this is the URI where the values were offloaded.
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `metadata` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  |  |
| `security_context` |  |  |
| `tags` |  |  |

## flytekit.remote.remote.FastPackageOptions

FastPackageOptions is used to set configuration options when packaging files.


```python
class FastPackageOptions(
    ignores: list[Ignore],
    keep_default_ignores: bool,
    copy_style: Optional[CopyFileDetection],
    show_files: bool,
)
```
| Parameter | Type |
|-|-|
| `ignores` | `list[Ignore]` |
| `keep_default_ignores` | `bool` |
| `copy_style` | `Optional[CopyFileDetection]` |
| `show_files` | `bool` |

## flytekit.remote.remote.FastSerializationSettings

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

## flytekit.remote.remote.FileAccessProvider

This is the class that is available through the FlyteContext and can be used for persisting data to the remote
durable store.


```python
class FileAccessProvider(
    local_sandbox_dir: typing.Union[str, os.PathLike],
    raw_output_prefix: str,
    data_config: typing.Optional[flytekit.configuration.DataConfig],
    execution_metadata: typing.Optional[dict],
)
```
| Parameter | Type |
|-|-|
| `local_sandbox_dir` | `typing.Union[str, os.PathLike]` |
| `raw_output_prefix` | `str` |
| `data_config` | `typing.Optional[flytekit.configuration.DataConfig]` |
| `execution_metadata` | `typing.Optional[dict]` |

### Methods

| Method | Description |
|-|-|
| [`async_get_data()`](#async_get_data) | . |
| [`async_put_data()`](#async_put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`async_put_raw_data()`](#async_put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`download()`](#download) | Downloads from remote to local. |
| [`download_directory()`](#download_directory) | Downloads directory from given remote to local path. |
| [`exists()`](#exists) |  |
| [`generate_new_custom_path()`](#generate_new_custom_path) | Generates a new path with the raw output prefix and a random string appended to it. |
| [`get()`](#get) |  |
| [`get_async_filesystem_for_path()`](#get_async_filesystem_for_path) |  |
| [`get_data()`](#get_data) | . |
| [`get_file_tail()`](#get_file_tail) |  |
| [`get_filesystem()`](#get_filesystem) |  |
| [`get_filesystem_for_path()`](#get_filesystem_for_path) |  |
| [`get_random_local_directory()`](#get_random_local_directory) |  |
| [`get_random_local_path()`](#get_random_local_path) | Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name. |
| [`get_random_remote_directory()`](#get_random_remote_directory) |  |
| [`get_random_remote_path()`](#get_random_remote_path) |  |
| [`get_random_string()`](#get_random_string) |  |
| [`is_remote()`](#is_remote) | Deprecated. |
| [`join()`](#join) |  |
| [`put_data()`](#put_data) | The implication here is that we're always going to put data to the remote location, so we . |
| [`put_raw_data()`](#put_raw_data) | This is a more flexible version of put that accepts a file-like object or a string path. |
| [`recursive_paths()`](#recursive_paths) |  |
| [`sep()`](#sep) |  |
| [`strip_file_header()`](#strip_file_header) | Drops file:// if it exists from the file. |
| [`upload()`](#upload) | . |
| [`upload_directory()`](#upload_directory) | . |


#### async_get_data()

```python
def async_get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_data()

```python
def async_put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### async_put_raw_data()

```python
def async_put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads from remote to local


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### download_directory()

```python
def download_directory(
    remote_path: str,
    local_path: str,
    kwargs,
)
```
Downloads directory from given remote to local path


| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### exists()

```python
def exists(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### generate_new_custom_path()

```python
def generate_new_custom_path(
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
    alt: typing.Optional[str],
    stem: typing.Optional[str],
) -> str
```
Generates a new path with the raw output prefix and a random string appended to it.
Optionally, you can provide an alternate prefix and a stem. If stem is provided, it
will be appended to the path instead of a random string. If alt is provided, it will
replace the first part of the output prefix, e.g. the S3 or GCS bucket.

If wanting to write to a non-random prefix in a non-default S3 bucket, this can be
called with alt="my-alt-bucket" and stem="my-stem" to generate a path like
s3://my-alt-bucket/default-prefix-part/my-stem



| Parameter | Type |
|-|-|
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |
| `alt` | `typing.Optional[str]` |
| `stem` | `typing.Optional[str]` |

#### get()

```python
def get(
    from_path: str,
    to_path: str,
    recursive: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `from_path` | `str` |
| `to_path` | `str` |
| `recursive` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_async_filesystem_for_path()

```python
def get_async_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> typing.Union[fsspec.asyn.AsyncFileSystem, fsspec.spec.AbstractFileSystem]
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_data()

```python
def get_data(
    remote_path: str,
    local_path: str,
    is_multipart: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `remote_path` | `str` |
| `local_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_file_tail()

```python
def get_file_tail(
    file_path_or_file_name: str,
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `str` |

#### get_filesystem()

```python
def get_filesystem(
    protocol: typing.Optional[str],
    anonymous: bool,
    path: typing.Optional[str],
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `protocol` | `typing.Optional[str]` |
| `anonymous` | `bool` |
| `path` | `typing.Optional[str]` |
| `kwargs` | ``**kwargs`` |

#### get_filesystem_for_path()

```python
def get_filesystem_for_path(
    path: str,
    anonymous: bool,
    kwargs,
) -> fsspec.spec.AbstractFileSystem
```
| Parameter | Type |
|-|-|
| `path` | `str` |
| `anonymous` | `bool` |
| `kwargs` | ``**kwargs`` |

#### get_random_local_directory()

```python
def get_random_local_directory()
```
#### get_random_local_path()

```python
def get_random_local_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
Use file_path_or_file_name, when you want a random directory, but want to preserve the leaf file name


| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_remote_directory()

```python
def get_random_remote_directory()
```
#### get_random_remote_path()

```python
def get_random_remote_path(
    file_path_or_file_name: typing.Optional[str],
) -> str
```
| Parameter | Type |
|-|-|
| `file_path_or_file_name` | `typing.Optional[str]` |

#### get_random_string()

```python
def get_random_string()
```
#### is_remote()

```python
def is_remote(
    path: typing.Union[str, os.PathLike],
) -> bool
```
Deprecated. Let's find a replacement


| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |

#### join()

```python
def join(
    args: `*args`,
    unstrip: bool,
    fs: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `unstrip` | `bool` |
| `fs` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### put_data()

```python
def put_data(
    local_path: typing.Union[str, os.PathLike],
    remote_path: str,
    is_multipart: bool,
    kwargs,
) -> str
```
The implication here is that we're always going to put data to the remote location, so we .remote to ensure
we don't use the true local proxy if the remote path is a file://



| Parameter | Type |
|-|-|
| `local_path` | `typing.Union[str, os.PathLike]` |
| `remote_path` | `str` |
| `is_multipart` | `bool` |
| `kwargs` | ``**kwargs`` |

#### put_raw_data()

```python
def put_raw_data(
    lpath: typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO],
    upload_prefix: typing.Optional[str],
    file_name: typing.Optional[str],
    read_chunk_size_bytes: int,
    encoding: str,
    skip_raw_data_prefix: bool,
    kwargs,
) -> str
```
This is a more flexible version of put that accepts a file-like object or a string path.
Writes to the raw output prefix only. If you want to write to another fs use put_data or get the fsspec
file system directly.
FYI: Currently the raw output prefix set by propeller is already unique per retry and looks like
s3://my-s3-bucket/data/o4/feda4e266c748463a97d-n0-0

If lpath is a folder, then recursive will be set.
If lpath is a streamable, then it can only be a single file.

Writes to:
{raw output prefix}/{upload_prefix}/{file_name}



| Parameter | Type |
|-|-|
| `lpath` | `typing.Union[str, os.PathLike, pathlib._local.Path, bytes, _io.BufferedReader, _io.BytesIO, _io.StringIO]` |
| `upload_prefix` | `typing.Optional[str]` |
| `file_name` | `typing.Optional[str]` |
| `read_chunk_size_bytes` | `int` |
| `encoding` | `str` |
| `skip_raw_data_prefix` | `bool` |
| `kwargs` | ``**kwargs`` |

#### recursive_paths()

```python
def recursive_paths(
    f: str,
    t: str,
) -> typing.Tuple[str, str]
```
| Parameter | Type |
|-|-|
| `f` | `str` |
| `t` | `str` |

#### sep()

```python
def sep(
    file_system: typing.Optional[fsspec.spec.AbstractFileSystem],
) -> str
```
| Parameter | Type |
|-|-|
| `file_system` | `typing.Optional[fsspec.spec.AbstractFileSystem]` |

#### strip_file_header()

```python
def strip_file_header(
    path: str,
    trim_trailing_sep: bool,
) -> str
```
Drops file:// if it exists from the file


| Parameter | Type |
|-|-|
| `path` | `str` |
| `trim_trailing_sep` | `bool` |

#### upload()

```python
def upload(
    file_path: str,
    to_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `file_path` | `str` |
| `to_path` | `str` |
| `kwargs` | ``**kwargs`` |

#### upload_directory()

```python
def upload_directory(
    local_path: str,
    remote_path: str,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `local_path` | `str` |
| `remote_path` | `str` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `data_config` |  |  |
| `local_access` |  |  |
| `local_sandbox_dir` |  | {{< multiline >}}This is a context based temp dir.
{{< /multiline >}} |
| `raw_output_fs` |  | {{< multiline >}}Returns a file system corresponding to the provided raw output prefix
{{< /multiline >}} |
| `raw_output_prefix` |  |  |

## flytekit.remote.remote.FlyteAssertion

Assertion failed.


```python
class FlyteAssertion(
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

## flytekit.remote.remote.FlyteContext

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

## flytekit.remote.remote.FlyteContextManager

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

## flytekit.remote.remote.FlyteEntityAlreadyExistsException

Assertion failed.


```python
class FlyteEntityAlreadyExistsException(
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

## flytekit.remote.remote.FlyteEntityNotExistException

Assertion failed.


```python
class FlyteEntityNotExistException(
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

## flytekit.remote.remote.FlyteExecutionSpan

```python
class FlyteExecutionSpan(
    span: flyteidl.core.metrics_pb2.Span,
)
```
| Parameter | Type |
|-|-|
| `span` | `flyteidl.core.metrics_pb2.Span` |

### Methods

| Method | Description |
|-|-|
| [`dump()`](#dump) |  |
| [`explain()`](#explain) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### dump()

```python
def dump()
```
#### explain()

```python
def explain()
```
#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
)
```
| Parameter | Type |
|-|-|
| `pb` |  |

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

## flytekit.remote.remote.FlyteLaunchPlan

A class encapsulating a remote Flyte launch plan.


```python
class FlyteLaunchPlan(
    id,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### compile()

```python
def compile(
    ctx: FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
) -> LaunchPlanSpec
```
| Parameter | Type |
|-|-|
| `pb2` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    id: id_models.Identifier,
    model: _launch_plan_models.LaunchPlanSpec,
) -> FlyteLaunchPlan
```
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `model` | `_launch_plan_models.LaunchPlanSpec` |

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
| `annotations` |  | {{< multiline >}}The annotations to execute the workflow with
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}The authorization method with which to execute the workflow.
{{< /multiline >}} |
| `default_inputs` |  | {{< multiline >}}Input values to be passed for the execution
{{< /multiline >}} |
| `entity_metadata` |  |  |
| `entity_type_text` |  |  |
| `fixed_inputs` |  | {{< multiline >}}Fixed, non-overridable inputs for the Launch Plan
{{< /multiline >}} |
| `flyte_workflow` |  |  |
| `id` |  |  |
| `interface` |  | {{< multiline >}}The interface is not technically part of the admin.LaunchPlanSpec in the IDL, however the workflow ID is, and
from the workflow ID, fetch will fill in the interface. This is nice because then you can __call__ the=
object and get a node.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_scheduled` |  |  |
| `labels` |  | {{< multiline >}}The labels to execute the workflow with
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `name` |  |  |
| `overwrite_cache` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}Where to store offloaded data like Blobs and Schemas
{{< /multiline >}} |
| `resource_type` |  |  |
| `security_context` |  |  |
| `workflow_id` |  | {{< multiline >}}Unique identifier for the workflow in question
{{< /multiline >}} |

## flytekit.remote.remote.FlyteNode

A class encapsulating a remote Flyte node.


```python
class FlyteNode(
    id,
    upstream_nodes,
    bindings,
    metadata,
    task_node: Optional[FlyteTaskNode],
    workflow_node: Optional[FlyteWorkflowNode],
    branch_node: Optional[FlyteBranchNode],
    gate_node: Optional[FlyteGateNode],
    array_node: Optional[FlyteArrayNode],
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `upstream_nodes` |  |
| `bindings` |  |
| `metadata` |  |
| `task_node` | `Optional[FlyteTaskNode]` |
| `workflow_node` | `Optional[FlyteWorkflowNode]` |
| `branch_node` | `Optional[FlyteBranchNode]` |
| `gate_node` | `Optional[FlyteGateNode]` |
| `array_node` | `Optional[FlyteArrayNode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Node
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    model: _workflow_model.Node,
    sub_workflows: Optional[Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]],
    node_launch_plans: Optional[Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]],
    tasks: Dict[id_models.Identifier, FlyteTask],
    converted_sub_workflows: Dict[id_models.Identifier, FlyteWorkflow],
) -> Tuple[Optional[FlyteNode], Dict[id_models.Identifier, FlyteWorkflow]]
```
| Parameter | Type |
|-|-|
| `model` | `_workflow_model.Node` |
| `sub_workflows` | `Optional[Dict[id_models.Identifier, _workflow_model.WorkflowTemplate]]` |
| `node_launch_plans` | `Optional[Dict[id_models.Identifier, _launch_plan_model.LaunchPlanSpec]]` |
| `tasks` | `Dict[id_models.Identifier, FlyteTask]` |
| `converted_sub_workflows` | `Dict[id_models.Identifier, FlyteWorkflow]` |

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
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

{{< /multiline >}} |
| `flyte_entity` |  |  |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

{{< /multiline >}} |
| `target` |  |  |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

{{< /multiline >}} |
| `upstream_nodes` |  |  |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

{{< /multiline >}} |

## flytekit.remote.remote.FlyteNodeExecution

A class encapsulating a node execution being run on a Flyte remote backend.


```python
class FlyteNodeExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
) -> NodeExecution
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: node_execution_models.NodeExecution,
) -> 'FlyteNodeExecution'
```
| Parameter | Type |
|-|-|
| `base_model` | `node_execution_models.NodeExecution` |

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
| `closure` |  |  |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception. Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `executions` |  |  |
| `id` |  |  |
| `input_uri` |  |  |
| `inputs` |  |  |
| `interface` |  | {{< multiline >}}Return the interface of the task or subworkflow associated with this node execution.
{{< /multiline >}} |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `subworkflow_node_executions` |  | {{< multiline >}}This returns underlying node executions in instances where the current node execution is
a parent node. This happens when it's either a static or dynamic subworkflow.
{{< /multiline >}} |
| `task_executions` |  |  |
| `workflow_executions` |  |  |

## flytekit.remote.remote.FlyteRemote

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

## flytekit.remote.remote.FlyteTask

A class encapsulating a remote Flyte task.


```python
class FlyteTask(
    id,
    type,
    metadata,
    interface,
    custom,
    container,
    task_type_version: int,
    security_context,
    config,
    k8s_pod,
    sql,
    extended_resources,
    should_register: bool,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `type` |  |
| `metadata` |  |
| `interface` |  |
| `custom` |  |
| `container` |  |
| `task_type_version` | `int` |
| `security_context` |  |
| `config` |  |
| `k8s_pod` |  |
| `sql` |  |
| `extended_resources` |  |
| `should_register` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_model()

```python
def promote_from_model(
    base_model: _task_model.TaskTemplate,
) -> FlyteTask
```
| Parameter | Type |
|-|-|
| `base_model` | `_task_model.TaskTemplate` |

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
| `config` |  | {{< multiline >}}Arbitrary dictionary containing metadata for parsing and handling custom plugins.

{{< /multiline >}} |
| `container` |  | {{< multiline >}}If not None, the target of execution should be a container.

{{< /multiline >}} |
| `custom` |  | {{< multiline >}}Arbitrary dictionary containing metadata for custom plugins.

{{< /multiline >}} |
| `docs` |  |  |
| `entity_type_text` |  |  |
| `extended_resources` |  |  |
| `id` |  | {{< multiline >}}This is generated by the system and uniquely identifies the task.

{{< /multiline >}} |
| `interface` |  | {{< multiline >}}The interface definition for this task.

{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  |  |
| `metadata` |  | {{< multiline >}}This contains information needed at runtime to determine behavior such as whether or not outputs are
discoverable, timeouts, and retries.

{{< /multiline >}} |
| `name` |  |  |
| `python_interface` |  |  |
| `resource_type` |  |  |
| `security_context` |  |  |
| `should_register` |  |  |
| `sql` |  |  |
| `task_type_version` |  |  |
| `template` |  |  |
| `type` |  | {{< multiline >}}This is used to identify additional extensions for use by Propeller or SDK.

{{< /multiline >}} |

## flytekit.remote.remote.FlyteTaskExecution

A class encapsulating a task execution being run on a Flyte remote backend.


```python
class FlyteTaskExecution(
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> TaskExecution
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: admin_task_execution_models.TaskExecution,
) -> 'FlyteTaskExecution'
```
| Parameter | Type |
|-|-|
| `base_model` | `admin_task_execution_models.TaskExecution` |

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
| `closure` |  |  |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception. Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `id` |  |  |
| `input_uri` |  |  |
| `inputs` |  |  |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_parent` |  |  |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `task` |  |  |

## flytekit.remote.remote.FlyteTaskNode

A class encapsulating a task that a Flyte node needs to execute.


```python
class FlyteTaskNode(
    flyte_task: FlyteTask,
)
```
Refers to the task that the Node is to execute.
This is currently a oneof in protobuf, but there's only one option currently.
This code should be updated when more options are available.



| Parameter | Type |
|-|-|
| `flyte_task` | `FlyteTask` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) | Takes the idl wrapper for a TaskNode,. |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskNode
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### promote_from_model()

```python
def promote_from_model(
    task: FlyteTask,
) -> FlyteTaskNode
```
Takes the idl wrapper for a TaskNode,
and returns the hydrated Flytekit object for it by fetching it with the FlyteTask control plane.


| Parameter | Type |
|-|-|
| `task` | `FlyteTask` |

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
| `flyte_task` |  |  |
| `is_empty` |  |  |
| `overrides` |  |  |
| `reference_id` |  | {{< multiline >}}A globally unique identifier for the task.
{{< /multiline >}} |

## flytekit.remote.remote.FlyteValueException

Inappropriate argument value (of correct type).


```python
class FlyteValueException(
    received_value,
    error_message,
)
```
| Parameter | Type |
|-|-|
| `received_value` |  |
| `error_message` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.remote.remote.FlyteWorkflow

A class encapsulating a remote Flyte workflow.


```python
class FlyteWorkflow(
    id: id_models.Identifier,
    nodes: List[FlyteNode],
    interface,
    output_bindings,
    metadata,
    metadata_defaults,
    subworkflows: Optional[List[FlyteWorkflow]],
    tasks: Optional[List[FlyteTask]],
    launch_plans: Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]],
    compiled_closure: Optional[compiler_models.CompiledWorkflowClosure],
    should_register: bool,
)
```
| Parameter | Type |
|-|-|
| `id` | `id_models.Identifier` |
| `nodes` | `List[FlyteNode]` |
| `interface` |  |
| `output_bindings` |  |
| `metadata` |  |
| `metadata_defaults` |  |
| `subworkflows` | `Optional[List[FlyteWorkflow]]` |
| `tasks` | `Optional[List[FlyteTask]]` |
| `launch_plans` | `Optional[Dict[id_models.Identifier, launch_plan_models.LaunchPlanSpec]]` |
| `compiled_closure` | `Optional[compiler_models.CompiledWorkflowClosure]` |
| `should_register` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`get_non_system_nodes()`](#get_non_system_nodes) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`promote_from_closure()`](#promote_from_closure) | Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


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
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowSpec
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### get_non_system_nodes()

```python
def get_non_system_nodes(
    nodes: List[_workflow_models.Node],
) -> List[_workflow_models.Node]
```
| Parameter | Type |
|-|-|
| `nodes` | `List[_workflow_models.Node]` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### promote_from_closure()

```python
def promote_from_closure(
    closure: compiler_models.CompiledWorkflowClosure,
    node_launch_plans: Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]],
)
```
Extracts out the relevant portions of a FlyteWorkflow from a closure from the control plane.



| Parameter | Type |
|-|-|
| `closure` | `compiler_models.CompiledWorkflowClosure` |
| `node_launch_plans` | `Optional[Dict[id_models, launch_plan_models.LaunchPlanSpec]]` |

#### promote_from_model()

```python
def promote_from_model(
    base_model: _workflow_models.WorkflowTemplate,
    sub_workflows: Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]],
    tasks: Optional[Dict[Identifier, FlyteTask]],
    node_launch_plans: Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]],
) -> FlyteWorkflow
```
| Parameter | Type |
|-|-|
| `base_model` | `_workflow_models.WorkflowTemplate` |
| `sub_workflows` | `Optional[Dict[Identifier, _workflow_models.WorkflowTemplate]]` |
| `tasks` | `Optional[Dict[Identifier, FlyteTask]]` |
| `node_launch_plans` | `Optional[Dict[Identifier, launch_plan_models.LaunchPlanSpec]]` |

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
| `docs` |  |  |
| `entity_type_text` |  |  |
| `failure_node` |  | {{< multiline >}}Node failure_node: A catch-all node. This node is executed whenever the execution engine determines the
workflow has failed. The interface of this node must match the Workflow interface with an additional input
named "error" of type pb.lyft.flyte.core.Error.
{{< /multiline >}} |
| `flyte_nodes` |  |  |
| `flyte_sub_workflows` |  |  |
| `flyte_tasks` |  |  |
| `id` |  | {{< multiline >}}This is an autogenerated id by the system. The id is globally unique across Flyte.
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}Defines a strongly typed interface for the Workflow (inputs, outputs). This can include some optional
parameters.
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}This contains information on how to run the workflow.
{{< /multiline >}} |
| `metadata_defaults` |  | {{< multiline >}}This contains information on how to run the workflow.
{{< /multiline >}} |
| `name` |  |  |
| `nodes` |  | {{< multiline >}}A list of nodes. In addition, "globals" is a special reserved node id that can be used to consume
workflow inputs
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}A list of output bindings that specify how to construct workflow outputs. Bindings can
pull node outputs or specify literals. All workflow outputs specified in the interface field must be bound
in order for the workflow to be validated. A workflow has an implicit dependency on all of its nodes
to execute successfully in order to bind final outputs.
{{< /multiline >}} |
| `python_interface` |  |  |
| `resource_type` |  |  |
| `should_register` |  |  |
| `sub_workflows` |  |  |
| `template` |  |  |

## flytekit.remote.remote.FlyteWorkflowExecution

A class encapsulating a workflow execution being run on a Flyte remote backend.


```python
class FlyteWorkflowExecution(
    type_hints: Optional[Dict[str, typing.Type]],
    remote: Optional['FlyteRemote'],
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `type_hints` | `Optional[Dict[str, typing.Type]]` |
| `remote` | `Optional['FlyteRemote']` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`sync()`](#sync) | Sync the state of the current execution and returns a new object with the updated state. |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |
| [`wait()`](#wait) | Wait for the execution to complete. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
) -> Execution
```
| Parameter | Type |
|-|-|
| `pb` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model: execution_models.Execution,
    remote: Optional['FlyteRemote'],
    type_hints: Optional[Dict[str, typing.Type]],
) -> 'FlyteWorkflowExecution'
```
| Parameter | Type |
|-|-|
| `base_model` | `execution_models.Execution` |
| `remote` | `Optional['FlyteRemote']` |
| `type_hints` | `Optional[Dict[str, typing.Type]]` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### sync()

```python
def sync(
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Sync the state of the current execution and returns a new object with the updated state.


| Parameter | Type |
|-|-|
| `sync_nodes` | `bool` |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
) -> 'FlyteWorkflowExecution'
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type |
|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` |
| `poll_interval` | `Optional[Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  |  |
| `error` |  | {{< multiline >}}If execution is in progress, raise an exception.  Otherwise, return None if no error was present upon
reaching completion.
{{< /multiline >}} |
| `execution_url` |  |  |
| `flyte_workflow` |  |  |
| `id` |  |  |
| `inputs` |  |  |
| `is_done` |  | {{< multiline >}}Whether or not the execution is complete.
{{< /multiline >}} |
| `is_empty` |  |  |
| `is_successful` |  | {{< multiline >}}Whether or not the execution is successful.
{{< /multiline >}} |
| `node_executions` |  | {{< multiline >}}Get a dictionary of node executions that are a part of this workflow execution.
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}:return: Returns the outputs LiteralsResolver to the execution
:raises: ``FlyteAssertion`` error if execution is in progress or execution ended in error.
{{< /multiline >}} |
| `spec` |  |  |

## flytekit.remote.remote.Identifier

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

## flytekit.remote.remote.ImageConfig

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

## flytekit.remote.remote.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
class ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry. |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled. |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment. |
| [`image_name()`](#image_name) | Full image name with tag. |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec. |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process. |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process. |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory. |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process. |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
) -> ImageSpec
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `tag` |  | {{< multiline >}}Calculate a hash from the image spec. The hash will be the tag of the image.
We will also read the content of the requirement file and the source root to calculate the hash.
Therefore, it will generate different hash if new dependencies are added or the source code is changed.

Keep in mind the fields source_root and copy may be changed by update_image_spec_copy_handling, so when
you call this property in relation to that function matter will change the output.
{{< /multiline >}} |

## flytekit.remote.remote.LaunchPlan

Launch Plans are one of the core constructs of Flyte. Please take a look at the discussion in the
:std:ref:`core concepts <flyte:divedeep-launchplans>` if you are unfamiliar with them.

Every workflow is registered with a default launch plan, which is just a launch plan with none of the additional
attributes set - no default values, fixed values, schedules, etc. Assuming you have the following workflow

.. code-block:: python

@workflow
def wf(a: int, c: str) -> str:
...

Create the default launch plan with

.. code-block:: python

LaunchPlan.get_or_create(workflow=my_wf)

If you specify additional parameters, you'll also have to give the launch plan a unique name. Default and
fixed inputs can be expressed as Python native values like so:

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # fixed_and_default_start
:end-before: # fixed_and_default_end
:language: python
:dedent: 4

Additionally, a launch plan can be configured to run on a schedule and emit notifications.


Please see the relevant Schedule and Notification objects as well.

To configure the remaining parameters, you'll need to import the relevant model objects as well.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # schedule_start
:end-before: # schedule_end
:language: python
:dedent: 4

.. code-block:: python

from flytekit.models.common import Annotations, AuthRole, Labels, RawOutputDataConfig

Then use as follows

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # auth_role_start
:end-before: # auth_role_end
:language: python
:dedent: 4


```python
class LaunchPlan(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    parameters: _interface_models.ParameterMap,
    fixed_inputs: _literal_models.LiteralMap,
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `parameters` | `_interface_models.ParameterMap` |
| `fixed_inputs` | `_literal_models.LiteralMap` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |


#### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `parameters` | `Optional[_interface_models.ParameterMap]` |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
) -> LaunchPlan
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `workflow` | `_annotated_workflow.WorkflowBase` |

#### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type |
|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `name` | `Optional[str]` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `fixed_inputs` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

## flytekit.remote.remote.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    val,
) -> Text
```
| Parameter | Type |
|-|-|
| `val` |  |

## flytekit.remote.remote.LazyEntity

Fetches the entity when the entity is called or when the entity is retrieved.
The entity is derived from RemoteEntity so that it behaves exactly like the mimicked entity.


```python
class LazyEntity(
    name: str,
    getter: typing.Callable[[], ~T],
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `getter` | `typing.Callable[[], ~T]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`entity_fetched()`](#entity_fetched) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


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
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### entity_fetched()

```python
def entity_fetched()
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
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `entity` |  | {{< multiline >}}If not already fetched / available, then the entity will be force fetched.
{{< /multiline >}} |
| `id` |  |  |
| `name` |  |  |
| `python_interface` |  |  |

## flytekit.remote.remote.Literal

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

## flytekit.remote.remote.LiteralMap

```python
class LiteralMap(
    literals,
)
```
| Parameter | Type |
|-|-|
| `literals` |  |

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
) -> LiteralMap
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
| `literals` |  | {{< multiline >}}A dictionary mapping Text key names to Literal objects.
{{< /multiline >}} |

## flytekit.remote.remote.LiteralsResolver

LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation
where you might be working with LiteralMaps. This object allows the caller to specify the Python type that should
correspond to an element of the map.


```python
class LiteralsResolver(
    literals: typing.Dict[str, Literal],
    variable_map: Optional[Dict[str, _interface_models.Variable]],
    ctx: Optional[FlyteContext],
)
```
| Parameter | Type |
|-|-|
| `literals` | `typing.Dict[str, Literal]` |
| `variable_map` | `Optional[Dict[str, _interface_models.Variable]]` |
| `ctx` | `Optional[FlyteContext]` |

### Methods

| Method | Description |
|-|-|
| [`as_python_native()`](#as_python_native) | This should return the native Python representation, compatible with unpacking. |
| [`clear()`](#clear) | D. |
| [`copy()`](#copy) |  |
| [`fromkeys()`](#fromkeys) |  |
| [`get()`](#get) | This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python. |
| [`get_literal()`](#get_literal) |  |
| [`items()`](#items) | D. |
| [`keys()`](#keys) | D. |
| [`pop()`](#pop) | D. |
| [`popitem()`](#popitem) | D. |
| [`setdefault()`](#setdefault) | D. |
| [`update()`](#update) | D. |
| [`update_type_hints()`](#update_type_hints) |  |
| [`values()`](#values) | D. |


#### as_python_native()

```python
def as_python_native(
    python_interface: Interface,
) -> typing.Any
```
This should return the native Python representation, compatible with unpacking.
This function relies on Python interface outputs being ordered correctly.



| Parameter | Type |
|-|-|
| `python_interface` | `Interface` |

#### clear()

```python
def clear()
```
D.clear() -> None.  Remove all items from D.


#### copy()

```python
def copy()
```
#### fromkeys()

```python
def fromkeys(
    iterable,
    value,
)
```
| Parameter | Type |
|-|-|
| `iterable` |  |
| `value` |  |

#### get()

```python
def get(
    attr: str,
    as_type: Optional[typing.Type],
) -> typing.Any
```
This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python
native value. A Python type can optionally be supplied. If successful, the native value will be cached and
future calls will return the cached value instead.



| Parameter | Type |
|-|-|
| `attr` | `str` |
| `as_type` | `Optional[typing.Type]` |

#### get_literal()

```python
def get_literal(
    key: str,
) -> Literal
```
| Parameter | Type |
|-|-|
| `key` | `str` |

#### items()

```python
def items()
```
D.items() -> a set-like object providing a view on D's items


#### keys()

```python
def keys()
```
D.keys() -> a set-like object providing a view on D's keys


#### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### popitem()

```python
def popitem()
```
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


#### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### update()

```python
def update(
    other,
    kwds,
)
```
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type |
|-|-|
| `other` |  |
| `kwds` |  |

#### update_type_hints()

```python
def update_type_hints(
    type_hints: typing.Dict[str, typing.Type],
)
```
| Parameter | Type |
|-|-|
| `type_hints` | `typing.Dict[str, typing.Type]` |

#### values()

```python
def values()
```
D.values() -> an object providing a view on D's values


### Properties

| Property | Type | Description |
|-|-|-|
| `literals` |  |  |
| `native_values` |  |  |
| `variable_map` |  |  |

## flytekit.remote.remote.NamedEntityIdentifier

```python
class NamedEntityIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | Stores object to a Flyte-IDL defined protobuf. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
) -> NamedEntityIdentifier
```
| Parameter | Type |
|-|-|
| `idl_object` |  |

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
Stores object to a Flyte-IDL defined protobuf.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}The name of the domain within the project.
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}The name of the entity within the namespace of the project and domain.
{{< /multiline >}} |
| `project` |  | {{< multiline >}}The name of the project in which this entity lives.
{{< /multiline >}} |

## flytekit.remote.remote.Node

```python
class Node(
    id,
    metadata,
    inputs,
    upstream_node_ids,
    output_aliases,
    task_node,
    workflow_node,
    branch_node,
    gate_node: typing.Optional[flytekit.models.core.workflow.GateNode],
    array_node: typing.Optional[flytekit.models.core.workflow.ArrayNode],
)
```
A Workflow graph Node. One unit of execution in the graph. Each node can be linked to a Task,
a Workflow or a branch node.  One of the nodes must be specified.



| Parameter | Type |
|-|-|
| `id` |  |
| `metadata` |  |
| `inputs` |  |
| `upstream_node_ids` |  |
| `output_aliases` |  |
| `task_node` |  |
| `workflow_node` |  |
| `branch_node` |  |
| `gate_node` | `typing.Optional[flytekit.models.core.workflow.GateNode]` |
| `array_node` | `typing.Optional[flytekit.models.core.workflow.ArrayNode]` |

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
) -> Node
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
| `array_node` |  |  |
| `branch_node` |  | {{< multiline >}}[Optional] Information about the branch node to evaluate in this node.

{{< /multiline >}} |
| `gate_node` |  |  |
| `id` |  | {{< multiline >}}A workflow-level unique identifier that identifies this node in the workflow. "inputs" and
"outputs" are reserved node ids that cannot be used by other nodes.

{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}Specifies how to bind the underlying interface's inputs.  All required inputs specified
in the underlying interface must be fulfilled.

{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}Extra metadata about the node.

{{< /multiline >}} |
| `output_aliases` |  | {{< multiline >}}[Optional] A node can define aliases for a subset of its outputs. This
is particularly useful if different nodes need to conform to the same interface (e.g. all branches in
a branch node). Downstream nodes must refer to this node's outputs using the alias if one is specified.

{{< /multiline >}} |
| `target` |  |  |
| `task_node` |  | {{< multiline >}}[Optional] Information about the Task to execute in this node.

{{< /multiline >}} |
| `upstream_node_ids` |  | {{< multiline >}}[Optional] Specifies execution dependency for this node ensuring it will
only get scheduled to run after all its upstream nodes have completed. This node will have
an implicit dependency on any node that appears in inputs field.

{{< /multiline >}} |
| `workflow_node` |  | {{< multiline >}}[Optional] Information about the Workflow to execute in this mode.

{{< /multiline >}} |

## flytekit.remote.remote.NodeExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


```python
class NodeExecutionGetDataResponse(
    args,
    dynamic_workflow: typing.Optional[DynamicWorkflowNodeMetadata],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `dynamic_workflow` | `typing.Optional[DynamicWorkflowNodeMetadata]` |
| `kwargs` | ``**kwargs`` |

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
) -> NodeExecutionGetDataResponse
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
| `dynamic_workflow` |  |  |
| `full_inputs` |  |  |
| `full_outputs` |  |  |
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.remote.remote.NodeMetadata

```python
class NodeMetadata(
    name,
    timeout,
    retries,
    interruptible: typing.Optional[bool],
    cacheable: typing.Optional[bool],
    cache_version: typing.Optional[str],
    cache_serializable: typing.Optional[bool],
)
```
Defines extra information about the Node.



| Parameter | Type |
|-|-|
| `name` |  |
| `timeout` |  |
| `retries` |  |
| `interruptible` | `typing.Optional[bool]` |
| `cacheable` | `typing.Optional[bool]` |
| `cache_version` | `typing.Optional[str]` |
| `cache_serializable` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
| `cache_serializable` |  |  |
| `cache_version` |  |  |
| `cacheable` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `retries` |  |  |
| `timeout` |  |  |

## flytekit.remote.remote.NotificationList

```python
class NotificationList(
    notifications,
)
```
| Parameter | Type |
|-|-|
| `notifications` |  |

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
) -> NotificationList
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
| `notifications` |  |  |

## flytekit.remote.remote.Options

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

## flytekit.remote.remote.OrderedDict

Dictionary that remembers insertion order


## flytekit.remote.remote.PickledEntity

Represents the structure of the pickled object stored in the .pkl file for interactive mode.

Attributes:
metadata: Metadata about the pickled entities including Python version
entities: Dictionary mapping entity names to their PythonAutoContainerTask instances


```python
class PickledEntity(
    metadata: PickledEntityMetadata,
    entities: Dict[str, PythonAutoContainerTask],
)
```
| Parameter | Type |
|-|-|
| `metadata` | `PickledEntityMetadata` |
| `entities` | `Dict[str, PythonAutoContainerTask]` |

## flytekit.remote.remote.PickledEntityMetadata

Metadata for a pickled entity containing version information.

Attributes:
python_version: The Python version string (e.g. "3.12.0") used to create the pickle


```python
class PickledEntityMetadata(
    python_version: str,
)
```
| Parameter | Type |
|-|-|
| `python_version` | `str` |

## flytekit.remote.remote.Progress

Renders an auto-updating progress bar(s).



```python
class Progress(
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
)
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
| [`add_task()`](#add_task) | Add a new 'task' to the Progress display. |
| [`advance()`](#advance) | Advance task by a number of steps. |
| [`get_default_columns()`](#get_default_columns) | Get the default columns used for a new Progress instance:. |
| [`get_renderable()`](#get_renderable) | Get a renderable for the progress display. |
| [`get_renderables()`](#get_renderables) | Get a number of renderables for the progress display. |
| [`make_tasks_table()`](#make_tasks_table) | Get a table to render the Progress display. |
| [`open()`](#open) | Track progress while reading from a binary file. |
| [`refresh()`](#refresh) | Refresh (render) the progress information. |
| [`remove_task()`](#remove_task) | Delete a task if it exists. |
| [`reset()`](#reset) | Reset a task so completed is 0 and the clock is reset. |
| [`start()`](#start) | Start the progress display. |
| [`start_task()`](#start_task) | Start a task. |
| [`stop()`](#stop) | Stop the progress display. |
| [`stop_task()`](#stop_task) | Stop a task. |
| [`track()`](#track) | Track progress by iterating over a sequence. |
| [`update()`](#update) | Update information associated with a task. |
| [`wrap_file()`](#wrap_file) | Track progress file reading from a binary file. |


#### add_task()

```python
def add_task(
    description: str,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: bool,
    fields: typing.Any,
) -> rich.progress.TaskID
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
)
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
) -> rich.table.Table
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
) -> typing.Union[typing.BinaryIO, typing.TextIO]
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
)
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
)
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
)
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
)
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
) -> typing.Iterable[~ProgressType]
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
)
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
) -> typing.BinaryIO
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
| `console` |  |  |
| `finished` |  | {{< multiline >}}Check if all tasks have been completed.
{{< /multiline >}} |
| `task_ids` |  | {{< multiline >}}A list of task IDs.
{{< /multiline >}} |
| `tasks` |  | {{< multiline >}}Get a list of Task instances.
{{< /multiline >}} |

## flytekit.remote.remote.Project

```python
class Project(
    id,
    name,
    description,
    state,
)
```
A project represents a logical grouping used to organize entities (tasks, workflows, executions) in the Flyte
platform.



| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |
| `description` |  |
| `state` |  |

### Methods

| Method | Description |
|-|-|
| [`active_project()`](#active_project) |  |
| [`archived_project()`](#archived_project) |  |
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### active_project()

```python
def active_project(
    id,
)
```
| Parameter | Type |
|-|-|
| `id` |  |

#### archived_project()

```python
def archived_project(
    id,
)
```
| Parameter | Type |
|-|-|
| `id` |  |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Project
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
| `description` |  | {{< multiline >}}A concise description for this project.
{{< /multiline >}} |
| `id` |  | {{< multiline >}}A globally unique identifier associated with this project
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}A human-readable name for this project.
{{< /multiline >}} |
| `state` |  | {{< multiline >}}The state of this project.
{{< /multiline >}} |

## flytekit.remote.remote.PythonAutoContainerTask

A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the
container and the container information to be automatically captured.
This base will auto configure the image and image version to be used for all its derivatives.

If you are looking to extend, you might prefer to use ``PythonFunctionTask`` or ``PythonInstanceTask``


```python
class PythonAutoContainerTask(
    name: str,
    task_config: T,
    task_type,
    container_image: Optional[Union[str, ImageSpec]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    environment: Optional[Dict[str, str]],
    task_resolver: Optional[TaskResolverMixin],
    secret_requests: Optional[List[Secret]],
    pod_template: Optional[PodTemplate],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `task_config` | `T` |
| `task_type` |  |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `environment` | `Optional[Dict[str, str]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `pod_template` | `Optional[PodTemplate]` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command. |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task. |


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
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
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
) -> Optional[Dict[str, str]]
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
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
) -> Optional[tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
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
) -> _task_model.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

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
) -> flytekit.models.literals.LiteralMap
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
)
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
)
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

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
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_resolver` |  |  |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.remote.remote.PythonFunctionTask

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
class PythonFunctionTask(
    task_config: T,
    task_function: Callable,
    task_type,
    ignore_input_vars: Optional[List[str]],
    execution_mode: ExecutionBehavior,
    task_resolver: Optional[TaskResolverMixin],
    node_dependency_hints: Optional[Iterable[Union['PythonFunctionTask', '_annotated_launch_plan.LaunchPlan', WorkflowBase]]],
    pickle_untyped: bool,
    kwargs,
)
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
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`compile_into_workflow()`](#compile_into_workflow) | In the case of dynamic workflows, this function will produce a workflow definition at execution time which will. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`dynamic_execute()`](#dynamic_execute) | By the time this function is invoked, the local_execute function should have unwrapped the Promises and Flyte. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command. |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task. |


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

#### compile_into_workflow()

```python
def compile_into_workflow(
    ctx: FlyteContext,
    task_function: Callable,
    kwargs,
) -> Union[_dynamic_job.DynamicJobSpec, _literal_models.LiteralMap]
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

#### dynamic_execute()

```python
def dynamic_execute(
    task_function: Callable,
    kwargs,
) -> Any
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
) -> Any
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
) -> List[str]
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
) -> Optional[Dict[str, str]]
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
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
) -> Optional[tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
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
) -> _task_model.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

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
) -> flytekit.models.literals.LiteralMap
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
)
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
)
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

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
| `execution_mode` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  | {{< multiline >}}Returns the name of the task.
{{< /multiline >}} |
| `node_dependency_hints` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_function` |  |  |
| `task_resolver` |  |  |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.remote.remote.PythonFunctionWorkflow

Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte.
This Python object represents a workflow  defined by a function and decorated with the
:py:func:`@workflow <flytekit.workflow>` decorator. Please see notes on that object for additional information.


```python
class PythonFunctionWorkflow(
    workflow_function: Callable,
    metadata: WorkflowMetadata,
    default_metadata: WorkflowMetadataDefaults,
    docstring: Optional[Docstring],
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
)
```
| Parameter | Type |
|-|-|
| `workflow_function` | `Callable` |
| `metadata` | `WorkflowMetadata` |
| `default_metadata` | `WorkflowMetadataDefaults` |
| `docstring` | `Optional[Docstring]` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `pickle_untyped` | `bool` |
| `default_options` | `Optional[Options]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) | Supply static Python native values in the kwargs if you want them to be used in the compilation. |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) | This function is here only to try to streamline the pattern between workflows and tasks. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### compile()

```python
def compile(
    kwargs,
)
```
Supply static Python native values in the kwargs if you want them to be used in the compilation. This mimics
a 'closure' in the traditional sense of the word.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
)
```
This function is here only to try to streamline the pattern between workflows and tasks. Since tasks
call execute from dispatch_execute which is in local_execute, workflows should also call an execute inside
local_execute. This makes mocking cleaner.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

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
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `function` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.remote.remote.PythonTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
class PythonTask(
    task_type: str,
    name: str,
    task_config: typing.Optional[~T],
    interface: typing.Optional[flytekit.core.interface.Interface],
    environment: typing.Optional[typing.Dict[str, str]],
    disable_deck: typing.Optional[bool],
    enable_deck: typing.Optional[bool],
    deck_fields: typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]],
    kwargs,
)
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
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
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
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.remote.remote.ReferenceEntity

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

## flytekit.remote.remote.ReferenceLaunchPlan

A reference launch plan serves as a pointer to a Launch Plan that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.


```python
class ReferenceLaunchPlan(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) |  |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`execute()`](#execute) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `parameters` | `Optional[_interface_models.ParameterMap]` |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

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
#### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
) -> LaunchPlan
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `workflow` | `_annotated_workflow.WorkflowBase` |

#### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type |
|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `name` | `Optional[str]` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

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
| `annotations` |  |  |
| `fixed_inputs` |  |  |
| `id` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `reference` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

## flytekit.remote.remote.ReferenceSpec

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

## flytekit.remote.remote.ReferenceTask

This is a reference task, the body of the function passed in through the constructor will never be used, only the
signature of the function will be. The signature should also match the signature of the task you're referencing,
as stored by Flyte Admin, if not, workflows using this will break upon compilation.


```python
class ReferenceTask(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
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
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.remote.remote.ReferenceWorkflow

A reference workflow is a pointer to a workflow that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.


```python
class ReferenceWorkflow(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

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

#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

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
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

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
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `function` |  |  |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.remote.remote.RegistrationSkipped

RegistrationSkipped error is raised when trying to register an entity that is not registrable.


## flytekit.remote.remote.RemoteEntity

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class RemoteEntity(
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
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


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
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


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
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `name` |  |  |
| `python_interface` |  |  |

## flytekit.remote.remote.ResolvedIdentifiers

```python
class ResolvedIdentifiers(
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

## flytekit.remote.remote.ResourceType

## flytekit.remote.remote.SerializationSettings

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

## flytekit.remote.remote.Signal

A ProtocolMessage


## flytekit.remote.remote.SignalIdentifier

```python
class SignalIdentifier(
    signal_id: str,
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.identifier_pb2.SignalIdentifier,
) -> SignalIdentifier
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.identifier_pb2.SignalIdentifier` |

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
| `execution_id` |  |  |
| `is_empty` |  |  |
| `signal_id` |  |  |

## flytekit.remote.remote.SignalListRequest

A ProtocolMessage


## flytekit.remote.remote.SignalSetRequest

A ProtocolMessage


## flytekit.remote.remote.Sort

```python
class Sort(
    key,
    direction,
)
```
| Parameter | Type |
|-|-|
| `key` |  |
| `direction` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`from_python_std()`](#from_python_std) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Sort
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    text,
) -> Sort
```
| Parameter | Type |
|-|-|
| `text` |  |

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
| `direction` |  |  |
| `is_empty` |  |  |
| `key` |  |  |

## flytekit.remote.remote.SynchronousFlyteClient

This is a low-level client that users can use to make direct gRPC service calls to the control plane. See the
:std:doc:`service spec <idl:protos/docs/service/index>`. This is more user-friendly interface than the
:py:class:`raw client <flytekit.clients.raw.RawSynchronousFlyteClient>` so users should try to use this class
first. Create a client by ::

SynchronousFlyteClient("your.domain:port", insecure=True)
# insecure should be True if your flyteadmin deployment doesn't have SSL enabled


```python
class SynchronousFlyteClient(
    cfg: PlatformConfig,
    kwargs,
)
```
Initializes a gRPC channel to the given Flyte Admin service.



| Parameter | Type |
|-|-|
| `cfg` | `PlatformConfig` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`create_download_link()`](#create_download_link) |  |
| [`create_download_location()`](#create_download_location) |  |
| [`create_execution()`](#create_execution) | This will create an execution for the given execution spec. |
| [`create_launch_plan()`](#create_launch_plan) | This will create a launch plan definition in the Admin database. |
| [`create_task()`](#create_task) | This will create a task definition in the Admin database. |
| [`create_upload_location()`](#create_upload_location) | Get a signed url to be used during fast registration. |
| [`create_workflow()`](#create_workflow) | This will create a workflow definition in the Admin database. |
| [`get_active_launch_plan()`](#get_active_launch_plan) | Retrieves the active launch plan entity given a named entity identifier (project, domain, name). |
| [`get_control_plane_version()`](#get_control_plane_version) | Retrieve the Control Plane version from Flyteadmin. |
| [`get_data()`](#get_data) |  |
| [`get_domains()`](#get_domains) | This returns a list of domains. |
| [`get_download_artifact_signed_url()`](#get_download_artifact_signed_url) | Get a signed url for an artifact. |
| [`get_download_signed_url()`](#get_download_signed_url) |  |
| [`get_execution()`](#get_execution) | . |
| [`get_execution_data()`](#get_execution_data) | Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available). |
| [`get_execution_metrics()`](#get_execution_metrics) | Returns metrics partitioning and categorizing the workflow execution time-series. |
| [`get_node_execution()`](#get_node_execution) | . |
| [`get_node_execution_data()`](#get_node_execution_data) | Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available). |
| [`get_project_domain_attributes()`](#get_project_domain_attributes) | Fetches the custom attributes set for a project and domain combination. |
| [`get_task_execution()`](#get_task_execution) | . |
| [`get_task_execution_data()`](#get_task_execution_data) | Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available). |
| [`get_upload_signed_url()`](#get_upload_signed_url) | Get a signed url to be used during fast registration. |
| [`get_workflow_attributes()`](#get_workflow_attributes) | Fetches the custom attributes set for a project, domain, and workflow combination. |
| [`list_active_launch_plans_paginated()`](#list_active_launch_plans_paginated) | This returns a page of currently active launch plan meta-information for launch plans in a given project and. |
| [`list_executions_paginated()`](#list_executions_paginated) | This returns a page of executions in a given project and domain. |
| [`list_launch_plan_ids_paginated()`](#list_launch_plan_ids_paginated) | This returns a page of identifiers for the launch plans for a given project and domain. |
| [`list_launch_plans_paginated()`](#list_launch_plans_paginated) | This returns a page of launch plan meta-information for launch plans in a given project and domain. |
| [`list_matchable_attributes()`](#list_matchable_attributes) | Fetches all custom attributes for a resource type. |
| [`list_node_executions()`](#list_node_executions) | Get node executions associated with a given workflow execution. |
| [`list_node_executions_for_task_paginated()`](#list_node_executions_for_task_paginated) | This returns nodes spawned by a specific task execution. |
| [`list_node_executions_paginated()`](#list_node_executions_paginated) | . |
| [`list_projects()`](#list_projects) | This will return a list of the projects registered with the Flyte Admin Service. |
| [`list_projects_paginated()`](#list_projects_paginated) | This returns a page of projects. |
| [`list_signals()`](#list_signals) | This lists signals. |
| [`list_task_executions_paginated()`](#list_task_executions_paginated) | . |
| [`list_task_ids_paginated()`](#list_task_ids_paginated) | This returns a page of identifiers for the tasks for a given project and domain. |
| [`list_tasks_paginated()`](#list_tasks_paginated) | This returns a page of task metadata for tasks in a given project and domain. |
| [`list_workflow_ids_paginated()`](#list_workflow_ids_paginated) | This returns a page of identifiers for the workflows for a given project and domain. |
| [`list_workflows_paginated()`](#list_workflows_paginated) | This returns a page of workflow meta-information for workflows in a given project and domain. |
| [`recover_execution()`](#recover_execution) | Recreates a previously-run workflow execution that will only start executing from the last known failure point. |
| [`register_project()`](#register_project) | Registers a project. |
| [`relaunch_execution()`](#relaunch_execution) | . |
| [`set_signal()`](#set_signal) | This sets a signal. |
| [`terminate_execution()`](#terminate_execution) | . |
| [`update_launch_plan()`](#update_launch_plan) | Updates a launch plan. |
| [`update_named_entity()`](#update_named_entity) | Updates the metadata associated with a named entity. |
| [`update_project()`](#update_project) | Update an existing project specified by id. |
| [`update_project_domain_attributes()`](#update_project_domain_attributes) | Sets custom attributes for a project and domain combination. |
| [`update_workflow_attributes()`](#update_workflow_attributes) | Sets custom attributes for a project, domain, and workflow combination. |
| [`with_root_certificate()`](#with_root_certificate) |  |


#### create_download_link()

```python
def create_download_link(
    create_download_link_request: _dataproxy_pb2.CreateDownloadLinkRequest,
) -> _dataproxy_pb2.CreateDownloadLinkResponse
```
| Parameter | Type |
|-|-|
| `create_download_link_request` | `_dataproxy_pb2.CreateDownloadLinkRequest` |

#### create_download_location()

```python
def create_download_location(
    create_download_location_request: _dataproxy_pb2.CreateDownloadLocationRequest,
) -> _dataproxy_pb2.CreateDownloadLocationResponse
```
| Parameter | Type |
|-|-|
| `create_download_location_request` | `_dataproxy_pb2.CreateDownloadLocationRequest` |

#### create_execution()

```python
def create_execution(
    project,
    domain,
    name,
    execution_spec,
    inputs,
) -> flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
This will create an execution for the given execution spec.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |
| `execution_spec` |  |
| `inputs` |  |

#### create_launch_plan()

```python
def create_launch_plan(
    launch_plan_identifer,
    launch_plan_spec,
)
```
This will create a launch plan definition in the Admin database.  Once successful, the launch plan object can be
retrieved via the client or viewed via the UI or command-line interfaces.

.. note ::

Overwrites are not supported so any request for a given project, domain, name, and version that exists in
the database must match the existing definition exactly.  This also means that as long as the request
remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `launch_plan_identifer` |  |
| `launch_plan_spec` |  |

#### create_task()

```python
def create_task(
    task_identifer,
    task_spec,
)
```
This will create a task definition in the Admin database. Once successful, the task object can be
retrieved via the client or viewed via the UI or command-line interfaces.

> [!NOTE]
> Overwrites are not supported so any request for a given project, domain, name, and version that exists in
the database must match the existing definition exactly. Furthermore, as long as the request
remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `task_identifer` |  |
| `task_spec` |  |

#### create_upload_location()

```python
def create_upload_location(
    create_upload_location_request: _dataproxy_pb2.CreateUploadLocationRequest,
) -> flyteidl.service.dataproxy_pb2.CreateUploadLocationResponse
```
Get a signed url to be used during fast registration


| Parameter | Type |
|-|-|
| `create_upload_location_request` | `_dataproxy_pb2.CreateUploadLocationRequest` |

#### create_workflow()

```python
def create_workflow(
    workflow_identifier,
    workflow_spec,
)
```
This will create a workflow definition in the Admin database. Once successful, the workflow object can be
retrieved via the client or viewed via the UI or command-line interfaces.

.. note ::

Overwrites are not supported so any request for a given project, domain, name, and version that exists in
the database must match the existing definition exactly. Furthermore, as long as the request
remains identical, calling this method multiple times will result in success.



| Parameter | Type |
|-|-|
| `workflow_identifier` |  |
| `workflow_spec` |  |

#### get_active_launch_plan()

```python
def get_active_launch_plan(
    identifier,
) -> flytekit.models.launch_plan.LaunchPlan
```
Retrieves the active launch plan entity given a named entity identifier (project, domain, name).  Raises an
error if no active launch plan exists.



| Parameter | Type |
|-|-|
| `identifier` |  |

#### get_control_plane_version()

```python
def get_control_plane_version()
```
Retrieve the Control Plane version from Flyteadmin.

This method calls Flyteadmin's GetVersion API to obtain the current version information of the control plane.
The retrieved version can be used to enable or disable specific features based on the Flyteadmin version.

Returns:
str: The version string of the control plane.


#### get_data()

```python
def get_data(
    flyte_uri: str,
) -> flyteidl.service.dataproxy_pb2.GetDataResponse
```
| Parameter | Type |
|-|-|
| `flyte_uri` | `str` |

#### get_domains()

```python
def get_domains()
```
This returns a list of domains.



#### get_download_artifact_signed_url()

```python
def get_download_artifact_signed_url(
    node_id: str,
    project: str,
    domain: str,
    name: str,
    artifact_type: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x102e95ed0>,
    expires_in: datetime.timedelta,
) -> flyteidl.service.dataproxy_pb2.CreateDownloadLinkResponse
```
Get a signed url for an artifact.



| Parameter | Type |
|-|-|
| `node_id` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `artifact_type` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x102e95ed0>` |
| `expires_in` | `datetime.timedelta` |

#### get_download_signed_url()

```python
def get_download_signed_url(
    native_url: str,
    expires_in: datetime.timedelta,
) -> flyteidl.service.dataproxy_pb2.CreateDownloadLocationResponse
```
| Parameter | Type |
|-|-|
| `native_url` | `str` |
| `expires_in` | `datetime.timedelta` |

#### get_execution()

```python
def get_execution(
    id,
) -> flytekit.models.execution.Execution
```
| Parameter | Type |
|-|-|
| `id` |  |

#### get_execution_data()

```python
def get_execution_data(
    id,
) -> flytekit.models.execution.WorkflowExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for an execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `id` |  |

#### get_execution_metrics()

```python
def get_execution_metrics(
    id,
    depth,
) -> flyteidl.admin.execution_pb2.WorkflowExecutionGetMetricsResponse
```
Returns metrics partitioning and categorizing the workflow execution time-series.



| Parameter | Type |
|-|-|
| `id` |  |
| `depth` |  |

#### get_node_execution()

```python
def get_node_execution(
    node_execution_identifier,
) -> flytekit.models.node_execution.NodeExecution
```
| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |

#### get_node_execution_data()

```python
def get_node_execution_data(
    node_execution_identifier,
) -> flytekit.models.execution.NodeExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |

#### get_project_domain_attributes()

```python
def get_project_domain_attributes(
    project,
    domain,
    resource_type,
)
```
Fetches the custom attributes set for a project and domain combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `resource_type` |  |

#### get_task_execution()

```python
def get_task_execution(
    id,
) -> flytekit.models.admin.task_execution.TaskExecution
```
| Parameter | Type |
|-|-|
| `id` |  |

#### get_task_execution_data()

```python
def get_task_execution_data(
    task_execution_identifier,
) -> flytekit.models.execution.NodeExecutionGetDataResponse
```
Returns signed URLs to LiteralMap blobs for a node execution's inputs and outputs (when available).



| Parameter | Type |
|-|-|
| `task_execution_identifier` |  |

#### get_upload_signed_url()

```python
def get_upload_signed_url(
    project: str,
    domain: str,
    content_md5: typing.Optional[bytes],
    filename: typing.Optional[str],
    expires_in: typing.Optional[datetime.timedelta],
    filename_root: typing.Optional[str],
    add_content_md5_metadata: bool,
) -> flyteidl.service.dataproxy_pb2.CreateUploadLocationResponse
```
Get a signed url to be used during fast registration



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `content_md5` | `typing.Optional[bytes]` |
| `filename` | `typing.Optional[str]` |
| `expires_in` | `typing.Optional[datetime.timedelta]` |
| `filename_root` | `typing.Optional[str]` |
| `add_content_md5_metadata` | `bool` |

#### get_workflow_attributes()

```python
def get_workflow_attributes(
    project,
    domain,
    workflow,
    resource_type,
)
```
Fetches the custom attributes set for a project, domain, and workflow combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `workflow` |  |
| `resource_type` |  |

#### list_active_launch_plans_paginated()

```python
def list_active_launch_plans_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> list[flytekit.models.launch_plan.LaunchPlan], str
```
This returns a page of currently active launch plan meta-information for launch plans in a given project and
domain.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_executions_paginated()

```python
def list_executions_paginated(
    project,
    domain,
    limit,
    token,
    filters,
    sort_by,
) -> (list[flytekit.models.execution.Execution], Text)
```
This returns a page of executions in a given project and domain.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_launch_plan_ids_paginated()

```python
def list_launch_plan_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the launch plans for a given project and domain. Filters can also be
specified.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_launch_plans_paginated()

```python
def list_launch_plans_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> list[flytekit.models.launch_plan.LaunchPlan], str
```
This returns a page of launch plan meta-information for launch plans in a given project and domain.  Optionally,
specifying a name will limit the results to only workflows with that name in the given project and domain.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_matchable_attributes()

```python
def list_matchable_attributes(
    resource_type,
)
```
Fetches all custom attributes for a resource type.


| Parameter | Type |
|-|-|
| `resource_type` |  |

#### list_node_executions()

```python
def list_node_executions(
    workflow_execution_identifier,
    limit: int,
    token: typing.Optional[str],
    filters: typing.List[flytekit.models.filters.Filter],
    sort_by: flytekit.models.admin.common.Sort,
    unique_parent_id: str,
) -> list[flytekit.models.node_execution.NodeExecution], Text
```
Get node executions associated with a given workflow execution.



| Parameter | Type |
|-|-|
| `workflow_execution_identifier` |  |
| `limit` | `int` |
| `token` | `typing.Optional[str]` |
| `filters` | `typing.List[flytekit.models.filters.Filter]` |
| `sort_by` | `flytekit.models.admin.common.Sort` |
| `unique_parent_id` | `str` |

#### list_node_executions_for_task_paginated()

```python
def list_node_executions_for_task_paginated(
    task_execution_identifier,
    limit,
    token,
    filters,
    sort_by,
) -> list[flytekit.models.node_execution.NodeExecution], Text
```
This returns nodes spawned by a specific task execution.  This is generally from things like dynamic tasks.


| Parameter | Type |
|-|-|
| `task_execution_identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_node_executions_paginated()

```python
def list_node_executions_paginated(
    node_execution_list_request,
) -> flyteidl.admin.node_execution_pb2.NodeExecutionList
```
| Parameter | Type |
|-|-|
| `node_execution_list_request` |  |

#### list_projects()

```python
def list_projects(
    project_list_request: typing.Optional[ProjectListRequest],
) -> flyteidl.admin.project_pb2.Projects
```
This will return a list of the projects registered with the Flyte Admin Service


| Parameter | Type |
|-|-|
| `project_list_request` | `typing.Optional[ProjectListRequest]` |

#### list_projects_paginated()

```python
def list_projects_paginated(
    limit,
    token,
    filters,
    sort_by,
) -> (list[flytekit.models.Project], Text)
```
This returns a page of projects.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_signals()

```python
def list_signals(
    signal_list_request: SignalListRequest,
) -> SignalList
```
This lists signals


| Parameter | Type |
|-|-|
| `signal_list_request` | `SignalListRequest` |

#### list_task_executions_paginated()

```python
def list_task_executions_paginated(
    node_execution_identifier,
    limit,
    token,
    filters,
    sort_by,
) -> (list[flytekit.models.admin.task_execution.TaskExecution], Text)
```
| Parameter | Type |
|-|-|
| `node_execution_identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_task_ids_paginated()

```python
def list_task_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the tasks for a given project and domain. Filters can also be
specified.

> [!NOTE]

>    This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

> [!NOTE]

>    If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_tasks_paginated()

```python
def list_tasks_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> list[flytekit.models.task.Task], Text
```
This returns a page of task metadata for tasks in a given project and domain.  Optionally,
specifying a name will limit the results to only tasks with that name in the given project and domain.

> [!NOTE]
> This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### list_workflow_ids_paginated()

```python
def list_workflow_ids_paginated(
    project,
    domain,
    limit,
    token,
    sort_by,
) -> list[flytekit.models.common.NamedEntityIdentifier], Text
```
This returns a page of identifiers for the workflows for a given project and domain. Filters can also be
specified.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `limit` |  |
| `token` |  |
| `sort_by` |  |

#### list_workflows_paginated()

```python
def list_workflows_paginated(
    identifier,
    limit,
    token,
    filters,
    sort_by,
) -> list[flytekit.models.admin.workflow.Workflow], Text
```
This returns a page of workflow meta-information for workflows in a given project and domain.  Optionally,
specifying a name will limit the results to only workflows with that name in the given project and domain.

.. note ::

This is a paginated API.  Use the token field in the request to specify a page offset token.
The user of the API is responsible for providing this token.

.. note ::

If entries are added to the database between requests for different pages, it is possible to receive
entries on the second page that also appeared on the first.



| Parameter | Type |
|-|-|
| `identifier` |  |
| `limit` |  |
| `token` |  |
| `filters` |  |
| `sort_by` |  |

#### recover_execution()

```python
def recover_execution(
    id,
    name: str,
) -> flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
Recreates a previously-run workflow execution that will only start executing from the last known failure point.


| Parameter | Type |
|-|-|
| `id` |  |
| `name` | `str` |

#### register_project()

```python
def register_project(
    project,
) -> flyteidl.admin.project_pb2.ProjectRegisterResponse
```
Registers a project.


| Parameter | Type |
|-|-|
| `project` |  |

#### relaunch_execution()

```python
def relaunch_execution(
    id,
    name,
) -> flytekit.models.core.identifier.WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |

#### set_signal()

```python
def set_signal(
    signal_set_request: SignalSetRequest,
) -> SignalSetResponse
```
This sets a signal


| Parameter | Type |
|-|-|
| `signal_set_request` | `SignalSetRequest` |

#### terminate_execution()

```python
def terminate_execution(
    id,
    cause,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `cause` |  |

#### update_launch_plan()

```python
def update_launch_plan(
    id,
    state,
)
```
Updates a launch plan.  Currently, this can only be used to update a given launch plan's state (ACTIVE v.
INACTIVE) for schedules.  If a launch plan with a given project, domain, and name is set to ACTIVE,
then any other launch plan with the same project, domain, and name that was set to ACTIVE will be switched to
INACTIVE in one transaction.



| Parameter | Type |
|-|-|
| `id` |  |
| `state` |  |

#### update_named_entity()

```python
def update_named_entity(
    resource_type,
    id,
    metadata,
)
```
Updates the metadata associated with a named entity.  A named entity is designated a resource, e.g. a workflow,
task or launch plan specified by {project, domain, name} across all versions of the resource.



| Parameter | Type |
|-|-|
| `resource_type` |  |
| `id` |  |
| `metadata` |  |

#### update_project()

```python
def update_project(
    project,
) -> flyteidl.admin.project_pb2.ProjectUpdateResponse
```
Update an existing project specified by id.


| Parameter | Type |
|-|-|
| `project` |  |

#### update_project_domain_attributes()

```python
def update_project_domain_attributes(
    project,
    domain,
    matching_attributes,
)
```
Sets custom attributes for a project and domain combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `matching_attributes` |  |

#### update_workflow_attributes()

```python
def update_workflow_attributes(
    project,
    domain,
    workflow,
    matching_attributes,
)
```
Sets custom attributes for a project, domain, and workflow combination.


| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `workflow` |  |
| `matching_attributes` |  |

#### with_root_certificate()

```python
def with_root_certificate(
    cfg: PlatformConfig,
    root_cert_file: str,
) -> RawSynchronousFlyteClient
```
| Parameter | Type |
|-|-|
| `cfg` | `PlatformConfig` |
| `root_cert_file` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `raw` |  | {{< multiline >}}Gives access to the raw client
{{< /multiline >}} |
| `url` |  |  |

## flytekit.remote.remote.TextColumn

A column containing text.


```python
class TextColumn(
    text_format: str,
    style: typing.Union[str, ForwardRef('Style')],
    justify: typing.Literal['default', 'left', 'center', 'right', 'full'],
    markup: bool,
    highlighter: typing.Optional[rich.highlighter.Highlighter],
    table_column: typing.Optional[rich.table.Column],
)
```
| Parameter | Type |
|-|-|
| `text_format` | `str` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `justify` | `typing.Literal['default', 'left', 'center', 'right', 'full']` |
| `markup` | `bool` |
| `highlighter` | `typing.Optional[rich.highlighter.Highlighter]` |
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table. |
| [`render()`](#render) | Should return a renderable object. |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
) -> rich.text.Text
```
Should return a renderable object.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.remote.remote.TimeElapsedColumn

Renders time elapsed.


```python
class TimeElapsedColumn(
    table_column: typing.Optional[rich.table.Column],
)
```
| Parameter | Type |
|-|-|
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table. |
| [`render()`](#render) | Show time elapsed. |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
) -> rich.text.Text
```
Show time elapsed.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.remote.remote.TypeEngine

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

## flytekit.remote.remote.TypedInterface

```python
class TypedInterface(
    inputs,
    outputs,
)
```
Please note that this model is slightly incorrect, but is more user-friendly. The underlying inputs and
outputs are represented directly as Python dicts, rather than going through the additional VariableMap layer.



| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`promote_from_model()`](#promote_from_model) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
) -> TypedInterface
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.interface_pb2.TypedInterface` |

#### promote_from_model()

```python
def promote_from_model(
    model,
) -> TypedInterface
```
| Parameter | Type |
|-|-|
| `model` |  |

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
#### transform_interface_to_list()

```python
def transform_interface_to_list(
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
) -> TypedInterface
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed
python map like functions


| Parameter | Type |
|-|-|
| `bound_inputs` | `typing.Set[str]` |
| `excluded_inputs` | `typing.Set[str]` |

#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.remote.remote.WorkflowBase

```python
class WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow_metadata` | `WorkflowMetadata` |
| `workflow_metadata_defaults` | `WorkflowMetadataDefaults` |
| `python_interface` | `Interface` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `default_options` | `Optional[Options]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


#### compile()

```python
def compile(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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
### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.remote.remote.WorkflowExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


```python
class WorkflowExecutionGetDataResponse(
    inputs,
    outputs,
    full_inputs,
    full_outputs,
)
```
| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |
| `full_inputs` |  |
| `full_outputs` |  |

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
) -> WorkflowExecutionGetDataResponse
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
| `full_inputs` |  |  |
| `full_outputs` |  |  |
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.remote.remote.WorkflowExecutionIdentifier

```python
class WorkflowExecutionIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

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
    p,
) -> WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `p` |  |

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

## flytekit.remote.remote.WorkflowFailurePolicy

Defines the behavior for a workflow execution in the case of an observed node execution failure. By default, a
workflow execution will immediately enter a failed state if a component node fails.


## flytekit.remote.remote.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.remote.remote.timedelta

Difference between two datetime values.

timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

All arguments are optional and default to 0.
Arguments may be integers or floats, and may be positive or negative.


