---
title: vscode
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# vscode

**Package:** `flytekit.interactive`

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
def vscode(
    task_function: typing.Optional[typing.Callable],
    max_idle_seconds: typing.Optional[int],
    port: int,
    enable: bool,
    run_task_first: bool,
    pre_execute: typing.Optional[typing.Callable],
    post_execute: typing.Optional[typing.Callable],
    config: typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig],
):
```
vscode decorator modifies a container to run a VSCode server:
1. Overrides the user function with a VSCode setup function.
2. Download vscode server and extension from remote to local.
3. Prepare the interactive debugging Python script and launch.json.
4. Prepare task resumption script.
5. Launches and monitors the VSCode server.
6. Register signal handler for task resumption.
7. Terminates if the server is idle for a set duration or user trigger task resumption.



| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `max_idle_seconds` | `typing.Optional[int]` |
| `port` | `int` |
| `enable` | `bool` |
| `run_task_first` | `bool` |
| `pre_execute` | `typing.Optional[typing.Callable]` |
| `post_execute` | `typing.Optional[typing.Callable]` |
| `config` | `typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig]` |
## Methods

### execute()

```python
def execute(
    args,
    kwargs,
):
```
This method will be called when the decorated function is called.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


No parameters
