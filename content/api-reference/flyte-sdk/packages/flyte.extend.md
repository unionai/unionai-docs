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


| Parameter | Type |
|-|-|
| `code_bundle` | {{< multiline >}}`flyte.models.CodeBundle`
doc: The code bundle to download.
:return: The code bundle with the downloaded path.
{{< /multiline >}} |

#### get_proto_resources()

```python
def get_proto_resources(
    resources: flyte._resources.Resources | None,
) -> typing.Optional[flyteidl2.core.tasks_pb2.Resources]
```
Get main resources IDL representation from the resources object



| Parameter | Type |
|-|-|
| `resources` | {{< multiline >}}`flyte._resources.Resources \| None`
doc: User facing Resources object containing potentially both requests and limits
:return: The given resources as requests and limits
{{< /multiline >}} |

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
| `kwargs` | {{< multiline >}}`**kwargs`
doc: 
:return:
{{< /multiline >}} |

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
| `kwargs` | {{< multiline >}}`**kwargs`
doc: 
:return:
{{< /multiline >}} |

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
| `short_name` | {{< multiline >}}`Optional[str]`
doc: Optional override for the short name of the task.
{{< /multiline >}} |
| `resources` | {{< multiline >}}`Optional[Resources]`
doc: Optional override for the resources to use for the task.
{{< /multiline >}} |
| `cache` | {{< multiline >}}`Optional[CacheRequest]`
doc: Optional override for the cache policy for the task.
{{< /multiline >}} |
| `retries` | {{< multiline >}}`Union[int, RetryStrategy]`
doc: Optional override for the number of retries for the task.
{{< /multiline >}} |
| `timeout` | {{< multiline >}}`Optional[TimeoutType]`
doc: Optional override for the timeout for the task.
{{< /multiline >}} |
| `reusable` | {{< multiline >}}`Union[ReusePolicy, Literal['off'], None]`
doc: Optional override for the reusability policy for the task.
{{< /multiline >}} |
| `env_vars` | {{< multiline >}}`Optional[Dict[str, str]]`
doc: Optional override for the environment variables to set for the task.
{{< /multiline >}} |
| `secrets` | {{< multiline >}}`Optional[SecretRequest]`
doc: Optional override for the secrets that will be injected into the task at runtime.
{{< /multiline >}} |
| `max_inline_io_bytes` | {{< multiline >}}`int \| None`
doc: Optional override for the maximum allowed size (in bytes) for all inputs and outputs
passed directly to the task.
{{< /multiline >}} |
| `pod_template` | {{< multiline >}}`Optional[Union[str, PodTemplate]]`
doc: Optional override for the pod template to use for the task.
{{< /multiline >}} |
| `queue` | {{< multiline >}}`Optional[str]`
doc: Optional override for the queue to use for the task.
{{< /multiline >}} |
| `interruptible` | `Optional[bool]` |
| `kwargs` | {{< multiline >}}`**kwargs`
doc: Additional keyword arguments for further overrides. Some fields like name, image, docs,
and interface cannot be overridden.

:return: A new TaskTemplate instance with the overridden parameters.
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `image` | `Image` |
| `builder` | `ImageBuildEngine.ImageBuilderType \| None` |
| `dry_run` | {{< multiline >}}`bool`
doc: Tell the builder to not actually build. Different builders will have different behaviors.
{{< /multiline >}} |
| `force` | {{< multiline >}}`bool`
doc: Skip the existence check. Normally if the image already exists we won't build it.
:return:
{{< /multiline >}} |

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
| Parameter | Type |
|-|-|
| `name` | {{< multiline >}}`str`
doc: Optional The name of the task (defaults to the function name)
{{< /multiline >}} |
| `interface` | `NativeInterface` |
| `short_name` | `str` |
| `task_type` | {{< multiline >}}`str`
doc: Router type for the task, this is used to determine how the task will be executed.
This is usually set to match with th execution plugin.
{{< /multiline >}} |
| `task_type_version` | `int` |
| `image` | {{< multiline >}}`Union[str, Image, Literal['auto']]`
doc: Optional The image to use for the task, if set to "auto" will use the default image for the python
version with flyte installed
{{< /multiline >}} |
| `resources` | {{< multiline >}}`Optional[Resources]`
doc: Optional The resources to use for the task
{{< /multiline >}} |
| `cache` | {{< multiline >}}`CacheRequest`
doc: Optional The cache policy for the task, defaults to auto, which will cache the results of the task.
{{< /multiline >}} |
| `interruptible` | {{< multiline >}}`bool`
doc: Optional The interruptible policy for the task, defaults to False, which means the task
will not be scheduled on interruptible nodes. If set to True, the task will be scheduled on interruptible nodes,
and the code should handle interruptions and resumptions.
{{< /multiline >}} |
| `retries` | {{< multiline >}}`Union[int, RetryStrategy]`
doc: Optional The number of retries for the task, defaults to 0, which means no retries.
{{< /multiline >}} |
| `reusable` | {{< multiline >}}`Union[ReusePolicy, None]`
doc: Optional The reusability policy for the task, defaults to None, which means the task environment
will not be reused across task invocations.
{{< /multiline >}} |
| `docs` | {{< multiline >}}`Optional[Documentation]`
doc: Optional The documentation for the task, if not provided the function docstring will be used.
{{< /multiline >}} |
| `env_vars` | {{< multiline >}}`Optional[Dict[str, str]]`
doc: Optional The environment variables to set for the task.
{{< /multiline >}} |
| `secrets` | {{< multiline >}}`Optional[SecretRequest]`
doc: Optional The secrets that will be injected into the task at runtime.
{{< /multiline >}} |
| `timeout` | {{< multiline >}}`Optional[TimeoutType]`
doc: Optional The timeout for the task.
{{< /multiline >}} |
| `pod_template` | {{< multiline >}}`Optional[Union[str, PodTemplate]]`
doc: Optional The pod template to use for the task.
{{< /multiline >}} |
| `report` | {{< multiline >}}`bool`
doc: Optional Whether to report the task execution to the Flyte console, defaults to False.
{{< /multiline >}} |
| `queue` | {{< multiline >}}`Optional[str]`
doc: Optional The queue to use for the task. If not provided, the default queue will be used.
{{< /multiline >}} |
| `debuggable` | {{< multiline >}}`bool`
doc: Optional Whether the task supports debugging capabilities, defaults to False.
{{< /multiline >}} |
| `parent_env` | `Optional[weakref.ReferenceType[TaskEnvironment]]` |
| `parent_env_name` | `Optional[str]` |
| `max_inline_io_bytes` | {{< multiline >}}`int`
doc: Maximum allowed size (in bytes) for all inputs and outputs passed directly to the task
(e.g., primitives, strings, dicts). Does not apply to files, directories, or dataframes.
{{< /multiline >}} |
| `triggers` | `Tuple[Trigger, ...]` |
| `_call_as_synchronous` | `bool` |

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
| `kwargs` | {{< multiline >}}`**kwargs`
doc: 
:return:
{{< /multiline >}} |

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
    sctx: SerializationContext,
) -> List[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type |
|-|-|
| `sctx` | `SerializationContext` |

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
    args,
    kwargs,
) -> Any
```
This is the pure python function that will be executed when the task is called.


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
| `kwargs` | {{< multiline >}}`**kwargs`
doc: 
:return:
{{< /multiline >}} |

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
| `short_name` | {{< multiline >}}`Optional[str]`
doc: Optional override for the short name of the task.
{{< /multiline >}} |
| `resources` | {{< multiline >}}`Optional[Resources]`
doc: Optional override for the resources to use for the task.
{{< /multiline >}} |
| `cache` | {{< multiline >}}`Optional[CacheRequest]`
doc: Optional override for the cache policy for the task.
{{< /multiline >}} |
| `retries` | {{< multiline >}}`Union[int, RetryStrategy]`
doc: Optional override for the number of retries for the task.
{{< /multiline >}} |
| `timeout` | {{< multiline >}}`Optional[TimeoutType]`
doc: Optional override for the timeout for the task.
{{< /multiline >}} |
| `reusable` | {{< multiline >}}`Union[ReusePolicy, Literal['off'], None]`
doc: Optional override for the reusability policy for the task.
{{< /multiline >}} |
| `env_vars` | {{< multiline >}}`Optional[Dict[str, str]]`
doc: Optional override for the environment variables to set for the task.
{{< /multiline >}} |
| `secrets` | {{< multiline >}}`Optional[SecretRequest]`
doc: Optional override for the secrets that will be injected into the task at runtime.
{{< /multiline >}} |
| `max_inline_io_bytes` | {{< multiline >}}`int \| None`
doc: Optional override for the maximum allowed size (in bytes) for all inputs and outputs
passed directly to the task.
{{< /multiline >}} |
| `pod_template` | {{< multiline >}}`Optional[Union[str, PodTemplate]]`
doc: Optional override for the pod template to use for the task.
{{< /multiline >}} |
| `queue` | {{< multiline >}}`Optional[str]`
doc: Optional override for the queue to use for the task.
{{< /multiline >}} |
| `interruptible` | `Optional[bool]` |
| `kwargs` | {{< multiline >}}`**kwargs`
doc: Additional keyword arguments for further overrides. Some fields like name, image, docs,
and interface cannot be overridden.

:return: A new TaskTemplate instance with the overridden parameters.
{{< /multiline >}} |

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
| `source_file` | `None` |  |

