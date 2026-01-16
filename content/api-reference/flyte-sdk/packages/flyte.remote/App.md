---
title: App
version: 2.0.0b48
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

## Properties

| Property | Type | Description |
|-|-|-|
| `deployment_status` | `None` | Get the deployment status of the app Returns: |
| `desired_state` | `None` | Get the desired state of the app. |
| `endpoint` | `None` | Get the public endpoint URL of the app. |
| `name` | `None` | Get the name of the app. |
| `revision` | `None` | Get the revision number of the app. |
| `url` | `None` | Get the console URL for viewing the app. |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) | Start the app. |
| [`create()`](#create) |  |
| [`deactivate()`](#deactivate) | Stop the app. |
| [`get()`](#get) | Get an app by name. |
| [`is_active()`](#is_active) | Check if the app is currently active or started. |
| [`is_deactivated()`](#is_deactivated) | Check if the app is currently deactivated or stopped. |
| [`listall()`](#listall) |  |
| [`replace()`](#replace) | Replace an existing app's that matches the given name, with a new spec and optionally labels. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) |  |
| [`watch()`](#watch) | Watch for the app to reach activated or deactivated state. |


### activate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <App instance>.activate.aio()`.
```python
def activate(
    wait: bool,
) -> App
```
Start the app


| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | Wait for the app to reach started state |

### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.create.aio()`.
```python
def create(
    cls,
    app: app_definition_pb2.App,
) -> App
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `app` | `app_definition_pb2.App` | |

### deactivate()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <App instance>.deactivate.aio()`.
```python
def deactivate(
    wait: bool,
)
```
Stop the app


| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | Wait for the app to reach the deactivated state |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.get.aio()`.
```python
def get(
    cls,
    name: str,
    project: str | None,
    domain: str | None,
) -> App
```
Get an app by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the app. |
| `project` | `str \| None` | The project of the app. |
| `domain` | `str \| None` | The domain of the app. :return: The app remote object. |

### is_active()

```python
def is_active()
```
Check if the app is currently active or started.


### is_deactivated()

```python
def is_deactivated()
```
Check if the app is currently deactivated or stopped.


### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.listall.aio()`.
```python
def listall(
    cls,
    created_by_subject: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    limit: int,
) -> AsyncIterator[App]
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `created_by_subject` | `str \| None` | |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | |
| `limit` | `int` | |

### replace()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.replace.aio()`.
```python
def replace(
    cls,
    name: str,
    updated_app_spec: app_definition_pb2.Spec,
    reason: str,
    labels: Mapping[str, str] | None,
    project: str | None,
    domain: str | None,
) -> App
```
Replace an existing app's that matches the given name, with a new spec and optionally labels.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | Name of the new app |
| `updated_app_spec` | `app_definition_pb2.Spec` | Updated app spec |
| `reason` | `str` | |
| `labels` | `Mapping[str, str] \| None` | Optional labels for the new app |
| `project` | `str \| None` | Optional project for the new app |
| `domain` | `str \| None` | Optional domain for the new app :return: A new app |

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


### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.update.aio()`.
```python
def update(
    cls,
    updated_app_proto: app_definition_pb2.App,
    reason: str,
) -> App
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `updated_app_proto` | `app_definition_pb2.App` | |
| `reason` | `str` | |

### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <App instance>.watch.aio()`.
```python
def watch(
    wait_for: WaitFor,
) -> App
```
Watch for the app to reach activated or deactivated state.


| Parameter | Type | Description |
|-|-|-|
| `wait_for` | `WaitFor` | ["activated", "deactivated"]  Returns: The app in the desired state. Raises: RuntimeError if the app did not reach desired state and failed! |

