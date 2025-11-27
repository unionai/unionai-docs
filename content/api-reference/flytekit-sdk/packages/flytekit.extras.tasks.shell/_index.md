---
title: flytekit.extras.tasks.shell
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.tasks.shell

## Directory

### Classes

| Class | Description |
|-|-|
| [`AttrDict`](../flytekit.extras.tasks.shell/attrdict) | Convert a dictionary to an attribute style lookup. |
| [`OutputLocation`](../flytekit.extras.tasks.shell/outputlocation) |  |
| [`ProcessResult`](../flytekit.extras.tasks.shell/processresult) | Stores a process return code, standard output and standard error. |
| [`RawShellTask`](../flytekit.extras.tasks.shell/rawshelltask) |  |
| [`ShellTask`](../flytekit.extras.tasks.shell/shelltask) |  |

### Methods

| Method | Description |
|-|-|
| [`get_raw_shell_task()`](#get_raw_shell_task) |  |
| [`subproc_execute()`](#subproc_execute) | Execute a command and capture its stdout and stderr. |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## Methods

#### get_raw_shell_task()

```python
def get_raw_shell_task(
    name: str,
) -> flytekit.extras.tasks.shell.RawShellTask
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

#### subproc_execute()

```python
def subproc_execute(
    command: typing.Union[typing.List[str], str],
    kwargs,
) -> flytekit.extras.tasks.shell.ProcessResult
```
Execute a command and capture its stdout and stderr. Useful for executing
shell commands from within a python task.



| Parameter | Type | Description |
|-|-|-|
| `command` | `typing.Union[typing.List[str], str]` | The command to be executed as a list of strings. |
| `kwargs` | `**kwargs` | |

