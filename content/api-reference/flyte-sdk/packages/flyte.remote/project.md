---
title: Project
version: 2.0.5
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Project

**Package:** `flyte.remote`

A class representing a project in the Union API.



```python
class Project(
    pb2: project_service_pb2.Project,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `project_service_pb2.Project` | |

## Methods

| Method | Description |
|-|-|
| [`archive()`](#archive) | Archive this project. |
| [`create()`](#create) | Create a new project. |
| [`get()`](#get) | Get a project by name. |
| [`listall()`](#listall) | List all projects. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`unarchive()`](#unarchive) | Unarchive (activate) this project. |
| [`update()`](#update) | Update an existing project. |


### archive()

```python
def archive()
```
Archive this project.


### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Project.create.aio()`.
```python
def create(
    cls,
    id: str,
    name: str,
    description: str,
    labels: Dict[str, str] | None,
) -> Project
```
Create a new project.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `id` | `str` | The unique identifier for the project. |
| `name` | `str` | The display name for the project. |
| `description` | `str` | A description for the project. |
| `labels` | `Dict[str, str] \| None` | Optional key-value labels for the project. |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Project.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Project
```
Get a project by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the project. |

### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Project.listall.aio()`.
```python
def listall(
    cls,
    filters: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    archived: bool,
) -> Union[AsyncIterator[Project], Iterator[Project]]
```
List all projects.

By default, lists active (unarchived) projects. Set ``archived=True`` to list
archived projects instead.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `filters` | `str \| None` | The filters to apply to the project list. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). |
| `archived` | `bool` | If True, list archived projects. If False (default), list active projects. :return: An iterator of projects. |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### unarchive()

```python
def unarchive()
```
Unarchive (activate) this project.


### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Project.update.aio()`.
```python
def update(
    cls,
    id: str,
    name: str | None,
    description: str | None,
    labels: Dict[str, str] | None,
    state: Literal['archived', 'active'] | None,
) -> Project
```
Update an existing project.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `id` | `str` | The id of the project to update. |
| `name` | `str \| None` | New display name. If None, the existing name is preserved. |
| `description` | `str \| None` | New description. If None, the existing description is preserved. |
| `labels` | `Dict[str, str] \| None` | New labels. If None, the existing labels are preserved. |
| `state` | `Literal['archived', 'active'] \| None` | "archived" or "active". If None, the existing state is preserved. |

