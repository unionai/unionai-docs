---
title: flytekit.interactive.vscode_lib.decorator
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interactive.vscode_lib.decorator

## Directory

### Classes

| Class | Description |
|-|-|
| [`ClassDecorator`](.././flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorclassdecorator) | Abstract class for class decorators. |
| [`FlyteContextManager`](.././flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`VscodeConfig`](.././flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscodeconfig) | VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths. |
| [`vscode`](.././flytekit.interactive.vscode_lib.decorator#flytekitinteractivevscode_libdecoratorvscode) | Abstract class for class decorators. |

## flytekit.interactive.vscode_lib.decorator.ClassDecorator

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
def ClassDecorator(
    task_function,
    kwargs,
):
```
If the decorator is called with arguments, func will be None.
If the decorator is called without arguments, func will be function to be decorated.


| Parameter | Type |
|-|-|
| `task_function` |  |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator |


#### execute()

```python
def execute(
    args,
    kwargs,
):
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


## flytekit.interactive.vscode_lib.decorator.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) | None |
| [`current_context()`](#current_context) | None |
| [`get_origin_stackframe()`](#get_origin_stackframe) | None |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context |
| [`pop_context()`](#pop_context) | None |
| [`push_context()`](#push_context) | None |
| [`size()`](#size) | None |
| [`with_context()`](#with_context) | None |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
):
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
):
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
):
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.interactive.vscode_lib.decorator.VscodeConfig

VscodeConfig is the config contains default URLs of the VSCode server and extension remote paths.



```python
def VscodeConfig(
    code_server_remote_paths: typing.Optional[typing.Dict[str, str]],
    code_server_dir_names: typing.Optional[typing.Dict[str, str]],
    extension_remote_paths: typing.Optional[typing.List[str]],
):
```
| Parameter | Type |
|-|-|
| `code_server_remote_paths` | `typing.Optional[typing.Dict[str, str]]` |
| `code_server_dir_names` | `typing.Optional[typing.Dict[str, str]]` |
| `extension_remote_paths` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`add_extensions()`](#add_extensions) | Add additional extensions to the extension_remote_paths list |


#### add_extensions()

```python
def add_extensions(
    extensions: typing.Union[str, typing.List[str]],
):
```
Add additional extensions to the extension_remote_paths list.


| Parameter | Type |
|-|-|
| `extensions` | `typing.Union[str, typing.List[str]]` |

## flytekit.interactive.vscode_lib.decorator.vscode

Abstract class for class decorators.
We can attach config on the decorator class and use it in the upper level.


```python
def vscode(
    task_function: typing.Optional[typing.Callable],
    max_idle_seconds: typing.Optional[int],
    port: int,
    enable: bool,
    run_task_first: bool,
    pre_execute: typing.Optional[typing.Callable],
    post_execute: typing.Optional[typing.Callable],
    config: typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig],
):
```
vscode decorator modifies a container to run a VSCode server:
1. Overrides the user function with a VSCode setup function.
2. Download vscode server and extension from remote to local.
3. Prepare the interactive debugging Python script and launch.json.
4. Prepare task resumption script.
5. Launches and monitors the VSCode server.
6. Register signal handler for task resumption.
7. Terminates if the server is idle for a set duration or user trigger task resumption.



| Parameter | Type |
|-|-|
| `task_function` | `typing.Optional[typing.Callable]` |
| `max_idle_seconds` | `typing.Optional[int]` |
| `port` | `int` |
| `enable` | `bool` |
| `run_task_first` | `bool` |
| `pre_execute` | `typing.Optional[typing.Callable]` |
| `post_execute` | `typing.Optional[typing.Callable]` |
| `config` | `typing.Optional[flytekit.interactive.vscode_lib.config.VscodeConfig]` |

### Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | This method will be called when the decorated function is called |
| [`get_extra_config()`](#get_extra_config) | Get the config of the decorator |


#### execute()

```python
def execute(
    args,
    kwargs,
):
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


