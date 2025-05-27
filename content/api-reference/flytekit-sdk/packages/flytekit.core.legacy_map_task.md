---
title: flytekit.core.legacy_map_task
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.legacy_map_task


Flytekit map tasks specify how to run a single task across a list of inputs. Map tasks themselves are constructed with
a reference task as well as run-time parameters that limit execution concurrency and failure tolerations.

## Directory

### Classes

| Class | Description |
|-|-|
| [`MapPythonTask`](.././flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmappythontask) | A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run. |
| [`MapTaskResolver`](.././flytekit.core.legacy_map_task#flytekitcorelegacy_map_taskmaptaskresolver) | Special resolver that is used for MapTasks. |

### Methods

| Method | Description |
|-|-|
| [`map_task()`](#map_task) | Use a map task for parallelizable tasks that run across a list of an input type. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CONTAINER_ARRAY_TASK` | `str` |  |

## Methods

#### map_task()

```python
def map_task(
    task_function: typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial],
    concurrency: int,
    min_success_ratio: float,
    kwargs,
)
```
Use a map task for parallelizable tasks that run across a list of an input type. A map task can be composed of
any individual {{<py_class_ref "flytekit.PythonFunctionTask">}}.

Invoke a map task with arguments using {{<py_class_ref list>}} version of the expected input.

Usage:

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_map_task.py
   :start-after: # test_map_task_start
   :end-before: # test_map_task_end
   :language: python
   :dedent: 4
-->

```python
@task
def my_mappable_task(a: int) -> typing.Optional[str]:
    return str(a)

@workflow
def my_wf(x: typing.List[int]) -> typing.List[typing.Optional[str]]:
    return map_task(
        my_mappable_task,
        metadata=TaskMetadata(retries=1),
        concurrency=10,
        min_success_ratio=0.75,
    )(a=x).with_overrides(requests=Resources(cpu="10M"))
```
At run time, the underlying map task will be run for every value in the input collection. Attributes
such as {{<py_class_ref "flytekit.TaskMetadata">}} and ``with_overrides`` are applied to individual instances
of the mapped task.

**Map Task Plugins**

There are two plugins to run maptasks that ship as part of flyteplugins:

1. K8s Array
2. [`AWS batch`](https://docs.flyte.org/en/latest/deployment/plugin_setup/aws/batch.html)

Enabling a plugin is controlled in the plugin configuration at [`values-sandbox.yaml`](https://github.com/flyteorg/flyte/blob/10cee9f139824512b6c5be1667d321bdbc8835fa/charts/flyte/values-sandbox.yaml#L152-L162).

**K8s Array**

By default, the map task uses the ``K8s Array`` plugin. It executes array tasks by launching a pod for every instance in the array. It’s simple to use, has a straightforward implementation, and works out of the box.

**AWS batch**

Learn more about ``AWS batch`` setup configuration [`here`](https://docs.flyte.org/en/latest/deployment/plugin_setup/aws/batch.html#deployment-plugin-setup-aws-array).

A custom plugin can also be implemented to handle the task type.



| Parameter | Type |
|-|-|
| `task_function` | `typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial]` |
| `concurrency` | `int` |
| `min_success_ratio` | `float` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.legacy_map_task.MapPythonTask

A MapPythonTask defines a {{< py_class_ref flytekit.PythonTask >}} which specifies how to run
an inner {{< py_class_ref flytekit.PythonFunctionTask >}} across a range of inputs in parallel.


```python
class MapPythonTask(
    python_function_task: typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial],
    concurrency: typing.Optional[int],
    min_success_ratio: typing.Optional[float],
    bound_inputs: typing.Optional[typing.Set[str]],
    kwargs,
)
```
Wrapper that creates a MapPythonTask



| Parameter | Type |
|-|-|
| `python_function_task` | `typing.Union[flytekit.core.python_function_task.PythonFunctionTask, flytekit.core.python_function_task.PythonInstanceTask, functools.partial]` |
| `concurrency` | `typing.Optional[int]` |
| `min_success_ratio` | `typing.Optional[float]` |
| `bound_inputs` | `typing.Optional[typing.Set[str]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_command()`](#get_command) | TODO ADD bound variables to the resolver. |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | We override this method from flytekit. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`prepare_target()`](#prepare_target) | Alters the underlying run_task command to modify it for map task execution and then resets it after. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`set_command_prefix()`](#set_command_prefix) |  |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.List[str]
```
TODO ADD bound variables to the resolver. Maybe we need a different resolver?


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Dict[str, typing.Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.K8sPod
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> flytekit.models.task.Sql
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
) -> typing.Type[typing.Any]
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
) -> type
```
We override this method from flytekit.core.base_task Task because the dispatch_execute method uses this
interface to construct outputs. Each instance of an container_array task will however produce outputs
according to the underlying run_task interface and the array plugin handler will actually create a collection
from these individual outputs as the final output value.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

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


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

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



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

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


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### prepare_target()

```python
def prepare_target()
```
Alters the underlying run_task command to modify it for map task execution and then resets it after.


#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### set_command_prefix()

```python
def set_command_prefix(
    cmd: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `cmd` | `typing.Optional[typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `bound_inputs` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `run_task` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.core.legacy_map_task.MapTaskResolver

Special resolver that is used for MapTasks.
This exists because it is possible that MapTasks are created using nested "partial" subtasks.
When a maptask is created its interface is interpolated from the interface of the subtask - the interpolation,
simply converts every input into a list/collection input.

For example:
  interface -> (i: int, j: str) -> str  => map_task interface -> (i: List[int], j: List[str]) -> List[str]

But in cases in which `j` is bound to a fixed value by using `functools.partial` we need a way to ensure that
the interface is not simply interpolated, but only the unbound inputs are interpolated.

```python
def foo((i: int, j: str) -> str:
    ...

mt = map_task(functools.partial(foo, j=10))

print(mt.interface)
```

output:

        (i: List[int], j: str) -> List[str]

But, at runtime this information is lost. To reconstruct this, we use MapTaskResolver that records the "bound vars"
and then at runtime reconstructs the interface with this knowledge


```python
class MapTaskResolver(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Loader args should be of the form. |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task. |
| [`name()`](#name) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
    max_concurrency: int,
) -> flytekit.core.legacy_map_task.MapPythonTask
```
Loader args should be of the form
vars "var1,var2,.." resolver "resolver" [resolver_args]


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |
| `max_concurrency` | `int` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.legacy_map_task.MapPythonTask,
) -> typing.List[str]
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.legacy_map_task.MapPythonTask` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
) -> typing.Optional[str]
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

