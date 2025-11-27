---
title: App
version: 2.0.0b32.dev0+g54ab96db3.d20251127
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# App

**Package:** `flyte.remote`

A mixin class that provides a method to convert an object to a JSON-serializable dictionary.


```python
class App(
    pb2: app_definition_pb2.App,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `app_definition_pb2.App` | |

## Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get an app by name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### get()

```python
def get(
    name: str,
    project: str | None,
    domain: str | None,
) -> App
```
Get an app by name.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the app. |
| `project` | `str \| None` | The project of the app. |
| `domain` | `str \| None` | The domain of the app. :return: The app remote object. |

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


## Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |
| `name` | `None` |  |
| `revision` | `None` |  |

