---
title: flytekit.models.project
version: 0.1.dev2192+g7c539c3.d20250403
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



| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |
| `description` |  |
| `state` |  |

### Methods

| Method | Description |
|-|-|
| [`active_project()`](#active_project) |  |
| [`archived_project()`](#archived_project) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### active_project()

```python
def active_project(
    id,
)
```
| Parameter | Type |
|-|-|
| `id` |  |

#### archived_project()

```python
def archived_project(
    id,
)
```
| Parameter | Type |
|-|-|
| `id` |  |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Project
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
:rtype: flyteidl.admin.project_pb2.Project


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `description` |  | {{< multiline >}}A concise description for this project.
:rtype: Text
{{< /multiline >}} |
| `id` |  | {{< multiline >}}A globally unique identifier associated with this project
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}A human-readable name for this project.
:rtype: Text
{{< /multiline >}} |
| `state` |  | {{< multiline >}}The state of this project.
:rtype: int
{{< /multiline >}} |

