---
title: Snowflake
version: 2.0.0b57
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Snowflake

**Package:** `flyteplugins.snowflake`

```python
class Snowflake(
    name: str,
    query_template: str,
    plugin_config: flyteplugins.snowflake.task.SnowflakeConfig,
    inputs: typing.Optional[typing.Dict[str, typing.Type]],
    output_dataframe_type: typing.Optional[typing.Type],
    secret_group: typing.Optional[str],
    snowflake_private_key: typing.Optional[str],
    snowflake_private_key_passphrase: typing.Optional[str],
    batch: bool,
    kwargs,
)
```
Task to run parameterized SQL queries against Snowflake.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of this task. |
| `query_template` | `str` | The actual query to run. This can be parameterized using Python's printf-style string formatting with named parameters (e.g. %(param_name)s). |
| `plugin_config` | `flyteplugins.snowflake.task.SnowflakeConfig` | `SnowflakeConfig` object containing connection metadata. |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Type]]` | Name and type of inputs specified as a dictionary. |
| `output_dataframe_type` | `typing.Optional[typing.Type]` | If some data is produced by this query, then you can specify the output dataframe type. |
| `secret_group` | `typing.Optional[str]` | Optional group for secrets in the secret store. The environment variable name is auto-generated from ``{secret_group}_{key}``, uppercased with hyphens replaced by underscores. If omitted, the key alone is used. |
| `snowflake_private_key` | `typing.Optional[str]` | The secret key for the Snowflake private key (key-pair auth). |
| `snowflake_private_key_passphrase` | `typing.Optional[str]` | The secret key for the private key passphrase (if encrypted). |
| `batch` | `bool` | When True, list inputs are expanded into a multi-row VALUES clause. The query_template should contain a single ``VALUES (%(col)s, ...)`` placeholder and each input should be a list of equal length. |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `native_interface` | `None` |  |
| `source_file` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`aio()`](#aio) | The aio function allows executing "sync" tasks, in an async context. |
| [`config()`](#config) | Returns additional configuration for the task. |
| [`container_args()`](#container_args) | Returns the container args for the task. |
| [`custom_config()`](#custom_config) | Returns additional configuration for the task. |
| [`data_loading_config()`](#data_loading_config) | This configuration allows executing raw containers in Flyte using the Flyte CoPilot system. |
| [`execute()`](#execute) |  |
| [`forward()`](#forward) | Think of this as a local execute method for your task. |
| [`override()`](#override) | Override various parameters of the task template. |
| [`post()`](#post) | This is the postexecute function that will be. |
| [`pre()`](#pre) | This is the preexecute function that will be. |
| [`sql()`](#sql) | Returns the SQL for the task. |


### aio()

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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | :return: |

### config()

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

### container_args()

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

### custom_config()

```python
def custom_config(
    sctx: flyte.models.SerializationContext,
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `flyte.models.SerializationContext` | |

### data_loading_config()

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

### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
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

### override()

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
    links: Tuple[Link, ...],
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
| `interruptible` | `Optional[bool]` | Optional override for the interruptible policy for the task. |
| `links` | `Tuple[Link, ...]` | Optional override for the Links associated with the task. |
| `kwargs` | `**kwargs` | Additional keyword arguments for further overrides. Some fields like name, image, docs, and interface cannot be overridden.  :return: A new TaskTemplate instance with the overridden parameters. |

### post()

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

### pre()

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

### sql()

```python
def sql(
    sctx: flyte.models.SerializationContext,
) -> typing.Optional[str]
```
Returns the SQL for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `flyte.models.SerializationContext` | |

