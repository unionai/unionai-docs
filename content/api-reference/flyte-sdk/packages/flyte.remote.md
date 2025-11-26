---
title: flyte.remote
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.remote


Remote Entities that are accessible from the Union Server once deployed or created.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Action`](.././flyte.remote#flyteremoteaction) | A class representing an action. |
| [`ActionDetails`](.././flyte.remote#flyteremoteactiondetails) | A class representing an action. |
| [`ActionInputs`](.././flyte.remote#flyteremoteactioninputs) | A class representing the inputs of an action. |
| [`ActionOutputs`](.././flyte.remote#flyteremoteactionoutputs) | A class representing the outputs of an action. |
| [`App`](.././flyte.remote#flyteremoteapp) | A mixin class that provides a method to convert an object to a JSON-serializable dictionary. |
| [`Project`](.././flyte.remote#flyteremoteproject) | A class representing a project in the Union API. |
| [`Run`](.././flyte.remote#flyteremoterun) | A class representing a run of a task. |
| [`RunDetails`](.././flyte.remote#flyteremoterundetails) | A class representing a run of a task. |
| [`Secret`](.././flyte.remote#flyteremotesecret) |  |
| [`Task`](.././flyte.remote#flyteremotetask) |  |
| [`TaskDetails`](.././flyte.remote#flyteremotetaskdetails) |  |
| [`Trigger`](.././flyte.remote#flyteremotetrigger) |  |
| [`User`](.././flyte.remote#flyteremoteuser) |  |

### Methods

| Method | Description |
|-|-|
| [`create_channel()`](#create_channel) | Creates a new gRPC channel with appropriate authentication interceptors. |
| [`upload_dir()`](#upload_dir) | Uploads a directory to a remote location and returns the remote URI. |
| [`upload_file()`](#upload_file) | Uploads a file to a remote location and returns the remote URI. |


## Methods

#### create_channel()

```python
def create_channel(
    endpoint: str | None,
    api_key: str | None,
    insecure: typing.Optional[bool],
    insecure_skip_verify: typing.Optional[bool],
    ca_cert_file_path: typing.Optional[str],
    ssl_credentials: typing.Optional[ssl_channel_credentials],
    grpc_options: typing.Optional[typing.Sequence[typing.Tuple[str, typing.Any]]],
    compression: typing.Optional[grpc.Compression],
    http_session: httpx.AsyncClient | None,
    proxy_command: typing.Optional[typing.List[str]],
    kwargs,
) -> grpc.aio._base_channel.Channel
```
Creates a new gRPC channel with appropriate authentication interceptors.

This function creates either a secure or insecure gRPC channel based on the provided parameters,
and adds authentication interceptors to the channel. If SSL credentials are not provided,
they are created based on the insecure_skip_verify and ca_cert_file_path parameters.

The function is async because it may need to read certificate files asynchronously
and create authentication interceptors that perform async operations.



| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str \| None` | The endpoint URL for the gRPC channel |
| `api_key` | `str \| None` | API key for authentication; if provided, it will be used to detect the endpoint and credentials. |
| `insecure` | `typing.Optional[bool]` | Whether to use an insecure channel (no SSL) |
| `insecure_skip_verify` | `typing.Optional[bool]` | Whether to skip SSL certificate verification |
| `ca_cert_file_path` | `typing.Optional[str]` | Path to CA certificate file for SSL verification |
| `ssl_credentials` | `typing.Optional[ssl_channel_credentials]` | Pre-configured SSL credentials for the channel |
| `grpc_options` | `typing.Optional[typing.Sequence[typing.Tuple[str, typing.Any]]]` | Additional gRPC channel options |
| `compression` | `typing.Optional[grpc.Compression]` | Compression method for the channel |
| `http_session` | `httpx.AsyncClient \| None` | Pre-configured HTTP session to use for requests |
| `proxy_command` | `typing.Optional[typing.List[str]]` | List of strings for proxy command configuration |
| `kwargs` | `**kwargs` | Additional arguments passed to various functions - For grpc.aio.insecure_channel/secure_channel: - root_certificates: Root certificates for SSL credentials - private_key: Private key for SSL credentials - certificate_chain: Certificate chain for SSL credentials - options: gRPC channel options - compression: gRPC compression method - For proxy configuration: - proxy_env: Dict of environment variables for proxy - proxy_timeout: Timeout for proxy connection - For authentication interceptors (passed to create_auth_interceptors and create_proxy_auth_interceptors): - auth_type: The authentication type to use ("Pkce", "ClientSecret", "ExternalCommand", "DeviceFlow") - command: Command to execute for ExternalCommand authentication - client_id: Client ID for ClientSecret authentication - client_secret: Client secret for ClientSecret authentication - client_credentials_secret: Client secret for ClientSecret authentication (alias) - scopes: List of scopes to request during authentication - audience: Audience for the token - http_proxy_url: HTTP proxy URL - verify: Whether to verify SSL certificates - ca_cert_path: Optional path to CA certificate file - header_key: Header key to use for authentication - redirect_uri: OAuth2 redirect URI for PKCE authentication - add_request_auth_code_params_to_request_access_token_params: Whether to add auth code params to token request - request_auth_code_params: Parameters to add to login URI opened in browser - request_access_token_params: Parameters to add when exchanging auth code for access token - refresh_access_token_params: Parameters to add when refreshing access token :return: grpc.aio.Channel with authentication interceptors configured |

#### upload_dir()

```python
def upload_dir(
    dir_path: pathlib._local.Path,
    verify: bool,
) -> str
```
Uploads a directory to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `dir_path` | `pathlib._local.Path` | The directory path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. :return: The remote URI of the uploaded directory. |

#### upload_file()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await upload_file.aio()`.
```python
def upload_file(
    fp: pathlib._local.Path,
    verify: bool,
) -> typing.Tuple[str, str]
```
Uploads a file to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `fp` | `pathlib._local.Path` | The file path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. :return: A tuple containing the MD5 digest and the remote URI. |

## flyte.remote.Action

A class representing an action. It is used to manage the run of a task and its state on the remote Union API.


```python
class Action(
    pb2: run_definition_pb2.Action,
    _details: ActionDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Action` | |
| `_details` | `ActionDetails \| None` | |

### Methods

| Method | Description |
|-|-|
| [`details()`](#details) | Get the details of the action. |
| [`done()`](#done) | Check if the action is done. |
| [`get()`](#get) | Get a run by its ID or name. |
| [`listall()`](#listall) | Get all actions for a given run. |
| [`show_logs()`](#show_logs) |  |
| [`sync()`](#sync) | Sync the action with the remote server. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`wait()`](#wait) | Wait for the run to complete, displaying a rich progress panel with status transitions,. |
| [`watch()`](#watch) | Watch the action for updates. |


#### details()

```python
def details()
```
Get the details of the action. This is a placeholder for getting the action details.


#### done()

```python
def done()
```
Check if the action is done.


#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Action.get.aio()`.
```python
def get(
    cls,
    uri: str | None,
    run_name: str | None,
    name: str | None,
) -> Action
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `uri` | `str \| None` | The URI of the action. |
| `run_name` | `str \| None` | The name of the action. |
| `name` | `str \| None` | The name of the action. |

#### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Action.listall.aio()`.
```python
def listall(
    cls,
    for_run_name: str,
    filters: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
) -> Union[Iterator[Action], AsyncIterator[Action]]
```
Get all actions for a given run.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `for_run_name` | `str` | The name of the run. |
| `filters` | `str \| None` | The filters to apply to the project list. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). :return: An iterator of projects. |

#### show_logs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Action instance>.show_logs.aio()`.
```python
def show_logs(
    attempt: int | None,
    max_lines: int,
    show_ts: bool,
    raw: bool,
    filter_system: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | |
| `max_lines` | `int` | |
| `show_ts` | `bool` | |
| `raw` | `bool` | |
| `filter_system` | `bool` | |

#### sync()

```python
def sync()
```
Sync the action with the remote server. This is a placeholder for syncing the action.


#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


#### wait()

```python
def wait(
    quiet: bool,
    wait_for: WaitFor,
)
```
Wait for the run to complete, displaying a rich progress panel with status transitions,
time elapsed, and error details in case of failure.


| Parameter | Type | Description |
|-|-|-|
| `quiet` | `bool` | |
| `wait_for` | `WaitFor` | |

#### watch()

```python
def watch(
    cache_data_on_done: bool,
    wait_for: WaitFor,
) -> AsyncGenerator[ActionDetails, None]
```
Watch the action for updates. This is a placeholder for watching the action.


| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |
| `wait_for` | `WaitFor` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `None` | Get the action ID. |
| `name` | `None` | Get the name of the action. |
| `phase` | `None` | Get the phase of the action. |
| `raw_phase` | `None` | Get the raw phase of the action. |
| `run_name` | `None` | Get the name of the run. |
| `task_name` | `None` | Get the name of the task. |

## flyte.remote.ActionDetails

A class representing an action. It is used to manage the run of a task and its state on the remote Union API.


```python
class ActionDetails(
    pb2: run_definition_pb2.ActionDetails,
    _inputs: ActionInputs | None,
    _outputs: ActionOutputs | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.ActionDetails` | |
| `_inputs` | `ActionInputs \| None` | |
| `_outputs` | `ActionOutputs \| None` | |

### Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the action is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the action. |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`logs_available()`](#logs_available) | Check if logs are available for the action, optionally for a specific attempt. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch()`](#watch) | Watch the action for updates. |
| [`watch_updates()`](#watch_updates) |  |


#### done()

```python
def done()
```
Check if the action is in a terminal state (completed or failed). This is a placeholder for checking the
action state.


#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.get.aio()`.
```python
def get(
    cls,
    uri: str | None,
    run_name: str | None,
    name: str | None,
) -> ActionDetails
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `uri` | `str \| None` | The URI of the action. |
| `run_name` | `str \| None` | The name of the run. |
| `name` | `str \| None` | The name of the action. |

#### get_details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.get_details.aio()`.
```python
def get_details(
    cls,
    action_id: identifier_pb2.ActionIdentifier,
) -> ActionDetails
```
Get the details of the action. This is a placeholder for getting the action details.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `action_id` | `identifier_pb2.ActionIdentifier` | |

#### inputs()

```python
def inputs()
```
Placeholder for inputs. This can be extended to handle inputs from the run context.


#### logs_available()

```python
def logs_available(
    attempt: int | None,
) -> bool
```
Check if logs are available for the action, optionally for a specific attempt.
If attempt is None, it checks for the latest attempt.


| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | |

#### outputs()

```python
def outputs()
```
Placeholder for outputs. This can be extended to handle outputs from the run context.


#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


#### watch()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ActionDetails.watch.aio()`.
```python
def watch(
    cls,
    action_id: identifier_pb2.ActionIdentifier,
) -> AsyncIterator[ActionDetails]
```
Watch the action for updates. This is a placeholder for watching the action.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `action_id` | `identifier_pb2.ActionIdentifier` | |

#### watch_updates()

```python
def watch_updates(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `abort_info` | `None` |  |
| `action_id` | `None` | Get the action ID. |
| `attempts` | `None` | Get the number of attempts of the action. |
| `error_info` | `None` |  |
| `is_running` | `None` | Check if the action is currently running. |
| `metadata` | `None` |  |
| `name` | `None` | Get the name of the action. |
| `phase` | `None` | Get the phase of the action. |
| `raw_phase` | `None` | Get the raw phase of the action. |
| `run_name` | `None` | Get the name of the run. |
| `runtime` | `None` | Get the runtime of the action. |
| `status` | `None` |  |
| `task_name` | `None` | Get the name of the task. |

## flyte.remote.ActionInputs

A class representing the inputs of an action. It is used to manage the inputs of a task and its state on the
remote Union API.


```python
class ActionInputs(
    pb2: common_pb2.Inputs,
    data: Dict[str, Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Inputs` | |
| `data` | `Dict[str, Any]` | |

### Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) | D. |
| [`copy()`](#copy) |  |
| [`fromkeys()`](#fromkeys) |  |
| [`get()`](#get) | D. |
| [`items()`](#items) | D. |
| [`keys()`](#keys) | D. |
| [`pop()`](#pop) | D. |
| [`popitem()`](#popitem) | D. |
| [`setdefault()`](#setdefault) | D. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | D. |
| [`values()`](#values) | D. |


#### clear()

```python
def clear()
```
D.clear() -&gt; None.  Remove all items from D.


#### copy()

```python
def copy()
```
#### fromkeys()

```python
def fromkeys(
    iterable,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `iterable` |  | |
| `value` |  | |

#### get()

```python
def get(
    key,
    default,
)
```
D.get(k[,d]) -&gt; D[k] if k in D, else d.  d defaults to None.


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

#### items()

```python
def items()
```
D.items() -&gt; a set-like object providing a view on D's items


#### keys()

```python
def keys()
```
D.keys() -&gt; a set-like object providing a view on D's keys


#### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -&gt; v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

#### popitem()

```python
def popitem()
```
D.popitem() -&gt; (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


#### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -&gt; D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


#### update()

```python
def update(
    other,
    kwds,
)
```
D.update([E, ]**F) -&gt; None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E.keys(): D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type | Description |
|-|-|-|
| `other` |  | |
| `kwds` |  | |

#### values()

```python
def values()
```
D.values() -&gt; an object providing a view on D's values


## flyte.remote.ActionOutputs

A class representing the outputs of an action. It is used to manage the outputs of a task and its state on the
remote Union API.


```python
class ActionOutputs(
    pb2: common_pb2.Outputs,
    data: Tuple[Any, ...],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Outputs` | |
| `data` | `Tuple[Any, ...]` | |

### Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


## flyte.remote.App

A mixin class that provides a method to convert an object to a JSON-serializable dictionary.


```python
class App(
    pb2: app_definition_pb2.App,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `app_definition_pb2.App` | |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get an app by name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### get()

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

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` |  |
| `name` | `None` |  |
| `revision` | `None` |  |

## flyte.remote.Project

A class representing a project in the Union API.


```python
class Project(
    pb2: project_pb2.Project,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `project_pb2.Project` | |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a run by its ID or name. |
| [`listall()`](#listall) | Get a run by its ID or name. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### get()


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

#### listall()


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

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


## flyte.remote.Run

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class Run(
    pb2: run_definition_pb2.Run,
    _details: RunDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.Run` | |
| `_details` | `RunDetails \| None` | |

### Methods

| Method | Description |
|-|-|
| [`abort()`](#abort) | Aborts / Terminates the run. |
| [`details()`](#details) | Get the details of the run. |
| [`done()`](#done) | Check if the run is done. |
| [`get()`](#get) | Get the current run. |
| [`inputs()`](#inputs) | Get the inputs of the run. |
| [`listall()`](#listall) | Get all runs for the current project and domain. |
| [`outputs()`](#outputs) | Get the outputs of the run. |
| [`show_logs()`](#show_logs) |  |
| [`sync()`](#sync) | Sync the run with the remote server. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`wait()`](#wait) | Wait for the run to complete, displaying a rich progress panel with status transitions,. |
| [`watch()`](#watch) | Get the details of the run. |


#### abort()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.abort.aio()`.
```python
def abort()
```
Aborts / Terminates the run.


#### details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.details.aio()`.
```python
def details()
```
Get the details of the run. This is a placeholder for getting the run details.


#### done()

```python
def done()
```
Check if the run is done.


#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Run.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Run
```
Get the current run.

:return: The current run.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

#### inputs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.inputs.aio()`.
```python
def inputs()
```
Get the inputs of the run. This is a placeholder for getting the run inputs.


#### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Run.listall.aio()`.
```python
def listall(
    cls,
    in_phase: Tuple[Phase] | None,
    created_by_subject: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    limit: int,
) -> AsyncIterator[Run]
```
Get all runs for the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `in_phase` | `Tuple[Phase] \| None` | Filter runs by one or more phases. |
| `created_by_subject` | `str \| None` | Filter runs by the subject that created them. (this is not username, but the subject) |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). |
| `limit` | `int` | The maximum number of runs to return. :return: An iterator of runs. |

#### outputs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.outputs.aio()`.
```python
def outputs()
```
Get the outputs of the run. This is a placeholder for getting the run outputs.


#### show_logs()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.show_logs.aio()`.
```python
def show_logs(
    attempt: int | None,
    max_lines: int,
    show_ts: bool,
    raw: bool,
    filter_system: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `attempt` | `int \| None` | |
| `max_lines` | `int` | |
| `show_ts` | `bool` | |
| `raw` | `bool` | |
| `filter_system` | `bool` | |

#### sync()

```python
def sync()
```
Sync the run with the remote server. This is a placeholder for syncing the run.


#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


#### wait()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await <Run instance>.wait.aio()`.
```python
def wait(
    quiet: bool,
    wait_for: Literal['terminal', 'running'],
)
```
Wait for the run to complete, displaying a rich progress panel with status transitions,
time elapsed, and error details in case of failure.


| Parameter | Type | Description |
|-|-|-|
| `quiet` | `bool` | |
| `wait_for` | `Literal['terminal', 'running']` | |

#### watch()

```python
def watch(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
Get the details of the run. This is a placeholder for getting the run details.


| Parameter | Type | Description |
|-|-|-|
| `cache_data_on_done` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | Get the name of the run. |
| `phase` | `None` | Get the phase of the run. |
| `raw_phase` | `None` | Get the raw phase of the run. |
| `url` | `None` | Get the URL of the run. |

## flyte.remote.RunDetails

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class RunDetails(
    pb2: run_definition_pb2.RunDetails,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `run_definition_pb2.RunDetails` | |

### Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the run is in a terminal state (completed or failed). |
| [`get()`](#get) | Get a run by its ID or name. |
| [`get_details()`](#get_details) | Get the details of the run. |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### done()

```python
def done()
```
Check if the run is in a terminal state (completed or failed). This is a placeholder for checking the
run state.


#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await RunDetails.get.aio()`.
```python
def get(
    cls,
    name: str | None,
) -> RunDetails
```
Get a run by its ID or name. If both are provided, the ID will take precedence.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str \| None` | The name of the run. |

#### get_details()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await RunDetails.get_details.aio()`.
```python
def get_details(
    cls,
    run_id: identifier_pb2.RunIdentifier,
) -> RunDetails
```
Get the details of the run. This is a placeholder for getting the run details.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `run_id` | `identifier_pb2.RunIdentifier` | |

#### inputs()

```python
def inputs()
```
Placeholder for inputs. This can be extended to handle inputs from the run context.


#### outputs()

```python
def outputs()
```
Placeholder for outputs. This can be extended to handle outputs from the run context.


#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `None` | Get the action ID. |
| `name` | `None` | Get the name of the action. |
| `task_name` | `None` | Get the name of the task. |

## flyte.remote.Secret

```python
class Secret(
    pb2: definition_pb2.Secret,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `definition_pb2.Secret` | |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) |  |
| [`delete()`](#delete) |  |
| [`get()`](#get) |  |
| [`listall()`](#listall) |  |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.create.aio()`.
```python
def create(
    cls,
    name: str,
    value: Union[str, bytes],
    type: SecretTypes,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `value` | `Union[str, bytes]` | |
| `type` | `SecretTypes` | |

#### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.delete.aio()`.
```python
def delete(
    cls,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` |  | |

#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.get.aio()`.
```python
def get(
    cls,
    name: str,
) -> Secret
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |

#### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Secret.listall.aio()`.
```python
def listall(
    cls,
    limit: int,
) -> AsyncIterator[Secret]
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `limit` | `int` | |

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `type` | `None` |  |

## flyte.remote.Task

```python
class Task(
    pb2: task_definition_pb2.Task,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `task_definition_pb2.Task` | |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a task by its ID or name. |
| [`listall()`](#listall) | Get all runs for the current project and domain. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### get()

```python
def get(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> LazyEntity
```
Get a task by its ID or name. If both are provided, the ID will take precedence.

Either version or auto_version are required parameters.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the task. |
| `project` | `str \| None` | The project of the task. |
| `domain` | `str \| None` | The domain of the task. |
| `version` | `str \| None` | The version of the task. |
| `auto_version` | `AutoVersioning \| None` | If set to "latest", the latest-by-time ordered from now, version of the task will be used. If set to "current", the version will be derived from the callee tasks context. This is useful if you are deploying all environments with the same version. If auto_version is current, you can only access the task from within a task context. |

#### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Task.listall.aio()`.
```python
def listall(
    cls,
    by_task_name: str | None,
    by_task_env: str | None,
    project: str | None,
    domain: str | None,
    sort_by: Tuple[str, Literal['asc', 'desc']] | None,
    limit: int,
) -> Union[AsyncIterator[Task], Iterator[Task]]
```
Get all runs for the current project and domain.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `by_task_name` | `str \| None` | If provided, only tasks with this name will be returned. |
| `by_task_env` | `str \| None` | If provided, only tasks with this environment prefix will be returned. |
| `project` | `str \| None` | The project to filter tasks by. If None, the current project will be used. |
| `domain` | `str \| None` | The domain to filter tasks by. If None, the current domain will be used. |
| `sort_by` | `Tuple[str, Literal['asc', 'desc']] \| None` | The sorting criteria for the project list, in the format (field, order). |
| `limit` | `int` | The maximum number of tasks to return. :return: An iterator of runs. |

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | The name of the task. |
| `version` | `None` | The version of the task. |

## flyte.remote.TaskDetails

```python
class TaskDetails(
    pb2: task_definition_pb2.TaskDetails,
    max_inline_io_bytes: int,
    overriden_queue: Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `task_definition_pb2.TaskDetails` | |
| `max_inline_io_bytes` | `int` | |
| `overriden_queue` | `Optional[str]` | |

### Methods

| Method | Description |
|-|-|
| [`fetch()`](#fetch) |  |
| [`get()`](#get) | Get a task by its ID or name. |
| [`override()`](#override) |  |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### fetch()

```python
def fetch(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> TaskDetails
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `version` | `str \| None` | |
| `auto_version` | `AutoVersioning \| None` | |

#### get()

```python
def get(
    name: str,
    project: str | None,
    domain: str | None,
    version: str | None,
    auto_version: AutoVersioning | None,
) -> LazyEntity
```
Get a task by its ID or name. If both are provided, the ID will take precedence.

Either version or auto_version are required parameters.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the task. |
| `project` | `str \| None` | The project of the task. |
| `domain` | `str \| None` | The domain of the task. |
| `version` | `str \| None` | The version of the task. |
| `auto_version` | `AutoVersioning \| None` | If set to "latest", the latest-by-time ordered from now, version of the task will be used. If set to "current", the version will be derived from the callee tasks context. This is useful if you are deploying all environments with the same version. If auto_version is current, you can only access the task from within a task context. |

#### override()

```python
def override(
    short_name: Optional[str],
    resources: Optional[flyte.Resources],
    retries: Union[int, flyte.RetryStrategy],
    timeout: Optional[flyte.TimeoutType],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[flyte.SecretRequest],
    max_inline_io_bytes: Optional[int],
    cache: Optional[flyte.Cache],
    queue: Optional[str],
    kwargs: **kwargs,
) -> TaskDetails
```
| Parameter | Type | Description |
|-|-|-|
| `short_name` | `Optional[str]` | |
| `resources` | `Optional[flyte.Resources]` | |
| `retries` | `Union[int, flyte.RetryStrategy]` | |
| `timeout` | `Optional[flyte.TimeoutType]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[flyte.SecretRequest]` | |
| `max_inline_io_bytes` | `Optional[int]` | |
| `cache` | `Optional[flyte.Cache]` | |
| `queue` | `Optional[str]` | |
| `kwargs` | `**kwargs` | |

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### Properties

| Property | Type | Description |
|-|-|-|
| `cache` | `None` | The cache policy of the task. |
| `default_input_args` | `None` | The default input arguments of the task. |
| `name` | `None` | The name of the task. |
| `queue` | `None` | The queue to use for the task. |
| `required_args` | `None` | The required input arguments of the task. |
| `resources` | `None` | The resources of the task. |
| `secrets` | `None` | The secrets of the task. |
| `task_type` | `None` | The type of the task. |
| `version` | `None` | The version of the task. |

## flyte.remote.Trigger

```python
class Trigger(
    pb2: trigger_definition_pb2.Trigger,
    details: TriggerDetails | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `trigger_definition_pb2.Trigger` | |
| `details` | `TriggerDetails \| None` | |

### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Create a new trigger in the Flyte platform. |
| [`delete()`](#delete) | Delete a trigger by its name. |
| [`get()`](#get) | Retrieve a trigger by its name and associated task name. |
| [`get_details()`](#get_details) | Get detailed information about this trigger. |
| [`listall()`](#listall) | List all triggers associated with a specific task or all tasks if no task name is provided. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | Pause a trigger by its name and associated task name. |


#### create()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.create.aio()`.
```python
def create(
    cls,
    trigger: flyte.Trigger,
    task_name: str,
    task_version: str | None,
) -> Trigger
```
Create a new trigger in the Flyte platform.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `trigger` | `flyte.Trigger` | The flyte.Trigger object containing the trigger definition. |
| `task_name` | `str` | Optional name of the task to associate with the trigger. |
| `task_version` | `str \| None` | |

#### delete()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.delete.aio()`.
```python
def delete(
    cls,
    name: str,
    task_name: str,
)
```
Delete a trigger by its name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |

#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.get.aio()`.
```python
def get(
    cls,
    name: str,
    task_name: str,
) -> TriggerDetails
```
Retrieve a trigger by its name and associated task name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |

#### get_details()

```python
def get_details()
```
Get detailed information about this trigger.


#### listall()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.listall.aio()`.
```python
def listall(
    cls,
    task_name: str | None,
    task_version: str | None,
    limit: int,
) -> AsyncIterator[Trigger]
```
List all triggers associated with a specific task or all tasks if no task name is provided.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `task_name` | `str \| None` | |
| `task_version` | `str \| None` | |
| `limit` | `int` | |

#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


#### update()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await Trigger.update.aio()`.
```python
def update(
    cls,
    name: str,
    task_name: str,
    active: bool,
)
```
Pause a trigger by its name and associated task name.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `name` | `str` | |
| `task_name` | `str` | |
| `active` | `bool` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `automation_spec` | `None` |  |
| `id` | `None` |  |
| `is_active` | `None` |  |
| `name` | `None` |  |
| `task_name` | `None` |  |

## flyte.remote.User

```python
class User(
    pb2: UserInfoResponse,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `UserInfoResponse` | |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Fetches information about the currently logged in user. |
| [`name()`](#name) |  |
| [`subject()`](#subject) |  |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await User.get.aio()`.
```python
def get(
    cls,
) -> User
```
Fetches information about the currently logged in user.
Returns: A User object containing details about the user.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

#### name()

```python
def name()
```
#### subject()

```python
def subject()
```
#### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


#### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


