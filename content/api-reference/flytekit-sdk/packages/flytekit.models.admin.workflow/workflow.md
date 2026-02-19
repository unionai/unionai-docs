---
title: Workflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Workflow

**Package:** `flytekit.models.admin.workflow`

```python
class Workflow(
    id,
    closure,
    short_description,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `closure` |  | |
| `short_description` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `closure` | `None` | :rtype: WorkflowClosure |
| `id` | `None` | :rtype: flytekit.models.core.identifier.Identifier |
| `is_empty` | `None` |  |
| `short_description` | `None` | :rtype: str |

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
:rtype: flyteidl.admin.workflow_pb2.Workflow


