---
title: flyte.remote
version: 2.1.2.dev2+g62f55b516
variants: +flyte +union
layout: py_api
sidebar_expanded: true
---

# flyte.remote

Remote Entities that are accessible from the Union Server once deployed or created.
## Directory

### Classes

| Class | Description |
|-|-|
| [`Action`](../flyte.remote/action) | A class representing an action. |
| [`ActionDetails`](../flyte.remote/actiondetails) | A class representing an action. |
| [`ActionInputs`](../flyte.remote/actioninputs) | A class representing the inputs of an action. |
| [`ActionOutputs`](../flyte.remote/actionoutputs) | A class representing the outputs of an action. |
| [`App`](../flyte.remote/app) |  |
| [`Project`](../flyte.remote/project) | A class representing a project in the Union API. |
| [`Run`](../flyte.remote/run) | A class representing a run of a task. |
| [`RunDetails`](../flyte.remote/rundetails) | A class representing a run of a task. |
| [`Secret`](../flyte.remote/secret) |  |
| [`Task`](../flyte.remote/task) |  |
| [`TaskDetails`](../flyte.remote/taskdetails) |  |
| [`TimeFilter`](../flyte.remote/timefilter) | Filter for time-based fields (e. |
| [`Trigger`](../flyte.remote/trigger) | Represents a trigger in the Flyte platform. |
| [`User`](../flyte.remote/user) | Represents a user in the Flyte platform. |

### Methods

| Method | Description |
|-|-|
| [`auth_metadata()`](#auth_metadata) | This context manager allows you to pass contextualized auth metadata downstream to the Flyte authentication system. |
| [`upload_dir()`](#upload_dir) | Uploads a directory to a remote location and returns the remote URI. |
| [`upload_file()`](#upload_file) | Uploads a file to a remote location and returns the remote URI. |


## Methods

#### auth_metadata()

```python
def auth_metadata(
    kv: typing.Tuple[str, str],
)
```
This context manager allows you to pass contextualized auth metadata downstream to the Flyte authentication system.

This is only useful if flyte.init_passthrough() has been called.

```python

flyte.init_passthrough("my-endpoint")

...

with auth_metadata((key1, value1), (key2, value2)):
    ...
```



| Parameter | Type | Description |
|-|-|-|
| `kv` | `typing.Tuple[str, str]` | |

#### upload_dir()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await upload_dir.aio()`.
```python
def upload_dir(
    dir_path: pathlib.Path,
    verify: bool,
    prefix: str | None,
) -> str
```
Uploads a directory to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `dir_path` | `pathlib.Path` | The directory path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. |
| `prefix` | `str \| None` | |

**Returns:** The remote URI of the uploaded directory.

#### upload_file()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await upload_file.aio()`.
```python
def upload_file(
    fp: pathlib.Path,
    verify: bool,
    fname: str | None,
) -> typing.Tuple[str, str]
```
Uploads a file to a remote location and returns the remote URI.



| Parameter | Type | Description |
|-|-|-|
| `fp` | `pathlib.Path` | The file path to upload. |
| `verify` | `bool` | Whether to verify the certificate for HTTPS requests. |
| `fname` | `str \| None` | Optional file name for the remote path. |

**Returns:** Tuple of (MD5 digest hex string, remote native URL).

