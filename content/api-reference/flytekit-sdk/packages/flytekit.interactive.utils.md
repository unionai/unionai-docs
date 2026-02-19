---
title: flytekit.interactive.utils
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interactive.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`execute_command()`](#execute_command) | Execute a command in the shell. |
| [`get_task_inputs()`](#get_task_inputs) | Read task input data from inputs. |
| [`load_module_from_path()`](#load_module_from_path) | Imports a Python module from a specified file path. |


### Variables

| Property | Type | Description |
|-|-|-|
| `EXIT_CODE_SUCCESS` | `int` |  |

## Methods

#### execute_command()

```python
def execute_command(
    cmd,
)
```
Execute a command in the shell.


| Parameter | Type | Description |
|-|-|-|
| `cmd` |  | |

#### get_task_inputs()

```python
def get_task_inputs(
    task_module_name,
    task_name,
    context_working_dir,
)
```
Read task input data from inputs.pb for a specific task function and convert it into Python types and structures.



| Parameter | Type | Description |
|-|-|-|
| `task_module_name` |  | The name of the Python module containing the task function. |
| `task_name` |  | The name of the task function within the module. |
| `context_working_dir` |  | The directory path where the input file and module file are located. |

#### load_module_from_path()

```python
def load_module_from_path(
    module_name,
    path,
)
```
Imports a Python module from a specified file path.



| Parameter | Type | Description |
|-|-|-|
| `module_name` |  | The name you want to assign to the imported module. |
| `path` |  | The file system path to the Python file (.py) that contains the module you want to import. |

