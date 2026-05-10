---
title: NotebookTask
version: 2.2.2
variants: +flyte +union
layout: py_api
---

# NotebookTask

**Package:** `flyteplugins.papermill`

A Flyte task that executes a Jupyter notebook via Papermill.

The notebook receives task inputs as parameters (injected into the cell
tagged ``parameters``) and produces outputs via ``record_outputs()``
called inside the notebook.

Inside *notebooks/analyze.ipynb*::

    from flyteplugins.papermill import record_outputs

    result = x + y  # x, y injected by papermill
    record_outputs(result=int(result))

You can also call other Flyte tasks from within the notebook — just
import and call them as usual::

    from my_tasks import expensive_task

    intermediate = await expensive_task(data=x)  # submitted to Flyte when running remotely
    record_outputs(result=intermediate)

Spark example::

    from flyteplugins.papermill import NotebookTask
    from flyteplugins.spark import Spark

    spark_nb = NotebookTask(
        name="spark_analyze",
        notebook_path="notebooks/spark_analysis.ipynb",
        task_environment=env,
        plugin_config=Spark(spark_conf={...}),
        inputs={"path": str},
        outputs={"count": int},
    )



## Parameters

```python
class NotebookTask(
    name: str,
    notebook_path: str,
    task_environment: TaskEnvironment,
    plugin_config: Optional[Any],
    inputs: Optional[dict[str, Type]],
    outputs: Optional[dict[str, Type]],
    kernel_name: Optional[str],
    engine_name: Optional[str],
    log_output: bool,
    start_timeout: int,
    execution_timeout: Optional[int],
    report_mode: bool,
    request_save_on_cell_execute: bool,
    progress_bar: bool,
    language: Optional[str],
    engine_kwargs: Optional[dict[str, Any]],
    output_notebooks: bool,
    kwargs: **kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Task name. |
| `notebook_path` | `str` | Path to the ``.ipynb`` file (relative to the caller's file or absolute). |
| `task_environment` | `TaskEnvironment` | The ``TaskEnvironment`` this task belongs to. Required for remote execution. |
| `plugin_config` | `Optional[Any]` | Plugin configuration (e.g. ``Spark(...)``). Sets the task type and execution environment accordingly. |
| `inputs` | `Optional[dict[str, Type]]` | Mapping of input names to Python types. |
| `outputs` | `Optional[dict[str, Type]]` | Mapping of output names to Python types. |
| `kernel_name` | `Optional[str]` | Jupyter kernel to use. Defaults to the kernel specified in the notebook metadata. |
| `engine_name` | `Optional[str]` | Papermill engine name. Defaults to the standard ``nbclient`` engine. Custom engines registered via the ``papermill.engine`` entry point are also available. |
| `log_output` | `bool` | Stream cell outputs to the task log. |
| `start_timeout` | `int` | Seconds to wait for the kernel to start. |
| `execution_timeout` | `Optional[int]` | Per-cell execution timeout in seconds. ``None`` means no timeout. |
| `report_mode` | `bool` | Hide input cells in the output notebook. |
| `request_save_on_cell_execute` | `bool` | Save the notebook after every cell execution. Useful for inspecting partial progress on failure. |
| `progress_bar` | `bool` | Show a progress bar during execution. |
| `language` | `Optional[str]` | Override the notebook language. |
| `engine_kwargs` | `Optional[dict[str, Any]]` | Extra keyword arguments forwarded to the papermill engine (e.g. ``autosave_cell_every``). |
| `output_notebooks` | `bool` | When ``True``, the actual and executed ``.ipynb`` files are uploaded to remote storage and returned as `Files`s in the task output, making it accessible to downstream tasks. |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `native_interface` | `NativeInterface` |  |
| `output_notebook_path` | `str` |  |
| `resolved_notebook_path` | `str` |  |
| `source_file` | `Optional[str]` |  |

## Methods

| Method | Description |
|-|-|
| [`aio()`](#aio) | The aio function allows executing "sync" tasks, in an async context. |
| [`config()`](#config) | Returns additional configuration for the task. |
| [`container_args()`](#container_args) | Returns the container args for the task. |
| [`custom_config()`](#custom_config) | Returns additional configuration for the task. |
| [`data_loading_config()`](#data_loading_config) | This configuration allows executing raw containers in Flyte using the Flyte CoPilot system. |
| [`execute()`](#execute) | Execute the notebook within a Flyte task context. |
| [`forward()`](#forward) | Execute the notebook locally (outside of a Flyte run context). |
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
| `kwargs` | `**kwargs` | |

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
    serialize_context: SerializationContext,
) -> list[str]
```
Returns the container args for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `SerializationContext` | |

### custom_config()

```python
def custom_config(
    sctx: SerializationContext,
) -> dict[str, Any]
```
Returns additional configuration for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

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
    args: *args,
    kwargs: **kwargs,
) -> Any
```
Execute the notebook within a Flyte task context.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### forward()

```python
def forward(
    args: *args,
    kwargs: **kwargs,
) -> Any
```
Execute the notebook locally (outside of a Flyte run context).

Called when the task is invoked directly as a Python function
(e.g. in a test or script) rather than through the Flyte runner.
Runs the notebook in-process and returns Python values.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

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
    entrypoint: Optional[bool],
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
| `entrypoint` | `Optional[bool]` | Optional override for the entrypoint flag for the task. |
| `links` | `Tuple[Link, ...]` | Optional override for the Links associated with the task. |
| `kwargs` | `**kwargs` | Additional keyword arguments for further overrides. Some fields like name, image, docs, and interface cannot be overridden. |

**Returns:** A new TaskTemplate instance with the overridden parameters.

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
    sctx: SerializationContext,
) -> Optional[str]
```
Returns the SQL for the task. This is a set of key-value pairs that can be used to
configure the task execution environment at runtime. This is usually used by plugins.


| Parameter | Type | Description |
|-|-|-|
| `sctx` | `SerializationContext` | |

