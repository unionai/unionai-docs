---
title: flyte.extend
version: 2.0.0b28
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.extend

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncFunctionTaskTemplate`](.././flyte.extend#flyteextendasyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |

### Methods

| Method | Description |
|-|-|
| [`download_code_bundle()`](#download_code_bundle) | Downloads the code bundle if it is not already downloaded. |
| [`get_proto_resources()`](#get_proto_resources) | Get main resources IDL representation from the resources object. |
| [`is_initialized()`](#is_initialized) | Check if the system has been initialized. |
| [`pod_spec_from_resources()`](#pod_spec_from_resources) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `PRIMARY_CONTAINER_DEFAULT_NAME` | `str` |  |
| `TaskPluginRegistry` | `_Registry` |  |

## Methods

#### download_code_bundle()

```python
def download_code_bundle(
    code_bundle: flyte.models.CodeBundle,
) -> flyte.models.CodeBundle
```
Downloads the code bundle if it is not already downloaded.


| Parameter | Type |
|-|-|
| `code_bundle` | `flyte.models.CodeBundle` |

#### get_proto_resources()

```python
def get_proto_resources(
    resources: flyte._resources.Resources | None,
) -> typing.Optional[flyteidl2.core.tasks_pb2.Resources]
```
Get main resources IDL representation from the resources object



| Parameter | Type |
|-|-|
| `resources` | `flyte._resources.Resources \| None` |

#### is_initialized()

```python
def is_initialized()
```
Check if the system has been initialized.

:return: True if initialized, False otherwise


#### pod_spec_from_resources()

```python
def pod_spec_from_resources(
    primary_container_name: str,
    requests: typing.Optional[flyte._resources.Resources],
    limits: typing.Optional[flyte._resources.Resources],
    k8s_gpu_resource_key: str,
) -> V1PodSpec
```
| Parameter | Type |
|-|-|
| `primary_container_name` | `str` |
| `requests` | `typing.Optional[flyte._resources.Resources]` |
| `limits` | `typing.Optional[flyte._resources.Resources]` |
| `k8s_gpu_resource_key` | `str` |

## flyte.extend.AsyncFunctionTaskTemplate

A task template that wraps an asynchronous functions. This is automatically created when an asynchronous function
is decorated with the task decorator.


```python
class AsyncFunctionTaskTemplate(
    name: str,
    interface: NativeInterface,
    short_name: str,
    task_type: str,
    task_type_version: int,
    image: Union[str, Image, Literal['auto']],
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
    _call_as_synchronous: bool,
    func: F,
    plugin_config: Optional[Any],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `interface` | `NativeInterface` |
| `short_name` | `str` |
| `task_type` | `str` |
| `task_type_version` | `int` |
| `image` | `Union[str, Image, Literal['auto']]` |
| `resources` | `Optional[Resources]` |
| `cache` | `CacheRequest` |
| `interruptible` | `bool` |
| `retries` | `Union[int, RetryStrategy]` |
| `reusable` | `Union[ReusePolicy, None]` |
| `docs` | `Optional[Documentation]` |
| `env_vars` | `Optional[Dict[str, str]]` |
| `secrets` | `Optional[SecretRequest]` |
| `timeout` | `Optional[TimeoutType]` |
| `pod_template` | `Optional[Union[str, PodTemplate]]` |
| `report` | `bool` |
| `queue` | `Optional[str]` |
| `debuggable` | `bool` |
| `parent_env` | `Optional[weakref.ReferenceType[TaskEnvironment]]` |
| `parent_env_name` | `Optional[str]` |
| `max_inline_io_bytes` | `int` |
| `triggers` | `Tuple[Trigger, ...]` |
| `_call_as_synchronous` | `bool` |
| `func` | `F` |
| `plugin_config` | `Optional[Any]` |

### Methods

| Method | Description |
|-|-|
| [`aio()`](#aio) | The aio function allows executing "sync" tasks, in an async context. |
| [`config()`](#config) | Returns additional configuration for the task. |
| [`container_args()`](#container_args) | Returns the container args for the task. |
| [`custom_config()`](#custom_config) | Returns additional configuration for the task. |
| [`data_loading_config()`](#data_loading_config) | This configuration allows executing raw containers in Flyte using the Flyte CoPilot system. |
| [`execute()`](#execute) | This is the execute method that will be called when the task is invoked. |
| [`forward()`](#forward) | Think of this as a local execute method for your task. |
| [`override()`](#override) | Override various parameters of the task template. |
| [`post()`](#post) | This is the postexecute function that will be. |
| [`pre()`](#pre) | This is the preexecute function that will be. |
| [`sql()`](#sql) | Returns the SQL for the task. |


#### aio()

```python
def aio(
    args: *args,
    kwargs: **kwargs,
) -> Coroutine[Any, Any, R] | R
```
The aio function allows executing "sync" tasks, in an async context. This helps with migrating v1 defined sync
tasks to be used within an asyncio parent task.
This function will also re-raise exceptions from the underlying task.

Example:
```python
@env.task
def my_legacy_task(x: int) -> int:
    return x

@env.task
async def my_new_parent_task(n: int) -> List[int]:
    collect = []
    for x in range(n):
        collect.append(my_legacy_task.aio(x))
    return asyncio.gather(*collect)
```


| Parameter | Type |
|-|-|
| `args` | `*args` |
| `kwargs` | `**kwargs` |

#### config()

```python
def config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type |
|-|-|
| `sctx` | `SerializationContext` |

#### container_args()

```python
def container_args(
    serialize_context: SerializationContext,
) -> List[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type |
|-|-|
| `serialize_context` | `SerializationContext` |

#### custom_config()

```python
def custom_config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type |
|-|-|
| `sctx` | `SerializationContext` |

#### data_loading_config()

```python
def data_loading_config(
    sctx: SerializationContext,
) -> DataLoadingConfig
```
This configuration allows executing raw containers in Flyte using the Flyte CoPilot system
Flyte CoPilot, eliminates the needs of sdk inside the container. Any inputs required by the users container
are side-loaded in the input_path
Any outputs generated by the user container - within output_path are automatically uploaded


| Parameter | Type |
|-|-|
| `sctx` | `SerializationContext` |

#### execute()

```python
def execute(
    args: *args,
    kwargs: **kwargs,
) -> R
```
This is the execute method that will be called when the task is invoked. It will call the actual function.
# TODO We may need to keep this as the bare func execute, and need a pre and post execute some other func.


| Parameter | Type |
|-|-|
| `args` | `*args` |
| `kwargs` | `**kwargs` |

#### forward()

```python
def forward(
    args: *args,
    kwargs: **kwargs,
) -> Coroutine[Any, Any, R] | R
```
Think of this as a local execute method for your task. This function will be invoked by the __call__ method
when not in a Flyte task execution context.  See the implementation below for an example.



| Parameter | Type |
|-|-|
| `args` | `*args` |
| `kwargs` | `**kwargs` |

#### override()

```python
def override(
    short_name: Optional[str],
    resources: Optional[Resources],
    cache: Optional[CacheRequest],
    retries: Union[int, RetryStrategy],
    timeout: Optional[TimeoutType],
    reusable: Union[ReusePolicy, Literal['off'], None],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    max_inline_io_bytes: int | None,
    pod_template: Optional[Union[str, PodTemplate]],
    queue: Optional[str],
    interruptible: Optional[bool],
    kwargs: **kwargs,
) -> TaskTemplate
```
Override various parameters of the task template. This allows for dynamic configuration of the task
when it is called, such as changing the image, resources, cache policy, etc.



| Parameter | Type |
|-|-|
| `short_name` | `Optional[str]` |
| `resources` | `Optional[Resources]` |
| `cache` | `Optional[CacheRequest]` |
| `retries` | `Union[int, RetryStrategy]` |
| `timeout` | `Optional[TimeoutType]` |
| `reusable` | `Union[ReusePolicy, Literal['off'], None]` |
| `env_vars` | `Optional[Dict[str, str]]` |
| `secrets` | `Optional[SecretRequest]` |
| `max_inline_io_bytes` | `int \| None` |
| `pod_template` | `Optional[Union[str, PodTemplate]]` |
| `queue` | `Optional[str]` |
| `interruptible` | `Optional[bool]` |
| `kwargs` | `**kwargs` |

#### post()

```python
def post(
    return_vals: Any,
) -> Any
```
This is the postexecute function that will be
called after the task is executed


| Parameter | Type |
|-|-|
| `return_vals` | `Any` |

#### pre()

```python
def pre(
    args,
    kwargs,
) -> Dict[str, Any]
```
This is the preexecute function that will be
called before the task is executed


| Parameter | Type |
|-|-|
| `args` | `*args` |
| `kwargs` | `**kwargs` |

#### sql()

```python
def sql(
    sctx: SerializationContext,
) -> Optional[str]
```
Returns the SQL for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type |
|-|-|
| `sctx` | `SerializationContext` |

### Properties

| Property | Type | Description |
|-|-|-|
| `native_interface` | `None` |  |
| `source_file` | `None` | {{< multiline >}}Returns the source file of the function, if available. This is useful for debugging and tracing.
{{< /multiline >}} |

