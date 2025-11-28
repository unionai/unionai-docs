---
title: flytekit.models.node_execution
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.node_execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicWorkflowNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executiondynamicworkflownodemetadata) |  |
| [`NodeExecution`](.././flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecution) |  |
| [`NodeExecutionClosure`](.././flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecutionclosure) |  |
| [`TaskNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executiontasknodemetadata) |  |
| [`WorkflowNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executionworkflownodemetadata) |  |

## flytekit.models.node_execution.DynamicWorkflowNodeMetadata

```python
class DynamicWorkflowNodeMetadata(
    id: flytekit.models.core.identifier.Identifier,
    compiled_workflow: flytekit.models.core.compiler.CompiledWorkflowClosure,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` | `flytekit.models.core.identifier.Identifier` | |
| `compiled_workflow` | `flytekit.models.core.compiler.CompiledWorkflowClosure` | |

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
    p: flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata,
) -> DynamicWorkflowNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata` | |

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
| `compiled_workflow` |  |  |
| `id` |  |  |
| `is_empty` |  |  |

## flytekit.models.node_execution.NodeExecution

```python
class NodeExecution(
    id,
    input_uri,
    closure,
    metadata: flyteidl.admin.node_execution_pb2.NodeExecutionMetaData,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `input_uri` |  | |
| `closure` |  | |
| `metadata` | `flyteidl.admin.node_execution_pb2.NodeExecutionMetaData` | |

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
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
) -> NodeExecution
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` | |

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
| `closure` |  | {{< multiline >}}:rtype: NodeExecutionClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.NodeExecutionIdentifier
{{< /multiline >}} |
| `input_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `metadata` |  |  |

## flytekit.models.node_execution.NodeExecutionClosure

```python
class NodeExecutionClosure(
    phase,
    started_at,
    duration,
    output_uri,
    deck_uri,
    error,
    workflow_node_metadata: typing.Optional[flytekit.models.node_execution.WorkflowNodeMetadata],
    task_node_metadata: typing.Optional[flytekit.models.node_execution.TaskNodeMetadata],
    created_at: typing.Optional[datetime.datetime],
    updated_at: typing.Optional[datetime.datetime],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` |  | |
| `started_at` |  | |
| `duration` |  | |
| `output_uri` |  | |
| `deck_uri` |  | |
| `error` |  | |
| `workflow_node_metadata` | `typing.Optional[flytekit.models.node_execution.WorkflowNodeMetadata]` | |
| `task_node_metadata` | `typing.Optional[flytekit.models.node_execution.TaskNodeMetadata]` | |
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
:rtype: flyteidl.admin.node_execution_pb2.NodeExecutionClosure


### Properties

| Property | Type | Description |
|-|-|-|
| `created_at` |  |  |
| `deck_uri` |  | {{< multiline >}}:rtype: str
{{< /multiline >}} |
| `duration` |  | {{< multiline >}}:rtype: datetime.timedelta
{{< /multiline >}} |
| `error` |  | {{< multiline >}}:rtype: flytekit.models.core.execution.ExecutionError
{{< /multiline >}} |
| `is_empty` |  |  |
| `output_uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `phase` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `started_at` |  | {{< multiline >}}:rtype: datetime.datetime
{{< /multiline >}} |
| `target_metadata` |  |  |
| `task_node_metadata` |  |  |
| `updated_at` |  |  |
| `workflow_node_metadata` |  |  |

## flytekit.models.node_execution.TaskNodeMetadata

```python
class TaskNodeMetadata(
    cache_status: int,
    catalog_key: flytekit.models.core.catalog.CatalogMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cache_status` | `int` | |
| `catalog_key` | `flytekit.models.core.catalog.CatalogMetadata` | |

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
    p: flyteidl.admin.node_execution_pb2.TaskNodeMetadata,
) -> TaskNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.TaskNodeMetadata` | |

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
| `cache_status` |  |  |
| `catalog_key` |  |  |
| `is_empty` |  |  |

## flytekit.models.node_execution.WorkflowNodeMetadata

```python
class WorkflowNodeMetadata(
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` | |

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
    p: flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata,
) -> WorkflowNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata` | |

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
| `execution_id` |  |  |
| `is_empty` |  |  |

