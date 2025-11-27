---
title: BranchNode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BranchNode

**Package:** `flytekit.models.core.workflow`

```python
class BranchNode(
    if_else: flytekit.models.core.workflow.IfElseBlock,
)
```
BranchNode is a special node that alter the flow of the workflow graph. It allows the control flow to branch at
runtime based on a series of conditions that get evaluated on various parameters (e.g. inputs, primitives).



| Parameter | Type | Description |
|-|-|-|
| `if_else` | `flytekit.models.core.workflow.IfElseBlock` | |

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
    pb2_objct,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_objct` |  | |

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
:rtype: flyteidl.core.workflow_pb2.BranchNode


## Properties

| Property | Type | Description |
|-|-|-|
| `if_else` |  | {{< multiline >}}:rtype: IfElseBlock
{{< /multiline >}} |
| `is_empty` |  |  |

