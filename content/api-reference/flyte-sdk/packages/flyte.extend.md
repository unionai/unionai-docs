---
title: flyte.extend
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.extend

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncFunctionTaskTemplate`](.././flyte.extend#flyteextendasyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`ImageBuildEngine`](.././flyte.extend#flyteextendimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`TaskTemplate`](.././flyte.extend#flyteextendtasktemplate) | Task template is a template for a task that can be executed. |

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


| Parameter | Type | Description |
|-|-|-|
| `code_bundle` | `flyte.models.CodeBundle` | The code bundle to download. :return: The code bundle with the downloaded path. |

#### get_proto_resources()

```python
def get_proto_resources(
    resources: flyte._resources.Resources | None,
) -> typing.Optional[flyteidl2.core.tasks_pb2.Resources]
```
Get main resources IDL representation from the resources object



| Parameter | Type | Description |
|-|-|-|
| `resources` | `flyte._resources.Resources \| None` | User facing Resources object containing potentially both requests and limits :return: The given resources as requests and limits |

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
| Parameter | Type | Description |
|-|-|-|
| `primary_container_name` | `str` | |
| `requests` | `typing.Optional[flyte._resources.Resources]` | |
| `limits` | `typing.Optional[flyte._resources.Resources]` | |
| `k8s_gpu_resource_key` | `str` | |

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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `interface` | `NativeInterface` | |
| `short_name` | `str` | |
| `task_type` | `str` | |
| `task_type_version` | `int` | |
| `image` | `Union[str, Image, Literal['auto']]` | |
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
| `_call_as_synchronous` | `bool` | |
| `func` | `F` | |
| `plugin_config` | `Optional[Any]` | |

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
def my_legacy_task(x: int) -&gt; int:
    return x

@env.task
async def my_new_parent_task(n: int) -&gt; List[int]:
    collect = []
    for x in range(n):
        collect.append(my_legacy_task.aio(x))
    return asyncio.gather(*collect)
```


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | :return: |

#### config()

```python
def config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

#### container_args()

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

#### custom_config()

```python
def custom_config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

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


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

#### execute()

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

#### forward()

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



| Parameter | Type | Description |
|-|-|-|
| `short_name` | `Optional[str]` | Optional override for the short name of the task. |
| `resources` | `Optional[Resources]` | Optional override for the resources to use for the task. |
| `cache` | `Optional[CacheRequest]` | Optional override for the cache policy for the task. |
| `retries` | `Union[int, RetryStrategy]` | Optional override for the number of retries for the task. |
| `timeout` | `Optional[TimeoutType]` | Optional override for the timeout for the task. |
| `reusable` | `Union[ReusePolicy, Literal['off'], None]` | Optional override for the reusability policy for the task. |
| `env_vars` | `Optional[Dict[str, str]]` | Optional override for the environment variables to set for the task. |
| `secrets` | `Optional[SecretRequest]` | Optional override for the secrets that will be injected into the task at runtime. |
| `max_inline_io_bytes` | `int \| None` | Optional override for the maximum allowed size (in bytes) for all inputs and outputs passed directly to the task. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional override for the pod template to use for the task. |
| `queue` | `Optional[str]` | Optional override for the queue to use for the task. |
| `interruptible` | `Optional[bool]` | |
| `kwargs` | `**kwargs` | Additional keyword arguments for further overrides. Some fields like name, image, docs, and interface cannot be overridden.  :return: A new TaskTemplate instance with the overridden parameters. |

#### post()

```python
def post(
    return_vals: Any,
) -> Any
```
This is the postexecute function that will be
called after the task is executed


| Parameter | Type | Description |
|-|-|-|
| `return_vals` | `Any` | |

#### pre()

```python
def pre(
    args,
    kwargs,
) -> Dict[str, Any]
```
This is the preexecute function that will be
called before the task is executed


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### sql()

```python
def sql(
    sctx: SerializationContext,
) -> Optional[str]
```
Returns the SQL for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `native_interface` | `None` |  |
| `source_file` | `None` | Returns the source file of the function, if available. This is useful for debugging and tracing. |

## flyte.extend.ImageBuildEngine

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


### Methods

| Method | Description |
|-|-|
| [`build()`](#build) | Build the image. |


#### build()

```python
def build(
    image: Image,
    builder: ImageBuildEngine.ImageBuilderType | None,
    dry_run: bool,
    force: bool,
) -> str
```
Build the image. Images to be tagged with latest will always be built. Otherwise, this engine will check the
registry to see if the manifest exists.



| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | |
| `builder` | `ImageBuildEngine.ImageBuilderType \| None` | |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check. Normally if the image already exists we won't build it. :return: |

## flyte.extend.TaskTemplate

Task template is a template for a task that can be executed. It defines various parameters for the task, which
can be defined statically at the time of task definition or dynamically at the time of task invocation using
the override method.

Example usage:
```python
@task(name="my_task", image="my_image", resources=Resources(cpu="1", memory="1Gi"))
def my_task():
    pass
```



```python
class TaskTemplate(
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
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Optional The name of the task (defaults to the function name) |
| `interface` | `NativeInterface` | |
| `short_name` | `str` | |
| `task_type` | `str` | Router type for the task, this is used to determine how the task will be executed. This is usually set to match with th execution plugin. |
| `task_type_version` | `int` | |
| `image` | `Union[str, Image, Literal['auto']]` | Optional The image to use for the task, if set to "auto" will use the default image for the python version with flyte installed |
| `resources` | `Optional[Resources]` | Optional The resources to use for the task |
| `cache` | `CacheRequest` | Optional The cache policy for the task, defaults to auto, which will cache the results of the task. |
| `interruptible` | `bool` | Optional The interruptible policy for the task, defaults to False, which means the task will not be scheduled on interruptible nodes. If set to True, the task will be scheduled on interruptible nodes, and the code should handle interruptions and resumptions. |
| `retries` | `Union[int, RetryStrategy]` | Optional The number of retries for the task, defaults to 0, which means no retries. |
| `reusable` | `Union[ReusePolicy, None]` | Optional The reusability policy for the task, defaults to None, which means the task environment will not be reused across task invocations. |
| `docs` | `Optional[Documentation]` | Optional The documentation for the task, if not provided the function docstring will be used. |
| `env_vars` | `Optional[Dict[str, str]]` | Optional The environment variables to set for the task. |
| `secrets` | `Optional[SecretRequest]` | Optional The secrets that will be injected into the task at runtime. |
| `timeout` | `Optional[TimeoutType]` | Optional The timeout for the task. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional The pod template to use for the task. |
| `report` | `bool` | Optional Whether to report the task execution to the Flyte console, defaults to False. |
| `queue` | `Optional[str]` | Optional The queue to use for the task. If not provided, the default queue will be used. |
| `debuggable` | `bool` | Optional Whether the task supports debugging capabilities, defaults to False. |
| `parent_env` | `Optional[weakref.ReferenceType[TaskEnvironment]]` | |
| `parent_env_name` | `Optional[str]` | |
| `max_inline_io_bytes` | `int` | Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task (e.g., primitives, strings, dicts). Does not apply to files, directories, or dataframes. |
| `triggers` | `Tuple[Trigger, ...]` | |
| `_call_as_synchronous` | `bool` | |

### Methods

| Method | Description |
|-|-|
| [`aio()`](#aio) | The aio function allows executing "sync" tasks, in an async context. |
| [`config()`](#config) | Returns additional configuration for the task. |
| [`container_args()`](#container_args) | Returns the container args for the task. |
| [`custom_config()`](#custom_config) | Returns additional configuration for the task. |
| [`data_loading_config()`](#data_loading_config) | This configuration allows executing raw containers in Flyte using the Flyte CoPilot system. |
| [`execute()`](#execute) | This is the pure python function that will be executed when the task is called. |
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
def my_legacy_task(x: int) -&gt; int:
    return x

@env.task
async def my_new_parent_task(n: int) -&gt; List[int]:
    collect = []
    for x in range(n):
        collect.append(my_legacy_task.aio(x))
    return asyncio.gather(*collect)
```


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | :return: |

#### config()

```python
def config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

#### container_args()

```python
def container_args(
    sctx: SerializationContext,
) -> List[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

#### custom_config()

```python
def custom_config(
    sctx: SerializationContext,
) -> Dict[str, str]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

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


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

#### execute()

```python
def execute(
    args,
    kwargs,
) -> Any
```
This is the pure python function that will be executed when the task is called.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### forward()

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



| Parameter | Type | Description |
|-|-|-|
| `short_name` | `Optional[str]` | Optional override for the short name of the task. |
| `resources` | `Optional[Resources]` | Optional override for the resources to use for the task. |
| `cache` | `Optional[CacheRequest]` | Optional override for the cache policy for the task. |
| `retries` | `Union[int, RetryStrategy]` | Optional override for the number of retries for the task. |
| `timeout` | `Optional[TimeoutType]` | Optional override for the timeout for the task. |
| `reusable` | `Union[ReusePolicy, Literal['off'], None]` | Optional override for the reusability policy for the task. |
| `env_vars` | `Optional[Dict[str, str]]` | Optional override for the environment variables to set for the task. |
| `secrets` | `Optional[SecretRequest]` | Optional override for the secrets that will be injected into the task at runtime. |
| `max_inline_io_bytes` | `int \| None` | Optional override for the maximum allowed size (in bytes) for all inputs and outputs passed directly to the task. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Optional override for the pod template to use for the task. |
| `queue` | `Optional[str]` | Optional override for the queue to use for the task. |
| `interruptible` | `Optional[bool]` | |
| `kwargs` | `**kwargs` | Additional keyword arguments for further overrides. Some fields like name, image, docs, and interface cannot be overridden.  :return: A new TaskTemplate instance with the overridden parameters. |

#### post()

```python
def post(
    return_vals: Any,
) -> Any
```
This is the postexecute function that will be
called after the task is executed


| Parameter | Type | Description |
|-|-|-|
| `return_vals` | `Any` | |

#### pre()

```python
def pre(
    args,
    kwargs,
) -> Dict[str, Any]
```
This is the preexecute function that will be
called before the task is executed


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### sql()

```python
def sql(
    sctx: SerializationContext,
) -> Optional[str]
```
Returns the SQL for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `native_interface` | `None` |  |
| `source_file` | `None` |  |

