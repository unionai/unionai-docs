---
title: DynamicWorkflowNodeMetadata
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DynamicWorkflowNodeMetadata

**Package:** `flytekit.models.node_execution`

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

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata,
) -> DynamicWorkflowNodeMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.admin.node_execution_pb2.DynamicWorkflowNodeMetadata` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `compiled_workflow` |  |  |
| `id` |  |  |
| `is_empty` |  |  |

