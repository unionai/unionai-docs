---
title: flytekit.models.execution
version: 1.16.10
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
| [`NodeExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`NotificationList`](.././flytekit.models.execution#flytekitmodelsexecutionnotificationlist) |  |
| [`SystemMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) |  |
| [`TaskExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`WorkflowExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |

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
### Properties

| Property | Type | Description |
|-|-|-|
| `cause` |  |  |
| `is_empty` |  |  |
| `principal` |  |  |

## flytekit.models.execution.ClusterAssignment

```python
class ClusterAssignment(
    cluster_pool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cluster_pool` |  | |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_pool` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: ExecutionClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.WorkflowExecutionIdentifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `spec` |  | {{< multiline >}}:rtype: ExecutionSpec
{{< /multiline >}} |

## flytekit.models.execution.ExecutionClosure

```python
class ExecutionClosure(
    phase: int,
    started_at: datetime.datetime,
    duration: datetime.timedelta,
    error: typing.Optional[flytekit.models.core.execution.ExecutionError],
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
| `error` | `typing.Optional[flytekit.models.core.execution.ExecutionError]` | |
| `outputs` | `typing.Optional[LiteralMapBlob]` | |
| `abort_metadata` | `typing.Optional[AbortMetadata]` | Specifies metadata around an aborted workflow execution. |
| `created_at` | `typing.Optional[datetime.datetime]` | |
| `updated_at` | `typing.Optional[datetime.datetime]` | |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `abort_metadata` |  |  |
| `created_at` |  |  |
| `duration` |  |  |
| `error` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |
| `phase` |  | {{< multiline >}}From the flytekit.models.core.execution.WorkflowExecutionPhase enum
{{< /multiline >}} |
| `started_at` |  |  |
| `updated_at` |  |  |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  | {{< multiline >}}:rtype: flytekit.models.common.Annotations
{{< /multiline >}} |
| `auth_role` |  | {{< multiline >}}:rtype: flytekit.models.common.AuthRole
{{< /multiline >}} |
| `cluster_assignment` |  |  |
| `disable_all` |  | {{< multiline >}}:rtype: Optional[bool]
{{< /multiline >}} |
| `envs` |  |  |
| `execution_cluster_label` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `labels` |  | {{< multiline >}}:rtype: flytekit.models.common.Labels
{{< /multiline >}} |
| `launch_plan` |  | {{< multiline >}}If the values were too large, this is the URI where the values were offloaded.
:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `metadata` |  | {{< multiline >}}:rtype: ExecutionMetadata
{{< /multiline >}} |
| `notifications` |  | {{< multiline >}}:rtype: Optional[NotificationList]
{{< /multiline >}} |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  | {{< multiline >}}:rtype: flytekit.models.common.RawOutputDataConfig
{{< /multiline >}} |
| `security_context` |  |  |
| `tags` |  |  |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `values` |  | {{< multiline >}}:rtype: flytekit.models.literals.LiteralMap
{{< /multiline >}} |

## flytekit.models.execution.NodeExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


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


### Properties

| Property | Type | Description |
|-|-|-|
| `dynamic_workflow` |  |  |
| `full_inputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `full_outputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |
| `is_empty` |  |  |
| `outputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |

## flytekit.models.execution.NotificationList

```python
class NotificationList(
    notifications,
)
```
| Parameter | Type | Description |
|-|-|-|
| `notifications` |  | |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `notifications` |  | {{< multiline >}}:rtype: list[flytekit.models.common.Notification]
{{< /multiline >}} |

## flytekit.models.execution.SystemMetadata

```python
class SystemMetadata(
    execution_cluster: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_cluster` | `str` | |

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
### Properties

| Property | Type | Description |
|-|-|-|
| `execution_cluster` |  |  |
| `is_empty` |  |  |

## flytekit.models.execution.TaskExecutionGetDataResponse

Currently, node, task, and workflow execution all have the same get data response. So we'll create this common
superclass to reduce code duplication until things diverge in the future.


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


### Properties

| Property | Type | Description |
|-|-|-|
| `full_inputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `full_outputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |
| `is_empty` |  |  |
| `outputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |

## flytekit.models.execution.WorkflowExecutionGetDataResponse

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
| Parameter | Type | Description |
|-|-|-|
| `inputs` |  | |
| `outputs` |  | |
| `full_inputs` |  | |
| `full_outputs` |  | |

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


### Properties

| Property | Type | Description |
|-|-|-|
| `full_inputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `full_outputs` |  | {{< multiline >}}:rtype: _literals_models.LiteralMap
{{< /multiline >}} |
| `inputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |
| `is_empty` |  |  |
| `outputs` |  | {{< multiline >}}:rtype: _common_models.UrlBlob
{{< /multiline >}} |

