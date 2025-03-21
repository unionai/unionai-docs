---
title: flytekit.models.project
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.project

## Directory

### Classes

| Class | Description |
|-|-|
| [`Project`](.././flytekit.models.project#flytekitmodelsprojectproject) | None. |

## flytekit.models.project.Project

```python
def Project(
    id,
    name,
    description,
    state,
):
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
| [`active_project()`](#active_project) | None |
| [`archived_project()`](#archived_project) | None |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### active_project()

```python
def active_project(
    id,
):
```
| Parameter | Type |
|-|-|
| `id` |  |

#### archived_project()

```python
def archived_project(
    id,
):
```
| Parameter | Type |
|-|-|
| `id` |  |

#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
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
| description |  |  |
| id |  |  |
| is_empty |  |  |
| name |  |  |
| state |  |  |

