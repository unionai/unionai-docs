---
title: flytekit.models.task
version: 1.16.16
variants: +flyte +union
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

### Parameters

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
| `template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** CompiledTask

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.compiler_pb2.CompiledTask

## flytekit.models.task.Container

### Parameters

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

:type DataLoadingConfig data_loading_config: object


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
| `args` | `None` | A list of arguments for the command.  i.e. ['s3://some/path', '/tmp/local/path'] |
| `command` | `None` | A list of 'words' for the command.  i.e. ['aws', 's3', 'ls'] |
| `config` | `None` | A definition of key-value pairs for configuration.  Currently, only str-&gt;str is     supported. |
| `data_loading_config` | `None` |  |
| `env` | `None` | A definition of key-value pairs for environment variables.  Currently, only str-&gt;str is     supported. |
| `image` | `None` | The fully-qualified identifier for the image. |
| `is_empty` | `None` |  |
| `resources` | `None` | A definition of requisite compute resources. |

### Methods

| Method | Description |
|-|-|
| [`add_env()`](#add_env) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


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

**Returns:** Container

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.tasks_pb2.Container

## flytekit.models.task.DataLoadingConfig

### Parameters

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
| [`short_string()`](#short_string) |  |
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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.IOStrategy

Provides methods to manage data in and out of the Raw container using Download Modes. This can only be used if DataLoadingConfig is enabled.


### Parameters

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
| [`short_string()`](#short_string) |  |
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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.K8sObjectMetadata

### Parameters

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
| [`short_string()`](#short_string) |  |
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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.K8sPod

### Parameters

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
| [`short_string()`](#short_string) |  |
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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### to_pod_template()

```python
def to_pod_template()
```
## flytekit.models.task.Resources

### Parameters

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
| `limits` | `None` | These are the limits required.  These are guaranteed to be satisfied. |
| `requests` | `None` | The desired resources for execution.  This is given on a best effort basis. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Resources

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.tasks_pb2.Resources

## flytekit.models.task.RuntimeMetadata

### Parameters

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
| `flavor` | `None` | Optional extra information about runtime environment (e.g. Python, GoLang, etc.) |
| `is_empty` | `None` |  |
| `type` | `None` | Enum type from RuntimeMetadata.RuntimeType |
| `version` | `None` | Version string for SDK version.  Can be used for metrics or managing breaking changes in Admin or Propeller |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** RuntimeMetadata

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.tasks_pb2.RuntimeMetadata

## flytekit.models.task.Sql

### Parameters

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
| [`short_string()`](#short_string) |  |
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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.task.Task

### Parameters

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
| `closure` | `None` | The closure for the underlying workload. |
| `id` | `None` | The (project, domain, name, version) identifier for this task. |
| `is_empty` | `None` |  |
| `short_description` | `None` | The short description of the task. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskDefinition

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.task_pb2.Task

## flytekit.models.task.TaskClosure

### Parameters

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
| `compiled_task` | `None` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskClosure

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.task_pb2.TaskClosure

## flytekit.models.task.TaskExecutionMetadata

### Parameters

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
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskExecutionMetadata

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.agent_pb2.TaskExecutionMetadata

## flytekit.models.task.TaskMetadata

### Parameters

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
| `cache_ignore_input_vars` | `None` | Input variables that should not be included when calculating hash for cache. |
| `cache_serializable` | `None` | Whether or not caching operations are executed in serial. This means only a single instance over identical inputs is executed, other concurrent executions wait for the cached results. |
| `deprecated_error_message` | `None` | This string can be used to mark the task as deprecated.  Consumers of the task will receive deprecation warnings. |
| `discoverable` | `None` | Whether or not the outputs of this task should be cached for discovery. |
| `discovery_version` | `None` | This is the version used to create a logical version for data in the cache. This is only used when `discoverable` is true.  Data is considered discoverable if: the inputs to a given task are the same and the discovery_version is also the same. |
| `generates_deck` | `None` | Whether the task will generate a Deck. |
| `interruptible` | `None` | Whether or not the task is interruptible. |
| `is_eager` | `None` |  |
| `is_empty` | `None` |  |
| `k8s_object_metadata` | `None` | Kubernetes metadata for the task. |
| `pod_template_name` | `None` | The name of the existing PodTemplate resource which will be used in this task. |
| `retries` | `None` | Retry strategy for this task.  0 retries means only try once. |
| `runtime` | `None` | Metadata describing the runtime environment for this task. |
| `timeout` | `None` | The amount of time to wait before timing out.  This includes queuing and scheduler latency. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.TaskMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.TaskMetadata` | |

**Returns:** TaskMetadata

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.task_pb2.TaskMetadata

## flytekit.models.task.TaskSpec

### Parameters

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
| `docs` | `None` |  |
| `is_empty` | `None` |  |
| `template` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskSpec

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.tasks_pb2.TaskSpec

## flytekit.models.task.TaskTemplate

### Parameters

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
| `config` | `None` | Arbitrary dictionary containing metadata for parsing and handling custom plugins. |
| `container` | `None` | If not None, the target of execution should be a container. |
| `custom` | `None` | Arbitrary dictionary containing metadata for custom plugins. |
| `extended_resources` | `None` | If not None, the extended resources to allocate to the task. |
| `id` | `None` | This is generated by the system and uniquely identifies the task. |
| `interface` | `None` | The interface definition for this task. |
| `is_empty` | `None` |  |
| `k8s_pod` | `None` |  |
| `metadata` | `None` | This contains information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts, and retries. |
| `security_context` | `None` |  |
| `sql` | `None` |  |
| `task_type_version` | `None` |  |
| `type` | `None` | This is used to identify additional extensions for use by Propeller or SDK. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** TaskTemplate

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.tasks_pb2.TaskTemplate

