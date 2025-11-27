---
title: flytekit.core.utils
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`AutoDeletingTempDir`](../flytekit.core.utils/autodeletingtempdir) | Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`ClassDecorator`](../flytekit.core.utils/classdecorator) | Abstract class for class decorators. |
| [`Directory`](../flytekit.core.utils/directory) |  |
| [`timeit`](../flytekit.core.utils/timeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

### Methods

| Method | Description |
|-|-|
| [`has_return_statement()`](#has_return_statement) |  |
| [`load_proto_from_file()`](#load_proto_from_file) |  |
| [`str2bool()`](#str2bool) | Convert a string to a boolean. |
| [`write_proto_to_file()`](#write_proto_to_file) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### has_return_statement()

```python
def has_return_statement(
    func: typing.Callable,
) -> bool
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable` | |

#### load_proto_from_file()

```python
def load_proto_from_file(
    pb2_type,
    path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_type` |  | |
| `path` |  | |

#### str2bool()

```python
def str2bool(
    value: typing.Optional[str],
) -> bool
```
Convert a string to a boolean. This is useful for parsing environment variables.


| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Optional[str]` | The string to convert to a boolean :return: the boolean value |

#### write_proto_to_file()

```python
def write_proto_to_file(
    proto,
    path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |
| `path` |  | |

