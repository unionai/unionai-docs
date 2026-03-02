---
title: flytekit.models.execution
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`AbortMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionabortmetadata) |  |
| [`ClusterAssignment`](.././flytekit.models.execution#flytekitmodelsexecutionclusterassignment) |  |
| [`Execution`](.././flytekit.models.execution#flytekitmodelsexecutionexecution) |  |
| [`ExecutionClosure`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) |  |
| [`ExecutionMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionmetadata) |  |
| [`ExecutionSpec`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionspec) |  |
| [`LiteralMapBlob`](.././flytekit.models.execution#flytekitmodelsexecutionliteralmapblob) |  |
| [`NodeExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) |  |
| [`NotificationList`](.././flytekit.models.execution#flytekitmodelsexecutionnotificationlist) |  |
| [`SystemMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) |  |
| [`TaskExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) |  |
| [`WorkflowExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) |  |

## flytekit.models.execution.AbortMetadata

```python
class AbortMetadata(
    cause: str,
    principal: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cause` | `str` | |
| `principal` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cause` | `None` |  |
| `is_empty` | `None` |  |
| `principal` | `None` |  |

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
    pb2_object: flyteidl.admin.execution_pb2.AbortMetadata,
) -> AbortMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.execution_pb2.AbortMetadata` | |

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
## flytekit.models.execution.ClusterAssignment

```python
class ClusterAssignment(
    cluster_pool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cluster_pool` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_pool` | `None` | :rtype: Text |
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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin._cluster_assignment_pb2.ClusterAssignment


## flytekit.models.execution.Execution

```python
class Execution(
    id,
    spec,
    closure,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `spec` |  | |
| `closure` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: ExecutionClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.WorkflowExecutionIdentifier |
| `is_empty` | `None` |  |
| `spec` | `None` | :rtype: ExecutionSpec |

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
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

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
:rtype: flyteidl.admin.execution_pb2.Execution


## flytekit.models.execution.ExecutionClosure

```python
class ExecutionClosure(
    phase: int,
    started_at: datetime.datetime,
    duration: datetime.timedelta,
    error: typing.Optional[_core_execution.ExecutionError],
    outputs: typing.Optional[LiteralMapBlob],
    abort_metadata: typing.Optional[AbortMetadata],
    created_at: typing.Optional[datetime.datetime],
    updated_at: typing.Optional[datetime.datetime],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` | `int` | From the flytekit.models.core.execution.WorkflowExecutionPhase enum |
| `started_at` | `datetime.datetime` | |
| `duration` | `datetime.timedelta` | Duration for which the execution has been running. |
| `error` | `typing.Optional[_core_execution.ExecutionError]` | |
| `outputs` | `typing.Optional[LiteralMapBlob]` | |
| `abort_metadata` | `typing.Optional[AbortMetadata]` | Specifies metadata around an aborted workflow execution. |
| `created_at` | `typing.Optional[datetime.datetime]` | |
| `updated_at` | `typing.Optional[datetime.datetime]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `abort_metadata` | `None` |  |
| `created_at` | `None` |  |
| `duration` | `None` |  |
| `error` | `None` |  |
| `is_empty` | `None` |  |
| `outputs` | `None` |  |
| `phase` | `None` | From the flytekit.models.core.execution.WorkflowExecutionPhase enum |
| `started_at` | `None` |  |
| `updated_at` | `None` |  |

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
:rtype: flyteidl.admin.execution_pb2.ExecutionClosure


## flytekit.models.execution.ExecutionMetadata

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
| Parameter | Type | Description |
|-|-|-|
| `mode` | `int` | An enum value from ExecutionMetadata.ExecutionMode which specifies how the job started. |
| `principal` | `str` | The entity that triggered the execution |
| `nesting` | `int` | An integer representing how deeply nested the workflow is (i.e. was it triggered by a parent workflow) |
| `scheduled_at` | `Optional[datetime.datetime]` | For scheduled executions, the requested time for execution for this specific schedule invocation. |
| `parent_node_execution` | `Optional[_identifier.NodeExecutionIdentifier]` | Which subworkflow node (if any) launched this execution |
| `reference_execution` | `Optional[_identifier.WorkflowExecutionIdentifier]` | Optional, reference workflow execution related to this execution |
| `system_metadata` | `Optional[SystemMetadata]` | Optional, platform-specific metadata about the execution. |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `mode` | `None` | An enum value from ExecutionMetadata.ExecutionMode which specifies how the job started. |
| `nesting` | `None` | An integer representing how deeply nested the workflow is (i.e. was it triggered by a parent workflow) |
| `parent_node_execution` | `None` | Which subworkflow node (if any) launched this execution |
| `principal` | `None` | The entity that triggered the execution |
| `reference_execution` | `None` | Optional, reference workflow execution related to this execution |
| `scheduled_at` | `None` | For scheduled executions, the requested time for execution for this specific schedule invocation. |
| `system_metadata` | `None` | Optional, platform-specific metadata about the execution. |

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
:rtype: flyteidl.admin.execution_pb2.ExecutionMetadata


## flytekit.models.execution.ExecutionSpec

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
| Parameter | Type | Description |
|-|-|-|
| `launch_plan` |  | |
| `metadata` |  | |
| `notifications` |  | |
| `disable_all` |  | |
| `labels` |  | |
| `annotations` |  | |
| `auth_role` |  | |
| `raw_output_data_config` |  | Optional location of offloaded data for things like S3, etc. |
| `max_parallelism` | `Optional[int]` | |
| `security_context` | `Optional[security.SecurityContext]` | Optional security context to use for this execution. |
| `overwrite_cache` | `Optional[bool]` | Optional flag to overwrite the cache for this execution. |
| `interruptible` | `Optional[bool]` | Optional flag to override the default interruptible flag of the executed entity. |
| `envs` | `Optional[_common_models.Envs]` | flytekit.models.common.Envs environment variables to set for this execution. |
| `tags` | `Optional[typing.List[str]]` | Optional list of tags to apply to the execution. |
| `cluster_assignment` | `Optional[ClusterAssignment]` | |
| `execution_cluster_label` | `Optional[ExecutionClusterLabel]` | Optional execution cluster label to use for this execution. |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` | `None` | :rtype: flytekit.models.common.Annotations |
| `auth_role` | `None` | :rtype: flytekit.models.common.AuthRole |
| `cluster_assignment` | `None` |  |
| `disable_all` | `None` | :rtype: Optional[bool] |
| `envs` | `None` |  |
| `execution_cluster_label` | `None` |  |
| `interruptible` | `None` |  |
| `is_empty` | `None` |  |
| `labels` | `None` | :rtype: flytekit.models.common.Labels |
| `launch_plan` | `None` | If the values were too large, this is the URI where the values were offloaded. :rtype: flytekit.models.core.identifier.Identifier |
| `max_parallelism` | `None` |  |
| `metadata` | `None` | :rtype: ExecutionMetadata |
| `notifications` | `None` | :rtype: Optional[NotificationList] |
| `overwrite_cache` | `None` |  |
| `raw_output_data_config` | `None` | :rtype: flytekit.models.common.RawOutputDataConfig |
| `security_context` | `None` |  |
| `tags` | `None` |  |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.execution_pb2.ExecutionSpec


## flytekit.models.execution.LiteralMapBlob

```python
class LiteralMapBlob(
    values,
    uri,
)
```
| Parameter | Type | Description |
|-|-|-|
| `values` |  | |
| `uri` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `uri` | `None` | :rtype: Text |
| `values` | `None` | :rtype: flytekit.models.literals.LiteralMap |

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
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

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
:rtype: flyteidl.admin.execution_pb2.LiteralMapBlob


## flytekit.models.execution.NodeExecutionGetDataResponse

```python
class NodeExecutionGetDataResponse(
    args,
    dynamic_workflow: typing.Optional[DynamicWorkflowNodeMetadata],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `dynamic_workflow` | `typing.Optional[DynamicWorkflowNodeMetadata]` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `dynamic_workflow` | `None` |  |
| `full_inputs` | `None` | :rtype: _literals_models.LiteralMap |
| `full_outputs` | `None` | :rtype: _literals_models.LiteralMap |
| `inputs` | `None` | :rtype: _common_models.UrlBlob |
| `is_empty` | `None` |  |
| `outputs` | `None` | :rtype: _common_models.UrlBlob |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _node_execution_pb2. |


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
:rtype: _node_execution_pb2.NodeExecutionGetDataResponse


## flytekit.models.execution.NotificationList

```python
class NotificationList(
    notifications,
)
```
| Parameter | Type | Description |
|-|-|-|
| `notifications` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `notifications` | `None` | :rtype: list[flytekit.models.common.Notification] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype:  flyteidl. |


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
:rtype:  flyteidl.admin.execution_pb2.NotificationList


## flytekit.models.execution.SystemMetadata

```python
class SystemMetadata(
    execution_cluster: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_cluster` | `str` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `execution_cluster` | `None` |  |
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
    pb2_object: flyteidl.admin.execution_pb2.SystemMetadata,
) -> SystemMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.execution_pb2.SystemMetadata` | |

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
## flytekit.models.execution.TaskExecutionGetDataResponse

```python
class TaskExecutionGetDataResponse(
    inputs,
    outputs,
    full_inputs,
    full_outputs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` |  | |
| `outputs` |  | |
| `full_inputs` |  | |
| `full_outputs` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `full_inputs` | `None` | :rtype: _literals_models.LiteralMap |
| `full_outputs` | `None` | :rtype: _literals_models.LiteralMap |
| `inputs` | `None` | :rtype: _common_models.UrlBlob |
| `is_empty` | `None` |  |
| `outputs` | `None` | :rtype: _common_models.UrlBlob |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _task_execution_pb2. |


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
:rtype: _task_execution_pb2.TaskExecutionGetDataResponse


## flytekit.models.execution.WorkflowExecutionGetDataResponse

```python
class WorkflowExecutionGetDataResponse(
    inputs,
    outputs,
    full_inputs,
    full_outputs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` |  | |
| `outputs` |  | |
| `full_inputs` |  | |
| `full_outputs` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `full_inputs` | `None` | :rtype: _literals_models.LiteralMap |
| `full_outputs` | `None` | :rtype: _literals_models.LiteralMap |
| `inputs` | `None` | :rtype: _common_models.UrlBlob |
| `is_empty` | `None` |  |
| `outputs` | `None` | :rtype: _common_models.UrlBlob |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _execution_pb2. |


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
:rtype: _execution_pb2.WorkflowExecutionGetDataResponse


