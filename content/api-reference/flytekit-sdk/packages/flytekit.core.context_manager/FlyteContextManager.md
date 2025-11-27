---
title: FlyteContextManager
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteContextManager

**Package:** `flytekit.core.context_manager`

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

```python
FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
    pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()
```


## Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` | |

### current_context()

```python
def current_context()
```
### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
) -> traceback.FrameSummary
```
| Parameter | Type | Description |
|-|-|-|
| `limit` |  | |

### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


### pop_context()

```python
def pop_context()
```
### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
) -> FlyteContext
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `f` | `Optional[traceback.FrameSummary]` | |

### size()

```python
def size()
```
### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `b` | `FlyteContext.Builder` | |

