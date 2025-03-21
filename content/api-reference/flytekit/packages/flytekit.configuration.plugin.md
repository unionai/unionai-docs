---
title: flytekit.configuration.plugin
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.configuration.plugin

Defines a plugin API allowing other libraries to modify the behavior of flytekit.

Libraries can register by defining an object that follows the same API as FlytekitPlugin
and providing an entrypoint with the group name "flytekit.plugin". In `setuptools`,
you can specific them with:

```python
setup(entry_points={
    "flytekit.configuration.plugin": ["my_plugin=my_module:MyCustomPlugin"]
})
```

or in pyproject.toml:

```toml
[project.entry-points."flytekit.configuration.plugin"]
my_plugin = "my_module:MyCustomPlugin"
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`CachePolicy`](.././flytekit.configuration.plugin#flytekitconfigurationplugincachepolicy) | Base class for protocol classes. |
| [`Config`](.././flytekit.configuration.plugin#flytekitconfigurationpluginconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`FlyteRemote`](.././flytekit.configuration.plugin#flytekitconfigurationpluginflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`FlytekitPlugin`](.././flytekit.configuration.plugin#flytekitconfigurationpluginflytekitplugin) | None. |
| [`FlytekitPluginProtocol`](.././flytekit.configuration.plugin#flytekitconfigurationpluginflytekitpluginprotocol) | Base class for protocol classes. |
| [`Group`](.././flytekit.configuration.plugin#flytekitconfigurationplugingroup) | A group allows a command to have subcommands attached. |
| [`Protocol`](.././flytekit.configuration.plugin#flytekitconfigurationpluginprotocol) | Base class for protocol classes. |

## flytekit.configuration.plugin.CachePolicy

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
def CachePolicy(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`get_version()`](#get_version) | None |


#### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
):
```
| Parameter | Type |
|-|-|
| `salt` | `str` |
| `params` | `flytekit.core.cache.VersionParameters` |

## flytekit.configuration.plugin.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task



```python
def Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
):
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
| [`auto()`](#auto) | Automatically constructs the Config Object |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox` |
| [`with_params()`](#with_params) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

## flytekit.configuration.plugin.FlyteRemote

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
def FlyteRemote(
    config: Config,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: typing.Optional[bool],
    kwargs,
):
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
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated |
| [`approve()`](#approve) |  |
| [`auto()`](#auto) | None |
| [`download()`](#download) | Download the data to the specified location |
| [`execute()`](#execute) | Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity |
| [`execute_local_launch_plan()`](#execute_local_launch_plan) | Execute a locally defined `LaunchPlan` |
| [`execute_local_task()`](#execute_local_task) | Execute a @task-decorated function or TaskTemplate task |
| [`execute_local_workflow()`](#execute_local_workflow) | Execute an @workflow decorated function |
| [`execute_reference_launch_plan()`](#execute_reference_launch_plan) | Execute a ReferenceLaunchPlan |
| [`execute_reference_task()`](#execute_reference_task) | Execute a ReferenceTask |
| [`execute_reference_workflow()`](#execute_reference_workflow) | Execute a ReferenceWorkflow |
| [`execute_remote_task_lp()`](#execute_remote_task_lp) | Execute a FlyteTask, or FlyteLaunchplan |
| [`execute_remote_wf()`](#execute_remote_wf) | Execute a FlyteWorkflow |
| [`fast_package()`](#fast_package) | Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location |
| [`fast_register_workflow()`](#fast_register_workflow) | Use this method to register a workflow with zip mode |
| [`fetch_active_launchplan()`](#fetch_active_launchplan) | Returns the active version of the launch plan if it exists or returns None |
| [`fetch_execution()`](#fetch_execution) | Fetch a workflow execution entity from flyte admin |
| [`fetch_launch_plan()`](#fetch_launch_plan) | Fetch a launchplan entity from flyte admin |
| [`fetch_task()`](#fetch_task) | Fetch a task entity from flyte admin |
| [`fetch_task_lazy()`](#fetch_task_lazy) | Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`fetch_workflow()`](#fetch_workflow) | Fetch a workflow entity from flyte admin |
| [`fetch_workflow_lazy()`](#fetch_workflow_lazy) | Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`find_launch_plan()`](#find_launch_plan) | None |
| [`find_launch_plan_for_node()`](#find_launch_plan_for_node) | None |
| [`for_endpoint()`](#for_endpoint) | None |
| [`for_sandbox()`](#for_sandbox) | None |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted |
| [`generate_console_url()`](#generate_console_url) | Generate a Flyteconsole URL for the given Flyte remote endpoint |
| [`get()`](#get) | General function that works with flyte tiny urls |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) | None |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin |
| [`list_signals()`](#list_signals) |  |
| [`list_tasks_by_version()`](#list_tasks_by_version) | None |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities |
| [`recent_executions()`](#recent_executions) | None |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow |
| [`reject()`](#reject) |  |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration |
| [`set_input()`](#set_input) |  |
| [`set_signal()`](#set_signal) |  |
| [`sync()`](#sync) | This function was previously a singledispatchmethod |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state |
| [`terminate()`](#terminate) | Terminate a workflow execution |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service |
| [`wait()`](#wait) | Wait for an execution to finish |


#### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
| client |  |  |
| config |  |  |
| context |  |  |
| default_domain |  |  |
| default_project |  |  |
| file_access |  |  |
| interactive_mode_enabled |  |  |

## flytekit.configuration.plugin.FlytekitPlugin

### Methods

| Method | Description |
|-|-|
| [`configure_pyflyte_cli()`](#configure_pyflyte_cli) | Configure pyflyte's CLI |
| [`get_auth_success_html()`](#get_auth_success_html) | Get default success html |
| [`get_default_cache_policies()`](#get_default_cache_policies) | Get default cache policies for tasks |
| [`get_default_image()`](#get_default_image) | Get default image |
| [`get_remote()`](#get_remote) | Get FlyteRemote object for CLI session |
| [`secret_requires_group()`](#secret_requires_group) | Return True if secrets require group entry during registration time |


#### configure_pyflyte_cli()

```python
def configure_pyflyte_cli(
    main: click.core.Group,
):
```
Configure pyflyte's CLI.


| Parameter | Type |
|-|-|
| `main` | `click.core.Group` |

#### get_auth_success_html()

```python
def get_auth_success_html(
    endpoint: str,
):
```
Get default success html. Return None to use flytekit's default success html.


| Parameter | Type |
|-|-|
| `endpoint` | `str` |

#### get_default_cache_policies()

```python
def get_default_cache_policies()
```
Get default cache policies for tasks.


#### get_default_image()

```python
def get_default_image()
```
Get default image. Return None to use the images from flytekit.configuration.DefaultImages


#### get_remote()

```python
def get_remote(
    config: typing.Optional[str],
    project: str,
    domain: str,
    data_upload_location: typing.Optional[str],
):
```
Get FlyteRemote object for CLI session.


| Parameter | Type |
|-|-|
| `config` | `typing.Optional[str]` |
| `project` | `str` |
| `domain` | `str` |
| `data_upload_location` | `typing.Optional[str]` |

#### secret_requires_group()

```python
def secret_requires_group()
```
Return True if secrets require group entry during registration time.


## flytekit.configuration.plugin.FlytekitPluginProtocol

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
def FlytekitPluginProtocol(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`configure_pyflyte_cli()`](#configure_pyflyte_cli) | Configure pyflyte's CLI |
| [`get_auth_success_html()`](#get_auth_success_html) | Get default success html for auth |
| [`get_default_cache_policies()`](#get_default_cache_policies) | Get default cache policies for tasks |
| [`get_default_image()`](#get_default_image) | Get default image |
| [`get_remote()`](#get_remote) | Get FlyteRemote object for CLI session |
| [`secret_requires_group()`](#secret_requires_group) | Return True if secrets require group entry |


#### configure_pyflyte_cli()

```python
def configure_pyflyte_cli(
    main: click.core.Group,
):
```
Configure pyflyte's CLI.


| Parameter | Type |
|-|-|
| `main` | `click.core.Group` |

#### get_auth_success_html()

```python
def get_auth_success_html(
    endpoint: str,
):
```
Get default success html for auth. Return None to use flytekit's default success html.


| Parameter | Type |
|-|-|
| `endpoint` | `str` |

#### get_default_cache_policies()

```python
def get_default_cache_policies()
```
Get default cache policies for tasks.


#### get_default_image()

```python
def get_default_image()
```
Get default image. Return None to use the images from flytekit.configuration.DefaultImages


#### get_remote()

```python
def get_remote(
    config: typing.Optional[str],
    project: str,
    domain: str,
    data_upload_location: typing.Optional[str],
):
```
Get FlyteRemote object for CLI session.


| Parameter | Type |
|-|-|
| `config` | `typing.Optional[str]` |
| `project` | `str` |
| `domain` | `str` |
| `data_upload_location` | `typing.Optional[str]` |

#### secret_requires_group()

```python
def secret_requires_group()
```
Return True if secrets require group entry.


## flytekit.configuration.plugin.Group

A group allows a command to have subcommands attached. This is
the most common way to implement nesting in Click.



```python
def Group(
    name: typing.Optional[str],
    commands: typing.Union[typing.MutableMapping[str, click.core.Command], typing.Sequence[click.core.Command], NoneType],
    attrs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |
| `commands` | `typing.Union[typing.MutableMapping[str, click.core.Command], typing.Sequence[click.core.Command], NoneType]` |
| `attrs` | `typing.Any` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter |
| [`get_command()`](#get_command) | Given a context and a command name, this returns a |
| [`get_help()`](#get_help) | Formats the help into a string and returns it |
| [`get_help_option()`](#get_help_option) | Returns the help option object |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option |
| [`get_params()`](#get_params) | None |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should |
| [`main()`](#main) | This is the way to invoke a script with all the bells and |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser |
| [`resolve_command()`](#resolve_command) | None |
| [`result_callback()`](#result_callback) | Adds a result callback to the command |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
):
```
Registers another :class:`Command` with this group.  If the name
is not provided, the name of the command is used.


| Parameter | Type |
|-|-|
| `cmd` | `click.core.Command` |
| `name` | `typing.Optional[str]` |

#### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
):
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### command()

```python
def command(
    args: `*args`,
    kwargs: `**kwargs`,
):
```
A shortcut decorator for declaring and attaching a command to
the group. This takes the same arguments as :func:`command` and
immediately registers the created command with this group by
calling :meth:`add_command`.

To customize the command class used, set the
:attr:`command_class` attribute.

.. versionchanged:: 8.1
This decorator can be applied without parentheses.

.. versionchanged:: 8.0
Added the :attr:`command_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### format_commands()

```python
def format_commands(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Extra format methods for multi methods that adds all the commands
after the options.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_epilog()

```python
def format_epilog(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Writes the epilog into the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_help()

```python
def format_help(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Writes the help into the formatter if it exists.

This is a low-level method called by :meth:`get_help`.

This calls the following methods:

-   :meth:`format_usage`
-   :meth:`format_help_text`
-   :meth:`format_options`
-   :meth:`format_epilog`


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_help_text()

```python
def format_help_text(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Writes the help text to the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_options()

```python
def format_options(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Writes all the options into the formatter if they exist.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_usage()

```python
def format_usage(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
):
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### get_command()

```python
def get_command(
    ctx: click.core.Context,
    cmd_name: str,
):
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `cmd_name` | `str` |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
):
```
Formats the help into a string and returns it.

Calls :meth:`format_help` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option()

```python
def get_help_option(
    ctx: click.core.Context,
):
```
Returns the help option object.

Unless ``add_help_option`` is ``False``.

.. versionchanged:: 8.1.8
The help option is now cached to avoid creating it multiple times.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option_names()

```python
def get_help_option_names(
    ctx: click.core.Context,
):
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
):
```
Gets short help for the command or makes it by shortening the
long help string.


| Parameter | Type |
|-|-|
| `limit` | `int` |

#### get_usage()

```python
def get_usage(
    ctx: click.core.Context,
):
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### group()

```python
def group(
    args: `*args`,
    kwargs: `**kwargs`,
):
```
A shortcut decorator for declaring and attaching a group to
the group. This takes the same arguments as :func:`group` and
immediately registers the created group with this group by
calling :meth:`add_command`.

To customize the group class used, set the :attr:`group_class`
attribute.

.. versionchanged:: 8.1
This decorator can be applied without parentheses.

.. versionchanged:: 8.0
Added the :attr:`group_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
):
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx: click.core.Context,
):
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
):
```
This is the way to invoke a script with all the bells and
whistles as a command line application.  This will always terminate
the application after a call.  If this is not wanted, ``SystemExit``
needs to be caught.

This method is also available by directly calling the instance of
a :class:`Command`.



| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `prog_name` | `typing.Optional[str]` |
| `complete_var` | `typing.Optional[str]` |
| `standalone_mode` | `bool` |
| `windows_expand_args` | `bool` |
| `extra` | `typing.Any` |

#### make_context()

```python
def make_context(
    info_name: typing.Optional[str],
    args: `*args`,
    parent: typing.Optional[click.core.Context],
    extra: typing.Any,
):
```
This function when given an info name and arguments will kick
off the parsing and create a new :class:`Context`.  It does not
invoke the actual command callback though.

To quickly customize the context class used without overriding
this method, set the :attr:`context_class` attribute.



| Parameter | Type |
|-|-|
| `info_name` | `typing.Optional[str]` |
| `args` | ``*args`` |
| `parent` | `typing.Optional[click.core.Context]` |
| `extra` | `typing.Any` |

#### make_parser()

```python
def make_parser(
    ctx: click.core.Context,
):
```
Creates the underlying option parser for this command.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### parse_args()

```python
def parse_args(
    ctx: click.core.Context,
    args: `*args`,
):
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### resolve_command()

```python
def resolve_command(
    ctx: click.core.Context,
    args: `*args`,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
):
```
Adds a result callback to the command.  By default if a
result callback is already registered this will chain them but
this can be disabled with the `replace` parameter.  The result
callback is invoked with the return value of the subcommand
(or the list of return values from all subcommands if chaining
is enabled) as well as the parameters as they would be passed
to the main callback.

Example::

@click.group()
@click.option('-i', '--input', default=23)
def cli(input):
return 42

@cli.result_callback()
def process_result(result, input):
return result + input



| Parameter | Type |
|-|-|
| `replace` | `bool` |

#### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
):
```
Return a list of completions for the incomplete value. Looks
at the names of options, subcommands, and chained
multi-commands.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `incomplete` | `str` |

#### to_info_dict()

```python
def to_info_dict(
    ctx: click.core.Context,
):
```
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

## flytekit.configuration.plugin.Protocol

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


