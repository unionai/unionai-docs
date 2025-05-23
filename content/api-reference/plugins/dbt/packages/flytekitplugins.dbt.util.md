---
title: flytekitplugins.dbt.util
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.dbt.util

## Directory

### Methods

| Method | Description |
|-|-|
| [`run_cli()`](#run_cli) | Execute a CLI command in a subprocess. |


## Methods

#### run_cli()

```python
def run_cli(
    cmd: typing.List[str],
) -> (<class 'int'>, typing.List[str])
```
Execute a CLI command in a subprocess

Parameters
----------
cmd : list of str
    Command to be executed.

Returns
-------
int
    Command's exit code.
list of str
    Logs produced by the command execution.


| Parameter | Type |
|-|-|
| `cmd` | `typing.List[str]` |

