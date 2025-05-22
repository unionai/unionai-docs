---
title: flytekit.interactive.vscode_lib.decorator
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.decorator

## Directory

### Classes

| Class | Description |
|-|-|
| [`vscode`](.././flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscode) | Abstract class for class decorators. |

### Methods

| Method | Description |
|-|-|
| [`download_file()`](#download_file) | Download a file from a given URL using fsspec. |
| [`download_vscode()`](#download_vscode) | Download vscode server and extension from remote to local and add the directory of binary executable to $PATH. |
| [`exit_handler()`](#exit_handler) | 1. |
| [`get_code_server_info()`](#get_code_server_info) | Returns the code server information based on the system's architecture. |
| [`get_installed_extensions()`](#get_installed_extensions) | Get the list of installed extensions. |
| [`is_extension_installed()`](#is_extension_installed) |  |
| [`prepare_interactive_python()`](#prepare_interactive_python) | 1. |
| [`prepare_launch_json()`](#prepare_launch_json) | Generate the launch. |
| [`prepare_resume_task_python()`](#prepare_resume_task_python) | Generate a Python script for users to resume the task. |


### Variables

| Property | Type | Description |
|-|-|-|
| `EXECUTABLE_NAME` | `str` |  |
| `EXIT_CODE_SUCCESS` | `int` |  |
| `HEARTBEAT_PATH` | `str` |  |
| `INTERACTIVE_DEBUGGING_FILE_NAME` | `str` |  |
| `MAX_IDLE_SECONDS` | `int` |  |
| `RESUME_TASK_FILE_NAME` | `str` |  |
| `TASK_FUNCTION_SOURCE_PATH` | `str` |  |
| `VSCODE_TYPE_VALUE` | `str` |  |

## Methods

#### download_file()

```python
def download_file(
    url,
    target_dir: typing.Optional[str],
)
```
Download a file from a given URL using fsspec.



| Parameter | Type |
|-|-|
| `url` |  |
| `target_dir` | `typing.Optional[str]` |

#### download_vscode()

```python
def download_vscode(
    config: flytekit.interactive.vscode_lib.config.VscodeConfig,
)
```
Download vscode server and extension from remote to local and add the directory of binary executable to $PATH.



| Parameter | Type |
|-|-|
| `config` | `flytekit.interactive.vscode_lib.config.VscodeConfig` |

#### exit_handler()

```python
def exit_handler(
    child_process: multiprocessing.context.Process,
    task_function,
    args,
    kwargs,
    max_idle_seconds: int,
    post_execute: typing.Optional[typing.Callable],
)
```
1. Check the modified time of ~/.local/share/code-server/heartbeat.
   If it is older than max_idle_second seconds, kill the container.
   Otherwise, check again every HEARTBEAT_CHECK_SECONDS.
2. Wait for user to resume the task. If resume_task is set, terminate the VSCode server, reload the task function, and run it with the input of the task.



| Parameter | Type |
|-|-|
| `child_process` | `multiprocessing.context.Process` |
| `task_function` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
| `max_idle_seconds` | `int` |
| `post_execute` | `typing.Optional[typing.Callable]` |

#### get_code_server_info()

```python
def get_code_server_info(
    code_server_info_dict: dict,
) -> str
```
Returns the code server information based on the system's architecture.

This function checks the system's architecture and returns the corresponding
code server information from the provided dictionary. The function currently
supports AMD64 and ARM64 architectures.



| Parameter | Type |
|-|-|
| `code_server_info_dict` | `dict` |

#### get_installed_extensions()

```python
def get_installed_extensions()
```
Get the list of installed extensions.

Returns:
    List[str]: The list of installed extensions.


#### is_extension_installed()

```python
def is_extension_installed(
    extension: str,
    installed_extensions: typing.List[str],
) -> bool
```
| Parameter | Type |
|-|-|
| `extension` | `str` |
| `installed_extensions` | `typing.List[str]` |

#### prepare_interactive_python()

```python
def prepare_interactive_python(
    task_function,
)
```
1. Copy the original task file to the context working directory. This ensures that the inputs.pb can be loaded, as loading requires the original task interface.
   By doing so, even if users change the task interface in their code, we can use the copied task file to load the inputs as native Python objects.
2. Generate a Python script and a launch.json for users to debug interactively.



| Parameter | Type |
|-|-|
| `task_function` |  |

#### prepare_launch_json()

```python
def prepare_launch_json()
```
Generate the launch.json and settings.json for users to easily launch interactive debugging and task resumption.


#### prepare_resume_task_python()

```python
def prepare_resume_task_python(
    pid: int,
)
```
Generate a Python script for users to resume the task.


| Parameter | Type |
|-|-|
| `pid` | `int` |

## flytekit.interactive.vscode_lib.decorator.vscode

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
| [`execute()`](#execute) | This method will be called when the decorated function is called. |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator. |


#### execute()

```python
def execute(
    args,
    kwargs,
)
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


