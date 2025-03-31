---
title: flytekit.models.execution
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`AbortMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionabortmetadata) |  |
| [`BoolValue`](.././flytekit.models.execution#flytekitmodelsexecutionboolvalue) | A ProtocolMessage. |
| [`ClusterAssignment`](.././flytekit.models.execution#flytekitmodelsexecutionclusterassignment) |  |
| [`DynamicWorkflowNodeMetadata`](.././flytekit.models.execution#flytekitmodelsexecutiondynamicworkflownodemetadata) |  |
| [`Execution`](.././flytekit.models.execution#flytekitmodelsexecutionexecution) |  |
| [`ExecutionClosure`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionclosure) |  |
| [`ExecutionClusterLabel`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionclusterlabel) |  |
| [`ExecutionMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionmetadata) |  |
| [`ExecutionSpec`](.././flytekit.models.execution#flytekitmodelsexecutionexecutionspec) |  |
| [`LiteralMapBlob`](.././flytekit.models.execution#flytekitmodelsexecutionliteralmapblob) |  |
| [`NodeExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionnodeexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`NotificationList`](.././flytekit.models.execution#flytekitmodelsexecutionnotificationlist) |  |
| [`SystemMetadata`](.././flytekit.models.execution#flytekitmodelsexecutionsystemmetadata) |  |
| [`TaskExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutiontaskexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |
| [`WorkflowExecutionGetDataResponse`](.././flytekit.models.execution#flytekitmodelsexecutionworkflowexecutiongetdataresponse) | Currently, node, task, and workflow execution all have the same get data response. |

### Variables

| Property | Type | Description |
|-|-|-|
| `annotations` | `_Feature` |  |

## flytekit.models.execution.AbortMetadata

```python
class AbortMetadata(
    cause: str,
    principal: str,
)
```
| Parameter | Type |
|-|-|
| `cause` | `str` |
| `principal` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.execution_pb2.AbortMetadata,
) -> AbortMetadata
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
| `cause` |  |  |
| `is_empty` |  |  |
| `principal` |  |  |

## flytekit.models.execution.BoolValue

A ProtocolMessage


## flytekit.models.execution.ClusterAssignment

```python
class ClusterAssignment(
    cluster_pool,
)
```
| Parameter | Type |
|-|-|
| `cluster_pool` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> flyteidl.admin.ClusterAssignment
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
| `cluster_pool` |  |  |
| `is_empty` |  |  |

## flytekit.models.execution.DynamicWorkflowNodeMetadata

```python
class DynamicWorkflowNodeMetadata(
    id: flytekit.models.core.identifier.Identifier,
    compiled_workflow: flytekit.models.core.compiler.CompiledWorkflowClosure,
)
```
| Parameter | Type |
|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` |
| `compiled_workflow` | `flytekit.models.core.compiler.CompiledWorkflowClosure` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata,
) -> DynamicWorkflowNodeMetadata
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
| `compiled_workflow` |  |  |
| `id` |  |  |
| `is_empty` |  |  |

## flytekit.models.execution.Execution

```python
class Execution(
    id,
    spec,
    closure,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `spec` |  |
| `closure` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
) -> Execution
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
| `closure` |  |  |
| `id` |  |  |
| `is_empty` |  |  |
| `spec` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ExecutionClosure
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

## flytekit.models.execution.ExecutionClusterLabel

```python
class ExecutionClusterLabel(
    value,
)
```
Label value to determine where the execution will be run



| Parameter | Type |
|-|-|
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ExecutionClusterLabel
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
| `is_empty` |  |  |
| `value` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
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
| `annotations` |  |  |
| `auth_role` |  |  |
| `cluster_assignment` |  |  |
| `disable_all` |  |  |
| `envs` |  |  |
| `execution_cluster_label` |  |  |
| `interruptible` |  |  |
| `is_empty` |  |  |
| `labels` |  |  |
| `launch_plan` |  | {{< multiline >}}If the values were too large, this is the URI where the values were offloaded.
{{< /multiline >}} |
| `max_parallelism` |  |  |
| `metadata` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `raw_output_data_config` |  |  |
| `security_context` |  |  |
| `tags` |  |  |

## flytekit.models.execution.LiteralMapBlob

```python
class LiteralMapBlob(
    values,
    uri,
)
```
| Parameter | Type |
|-|-|
| `values` |  |
| `uri` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
) -> LiteralMapBlob
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
| `is_empty` |  |  |
| `uri` |  |  |
| `values` |  |  |

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
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `dynamic_workflow` | `typing.Optional[DynamicWorkflowNodeMetadata]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> NodeExecutionGetDataResponse
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
| `dynamic_workflow` |  |  |
| `full_inputs` |  |  |
| `full_outputs` |  |  |
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.models.execution.NotificationList

```python
class NotificationList(
    notifications,
)
```
| Parameter | Type |
|-|-|
| `notifications` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> NotificationList
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
| `is_empty` |  |  |
| `notifications` |  |  |

## flytekit.models.execution.SystemMetadata

```python
class SystemMetadata(
    execution_cluster: str,
)
```
| Parameter | Type |
|-|-|
| `execution_cluster` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.execution_pb2.SystemMetadata,
) -> SystemMetadata
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
| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |
| `full_inputs` |  |
| `full_outputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskExecutionGetDataResponse
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
| `full_inputs` |  |  |
| `full_outputs` |  |  |
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

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
| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |
| `full_inputs` |  |
| `full_outputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowExecutionGetDataResponse
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
| `full_inputs` |  |  |
| `full_outputs` |  |  |
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

