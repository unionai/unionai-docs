---
title: ToolTaskResolver
version: 2.5.18
variants: +flyte +union
layout: py_api
---

# ToolTaskResolver

**Package:** `flyteplugins.agents.core`

Resolver for a task shadowed at module scope by a tool wrapper.

Recovers the underlying task via the wrapper's ``__wrapped_task__`` hook so
the worker runs the task's own body instead of re-dispatching the tool.


## Properties

| Property | Type | Description |
|-|-|-|
| `import_path` | `str` | The import path of the resolver. This should be a valid python import path. |

## Methods

| Method | Description |
|-|-|
| [`connection_lost()`](#connection_lost) | Called when the connection is lost or closed. |
| [`connection_made()`](#connection_made) | Called when a connection is made. |
| [`data_received()`](#data_received) | Called when some data is received. |
| [`eof_received()`](#eof_received) | Called when the other end calls write_eof() or equivalent. |
| [`load_app_env()`](#load_app_env) | Given the set of identifier keys, should return one AppEnvironment or raise an error if not found. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one TaskTemplate or raise an error if not found. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter TaskTemplate. |
| [`pause_writing()`](#pause_writing) | Called when the transport's buffer goes over the high-water mark. |
| [`resume_writing()`](#resume_writing) | Called when the transport's buffer drains below the low-water mark. |


### connection_lost()

```python
def connection_lost(
    exc,
)
```
Called when the connection is lost or closed.

The argument is an exception object or None (the latter
meaning a regular EOF is received or the connection was
aborted or closed).


| Parameter | Type | Description |
|-|-|-|
| `exc` |  | |

### connection_made()

```python
def connection_made(
    transport,
)
```
Called when a connection is made.

The argument is the transport representing the pipe connection.
To receive data, wait for data_received() calls.
When the connection is closed, connection_lost() is called.


| Parameter | Type | Description |
|-|-|-|
| `transport` |  | |

### data_received()

```python
def data_received(
    data,
)
```
Called when some data is received.

The argument is a bytes object.


| Parameter | Type | Description |
|-|-|-|
| `data` |  | |

### eof_received()

```python
def eof_received()
```
Called when the other end calls write_eof() or equivalent.

If this returns a false value (including None), the transport
will close itself.  If it returns a true value, closing the
transport is up to the protocol.


### load_app_env()

```python
def load_app_env(
    loader_args: str,
) -> AppEnvironment
```
Given the set of identifier keys, should return one AppEnvironment or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `str` | |

### load_task()

```python
def load_task(
    loader_args,
)
```
Given the set of identifier keys, should return one TaskTemplate or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` |  | |

### loader_args()

```python
def loader_args(
    task: flyte._task.TaskTemplate,
    root_dir: pathlib.Path,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter TaskTemplate. Each string should not have
spaces or special characters. This is used to identify the task in the resolver.


| Parameter | Type | Description |
|-|-|-|
| `task` | `flyte._task.TaskTemplate` | |
| `root_dir` | `pathlib.Path` | |

### pause_writing()

```python
def pause_writing()
```
Called when the transport's buffer goes over the high-water mark.

Pause and resume calls are paired -- pause_writing() is called
once when the buffer goes strictly over the high-water mark
(even if subsequent writes increases the buffer size even
more), and eventually resume_writing() is called once when the
buffer size reaches the low-water mark.

Note that if the buffer size equals the high-water mark,
pause_writing() is not called -- it must go strictly over.
Conversely, resume_writing() is called when the buffer size is
equal or lower than the low-water mark.  These end conditions
are important to ensure that things go as expected when either
mark is zero.

NOTE: This is the only Protocol callback that is not called
through EventLoop.call_soon() -- if it were, it would have no
effect when it's most needed (when the app keeps writing
without yielding until pause_writing() is called).


### resume_writing()

```python
def resume_writing()
```
Called when the transport's buffer drains below the low-water mark.

See pause_writing() for details.


