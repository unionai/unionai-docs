---
title: flytekit.models.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`CompiledTask`](.././flytekit.models.task#flytekitmodelstaskcompiledtask) |  |
| [`Container`](.././flytekit.models.task#flytekitmodelstaskcontainer) |  |
| [`DataLoadingConfig`](.././flytekit.models.task#flytekitmodelstaskdataloadingconfig) |  |
| [`IOStrategy`](.././flytekit.models.task#flytekitmodelstaskiostrategy) | Provides methods to manage data in and out of the Raw container using Download Modes. |
| [`K8sObjectMetadata`](.././flytekit.models.task#flytekitmodelstaskk8sobjectmetadata) |  |
| [`K8sPod`](.././flytekit.models.task#flytekitmodelstaskk8spod) |  |
| [`Resources`](.././flytekit.models.task#flytekitmodelstaskresources) |  |
| [`RuntimeMetadata`](.././flytekit.models.task#flytekitmodelstaskruntimemetadata) |  |
| [`Sql`](.././flytekit.models.task#flytekitmodelstasksql) |  |
| [`Task`](.././flytekit.models.task#flytekitmodelstasktask) |  |
| [`TaskClosure`](.././flytekit.models.task#flytekitmodelstasktaskclosure) |  |
| [`TaskExecutionMetadata`](.././flytekit.models.task#flytekitmodelstasktaskexecutionmetadata) |  |
| [`TaskMetadata`](.././flytekit.models.task#flytekitmodelstasktaskmetadata) |  |
| [`TaskSpec`](.././flytekit.models.task#flytekitmodelstasktaskspec) |  |
| [`TaskTemplate`](.././flytekit.models.task#flytekitmodelstasktasktemplate) |  |

## flytekit.models.task.CompiledTask

```python
class CompiledTask(
    template,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `template` | `None` | :rtype: TaskTemplate |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.compiler_pb2.CompiledTask


## flytekit.models.task.Container

```python
class Container(
    image,
    command,
    args,
    resources,
    env,
    config,
    data_loading_config,
)
```
This defines a container target.  It will execute the appropriate command line on the appropriate image with
the given configurations.



| Parameter | Type | Description |
|-|-|-|
| `image` |  | |
| `command` |  | |
| `args` | `*args` | |
| `resources` |  | |
| `env` |  | |
| `config` |  | |
| `data_loading_config` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `args` | `None` | A list of arguments for the command.  i.e. ['s3://some/path', '/tmp/local/path'] rtype: list[Text] |
| `command` | `None` | A list of 'words' for the command.  i.e. ['aws', 's3', 'ls'] :rtype: list[Text] |
| `config` | `None` | A definition of key-value pairs for configuration.  Currently, only str-&gt;str is     supported. :rtype: dict[Text, Text] |
| `data_loading_config` | `None` | :rtype: DataLoadingConfig |
| `env` | `None` | A definition of key-value pairs for environment variables.  Currently, only str-&gt;str is     supported. :rtype: dict[Text, Text] |
| `image` | `None` | The fully-qualified identifier for the image. :rtype: Text |
| `is_empty` | `None` |  |
| `resources` | `None` | A definition of requisite compute resources. :rtype: Resources |

### Methods

| Method | Description |
|-|-|
| [`add_env()`](#add_env) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### add_env()

```python
def add_env(
    key: str,
    val: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |
| `val` | `str` | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.Container


## flytekit.models.task.DataLoadingConfig

```python
class DataLoadingConfig(
    input_path: str,
    output_path: str,
    enabled: bool,
    format: google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper,
    io_strategy: flytekit.models.task.IOStrategy,
)
```
| Parameter | Type | Description |
|-|-|-|
| `input_path` | `str` | |
| `output_path` | `str` | |
| `enabled` | `bool` | |
| `format` | `google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper` | |
| `io_strategy` | `flytekit.models.task.IOStrategy` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.core.tasks_pb2.DataLoadingConfig,
) -> DataLoadingConfig
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `flyteidl.core.tasks_pb2.DataLoadingConfig` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.IOStrategy

Provides methods to manage data in and out of the Raw container using Download Modes. This can only be used if DataLoadingConfig is enabled.



```python
class IOStrategy(
    download_mode: google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper,
    upload_mode: google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper,
)
```
| Parameter | Type | Description |
|-|-|-|
| `download_mode` | `google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper` | |
| `upload_mode` | `google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.IOStrategy,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.IOStrategy` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.K8sObjectMetadata

```python
class K8sObjectMetadata(
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
)
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type | Description |
|-|-|-|
| `labels` | `typing.Optional[typing.Dict[str, str]]` | |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` |  |
| `is_empty` | `None` |  |
| `labels` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sObjectMetadata` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.K8sPod

```python
class K8sPod(
    metadata: flytekit.models.task.K8sObjectMetadata,
    pod_spec: typing.Dict[str, typing.Any],
    data_config: typing.Optional[flytekit.models.task.DataLoadingConfig],
    primary_container_name: typing.Optional[str],
)
```
This defines a kubernetes pod target.  It will build the pod target during task execution


| Parameter | Type | Description |
|-|-|-|
| `metadata` | `flytekit.models.task.K8sObjectMetadata` | |
| `pod_spec` | `typing.Dict[str, typing.Any]` | |
| `data_config` | `typing.Optional[flytekit.models.task.DataLoadingConfig]` | |
| `primary_container_name` | `typing.Optional[str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `data_config` | `None` |  |
| `is_empty` | `None` |  |
| `metadata` | `None` |  |
| `pod_spec` | `None` |  |
| `primary_container_name` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_pod_template()`](#from_pod_template) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_pod_template()`](#to_pod_template) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sPod,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sPod` | |

#### from_pod_template()

```python
def from_pod_template(
    pod_template: PodTemplate,
) -> K8sPod
```
| Parameter | Type | Description |
|-|-|-|
| `pod_template` | `PodTemplate` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### to_pod_template()

```python
def to_pod_template()
```
## flytekit.models.task.Resources

```python
class Resources(
    requests,
    limits,
)
```
| Parameter | Type | Description |
|-|-|-|
| `requests` |  | |
| `limits` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `limits` | `None` | These are the limits required.  These are guaranteed to be satisfied. :rtype: list[Resources.ResourceEntry] |
| `requests` | `None` | The desired resources for execution.  This is given on a best effort basis. :rtype: list[Resources.ResourceEntry] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.Resources


## flytekit.models.task.RuntimeMetadata

```python
class RuntimeMetadata(
    type,
    version,
    flavor,
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |
| `version` |  | |
| `flavor` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `flavor` | `None` | Optional extra information about runtime environment (e.g. Python, GoLang, etc.) :rtype: Text |
| `is_empty` | `None` |  |
| `type` | `None` | Enum type from RuntimeMetadata.RuntimeType :rtype: int |
| `version` | `None` | Version string for SDK version.  Can be used for metrics or managing breaking changes in Admin or Propeller :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.RuntimeMetadata


## flytekit.models.task.Sql

```python
class Sql(
    statement: str,
    dialect: int,
)
```
This defines a kubernetes pod target. It will build the pod target during task execution


| Parameter | Type | Description |
|-|-|-|
| `statement` | `str` | |
| `dialect` | `int` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `dialect` | `None` |  |
| `is_empty` | `None` |  |
| `statement` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.Sql,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.Sql` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.Task

```python
class Task(
    id,
    closure,
    short_description,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `closure` |  | |
| `short_description` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | The closure for the underlying workload. :rtype: TaskClosure |
| `id` | `None` | The (project, domain, name, version) identifier for this task. :rtype: flytekit.models.core.identifier.Identifier |
| `is_empty` | `None` |  |
| `short_description` | `None` | The short description of the task. :rtype: str |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.Task


## flytekit.models.task.TaskClosure

```python
class TaskClosure(
    compiled_task,
)
```
| Parameter | Type | Description |
|-|-|-|
| `compiled_task` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `compiled_task` | `None` | :rtype: CompiledTask |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.TaskClosure


## flytekit.models.task.TaskExecutionMetadata

```python
class TaskExecutionMetadata(
    task_execution_id,
    namespace,
    labels,
    annotations,
    k8s_service_account,
    environment_variables,
    identity,
)
```
Runtime task execution metadata.



| Parameter | Type | Description |
|-|-|-|
| `task_execution_id` |  | |
| `namespace` |  | |
| `labels` |  | |
| `annotations` |  | |
| `k8s_service_account` |  | |
| `environment_variables` |  | |
| `identity` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` |  |
| `environment_variables` | `None` |  |
| `identity` | `None` |  |
| `is_empty` | `None` |  |
| `k8s_service_account` | `None` |  |
| `labels` | `None` |  |
| `namespace` | `None` |  |
| `task_execution_id` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.agent_pb2.TaskExecutionMetadata


## flytekit.models.task.TaskMetadata

```python
class TaskMetadata(
    discoverable,
    runtime,
    timeout,
    retries,
    interruptible,
    discovery_version,
    deprecated_error_message,
    cache_serializable,
    pod_template_name,
    cache_ignore_input_vars,
    is_eager: bool,
    generates_deck: bool,
    k8s_object_metadata: typing.Optional[ForwardRef('K8sObjectMetadata')],
)
```
Information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts,
and retries.



| Parameter | Type | Description |
|-|-|-|
| `discoverable` |  | |
| `runtime` |  | |
| `timeout` |  | |
| `retries` |  | |
| `interruptible` |  | |
| `discovery_version` |  | |
| `deprecated_error_message` |  | |
| `cache_serializable` |  | |
| `pod_template_name` |  | The name of the existing PodTemplate resource which will be used in this task. |
| `cache_ignore_input_vars` |  | Input variables that should not be included when calculating hash for cache. |
| `is_eager` | `bool` | |
| `generates_deck` | `bool` | |
| `k8s_object_metadata` | `typing.Optional[ForwardRef('K8sObjectMetadata')]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cache_ignore_input_vars` | `None` | Input variables that should not be included when calculating hash for cache. :rtype: tuple[Text] |
| `cache_serializable` | `None` | Whether or not caching operations are executed in serial. This means only a single instance over identical inputs is executed, other concurrent executions wait for the cached results. :rtype: bool |
| `deprecated_error_message` | `None` | This string can be used to mark the task as deprecated.  Consumers of the task will receive deprecation warnings. :rtype: Text |
| `discoverable` | `None` | Whether or not the outputs of this task should be cached for discovery. :rtype: bool |
| `discovery_version` | `None` | This is the version used to create a logical version for data in the cache. This is only used when `discoverable` is true.  Data is considered discoverable if: the inputs to a given task are the same and the discovery_version is also the same. :rtype: Text |
| `generates_deck` | `None` | Whether the task will generate a Deck. :rtype: bool |
| `interruptible` | `None` | Whether or not the task is interruptible. :rtype: bool |
| `is_eager` | `None` |  |
| `is_empty` | `None` |  |
| `k8s_object_metadata` | `None` | Kubernetes metadata for the task. :rtype: K8sObjectMetadata |
| `pod_template_name` | `None` | The name of the existing PodTemplate resource which will be used in this task. :rtype: Text |
| `retries` | `None` | Retry strategy for this task.  0 retries means only try once. :rtype: flytekit.models.literals.RetryStrategy |
| `runtime` | `None` | Metadata describing the runtime environment for this task. :rtype: RuntimeMetadata |
| `timeout` | `None` | The amount of time to wait before timing out.  This includes queuing and scheduler latency. :rtype: datetime.timedelta |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.TaskMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.TaskMetadata` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.TaskMetadata


## flytekit.models.task.TaskSpec

```python
class TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` | `flytekit.models.task.TaskTemplate` | |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `docs` | `None` | :rtype: Description entity for the task |
| `is_empty` | `None` |  |
| `template` | `None` | :rtype: TaskTemplate |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.tasks_pb2.TaskSpec


## flytekit.models.task.TaskTemplate

```python
class TaskTemplate(
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
)
```
A task template represents the full set of information necessary to perform a unit of work in the Flyte system.
It contains the metadata about what inputs and outputs are consumed or produced.  It also contains the metadata
necessary for Flyte Propeller to do the appropriate work.



| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `type` |  | |
| `metadata` |  | |
| `interface` |  | |
| `custom` |  | |
| `container` |  | |
| `task_type_version` |  | |
| `security_context` |  | |
| `config` |  | |
| `k8s_pod` |  | |
| `sql` |  | |
| `extended_resources` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `config` | `None` | Arbitrary dictionary containing metadata for parsing and handling custom plugins. :rtype: dict[Text, T] |
| `container` | `None` | If not None, the target of execution should be a container. :rtype: Container |
| `custom` | `None` | Arbitrary dictionary containing metadata for custom plugins. :rtype: dict[Text, T] |
| `extended_resources` | `None` | If not None, the extended resources to allocate to the task. :rtype: flyteidl.core.tasks_pb2.ExtendedResources |
| `id` | `None` | This is generated by the system and uniquely identifies the task. :rtype: flytekit.models.core.identifier.Identifier |
| `interface` | `None` | The interface definition for this task. :rtype: flytekit.models.interface.TypedInterface |
| `is_empty` | `None` |  |
| `k8s_pod` | `None` |  |
| `metadata` | `None` | This contains information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts, and retries. :rtype: TaskMetadata |
| `security_context` | `None` |  |
| `sql` | `None` |  |
| `task_type_version` | `None` |  |
| `type` | `None` | This is used to identify additional extensions for use by Propeller or SDK. :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.TaskTemplate


