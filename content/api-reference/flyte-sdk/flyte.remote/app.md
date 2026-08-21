---
title: App
version: 2.6.5
variants: +flyte +union
layout: py_api
---

# App

**Package:** `flyte.remote`

## Parameters

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
| `deployment_status` | `app_definition_pb2.Status.DeploymentStatus` | Get the deployment status of the app |
| `desired_state` | `app_definition_pb2.Spec.DesiredState` | Get the desired state of the app. |
| `endpoint` | `str` | Get the public endpoint URL of the app. |
| `name` | `str` | Get the name of the app. |
| `revision` | `int` | Get the revision number of the app. |
| `url` | `str` | Get the console URL for viewing the app. |

## Methods

| Method | Description |
|-|-|
| [`activate()`](#activate) | Start the app. |
| [`create()`](#create) |  |
| [`deactivate()`](#deactivate) | Stop the app. |
| [`delete()`](#delete) | Delete an app by name. |
| [`ephemeral_ctx()`](#ephemeral_ctx) | Async context manager that activates the app and deactivates it when the context is exited. |
| [`ephemeral_ctx_sync()`](#ephemeral_ctx_sync) | Context manager that activates the app and deactivates it when the context is exited. |
| [`get()`](#get) | Get an app by name. |
| [`is_active()`](#is_active) | Check if the app is currently active or started. |
| [`is_deactivated()`](#is_deactivated) | Check if the app is currently deactivated or stopped. |
| [`listall()`](#listall) | List all apps, optionally filtered. |
| [`replace()`](#replace) | Replace an existing app's that matches the given name, with a new spec and optionally labels. |
| [`show_logs()`](#show_logs) | Display logs for the app, streaming until interrupted or the stream ends. |
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
    wait: bool = False,
) -> App
```
Start the app



| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | Wait for the app to reach activated state |

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
    wait: bool = False,
) -> App
```
Stop the app



| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | Wait for the app to reach the deactivated state |

### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.delete.aio()`.
```python
def delete(
    cls,
    name: str,
    project: str | None = None,
    domain: str | None = None,
)
```
Delete an app by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the app to delete. |
| `project` | `str \| None` | The name of the project to delete. |
| `domain` | `str \| None` | The name of the domain to delete. |

### ephemeral_ctx()

```python
def ephemeral_ctx()
```
Async context manager that activates the app and deactivates it when the context is exited.


### ephemeral_ctx_sync()

```python
def ephemeral_ctx_sync()
```
Context manager that activates the app and deactivates it when the context is exited.


### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await App.get.aio()`.
```python
def get(
    cls,
    name: str,
    project: str | None = None,
    domain: str | None = None,
) -> App
```
Get an app by name.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | The name of the app. |
| `project` | `str \| None` | The project of the app. |
| `domain` | `str \| None` | The domain of the app. |

**Returns:** The app remote object.

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
    created_by_subject: str | None = None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None = None,
    limit: int = 100,
    in_status: str | Tuple[str, ...] | None = None,
) -> AsyncIterator[App]
```
List all apps, optionally filtered.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `created_by_subject` | `str \| None` | Only return apps created by this subject. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | Sorting criteria, in the format (field, order). |
| `limit` | `int` | Maximum number of apps to return. |
| `in_status` | `str \| Tuple[str, ...] \| None` | Filter apps by one or more deployment statuses, e.g. "active" or ("active", "failed"). Accepts short names (case-insensitive) or full DEPLOYMENT_STATUS_* names. |

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
    labels: Mapping[str, str] | None = None,
    project: str | None = None,
    domain: str | None = None,
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
| `domain` | `str \| None` | Optional domain for the new app |

**Returns:** A new app

### show_logs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <App instance>.show_logs.aio()`.
```python
def show_logs(
    max_lines: int = 30,
    show_ts: bool = False,
    raw: bool = False,
    filter_system: bool = False,
    replica_name: str | None = None,
)
```
Display logs for the app, streaming until interrupted or the stream ends.



| Parameter | Type | Description |
|-|-|-|
| `max_lines` | `int` | Maximum number of lines to keep in view when using the live viewer. |
| `show_ts` | `bool` | Whether to show timestamps in the logs. |
| `raw` | `bool` | If True, print raw log lines instead of using the live viewer. |
| `filter_system` | `bool` | Whether to filter out system log lines. |
| `replica_name` | `str \| None` | Optional replica name to restrict the stream to. |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

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
    wait_for: WaitFor = 'activated',
) -> App
```
Watch for the app to reach activated or deactivated state.

Returns: The app in the desired state.
Raises: RuntimeError if the app did not reach desired state and failed!


| Parameter | Type | Description |
|-|-|-|
| `wait_for` | `WaitFor` | ["activated", "deactivated"] |

