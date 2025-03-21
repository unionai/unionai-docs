---
title: flytekit.interactive
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interactive


..
currentmodule:: flytekit.interactive

This package contains flyteinteractive plugin for Flytekit.

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   vscode
   VscodeConfig
   DEFAULT_CODE_SERVER_DIR_NAME
   DEFAULT_CODE_SERVER_REMOTE_PATH
   DEFAULT_CODE_SERVER_EXTENSIONS
   get_task_inputs

## Directory

### Classes

| Class | Description |
|-|-|
| [`VscodeConfig`](.././flytekit.interactive#flytekitinteractivevscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`vscode`](.././flytekit.interactive#flytekitinteractivevscode) | Abstract class for class decorators. |

## flytekit.interactive.VscodeConfig

VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths.



```python
def VscodeConfig(
    code_server_remote_paths: typing.Optional[typing.Dict[str, str]],
    code_server_dir_names: typing.Optional[typing.Dict[str, str]],
    extension_remote_paths: typing.Optional[typing.List[str]],
):
```
| Parameter | Type |
|-|-|
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`add_extensions()`](#add_extensions) | Add additional extensions to the extension_remote_paths list |


#### add_extensions()

```python
def add_extensions(
    extensions: typing.Union[str, typing.List[str]],
):
```
Add additional extensions to the extension_remote_paths list.


| Parameter | Type |
|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` |

## flytekit.interactive.vscode

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

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator |


#### execute()

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

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


