---
title: flytekit.models.task
version: 0.1.dev2192+g7c539c3.d20250403
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
| Parameter | Type |
|-|-|
| `template` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: CompiledTask
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.compiler_pb2.CompiledTask


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `template` |  | {{< multiline >}}:rtype: TaskTemplate
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `image` |  |
| `command` |  |
| `args` | ``*args`` |
| `resources` |  |
| `env` |  |
| `config` |  |
| `data_loading_config` |  |

### Methods

| Method | Description |
|-|-|
| [`add_env()`](#add_env) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### add_env()

```python
def add_env(
    key: str,
    val: str,
)
```
| Parameter | Type |
|-|-|
| `key` | `str` |
| `val` | `str` |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Container
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.Container


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `args` |  | {{< multiline >}}A list of arguments for the command.  i.e. ['s3://some/path', '/tmp/local/path']
rtype: list[Text]
{{< /multiline >}} |
| `command` |  | {{< multiline >}}A list of 'words' for the command.  i.e. ['aws', 's3', 'ls']
:rtype: list[Text]
{{< /multiline >}} |
| `config` |  | {{< multiline >}}A definition of key-value pairs for configuration.  Currently, only str->str is
    supported.
:rtype: dict[Text, Text]
{{< /multiline >}} |
| `data_loading_config` |  | {{< multiline >}}:rtype: DataLoadingConfig
{{< /multiline >}} |
| `env` |  | {{< multiline >}}A definition of key-value pairs for environment variables.  Currently, only str->str is
    supported.
:rtype: dict[Text, Text]
{{< /multiline >}} |
| `image` |  | {{< multiline >}}The fully-qualified identifier for the image.
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `resources` |  | {{< multiline >}}A definition of requisite compute resources.
:rtype: Resources
{{< /multiline >}} |

## flytekit.models.task.DataLoadingConfig

```python
class DataLoadingConfig(
    input_path: str,
    output_path: str,
    enabled: bool,
    format: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a3930>,
    io_strategy: flytekit.models.task.IOStrategy,
)
```
| Parameter | Type |
|-|-|
| `input_path` | `str` |
| `output_path` | `str` |
| `enabled` | `bool` |
| `format` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a3930>` |
| `io_strategy` | `flytekit.models.task.IOStrategy` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.core.tasks_pb2.DataLoadingConfig,
) -> DataLoadingConfig
```
| Parameter | Type |
|-|-|
| `pb2` | `flyteidl.core.tasks_pb2.DataLoadingConfig` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.task.IOStrategy

Provides methods to manage data in and out of the Raw container using Download Modes. This can only be used if DataLoadingConfig is enabled.


```python
class IOStrategy(
    download_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a9310>,
    upload_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a9400>,
)
```
| Parameter | Type |
|-|-|
| `download_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a9310>` |
| `upload_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1069a9400>` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.IOStrategy,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.IOStrategy` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.task.K8sObjectMetadata

```python
class K8sObjectMetadata(
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
)
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type |
|-|-|
| `labels` | `typing.Dict[str, str]` |
| `annotations` | `typing.Dict[str, str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sObjectMetadata` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `is_empty` |  |  |
| `labels` |  |  |

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


| Parameter | Type |
|-|-|
| `metadata` | `flytekit.models.task.K8sObjectMetadata` |
| `pod_spec` | `typing.Dict[str, typing.Any]` |
| `data_config` | `typing.Optional[flytekit.models.task.DataLoadingConfig]` |
| `primary_container_name` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_pod_template()`](#from_pod_template) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_pod_template()`](#to_pod_template) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sPod,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sPod` |

#### from_pod_template()

```python
def from_pod_template(
    pod_template: PodTemplate,
) -> K8sPod
```
| Parameter | Type |
|-|-|
| `pod_template` | `PodTemplate` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `data_config` |  |  |
| `is_empty` |  |  |
| `metadata` |  |  |
| `pod_spec` |  |  |
| `primary_container_name` |  |  |

## flytekit.models.task.Resources

```python
class Resources(
    requests,
    limits,
)
```
| Parameter | Type |
|-|-|
| `requests` |  |
| `limits` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Resources
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.Resources


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `limits` |  | {{< multiline >}}These are the limits required.  These are guaranteed to be satisfied.
:rtype: list[Resources.ResourceEntry]
{{< /multiline >}} |
| `requests` |  | {{< multiline >}}The desired resources for execution.  This is given on a best effort basis.
:rtype: list[Resources.ResourceEntry]
{{< /multiline >}} |

## flytekit.models.task.RuntimeMetadata

```python
class RuntimeMetadata(
    type,
    version,
    flavor,
)
```
| Parameter | Type |
|-|-|
| `type` |  |
| `version` |  |
| `flavor` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: RuntimeMetadata
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.RuntimeMetadata


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `flavor` |  | {{< multiline >}}Optional extra information about runtime environment (e.g. Python, GoLang, etc.)
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `type` |  | {{< multiline >}}Enum type from RuntimeMetadata.RuntimeType
:rtype: int
{{< /multiline >}} |
| `version` |  | {{< multiline >}}Version string for SDK version.  Can be used for metrics or managing breaking changes in Admin or Propeller
:rtype: Text
{{< /multiline >}} |

## flytekit.models.task.Sql

```python
class Sql(
    statement: str,
    dialect: int,
)
```
This defines a kubernetes pod target. It will build the pod target during task execution


| Parameter | Type |
|-|-|
| `statement` | `str` |
| `dialect` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.Sql,
)
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.Sql` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `dialect` |  |  |
| `is_empty` |  |  |
| `statement` |  |  |

## flytekit.models.task.Task

```python
class Task(
    id,
    closure,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `closure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskDefinition
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.Task


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}The closure for the underlying workload.
:rtype: TaskClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}The (project, domain, name, version) identifier for this task.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.task.TaskClosure

```python
class TaskClosure(
    compiled_task,
)
```
| Parameter | Type |
|-|-|
| `compiled_task` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskClosure
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.task_pb2.TaskClosure


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `compiled_task` |  | {{< multiline >}}:rtype: CompiledTask
{{< /multiline >}} |
| `is_empty` |  |  |

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
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskExecutionMetadata
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.agent_pb2.TaskExecutionMetadata


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `environment_variables` |  |  |
| `identity` |  |  |
| `is_empty` |  |  |
| `k8s_service_account` |  |  |
| `labels` |  |  |
| `namespace` |  |  |
| `task_execution_id` |  |  |

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
)
```
Information needed at runtime to determine behavior such as whether or not outputs are discoverable, timeouts,
and retries.



| Parameter | Type |
|-|-|
| `discoverable` |  |
| `runtime` |  |
| `timeout` |  |
| `retries` |  |
| `interruptible` |  |
| `discovery_version` |  |
| `deprecated_error_message` |  |
| `cache_serializable` |  |
| `pod_template_name` |  |
| `cache_ignore_input_vars` |  |
| `is_eager` | `bool` |
| `generates_deck` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.TaskMetadata,
) -> e: TaskMetadata
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.TaskMetadata` |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `cache_ignore_input_vars` |  | {{< multiline >}}Input variables that should not be included when calculating hash for cache.
:rtype: tuple[Text]
{{< /multiline >}} |
| `cache_serializable` |  | {{< multiline >}}Whether or not caching operations are executed in serial. This means only a single instance over identical
inputs is executed, other concurrent executions wait for the cached results.
:rtype: bool
{{< /multiline >}} |
| `deprecated_error_message` |  | {{< multiline >}}This string can be used to mark the task as deprecated.  Consumers of the task will receive deprecation
warnings.
:rtype: Text
{{< /multiline >}} |
| `discoverable` |  | {{< multiline >}}Whether or not the outputs of this task should be cached for discovery.
:rtype: bool
{{< /multiline >}} |
| `discovery_version` |  | {{< multiline >}}This is the version used to create a logical version for data in the cache.
This is only used when `discoverable` is true.  Data is considered discoverable if: the inputs to a given
task are the same and the discovery_version is also the same.
:rtype: Text
{{< /multiline >}} |
| `generates_deck` |  | {{< multiline >}}Whether the task will generate a Deck.
:rtype: bool
{{< /multiline >}} |
| `interruptible` |  | {{< multiline >}}Whether or not the task is interruptible.
:rtype: bool
{{< /multiline >}} |
| `is_eager` |  |  |
| `is_empty` |  |  |
| `pod_template_name` |  | {{< multiline >}}The name of the existing PodTemplate resource which will be used in this task.
:rtype: Text
{{< /multiline >}} |
| `retries` |  | {{< multiline >}}Retry strategy for this task.  0 retries means only try once.
:rtype: flytekit.models.literals.RetryStrategy
{{< /multiline >}} |
| `runtime` |  | {{< multiline >}}Metadata describing the runtime environment for this task.
:rtype: RuntimeMetadata
{{< /multiline >}} |
| `timeout` |  | {{< multiline >}}The amount of time to wait before timing out.  This includes queuing and scheduler latency.
:rtype: datetime.timedelta
{{< /multiline >}} |

## flytekit.models.task.TaskSpec

```python
class TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
)
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.models.task.TaskTemplate` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskSpec
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.tasks_pb2.TaskSpec


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `docs` |  | {{< multiline >}}:rtype: Description entity for the task
{{< /multiline >}} |
| `is_empty` |  |  |
| `template` |  | {{< multiline >}}:rtype: TaskTemplate
{{< /multiline >}} |

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
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskTemplate
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.tasks_pb2.TaskTemplate


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `config` |  | {{< multiline >}}Arbitrary dictionary containing metadata for parsing and handling custom plugins.
:rtype: dict[Text, T]
{{< /multiline >}} |
| `container` |  | {{< multiline >}}If not None, the target of execution should be a container.
:rtype: Container
{{< /multiline >}} |
| `custom` |  | {{< multiline >}}Arbitrary dictionary containing metadata for custom plugins.
:rtype: dict[Text, T]
{{< /multiline >}} |
| `extended_resources` |  | {{< multiline >}}If not None, the extended resources to allocate to the task.
:rtype: flyteidl.core.tasks_pb2.ExtendedResources
{{< /multiline >}} |
| `id` |  | {{< multiline >}}This is generated by the system and uniquely identifies the task.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `interface` |  | {{< multiline >}}The interface definition for this task.
:rtype: flytekit.models.interface.TypedInterface
{{< /multiline >}} |
| `is_empty` |  |  |
| `k8s_pod` |  |  |
| `metadata` |  | {{< multiline >}}This contains information needed at runtime to determine behavior such as whether or not outputs are
discoverable, timeouts, and retries.
:rtype: TaskMetadata
{{< /multiline >}} |
| `security_context` |  |  |
| `sql` |  |  |
| `task_type_version` |  |  |
| `type` |  | {{< multiline >}}This is used to identify additional extensions for use by Propeller or SDK.
:rtype: Text
{{< /multiline >}} |

