---
title: flyte.remote
version: 2.0.0b25
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
| [`Project`](.././flyte.remote#flyteremoteproject) | A class representing a project in the Union API. |
| [`Run`](.././flyte.remote#flyteremoterun) | A class representing a run of a task. |
| [`RunDetails`](.././flyte.remote#flyteremoterundetails) | A class representing a run of a task. |
| [`Secret`](.././flyte.remote#flyteremotesecret) |  |
| [`Task`](.././flyte.remote#flyteremotetask) |  |
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



| Parameter | Type |
|-|-|
| `endpoint` | `str \| None` |
| `api_key` | `str \| None` |
| `insecure` | `typing.Optional[bool]` |
| `insecure_skip_verify` | `typing.Optional[bool]` |
| `ca_cert_file_path` | `typing.Optional[str]` |
| `ssl_credentials` | `typing.Optional[ssl_channel_credentials]` |
| `grpc_options` | `typing.Optional[typing.Sequence[typing.Tuple[str, typing.Any]]]` |
| `compression` | `typing.Optional[grpc.Compression]` |
| `http_session` | `httpx.AsyncClient \| None` |
| `proxy_command` | `typing.Optional[typing.List[str]]` |
| `kwargs` | `**kwargs` |

#### upload_dir()

```python
def upload_dir(
    dir_path: pathlib._local.Path,
    verify: bool,
) -> str
```
Uploads a directory to a remote location and returns the remote URI.



| Parameter | Type |
|-|-|
| `dir_path` | `pathlib._local.Path` |
| `verify` | `bool` |

#### upload_file()

```python
def upload_file(
    fp: pathlib._local.Path,
    verify: bool,
) -> typing.Tuple[str, str]
```
Uploads a file to a remote location and returns the remote URI.



| Parameter | Type |
|-|-|
| `fp` | `pathlib._local.Path` |
| `verify` | `bool` |

## flyte.remote.Action

A class representing an action. It is used to manage the run of a task and its state on the remote Union API.


```python
class Action(
    pb2: run_definition_pb2.Action,
    _details: ActionDetails | None,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `run_definition_pb2.Action` |
| `_details` | `ActionDetails \| None` |

### Methods

| Method | Description |
|-|-|
| [`details()`](#details) | Get the details of the action. |
| [`done()`](#done) | Check if the action is done. |
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


| Parameter | Type |
|-|-|
| `quiet` | `bool` |
| `wait_for` | `WaitFor` |

#### watch()

```python
def watch(
    cache_data_on_done: bool,
    wait_for: WaitFor,
) -> AsyncGenerator[ActionDetails, None]
```
Watch the action for updates. This is a placeholder for watching the action.


| Parameter | Type |
|-|-|
| `cache_data_on_done` | `bool` |
| `wait_for` | `WaitFor` |

### Properties

| Property | Type | Description |
|-|-|-|
| `action_id` | `None` | {{< multiline >}}Get the action ID.
{{< /multiline >}} |
| `name` | `None` | {{< multiline >}}Get the name of the action.
{{< /multiline >}} |
| `phase` | `None` | {{< multiline >}}Get the phase of the action.
{{< /multiline >}} |
| `raw_phase` | `None` | {{< multiline >}}Get the raw phase of the action.
{{< /multiline >}} |
| `run_name` | `None` | {{< multiline >}}Get the name of the run.
{{< /multiline >}} |
| `task_name` | `None` | {{< multiline >}}Get the name of the task.
{{< /multiline >}} |

## flyte.remote.ActionDetails

A class representing an action. It is used to manage the run of a task and its state on the remote Union API.


```python
class ActionDetails(
    pb2: run_definition_pb2.ActionDetails,
    _inputs: ActionInputs | None,
    _outputs: ActionOutputs | None,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `run_definition_pb2.ActionDetails` |
| `_inputs` | `ActionInputs \| None` |
| `_outputs` | `ActionOutputs \| None` |

### Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the action is in a terminal state (completed or failed). |
| [`inputs()`](#inputs) | Placeholder for inputs. |
| [`logs_available()`](#logs_available) | Check if logs are available for the action, optionally for a specific attempt. |
| [`outputs()`](#outputs) | Placeholder for outputs. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch_updates()`](#watch_updates) |  |


#### done()

```python
def done()
```
Check if the action is in a terminal state (completed or failed). This is a placeholder for checking the
action state.


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


| Parameter | Type |
|-|-|
| `attempt` | `int \| None` |

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


#### watch_updates()

```python
def watch_updates(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
| Parameter | Type |
|-|-|
| `cache_data_on_done` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `abort_info` | `None` |  |
| `action_id` | `None` | {{< multiline >}}Get the action ID.
{{< /multiline >}} |
| `attempts` | `None` | {{< multiline >}}Get the number of attempts of the action.
{{< /multiline >}} |
| `error_info` | `None` |  |
| `is_running` | `None` | {{< multiline >}}Check if the action is currently running.
{{< /multiline >}} |
| `metadata` | `None` |  |
| `name` | `None` | {{< multiline >}}Get the name of the action.
{{< /multiline >}} |
| `phase` | `None` | {{< multiline >}}Get the phase of the action.
{{< /multiline >}} |
| `raw_phase` | `None` | {{< multiline >}}Get the raw phase of the action.
{{< /multiline >}} |
| `run_name` | `None` | {{< multiline >}}Get the name of the run.
{{< /multiline >}} |
| `runtime` | `None` | {{< multiline >}}Get the runtime of the action.
{{< /multiline >}} |
| `status` | `None` |  |
| `task_name` | `None` | {{< multiline >}}Get the name of the task.
{{< /multiline >}} |

## flyte.remote.ActionInputs

A class representing the inputs of an action. It is used to manage the inputs of a task and its state on the
remote Union API.


```python
class ActionInputs(
    pb2: common_pb2.Inputs,
    data: Dict[str, Any],
)
```
| Parameter | Type |
|-|-|
| `pb2` | `common_pb2.Inputs` |
| `data` | `Dict[str, Any]` |

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
D.clear() -> None.  Remove all items from D.


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
| Parameter | Type |
|-|-|
| `iterable` |  |
| `value` |  |

#### get()

```python
def get(
    key,
    default,
)
```
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### items()

```python
def items()
```
D.items() -> a set-like object providing a view on D's items


#### keys()

```python
def keys()
```
D.keys() -> a set-like object providing a view on D's keys


#### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

#### popitem()

```python
def popitem()
```
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


#### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type |
|-|-|
| `key` |  |
| `default` |  |

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
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type |
|-|-|
| `other` |  |
| `kwds` |  |

#### values()

```python
def values()
```
D.values() -> an object providing a view on D's values


## flyte.remote.ActionOutputs

A class representing the outputs of an action. It is used to manage the outputs of a task and its state on the
remote Union API.


```python
class ActionOutputs(
    pb2: common_pb2.Outputs,
    data: Tuple[Any, ...],
)
```
| Parameter | Type |
|-|-|
| `pb2` | `common_pb2.Outputs` |
| `data` | `Tuple[Any, ...]` |

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


## flyte.remote.Project

A class representing a project in the Union API.


```python
class Project(
    pb2: project_pb2.Project,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `project_pb2.Project` |

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


## flyte.remote.Run

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class Run(
    pb2: run_definition_pb2.Run,
    _details: RunDetails | None,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `run_definition_pb2.Run` |
| `_details` | `RunDetails \| None` |

### Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the run is done. |
| [`sync()`](#sync) | Sync the run with the remote server. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`watch()`](#watch) | Get the details of the run. |


#### done()

```python
def done()
```
Check if the run is done.


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


#### watch()

```python
def watch(
    cache_data_on_done: bool,
) -> AsyncGenerator[ActionDetails, None]
```
Get the details of the run. This is a placeholder for getting the run details.


| Parameter | Type |
|-|-|
| `cache_data_on_done` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | {{< multiline >}}Get the name of the run.
{{< /multiline >}} |
| `phase` | `None` | {{< multiline >}}Get the phase of the run.
{{< /multiline >}} |
| `raw_phase` | `None` | {{< multiline >}}Get the raw phase of the run.
{{< /multiline >}} |
| `url` | `None` | {{< multiline >}}Get the URL of the run.
{{< /multiline >}} |

## flyte.remote.RunDetails

A class representing a run of a task. It is used to manage the run of a task and its state on the remote
Union API.


```python
class RunDetails(
    pb2: run_definition_pb2.RunDetails,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `run_definition_pb2.RunDetails` |

### Methods

| Method | Description |
|-|-|
| [`done()`](#done) | Check if the run is in a terminal state (completed or failed). |
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
| `action_id` | `None` | {{< multiline >}}Get the action ID.
{{< /multiline >}} |
| `name` | `None` | {{< multiline >}}Get the name of the action.
{{< /multiline >}} |
| `task_name` | `None` | {{< multiline >}}Get the name of the task.
{{< /multiline >}} |

## flyte.remote.Secret

```python
class Secret(
    pb2: definition_pb2.Secret,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `definition_pb2.Secret` |

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
| Parameter | Type |
|-|-|
| `pb2` | `task_definition_pb2.Task` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | Get a task by its ID or name. |
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



| Parameter | Type |
|-|-|
| `name` | `str` |
| `project` | `str \| None` |
| `domain` | `str \| None` |
| `version` | `str \| None` |
| `auto_version` | `AutoVersioning \| None` |

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
| `name` | `None` | {{< multiline >}}The name of the task.
{{< /multiline >}} |
| `version` | `None` | {{< multiline >}}The version of the task.
{{< /multiline >}} |

## flyte.remote.Trigger

```python
class Trigger(
    pb2: trigger_definition_pb2.Trigger,
    details: TriggerDetails | None,
)
```
| Parameter | Type |
|-|-|
| `pb2` | `trigger_definition_pb2.Trigger` |
| `details` | `TriggerDetails \| None` |

### Methods

| Method | Description |
|-|-|
| [`get_details()`](#get_details) | Get detailed information about this trigger. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


#### get_details()

```python
def get_details()
```
Get detailed information about this trigger.


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
| Parameter | Type |
|-|-|
| `pb2` | `UserInfoResponse` |

### Methods

| Method | Description |
|-|-|
| [`name()`](#name) |  |
| [`subject()`](#subject) |  |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


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


