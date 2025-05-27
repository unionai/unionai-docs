---
title: flytekitplugins.spark.task
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.spark.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Databricks`](.././flytekitplugins.spark.task#flytekitpluginssparktaskdatabricks) | Deprecated. |
| [`DatabricksV2`](.././flytekitplugins.spark.task#flytekitpluginssparktaskdatabricksv2) | Use this to configure a Databricks task. |
| [`PysparkFunctionTask`](.././flytekitplugins.spark.task#flytekitpluginssparktaskpysparkfunctiontask) | Actual Plugin that transforms the local python code for execution within a spark context. |
| [`Spark`](.././flytekitplugins.spark.task#flytekitpluginssparktaskspark) | Use this to configure a SparkContext for a your task. |

### Methods

| Method | Description |
|-|-|
| [`new_spark_session()`](#new_spark_session) | Optionally creates a new spark session and returns it. |


### Variables

| Property | Type | Description |
|-|-|-|
| `PRIMARY_CONTAINER_DEFAULT_NAME` | `str` |  |

## Methods

#### new_spark_session()

```python
def new_spark_session(
    name: str,
    conf: typing.Dict[str, str],
)
```
Optionally creates a new spark session and returns it.
In cluster mode (running in hosted flyte, this will disregard the spark conf passed in)

This method is safe to be used from any other method. That is one reason why, we have duplicated this code
fragment with the pre-execute. For example in the notebook scenario we might want to call it from a separate kernel


| Parameter | Type |
|-|-|
| `name` | `str` |
| `conf` | `typing.Dict[str, str]` |

## flytekitplugins.spark.task.Databricks

Deprecated. Use DatabricksV2 instead.


```python
class Databricks(
    spark_conf: typing.Optional[typing.Dict[str, str]],
    hadoop_conf: typing.Optional[typing.Dict[str, str]],
    executor_path: typing.Optional[str],
    applications_path: typing.Optional[str],
    driver_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
    executor_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
    databricks_conf: typing.Optional[typing.Dict[str, typing.Union[str, dict]]],
    databricks_instance: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `executor_path` | `typing.Optional[str]` |
| `applications_path` | `typing.Optional[str]` |
| `driver_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `executor_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Union[str, dict]]]` |
| `databricks_instance` | `typing.Optional[str]` |

## flytekitplugins.spark.task.DatabricksV2

Use this to configure a Databricks task. Task's marked with this will automatically execute
natively onto databricks platform as a distributed execution of spark



```python
class DatabricksV2(
    spark_conf: typing.Optional[typing.Dict[str, str]],
    hadoop_conf: typing.Optional[typing.Dict[str, str]],
    executor_path: typing.Optional[str],
    applications_path: typing.Optional[str],
    driver_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
    executor_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
    databricks_conf: typing.Optional[typing.Dict[str, typing.Union[str, dict]]],
    databricks_instance: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `executor_path` | `typing.Optional[str]` |
| `applications_path` | `typing.Optional[str]` |
| `driver_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `executor_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Union[str, dict]]]` |
| `databricks_instance` | `typing.Optional[str]` |

## flytekitplugins.spark.task.PysparkFunctionTask

Actual Plugin that transforms the local python code for execution within a spark context


```python
class PysparkFunctionTask(
    task_config: flytekitplugins.spark.task.Spark,
    task_function: typing.Callable,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `task_config` | `flytekitplugins.spark.task.Spark` |
| `task_function` | `typing.Callable` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`agent_signal_handler()`](#agent_signal_handler) |  |
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
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
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
| [`to_k8s_pod()`](#to_k8s_pod) | Convert the podTemplate to K8sPod. |


#### agent_signal_handler()

```python
def agent_signal_handler(
    resource_meta: flytekit.extend.backend.base_agent.ResourceMeta,
    signum: int,
    frame: frame,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_agent.ResourceMeta` |
| `signum` | `int` |
| `frame` | `frame` |

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


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `task_function` | `Callable` |
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


| Parameter | Type |
|-|-|
| `task_function` | `Callable` |
| `kwargs` | ``**kwargs`` |

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
This method will be invoked to execute the task. If you do decide to override this method you must also
handle dynamic tasks or you will no longer be able to use the task as a dynamic task generator.


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
    settings: SerializationSettings,
) -> List[str]
```
Returns the command which should be used in the container definition for the serialized version of this task
registered on a hosted Flyte platform.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
) -> Optional[Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: SerializationSettings,
) -> _task_model.Container
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

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

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
) -> List[str]
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
) -> Optional[tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
) -> str
```
Update image spec based on fast registration usage, and return string representing the image


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

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


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Sql]
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
) -> typing.Type[typing.Any]
```
Returns the python type for the specified output variable by name.


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
    user_params: flytekit.core.context_manager.ExecutionParameters,
) -> flytekit.core.context_manager.ExecutionParameters
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `flytekit.core.context_manager.ExecutionParameters` |

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


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### set_command_fn()

```python
def set_command_fn(
    get_command_fn: Optional[Callable[[SerializationSettings], List[str]]],
)
```
By default, the task will run on the Flyte platform using the pyflyte-execute command.
However, it can be useful to update the command with which the task is serialized for specific cases like
running map tasks ("pyflyte-map-execute") or for fast-executed tasks.


| Parameter | Type |
|-|-|
| `get_command_fn` | `Optional[Callable[[SerializationSettings], List[str]]]` |

#### set_resolver()

```python
def set_resolver(
    resolver: TaskResolverMixin,
)
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

#### to_k8s_pod()

```python
def to_k8s_pod(
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Convert the podTemplate to K8sPod


| Parameter | Type |
|-|-|
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `container_image` |  |  |
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `execution_mode` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  | {{< multiline >}}Returns the name of the task.
{{< /multiline >}} |
| `node_dependency_hints` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_function` |  |  |
| `task_resolver` |  |  |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekitplugins.spark.task.Spark

Use this to configure a SparkContext for a your task. Task's marked with this will automatically execute
natively onto K8s as a distributed execution of spark

Attributes:
    spark_conf (Optional[Dict[str, str]]): Spark configuration dictionary.
    hadoop_conf (Optional[Dict[str, str]]): Hadoop configuration dictionary.
    executor_path (Optional[str]): Path to the Python binary for PySpark execution.
    applications_path (Optional[str]): Path to the main application file.
    driver_pod (Optional[PodTemplate]): The pod template for the Spark driver pod.
    executor_pod (Optional[PodTemplate]): The pod template for the Spark executor pod.


```python
class Spark(
    spark_conf: typing.Optional[typing.Dict[str, str]],
    hadoop_conf: typing.Optional[typing.Dict[str, str]],
    executor_path: typing.Optional[str],
    applications_path: typing.Optional[str],
    driver_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
    executor_pod: typing.Optional[flytekit.core.pod_template.PodTemplate],
)
```
| Parameter | Type |
|-|-|
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `executor_path` | `typing.Optional[str]` |
| `applications_path` | `typing.Optional[str]` |
| `driver_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `executor_pod` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |

