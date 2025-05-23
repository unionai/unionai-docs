---
title: flytekit.interactive.utils
version: 0.1.dev2192+g7c539c3.d20250403
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


| Parameter | Type |
|-|-|
| `cmd` |  |

#### get_task_inputs()

```python
def get_task_inputs(
    task_module_name,
    task_name,
    context_working_dir,
)
```
Read task input data from inputs.pb for a specific task function and convert it into Python types and structures.



| Parameter | Type |
|-|-|
| `task_module_name` |  |
| `task_name` |  |
| `context_working_dir` |  |

#### load_module_from_path()

```python
def load_module_from_path(
    module_name,
    path,
)
```
Imports a Python module from a specified file path.



| Parameter | Type |
|-|-|
| `module_name` |  |
| `path` |  |

