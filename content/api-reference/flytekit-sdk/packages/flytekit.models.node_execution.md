---
title: flytekit.models.node_execution
version: 1.16.14
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

### Properties

| Property | Type | Description |
|-|-|-|
| `compiled_workflow` | `None` |  |
| `id` | `None` |  |
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

### Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: NodeExecutionClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.NodeExecutionIdentifier |
| `input_uri` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `metadata` | `None` |  |

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

### Properties

| Property | Type | Description |
|-|-|-|
| `created_at` | `None` |  |
| `deck_uri` | `None` | :rtype: str |
| `duration` | `None` | :rtype: datetime.timedelta |
| `error` | `None` | :rtype: flytekit.models.core.execution.ExecutionError |
| `is_empty` | `None` |  |
| `output_uri` | `None` | :rtype: Text |
| `phase` | `None` | :rtype: int |
| `started_at` | `None` | :rtype: datetime.datetime |
| `target_metadata` | `None` |  |
| `task_node_metadata` | `None` |  |
| `updated_at` | `None` |  |
| `workflow_node_metadata` | `None` |  |

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

### Properties

| Property | Type | Description |
|-|-|-|
| `cache_status` | `None` |  |
| `catalog_key` | `None` |  |
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
## flytekit.models.node_execution.WorkflowNodeMetadata

```python
class WorkflowNodeMetadata(
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` | `None` |  |
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
