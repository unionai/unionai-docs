---
title: flytekit.core.task
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Echo`](.././flytekit.core.task#flytekitcoretaskecho) | Base Class for all Tasks with a Python native ``Interface``. |
| [`ReferenceTask`](.././flytekit.core.task#flytekitcoretaskreferencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`TaskPlugins`](.././flytekit.core.task#flytekitcoretasktaskplugins) | This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |

### Methods

| Method | Description |
|-|-|
| [`decorate_function()`](#decorate_function) | Decorates the task with additional functionality if necessary. |
| [`eager()`](#eager) | Eager workflow decorator. |
| [`reference_task()`](#reference_task) | A reference task is a pointer to a task that already exists on your Flyte installation. |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FLYTE_ENABLE_VSCODE_KEY` | `str` |  |
| `FuncOut` | `TypeVar` |  |
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |

## Methods

#### decorate_function()

```python
def decorate_function(
    fn: Callable[P, Any],
) -> Callable[P, Any]
```
Decorates the task with additional functionality if necessary.



| Parameter | Type | Description |
|-|-|-|
| `fn` | `Callable[P, Any]` | python function to decorate. :return: a decorated python function. |

#### eager()

```python
def eager(
    _fn,
    args,
    kwargs,
) -> Union[EagerAsyncPythonFunctionTask, partial]
```
Eager workflow decorator.

This type of task will execute all Flyte entities within it eagerly, meaning that all python constructs can be
used inside of an ``@eager``-decorated function. This is because eager workflows use a
{{< py_class_ref flytekit.remote.remote.FlyteRemote >}} object to kick off executions when a flyte entity needs to produce a
value. Basically think about it as: every Flyte entity that is called(), the stack frame is an execution with its
own Flyte URL. Results (or the error) are fetched when the execution is finished.

For example:

```python
from flytekit import task, eager

@task
def add_one(x: int) -> int:
    return x + 1

@task
def double(x: int) -> int:
    return x * 2

@eager
async def eager_workflow(x: int) -> int:
    out = add_one(x=x)
    return double(x=out)

# run locally with asyncio
if __name__ == "__main__":
    import asyncio

    result = asyncio.run(eager_workflow(x=1))
    print(f"Result: {result}")  # "Result: 4"
```
Unlike {{< py_func_ref dynamic workflows flytekit.dynamic >}}, eager workflows are not compiled into a workflow spec, but
uses python's [`async`](https://docs.python.org/3/library/asyncio.html) capabilities to execute flyte entities.

> [!NOTE]
> Eager workflows only support `@task`, `@workflow`, and `@eager` entities. Conditionals are not supported, use a
   plain Python if statement instead.

> [!IMPORTANT]
> A ``client_secret_group`` and ``client_secret_key`` is needed for authenticating via
   {{< py_class_ref flytekit.remote.remote.FlyteRemote >}} using the ``client_credentials`` authentication, which is
   configured via {{< py_class_ref flytekit.configuration.PlatformConfig >}}.

   ```python
    from flytekit.remote import FlyteRemote
    from flytekit.configuration import Config

    @eager(
        remote=FlyteRemote(config=Config.auto(config_file="config.yaml")),
        client_secret_group="my_client_secret_group",
        client_secret_key="my_client_secret_key",
    )
    async def eager_workflow(x: int) -> int:
        out = await add_one(x)
        return await double(one)
    ```
   Where ``config.yaml`` contains is a flytectl-compatible config file.
   For more details, see [`here`](https://docs.flyte.org/en/latest/flytectl/overview.html#configuration).

   When using a sandbox cluster started with ``flytectl demo start``, however, the ``client_secret_group``
   and ``client_secret_key`` are not needed, :

   ```python
    @eager
    async def eager_workflow(x: int) -> int:
        ...
 ```


| Parameter | Type | Description |
|-|-|-|
| `_fn` |  | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### reference_task()

```python
def reference_task(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> Callable[[Callable[..., Any]], ReferenceTask]
```
A reference task is a pointer to a task that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.

Example:
<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
   :pyobject: ref_t1
-->
```python
@reference_task(
project="flytesnacks",
domain="development",
name="recipes.aaa.simple.join_strings",
version="553018f39e519bdb2597b652639c30ce16b99c79",
)
def ref_t1(a: typing.List[str]) -> str:
    '''
    The empty function acts as a convenient skeleton to make it intuitive to call/reference this task from workflows.
    The interface of the task must match that of the remote task. Otherwise, remote compilation of the workflow will
    fail.
    '''
    return "hello"
```


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |
| `version` | `str` | |

#### task()

```python
def task(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    labels: Optional[dict[str, str]],
    annotations: Optional[dict[str, str]],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

```python
@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
    ...
```

For specific task types

```python
@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
    ...
```
Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type | Description |
|-|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` | This argument is implicitly passed and represents the decorated function |
| `task_config` | `Optional[T]` | This argument provides configuration for a specific task types. Please refer to the plugins documentation for the right object to use. |
| `cache` | `Union[bool, Cache]` | Boolean or Cache that indicates how caching is configured. :deprecated param cache_serialize: (deprecated - please use Cache) Boolean that indicates if identical (ie. same inputs) instances of this task should be executed in serial when caching is enabled. This means that given multiple concurrent executions over identical inputs, only a single instance executes and the rest wait to reuse the cached results. This parameter does nothing without also setting the cache parameter. :deprecated param cache_version: (deprecated - please use Cache) Cache version to use. Changes to the task signature will automatically trigger a cache miss, but you can always manually update this field as well to force a cache miss. You should also manually bump this version if the function body/business logic has changed, but the signature hasn't. :deprecated param cache_ignore_input_vars: (deprecated - please use Cache) Input variables that should not be included when calculating hash for cache. |
| `retries` | `int` | Number of times to retry this task during a workflow execution. |
| `interruptible` | `Optional[bool]` | [Optional] Boolean that indicates that this task can be interrupted and/or scheduled on nodes with lower QoS guarantees. This will directly reduce the `$`/`execution cost` associated, at the cost of performance penalties due to potential interruptions. Requires additional Flyte platform level configuration. If no value is provided, the task will inherit this attribute from its workflow, as follows: No values set for interruptible at the task or workflow level - task is not interruptible Task has interruptible=True, but workflow has no value set - task is interruptible Workflow has interruptible=True, but task has no value set - task is interruptible Workflow has interruptible=False, but task has interruptible=True - task is interruptible Workflow has interruptible=True, but task has interruptible=False - task is not interruptible |
| `deprecated` | `str` | A string that can be used to provide a warning message for deprecated task. Absence / empty str indicates that the task is active and not deprecated |
| `timeout` | `Union[datetime.timedelta, int]` | the max amount of time for which one execution of this task should be executed for. The execution will be terminated if the runtime exceeds the given timeout (approximately). |
| `container_image` | `Optional[Union[str, ImageSpec]]` | By default the configured FLYTE_INTERNAL_IMAGE is used for every task. This directive can be used to provide an alternate image for a specific task. This is useful for the cases in which images bloat because of various dependencies and a dependency is only required for this or a set of tasks, and they vary from the default.  ```python # Use default image name `fqn` and alter the tag to `tag-{{default.tag}}` tag of the default image # with a prefix. In this case, it is assumed that the image like # flytecookbook:tag-gitsha is published alongwith the default of flytecookbook:gitsha @task(container_image='{{.images.default.fqn}}:tag-{{images.default.tag}}') def foo(): ...  # Refer to configurations to configure fqns for other images besides default. In this case it will # lookup for an image named xyz @task(container_image='{{.images.xyz.fqn}}:{{images.default.tag}}') def foo2(): ... ``` |
| `environment` | `Optional[Dict[str, str]]` | Environment variables that should be added for this tasks execution |
| `requests` | `Optional[Resources]` | Specify compute resource requests for your task. For Pod-plugin tasks, these values will apply only to the primary container. |
| `limits` | `Optional[Resources]` | Compute limits. Specify compute resource limits for your task. For Pod-plugin tasks, these values will apply only to the primary container. For more information, please see {{&lt; py_class_ref flytekit.Resources &gt;}}. |
| `secret_requests` | `Optional[List[Secret]]` | Keys that can identify the secrets supplied at runtime. Ideally the secret keys should also be semi-descriptive. The key values will be available from runtime, if the backend is configured to provide secrets and if secrets are available in the configured secrets store. Possible options for secret stores are - Vault, Confidant, Kube secrets, AWS KMS etc Refer to {{&lt; py_class_ref Secret &gt;}} to understand how to specify the request for a secret. It may change based on the backend provider.  &gt; [!NOTE] &gt; During local execution, the secrets will be pulled from the local environment variables with the format `{GROUP}_{GROUP_VERSION}_{KEY}`, where all the characters are capitalized and the prefix is not used. |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` | This is mainly for internal use. Please ignore. It is filled in automatically. |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` | A list of tasks, launchplans, or workflows that this task depends on. This is only for dynamic tasks/workflows, where flyte cannot automatically determine the dependencies prior to runtime. Even on dynamic tasks this is optional, but in some scenarios it will make registering the workflow easier, because it allows registration to be done the same as for static tasks/workflows.  For example this is useful to run launchplans dynamically, because launchplans must be registered on flyteadmin before they can be run. Tasks and workflows do not have this requirement.  ```python @workflow def workflow0(): ...  launchplan0 = LaunchPlan.get_or_create(workflow0)  # Specify node_dependency_hints so that launchplan0 will be registered on flyteadmin, despite this being a # dynamic task. @dynamic(node_dependency_hints=[launchplan0]) def launch_dynamically(): # To run a sub-launchplan it must have previously been registered on flyteadmin. return [launchplan0]*10 ``` |
| `task_resolver` | `Optional[TaskResolverMixin]` | Provide a custom task resolver. |
| `docs` | `Optional[Documentation]` | Documentation about this task |
| `disable_deck` | `Optional[bool]` | If true, this task will not output deck html file |
| `enable_deck` | `Optional[bool]` | If true, this task will output deck html file |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` | If specified and enble_deck is True, this task will output deck html file with the fields specified in the tuple |
| `pod_template` | `Optional['PodTemplate']` | Custom PodTemplate for this task. |
| `pod_template_name` | `Optional[str]` | The name of the existing PodTemplate resource which will be used in this task. |
| `accelerator` | `Optional[BaseAccelerator]` | The accelerator to use for this task. |
| `pickle_untyped` | `bool` | Boolean that indicates if the task allows unspecified data types. |
| `shared_memory` | `Optional[Union[L[True], str]]` | If True, then shared memory will be attached to the container where the size is equal to the allocated memory. If int, then the shared memory is set to that size. |
| `resources` | `Optional[Resources]` | Specify both the request and the limit. When the value is set to a tuple or list, the first value is the request and the second value is the limit. If the value is a single value, then both the requests and limit is set to that value. For example, the `Resource(cpu=("1", "2"), mem="1Gi")` will set the cpu request to 1, cpu limit to 2, and mem request to 1Gi. |
| `labels` | `Optional[dict[str, str]]` | Labels to be applied to the task resource. |
| `annotations` | `Optional[dict[str, str]]` | Annotations to be applied to the task resource. |
| `kwargs` | `**kwargs` | |

## flytekit.core.task.Echo

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to {{< py_class_ref flytekit.PythonFunctionTask >}}.


```python
class Echo(
    name: str,
    inputs: Optional[Dict[str, Type]],
    kwargs,
)
```
A task that simply echoes the inputs back to the user.
The task's inputs and outputs interface are the same.

FlytePropeller uses echo plugin to handle this task, and it won't create a pod for this task.
It will simply pass the inputs to the outputs.
https://github.com/flyteorg/flyte/blob/master/flyteplugins/go/tasks/plugins/testing/echo.go

Note: Make sure to enable the echo plugin in the propeller config to use this task.
```
task-plugins:
  enabled-plugins:
    - echo
```



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the task. |
| `inputs` | `Optional[Dict[str, Type]]` | Name and type of inputs specified as a dictionary. e.g. {"a": int, "b": str}. |
| `kwargs` | `**kwargs` | All other args required by the parent type - PythonTask. |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) | This method will be invoked to execute the task. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |


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

#### execute()

```python
def execute(
    kwargs,
) -> Any
```
This method will be invoked to execute the task.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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

### Properties

| Property | Type | Description |
|-|-|-|
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
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.core.task.ReferenceTask

This is a reference task, the body of the function passed in through the constructor will never be used, only the
signature of the function will be. The signature should also match the signature of the task you're referencing,
as stored by Flyte Admin, if not, workflows using this will break upon compilation.


```python
class ReferenceTask(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | A unique name for the task instantiation. This is unique for every instance of task. |
| `version` | `str` | |
| `inputs` | `Dict[str, type]` | |
| `outputs` | `Dict[str, Type]` | |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary. |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte. |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary. |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte. |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task. |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte. |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up,. |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs. |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution. |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
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

#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, str]]
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flyteidl.core.tasks_pb2.ExtendedResources]
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |

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
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


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

#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `deck_fields` |  | {{< multiline >}}If not empty, this task will output deck html file for the specified decks
{{< /multiline >}} |
| `disable_deck` |  | {{< multiline >}}If true, this task will not output deck html file
{{< /multiline >}} |
| `docs` |  |  |
| `enable_deck` |  | {{< multiline >}}If true, this task will output deck html file
{{< /multiline >}} |
| `environment` |  | {{< multiline >}}Any environment variables that supplied during the execution of the task.
{{< /multiline >}} |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.core.task.TaskPlugins

This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask.
Every task that the user wishes to use should be available in this factory.
Usage

```python
TaskPlugins.register_pythontask_plugin(config_object_type, plugin_object_type)
# config_object_type is any class that will be passed to the plugin_object as task_config
# Plugin_object_type is a derivative of ``PythonFunctionTask``
```
Examples of available task plugins include different query-based plugins such as
{{< py_class_ref flytekitplugins.athena.task.AthenaTask >}} and {{< py_class_ref flytekitplugins.hive.task.HiveTask >}}, kubeflow
operators like {{< py_class_ref plugins.kfpytorch.flytekitplugins.kfpytorch.task.PyTorchFunctionTask >}} and
{{< py_class_ref plugins.kftensorflow.flytekitplugins.kftensorflow.task.TensorflowFunctionTask >}}, and generic plugins like
{{< py_class_ref flytekitplugins.pod.task.PodFunctionTask >}} which doesn't integrate with third party tools or services.

The `task_config` is different for every task plugin type. This is filled out by users when they define a task to
specify plugin-specific behavior and features.  For example, with a query type task plugin, the config might store
information related to which database to query.

The `plugin_object_type` can be used to customize execution behavior and task serialization properties in tandem
with the `task_config`.


### Methods

| Method | Description |
|-|-|
| [`find_pythontask_plugin()`](#find_pythontask_plugin) | Returns a PluginObjectType if found or returns the base PythonFunctionTask. |
| [`register_pythontask_plugin()`](#register_pythontask_plugin) | Use this method to register a new plugin into Flytekit. |


#### find_pythontask_plugin()

```python
def find_pythontask_plugin(
    plugin_config_type: type,
) -> Type[PythonFunctionTask]
```
Returns a PluginObjectType if found or returns the base PythonFunctionTask


| Parameter | Type | Description |
|-|-|-|
| `plugin_config_type` | `type` | |

#### register_pythontask_plugin()

```python
def register_pythontask_plugin(
    plugin_config_type: type,
    plugin: Type[PythonFunctionTask],
)
```
Use this method to register a new plugin into Flytekit. Usage ::

```python
TaskPlugins.register_pythontask_plugin(config_object_type, plugin_object_type)
# config_object_type is any class that will be passed to the plugin_object as task_config
# Plugin_object_type is a derivative of ``PythonFunctionTask``
```


| Parameter | Type | Description |
|-|-|-|
| `plugin_config_type` | `type` | |
| `plugin` | `Type[PythonFunctionTask]` | |

