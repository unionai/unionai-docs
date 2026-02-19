---
title: CompiledWorkflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CompiledWorkflow

**Package:** `flytekit.models.core.compiler`

```python
class CompiledWorkflow(
    template,
    connections,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |
| `connections` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `connections` | `None` | :rtype: ConnectionSet |
| `is_empty` | `None` |  |
| `template` | `None` | :rtype: flytekit.models.core.workflow.WorkflowTemplate |

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
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.core.compiler_pb2.CompiledWorkflow


