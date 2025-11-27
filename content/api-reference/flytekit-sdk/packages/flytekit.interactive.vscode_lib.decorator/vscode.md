---
title: vscode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# vscode

**Package:** `flytekit.interactive.vscode_lib.decorator`

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
class vscode(
    task_function: typing.Optional[typing.Callable],
    max_idle_seconds: typing.Optional[int],
    port: int,
    enable: bool,
    run_task_first: bool,
    pre_execute: typing.Optional[typing.Callable],
    post_execute: typing.Optional[typing.Callable],
    config: typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig],
)
```
vscode decorator modifies a container to run a VSCode server:
1. Overrides the user function with a VSCode setup function.
2. Download vscode server and extension from remote to local.
3. Prepare the interactive debugging Python script and launch.json.
4. Prepare task resumption script.
5. Launches and monitors the VSCode server.
6. Register signal handler for task resumption.
7. Terminates if the server is idle for a set duration or user trigger task resumption.



| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Optional[typing.Callable]` | The user function to be decorated. Defaults to None. |
| `max_idle_seconds` | `typing.Optional[int]` | The duration in seconds to live after no activity detected. |
| `port` | `int` | The port to be used by the VSCode server. Defaults to 8080. |
| `enable` | `bool` | Whether to enable the VSCode decorator. Defaults to True. |
| `run_task_first` | `bool` | Executes the user's task first when True. Launches the VSCode server only if the user's task fails. Defaults to False. |
| `pre_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the vscode setup function. |
| `post_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the vscode is self-terminated. |
| `config` | `typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig]` | VSCode config contains default URLs of the VSCode server and extension remote paths. |

## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called. |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator. |


### execute()

```python
def execute(
    args,
    kwargs,
)
```
This method will be called when the decorated function is called.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


