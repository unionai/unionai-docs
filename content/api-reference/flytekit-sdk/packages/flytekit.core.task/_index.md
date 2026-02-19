---
title: flytekit.core.task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Echo`](../flytekit.core.task/echo) |  |
| [`ReferenceTask`](../flytekit.core.task/referencetask) | This is a reference task, the body of the function passed in through the constructor will never be used, only the. |
| [`TaskPlugins`](../flytekit.core.task/taskplugins) | This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask. |

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
{{&lt; py_class_ref flytekit.remote.remote.FlyteRemote &gt;}} object to kick off executions when a flyte entity needs to produce a
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
Unlike {{&lt; py_func_ref dynamic workflows flytekit.dynamic &gt;}}, eager workflows are not compiled into a workflow spec, but
uses python's [`async`](https://docs.python.org/3/library/asyncio.html) capabilities to execute flyte entities.

> [!NOTE]
> Eager workflows only support `@task`, `@workflow`, and `@eager` entities. Conditionals are not supported, use a
   plain Python if statement instead.

> [!IMPORTANT]
> A ``client_secret_group`` and ``client_secret_key`` is needed for authenticating via
   {{&lt; py_class_ref flytekit.remote.remote.FlyteRemote &gt;}} using the ``client_credentials`` authentication, which is
   configured via {{&lt; py_class_ref flytekit.configuration.PlatformConfig &gt;}}.

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
&lt;!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
   :pyobject: ref_t1
--&gt;
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
Please see some cookbook :std:ref:`task examples &lt;cookbook:tasks&gt;` for additional information.



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
| `secret_requests` | `Optional[List[Secret]]` | Keys that can identify the secrets supplied at runtime. Ideally the secret keys should also be semi-descriptive. The key values will be available from runtime, if the backend is configured to provide secrets and if secrets are available in the configured secrets store. Possible options for secret stores are - Vault, Confidant, Kube secrets, AWS KMS etc Refer to {{&lt; py_class_ref Secret &gt;}} to understand how to specify the request for a secret. It may change based on the backend provider.  > [!NOTE] > During local execution, the secrets will be pulled from the local environment variables with the format `{GROUP}_{GROUP_VERSION}_{KEY}`, where all the characters are capitalized and the prefix is not used. |
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

