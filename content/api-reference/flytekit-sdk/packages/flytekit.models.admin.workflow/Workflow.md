---
title: Workflow
version: 1.16.10
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


## Properties

| Property | Type | Description |
|-|-|-|
| `closure` |  | {{< multiline >}}:rtype: WorkflowClosure
{{< /multiline >}} |
| `id` |  | {{< multiline >}}:rtype: flytekit.models.core.identifier.Identifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `short_description` |  | {{< multiline >}}:rtype: str
{{< /multiline >}} |

