---
title: flytekitplugins.kfpytorch.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.kfpytorch.task


This Plugin adds the capability of running distributed pytorch training to Flyte using backend plugins, natively on
Kubernetes. It leverages [`Pytorch Job`](https://github.com/kubeflow/pytorch-operator) Plugin from kubeflow.

## Directory

### Classes

| Class | Description |
|-|-|
| [`CleanPodPolicy`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskcleanpodpolicy) | CleanPodPolicy describes how to deal with pods when the job is finished. |
| [`Elastic`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskelastic) | Configuration for [`torch elastic training`](https://pytorch. |
| [`ElasticWorkerResult`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskelasticworkerresult) | A named tuple representing the result of a torch elastic worker process. |
| [`Master`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskmaster) | Configuration for master replica group. |
| [`PyTorch`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorch) | Configuration for an executable [`PyTorch Job`](https://github. |
| [`PyTorchFunctionTask`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorchfunctiontask) | Plugin that submits a PyTorchJob (see https://github. |
| [`PytorchElasticFunctionTask`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskpytorchelasticfunctiontask) | Plugin for distributed training with torch elastic/torchrun (see. |
| [`RestartPolicy`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskrestartpolicy) | RestartPolicy describes how the replicas should be restarted. |
| [`RunPolicy`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskrunpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`Worker`](.././flytekitplugins.kfpytorch.task#flytekitpluginskfpytorchtaskworker) |  |

### Methods

| Method | Description |
|-|-|
| [`spawn_helper()`](#spawn_helper) | Help to spawn worker processes. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TORCH_IMPORT_ERROR_MESSAGE` | `str` |  |

## Methods

#### spawn_helper()

```python
def spawn_helper(
    fn: bytes,
    raw_output_prefix: str,
    checkpoint_dest: str,
    checkpoint_src: str,
    kwargs,
) -> flytekitplugins.kfpytorch.task.ElasticWorkerResult
```
Help to spawn worker processes.

The purpose of this function is to 1) be pickleable so that it can be used with
the multiprocessing start method `spawn` and 2) to call a cloudpickle-serialized
function passed to it. This function itself doesn't have to be pickleable. Without
such a helper task functions, which are not pickleable, couldn't be used with the
start method `spawn`.



| Parameter | Type | Description |
|-|-|-|
| `fn` | `bytes` | Cloudpickle-serialized target function to be executed in the worker process. |
| `raw_output_prefix` | `str` | Where to write offloaded data (files, directories, dataframes). |
| `checkpoint_dest` | `str` | If a previous checkpoint exists, this path should is set to the folder that contains the checkpoint information. |
| `checkpoint_src` | `str` | Location where the new checkpoint should be copied to. |
| `kwargs` | `**kwargs` | |

## flytekitplugins.kfpytorch.task.CleanPodPolicy

CleanPodPolicy describes how to deal with pods when the job is finished.



## flytekitplugins.kfpytorch.task.Elastic

Configuration for [`torch elastic training`](https://pytorch.org/docs/stable/elastic/run.html).

Use this to run single- or multi-node distributed pytorch elastic training on k8s.

Single-node elastic training is executed in a k8s pod when `nnodes` is set to 1.
Multi-node training is executed otherwise using a [`Pytorch Job`](https://github.com/kubeflow/training-operator).

Like `torchrun`, this plugin sets the environment variable `OMP_NUM_THREADS` to 1 if it is not set.
Please see https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html for potential performance improvements.
To change `OMP_NUM_THREADS`, specify it in the environment dict of the flytekit task decorator or via `pyflyte run --env`.



```python
class Elastic(
    nnodes: typing.Union[int, str],
    nproc_per_node: int,
    start_method: str,
    monitor_interval: int,
    max_restarts: int,
    rdzv_configs: typing.Dict[str, typing.Any],
    increase_shared_mem: bool,
    run_policy: typing.Optional[flytekitplugins.kfpytorch.task.RunPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `nnodes` | `typing.Union[int, str]` | |
| `nproc_per_node` | `int` | Number of workers per node. |
| `start_method` | `str` | Multiprocessing start method to use when creating workers. |
| `monitor_interval` | `int` | Interval, in seconds, to monitor the state of workers. |
| `max_restarts` | `int` | Maximum number of worker group restarts before failing. See `torch.distributed.launcher.api.LaunchConfig` and `torch.distributed.elastic.rendezvous.dynamic_rendezvous.create_handler`. Default timeouts are set to 15 minutes to account for the fact that some workers might start faster than others: Some pods might be assigned to a running node which might have the image in its cache while other workers might require a node scale up and image pull. |
| `rdzv_configs` | `typing.Dict[str, typing.Any]` | |
| `increase_shared_mem` | `bool` | [DEPRECATED] This argument is deprecated. Use `@task(shared_memory=...)` instead. PyTorch uses shared memory to share data between processes. If torch multiprocessing is used (e.g. for multi-processed data loaders) the default shared memory segment size that the container runs with might not be enough and and one might have to increase the shared memory size. This option configures the task's pod template to mount an `emptyDir` volume with medium `Memory` to to `/dev/shm`. The shared memory size upper limit is the sum of the memory limits of the containers in the pod. |
| `run_policy` | `typing.Optional[flytekitplugins.kfpytorch.task.RunPolicy]` | Configuration for the run policy. |

## flytekitplugins.kfpytorch.task.ElasticWorkerResult

A named tuple representing the result of a torch elastic worker process.

Attributes:
    return_value (Any): The value returned by the task function in the worker process.
    decks (list[flytekit.Deck]): A list of flytekit Deck objects created in the worker process.



## flytekitplugins.kfpytorch.task.Master

Configuration for master replica group. Master should always have 1 replica, so we don't need a `replicas` field



```python
class Master(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    restart_policy: typing.Optional[flytekitplugins.kfpytorch.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kfpytorch.task.RestartPolicy]` | |

## flytekitplugins.kfpytorch.task.PyTorch

Configuration for an executable [`PyTorch Job`](https://github.com/kubeflow/pytorch-operator). Use this
to run distributed PyTorch training on Kubernetes. Please notice, in most cases, you should not worry
about the configuration of the master and worker groups. The default configuration should work. The only
field you should change is the number of workers. Both replicas will use the same image, and the same
resources inherited from task function decoration.



```python
class PyTorch(
    master: flytekitplugins.kfpytorch.task.Master,
    worker: flytekitplugins.kfpytorch.task.Worker,
    run_policy: typing.Optional[flytekitplugins.kfpytorch.task.RunPolicy],
    num_workers: typing.Optional[int],
    increase_shared_mem: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `master` | `flytekitplugins.kfpytorch.task.Master` | Configuration for the master replica group. |
| `worker` | `flytekitplugins.kfpytorch.task.Worker` | Configuration for the worker replica group. |
| `run_policy` | `typing.Optional[flytekitplugins.kfpytorch.task.RunPolicy]` | Configuration for the run policy. |
| `num_workers` | `typing.Optional[int]` | [DEPRECATED] This argument is deprecated. Use `worker.replicas` instead. |
| `increase_shared_mem` | `bool` | [DEPRECATED] This argument is deprecated. Use `@task(shared_memory=...)` instead. PyTorch uses shared memory to share data between processes. If torch multiprocessing is used (e.g. for multi-processed data loaders) the default shared memory segment size that the container runs with might not be enough and and one might have to increase the shared memory size. This option configures the task's pod template to mount an `emptyDir` volume with medium `Memory` to to `/dev/shm`. The shared memory size upper limit is the sum of the memory limits of the containers in the pod. |

## flytekitplugins.kfpytorch.task.PyTorchFunctionTask

Plugin that submits a PyTorchJob (see https://github.com/kubeflow/pytorch-operator)
    defined by the code within the _task_function to k8s cluster.



```python
class PyTorchFunctionTask(
    task_config: flytekitplugins.kfpytorch.task.PyTorch,
    task_function: typing.Callable,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_config` | `flytekitplugins.kfpytorch.task.PyTorch` | |
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

## flytekitplugins.kfpytorch.task.PytorchElasticFunctionTask

Plugin for distributed training with torch elastic/torchrun (see
https://pytorch.org/docs/stable/elastic/run.html).



```python
class PytorchElasticFunctionTask(
    task_config: flytekitplugins.kfpytorch.task.Elastic,
    task_function: typing.Callable,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_config` | `flytekitplugins.kfpytorch.task.Elastic` | |
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
) -> typing.Any
```
This method will be invoked to execute the task.

Handles the exception scope for the `_execute` method.


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

## flytekitplugins.kfpytorch.task.RestartPolicy

RestartPolicy describes how the replicas should be restarted



## flytekitplugins.kfpytorch.task.RunPolicy

RunPolicy describes some policy to apply to the execution of a kubeflow job.


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
| `clean_pod_policy` | `<enum 'CleanPodPolicy'>` | Defines the policy for cleaning up pods after the PyTorchJob completes. Default to None. |
| `ttl_seconds_after_finished` | `typing.Optional[int]` | Defines the TTL for cleaning up finished PyTorchJobs. |
| `active_deadline_seconds` | `typing.Optional[int]` | Specifies the duration (in seconds) since startTime during which the job. |
| `backoff_limit` | `typing.Optional[int]` | Number of retries before marking this job as failed. |

## flytekitplugins.kfpytorch.task.Worker

```python
class Worker(
    image: typing.Optional[str],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    replicas: typing.Optional[int],
    restart_policy: typing.Optional[flytekitplugins.kfpytorch.task.RestartPolicy],
)
```
| Parameter | Type | Description |
|-|-|-|
| `image` | `typing.Optional[str]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `replicas` | `typing.Optional[int]` | |
| `restart_policy` | `typing.Optional[flytekitplugins.kfpytorch.task.RestartPolicy]` | |

