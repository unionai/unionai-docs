---
title: flytekitplugins.flyteinteractive.jupyter_lib.decorator
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.flyteinteractive.jupyter_lib.decorator

## Directory

### Classes

| Class | Description |
|-|-|
| [`jupyter`](.././flytekitplugins.flyteinteractive.jupyter_lib.decorator#flytekitpluginsflyteinteractivejupyter_libdecoratorjupyter) | Abstract class for class decorators. |

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



| Parameter | Type |
|-|-|
| `child_process` | `multiprocessing.context.Process` |
| `task_function` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
| `post_execute` | `typing.Optional[typing.Callable]` |

#### write_example_notebook()

```python
def write_example_notebook(
    task_function: typing.Optional[typing.Callable],
    notebook_dir: str,
)
```
Create an example notebook with markdown and code cells that show instructions to resume task & jupyter task code.



| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `notebook_dir` | `str` |

## flytekitplugins.flyteinteractive.jupyter_lib.decorator.jupyter

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


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



| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `max_idle_seconds` | `typing.Optional[int]` |
| `port` | `int` |
| `enable` | `bool` |
| `run_task_first` | `bool` |
| `notebook_dir` | `typing.Optional[str]` |
| `pre_execute` | `typing.Optional[typing.Callable]` |
| `post_execute` | `typing.Optional[typing.Callable]` |

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


