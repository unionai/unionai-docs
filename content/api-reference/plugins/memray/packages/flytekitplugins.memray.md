---
title: flytekitplugins.memray
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.memray

## Directory

### Classes

| Class | Description |
|-|-|
| [`memray_profiling`](.././flytekitplugins.memray#flytekitpluginsmemraymemray_profiling) |  |

## flytekitplugins.memray.memray_profiling

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


| Parameter | Type | Description |
|-|-|-|
| `task_function` | `typing.Optional[typing.Callable]` | The user function to be decorated. Defaults to None. |
| `native_traces` | `bool` | |
| `trace_python_allocators` | `bool` | |
| `follow_fork` | `bool` | |
| `memory_interval_ms` | `int` | How many milliseconds to wait between sending periodic resident set size updates. By default, every 10 milliseconds a record is written that contains the current timestamp and the total number of bytes of virtual memory allocated by the process. These records are used to create the graph of memory usage over time that appears at the top of the flame graph, for instance. This parameter lets you adjust the frequency between updates, though you shouldn't need to change it. |
| `memray_html_reporter` | `str` | The name of the memray reporter which generates an html report. Today there is only 'flamegraph' & 'table'. |
| `memray_reporter_args` | `typing.Optional[typing.List[str]]` | A list of arguments to pass to the reporter commands. See the [flamegraph](https://bloomberg.github.io/memray/flamegraph.html#reference) and [table](https://bloomberg.github.io/memray/table.html#cli-reference) docs for details on supported arguments. |

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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### generate_flytedeck_html()

```python
def generate_flytedeck_html(
    reporter,
    bin_filepath,
)
```
| Parameter | Type | Description |
|-|-|-|
| `reporter` |  | |
| `bin_filepath` |  | |

#### get_extra_config()

```python
def get_extra_config()
```
Get the config of the decorator.


