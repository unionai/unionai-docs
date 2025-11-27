---
title: UnionRemote
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# UnionRemote

**Package:** `union`

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
class UnionRemote(
    config: typing.Optional[Union[Config, str]],
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


| Parameter | Type | Description |
|-|-|-|
| `config` | `typing.Optional[Union[Config, str]]` | |
| `default_project` | `typing.Optional[str]` | default project to use when fetching or executing flyte entities. |
| `default_domain` | `typing.Optional[str]` | default domain to use when fetching or executing flyte entities. |
| `data_upload_location` | `str` | this is where all the default data will be uploaded when providing inputs. The default location - `s3://my-s3-bucket/data` works for sandbox/demo environment. Please override this for non-sandbox cases. |
| `interactive_mode_enabled` | `typing.Optional[bool]` | If set to True, the FlyteRemote will pickle the task/workflow, if False, it will not. If set to None, then it will automatically detect if it is running in an interactive environment like a Jupyter notebook and enable interactive mode. |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated. |
| [`approve()`](#approve) |  |
| [`async_channel()`](#async_channel) |  |
| [`auto()`](#auto) |  |
| [`create_artifact()`](#create_artifact) | Create an artifact in FlyteAdmin. |
| [`deactivate_launchplan()`](#deactivate_launchplan) | Given a launchplan, deactivate it, all previous versions are deactivated. |
| [`deploy_app()`](#deploy_app) | Deploy an application. |
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
| [`from_api_key()`](#from_api_key) | Call this if you want to directly instantiate a UnionRemote from an API key. |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted. |
| [`generate_console_url()`](#generate_console_url) | Generate a UnionAI console URL for the given Flyte remote endpoint. |
| [`get()`](#get) | General function that works with flyte tiny urls. |
| [`get_artifact()`](#get_artifact) | Get the specified artifact. |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin. |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution. |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) |  |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan. |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin. |
| [`list_signals()`](#list_signals) |  |
| [`list_tasks_by_version()`](#list_tasks_by_version) |  |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities. |
| [`recent_executions()`](#recent_executions) |  |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options. |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode. |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote. |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow. |
| [`reject()`](#reject) |  |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration. |
| [`search_artifacts()`](#search_artifacts) |  |
| [`set_input()`](#set_input) |  |
| [`set_signal()`](#set_signal) |  |
| [`stop_app()`](#stop_app) | Stop an application. |
| [`stream_execution_events()`](#stream_execution_events) | Stream execution events from the given tenant. |
| [`sync()`](#sync) | This function was previously a singledispatchmethod. |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state. |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution. |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state. |
| [`terminate()`](#terminate) | Terminate a workflow execution. |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service. |
| [`wait()`](#wait) | Wait for an execution to finish. |


### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
)
```
Given a launchplan, activate it, all previous versions are deactivated.


| Parameter | Type | Description |
|-|-|-|
| `ident` | `Identifier` | |

### approve()

```python
def approve(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The name of the signal, this is the key used in the approve() or wait_for_input() call. |
| `execution_name` | `str` | The name of the execution. This is the tail-end of the URL when looking at the workflow execution. |
| `project` | `str` | The execution project, will default to the Remote's default project. |
| `domain` | `str` | The execution domain, will default to the Remote's default domain. |

### async_channel()

```python
def async_channel()
```
### auto()

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
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` | |
| `default_project` | `typing.Optional[str]` | |
| `default_domain` | `typing.Optional[str]` | |
| `data_upload_location` | `str` | |
| `interactive_mode_enabled` | `bool` | |
| `kwargs` | `**kwargs` | |

### create_artifact()

```python
def create_artifact(
    artifact: Artifact,
) -> Artifact
```
Create an artifact in FlyteAdmin.



| Parameter | Type | Description |
|-|-|-|
| `artifact` | `Artifact` | The artifact to create. :return: The artifact as persisted in the service. |

### deactivate_launchplan()

```python
def deactivate_launchplan(
    ident: Identifier,
)
```
Given a launchplan, deactivate it, all previous versions are deactivated.


| Parameter | Type | Description |
|-|-|-|
| `ident` | `Identifier` | |

### deploy_app()

```python
def deploy_app(
    app: App,
    project: Optional[str],
    domain: Optional[str],
) -> AppIDL
```
Deploy an application.



| Parameter | Type | Description |
|-|-|-|
| `app` | `App` | Application to deploy. |
| `project` | `Optional[str]` | Domain name. If None, uses default_domain. :return: The App IDL for the deployed application. |
| `domain` | `Optional[str]` | |

### download()

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



| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Union[LiteralsResolver, Literal, LiteralMap]` | data to be downloaded |
| `download_to` | `str` | location to download to (str) that should be a valid path |
| `recursive` | `bool` | if the data is a LiteralsResolver or LiteralMap, then this flag will recursively download |

### execute()

```python
def execute(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity],
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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



| Parameter | Type | Description |
|-|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity]` | entity to execute |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | dictionary mapping argument names to values |
| `project` | `str` | execute entity in this project. If entity doesn't exist in the project, register the entity first before executing. |
| `domain` | `str` | execute entity in this domain. If entity doesn't exist in the domain, register the entity first before executing. |
| `name` | `str` | execute entity using this name. If not None, use this value instead of ``entity.name`` |
| `version` | `str` | execute entity using this version. If None, uses auto-generated value. |
| `execution_name` | `typing.Optional[str]` | name of the execution. If None, uses auto-generated value. |
| `execution_name_prefix` | `typing.Optional[str]` | execution prefix to use. If provided, a random suffix will be appended |
| `image_config` | `typing.Optional[ImageConfig]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | if True, waits for execution to complete |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | Python types to be passed to the TypeEngine so that it knows how to properly convert the input values for the execution into Flyte literals. If missing, will default to first guessing the type using the type engine, and then to ``type(v)``. Providing the correct Python types is particularly important if the inputs are containers like lists or maps, or if the Python type is one of the more complex Flyte provided classes (like a StructuredDataset that's annotated with columns). |
| `overwrite_cache` | `typing.Optional[bool]` | Allows for all cached values of a workflow and its tasks to be overwritten for a single execution. If enabled, all calculations are performed even if cached results would be available, overwriting the stored data once execution finishes successfully. |
| `interruptible` | `typing.Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity. |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | Environment variables to be set for the execution. |
| `tags` | `typing.Optional[typing.List[str]]` | Tags to be set for the execution. |
| `cluster_pool` | `typing.Optional[str]` | Specify cluster pool on which newly created execution should be placed. |
| `execution_cluster_label` | `typing.Optional[str]` | Specify label of cluster(s) on which newly created execution should be placed. |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | Optionally provide serialization settings, in case the entity being run needs to first be registered. If not provided, a default will be used.  &gt; [!NOTE] &gt; The ``name`` and ``version`` arguments do not apply to ``FlyteTask``, ``FlyteLaunchPlan``, and ``FlyteWorkflow`` entity inputs. These values are determined by referencing the entity identifier values. |

### execute_local_launch_plan()

```python
def execute_local_launch_plan(
    entity: LaunchPlan,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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



| Parameter | Type | Description |
|-|-|-|
| `entity` | `LaunchPlan` | The locally defined launch plan object |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Inputs to be passed into the execution as a dict with Python native values. |
| `version` | `str` | The version to look up/register the launch plan (if not already exists) |
| `project` | `typing.Optional[str]` | The same as version, but will default to the Remote object's project |
| `domain` | `typing.Optional[str]` | The same as version, but will default to the Remote object's domain |
| `name` | `typing.Optional[str]` | The same as version, but will default to the entity's name |
| `execution_name` | `typing.Optional[str]` | If specified, will be used as the execution name instead of randomly generating. |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | Options to be passed into the execution. |
| `wait` | `bool` | If True, will wait for the execution to complete before returning. |
| `overwrite_cache` | `typing.Optional[bool]` | If True, will overwrite the cache. |
| `interruptible` | `typing.Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity. |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | Environment variables to be passed into the execution. |
| `tags` | `typing.Optional[typing.List[str]]` | Tags to be passed into the execution. |
| `cluster_pool` | `typing.Optional[str]` | Specify cluster pool on which newly created execution should be placed. |
| `execution_cluster_label` | `typing.Optional[str]` | Specify label of cluster(s) on which newly created execution should be placed. |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | Optionally provide serialization settings, in case the entity being run needs  :return: FlyteWorkflowExecution object |

### execute_local_task()

```python
def execute_local_task(
    entity: PythonTask,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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



| Parameter | Type | Description |
|-|-|-|
| `entity` | `PythonTask` | local task entity. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | register the task, which requires compiling the task, before running it. |
| `project` | `str` | The execution project, will default to the Remote's default project. |
| `domain` | `str` | The execution domain, will default to the Remote's default domain. |
| `name` | `str` | specific name of the task to run. |
| `version` | `str` | specific version of the task to run, default is a special string ``latest``, which implies latest version by time |
| `execution_name` | `typing.Optional[str]` | If provided, will use this name for the execution. |
| `execution_name_prefix` | `typing.Optional[str]` | If provided, will use this prefix for the execution name. |
| `image_config` | `typing.Optional[ImageConfig]` | If provided, will use this image config in the pod. |
| `wait` | `bool` | If True, will wait for the execution to complete before returning. |
| `overwrite_cache` | `typing.Optional[bool]` | If True, will overwrite the cache. |
| `interruptible` | `typing.Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity. |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | Environment variables to set for the execution. |
| `tags` | `typing.Optional[typing.List[str]]` | Tags to set for the execution. |
| `cluster_pool` | `typing.Optional[str]` | Specify cluster pool on which newly created execution should be placed. |
| `execution_cluster_label` | `typing.Optional[str]` | Specify label of cluster(s) on which newly created execution should be placed. |
| `options` | `typing.Optional[Options]` | Options to customize the execution. |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | If the task needs to be registered, this can be passed in.  :return: FlyteWorkflowExecution object. |

### execute_local_workflow()

```python
def execute_local_workflow(
    entity: WorkflowBase,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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



| Parameter | Type | Description |
|-|-|-|
| `entity` | `WorkflowBase` | The workflow to execute |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Input dictionary |
| `project` | `str` | Project to execute in |
| `domain` | `str` | Domain to execute in |
| `name` | `str` | Optional name override for the workflow |
| `version` | `str` | Optional version for the workflow |
| `execution_name` | `typing.Optional[str]` | Optional name for the execution |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `image_config` | `typing.Optional[ImageConfig]` | Optional image config override |
| `options` | `typing.Optional[Options]` | Optional Options object |
| `wait` | `bool` | Whether to wait for execution completion |
| `overwrite_cache` | `typing.Optional[bool]` | If True, will overwrite the cache |
| `interruptible` | `typing.Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | Environment variables to set for the execution |
| `tags` | `typing.Optional[typing.List[str]]` | Tags to set for the execution |
| `cluster_pool` | `typing.Optional[str]` | Specify cluster pool on which newly created execution should be placed |
| `execution_cluster_label` | `typing.Optional[str]` | Specify label of cluster(s) on which newly created execution should be placed |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | Optionally provide serialization settings, in case the entity being run needs to be registered  :return: FlyteWorkflowExecution object |

### execute_reference_launch_plan()

```python
def execute_reference_launch_plan(
    entity: ReferenceLaunchPlan,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `ReferenceLaunchPlan` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `execution_name` | `typing.Optional[str]` | |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | |
| `tags` | `typing.Optional[typing.List[str]]` | |
| `cluster_pool` | `typing.Optional[str]` | |
| `execution_cluster_label` | `typing.Optional[str]` | |

### execute_reference_task()

```python
def execute_reference_task(
    entity: ReferenceTask,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `ReferenceTask` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `execution_name` | `typing.Optional[str]` | |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | |
| `tags` | `typing.Optional[typing.List[str]]` | |
| `cluster_pool` | `typing.Optional[str]` | |
| `execution_cluster_label` | `typing.Optional[str]` | |

### execute_reference_workflow()

```python
def execute_reference_workflow(
    entity: ReferenceWorkflow,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `ReferenceWorkflow` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `execution_name` | `typing.Optional[str]` | |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | |
| `tags` | `typing.Optional[typing.List[str]]` | |
| `cluster_pool` | `typing.Optional[str]` | |
| `execution_cluster_label` | `typing.Optional[str]` | |

### execute_remote_task_lp()

```python
def execute_remote_task_lp(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan],
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan]` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `execution_name` | `typing.Optional[str]` | |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | |
| `tags` | `typing.Optional[typing.List[str]]` | |
| `cluster_pool` | `typing.Optional[str]` | |
| `execution_cluster_label` | `typing.Optional[str]` | |

### execute_remote_wf()

```python
def execute_remote_wf(
    entity: FlyteWorkflow,
    inputs: typing.Optional[typing.Dict[str, typing.Any]],
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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `FlyteWorkflow` | |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `execution_name` | `typing.Optional[str]` | |
| `execution_name_prefix` | `typing.Optional[str]` | |
| `options` | `typing.Optional[Options]` | |
| `wait` | `bool` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |
| `overwrite_cache` | `typing.Optional[bool]` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | |
| `tags` | `typing.Optional[typing.List[str]]` | |
| `cluster_pool` | `typing.Optional[str]` | |
| `execution_cluster_label` | `typing.Optional[str]` | |

### fast_package()

```python
def fast_package(
    root: os.PathLike,
    deref_symlinks: bool,
    output: str,
    options: typing.Optional[FastPackageOptions],
) -> typing.Tuple[bytes, str]
```
Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location


| Parameter | Type | Description |
|-|-|-|
| `root` | `os.PathLike` | path to the root of the package system that should be uploaded |
| `deref_symlinks` | `bool` | if symlinks should be dereferenced. Defaults to True |
| `output` | `str` | output path. Optional, will default to a tempdir |
| `options` | `typing.Optional[FastPackageOptions]` | additional options to customize fast_package behavior :return: md5_bytes, url |

### fast_register_workflow()

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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `WorkflowBase` | The workflow to be registered |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | The serialization settings to be used |
| `version` | `typing.Optional[str]` | version for the entity to be registered as |
| `default_launch_plan` | `typing.Optional[bool]` | This should be true if a default launch plan should be created for the workflow |
| `options` | `typing.Optional[Options]` | Additional execution options that can be configured for the default launchplan |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` | Options to customize copying behavior :return: |

### fetch_active_launchplan()

```python
def fetch_active_launchplan(
    project: str,
    domain: str,
    name: str,
) -> typing.Optional[FlyteLaunchPlan]
```
Returns the active version of the launch plan if it exists or returns None


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |

### fetch_execution()

```python
def fetch_execution(
    project: str,
    domain: str,
    name: str,
) -> FlyteWorkflowExecution
```
Fetch a workflow execution entity from flyte admin.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | fetch entity from this project. If None, uses the default_project attribute. |
| `domain` | `str` | fetch entity from this domain. If None, uses the default_domain attribute. |
| `name` | `str` | fetch entity with matching name. :returns: :class:`~flytekit.remote.workflow_execution.FlyteWorkflowExecution`  :raises: FlyteAssertion if name is None |

### fetch_launch_plan()

```python
def fetch_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteLaunchPlan
```
Fetch a launchplan entity from flyte admin.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | fetch entity from this project. If None, uses the default_project attribute. |
| `domain` | `str` | fetch entity from this domain. If None, uses the default_domain attribute. |
| `name` | `str` | fetch entity with matching name. |
| `version` | `str` | fetch entity with matching version. If None, gets the latest version of the entity. :returns: :class:`~flytekit.remote.launch_plan.FlyteLaunchPlan`  :raises: FlyteAssertion if name is None |

### fetch_task()

```python
def fetch_task(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteTask
```
Fetch a task entity from flyte admin.



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | fetch entity from this project. If None, uses the default_project attribute. |
| `domain` | `str` | fetch entity from this domain. If None, uses the default_domain attribute. |
| `name` | `str` | fetch entity with matching name. |
| `version` | `str` | fetch entity with matching version. If None, gets the latest version of the entity. :returns: :class:`~flytekit.remote.tasks.task.FlyteTask`  :raises: FlyteAssertion if name is None |

### fetch_task_lazy()

```python
def fetch_task_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity
```
Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |
| `version` | `str` | |

### fetch_workflow()

```python
def fetch_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteWorkflow
```
Fetch a workflow entity from flyte admin.


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | fetch entity from this project. If None, uses the default_project attribute. |
| `domain` | `str` | fetch entity from this domain. If None, uses the default_domain attribute. |
| `name` | `str` | fetch entity with matching name. |
| `version` | `str` | fetch entity with matching version. If None, gets the latest version of the entity. :raises: FlyteAssertion if name is None |

### fetch_workflow_lazy()

```python
def fetch_workflow_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity[FlyteWorkflow]
```
Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |
| `version` | `str` | |

### find_launch_plan()

```python
def find_launch_plan(
    lp_ref: id_models,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type | Description |
|-|-|-|
| `lp_ref` | `id_models` | |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` | |

### find_launch_plan_for_node()

```python
def find_launch_plan_for_node(
    node: Node,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type | Description |
|-|-|-|
| `node` | `Node` | |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` | |

### for_endpoint()

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
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `insecure` | `bool` | |
| `data_config` | `typing.Optional[DataConfig]` | |
| `config_file` | `typing.Union[str, ConfigFile]` | |
| `default_project` | `typing.Optional[str]` | |
| `default_domain` | `typing.Optional[str]` | |
| `data_upload_location` | `str` | |
| `interactive_mode_enabled` | `bool` | |
| `kwargs` | `**kwargs` | |

### for_sandbox()

```python
def for_sandbox(
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type | Description |
|-|-|-|
| `default_project` | `typing.Optional[str]` | |
| `default_domain` | `typing.Optional[str]` | |
| `data_upload_location` | `str` | |
| `interactive_mode_enabled` | `bool` | |
| `kwargs` | `**kwargs` | |

### from_api_key()

```python
def from_api_key(
    api_key: str,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    kwargs,
) -> 'UnionRemote'
```
Call this if you want to directly instantiate a UnionRemote from an API key


| Parameter | Type | Description |
|-|-|-|
| `api_key` | `str` | |
| `default_project` | `typing.Optional[str]` | |
| `default_domain` | `typing.Optional[str]` | |
| `data_upload_location` | `str` | |
| `kwargs` | `**kwargs` | |

### generate_console_http_domain()

```python
def generate_console_http_domain()
```
This should generate the domain where console is hosted.

:return:


### generate_console_url()

```python
def generate_console_url(
    entity: typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, FlyteLaunchPlan, Artifact],
)
```
Generate a UnionAI console URL for the given Flyte remote endpoint.
It will also handle Union AI specific entities like Artifacts.

This will automatically determine if this is an execution or an entity
and change the type automatically.


| Parameter | Type | Description |
|-|-|-|
| `entity` | `typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, FlyteLaunchPlan, Artifact]` | |

### get()

```python
def get(
    uri: typing.Optional[str],
) -> typing.Optional[typing.Union[LiteralsResolver, Literal, bytes]]
```
General function that works with flyte tiny urls. This can return outputs (in the form of LiteralsResolver, or
individual Literals for singular requests), or HTML if passed a deck link, or bytes containing HTML,
if ipython is not available locally.


| Parameter | Type | Description |
|-|-|-|
| `uri` | `typing.Optional[str]` | |

### get_artifact()

```python
def get_artifact(
    uri: typing.Optional[str],
    artifact_key: typing.Optional[art_id.ArtifactKey],
    artifact_id: typing.Optional[art_id.ArtifactID],
    query: typing.Optional[typing.Union[art_id.ArtifactQuery, ArtifactQuery]],
    get_details: bool,
) -> typing.Optional[Artifact]
```
Get the specified artifact.



| Parameter | Type | Description |
|-|-|-|
| `uri` | `typing.Optional[str]` | An artifact URI. |
| `artifact_key` | `typing.Optional[art_id.ArtifactKey]` | An artifact key. |
| `artifact_id` | `typing.Optional[art_id.ArtifactID]` | The artifact ID. |
| `query` | `typing.Optional[typing.Union[art_id.ArtifactQuery, ArtifactQuery]]` | An artifact query. |
| `get_details` | `bool` | A bool to indicate whether or not to return artifact details. :return: The artifact as persisted in the service. |

### get_domains()

```python
def get_domains()
```
Lists registered domains from flyte admin.

:returns: typing.List[flytekit.models.domain.Domain]


### get_execution_metrics()

```python
def get_execution_metrics(
    id: WorkflowExecutionIdentifier,
    depth: int,
) -> FlyteExecutionSpan
```
Get the metrics for a given execution.


| Parameter | Type | Description |
|-|-|-|
| `id` | `WorkflowExecutionIdentifier` | |
| `depth` | `int` | |

### get_extra_headers_for_protocol()

```python
def get_extra_headers_for_protocol(
    native_url,
)
```
| Parameter | Type | Description |
|-|-|-|
| `native_url` |  | |

### launch_backfill()

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



| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | str project name |
| `domain` | `str` | str domain name |
| `from_date` | `datetime` | datetime generate a backfill starting at this datetime (exclusive) |
| `to_date` | `datetime` | datetime generate a backfill ending at this datetime (inclusive) |
| `launchplan` | `str` | str launchplan name in the flyte backend |
| `launchplan_version` | `str` | str (optional) version for the launchplan. If not specified the most recent will be retrieved |
| `execution_name` | `str` | str (optional) the generated execution will be named so. this can help in ensuring idempotency |
| `version` | `str` | str (optional) version to be used for the newly created workflow. |
| `dry_run` | `bool` | bool do not register or execute the workflow |
| `execute` | `bool` | bool Register and execute the wwkflow. |
| `parallel` | `bool` | if the backfill should be run in parallel. False (default) will run each bacfill sequentially. |
| `failure_policy` | `typing.Optional[WorkflowFailurePolicy]` | WorkflowFailurePolicy (optional) to be used for the newly created workflow. This can control failure behavior - whether to continue on failure or stop immediately on failure |
| `overwrite_cache` | `typing.Optional[bool]` | if True, will overwrite the cache. :return: In case of dry-run, return WorkflowBase, else if no_execute return FlyteWorkflow else in the default case return a FlyteWorkflowExecution |

### list_projects()

```python
def list_projects(
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
    sort_by: typing.Optional[admin_common_models.Sort],
) -> typing.List[Project]
```
Lists registered projects from flyte admin.



| Parameter | Type | Description |
|-|-|-|
| `limit` | `typing.Optional[int]` | [Optional[int]] The maximum number of entries to return. |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` | |
| `sort_by` | `typing.Optional[admin_common_models.Sort]` | |

### list_signals()

```python
def list_signals(
    execution_name: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: int,
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[Signal]
```
| Parameter | Type | Description |
|-|-|-|
| `execution_name` | `str` | The name of the execution. This is the tailend of the URL when looking at the workflow execution. |
| `project` | `typing.Optional[str]` | The execution project, will default to the Remote's default project. |
| `domain` | `typing.Optional[str]` | The execution domain, will default to the Remote's default domain. |
| `limit` | `int` | The number of signals to fetch |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` | Optional list of filters |

### list_tasks_by_version()

```python
def list_tasks_by_version(
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
) -> typing.List[FlyteTask]
```
| Parameter | Type | Description |
|-|-|-|
| `version` | `str` | |
| `project` | `typing.Optional[str]` | |
| `domain` | `typing.Optional[str]` | |
| `limit` | `typing.Optional[int]` | |

### raw_register()

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



| Parameter | Type | Description |
|-|-|-|
| `cp_entity` | `FlyteControlPlaneEntity` | The controlplane "serializable" version of a flyte entity. This is in the form that FlyteAdmin understands. |
| `settings` | `SerializationSettings` | SerializationSettings to be used for registration - especially to identify the id |
| `version` | `str` | Version to be registered |
| `create_default_launchplan` | `bool` | boolean that indicates if a default launch plan should be created |
| `options` | `Options` | Options to be used if registering a default launch plan |
| `og_entity` | `FlyteLocalEntity` | Pass in the original workflow (flytekit type) if create_default_launchplan is true :return: Identifier of the created entity |

### recent_executions()

```python
def recent_executions(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[FlyteWorkflowExecution]
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `typing.Optional[str]` | |
| `domain` | `typing.Optional[str]` | |
| `limit` | `typing.Optional[int]` | |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` | |

### register_launch_plan()

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



| Parameter | Type | Description |
|-|-|-|
| `entity` | `LaunchPlan` | Launchplan to be registered |
| `version` | `typing.Optional[str]` | Version to be registered for the launch plan, and used to check (and register) underlying wf |
| `project` | `typing.Optional[str]` | Optionally provide a project, if not already provided in flyteremote constructor or a separate one |
| `domain` | `typing.Optional[str]` | Optionally provide a domain, if not already provided in FlyteRemote constructor or a separate one |
| `options` | `typing.Optional[Options]` | |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | Optionally provide serialization settings, if not provided, will use the default |

### register_script()

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
    default_resources: typing.Optional[ResourceSpec],
    fast_package_options: typing.Optional[FastPackageOptions],
) -> typing.Union[FlyteWorkflow, FlyteTask, FlyteLaunchPlan, ReferenceEntity]
```
Use this method to register a workflow via script mode.


| Parameter | Type | Description |
|-|-|-|
| `entity` | `typing.Union[WorkflowBase, PythonTask, LaunchPlan]` | The workflow to be registered or the task to be registered |
| `image_config` | `typing.Optional[ImageConfig]` | The image config to use for the workflow. |
| `version` | `typing.Optional[str]` | version for the entity to be registered as |
| `project` | `typing.Optional[str]` | The project to register the workflow in. |
| `domain` | `typing.Optional[str]` | The domain to register the workflow in. |
| `destination_dir` | `str` | The destination directory where the workflow will be copied to. |
| `copy_all` | `bool` | [deprecated] Please use the copy_style field in fast_package_options instead. |
| `default_launch_plan` | `bool` | This should be true if a default launch plan should be created for the workflow |
| `options` | `typing.Optional[Options]` | Additional execution options that can be configured for the default launchplan |
| `source_path` | `typing.Optional[str]` | The root of the project path |
| `module_name` | `typing.Optional[str]` | the name of the module |
| `envs` | `typing.Optional[typing.Dict[str, str]]` | Environment variables to be passed to the serialization |
| `default_resources` | `typing.Optional[ResourceSpec]` | Default resources to be passed to the serialization. These override the resource spec for any tasks that have no statically defined resource requests and limits. |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` | Options to customize copy_all behavior, ignored when copy_all is False. :return: |

### register_task()

```python
def register_task(
    entity: PythonTask,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
) -> FlyteTask
```
Register a qualified task (PythonTask) with Remote
For any conflicting parameters method arguments are regarded as overrides



| Parameter | Type | Description |
|-|-|-|
| `entity` | `PythonTask` | PythonTask can be either @task or a instance of a Task class |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | Settings that will be used to override various serialization parameters. |
| `version` | `typing.Optional[str]` | version that will be used to register. If not specified will default to using the serialization settings default :return: |

### register_workflow()

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


| Parameter | Type | Description |
|-|-|-|
| `entity` | `WorkflowBase` | The workflow to be registered |
| `serialization_settings` | `typing.Optional[SerializationSettings]` | The serialization settings to be used |
| `version` | `typing.Optional[str]` | version for the entity to be registered as |
| `default_launch_plan` | `typing.Optional[bool]` | This should be true if a default launch plan should be created for the workflow |
| `options` | `typing.Optional[Options]` | Additional execution options that can be configured for the default launchplan :return: |

### reject()

```python
def reject(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The name of the signal, this is the key used in the approve() or wait_for_input() call. |
| `execution_name` | `str` | The name of the execution. This is the tail-end of the URL when looking at the workflow execution. |
| `project` | `str` | The execution project, will default to the Remote's default project. |
| `domain` | `str` | The execution domain, will default to the Remote's default domain. |

### remote_context()

```python
def remote_context()
```
Context manager with remote-specific configuration.


### search_artifacts()

```python
def search_artifacts(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    name: typing.Optional[str],
    artifact_key: typing.Optional[art_id.ArtifactKey],
    query: typing.Optional[ArtifactQuery],
    partitions: typing.Optional[Union[Partitions, typing.Dict[str, str]]],
    time_partition: typing.Optional[Union[datetime.datetime, TimePartition]],
    group_by_key: bool,
    limit: int,
) -> typing.List[Artifact]
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `typing.Optional[str]` | |
| `domain` | `typing.Optional[str]` | |
| `name` | `typing.Optional[str]` | |
| `artifact_key` | `typing.Optional[art_id.ArtifactKey]` | |
| `query` | `typing.Optional[ArtifactQuery]` | |
| `partitions` | `typing.Optional[Union[Partitions, typing.Dict[str, str]]]` | |
| `time_partition` | `typing.Optional[Union[datetime.datetime, TimePartition]]` | |
| `group_by_key` | `bool` | |
| `limit` | `int` | |

### set_input()

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
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The name of the signal, this is the key used in the approve() or wait_for_input() call. |
| `execution_name` | `str` | The name of the execution. This is the tail-end of the URL when looking at the workflow execution. |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` | This is either a Literal or a Python value which FlyteRemote will invoke the TypeEngine to convert into a Literal. This argument is only value for wait_for_input type signals. |
| `project` |  | The execution project, will default to the Remote's default project. |
| `domain` |  | The execution domain, will default to the Remote's default domain. |
| `python_type` |  | Provide a python type to help with conversion if the value you provided is not a Literal. |
| `literal_type` |  | Provide a Flyte literal type to help with conversion if the value you provided is not a Literal |

### set_signal()

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
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | The name of the signal, this is the key used in the approve() or wait_for_input() call. |
| `execution_name` | `str` | The name of the execution. This is the tail-end of the URL when looking at the workflow execution. |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` | This is either a Literal or a Python value which FlyteRemote will invoke the TypeEngine to convert into a Literal. This argument is only value for wait_for_input type signals. |
| `project` | `typing.Optional[str]` | The execution project, will default to the Remote's default project. |
| `domain` | `typing.Optional[str]` | The execution domain, will default to the Remote's default domain. |
| `python_type` | `typing.Optional[typing.Type]` | Provide a python type to help with conversion if the value you provided is not a Literal. |
| `literal_type` | `typing.Optional[type_models.LiteralType]` | Provide a Flyte literal type to help with conversion if the value you provided is not a Literal |

### stop_app()

```python
def stop_app(
    name: str,
    project: Optional[str],
    domain: Optional[str],
)
```
Stop an application.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of application to stop. |
| `project` | `Optional[str]` | Domain name. If None, uses default_domain. :return: The App IDL for the stopped application. |
| `domain` | `Optional[str]` | |

### stream_execution_events()

```python
def stream_execution_events(
    event_count: Optional[int],
    include_workflow_executions: bool,
    include_task_executions: bool,
    include_node_executions: bool,
) -> AsyncGenerator[Union[CloudEventWorkflowExecution, CloudEventNodeExecution, CloudEventTaskExecution], None]
```
Stream execution events from the given tenant. This is a generator that yields events as they are received.

Events are guaranteed to be delivered at least once, and clients must implement handling for potentially
out-of-order event processing. Events will be retransmitted until acknowledged, with acknowledgment occurring
automatically upon normal return from the caller.
Note: if an exception is raised during event processing, the acknowledgment will not occur, and the event
will be redelivered in a subsequent transmission.



| Parameter | Type | Description |
|-|-|-|
| `event_count` | `Optional[int]` | Number of events to receive before closing the stream. If None, receive unlimited events. |
| `include_workflow_executions` | `bool` | Whether to include workflow execution events |
| `include_task_executions` | `bool` | Whether to include task execution events |
| `include_node_executions` | `bool` | Whether to include node execution events |

### sync()

```python
def sync(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
This function was previously a singledispatchmethod. We've removed that but this function remains
so that we don't break people.



| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteWorkflowExecution` | |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` | |
| `sync_nodes` | `bool` | By default sync will fetch data on all underlying node executions (recursively, so subworkflows and launch plans will also get picked up). Set this to False in order to prevent that (which will make this call faster). :return: Returns the same execution object, but with additional information pulled in. |

### sync_execution()

```python
def sync_execution(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Sync a FlyteWorkflowExecution object with its corresponding remote state.


| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteWorkflowExecution` | |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` | |
| `sync_nodes` | `bool` | |

### sync_node_execution()

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


| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteNodeExecution` | |
| `node_mapping` | `typing.Dict[str, FlyteNode]` | |

### sync_task_execution()

```python
def sync_task_execution(
    execution: FlyteTaskExecution,
    entity_interface: typing.Optional[TypedInterface],
    get_task_exec_data: bool,
) -> FlyteTaskExecution
```
Sync a FlyteTaskExecution object with its corresponding remote state.


| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteTaskExecution` | |
| `entity_interface` | `typing.Optional[TypedInterface]` | |
| `get_task_exec_data` | `bool` | |

### terminate()

```python
def terminate(
    execution: FlyteWorkflowExecution,
    cause: str,
)
```
Terminate a workflow execution.



| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteWorkflowExecution` | workflow execution to terminate |
| `cause` | `str` | reason for termination |

### upload_file()

```python
def upload_file(
    to_upload: pathlib.Path,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    filename_root: typing.Optional[str],
) -> typing.Tuple[bytes, str]
```
Function will use remote's client to hash and then upload the file using Admin's data proxy service.



| Parameter | Type | Description |
|-|-|-|
| `to_upload` | `pathlib.Path` | Must be a single file |
| `project` | `typing.Optional[str]` | Project to upload under, if not supplied will use the remote's default |
| `domain` | `typing.Optional[str]` | Domain to upload under, if not specified will use the remote's default |
| `filename_root` | `typing.Optional[str]` | If provided will be used as the root of the filename. If not, Admin will use a hash :return: The uploaded location. |

### wait()

```python
def wait(
    execution: FlyteWorkflowExecution,
    timeout: typing.Optional[typing.Union[timedelta, int]],
    poll_interval: typing.Optional[typing.Union[timedelta, int]],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Wait for an execution to finish.



| Parameter | Type | Description |
|-|-|-|
| `execution` | `FlyteWorkflowExecution` | execution object to wait on |
| `timeout` | `typing.Optional[typing.Union[timedelta, int]]` | maximum amount of time to wait. It can be a timedelta or a duration in seconds as int. |
| `poll_interval` | `typing.Optional[typing.Union[timedelta, int]]` | sync workflow execution at this interval. It can be a timedelta or a duration in seconds as int. |
| `sync_nodes` | `bool` | passed along to the sync call for the workflow execution |

## Properties

| Property | Type | Description |
|-|-|-|
| `apps_service_client` |  |  |
| `artifacts_client` |  |  |
| `authorizer_service_client` |  |  |
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
| `hooks_async_client` |  |  |
| `hooks_sync_client` |  |  |
| `images_client` |  |  |
| `interactive_mode_enabled` |  | {{< multiline >}}If set to True, the FlyteRemote will pickle the task/workflow.
{{< /multiline >}} |
| `secret_client` |  |  |
| `sync_channel` |  | {{< multiline >}}Return channel from client. This channel already has the org passed in dynamically by the interceptor.
{{< /multiline >}} |
| `user_service_client` |  |  |
| `users_client` |  |  |

