---
title: flyte.extras
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.extras

## Directory

### Classes

| Class | Description |
|-|-|
| [`ContainerTask`](.././flyte.extras#flyteextrascontainertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |

## flyte.extras.ContainerTask

This is an intermediate class that represents Flyte Tasks that run a container at execution time. This is the vast
majority of tasks - the typical ``@task`` decorated tasks; for instance, all run a container. An example of
something that doesn't run a container would be something like the Athena SQL task.



```python
class ContainerTask(
    name: str,
    image: typing.Union[str, flyte._image.Image],
    command: typing.List[str],
    inputs: typing.Optional[typing.Dict[str, typing.Type]],
    arguments: typing.Optional[typing.List[str]],
    outputs: typing.Optional[typing.Dict[str, typing.Type]],
    input_data_dir: str | pathlib._local.Path,
    output_data_dir: str | pathlib._local.Path,
    metadata_format: typing.Literal['JSON', 'YAML', 'PROTO'],
    local_logs: bool,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the task |
| `image` | `typing.Union[str, flyte._image.Image]` | The container image to use for the task. This can be a string or an Image object. |
| `command` | `typing.List[str]` | The command to run in the container. This can be a list of strings or a single string. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` | The inputs to the task. This is a dictionary of input names to types. |
| `arguments` | `typing.Optional[typing.List[str]]` | The arguments to pass to the command. This is a list of strings. |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Type]]` | The outputs of the task. This is a dictionary of output names to types. |
| `input_data_dir` | `str \| pathlib._local.Path` | The directory where the input data is stored. This is a string or a Path object. |
| `output_data_dir` | `str \| pathlib._local.Path` | The directory where the output data is stored. This is a string or a Path object. |
| `metadata_format` | `typing.Literal['JSON', 'YAML', 'PROTO']` | The format of the output file. This can be "JSON", "YAML", or "PROTO". |
| `local_logs` | `bool` | If True, logs will be printed to the console in the local execution. |
| `kwargs` | `**kwargs` | |

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
    sctx: flyte.models.SerializationContext,
) -> typing.List[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `flyte.models.SerializationContext` | |

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
    sctx: flyte.models.SerializationContext,
) -> flyteidl2.core.tasks_pb2.DataLoadingConfig
```
This configuration allows executing raw containers in Flyte using the Flyte CoPilot system
Flyte CoPilot, eliminates the needs of sdk inside the container. Any inputs required by the users container
are side-loaded in the input_path
Any outputs generated by the user container - within output_path are automatically uploaded


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `flyte.models.SerializationContext` | |

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
This is the pure python function that will be executed when the task is called.


| Parameter | Type | Description |
|-|-|-|
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

