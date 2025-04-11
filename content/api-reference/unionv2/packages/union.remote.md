---
title: union.remote
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.remote


Remote Entities that are accessible from the Union Server once deployed or created.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Run`](.././union.remote#unionremoterun) | A class representing a run of a task. |
| [`Task`](.././union.remote#unionremotetask) |  |

### Methods

| Method | Description |
|-|-|
| [`upload_dir()`](#upload_dir) | Uploads a directory to a remote location and returns the remote URI. |
| [`upload_file()`](#upload_file) | Uploads a file to a remote location and returns the remote URI. |


## Methods

#### upload_dir()

```python
def upload_dir(
    dir_path: pathlib._local.Path,
) -> typing.Tuple[str, str]
```
Uploads a directory to a remote location and returns the remote URI.


| Parameter | Type |
|-|-|
| `dir_path` | `pathlib._local.Path` |

#### upload_file()

```python
def upload_file(
    fp: pathlib._local.Path,
) -> typing.Tuple[str, str]
```
Uploads a file to a remote location and returns the remote URI.


| Parameter | Type |
|-|-|
| `fp` | `pathlib._local.Path` |

## union.remote.Run

A class representing a run of a task. It is used to manage the execution of a task and its state on the remote
Union API.


```python
class Run(
    run_id: str,
    _outputs: Any,
)
```
| Parameter | Type |
|-|-|
| `run_id` | `str` |
| `_outputs` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`cancel()`](#cancel) | Cancel the execution. |
| [`done()`](#done) | Check if the execution is in a terminal state (completed or failed). |
| [`exception()`](#exception) | Returns the Exceptions / error if set. |
| [`get()`](#get) |  |
| [`get_typed_outputs()`](#get_typed_outputs) | Get the typed outputs of the execution. |
| [`result()`](#result) | Get the results of the execution. |
| [`search()`](#search) |  |
| [`sync()`](#sync) | Sync the state of the execution. |
| [`wait()`](#wait) | Wait for the execution to complete. |


#### cancel()

```python
def cancel()
```
Cancel the execution. This is a placeholder for canceling the execution.


#### done()

```python
def done()
```
Check if the execution is in a terminal state (completed or failed). This is a placeholder for checking the
execution state.


#### exception()

```python
def exception()
```
Returns the Exceptions / error if set.


#### get()

```python
def get(
    uri: str | None,
    name: str | None,
    project: str | None,
    domain: str | None,
) -> Run
```
| Parameter | Type |
|-|-|
| `uri` | `str \| None` |
| `name` | `str \| None` |
| `project` | `str \| None` |
| `domain` | `str \| None` |

#### get_typed_outputs()

```python
def get_typed_outputs(
    hints: Dict[str, Type],
) -> Any
```
Get the typed outputs of the execution. This is a placeholder for getting the outputs.


| Parameter | Type |
|-|-|
| `hints` | `Dict[str, Type]` |

#### result()

```python
def result()
```
Get the results of the execution. This is a placeholder for getting the result.


#### search()

```python
def search(
    limit: int,
) -> Iterator[Run]
```
| Parameter | Type |
|-|-|
| `limit` | `int` |

#### sync()

```python
def sync()
```
Sync the state of the execution. This is a placeholder for syncing the execution state.


#### wait()

```python
def wait(
    timeout: Optional[Union[timedelta, int]],
    poll_interval: Optional[Union[timedelta, int]],
    sync_nodes: bool,
) -> Run
```
Wait for the execution to complete. This is a blocking call.



| Parameter | Type |
|-|-|
| `timeout` | `Optional[Union[timedelta, int]]` |
| `poll_interval` | `Optional[Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `error` |  | {{< multiline >}}Get the error if the execution has failed. This is a placeholder for getting the error state.
{{< /multiline >}} |
| `finished_at` |  | {{< multiline >}}Get the finish time of the execution. This is a placeholder for getting the finish time.
{{< /multiline >}} |
| `is_running` |  | {{< multiline >}}Check if the execution is currently running. This is a placeholder for checking the execution state.
{{< /multiline >}} |
| `outputs` |  | {{< multiline >}}Placeholder for outputs. This can be extended to handle outputs from the run context.
{{< /multiline >}} |
| `started_at` |  | {{< multiline >}}Get the start time of the execution. This is a placeholder for getting the start time.
{{< /multiline >}} |

## union.remote.Task

```python
class Task(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) |  |
| [`search()`](#search) |  |


#### get()

```python
def get(
    uri: str | None,
    name: str | None,
    project: str | None,
    domain: str | None,
) -> LazyEntity[Task]
```
| Parameter | Type |
|-|-|
| `uri` | `str \| None` |
| `name` | `str \| None` |
| `project` | `str \| None` |
| `domain` | `str \| None` |

#### search()

```python
def search(
    limit: int,
) -> Iterator[Task]
```
| Parameter | Type |
|-|-|
| `limit` | `int` |

