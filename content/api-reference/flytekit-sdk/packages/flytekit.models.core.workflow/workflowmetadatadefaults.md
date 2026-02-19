---
title: WorkflowMetadataDefaults
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowMetadataDefaults

**Package:** `flytekit.models.core.workflow`

```python
class WorkflowMetadataDefaults(
    interruptible,
)
```
Metadata Defaults for the workflow.


| Parameter | Type | Description |
|-|-|-|
| `interruptible` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `interruptible` | `None` |  |
| `is_empty` | `None` |  |

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
:rtype: flyteidl.core.workflow_pb2.WorkflowMetadataDefaults


