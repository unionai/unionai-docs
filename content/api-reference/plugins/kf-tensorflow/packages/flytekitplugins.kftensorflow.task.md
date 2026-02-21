---
title: flytekitplugins.kftensorflow.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.kftensorflow.task


This Plugin adds the capability of running distributed tensorflow training to Flyte using backend plugins, natively on
Kubernetes. It leverages [`TF Job`](https://github.com/kubeflow/tf-operator) Plugin from kubeflow.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Chief`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskchief) |  |
| [`CleanPodPolicy`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskcleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`Evaluator`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskevaluator) |  |
| [`PS`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskps) |  |
| [`RestartPolicy`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskrestartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`RunPolicy`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskrunpolicy) | RunPolicy describes a set of policies to apply to the execution of a Kubeflow job. |
| [`TensorflowFunctionTask`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtasktensorflowfunctiontask) | Plugin that submits a TFJob (see https://github. |
| [`TfJob`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtasktfjob) | Configuration for an executable [`TensorFlow Job`](https://github. |
| [`Worker`](.././flytekitplugins.kftensorflow.task#flytekitpluginskftensorflowtaskworker) |  |

## flytekitplugins.kftensorflow.task.Chief

```python
class Chief(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    replicas: typing.Optional[int],
    restart_policy: typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `replicas` | `typing.Optional[int]` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy]` | |

## flytekitplugins.kftensorflow.task.CleanPodPolicy

CleanPodPolicy describes how to deal with pods when the job is finished.



## flytekitplugins.kftensorflow.task.Evaluator

```python
class Evaluator(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    replicas: int,
    restart_policy: typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `replicas` | `int` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy]` | |

## flytekitplugins.kftensorflow.task.PS

```python
class PS(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    replicas: typing.Optional[int],
    restart_policy: typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `replicas` | `typing.Optional[int]` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy]` | |

## flytekitplugins.kftensorflow.task.RestartPolicy

RestartPolicy describes how the replicas should be restarted



## flytekitplugins.kftensorflow.task.RunPolicy

RunPolicy describes a set of policies to apply to the execution of a Kubeflow job.



```python
class RunPolicy(
    clean_pod_policy: <enum 'CleanPodPolicy'>,
    ttl_seconds_after_finished: typing.Optional[int],
    active_deadline_seconds: typing.Optional[int],
    backoff_limit: typing.Optional[int],
)
```
| Parameter | Type | Description |
|-|-|-|
| `clean_pod_policy` | `<enum 'CleanPodPolicy'>` | The policy for cleaning up pods after the job completes. Defaults to None. |
| `ttl_seconds_after_finished` | `typing.Optional[int]` | The time-to-live (TTL) in seconds for cleaning up finished jobs. |
| `active_deadline_seconds` | `typing.Optional[int]` | The duration (in seconds) since startTime during which the job can remain active before it is terminated. Must be a positive integer. This setting applies only to pods where restartPolicy is OnFailure or Always. |
| `backoff_limit` | `typing.Optional[int]` | The number of retries before marking this job as failed. |

## flytekitplugins.kftensorflow.task.TensorflowFunctionTask

Plugin that submits a TFJob (see https://github.com/kubeflow/tf-operator)
    defined by the code within the _task_function to k8s cluster.



```python
class TensorflowFunctionTask(
    task_config: flytekitplugins.kftensorflow.task.TfJob,
    task_function: typing.Callable,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_config` | `flytekitplugins.kftensorflow.task.TfJob` | |
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
) -> typing.Dict[str, typing.Any]
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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

## flytekitplugins.kftensorflow.task.TfJob

Configuration for an executable [`TensorFlow Job`](https://github.com/kubeflow/tf-operator). Use this
to run distributed TensorFlow training on Kubernetes.



```python
class TfJob(
    chief: flytekitplugins.kftensorflow.task.Chief,
    ps: flytekitplugins.kftensorflow.task.PS,
    worker: flytekitplugins.kftensorflow.task.Worker,
    evaluator: flytekitplugins.kftensorflow.task.Evaluator,
    run_policy: typing.Optional[flytekitplugins.kftensorflow.task.RunPolicy],
    num_workers: typing.Optional[int],
    num_ps_replicas: typing.Optional[int],
    num_chief_replicas: typing.Optional[int],
    num_evaluator_replicas: typing.Optional[int],
)
```
| Parameter | Type | Description |
|-|-|-|
| `chief` | `flytekitplugins.kftensorflow.task.Chief` | Configuration for the chief replica group. |
| `ps` | `flytekitplugins.kftensorflow.task.PS` | Configuration for the parameter server (PS) replica group. |
| `worker` | `flytekitplugins.kftensorflow.task.Worker` | Configuration for the worker replica group. |
| `evaluator` | `flytekitplugins.kftensorflow.task.Evaluator` | Configuration for the evaluator replica group. |
| `run_policy` | `typing.Optional[flytekitplugins.kftensorflow.task.RunPolicy]` | Configuration for the run policy. |
| `num_workers` | `typing.Optional[int]` | [DEPRECATED] This argument is deprecated. Use `worker.replicas` instead. |
| `num_ps_replicas` | `typing.Optional[int]` | [DEPRECATED] This argument is deprecated. Use `ps.replicas` instead. |
| `num_chief_replicas` | `typing.Optional[int]` | [DEPRECATED] This argument is deprecated. Use `chief.replicas` instead. |
| `num_evaluator_replicas` | `typing.Optional[int]` | |

## flytekitplugins.kftensorflow.task.Worker

```python
class Worker(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    replicas: typing.Optional[int],
    restart_policy: typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `replicas` | `typing.Optional[int]` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kftensorflow.task.RestartPolicy]` | |

