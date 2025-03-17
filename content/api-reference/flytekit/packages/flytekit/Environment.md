---
title: Environment
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Environment

**Package:** `flytekit`

```python
def Environment(
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
    kwargs,
):
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |
## Methods

### dynamic()

```python
def dynamic(
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
    kwargs,
):
```
Please first see the comments for :py:func:`flytekit.task` and :py:func:`flytekit.workflow`. This ``dynamic``
concept is an amalgamation of both and enables the user to pursue some :std:ref:`pretty incredible <cookbook:advanced_merge_sort>`
constructs.

In short, a task's function is run at execution time only, and a workflow function is run at compilation time only (local
execution notwithstanding). A dynamic workflow is modeled on the backend as a task, but at execution time, the function
body is run to produce a workflow. It is almost as if the decorator changed from ``@task`` to ``@workflow`` except workflows
cannot make use of their inputs like native Python values whereas dynamic workflows can.
The resulting workflow is passed back to the Flyte engine and is
run as a :std:ref:`subworkflow <cookbook:subworkflows>`.  Simple usage

.. code-block::

@dynamic
def my_dynamic_subwf(a: int) -> (typing.List[str], int):
s = []
for i in range(a):
s.append(t1(a=i))
return s, 5

Note in the code block that we call the Python ``range`` operator on the input. This is typically not allowed in a
workflow but it is here. You can even express dependencies between tasks.

.. code-block::

@dynamic
def my_dynamic_subwf(a: int, b: int) -> int:
x = t1(a=a)
return t2(b=b, x=x)

See the :std:ref:`cookbook <cookbook:subworkflows>` for a longer discussion.


| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |
### extend()

```python
def extend(
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
    kwargs,
):
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |
### show()

```python
def show()
```
No parameters
### task()

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
    kwargs,
):
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |
### update()

```python
def update(
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
    kwargs,
):
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |
