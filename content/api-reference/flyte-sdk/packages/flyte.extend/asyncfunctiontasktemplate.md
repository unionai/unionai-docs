---
title: AsyncFunctionTaskTemplate
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# AsyncFunctionTaskTemplate

**Package:** `flyte.extend`

A task template that wraps an asynchronous functions. This is automatically created when an asynchronous function
is decorated with the task decorator.



```python
class AsyncFunctionTaskTemplate(
    name: str,
    interface: NativeInterface,
    short_name: str,
    task_type: str,
    task_type_version: int,
    image: Union[str, Image, Literal['auto']] | None,
    resources: Optional[Resources],
    cache: CacheRequest,
    interruptible: bool,
    retries: Union[int, RetryStrategy],
    reusable: Union[ReusePolicy, None],
    docs: Optional[Documentation],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    timeout: Optional[TimeoutType],
    pod_template: Optional[Union[str, PodTemplate]],
    report: bool,
    queue: Optional[str],
    debuggable: bool,
    parent_env: Optional[weakref.ReferenceType[TaskEnvironment]],
    parent_env_name: Optional[str],
    max_inline_io_bytes: int,
    triggers: Tuple[Trigger, ...],
    links: Tuple[Link, ...],
    _call_as_synchronous: bool,
    func: F,
    plugin_config: Optional[Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `interface` | `NativeInterface` | |
| `short_name` | `str` | |
| `task_type` | `str` | |
| `task_type_version` | `int` | |
| `image` | `Union[str, Image, Literal['auto']] \| None` | |
| `resources` | `Optional[Resources]` | |
| `cache` | `CacheRequest` | |
| `interruptible` | `bool` | |
| `retries` | `Union[int, RetryStrategy]` | |
| `reusable` | `Union[ReusePolicy, None]` | |
| `docs` | `Optional[Documentation]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `timeout` | `Optional[TimeoutType]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `report` | `bool` | |
| `queue` | `Optional[str]` | |
| `debuggable` | `bool` | |
| `parent_env` | `Optional[weakref.ReferenceType[TaskEnvironment]]` | |
| `parent_env_name` | `Optional[str]` | |
| `max_inline_io_bytes` | `int` | |
| `triggers` | `Tuple[Trigger, ...]` | |
| `links` | `Tuple[Link, ...]` | |
| `_call_as_synchronous` | `bool` | |
| `func` | `F` | |
| `plugin_config` | `Optional[Any]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `json_schema` | `None` | JSON schema for the task inputs, following the Flyte standard.  Delegates to NativeInterface.json_schema, which uses the type engine to produce a LiteralType per input and converts to JSON schema. |
| `source_file` | `None` | Returns the source file of the function, if available. This is useful for debugging and tracing. |

## Methods

| Method | Description |
|-|-|
| [`container_args()`](#container_args) | Returns the container args for the task. |
| [`execute()`](#execute) | This is the execute method that will be called when the task is invoked. |
| [`forward()`](#forward) | Think of this as a local execute method for your task. |


### container_args()

```python
def container_args(
    serialize_context: SerializationContext,
) -> List[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `SerializationContext` | |

### execute()

```python
def execute(
    args: *args,
    kwargs: **kwargs,
) -> R
```
This is the execute method that will be called when the task is invoked. It will call the actual function.
# TODO We may need to keep this as the bare func execute, and need a pre and post execute some other func.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### forward()

```python
def forward(
    args: *args,
    kwargs: **kwargs,
) -> Coroutine[Any, Any, R] | R
```
Think of this as a local execute method for your task. This function will be invoked by the __call__ method
when not in a Flyte task execution context.  See the implementation below for an example.



| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | :return: |

