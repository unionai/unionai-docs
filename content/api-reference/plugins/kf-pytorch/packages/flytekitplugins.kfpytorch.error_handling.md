---
title: flytekitplugins.kfpytorch.error_handling
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.kfpytorch.error_handling

Handle errors in elastic training jobs.
## Directory

### Methods

| Method | Description |
|-|-|
| [`create_recoverable_error_file()`](#create_recoverable_error_file) | Create a file to signal to the agent process that an exception in the worker process is recoverable. |
| [`is_recoverable_worker_error()`](#is_recoverable_worker_error) | Check if the error in the worker process is recoverable. |


### Variables

| Property | Type | Description |
|-|-|-|
| `RECOVERABLE_ERROR_FILE_NAME` | `str` |  |

## Methods

#### create_recoverable_error_file()

```python
def create_recoverable_error_file()
```
Create a file to signal to the agent process that an exception in the worker process is recoverable.

Torch's `elastic_launch` gives the agent process access to exceptions raised in the worker
processes only as strings in an error file. Instead of parsing this error file in the agent process for
the string `FlyteRecoverableException` - which would not detect exceptions inheriting from
`FlyteRecoverableException` - we create a file in the worker process to signal to the agent process
that the exception is recoverable. The file is created in the directory where the default
torch elastic error file is written.

Raises:
    ValueError: If the environment variable `TORCHELASTIC_ERROR_FILE` is not set.


#### is_recoverable_worker_error()

```python
def is_recoverable_worker_error(
    failure,
) -> bool
```
Check if the error in the worker process is recoverable.

The error is considered recoverable if the directory containing the torch elastic error file contains
a file named `recoverable_error`.



| Parameter | Type |
|-|-|
| `failure` |  |

