---
title: Variable
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Variable

**Package:** `flytekit.models.interface`

```python
class Variable(
    type,
    description,
    artifact_partial_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
    artifact_tag: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag],
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |
| `description` |  | |
| `artifact_partial_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` | Optional Artifact object to control how the artifact is created when the task runs. |
| `artifact_tag` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag]` | Optional ArtifactTag object to automatically tag things. |

## Properties

| Property | Type | Description |
|-|-|-|
| `artifact_partial_id` | `None` |  |
| `artifact_tag` | `None` |  |
| `description` | `None` | This is a help string that can provide context for what this variable means in relation to a task or workflow. :rtype: Text |
| `is_empty` | `None` |  |
| `type` | `None` | This describes the type of value that must be provided to satisfy this variable. :rtype: flytekit.models.types.LiteralType |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`to_flyte_idl_list()`](#to_flyte_idl_list) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    variable_proto,
) -> flyteidl.core.interface_pb2.Variable
```
| Parameter | Type | Description |
|-|-|-|
| `variable_proto` |  | |

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
:rtype: flyteidl.core.interface_pb2.Variable


### to_flyte_idl_list()

```python
def to_flyte_idl_list()
```
:rtype: flyteidl.core.interface_pb2.Variable


