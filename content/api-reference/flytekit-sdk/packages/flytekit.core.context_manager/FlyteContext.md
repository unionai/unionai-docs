---
title: FlyteContext
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteContext

**Package:** `flytekit.core.context_manager`

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the `flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type | Description |
|-|-|-|
| `file_access` | `FileAccessProvider` | |
| `level` | `int` | |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` | |
| `compilation_state` | `Optional[CompilationState]` | |
| `execution_state` | `Optional[ExecutionState]` | |
| `serialization_settings` | `Optional[SerializationSettings]` | |
| `in_a_condition` | `bool` | |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` | |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` | |
| `worker_queue` | `Optional[Controller]` | |

## Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with {{< py_func_ref flytekit.current_context >}}


### enter_conditional_section()

```python
def enter_conditional_section()
```
### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

```python
with flytekit.new_context() as ctx:
    my_task(...)
ctx.get_deck()
```

OR if you wish to explicitly display

```python
from IPython import display
display(ctx.get_deck())
```


### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
### new_builder()

```python
def new_builder()
```
### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type | Description |
|-|-|-|
| `prefix` | `str` | |

### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type | Description |
|-|-|-|
| `working_dir` | `Optional[os.PathLike]` | |

### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `traceback.FrameSummary` | |

### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `c` | `SynchronousFlyteClient` | |

### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `c` | `CompilationState` | |

### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `es` | `ExecutionState` | |

### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `fa` | `FileAccessProvider` | |

### with_new_compilation_state()

```python
def with_new_compilation_state()
```
### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `OutputMetadataTracker` | |

### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `ss` | `SerializationSettings` | |

### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type | Description |
|-|-|-|
| `wq` | `Controller` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

