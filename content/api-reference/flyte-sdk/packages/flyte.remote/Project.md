---
title: Project
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Project

**Package:** `flyte.remote`

A class representing a project in the Union API.


```python
class Project(
    pb2: project_pb2.Project,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `project_pb2.Project` | |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a run by its ID or name. |
| [`listall()`](#listall) | Get a run by its ID or name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Project.get.aio()`.
```python
def get(
    cls,
    name: str,
    org: str | None,
) -> Project
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the project. |
| `org` | `str \| None` | The organization of the project (if applicable). |

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
) -> Union[AsyncIterator[Project], Iterator[Project]]
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `filters` | `str \| None` | The filters to apply to the project list. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). :return: An iterator of projects. |

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


