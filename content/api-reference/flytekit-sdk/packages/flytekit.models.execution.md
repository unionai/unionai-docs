---
title: flytekit.models.execution
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`AbortMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionabortmetadata) | None. |
| [`BoolValue`](.././flytekit.models.execution#flytekitmodelsexecutionboolvalue) | A ProtocolMessage. |
| [`ClusterAssignment`](.././flytekit.models.execution#flytekitmodelsexecutionclusterassignment) | None. |
| [`DynamicWorkflowNodeMetadata`](.././flytekit.models.execution#flytekitmodelsexecutiondynamicworkflownodemetadata) | None. |
| [`Execution`](.././flytekit.models.execution#flytekitmodelsexecutionexecution) | None. |
| [`ExecutionClosure`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) | None. |
| [`ExecutionClusterLabel`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionclusterlabel) | None. |
| [`ExecutionMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionmetadata) | None. |
| [`ExecutionSpec`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionspec) | None. |
| [`LiteralMapBlob`](.././flytekit.models.execution#flytekitmodelsexecutionliteralmapblob) | None. |
| [`NodeExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`NotificationList`](.././flytekit.models.execution#flytekitmodelsexecutionnotificationlist) | None. |
| [`SystemMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) | None. |
| [`TaskExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`WorkflowExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |

## flytekit.models.execution.AbortMetadata

```python
def AbortMetadata(
    cause: str,
    principal: str,
):
```
| Parameter | Type |
|-|-|
| `cause` | `str` |
| `principal` | `str` |

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
    pb2_object: flyteidl.admin.execution_pb2.AbortMetadata,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.execution_pb2.AbortMetadata` |

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
| cause |  |  |
| is_empty |  |  |
| principal |  |  |

## flytekit.models.execution.BoolValue

A ProtocolMessage


## flytekit.models.execution.ClusterAssignment

```python
def ClusterAssignment(
    cluster_pool,
):
```
| Parameter | Type |
|-|-|
| `cluster_pool` |  |

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
    p,
):
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
| cluster_pool |  |  |
| is_empty |  |  |

## flytekit.models.execution.DynamicWorkflowNodeMetadata

```python
def DynamicWorkflowNodeMetadata(
    id: flytekit.models.core.identifier.Identifier,
    compiled_workflow: flytekit.models.core.compiler.CompiledWorkflowClosure,
):
```
| Parameter | Type |
|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` |
| `compiled_workflow` | `flytekit.models.core.compiler.CompiledWorkflowClosure` |

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
    p: flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata` |

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
| compiled_workflow |  |  |
| id |  |  |
| is_empty |  |  |

## flytekit.models.execution.Execution

```python
def Execution(
    id,
    spec,
    closure,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `spec` |  |
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
    pb,
):
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
| closure |  |  |
| id |  |  |
| is_empty |  |  |
| spec |  |  |

## flytekit.models.execution.ExecutionClosure

```python
def ExecutionClosure(
    phase: int,
    started_at: datetime.datetime,
    duration: datetime.timedelta,
    error: typing.Optional[flytekit.models.core.execution.ExecutionError],
    outputs: typing.Optional[LiteralMapBlob],
    abort_metadata: typing.Optional[AbortMetadata],
    created_at: typing.Optional[datetime.datetime],
    updated_at: typing.Optional[datetime.datetime],
):
```
| Parameter | Type |
|-|-|
| `phase` | `int` |
| `started_at` | `datetime.datetime` |
| `duration` | `datetime.timedelta` |
| `error` | `typing.Optional[flytekit.models.core.execution.ExecutionError]` |
| `outputs` | `typing.Optional[LiteralMapBlob]` |
| `abort_metadata` | `typing.Optional[AbortMetadata]` |
| `created_at` | `typing.Optional[datetime.datetime]` |
| `updated_at` | `typing.Optional[datetime.datetime]` |

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
| abort_metadata |  |  |
| created_at |  |  |
| duration |  |  |
| error |  |  |
| is_empty |  |  |
| outputs |  |  |
| phase |  |  |
| started_at |  |  |
| updated_at |  |  |

## flytekit.models.execution.ExecutionClusterLabel

```python
def ExecutionClusterLabel(
    value,
):
```
Label value to determine where the execution will be run



| Parameter | Type |
|-|-|
| `value` |  |

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
| value |  |  |

## flytekit.models.execution.ExecutionMetadata

```python
def ExecutionMetadata(
    mode: int,
    principal: str,
    nesting: int,
    scheduled_at: Optional[datetime.datetime],
    parent_node_execution: Optional[_identifier.NodeExecutionIdentifier],
    reference_execution: Optional[_identifier.WorkflowExecutionIdentifier],
    system_metadata: Optional[SystemMetadata],
):
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
| mode |  |  |
| nesting |  |  |
| parent_node_execution |  |  |
| principal |  |  |
| reference_execution |  |  |
| scheduled_at |  |  |
| system_metadata |  |  |

## flytekit.models.execution.ExecutionSpec

```python
def ExecutionSpec(
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
):
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| annotations |  |  |
| auth_role |  |  |
| cluster_assignment |  |  |
| disable_all |  |  |
| envs |  |  |
| execution_cluster_label |  |  |
| interruptible |  |  |
| is_empty |  |  |
| labels |  |  |
| launch_plan |  |  |
| max_parallelism |  |  |
| metadata |  |  |
| notifications |  |  |
| overwrite_cache |  |  |
| raw_output_data_config |  |  |
| security_context |  |  |
| tags |  |  |

## flytekit.models.execution.LiteralMapBlob

```python
def LiteralMapBlob(
    values,
    uri,
):
```
| Parameter | Type |
|-|-|
| `values` |  |
| `uri` |  |

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
    pb,
):
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
| is_empty |  |  |
| uri |  |  |
| values |  |  |

## flytekit.models.execution.NodeExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


```python
def NodeExecutionGetDataResponse(
    args,
    dynamic_workflow: typing.Optional[DynamicWorkflowNodeMetadata],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `dynamic_workflow` | `typing.Optional[DynamicWorkflowNodeMetadata]` |
| `kwargs` | ``**kwargs`` |

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
| dynamic_workflow |  |  |
| full_inputs |  |  |
| full_outputs |  |  |
| inputs |  |  |
| is_empty |  |  |
| outputs |  |  |

## flytekit.models.execution.NotificationList

```python
def NotificationList(
    notifications,
):
```
| Parameter | Type |
|-|-|
| `notifications` |  |

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
| notifications |  |  |

## flytekit.models.execution.SystemMetadata

```python
def SystemMetadata(
    execution_cluster: str,
):
```
| Parameter | Type |
|-|-|
| `execution_cluster` | `str` |

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
    pb2_object: flyteidl.admin.execution_pb2.SystemMetadata,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.execution_pb2.SystemMetadata` |

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
| execution_cluster |  |  |
| is_empty |  |  |

## flytekit.models.execution.TaskExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


```python
def TaskExecutionGetDataResponse(
    inputs,
    outputs,
    full_inputs,
    full_outputs,
):
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
| full_inputs |  |  |
| full_outputs |  |  |
| inputs |  |  |
| is_empty |  |  |
| outputs |  |  |

## flytekit.models.execution.WorkflowExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


```python
def WorkflowExecutionGetDataResponse(
    inputs,
    outputs,
    full_inputs,
    full_outputs,
):
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
| full_inputs |  |  |
| full_outputs |  |  |
| inputs |  |  |
| is_empty |  |  |
| outputs |  |  |

