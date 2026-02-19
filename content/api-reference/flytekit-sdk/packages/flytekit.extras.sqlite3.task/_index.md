---
title: flytekit.extras.sqlite3.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.sqlite3.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`SQLite3Config`](../flytekit.extras.sqlite3.task/sqlite3config) | Use this configuration to configure if sqlite3 files that should be loaded by the task. |
| [`SQLite3Task`](../flytekit.extras.sqlite3.task/sqlite3task) | Run client side SQLite3 queries that optionally return a FlyteSchema object. |
| [`SQLite3TaskExecutor`](../flytekit.extras.sqlite3.task/sqlite3taskexecutor) |  |

### Methods

| Method | Description |
|-|-|
| [`unarchive_file()`](#unarchive_file) | Unarchive given archive and returns the unarchived file name. |


## Methods

#### unarchive_file()

```python
def unarchive_file(
    local_path: str,
    to_dir: str,
)
```
Unarchive given archive and returns the unarchived file name. It is expected that only one file is unarchived.
More than one file or 0 files will result in a ``RuntimeError``


| Parameter | Type | Description |
|-|-|-|
| `local_path` | `str` | |
| `to_dir` | `str` | |

