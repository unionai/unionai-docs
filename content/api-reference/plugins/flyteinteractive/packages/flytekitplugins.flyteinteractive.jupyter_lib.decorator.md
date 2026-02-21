---
title: flytekitplugins.flyteinteractive.jupyter_lib.decorator
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.flyteinteractive.jupyter_lib.decorator

## Directory

### Classes

| Class | Description |
|-|-|
| [`jupyter`](.././flytekitplugins.flyteinteractive.jupyter_lib.decorator#flytekitpluginsflyteinteractivejupyter_libdecoratorjupyter) |  |

### Methods

| Method | Description |
|-|-|
| [`exit_handler()`](#exit_handler) | 1. |
| [`write_example_notebook()`](#write_example_notebook) | Create an example notebook with markdown and code cells that show instructions to resume task & jupyter task code. |


### Variables

| Property | Type | Description |
|-|-|-|
| `EXAMPLE_JUPYTER_NOTEBOOK_NAME` | `str` |  |
| `JUPYTER_TYPE_VALUE` | `str` |  |
| `MAX_IDLE_SECONDS` | `int` |  |

## Methods

#### exit_handler()

```python
def exit_handler(
    child_process: multiprocessing.context.Process,
    task_function,
    args,
    kwargs,
    post_execute: typing.Optional[typing.Callable],
)
```
1. Wait for the child process to finish. This happens when the user clicks "Shut Down" in Jupyter
2. Execute post function, if given.
3. Executes the task function, when the Jupyter Notebook Server is terminated.



| Parameter | Type | Description |
|-|-|-|
| `child_process` | `multiprocessing.context.Process` | The process to be terminated. |
| `task_function` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |
| `post_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the jupyter notebook server is terminated. |

#### write_example_notebook()

```python
def write_example_notebook(
    task_function: typing.Optional[typing.Callable],
    notebook_dir: str,
)
```
Create an example notebook with markdown and code cells that show instructions to resume task & jupyter task code.



| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Optional[typing.Callable]` | User's task function. |
| `notebook_dir` | `str` | Local path to write the example notebook to |

## flytekitplugins.flyteinteractive.jupyter_lib.decorator.jupyter

```python
class jupyter(
    task_function: typing.Optional[typing.Callable],
    max_idle_seconds: typing.Optional[int],
    port: int,
    enable: bool,
    run_task_first: bool,
    notebook_dir: typing.Optional[str],
    pre_execute: typing.Optional[typing.Callable],
    post_execute: typing.Optional[typing.Callable],
)
```
jupyter decorator modifies a container to run a Jupyter Notebook server:
1. Launches and monitors the Jupyter Notebook server.
2. Write Example Jupyter Notebook.
3. Terminates if the server is idle for a set duration or user shuts down manually.



| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Optional[typing.Callable]` | The user function to be decorated. Defaults to None. |
| `max_idle_seconds` | `typing.Optional[int]` | The duration in seconds to live after no activity detected. |
| `port` | `int` | The port to be used by the Jupyter Notebook server. Defaults to 8888. |
| `enable` | `bool` | Whether to enable the Jupyter decorator. Defaults to True. |
| `run_task_first` | `bool` | Executes the user's task first when True. Launches the Jupyter Notebook server only if the user's task fails. Defaults to False. |
| `notebook_dir` | `typing.Optional[str]` | |
| `pre_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the jupyter setup function. |
| `post_execute` | `typing.Optional[typing.Callable]` | The function to be executed before the jupyter is self-terminated. |

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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


