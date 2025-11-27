---
title: ExecutionMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ExecutionMetadata

**Package:** `flytekit.models.execution`

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

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.execution_pb2.ExecutionMetadata


## Properties

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

