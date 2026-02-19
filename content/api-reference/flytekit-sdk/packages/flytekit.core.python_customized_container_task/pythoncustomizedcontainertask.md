---
title: PythonCustomizedContainerTask
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PythonCustomizedContainerTask

**Package:** `flytekit.core.python_customized_container_task`

Please take a look at the comments for {{&lt; py_class_ref flytekit.extend.ExecutableTemplateShimTask &gt;}} as well. This class
should be subclassed and a custom Executor provided as a default to this parent class constructor
when building a new external-container flytekit-only plugin.

This class provides authors of new task types the basic scaffolding to create task-template based tasks. In order
to write such a task, authors need to

* subclass the ``ShimTaskExecutor`` class  and override the ``execute_from_model`` function. This function is
  where all the business logic should go. Keep in mind though that you, the plugin author, will not have access
  to anything that's not serialized within the ``TaskTemplate`` which is why you'll also need to
* subclass this class, and override the ``get_custom`` function to include all the information the executor
  will need to run.
* Also pass the executor you created as the ``executor_type`` argument of this class's constructor.

Keep in mind that the total size of the ``TaskTemplate`` still needs to be small, since these will be accessed
frequently by the Flyte engine.



```python
class PythonCustomizedContainerTask(
    name: str,
    task_config: TC,
    container_image: str,
    executor_type: Type[ShimTaskExecutor],
    task_resolver: Optional[TaskTemplateResolver],
    task_type,
    requests: Optional[Resources],
    limits: Optional[Resources],
    environment: Optional[Dict[str, str]],
    secret_requests: Optional[List[Secret]],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | unique name for the task, usually the function's module and name. |
| `task_config` | `TC` | Configuration object for Task. Should be a unique type for that specific Task |
| `container_image` | `str` | This is the external container image the task should run at platform-run-time. |
| `executor_type` | `Type[ShimTaskExecutor]` | |
| `task_resolver` | `Optional[TaskTemplateResolver]` | Custom resolver - if you don't make one, use the default task template resolver. |
| `task_type` |  | String task type to be associated with this Task. |
| `requests` | `Optional[Resources]` | custom resource request settings. |
| `limits` | `Optional[Resources]` | custom resource limit settings. |
| `environment` | `Optional[Dict[str, str]]` | Environment variables you want the task to have when run. |
| `secret_requests` | `Optional[List[Secret]]` | |
| `kwargs` | `**kwargs` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `container_image` | `None` |  |
| `deck_fields` | `None` | If not empty, this task will output deck html file for the specified decks |
| `disable_deck` | `None` | If true, this task will not output deck html file |
| `docs` | `None` |  |
| `enable_deck` | `None` | If true, this task will output deck html file |
| `environment` | `None` | Any environment variables that supplied during the execution of the task. |
| `executor` | `None` |  |
| `executor_type` | `None` |  |
| `instantiated_in` | `None` |  |
| `interface` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |
| `metadata` | `None` |  |
| `name` | `None` | Return the name of the underlying task. |
| `python_interface` | `None` | Returns this task's python interface. |
| `resources` | `None` |  |
| `security_context` | `None` |  |
| `task_config` | `None` | Returns the user-specified task config which is used for plugin-specific handling of the task. |
| `task_resolver` | `None` |  |
| `task_template` | `None` | Override the base class implementation to serialize on first call. |
| `task_type` | `None` |  |
| `task_type_version` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This function is largely similar to the base PythonTask, with the exception that we have to infer the Python. |
| [`execute()`](#execute) | Rather than running here, send everything to the executor. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) |  |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`pre_execute()`](#pre_execute) | This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`serialize_to_model()`](#serialize_to_model) |  |


### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


### dispatch_execute()

```python
def dispatch_execute(
    ctx: FlyteContext,
    input_literal_map: _literal_models.LiteralMap,
) -> Union[_literal_models.LiteralMap, _dynamic_job.DynamicJobSpec]
```
This function is largely similar to the base PythonTask, with the exception that we have to infer the Python
interface before executing. Also, we refer to ``self.task_template`` rather than just ``self`` similar to task
classes that derive from the base ``PythonTask``.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `input_literal_map` | `_literal_models.LiteralMap` | |

### execute()

```python
def execute(
    kwargs,
) -> Any
```
Rather than running here, send everything to the executor.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### find_lhs()

```python
def find_lhs()
```
### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Dict[str, str]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

### get_container()

```python
def get_container(
    settings: SerializationSettings,
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

### get_custom()

```python
def get_custom(
    settings: SerializationSettings,
) -> Dict[str, Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
) -> typing.Type[typing.Any]
```
Returns the python type for an input variable by name.


| Parameter | Type | Description |
|-|-|-|
| `k` | `str` | |
| `v` | `typing.Any` | |

### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
) -> typing.Type[typing.Any]
```
Returns the python type for the specified output variable by name.


| Parameter | Type | Description |
|-|-|-|
| `k` | `str` | |
| `v` | `typing.Any` | |

### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, typing.Coroutine, NoneType]
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
### post_execute()

```python
def post_execute(
    _: Optional[ExecutionParameters],
    rval: Any,
) -> Any
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `_` | `Optional[ExecutionParameters]` | |
| `rval` | `Any` | |

### pre_execute()

```python
def pre_execute(
    user_params: Optional[ExecutionParameters],
) -> Optional[ExecutionParameters]
```
This function is a stub, just here to keep dispatch_execute compatibility between this class and PythonTask.


| Parameter | Type | Description |
|-|-|-|
| `user_params` | `Optional[ExecutionParameters]` | |

### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |

### serialize_to_model()

```python
def serialize_to_model(
    settings: SerializationSettings,
) -> _task_model.TaskTemplate
```
| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

