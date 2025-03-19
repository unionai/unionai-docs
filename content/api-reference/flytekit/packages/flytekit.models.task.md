---
title: flytekit.models.task
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`BoolValue`](.././flytekit.models.task#flytekitmodelstaskboolvalue) | A ProtocolMessage. |
| [`CompiledTask`](.././flytekit.models.task#flytekitmodelstaskcompiledtask) | None. |
| [`Container`](.././flytekit.models.task#flytekitmodelstaskcontainer) | None. |
| [`DataLoadingConfig`](.././flytekit.models.task#flytekitmodelstaskdataloadingconfig) | None. |
| [`Documentation`](.././flytekit.models.task#flytekitmodelstaskdocumentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`IOStrategy`](.././flytekit.models.task#flytekitmodelstaskiostrategy) | Provides methods to manage data in and out of the Raw container using Download Modes. |
| [`K8sObjectMetadata`](.././flytekit.models.task#flytekitmodelstaskk8sobjectmetadata) | None. |
| [`K8sPod`](.././flytekit.models.task#flytekitmodelstaskk8spod) | None. |
| [`Resources`](.././flytekit.models.task#flytekitmodelstaskresources) | None. |
| [`RuntimeMetadata`](.././flytekit.models.task#flytekitmodelstaskruntimemetadata) | None. |
| [`Sql`](.././flytekit.models.task#flytekitmodelstasksql) | None. |
| [`Task`](.././flytekit.models.task#flytekitmodelstasktask) | None. |
| [`TaskClosure`](.././flytekit.models.task#flytekitmodelstasktaskclosure) | None. |
| [`TaskExecutionMetadata`](.././flytekit.models.task#flytekitmodelstasktaskexecutionmetadata) | None. |
| [`TaskMetadata`](.././flytekit.models.task#flytekitmodelstasktaskmetadata) | None. |
| [`TaskSpec`](.././flytekit.models.task#flytekitmodelstasktaskspec) | None. |
| [`TaskTemplate`](.././flytekit.models.task#flytekitmodelstasktasktemplate) | None. |

## flytekit.models.task.BoolValue

A ProtocolMessage


## flytekit.models.task.CompiledTask

```python
def CompiledTask(
    template,
):
```
| Parameter | Type |
|-|-|
| `template` |  |

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
| template |  |  |

## flytekit.models.task.Container

```python
def Container(
    image,
    command,
    args,
    resources,
    env,
    config,
    data_loading_config,
):
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
| [`add_env()`](#add_env) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### add_env()

```python
def add_env(
    key: str,
    val: str,
):
```
| Parameter | Type |
|-|-|
| `key` | `str` |
| `val` | `str` |

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
| args |  |  |
| command |  |  |
| config |  |  |
| data_loading_config |  |  |
| env |  |  |
| image |  |  |
| is_empty |  |  |
| resources |  |  |

## flytekit.models.task.DataLoadingConfig

```python
def DataLoadingConfig(
    input_path: str,
    output_path: str,
    enabled: bool,
    format: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526acf0>,
    io_strategy: flytekit.models.task.IOStrategy,
):
```
| Parameter | Type |
|-|-|
| `input_path` | `str` |
| `output_path` | `str` |
| `enabled` | `bool` |
| `format` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526acf0>` |
| `io_strategy` | `flytekit.models.task.IOStrategy` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.core.tasks_pb2.DataLoadingConfig,
):
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

## flytekit.models.task.Documentation

DescriptionEntity contains detailed description for the task/workflow/launch plan.
Documentation could provide insight into the algorithms, business use case, etc.


```python
def Documentation(
    short_description: typing.Optional[str],
    long_description: typing.Optional[flytekit.models.documentation.Description],
    source_code: typing.Optional[flytekit.models.documentation.SourceCode],
):
```
| Parameter | Type |
|-|-|
| `short_description` | `typing.Optional[str]` |
| `long_description` | `typing.Optional[flytekit.models.documentation.Description]` |
| `source_code` | `typing.Optional[flytekit.models.documentation.SourceCode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.DescriptionEntity,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.DescriptionEntity` |

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

## flytekit.models.task.IOStrategy

Provides methods to manage data in and out of the Raw container using Download Modes. This can only be used if DataLoadingConfig is enabled.


```python
def IOStrategy(
    download_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526b4a0>,
    upload_mode: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526b080>,
):
```
| Parameter | Type |
|-|-|
| `download_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526b4a0>` |
| `upload_mode` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10526b080>` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.IOStrategy,
):
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

## flytekit.models.task.K8sObjectMetadata

```python
def K8sObjectMetadata(
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
):
```
This defines additional metadata for building a kubernetes pod.


| Parameter | Type |
|-|-|
| `labels` | `typing.Dict[str, str]` |
| `annotations` | `typing.Dict[str, str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sObjectMetadata,
):
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
| is_empty |  |  |
| labels |  |  |

## flytekit.models.task.K8sPod

```python
def K8sPod(
    metadata: flytekit.models.task.K8sObjectMetadata,
    pod_spec: typing.Dict[str, typing.Any],
    data_config: typing.Optional[flytekit.models.task.DataLoadingConfig],
    primary_container_name: typing.Optional[str],
):
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
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`from_pod_template()`](#from_pod_template) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`to_pod_template()`](#to_pod_template) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sPod,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sPod` |

#### from_pod_template()

```python
def from_pod_template(
    pod_template: PodTemplate,
):
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
### Properties

| Property | Type | Description |
|-|-|-|
| data_config |  |  |
| is_empty |  |  |
| metadata |  |  |
| pod_spec |  |  |
| primary_container_name |  |  |

## flytekit.models.task.Resources

```python
def Resources(
    requests,
    limits,
):
```
| Parameter | Type |
|-|-|
| `requests` |  |
| `limits` |  |

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
| limits |  |  |
| requests |  |  |

## flytekit.models.task.RuntimeMetadata

```python
def RuntimeMetadata(
    type,
    version,
    flavor,
):
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
| flavor |  |  |
| is_empty |  |  |
| type |  |  |
| version |  |  |

## flytekit.models.task.Sql

```python
def Sql(
    statement: str,
    dialect: int,
):
```
This defines a kubernetes pod target. It will build the pod target during task execution


| Parameter | Type |
|-|-|
| `statement` | `str` |
| `dialect` | `int` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.Sql,
):
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
| dialect |  |  |
| is_empty |  |  |
| statement |  |  |

## flytekit.models.task.Task

```python
def Task(
    id,
    closure,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `closure` |  |

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
| closure |  |  |
| id |  |  |
| is_empty |  |  |

## flytekit.models.task.TaskClosure

```python
def TaskClosure(
    compiled_task,
):
```
| Parameter | Type |
|-|-|
| `compiled_task` |  |

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
| compiled_task |  |  |
| is_empty |  |  |

## flytekit.models.task.TaskExecutionMetadata

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

## flytekit.models.task.TaskMetadata

```python
def TaskMetadata(
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
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.TaskMetadata,
):
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
| cache_ignore_input_vars |  |  |
| cache_serializable |  |  |
| deprecated_error_message |  |  |
| discoverable |  |  |
| discovery_version |  |  |
| generates_deck |  |  |
| interruptible |  |  |
| is_eager |  |  |
| is_empty |  |  |
| pod_template_name |  |  |
| retries |  |  |
| runtime |  |  |
| timeout |  |  |

## flytekit.models.task.TaskSpec

```python
def TaskSpec(
    template: flytekit.models.task.TaskTemplate,
    docs: typing.Optional[flytekit.models.documentation.Documentation],
):
```
| Parameter | Type |
|-|-|
| `template` | `flytekit.models.task.TaskTemplate` |
| `docs` | `typing.Optional[flytekit.models.documentation.Documentation]` |

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
| docs |  |  |
| is_empty |  |  |
| template |  |  |

## flytekit.models.task.TaskTemplate

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

