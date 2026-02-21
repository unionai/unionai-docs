---
title: flytekitplugins.dask.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.dask.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Dask`](.././flytekitplugins.dask.task#flytekitpluginsdasktaskdask) | Configuration for the dask task. |
| [`DaskTask`](.././flytekitplugins.dask.task#flytekitpluginsdasktaskdasktask) | Actual Plugin that transforms the local python code for execution within a dask cluster. |
| [`Scheduler`](.././flytekitplugins.dask.task#flytekitpluginsdasktaskscheduler) | Configuration for the scheduler pod. |
| [`WorkerGroup`](.././flytekitplugins.dask.task#flytekitpluginsdasktaskworkergroup) | Configuration for a group of dask worker pods. |

## flytekitplugins.dask.task.Dask

Configuration for the dask task



```python
class Dask(
    scheduler: flytekitplugins.dask.task.Scheduler,
    workers: flytekitplugins.dask.task.WorkerGroup,
)
```
| Parameter | Type | Description |
|-|-|-|
| `scheduler` | `flytekitplugins.dask.task.Scheduler` | Configuration for the scheduler pod. Optional, defaults to ``Scheduler()``. |
| `workers` | `flytekitplugins.dask.task.WorkerGroup` | Configuration for the pods of the default worker group. Optional, defaults to ``WorkerGroup()``. |

## flytekitplugins.dask.task.DaskTask

Actual Plugin that transforms the local python code for execution within a dask cluster



```python
class DaskTask(
    task_config: flytekitplugins.dask.task.Dask,
    task_function: typing.Callable,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_config` | `flytekitplugins.dask.task.Dask` | |
| `task_function` | `typing.Callable` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` | `None` |  |
| `deck_fields` | `None` | If not empty, this task will output deck html file for the specified decks |
| `disable_deck` | `None` | If true, this task will not output deck html file |
| `docs` | `None` |  |
| `enable_deck` | `None` | If true, this task will output deck html file |
| `environment` | `None` | Any environment variables that supplied during the execution of the task. |
| `execution_mode` | `None` |  |
| `instantiated_in` | `None` |  |
| `interface` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |
| `metadata` | `None` |  |
| `name` | `None` | Returns the name of the task. |
| `node_dependency_hints` | `None` |  |
| `python_interface` | `None` | Returns this task's python interface. |
| `resources` | `None` |  |
| `security_context` | `None` |  |
| `task_config` | `None` | Returns the user-specified task config which is used for plugin-specific handling of the task. |
| `task_function` | `None` |  |
| `task_resolver` | `None` |  |
| `task_type` | `None` |  |
| `task_type_version` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`compile_into_workflow()`](#compile_into_workflow) | In the case of dynamic workflows, this function will produce a workflow definition at execution time which will. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`dynamic_execute()`](#dynamic_execute) | By the time this function is invoked, the local_execute function should have unwrapped the Promises and Flyte. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Serialize the `dask` task config into a dict. |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command. |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task. |


#### compile()

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

#### compile_into_workflow()

```python
def compile_into_workflow(
    ctx: FlyteContext,
    task_function: Callable,
    kwargs,
) -> Union[_dynamic_job.DynamicJobSpec, _literal_models.LiteralMap]
```
In the case of dynamic workflows, this function will produce a workflow definition at execution time which will
then proceed to be executed.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `task_function` | `Callable` | |
| `kwargs` | `**kwargs` | |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> typing.Union[flytekit.models.literals.LiteralMap, flytekit.models.dynamic_job.DynamicJobSpec, typing.Coroutine]
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
  may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |

#### dynamic_execute()

```python
def dynamic_execute(
    task_function: Callable,
    kwargs,
) -> Any
```
By the time this function is invoked, the local_execute function should have unwrapped the Promises and Flyte
literal wrappers so that the kwargs we are working with here are now Python native literal values. This
function is also expected to return Python native literal values.

Since the user code within a dynamic task constitute a workflow, we have to first compile the workflow, and
then execute that workflow.

When running for real in production, the task would stop after the compilation step, and then create a file
representing that newly generated workflow, instead of executing it.


| Parameter | Type | Description |
|-|-|-|
| `task_function` | `Callable` | |
| `kwargs` | `**kwargs` | |

#### execute()

```python
def execute(
    kwargs,
) -> Any
```
This method will be invoked to execute the task. If you do decide to override this method you must also
handle dynamic tasks or you will no longer be able to use the task as a dynamic task generator.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the command which should be used in the container definition for the serialized version of this task
registered on a hosted Flyte platform.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Optional[Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_container()

```python
def get_container(
    settings: SerializationSettings,
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, typing.Any]]
```
Serialize the `dask` task config into a dict.



| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | Current serialization settings :return: Dictionary representation of the dask task config. |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
) -> Optional[tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
Update image spec based on fast registration usage, and return string representing the image


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: SerializationSettings,
) -> _task_model.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `SerializationSettings` | |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_type_for_input_var()

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

#### get_type_for_output_var()

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

#### local_execute()

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

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
) -> typing.Any
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type | Description |
|-|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` | are the modified user params as created during the pre_execute step |
| `rval` | `typing.Any` | |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
) -> typing.Optional[flytekit.core.context_manager.ExecutionParameters]
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type | Description |
|-|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` | |

#### reset_command_fn()

```python
def reset_command_fn()
```
Resets the command which should be used in the container definition of this task to the default arguments.
This is useful when the command line is overridden at serialization time.


#### sandbox_execute()

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

#### set_command_fn()

```python
def set_command_fn(
    get_command_fn: Optional[Callable[[SerializationSettings], List[str]]],
)
```
By default, the task will run on the Flyte platform using the pyflyte-execute command.
However, it can be useful to update the command with which the task is serialized for specific cases like
running map tasks ("pyflyte-map-execute") or for fast-executed tasks.


| Parameter | Type | Description |
|-|-|-|
| `get_command_fn` | `Optional[Callable[[SerializationSettings], List[str]]]` | |

#### set_resolver()

```python
def set_resolver(
    resolver: TaskResolverMixin,
)
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type | Description |
|-|-|-|
| `resolver` | `TaskResolverMixin` | |

## flytekitplugins.dask.task.Scheduler

Configuration for the scheduler pod



```python
class Scheduler(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | Custom image to use. If ``None``, will use the same image the task was registered with. Optional, defaults to ``None``. The image must have ``dask[distributed]`` installed and should have the same Python environment as the rest of the cluster (job runner pod + worker pods). |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | Resources to request for the scheduler pod. If ``None``, the requests passed into the task will be used. Optional, defaults to ``None``. |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | Resource limits for the scheduler pod. If ``None``, the limits passed into the task will be used. Optional, defaults to ``None``. |

## flytekitplugins.dask.task.WorkerGroup

Configuration for a group of dask worker pods



```python
class WorkerGroup(
    number_of_workers: typing.Optional[int],
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
)
```
| Parameter | Type | Description |
|-|-|-|
| `number_of_workers` | `typing.Optional[int]` | Number of workers to use. Optional, defaults to 1. |
| `image` | `typing.Optional[str]` | Custom image to use. If ``None``, will use the same image the task was registered with. Optional, defaults to ``None``. The image must have ``dask[distributed]`` installed. The provided image should have the same Python environment as the job runner/driver as well as the scheduler. |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | Resources to request for the worker pods. If ``None``, the requests passed into the task will be used. Optional, defaults to ``None``. |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | Resource limits for the worker pods. If ``None``, the limits passed into the task will be used. Optional, defaults to ``None``. |

