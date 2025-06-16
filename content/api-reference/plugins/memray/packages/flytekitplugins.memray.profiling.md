---
title: flytekitplugins.memray.profiling
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.memray.profiling

## Directory

### Classes

| Class | Description |
|-|-|
| [`memray_profiling`](.././flytekitplugins.memray.profiling#flytekitpluginsmemrayprofilingmemray_profiling) | Abstract class for class decorators. |

## flytekitplugins.memray.profiling.memray_profiling

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
class memray_profiling(
    task_function: typing.Optional[typing.Callable],
    native_traces: bool,
    trace_python_allocators: bool,
    follow_fork: bool,
    memory_interval_ms: int,
    memray_html_reporter: str,
    memray_reporter_args: typing.Optional[typing.List[str]],
)
```
Memray profiling plugin.


| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `native_traces` | `bool` |
| `trace_python_allocators` | `bool` |
| `follow_fork` | `bool` |
| `memory_interval_ms` | `int` |
| `memray_html_reporter` | `str` |
| `memray_reporter_args` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called. |
| [`generate_flytedeck_html()`](#generate_flytedeck_html) |  |
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

#### generate_flytedeck_html()

```python
def generate_flytedeck_html(
    reporter,
    bin_filepath,
)
```
| Parameter | Type |
|-|-|
| `reporter` |  |
| `bin_filepath` |  |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


