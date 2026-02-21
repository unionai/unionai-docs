---
title: flytekit.core.utils
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`AutoDeletingTempDir`](.././flytekit.core.utils#flytekitcoreutilsautodeletingtempdir) | Creates a posix safe tempdir which is auto deleted once out of scope. |
| [`ClassDecorator`](.././flytekit.core.utils#flytekitcoreutilsclassdecorator) | Abstract class for class decorators. |
| [`Directory`](.././flytekit.core.utils#flytekitcoreutilsdirectory) |  |
| [`timeit`](.././flytekit.core.utils#flytekitcoreutilstimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

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

## flytekit.core.utils.AutoDeletingTempDir

Creates a posix safe tempdir which is auto deleted once out of scope



```python
class AutoDeletingTempDir(
    working_dir_prefix,
    tmp_dir,
    cleanup,
)
```
| Parameter | Type | Description |
|-|-|-|
| `working_dir_prefix` |  | |
| `tmp_dir` |  | |
| `cleanup` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`force_cleanup()`](#force_cleanup) |  |
| [`get_named_tempfile()`](#get_named_tempfile) |  |
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths. |


#### force_cleanup()

```python
def force_cleanup()
```
#### get_named_tempfile()

```python
def get_named_tempfile(
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

#### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths
:rtype: list[Text]


## flytekit.core.utils.ClassDecorator

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.



```python
class ClassDecorator(
    task_function,
    kwargs,
)
```
If the decorator is called with arguments, func will be None.
If the decorator is called without arguments, func will be function to be decorated.


| Parameter | Type | Description |
|-|-|-|
| `task_function` |  | |
| `kwargs` | `**kwargs` | |

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


## flytekit.core.utils.Directory

```python
class Directory(
    path,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`list_dir()`](#list_dir) | The list of absolute filepaths for all immediate sub-paths. |


#### list_dir()

```python
def list_dir()
```
The list of absolute filepaths for all immediate sub-paths
:rtype: list[Text]


## flytekit.core.utils.timeit

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
    # your code



```python
class timeit(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | A string that describes the wrapped code block or function being executed. |

