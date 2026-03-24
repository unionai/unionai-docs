---
title: flytekit.models.project
version: 1.16.15
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.project

## Directory

### Classes

| Class | Description |
|-|-|
| [`Project`](.././flytekit.models.project#flytekitmodelsprojectproject) |  |

## flytekit.models.project.Project

### Parameters

```python
class Project(
    id,
    name,
    description,
    state,
)
```
A project represents a logical grouping used to organize entities (tasks, workflows, executions) in the Flyte
platform.



| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `name` |  | |
| `description` |  | |
| `state` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `description` | `None` | A concise description for this project. |
| `id` | `None` | A globally unique identifier associated with this project |
| `is_empty` | `None` |  |
| `name` | `None` | A human-readable name for this project. |
| `state` | `None` | The state of this project. |

### Methods

| Method | Description |
|-|-|
| [`active_project()`](#active_project) |  |
| [`archived_project()`](#archived_project) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### active_project()

```python
def active_project(
    id,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |

#### archived_project()

```python
def archived_project(
    id,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** Project

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.project_pb2.Project

