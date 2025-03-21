---
title: flytekit.models.node_execution
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.node_execution

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicWorkflowNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executiondynamicworkflownodemetadata) | None. |
| [`NodeExecution`](.././flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecution) | None. |
| [`NodeExecutionClosure`](.././flytekit.models.node_execution#flytekitmodelsnode_executionnodeexecutionclosure) | None. |
| [`TaskNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executiontasknodemetadata) | None. |
| [`WorkflowNodeMetadata`](.././flytekit.models.node_execution#flytekitmodelsnode_executionworkflownodemetadata) | None. |

## flytekit.models.node_execution.DynamicWorkflowNodeMetadata

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

## flytekit.models.node_execution.NodeExecution

```python
def NodeExecution(
    id,
    input_uri,
    closure,
    metadata: flyteidl.admin.node_execution_pb2.NodeExecutionMetaData,
):
```
| Parameter | Type |
|-|-|
| `id` |  |
| `input_uri` |  |
| `closure` |  |
| `metadata` | `flyteidl.admin.node_execution_pb2.NodeExecutionMetaData` |

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
    p: flyteidl.admin.node_execution_pb2.NodeExecution,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.NodeExecution` |

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
| input_uri |  |  |
| is_empty |  |  |
| metadata |  |  |

## flytekit.models.node_execution.NodeExecutionClosure

```python
def NodeExecutionClosure(
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
):
```
| Parameter | Type |
|-|-|
| `phase` |  |
| `started_at` |  |
| `duration` |  |
| `output_uri` |  |
| `deck_uri` |  |
| `error` |  |
| `workflow_node_metadata` | `typing.Optional[flytekit.models.node_execution.WorkflowNodeMetadata]` |
| `task_node_metadata` | `typing.Optional[flytekit.models.node_execution.TaskNodeMetadata]` |
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
| created_at |  |  |
| deck_uri |  |  |
| duration |  |  |
| error |  |  |
| is_empty |  |  |
| output_uri |  |  |
| phase |  |  |
| started_at |  |  |
| target_metadata |  |  |
| task_node_metadata |  |  |
| updated_at |  |  |
| workflow_node_metadata |  |  |

## flytekit.models.node_execution.TaskNodeMetadata

```python
def TaskNodeMetadata(
    cache_status: int,
    catalog_key: flytekit.models.core.catalog.CatalogMetadata,
):
```
| Parameter | Type |
|-|-|
| `cache_status` | `int` |
| `catalog_key` | `flytekit.models.core.catalog.CatalogMetadata` |

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
    p: flyteidl.admin.node_execution_pb2.TaskNodeMetadata,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.TaskNodeMetadata` |

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
| cache_status |  |  |
| catalog_key |  |  |
| is_empty |  |  |

## flytekit.models.node_execution.WorkflowNodeMetadata

```python
def WorkflowNodeMetadata(
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
):
```
| Parameter | Type |
|-|-|
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` |

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
    p: flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.WorkflowNodeMetadata` |

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
| execution_id |  |  |
| is_empty |  |  |

