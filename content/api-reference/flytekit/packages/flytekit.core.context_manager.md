---
title: flytekit.core.context_manager
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| [`BranchEvalMode`](.././flytekit.core.context_manager#flytekitcorecontext_managerbranchevalmode) | This is a 3-way class, with the None value meaning that we are not within a conditional context. |
| [`Checkpoint`](.././flytekit.core.context_manager#flytekitcorecontext_managercheckpoint) | Base class for Checkpoint system. |
| [`CompilationState`](.././flytekit.core.context_manager#flytekitcorecontext_managercompilationstate) | Compilation state is used during the compilation of a workflow or task. |
| [`Config`](.././flytekit.core.context_manager#flytekitcorecontext_managerconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`ContextVar`](.././flytekit.core.context_manager#flytekitcorecontext_managercontextvar) |  |
| [`Enum`](.././flytekit.core.context_manager#flytekitcorecontext_managerenum) | Create a collection of name/value pairs. |
| [`ExecutionParameters`](.././flytekit.core.context_manager#flytekitcorecontext_managerexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`ExecutionState`](.././flytekit.core.context_manager#flytekitcorecontext_managerexecutionstate) | This is the context that is active when executing a task or a local workflow. |
| [`FileAccessProvider`](.././flytekit.core.context_manager#flytekitcorecontext_managerfileaccessprovider) | This is the class that is available through the FlyteContext and can be used for persisting data to the remote. |
| [`FlyteContext`](.././flytekit.core.context_manager#flytekitcorecontext_managerflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit.core.context_manager#flytekitcorecontext_managerflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteEntities`](.././flytekit.core.context_manager#flytekitcorecontext_managerflyteentities) | This is a global Object that tracks various tasks and workflows that are declared within a VM during the. |
| [`FrameType`](.././flytekit.core.context_manager#flytekitcorecontext_managerframetype) |  |
| [`Node`](.././flytekit.core.context_manager#flytekitcorecontext_managernode) | This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like. |
| [`OutputMetadata`](.././flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadata) |  |
| [`OutputMetadataTracker`](.././flytekit.core.context_manager#flytekitcorecontext_manageroutputmetadatatracker) | This class is for the users to set arbitrary metadata on output literals. |
| [`SecretsConfig`](.././flytekit.core.context_manager#flytekitcorecontext_managersecretsconfig) | Configuration for secrets. |
| [`SecretsManager`](.././flytekit.core.context_manager#flytekitcorecontext_managersecretsmanager) | This provides a secrets resolution logic at runtime. |
| [`SerializableToString`](.././flytekit.core.context_manager#flytekitcorecontext_managerserializabletostring) | This protocol is used by the Artifact create_from function. |
| [`SerializationSettings`](.././flytekit.core.context_manager#flytekitcorecontext_managerserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`SyncCheckpoint`](.././flytekit.core.context_manager#flytekitcorecontext_managersynccheckpoint) | This class is NOT THREAD-SAFE!. |
| [`WorkflowExecutionIdentifier`](.././flytekit.core.context_manager#flytekitcorecontext_managerworkflowexecutionidentifier) |  |
| [`datetime`](.././flytekit.core.context_manager#flytekitcorecontext_managerdatetime) | datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]]). |
| [`timezone`](.././flytekit.core.context_manager#flytekitcorecontext_managertimezone) | Fixed offset from UTC implementation of tzinfo. |

### Methods

| Method | Description |
|-|-|
| [`contextmanager()`](#contextmanager) | @contextmanager decorator. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`field()`](#field) | Return an object to identify dataclass fields. |


### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |
| `default_local_file_access_provider` | `FileAccessProvider` |  |
| `developer_logger` | `Logger` |  |
| `flyte_context_Var` | `ContextVar` |  |
| `user_space_logger` | `Logger` |  |

## Methods

#### contextmanager()

```python
def contextmanager(
    func,
)
```
@contextmanager decorator.

Typical usage:

@contextmanager
def some_generator(<arguments>):
<setup>
try:
yield <value>
finally:
<cleanup>

This makes this:

with some_generator(<arguments>) as <variable>:
<body>

equivalent to this:

<setup>
try:
<variable> = <value>
<body>
finally:
<cleanup>


| Parameter | Type |
|-|-|
| `func` |  |

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

#### field()

```python
def field(
    default,
    default_factory,
    init,
    repr,
    hash,
    compare,
    metadata,
    kw_only,
)
```
Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.


| Parameter | Type |
|-|-|
| `default` |  |
| `default_factory` |  |
| `init` |  |
| `repr` |  |
| `hash` |  |
| `compare` |  |
| `metadata` |  |
| `kw_only` |  |

## flytekit.core.context_manager.BranchEvalMode

This is a 3-way class, with the None value meaning that we are not within a conditional context. The other two
values are
* Active - This means that the next ``then`` should run
* Skipped - The next ``then`` should not run


## flytekit.core.context_manager.Checkpoint

Base class for Checkpoint system. Checkpoint system allows reading and writing custom checkpoints from user
scripts


### Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) | . |
| [`write()`](#write) | This will overwrite the checkpoint. |


#### prev_exists()

```python
def prev_exists()
```
#### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


#### restore()

```python
def restore(
    path: typing.Union[pathlib._local.Path, str],
) -> typing.Optional[pathlib._local.Path]
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

.. note:

Download will not be performed, if the checkpoint was previously restored. The method will return the
previously downloaded path.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str]` |

#### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` |

#### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |

## flytekit.core.context_manager.CompilationState

Compilation state is used during the compilation of a workflow or task. It stores the nodes that were
created when walking through the workflow graph.

Attributes:
prefix (str): This is because we may one day want to be able to have subworkflows inside other workflows. If
users choose to not specify their node names, then we can end up with multiple "n0"s. This prefix allows
us to give those nested nodes a distinct name, as well as properly identify them in the workflow.
mode (int): refer to :py:class:`flytekit.extend.ExecutionState.Mode`
task_resolver (Optional[TaskResolverMixin]): Please see :py:class:`flytekit.extend.TaskResolverMixin`
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

## flytekit.core.context_manager.Config

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

## flytekit.core.context_manager.ContextVar

## flytekit.core.context_manager.Enum

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


## flytekit.core.context_manager.ExecutionParameters

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

## flytekit.core.context_manager.FileAccessProvider

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

## flytekit.core.context_manager.FlyteContext

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

## flytekit.core.context_manager.FlyteContextManager

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

## flytekit.core.context_manager.FlyteEntities

This is a global Object that tracks various tasks and workflows that are declared within a VM during the
registration process


## flytekit.core.context_manager.FrameType

## flytekit.core.context_manager.Node

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

## flytekit.core.context_manager.SecretsConfig

Configuration for secrets.



```python
class SecretsConfig(
    env_prefix: str,
    default_dir: str,
    file_prefix: str,
)
```
| Parameter | Type |
|-|-|
| `env_prefix` | `str` |
| `default_dir` | `str` |
| `file_prefix` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable or from config file. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> SecretsConfig
```
Reads from environment variable or from config file


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

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

## flytekit.core.context_manager.SerializationSettings

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

## flytekit.core.context_manager.SyncCheckpoint

This class is NOT THREAD-SAFE!
Sync Checkpoint, will synchronously checkpoint a user given file or folder.
It will also synchronously download / restore previous checkpoints, when restore is invoked.

TODO: Implement an async checkpoint system


```python
class SyncCheckpoint(
    checkpoint_dest: str,
    checkpoint_src: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `checkpoint_dest` | `str` |
| `checkpoint_src` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) | . |
| [`write()`](#write) | This will overwrite the checkpoint. |


#### prev_exists()

```python
def prev_exists()
```
#### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


#### restore()

```python
def restore(
    path: typing.Union[pathlib._local.Path, str, NoneType],
) -> typing.Optional[pathlib._local.Path]
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

.. note:

Download will not be performed, if the checkpoint was previously restored. The method will return the
previously downloaded path.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str, NoneType]` |

#### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` |

#### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |

## flytekit.core.context_manager.WorkflowExecutionIdentifier

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
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> WorkflowExecutionIdentifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `base_model` |  |

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

## flytekit.core.context_manager.datetime

datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

The year, month and day arguments are required. tzinfo may be None, or an
instance of a tzinfo subclass. The remaining arguments may be ints.


## flytekit.core.context_manager.timezone

Fixed offset from UTC implementation of tzinfo.


