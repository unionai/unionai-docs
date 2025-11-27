---
title: union
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union

## Directory

### Classes

| Class | Description |
|-|-|
| [`ActorEnvironment`](../union/actorenvironment) | ActorEnvironment class. |
| [`Artifact`](../union/artifact) | This is a wrapper around the Flytekit Artifact class. |
| [`Cache`](../union/cache) | Cache configuration for a task. |
| [`ContainerTask`](../union/containertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`Deck`](../union/deck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`FlyteDirectory`](../union/flytedirectory) |  |
| [`FlyteFile`](../union/flytefile) |  |
| [`ImageSpec`](../union/imagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`LaunchPlan`](../union/launchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`PodTemplate`](../union/podtemplate) | Custom PodTemplate specification for a Task. |
| [`Resources`](../union/resources) | This class is used to specify both resource requests and resource limits. |
| [`Secret`](../union/secret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`StructuredDataset`](../union/structureddataset) | This is the user facing StructuredDataset class. |
| [`UnionRemote`](../union/unionremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`VersionParameters`](../union/versionparameters) | Parameters used for version hash generation. |

### Protocols

| Protocol | Description |
|-|-|
| [`CachePolicy`](../union/cachepolicy) | Base class for protocol classes. |

### Methods

| Method | Description |
|-|-|
| [`actor_cache()`](#actor_cache) | Cache function between actor executions. |
| [`current_context()`](#current_context) | Use this method to get a handle of specific parameters available in a flyte task. |
| [`map()`](#map) | Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and. |
| [`map_task()`](#map_task) | Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask. |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |
| [`workflow()`](#workflow) | This decorator declares a function to be a Flyte workflow. |


## Methods

#### actor_cache()

```python
def actor_cache(
    f,
)
```
Cache function between actor executions.


| Parameter | Type | Description |
|-|-|-|
| `f` |  | |

#### current_context()

```python
def current_context()
```
Use this method to get a handle of specific parameters available in a flyte task.

Usage

```python
flytekit.current_context().logging.info(...)
```

Available params are documented in {{< py_class_ref flytekit.core.context_manager.ExecutionParams >}}.
There are some special params, that should be available


#### map()

```python
def map(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')],
    bound_inputs: typing.Optional[typing.Dict[str, typing.Any]],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: float,
    kwargs,
)
```
Use to map over tasks, actors, launch plans, reference tasks and launch plans, and remote tasks and
launch plans.



| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` | The Flyte entity of which will be mapped over |
| `bound_inputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | Inputs that are bound to the array node and will not be mapped over |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions |
| `min_success_ratio` | `float` | The minimum ratio of successful executions |
| `kwargs` | `**kwargs` | |

#### map_task()

```python
def map_task(
    target: typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')],
    concurrency: typing.Optional[int],
    min_successes: typing.Optional[int],
    min_success_ratio: float,
    kwargs,
)
```
Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask
or the drop in replacement ArrayNode implementation



| Parameter | Type | Description |
|-|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` | The Flyte entity of which will be mapped over |
| `concurrency` | `typing.Optional[int]` | If specified, this limits the number of mapped tasks than can run in parallel to the given batch size. If the size of the input exceeds the concurrency value, then multiple batches will be run serially until all inputs are processed. If set to 0, this means unbounded concurrency. If left unspecified, this means the array node will inherit parallelism from the workflow |
| `min_successes` | `typing.Optional[int]` | The minimum number of successful executions |
| `min_success_ratio` | `float` | The minimum ratio of successful executions |
| `kwargs` | `**kwargs` | |

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

#### workflow()

```python
def workflow(
    _workflow_function: Optional[Callable[P, FuncOut]],
    failure_policy: Optional[WorkflowFailurePolicy],
    interruptible: bool,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionWorkflow], PythonFunctionWorkflow]
```
This decorator declares a function to be a Flyte workflow. Workflows are declarative entities that construct a DAG
of tasks using the data flow between tasks.

Unlike a task, the function body of a workflow is evaluated at serialization-time (aka compile-time). This is
because while we can determine the entire structure of a task by looking at the function's signature, workflows need
to run through the function itself because the body of the function is what expresses the workflow structure. It's
also important to note that, local execution notwithstanding, it is not evaluated again when the workflow runs on
Flyte.
That is, workflows should not call non-Flyte entities since they are only run once (again, this is with respect to
the platform, local runs notwithstanding).

Example:

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_workflows.py
-->

```python
import os
import sys
import typing
from collections import OrderedDict
from unittest.mock import patch

import pytest
from typing_extensions import Annotated  # type: ignore

import flytekit.configuration
from flytekit import FlyteContextManager, StructuredDataset, kwtypes
from flytekit.configuration import Image, ImageConfig
from flytekit.core import context_manager
from flytekit.core.condition import conditional
from flytekit.core.task import task
from flytekit.core.workflow import WorkflowFailurePolicy, WorkflowMetadata, WorkflowMetadataDefaults, workflow
from flytekit.exceptions.user import FlyteValidationException, FlyteValueException, FlyteMissingReturnValueException
from flytekit.tools.translator import get_serializable
from flytekit.types.error.error import FlyteError

default_img = Image(name="default", fqn="test", tag="tag")
serialization_settings = flytekit.configuration.SerializationSettings(
    project="project",
    domain="domain",
    version="version",
    env=None,
    image_config=ImageConfig(default_image=default_img, images=[default_img]),
)

def test_metadata_values():
    with pytest.raises(FlyteValidationException):
        WorkflowMetadata(on_failure=0)

    wm = WorkflowMetadata(on_failure=WorkflowFailurePolicy.FAIL_IMMEDIATELY)
    assert wm.on_failure == WorkflowFailurePolicy.FAIL_IMMEDIATELY


def test_default_metadata_values():
    with pytest.raises(FlyteValidationException):
        WorkflowMetadataDefaults(3)

    wm = WorkflowMetadataDefaults(interruptible=False)
    assert wm.interruptible is False


def test_workflow_values():
    @task
    def t1(a: int) -> typing.NamedTuple("OutputsBC", [("t1_int_output", int), ("c", str)]):
        a = a + 2
        return a, "world-" + str(a)

    @workflow(interruptible=True, failure_policy=WorkflowFailurePolicy.FAIL_AFTER_EXECUTABLE_NODES_COMPLETE)
    def wf(a: int) -> typing.Tuple[str, str]:
        x, y = t1(a=a)
        _, v = t1(a=x)
        return y, v

    wf_spec = get_serializable(OrderedDict(), serialization_settings, wf)
    assert wf_spec.template.metadata_defaults.interruptible
    assert wf_spec.template.metadata.on_failure == 1

def test_default_values():
    @task
    def t() -> bool:
        return True

    @task
    def f() -> bool:
        return False

    @workflow
    def wf(a: bool = True) -> bool:
        return conditional("bool").if_(a.is_true()).then(t()).else_().then(f())  # type: ignore

    assert wf() is True
    assert wf(a=False) is False


def test_list_output_wf():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def list_output_wf() -> typing.List[int]:
        v = []
        for i in range(2):
            v.append(t1(a=i))
        return v

    x = list_output_wf()
    assert x == [5, 6]


def test_sub_wf_single_named_tuple():
    nt = typing.NamedTuple("SingleNamedOutput", [("named1", int)])

    @task
    def t1(a: int) -> nt:
        a = a + 2
        return nt(a)

    @workflow
    def subwf(a: int) -> nt:
        return t1(a=a)

    @workflow
    def wf(b: int) -> nt:
        out = subwf(a=b)
        return t1(a=out.named1)

    x = wf(b=3)
    assert x == (7,)


def test_sub_wf_multi_named_tuple():
    nt = typing.NamedTuple("Multi", [("named1", int), ("named2", int)])

    @task
    def t1(a: int) -> nt:
        a = a + 2
        return nt(a, a)

    @workflow
    def subwf(a: int) -> nt:
        return t1(a=a)

    @workflow
    def wf(b: int) -> nt:
        out = subwf(a=b)
        return t1(a=out.named1)

    x = wf(b=3)
    assert x == (7, 7)


def test_sub_wf_varying_types():
    @task
    def t1l(
        a: typing.List[typing.Dict[str, typing.List[int]]],
        b: typing.Dict[str, typing.List[int]],
        c: typing.Union[typing.List[typing.Dict[str, typing.List[int]]], typing.Dict[str, typing.List[int]], int],
        d: int,
    ) -> str:
        xx = ",".join([f"{k}:{v}" for d in a for k, v in d.items()])
        yy = ",".join([f"{k}: {i}" for k, v in b.items() for i in v])
        if isinstance(c, list):
            zz = ",".join([f"{k}:{v}" for d in c for k, v in d.items()])
        elif isinstance(c, dict):
            zz = ",".join([f"{k}: {i}" for k, v in c.items() for i in v])
        else:
            zz = str(c)
        return f"First: {xx} Second: {yy} Third: {zz} Int: {d}"

    @task
    def get_int() -> int:
        return 1

    @workflow
    def subwf(
        a: typing.List[typing.Dict[str, typing.List[int]]],
        b: typing.Dict[str, typing.List[int]],
        c: typing.Union[typing.List[typing.Dict[str, typing.List[int]]], typing.Dict[str, typing.List[int]]],
        d: int,
    ) -> str:
        return t1l(a=a, b=b, c=c, d=d)

    @workflow
    def wf() -> str:
        ds = [
            {"first_map_a": [42], "first_map_b": [get_int(), 2]},
            {
                "second_map_c": [33],
                "second_map_d": [9, 99],
            },
        ]
        ll = {
            "ll_1": [get_int(), get_int(), get_int()],
            "ll_2": [4, 5, 6],
        }
        out = subwf(a=ds, b=ll, c=ds, d=get_int())
        return out

    wf.compile()
    x = wf()
    expected = (
        "First: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Second: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Third: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Int: 1"
    )
    assert x == expected
    wf_spec = get_serializable(OrderedDict(), serialization_settings, wf)
    assert set(wf_spec.template.nodes[5].upstream_node_ids) == {"n2", "n1", "n0", "n4", "n3"}

    @workflow
    def wf() -> str:
        ds = [
            {"first_map_a": [42], "first_map_b": [get_int(), 2]},
            {
                "second_map_c": [33],
                "second_map_d": [9, 99],
            },
        ]
        ll = {
            "ll_1": [get_int(), get_int(), get_int()],
            "ll_2": [4, 5, 6],
        }
        out = subwf(a=ds, b=ll, c=ll, d=get_int())
        return out

    x = wf()
    expected = (
        "First: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Second: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Third: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Int: 1"
    )
    assert x == expected


def test_unexpected_outputs():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def no_outputs_wf():
        return t1(a=3)

    # Should raise an exception because the workflow returns something when it shouldn't
    with pytest.raises(FlyteValueException):
        no_outputs_wf()

@pytest.mark.skipif(sys.version_info < (3, 10, 10), reason="inspect module does not work correctly with Python <3.10.10. https://github.com/python/cpython/issues/102647#issuecomment-1466868212")
def test_missing_return_value():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    # Should raise an exception because it doesn't return something when it should
    with pytest.raises(FlyteMissingReturnValueException):

        @workflow
        def one_output_wf() -> int:  # type: ignore
            t1(a=3)

        one_output_wf()


def test_custom_wrapper():
    def our_task(
            _task_function: typing.Optional[typing.Callable] = None,
            **kwargs,
    ):
        def wrapped(_func: typing.Callable):
            return task(_task_function=_func)

        if _task_function:
            return wrapped(_task_function)
        else:
            return wrapped

    @our_task(
        foo={
            "bar1": lambda x: print(x),
            "bar2": lambda x: print(x),
        },
    )
    def missing_func_body() -> str:
        return "foo"


def test_wf_no_output():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def no_outputs_wf():
        t1(a=3)

    assert no_outputs_wf() is None


def test_wf_nested_comp(exec_prefix):
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def outer() -> typing.Tuple[int, int]:
        # You should not do this. This is just here for testing.
        @workflow
        def wf2() -> int:
            return t1(a=5)

        return t1(a=3), wf2()

    assert (8, 10) == outer()
    entity_mapping = OrderedDict()

    model_wf = get_serializable(entity_mapping, serialization_settings, outer)

    assert len(model_wf.template.interface.outputs) == 2
    assert len(model_wf.template.nodes) == 2
    assert model_wf.template.nodes[1].workflow_node is not None

    sub_wf = model_wf.sub_workflows[0]
    assert len(sub_wf.nodes) == 1
    assert sub_wf.nodes[0].id == "n0"
    assert sub_wf.nodes[0].task_node.reference_id.name == f"{exec_prefix}tests.flytekit.unit.core.test_workflows.t1"


@task
def add_5(a: int) -> int:
    a = a + 5
    return a


@workflow
def simple_wf() -> int:
    return add_5(a=1)

@workflow
def my_wf_example(a: int) -> typing.Tuple[int, int]:
    '''example

    Workflows can have inputs and return outputs of simple or complex types.

    '''

    x = add_5(a=a)

    # You can use outputs of a previous task as inputs to other nodes.
    z = add_5(a=x)

    # You can call other workflows from within this workflow
    d = simple_wf()

    # You can add conditions that can run on primitive types and execute different branches
    e = conditional("bool").if_(a == 5).then(add_5(a=d)).else_().then(add_5(a=z))

    # Outputs of the workflow have to be outputs returned by prior nodes.
    # No outputs and single or multiple outputs are supported
    return x, e

    def test_workflow_lhs():
    assert my_wf_example._lhs == "my_wf_example"


def test_all_node_types():
    assert my_wf_example(a=1) == (6, 16)
    entity_mapping = OrderedDict()

    model_wf = get_serializable(entity_mapping, serialization_settings, my_wf_example)

    assert len(model_wf.template.interface.outputs) == 2
    assert len(model_wf.template.nodes) == 4
    assert model_wf.template.nodes[2].workflow_node is not None

    sub_wf = model_wf.sub_workflows[0]
    assert len(sub_wf.nodes) == 1
    assert sub_wf.nodes[0].id == "n0"
    assert sub_wf.nodes[0].task_node.reference_id.name == "tests.flytekit.unit.core.test_workflows.add_5"


def test_wf_docstring():
    model_wf = get_serializable(OrderedDict(), serialization_settings, my_wf_example)

    assert len(model_wf.template.interface.outputs) == 2
    assert model_wf.template.interface.outputs["o0"].description == "outputs"
    assert model_wf.template.interface.outputs["o1"].description == "outputs"
    assert len(model_wf.template.interface.inputs) == 1
    assert model_wf.template.interface.inputs["a"].description == "input a"


@pytest.mark.skipif("pandas" not in sys.modules, reason="Pandas is not installed.")
def test_structured_dataset_wf():
    import pandas as pd
    from pandas.testing import assert_frame_equal

    from flytekit.types.schema import FlyteSchema

    superset_cols = kwtypes(Name=str, Age=int, Height=int)
    subset_cols = kwtypes(Name=str)
    superset_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22], "Height": [160, 178]})
    subset_df = pd.DataFrame({"Name": ["Tom", "Joseph"]})

    @task
    def t1() -> Annotated[pd.DataFrame, superset_cols]:
        return superset_df

    @task
    def t2(df: Annotated[pd.DataFrame, subset_cols]) -> Annotated[pd.DataFrame, subset_cols]:
        return df

    @task
    def t3(df: FlyteSchema[superset_cols]) -> FlyteSchema[superset_cols]:
        return df

    @task
    def t4() -> FlyteSchema[superset_cols]:
        return superset_df

    @task
    def t5(sd: Annotated[StructuredDataset, subset_cols]) -> Annotated[pd.DataFrame, subset_cols]:
        return sd.open(pd.DataFrame).all()

    @workflow
    def sd_wf() -> Annotated[pd.DataFrame, subset_cols]:
        # StructuredDataset -> StructuredDataset
        df = t1()
        return t2(df=df)

    @workflow
    def sd_to_schema_wf() -> pd.DataFrame:
        # StructuredDataset -> schema
        df = t1()
        return t3(df=df)

    @workflow
    def schema_to_sd_wf() -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
        # schema -> StructuredDataset
        df = t4()
        return t2(df=df), t5(sd=df)  # type: ignore

    assert_frame_equal(sd_wf(), subset_df)
    assert_frame_equal(sd_to_schema_wf(), superset_df)
    assert_frame_equal(schema_to_sd_wf()[0], subset_df)
    assert_frame_equal(schema_to_sd_wf()[1], subset_df)


@pytest.mark.skipif("pandas" not in sys.modules, reason="Pandas is not installed.")
def test_compile_wf_at_compile_time():
    import pandas as pd

    from flytekit.types.schema import FlyteSchema

    superset_cols = kwtypes(Name=str, Age=int, Height=int)
    superset_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22], "Height": [160, 178]})

    ctx = FlyteContextManager.current_context()
    with FlyteContextManager.with_context(
        ctx.with_execution_state(
            ctx.new_execution_state().with_params(mode=context_manager.ExecutionState.Mode.TASK_EXECUTION)
        )
    ):

        @task
        def t4() -> FlyteSchema[superset_cols]:
            return superset_df

        @workflow
        def wf():
            t4()

        assert ctx.compilation_state is None


@pytest.mark.parametrize(
    "error_message", [
        "Fail!",
        None,
        "",
        ("big", "boom!")
    ]
)
@patch("builtins.print")
def test_failure_node_local_execution(mock_print, error_message, exec_prefix):
    @task
    def clean_up(name: str, err: typing.Optional[FlyteError] = None):
        print(f"Deleting cluster {name} due to {err}")
        print("This is err:", str(err))

    @task
    def create_cluster(name: str):
        print(f"Creating cluster: {name}")

    @task
    def delete_cluster(name: str, err: typing.Optional[FlyteError] = None):
        print(f"Deleting cluster {name}")
        print(err)

    @task
    def t1(a: int, b: str):
        print(f"{a} {b}")
        raise ValueError(error_message)

    @workflow(on_failure=clean_up)
    def wf(name: str = "flyteorg"):
        c = create_cluster(name=name)
        t = t1(a=1, b="2")
        d = delete_cluster(name=name)
        c >> t >> d

    with pytest.raises(ValueError):
        wf()

    # Adjusted the error message to match the one in the failure
    expected_error_message = str(
        FlyteError(message=f"Error encountered while executing '{exec_prefix}tests.flytekit.unit.core.test_workflows.t1':
rror_message}", failed_node_id="fn0")
    )

    assert mock_print.call_count > 0

    mock_print.assert_any_call("Creating cluster: flyteorg")
    mock_print.assert_any_call("1 2")
    mock_print.assert_any_call(f"Deleting cluster flyteorg due to {expected_error_message}")
    mock_print.assert_any_call("This is err:", expected_error_message)
```


Again, users should keep in mind that even though the body of the function looks like regular Python, it is
actually not. When flytekit scans the workflow function, the objects being passed around between the tasks are not
your typical Python values. So even though you may have a task ``t1() -> int``, when ``a = t1()`` is called, ``a``
will not be an integer so if you try to ``range(a)`` you'll get an error.

Please see the :ref:`user guide <cookbook:workflow>` for more usage examples.



| Parameter | Type | Description |
|-|-|-|
| `_workflow_function` | `Optional[Callable[P, FuncOut]]` | This argument is implicitly passed and represents the decorated function. |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` | Use the options in flytekit.WorkflowFailurePolicy |
| `interruptible` | `bool` | Whether or not tasks launched from this workflow are by default interruptible |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` | Invoke this workflow or task on failure. The Workflow / task has to match the signature of the current workflow, with an additional parameter called `error` Error |
| `docs` | `Optional[Documentation]` | Description entity for the workflow |
| `pickle_untyped` | `bool` | This is a flag that allows users to bypass the type-checking that Flytekit does when constructing the workflow. This is not recommended for general use. |
| `default_options` | `Optional[Options]` | Default options for the workflow when creating a default launch plan. Currently only the labels and annotations are allowed to be set as defaults. |

