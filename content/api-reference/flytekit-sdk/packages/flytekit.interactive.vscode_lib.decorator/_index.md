---
title: flytekit.interactive.vscode_lib.decorator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.decorator

## Directory

### Classes

| Class | Description |
|-|-|
| [`vscode`](../flytekit.interactive.vscode_lib.decorator/vscode) | Abstract class for class decorators. |

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



| Parameter | Type | Description |
|-|-|-|
| `url` |  | The URL of the file to download. |
| `target_dir` | `typing.Optional[str]` | The directory where the file should be saved. Defaults to current directory. |

#### download_vscode()

```python
def download_vscode(
    config: flytekit.interactive.vscode_lib.config.VscodeConfig,
)
```
Download vscode server and extension from remote to local and add the directory of binary executable to $PATH.



| Parameter | Type | Description |
|-|-|-|
| `config` | `flytekit.interactive.vscode_lib.config.VscodeConfig` | VSCode config contains default URLs of the VSCode server and extension remote paths. |

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



| Parameter | Type | Description |
|-|-|-|
| `child_process` | `multiprocessing.context.Process` | The process to be terminated. |
| `task_function` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |
| `max_idle_seconds` | `int` | The duration in seconds to live after no activity detected. |
| `post_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the vscode is self-terminated. |

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



| Parameter | Type | Description |
|-|-|-|
| `code_server_info_dict` | `dict` | A dictionary containing code server information. The keys should be the architecture type ('amd64' or 'arm64') and the values should be the corresponding code server information. |

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
| Parameter | Type | Description |
|-|-|-|
| `extension` | `str` | |
| `installed_extensions` | `typing.List[str]` | |

#### prepare_interactive_python()

```python
def prepare_interactive_python(
    task_function,
)
```
1. Copy the original task file to the context working directory. This ensures that the inputs.pb can be loaded, as loading requires the original task interface.
   By doing so, even if users change the task interface in their code, we can use the copied task file to load the inputs as native Python objects.
2. Generate a Python script and a launch.json for users to debug interactively.



| Parameter | Type | Description |
|-|-|-|
| `task_function` |  | User's task function. |

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


| Parameter | Type | Description |
|-|-|-|
| `pid` | `int` | |

