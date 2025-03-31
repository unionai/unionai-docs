---
title: flytekit
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit


Core Flytekit
=====================

This package contains all of the most common abstractions you'll need to write Flyte workflows and extend Flytekit.

Basic Authoring
===============

These are the essentials needed to get started writing tasks and workflows.

- task
- workflow
- kwtypes
- current_context
- ExecutionParameters
- FlyteContext
- map_task
- ImperativeWorkflow
- create_node
- NodeOutput
- FlyteContextManager

> [!NOTE] Local Execution
> Tasks and Workflows can both be locally run, assuming the relevant tasks are capable of local execution.
> This is useful for unit testing.


Branching and Conditionals
==========================

Branches and conditionals can be expressed explicitly in Flyte. These conditions are evaluated
in the flyte engine and hence should be used for control flow. "dynamic workflows" can be used to perform custom conditional logic not supported by flytekit.

- conditional


Customizing Tasks & Workflows
==============================

- TaskMetadata - Wrapper object that allows users to specify Task
- Resources - Things like CPUs/Memory, etc.
- WorkflowFailurePolicy - Customizes what happens when a workflow fails.
- PodTemplate - Custom PodTemplate for a task.

Dynamic and Nested Workflows
==============================
See the Dynamic module for more information.

- dynamic

Signaling
=========

- approve
- sleep
- wait_for_input

Scheduling
============================

- CronSchedule
- FixedRate

Notifications
============================

- Email
- PagerDuty
- Slack

Reference Entities
====================

- get_reference_entity
- LaunchPlanReference
- TaskReference
- WorkflowReference
- reference_task
- reference_workflow
- reference_launch_plan

Core Task Types
=================

- SQLTask
- ContainerTask
- PythonFunctionTask
- PythonInstanceTask
- LaunchPlan

Secrets and SecurityContext
============================

- Secret
- SecurityContext


Common Flyte IDL Objects
=========================

- AuthRole
- Labels
- Annotations
- WorkflowExecutionPhase
- Blob
- BlobMetadata
- Literal
- Scalar
- LiteralType
- BlobType

Task Utilities
==============

- HashMethod

Artifacts
=========

- Artifact

Documentation
=============

- Description
- Documentation
- SourceCode

## Directory

### Classes

| Class | Description |
|-|-|
| [`Annotations`](.././flytekit#flytekitannotations) |  |
| [`Artifact`](.././flytekit#flytekitartifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`AuthRole`](.././flytekit#flytekitauthrole) |  |
| [`BatchSize`](.././flytekit#flytekitbatchsize) | This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. |
| [`Blob`](.././flytekit#flytekitblob) |  |
| [`BlobMetadata`](.././flytekit#flytekitblobmetadata) | This is metadata for the Blob literal. |
| [`BlobType`](.././flytekit#flytekitblobtype) | This type represents offloaded data and is typically used for things like files. |
| [`Cache`](.././flytekit#flytekitcache) | Cache configuration for a task. |
| [`CachePolicy`](.././flytekit#flytekitcachepolicy) | Base class for protocol classes. |
| [`Checkpoint`](.././flytekit#flytekitcheckpoint) | Base class for Checkpoint system. |
| [`Config`](.././flytekit#flytekitconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`ContainerTask`](.././flytekit#flytekitcontainertask) | This is an intermediate class that represents Flyte Tasks that run a container at execution time. |
| [`CronSchedule`](.././flytekit#flytekitcronschedule) | Use this when you have a launch plan that you want to run on a cron expression. |
| [`Deck`](.././flytekit#flytekitdeck) | Deck enable users to get customizable and default visibility into their tasks. |
| [`Description`](.././flytekit#flytekitdescription) | Full user description with formatting preserved. |
| [`Documentation`](.././flytekit#flytekitdocumentation) | DescriptionEntity contains detailed description for the task/workflow/launch plan. |
| [`Email`](.././flytekit#flytekitemail) | This notification should be used when sending regular emails to people. |
| [`Environment`](.././flytekit#flytekitenvironment) |  |
| [`ExecutionParameters`](.././flytekit#flytekitexecutionparameters) | This is a run-time user-centric context object that is accessible to every @task method. |
| [`FixedRate`](.././flytekit#flytekitfixedrate) | Use this class to schedule a fixed-rate interval for a launch plan. |
| [`FlyteContext`](.././flytekit#flytekitflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`FlyteContextManager`](.././flytekit#flytekitflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteDirectory`](.././flytekit#flytekitflytedirectory) |  |
| [`FlyteFile`](.././flytekit#flytekitflytefile) |  |
| [`FlyteRemote`](.././flytekit#flytekitflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`HashMethod`](.././flytekit#flytekithashmethod) | Flyte-specific object used to wrap the hash function for a specific type. |
| [`ImageSpec`](.././flytekit#flytekitimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`Labels`](.././flytekit#flytekitlabels) |  |
| [`LaunchPlan`](.././flytekit#flytekitlaunchplan) | Launch Plans are one of the core constructs of Flyte. |
| [`LaunchPlanReference`](.././flytekit#flytekitlaunchplanreference) | A reference object containing metadata that points to a remote launch plan. |
| [`Literal`](.././flytekit#flytekitliteral) |  |
| [`LiteralType`](.././flytekit#flytekitliteraltype) |  |
| [`Options`](.././flytekit#flytekitoptions) | These are options that can be configured for a launchplan during registration or overridden during an execution. |
| [`PagerDuty`](.././flytekit#flytekitpagerduty) | This notification should be used when sending emails to the PagerDuty service. |
| [`PodTemplate`](.././flytekit#flytekitpodtemplate) | Custom PodTemplate specification for a Task. |
| [`PythonFunctionTask`](.././flytekit#flytekitpythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`PythonInstanceTask`](.././flytekit#flytekitpythoninstancetask) | This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |
| [`Resources`](.././flytekit#flytekitresources) | This class is used to specify both resource requests and resource limits. |
| [`SQLTask`](.././flytekit#flytekitsqltask) | Base task types for all SQL tasks. |
| [`Scalar`](.././flytekit#flytekitscalar) |  |
| [`Secret`](.././flytekit#flytekitsecret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`SecurityContext`](.././flytekit#flytekitsecuritycontext) | This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`SensorEngine`](.././flytekit#flytekitsensorengine) | This is the base class for all async connectors. |
| [`Slack`](.././flytekit#flytekitslack) | This notification should be used when sending emails to the Slack. |
| [`SourceCode`](.././flytekit#flytekitsourcecode) | Link to source code used to define this task or workflow. |
| [`StructuredDataset`](.././flytekit#flytekitstructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetFormat`](.././flytekit#flytekitstructureddatasetformat) | str(object='') -> str. |
| [`StructuredDatasetTransformerEngine`](.././flytekit#flytekitstructureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`StructuredDatasetType`](.././flytekit#flytekitstructureddatasettype) |  |
| [`TaskMetadata`](.././flytekit#flytekittaskmetadata) | Metadata for a Task. |
| [`TaskReference`](.././flytekit#flytekittaskreference) | A reference object containing metadata that points to a remote task. |
| [`VersionParameters`](.././flytekit#flytekitversionparameters) | Parameters used for version hash generation. |
| [`Workflow`](.././flytekit#flytekitworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`WorkflowExecutionPhase`](.././flytekit#flytekitworkflowexecutionphase) | This class holds enum values used for setting notifications. |
| [`WorkflowFailurePolicy`](.././flytekit#flytekitworkflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`WorkflowReference`](.././flytekit#flytekitworkflowreference) | A reference object containing metadata that points to a remote workflow. |

### Methods

| Method | Description |
|-|-|
| [`approve()`](#approve) | Create a Gate object for binary approval. |
| [`conditional()`](#conditional) | Use a conditional section to control the flow of a workflow. |
| [`current_context()`](#current_context) | Use this method to get a handle of specific parameters available in a flyte task. |
| [`eager()`](#eager) | Eager workflow decorator. |
| [`entry_points()`](#entry_points) | Return EntryPoint objects for all installed packages. |
| [`get_reference_entity()`](#get_reference_entity) | See the documentation for :py:class:`flytekit. |
| [`kwtypes()`](#kwtypes) | This is a small helper function to convert the keyword arguments to an OrderedDict of types. |
| [`lazy_module()`](#lazy_module) | This function is used to lazily import modules. |
| [`load_implicit_plugins()`](#load_implicit_plugins) | This method allows loading all plugins that have the entrypoint specification. |
| [`map_task()`](#map_task) | Wrapper that creates a map task utilizing either the existing ArrayNodeMapTask. |
| [`new_context()`](#new_context) |  |
| [`reference_launch_plan()`](#reference_launch_plan) | A reference launch plan is a pointer to a launch plan that already exists on your Flyte installation. |
| [`reference_task()`](#reference_task) | A reference task is a pointer to a task that already exists on your Flyte installation. |
| [`reference_workflow()`](#reference_workflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`sleep()`](#sleep) | Create a sleep Gate object. |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |
| [`wait_for_input()`](#wait_for_input) | Create a Gate object that waits for user input of the specified type. |
| [`workflow()`](#workflow) | This decorator declares a function to be a Flyte workflow. |


### Variables

| Property | Type | Description |
|-|-|-|
| `LOGGING_RICH_FMT_ENV_VAR` | `str` |  |
| `logger` | `Logger` |  |

## Methods

#### approve()

```python
def approve(
    upstream_item: Union[Tuple[Promise], Promise, VoidPromise],
    name: str,
    timeout: datetime.timedelta,
)
```
Create a Gate object for binary approval.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type |
|-|-|
| `upstream_item` | `Union[Tuple[Promise], Promise, VoidPromise]` |
| `name` | `str` |
| `timeout` | `datetime.timedelta` |

#### conditional()

```python
def conditional(
    name: str,
) -> ConditionalSection
```
Use a conditional section to control the flow of a workflow. Conditional sections can only be used inside a workflow
context. Outside of a workflow they will raise an Assertion.

The ``conditional`` method returns a new conditional section, that allows to create a - ternary operator like
if-else clauses. The reason why it is called ternary-like is because, it returns the output of the branch result.
So in-effect it is a functional style condition.

Example of a condition usage. Note the nesting and the assignment to a LHS variable

.. code-block:: python

v = (
conditional("fractions")
.if_((my_input > 0.1) & (my_input < 1.0))
.then(
conditional("inner_fractions")
.if_(my_input < 0.5)
.then(double(n=my_input))
.elif_((my_input > 0.5) & (my_input < 0.7))
.then(square(n=my_input))
.else_()
.fail("Only <0.7 allowed")
)
.elif_((my_input > 1.0) & (my_input < 10.0))
.then(square(n=my_input))
.else_()
.then(double(n=my_input))
)


| Parameter | Type |
|-|-|
| `name` | `str` |

#### current_context()

```python
def current_context()
```
Use this method to get a handle of specific parameters available in a flyte task.

Usage

.. code-block:: python

flytekit.current_context().logging.info(...)

Available params are documented in :py:class:`flytekit.core.context_manager.ExecutionParams`.
There are some special params, that should be available


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
:py:class:`~flytekit.remote.remote.FlyteRemote` object to kick off executions when a flyte entity needs to produce a
value. Basically think about it as: every Flyte entity that is called(), the stack frame is an execution with its
own Flyte URL. Results (or the error) are fetched when the execution is finished.

For example:

.. code-block:: python

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

Unlike :py:func:`dynamic workflows <flytekit.dynamic>`, eager workflows are not compiled into a workflow spec, but
uses python's `async <https://docs.python.org/3/library/asyncio.html>`__ capabilities to execute flyte entities.

.. note::

Eager workflows only support `@task`, `@workflow`, and `@eager` entities. Conditionals are not supported, use a
plain Python if statement instead.

.. important::

A ``client_secret_group`` and ``client_secret_key`` is needed for authenticating via
:py:class:`~flytekit.remote.remote.FlyteRemote` using the ``client_credentials`` authentication, which is
configured via :py:class:`~flytekit.configuration.PlatformConfig`.

.. code-block:: python

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

Where ``config.yaml`` contains is a flytectl-compatible config file.
For more details, see `here <https://docs.flyte.org/en/latest/flytectl/overview.html#configuration>`__.

When using a sandbox cluster started with ``flytectl demo start``, however, the ``client_secret_group``
and ``client_secret_key`` are not needed, :

.. code-block:: python

@eager
async def eager_workflow(x: int) -> int:
...


| Parameter | Type |
|-|-|
| `_fn` |  |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### entry_points()

```python
def entry_points(
    params,
) -> EntryPoints
```
Return EntryPoint objects for all installed packages.

Pass selection parameters (group or name) to filter the
result to entry points matching those properties (see
EntryPoints.select()).

:return: EntryPoints for all installed packages.


| Parameter | Type |
|-|-|
| `params` |  |

#### get_reference_entity()

```python
def get_reference_entity(
    resource_type: int,
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
See the documentation for :py:class:`flytekit.reference_task` and :py:class:`flytekit.reference_workflow` as well.

This function is the general form of the two aforementioned functions. It's better for programmatic usage, as
the interface is passed in as arguments instead of analyzed from type annotations.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
:start-after: # docs_ref_start
:end-before: # docs_ref_end
:language: python
:dedent: 4



| Parameter | Type |
|-|-|
| `resource_type` | `int` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

#### kwtypes()

```python
def kwtypes(
    kwargs,
) -> typing.OrderedDict[str, typing.Type]
```
This is a small helper function to convert the keyword arguments to an OrderedDict of types.

.. code-block:: python

kwtypes(a=int, b=str)


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### lazy_module()

```python
def lazy_module(
    fullname,
)
```
This function is used to lazily import modules.  It is used in the following way:
.. code-block:: python
from flytekit.lazy_import import lazy_module
sklearn = lazy_module("sklearn")
sklearn.svm.SVC()


| Parameter | Type |
|-|-|
| `fullname` |  |

#### load_implicit_plugins()

```python
def load_implicit_plugins()
```
This method allows loading all plugins that have the entrypoint specification. This uses the plugin loading
behavior as explained `here <>`_.

This is an opt in system and plugins that have an implicit loading requirement should add the implicit loading
entrypoint specification to their setup.py. The following example shows how we can autoload a module called fsspec
(whose init files contains the necessary plugin registration step)

.. code-block::

# note the group is always ``flytekit.plugins``
setup(
...
entry_points={'flytekit.plugins': 'fsspec=flytekitplugins.fsspec'},
...
)

This works as long as the fsspec module has

.. code-block::

# For data persistence plugins
DataPersistencePlugins.register_plugin(f"{k}://", FSSpecPersistence, force=True)
# OR for type plugins
TypeEngine.register(PanderaTransformer())
# etc


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



| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.launch_plan.LaunchPlan, flytekit.core.python_function_task.PythonFunctionTask, ForwardRef('FlyteLaunchPlan')]` |
| `concurrency` | `typing.Optional[int]` |
| `min_successes` | `typing.Optional[int]` |
| `min_success_ratio` | `float` |
| `kwargs` | ``**kwargs`` |

#### new_context()

```python
def new_context()
```
#### reference_launch_plan()

```python
def reference_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> Callable[[Callable[..., Any]], ReferenceLaunchPlan]
```
A reference launch plan is a pointer to a launch plan that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface
via the function definition.

If at registration time the interface provided causes an issue with compilation, an error will be returned.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

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

.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
:pyobject: ref_t1


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### reference_workflow()

```python
def reference_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> Callable[[Callable[..., Any]], ReferenceWorkflow]
```
A reference workflow is a pointer to a workflow that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.

Example:

.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
:pyobject: ref_wf1


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### sleep()

```python
def sleep(
    duration: datetime.timedelta,
)
```
Create a sleep Gate object.



| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |

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

#### wait_for_input()

```python
def wait_for_input(
    name: str,
    timeout: datetime.timedelta,
    expected_type: typing.Type,
)
```
Create a Gate object that waits for user input of the specified type.

Create a Gate object. This object will function like a task. Note that unlike a task,
each time this function is called, a new Python object is created. If a workflow
calls a subworkflow twice, and the subworkflow has a signal, then two Gate
objects are created. This shouldn't be a problem as long as the objects are identical.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `timeout` | `datetime.timedelta` |
| `expected_type` | `typing.Type` |

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

.. literalinclude:: ../../../tests/flytekit/unit/core/test_workflows.py
:pyobject: my_wf_example

Again, users should keep in mind that even though the body of the function looks like regular Python, it is
actually not. When flytekit scans the workflow function, the objects being passed around between the tasks are not
your typical Python values. So even though you may have a task ``t1() -> int``, when ``a = t1()`` is called, ``a``
will not be an integer so if you try to ``range(a)`` you'll get an error.

Please see the :ref:`user guide <cookbook:workflow>` for more usage examples.



| Parameter | Type |
|-|-|
| `_workflow_function` | `Optional[Callable[P, FuncOut]]` |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` |
| `interruptible` | `bool` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `pickle_untyped` | `bool` |
| `default_options` | `Optional[Options]` |

## flytekit.Annotations

```python
class Annotations(
    values,
)
```
Annotation values to be applied to a workflow execution resource.



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Annotations
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

## flytekit.Artifact

An Artifact is effectively just a metadata layer on top of data that exists in Flyte. Most data of interest
will be the output of tasks and workflows. The other category is user uploads.

This Python class has limited purpose, as a way for users to specify that tasks/workflows create Artifacts
and the manner (i.e. name, partitions) in which they are created.

Control creation parameters at task/workflow execution time ::

@task
def t1() -> Annotated[nn.Module, Artifact(name="my.artifact.name")]:
...


```python
class Artifact(
    project: Optional[str],
    domain: Optional[str],
    name: Optional[str],
    version: Optional[str],
    time_partitioned: bool,
    time_partition: Optional[TimePartition],
    time_partition_granularity: Optional[Granularity],
    partition_keys: Optional[typing.List[str]],
    partitions: Optional[Union[Partitions, typing.Dict[str, str]]],
)
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `name` | `Optional[str]` |
| `version` | `Optional[str]` |
| `time_partitioned` | `bool` |
| `time_partition` | `Optional[TimePartition]` |
| `time_partition_granularity` | `Optional[Granularity]` |
| `partition_keys` | `Optional[typing.List[str]]` |
| `partitions` | `Optional[Union[Partitions, typing.Dict[str, str]]]` |

### Methods

| Method | Description |
|-|-|
| [`create_from()`](#create_from) | This function allows users to declare partition values dynamically from the body of a task. |
| [`embed_as_query()`](#embed_as_query) | This should only be called in the context of a Trigger. |
| [`query()`](#query) |  |
| [`to_id_idl()`](#to_id_idl) | Converts this object to the IDL representation. |


#### create_from()

```python
def create_from(
    o: O,
    card: Optional[SerializableToString],
    args: `*args`,
    kwargs,
) -> O
```
This function allows users to declare partition values dynamically from the body of a task. Note that you'll
still need to annotate your task function output with the relevant Artifact object. Below, one of the partition
values is bound to an input, and the other is set at runtime. Note that since tasks are not run at compile
time, flytekit cannot check that you've bound all the partition values. It's up to you to ensure that you've
done so.

Pricing = Artifact(name="pricing", partition_keys=["region"])
EstError = Artifact(name="estimation_error", partition_keys=["dataset"], time_partitioned=True)

@task
def t1() -> Annotated[pd.DataFrame, Pricing], Annotated[float, EstError]:
df = get_pricing_results()
dt = get_time()
return Pricing.create_from(df, region="dubai"),             EstError.create_from(msq_error, dataset="train", time_partition=dt)

You can mix and match with the input syntax as well.

@task
def my_task() -> Annotated[pd.DataFrame, RideCountData(region=Inputs.region)]:
...
return RideCountData.create_from(df, time_partition=datetime.datetime.now())


| Parameter | Type |
|-|-|
| `o` | `O` |
| `card` | `Optional[SerializableToString]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### embed_as_query()

```python
def embed_as_query(
    partition: Optional[str],
    bind_to_time_partition: Optional[bool],
    expr: Optional[str],
    op: Optional[Op],
) -> art_id.ArtifactQuery
```
This should only be called in the context of a Trigger. The type of query this returns is different from the
query() function. This type of query is used to reference the triggering artifact, rather than running a query.


| Parameter | Type |
|-|-|
| `partition` | `Optional[str]` |
| `bind_to_time_partition` | `Optional[bool]` |
| `expr` | `Optional[str]` |
| `op` | `Optional[Op]` |

#### query()

```python
def query(
    project: Optional[str],
    domain: Optional[str],
    time_partition: Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]],
    partitions: Optional[Union[typing.Dict[str, str], Partitions]],
    kwargs,
) -> ArtifactQuery
```
| Parameter | Type |
|-|-|
| `project` | `Optional[str]` |
| `domain` | `Optional[str]` |
| `time_partition` | `Optional[Union[datetime.datetime, TimePartition, art_id.InputBindingData]]` |
| `partitions` | `Optional[Union[typing.Dict[str, str], Partitions]]` |
| `kwargs` | ``**kwargs`` |

#### to_id_idl()

```python
def to_id_idl()
```
Converts this object to the IDL representation.
This is here instead of translator because it's in the interface, a relatively simple proto object
that's exposed to the user.


### Properties

| Property | Type | Description |
|-|-|-|
| `concrete_artifact_id` |  |  |
| `partitions` |  |  |
| `time_partition` |  |  |

## flytekit.AuthRole

```python
class AuthRole(
    assumable_iam_role,
    kubernetes_service_account,
)
```
Auth configuration for IAM or K8s service account.

Either one or both of the assumable IAM role and/or the K8s service account can be set.



| Parameter | Type |
|-|-|
| `assumable_iam_role` |  |
| `kubernetes_service_account` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Auth
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | {{< multiline >}}The IAM role to execute the workflow with
{{< /multiline >}} |
| `is_empty` |  |  |
| `kubernetes_service_account` |  | {{< multiline >}}The kubernetes service account to execute the workflow with
{{< /multiline >}} |

## flytekit.BatchSize

This is used to annotate a FlyteDirectory when we want to download/upload the contents of the directory in batches. For example,

```python
@task
def t1(directory: Annotated[FlyteDirectory, BatchSize(10)]) -> Annotated[FlyteDirectory, BatchSize(100)]:
...
return FlyteDirectory(...)
```

In the above example flytekit will download all files from the input `directory` in chunks of 10, i.e. first it
downloads 10 files, loads them to memory, then writes those 10 to local disk, then it loads the next 10, so on
and so forth. Similarly, for outputs, in this case flytekit is going to upload the resulting directory in chunks of
100.


```python
class BatchSize(
    val: int,
)
```
| Parameter | Type |
|-|-|
| `val` | `int` |

### Properties

| Property | Type | Description |
|-|-|-|
| `val` |  |  |

## flytekit.Blob

```python
class Blob(
    metadata,
    uri,
)
```
This literal model is used to represent binary data offloaded to some storage location which is
identifiable with a unique string. See :py:class:`flytekit.FlyteFile` as an example.



| Parameter | Type |
|-|-|
| `metadata` |  |
| `uri` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> Blob
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `metadata` |  |  |
| `uri` |  |  |

## flytekit.BlobMetadata

This is metadata for the Blob literal.


```python
class BlobMetadata(
    type,
)
```
| Parameter | Type |
|-|-|
| `type` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> BlobMetadata
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `type` |  |  |

## flytekit.BlobType

This type represents offloaded data and is typically used for things like files.


```python
class BlobType(
    format,
    dimensionality,
)
```
| Parameter | Type |
|-|-|
| `format` |  |
| `dimensionality` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> BlobType
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `dimensionality` |  | {{< multiline >}}An integer from BlobType.BlobDimensionality enum
{{< /multiline >}} |
| `format` |  | {{< multiline >}}A string describing the format of the underlying blob data.
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.Cache

Cache configuration for a task.



```python
class Cache(
    version: typing.Optional[str],
    serialize: bool,
    ignored_inputs: typing.Union[typing.Tuple[str, ...], str],
    salt: str,
    policies: typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType],
)
```
| Parameter | Type |
|-|-|
| `version` | `typing.Optional[str]` |
| `serialize` | `bool` |
| `ignored_inputs` | `typing.Union[typing.Tuple[str, ...], str]` |
| `salt` | `str` |
| `policies` | `typing.Union[typing.List[flytekit.core.cache.CachePolicy], flytekit.core.cache.CachePolicy, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`get_ignored_inputs()`](#get_ignored_inputs) |  |
| [`get_version()`](#get_version) |  |


#### get_ignored_inputs()

```python
def get_ignored_inputs()
```
#### get_version()

```python
def get_version(
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type |
|-|-|
| `params` | `flytekit.core.cache.VersionParameters` |

## flytekit.CachePolicy

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
class CachePolicy(
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
| [`get_version()`](#get_version) |  |


#### get_version()

```python
def get_version(
    salt: str,
    params: flytekit.core.cache.VersionParameters,
) -> str
```
| Parameter | Type |
|-|-|
| `salt` | `str` |
| `params` | `flytekit.core.cache.VersionParameters` |

## flytekit.Checkpoint

Base class for Checkpoint system. Checkpoint system allows reading and writing custom checkpoints from user
scripts


### Methods

| Method | Description |
|-|-|
| [`prev_exists()`](#prev_exists) |  |
| [`read()`](#read) | This should only be used if there is a singular checkpoint file written. |
| [`restore()`](#restore) | Given a path, if a previous checkpoint exists, will be downloaded to this path. |
| [`save()`](#save) | . |
| [`write()`](#write) | This will overwrite the checkpoint. |


#### prev_exists()

```python
def prev_exists()
```
#### read()

```python
def read()
```
This should only be used if there is a singular checkpoint file written. If more than one checkpoint file is
found, this will raise a ValueError


#### restore()

```python
def restore(
    path: typing.Union[pathlib._local.Path, str],
) -> typing.Optional[pathlib._local.Path]
```
Given a path, if a previous checkpoint exists, will be downloaded to this path.
If download is successful the downloaded path is returned

.. note:

Download will not be performed, if the checkpoint was previously restored. The method will return the
previously downloaded path.


| Parameter | Type |
|-|-|
| `path` | `typing.Union[pathlib._local.Path, str]` |

#### save()

```python
def save(
    cp: typing.Union[pathlib._local.Path, str, _io.BufferedReader],
)
```
| Parameter | Type |
|-|-|
| `cp` | `typing.Union[pathlib._local.Path, str, _io.BufferedReader]` |

#### write()

```python
def write(
    b: bytes,
)
```
This will overwrite the checkpoint. It can be retrieved using read or restore


| Parameter | Type |
|-|-|
| `b` | `bytes` |

## flytekit.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task



```python
class Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
)
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default. |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`. |
| [`with_params()`](#with_params) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
) -> Config
```
Automatically constructs the Config Object. The order of precedence is as follows
1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
2. If not found in environment then values ar read from the config file
3. If not found in the file, then the default values are used.



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
) -> Config
```
Creates an automatic config for the given endpoint and uses the config_file or environment variable for default.
Refer to `Config.auto()` to understand the default bootstrap behavior.

data_config can be used to configure how data is downloaded or uploaded to a specific Blob storage like S3 / GCS etc.
But, for permissions to a specific backend just use Cloud providers reqcommendation. If using fsspec, then
refer to fsspec documentation


| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |

#### for_sandbox()

```python
def for_sandbox()
```
Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`.
If you are using a hosted Sandbox like environment, then you may need to use port-forward or ingress urls
:return: Config


#### with_params()

```python
def with_params(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
) -> Config
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

## flytekit.ContainerTask

This is an intermediate class that represents Flyte Tasks that run a container at execution time. This is the vast
majority of tasks - the typical ``@task`` decorated tasks for instance all run a container. An example of
something that doesn't run a container would be something like the Athena SQL task.


```python
class ContainerTask(
    name: str,
    image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec],
    command: typing.List[str],
    inputs: typing.Optional[typing.OrderedDict[str, typing.Type]],
    metadata: typing.Optional[flytekit.core.base_task.TaskMetadata],
    arguments: typing.Optional[typing.List[str]],
    outputs: typing.Optional[typing.Dict[str, typing.Type]],
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
    input_data_dir: typing.Optional[str],
    output_data_dir: typing.Optional[str],
    metadata_format: <enum 'MetadataFormat'>,
    io_strategy: typing.Optional[flytekit.core.container_task.ContainerTask.IOStrategy],
    secret_requests: typing.Optional[typing.List[flytekit.models.security.Secret]],
    pod_template: typing.Optional[ForwardRef('PodTemplate')],
    pod_template_name: typing.Optional[str],
    local_logs: bool,
    resources: typing.Optional[flytekit.core.resources.Resources],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec]` |
| `command` | `typing.List[str]` |
| `inputs` | `typing.Optional[typing.OrderedDict[str, typing.Type]]` |
| `metadata` | `typing.Optional[flytekit.core.base_task.TaskMetadata]` |
| `arguments` | `typing.Optional[typing.List[str]]` |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `input_data_dir` | `typing.Optional[str]` |
| `output_data_dir` | `typing.Optional[str]` |
| `metadata_format` | `<enum 'MetadataFormat'>` |
| `io_strategy` | `typing.Optional[flytekit.core.container_task.ContainerTask.IOStrategy]` |
| `secret_requests` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` |
| `pod_template` | `typing.Optional[ForwardRef('PodTemplate')]` |
| `pod_template_name` | `typing.Optional[str]` |
| `local_logs` | `bool` |
| `resources` | `typing.Optional[flytekit.core.resources.Resources]` |
| `kwargs` | ``**kwargs`` |

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
) -> flytekit.models.literals.LiteralMap
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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
) -> typing.Optional[typing.Dict[str, typing.Any]]
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
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.CronSchedule

Use this when you have a launch plan that you want to run on a cron expression.
This uses standard `cron format <https://docs.flyte.org/en/latest/concepts/schedules.html#cron-expression-table>`__
in case where you are using default native scheduler using the schedule attribute.

.. code-block::

CronSchedule(
schedule="*/1 * * * *",  # Following schedule runs every min
)

See the :std:ref:`User Guide <cookbook:cron schedules>` for further examples.


```python
class CronSchedule(
    cron_expression: typing.Optional[str],
    schedule: typing.Optional[str],
    offset: typing.Optional[str],
    kickoff_time_input_arg: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `cron_expression` | `typing.Optional[str]` |
| `schedule` | `typing.Optional[str]` |
| `offset` | `typing.Optional[str]` |
| `kickoff_time_input_arg` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Schedule
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `cron_expression` |  |  |
| `cron_schedule` |  |  |
| `is_empty` |  |  |
| `kickoff_time_input_arg` |  |  |
| `rate` |  |  |
| `schedule_expression` |  |  |

## flytekit.Deck

Deck enable users to get customizable and default visibility into their tasks.

Deck contains a list of renderers (FrameRenderer, MarkdownRenderer) that can
generate a html file. For example, FrameRenderer can render a DataFrame as an HTML table,
MarkdownRenderer can convert Markdown string to HTML

Flyte context saves a list of deck objects, and we use renderers in those decks to render
the data and create an HTML file when those tasks are executed

Each task has a least three decks (input, output, default). Input/output decks are
used to render tasks' input/output data, and the default deck is used to render line plots,
scatter plots or Markdown text. In addition, users can create new decks to render
their data with custom renderers.

.. code-block:: python

iris_df = px.data.iris()

@task()
def t1() -> str:
md_text = '#Hello Flyte##Hello Flyte###Hello Flyte'
m = MarkdownRenderer()
s = BoxRenderer("sepal_length")
deck = flytekit.Deck("demo", s.to_html(iris_df))
deck.append(m.to_html(md_text))
default_deck = flytekit.current_context().default_deck
default_deck.append(m.to_html(md_text))
return md_text


# Use Annotated to override default renderer
@task()
def t2() -> Annotated[pd.DataFrame, TopFrameRenderer(10)]:
return iris_df


```python
class Deck(
    name: str,
    html: typing.Optional[str],
    auto_add_to_deck: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `html` | `typing.Optional[str]` |
| `auto_add_to_deck` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`append()`](#append) |  |
| [`publish()`](#publish) |  |


#### append()

```python
def append(
    html: str,
) -> Deck
```
| Parameter | Type |
|-|-|
| `html` | `str` |

#### publish()

```python
def publish()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `html` |  |  |
| `name` |  |  |

## flytekit.Description

Full user description with formatting preserved. This can be rendered
by clients, such as the console or command line tools with in-tact
formatting.


```python
class Description(
    value: typing.Optional[str],
    uri: typing.Optional[str],
    icon_link: typing.Optional[str],
    format: <enum 'DescriptionFormat'>,
)
```
| Parameter | Type |
|-|-|
| `value` | `typing.Optional[str]` |
| `uri` | `typing.Optional[str]` |
| `icon_link` | `typing.Optional[str]` |
| `format` | `<enum 'DescriptionFormat'>` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.Description,
) -> Description
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.Description` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.Documentation

DescriptionEntity contains detailed description for the task/workflow/launch plan.
Documentation could provide insight into the algorithms, business use case, etc.


```python
class Documentation(
    short_description: typing.Optional[str],
    long_description: typing.Optional[flytekit.models.documentation.Description],
    source_code: typing.Optional[flytekit.models.documentation.SourceCode],
)
```
| Parameter | Type |
|-|-|
| `short_description` | `typing.Optional[str]` |
| `long_description` | `typing.Optional[flytekit.models.documentation.Description]` |
| `source_code` | `typing.Optional[flytekit.models.documentation.SourceCode]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.DescriptionEntity,
) -> Documentation
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.DescriptionEntity` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.Email

This notification should be used when sending regular emails to people.

.. code-block:: python

from flytekit.models.core.execution import WorkflowExecutionPhase

Email(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])


```python
class Email(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> Notification
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `email` |  |  |
| `is_empty` |  |  |
| `pager_duty` |  |  |
| `phases` |  | {{< multiline >}}A list of phases to which users can associate the notifications.
{{< /multiline >}} |
| `slack` |  |  |

## flytekit.Environment

```python
class Environment(
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
)
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

### Methods

| Method | Description |
|-|-|
| [`dynamic()`](#dynamic) | Please first see the comments for :py:func:`flytekit. |
| [`extend()`](#extend) | This is the core decorator to use for any task type in flytekit. |
| [`show()`](#show) |  |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |
| [`update()`](#update) | This is the core decorator to use for any task type in flytekit. |


#### dynamic()

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
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
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

#### extend()

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

#### show()

```python
def show()
```
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

#### update()

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

## flytekit.ExecutionParameters

This is a run-time user-centric context object that is accessible to every @task method. It can be accessed using

.. code-block:: python

flytekit.current_context()

This object provides the following
* a statsd handler
* a logging handler
* the execution ID as an :py:class:`flytekit.models.core.identifier.WorkflowExecutionIdentifier` object
* a working directory for the user to write arbitrary files to

Please do not confuse this object with the :py:class:`flytekit.FlyteContext` object.


```python
class ExecutionParameters(
    execution_date,
    tmp_dir,
    stats,
    execution_id: typing.Optional[_identifier.WorkflowExecutionIdentifier],
    logging,
    raw_output_prefix,
    output_metadata_prefix,
    checkpoint,
    decks,
    task_id: typing.Optional[_identifier.Identifier],
    enable_deck: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `execution_date` |  |
| `tmp_dir` |  |
| `stats` |  |
| `execution_id` | `typing.Optional[_identifier.WorkflowExecutionIdentifier]` |
| `logging` |  |
| `raw_output_prefix` |  |
| `output_metadata_prefix` |  |
| `checkpoint` |  |
| `decks` |  |
| `task_id` | `typing.Optional[_identifier.Identifier]` |
| `enable_deck` | `bool` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`builder()`](#builder) |  |
| [`get()`](#get) | Returns task specific context if present else raise an error. |
| [`has_attr()`](#has_attr) |  |
| [`new_builder()`](#new_builder) |  |
| [`with_enable_deck()`](#with_enable_deck) |  |
| [`with_task_sandbox()`](#with_task_sandbox) |  |


#### builder()

```python
def builder()
```
#### get()

```python
def get(
    key: str,
) -> typing.Any
```
Returns task specific context if present else raise an error. The returned context will match the key


| Parameter | Type |
|-|-|
| `key` | `str` |

#### has_attr()

```python
def has_attr(
    attr_name: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `attr_name` | `str` |

#### new_builder()

```python
def new_builder(
    current: Optional[ExecutionParameters],
) -> Builder
```
| Parameter | Type |
|-|-|
| `current` | `Optional[ExecutionParameters]` |

#### with_enable_deck()

```python
def with_enable_deck(
    enable_deck: bool,
) -> Builder
```
| Parameter | Type |
|-|-|
| `enable_deck` | `bool` |

#### with_task_sandbox()

```python
def with_task_sandbox()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `checkpoint` |  |  |
| `decks` |  | {{< multiline >}}A list of decks of the tasks, and it will be rendered to a html at the end of the task execution.
{{< /multiline >}} |
| `default_deck` |  |  |
| `enable_deck` |  | {{< multiline >}}Returns whether deck is enabled or not
{{< /multiline >}} |
| `execution_date` |  | {{< multiline >}}This is a datetime representing the time at which a workflow was started.  This is consistent across all tasks
executed in a workflow or sub-workflow.

.. note::

Do NOT use this execution_date to drive any production logic.  It might be useful as a tag for data to help
in debugging.
{{< /multiline >}} |
| `execution_id` |  | {{< multiline >}}This is the identifier of the workflow execution within the underlying engine.  It will be consistent across all
task executions in a workflow or sub-workflow execution.

.. note::

Do NOT use this execution_id to drive any production logic.  This execution ID should only be used as a tag
on output data to link back to the workflow run that created it.
{{< /multiline >}} |
| `logging` |  | {{< multiline >}}A handle to a useful logging object.
TODO: Usage examples
{{< /multiline >}} |
| `output_metadata_prefix` |  |  |
| `raw_output_prefix` |  |  |
| `secrets` |  |  |
| `stats` |  | {{< multiline >}}A handle to a special statsd object that provides usefully tagged stats.
TODO: Usage examples and better comments
{{< /multiline >}} |
| `task_id` |  | {{< multiline >}}At production run-time, this will be generated by reading environment variables that are set
by the backend.
{{< /multiline >}} |
| `timeline_deck` |  |  |
| `working_directory` |  | {{< multiline >}}A handle to a special working directory for easily producing temporary files.
TODO: Usage examples
{{< /multiline >}} |

## flytekit.FixedRate

Use this class to schedule a fixed-rate interval for a launch plan.

.. code-block:: python

from datetime import timedelta

FixedRate(duration=timedelta(minutes=10))

See the :std:ref:`fixed rate intervals` chapter in the cookbook for additional usage examples.


```python
class FixedRate(
    duration: datetime.timedelta,
    kickoff_time_input_arg: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |
| `kickoff_time_input_arg` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Schedule
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `cron_expression` |  |  |
| `cron_schedule` |  |  |
| `is_empty` |  |  |
| `kickoff_time_input_arg` |  |  |
| `rate` |  |  |
| `schedule_expression` |  |  |

## flytekit.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
class FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
)
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility. |
| [`enter_conditional_section()`](#enter_conditional_section) |  |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution. |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) |  |
| [`new_builder()`](#new_builder) |  |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state. |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state. |
| [`set_stackframe()`](#set_stackframe) |  |
| [`with_client()`](#with_client) |  |
| [`with_compilation_state()`](#with_compilation_state) |  |
| [`with_execution_state()`](#with_execution_state) |  |
| [`with_file_access()`](#with_file_access) |  |
| [`with_new_compilation_state()`](#with_new_compilation_state) |  |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) |  |
| [`with_serialization_settings()`](#with_serialization_settings) |  |
| [`with_worker_queue()`](#with_worker_queue) |  |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
) -> CompilationState
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
) -> ExecutionState
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
)
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
) -> Builder
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
) -> Builder
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
) -> Builder
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
) -> Builder
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
) -> Builder
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| `user_space_params` |  |  |

## flytekit.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
) -> traceback.FrameSummary
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
) -> FlyteContext
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.FlyteDirectory

```python
class FlyteDirectory(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Optional[typing.Callable],
    remote_directory: typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]],
)
```
| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Optional[typing.Callable]` |
| `remote_directory` | `typing.Optional[typing.Union[os.PathLike, str, typing.Literal[False]]]` |

### Methods

| Method | Description |
|-|-|
| [`crawl()`](#crawl) | Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory". |
| [`deserialize_flyte_dir()`](#deserialize_flyte_dir) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteDirectory object with the remote source set to the input. |
| [`listdir()`](#listdir) | This function will list all files and folders in the given directory, but without downloading the contents. |
| [`new()`](#new) | Create a new FlyteDirectory object in current Flyte working directory. |
| [`new_dir()`](#new_dir) | This will create a new folder under the current folder. |
| [`new_file()`](#new_file) | This will create a new file under the current folder. |
| [`new_remote()`](#new_remote) | Create a new FlyteDirectory object using the currently configured default remote in the context (i. |
| [`schema()`](#schema) |  |
| [`serialize_flyte_dir()`](#serialize_flyte_dir) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### crawl()

```python
def crawl(
    maxdepth: typing.Optional[int],
    topdown: bool,
    kwargs,
) -> Generator[Tuple[typing.Union[str, os.PathLike[Any]], typing.Dict[Any, Any]], None, None]
```
Crawl returns a generator of all files prefixed by any sub-folders under the given "FlyteDirectory".
if details=True is passed, then it will return a dictionary as specified by fsspec.

Example:

>>> list(fd.crawl())
[("/base", "file1"), ("/base", "dir1/file1"), ("/base", "dir2/file1"), ("/base", "dir1/dir/file1")]

>>> list(x.crawl(detail=True))
[('/tmp/test', {'my-dir/ab.py': {'name': '/tmp/test/my-dir/ab.py', 'size': 0, 'type': 'file',
'created': 1677720780.2318847, 'islink': False, 'mode': 33188, 'uid': 501, 'gid': 0,
'mtime': 1677720780.2317934, 'ino': 1694329, 'nlink': 1}})]


| Parameter | Type |
|-|-|
| `maxdepth` | `typing.Optional[int]` |
| `topdown` | `bool` |
| `kwargs` | ``**kwargs`` |

#### deserialize_flyte_dir()

```python
def deserialize_flyte_dir(
    info,
) -> FlyteDirectory
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### listdir()

```python
def listdir(
    directory: FlyteDirectory,
) -> typing.List[typing.Union[FlyteDirectory, FlyteFile]]
```
This function will list all files and folders in the given directory, but without downloading the contents.
In addition, it will return a list of FlyteFile and FlyteDirectory objects that have ability to lazily download the
contents of the file/folder. For example:

.. code-block:: python

entity = FlyteDirectory.listdir(directory)
for e in entity:
print("s3 object:", e.remote_source)
# s3 object: s3://test-flytedir/file1.txt
# s3 object: s3://test-flytedir/file2.txt
# s3 object: s3://test-flytedir/sub_dir

open(entity[0], "r")  # This will download the file to the local disk.
open(entity[0], "r")  # flytekit will read data from the local disk if you open it again.


| Parameter | Type |
|-|-|
| `directory` | `FlyteDirectory` |

#### new()

```python
def new(
    dirname: str | os.PathLike,
) -> FlyteDirectory
```
Create a new FlyteDirectory object in current Flyte working directory.


| Parameter | Type |
|-|-|
| `dirname` | `str \| os.PathLike` |

#### new_dir()

```python
def new_dir(
    name: typing.Optional[str],
) -> FlyteDirectory
```
This will create a new folder under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_file()

```python
def new_file(
    name: typing.Optional[str],
) -> FlyteFile
```
This will create a new file under the current folder.
If given a name, it will use the name given, otherwise it'll pick a random string.
Collisions are not checked.


| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |

#### new_remote()

```python
def new_remote(
    stem: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteDirectory
```
Create a new FlyteDirectory object using the currently configured default remote in the context (i.e.
the raw_output_prefix configured in the current FileAccessProvider object in the context).
This is used if you explicitly have a folder somewhere that you want to create files under.
If you want to write a whole folder, you can let your task return a FlyteDirectory object,
and let flytekit handle the uploading.



| Parameter | Type |
|-|-|
| `stem` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### serialize_flyte_dir()

```python
def serialize_flyte_dir()
```
#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_directory` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is s3://something, flytekit will download the
directory for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |
| `sep` |  |  |

## flytekit.FlyteFile

```python
class FlyteFile(
    path: typing.Union[str, os.PathLike],
    downloader: typing.Callable,
    remote_path: typing.Optional[typing.Union[os.PathLike, str, bool]],
    metadata: typing.Optional[dict[str, str]],
)
```
FlyteFile's init method.



| Parameter | Type |
|-|-|
| `path` | `typing.Union[str, os.PathLike]` |
| `downloader` | `typing.Callable` |
| `remote_path` | `typing.Optional[typing.Union[os.PathLike, str, bool]]` |
| `metadata` | `typing.Optional[dict[str, str]]` |

### Methods

| Method | Description |
|-|-|
| [`deserialize_flyte_file()`](#deserialize_flyte_file) |  |
| [`download()`](#download) |  |
| [`extension()`](#extension) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_source()`](#from_source) | Create a new FlyteFile object with the remote source set to the input. |
| [`new()`](#new) | Create a new FlyteFile object in the current Flyte working directory. |
| [`new_remote_file()`](#new_remote_file) | Create a new FlyteFile object with a remote path. |
| [`open()`](#open) | Returns a streaming File handle. |
| [`serialize_flyte_file()`](#serialize_flyte_file) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### deserialize_flyte_file()

```python
def deserialize_flyte_file(
    info,
) -> 'FlyteFile'
```
| Parameter | Type |
|-|-|
| `info` |  |

#### download()

```python
def download()
```
#### extension()

```python
def extension()
```
#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_source()

```python
def from_source(
    source: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object with the remote source set to the input


| Parameter | Type |
|-|-|
| `source` | `str \| os.PathLike` |

#### new()

```python
def new(
    filename: str | os.PathLike,
) -> FlyteFile
```
Create a new FlyteFile object in the current Flyte working directory


| Parameter | Type |
|-|-|
| `filename` | `str \| os.PathLike` |

#### new_remote_file()

```python
def new_remote_file(
    name: typing.Optional[str],
    alt: typing.Optional[str],
) -> FlyteFile
```
Create a new FlyteFile object with a remote path.



| Parameter | Type |
|-|-|
| `name` | `typing.Optional[str]` |
| `alt` | `typing.Optional[str]` |

#### open()

```python
def open(
    mode: str,
    cache_type: typing.Optional[str],
    cache_options: typing.Optional[typing.Dict[str, typing.Any]],
)
```
Returns a streaming File handle

.. code-block:: python

@task
def copy_file(ff: FlyteFile) -> FlyteFile:
new_file = FlyteFile.new_remote_file()
with ff.open("rb", cache_type="readahead") as r:
with new_file.open("wb") as w:
w.write(r.read())
return new_file



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `cache_type` | `typing.Optional[str]` |
| `cache_options` | `typing.Optional[typing.Dict[str, typing.Any]]` |

#### serialize_flyte_file()

```python
def serialize_flyte_file()
```
#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `downloaded` |  |  |
| `remote_path` |  |  |
| `remote_source` |  | {{< multiline >}}If this is an input to a task, and the original path is an ``s3`` bucket, Flytekit downloads the
file for the user. In case the user wants access to the original path, it will be here.
{{< /multiline >}} |

## flytekit.FlyteRemote

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
class FlyteRemote(
    config: Config,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: typing.Optional[bool],
    kwargs,
)
```
Initialize a FlyteRemote object.

:type kwargs: All arguments that can be passed to create the SynchronousFlyteClient. These are usually grpc
parameters, if you want to customize credentials, ssl handling etc.


| Parameter | Type |
|-|-|
| `config` | `Config` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `typing.Optional[bool]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated. |
| [`approve()`](#approve) | . |
| [`auto()`](#auto) |  |
| [`download()`](#download) | Download the data to the specified location. |
| [`execute()`](#execute) | Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity. |
| [`execute_local_launch_plan()`](#execute_local_launch_plan) | Execute a locally defined `LaunchPlan`. |
| [`execute_local_task()`](#execute_local_task) | Execute a @task-decorated function or TaskTemplate task. |
| [`execute_local_workflow()`](#execute_local_workflow) | Execute an @workflow decorated function. |
| [`execute_reference_launch_plan()`](#execute_reference_launch_plan) | Execute a ReferenceLaunchPlan. |
| [`execute_reference_task()`](#execute_reference_task) | Execute a ReferenceTask. |
| [`execute_reference_workflow()`](#execute_reference_workflow) | Execute a ReferenceWorkflow. |
| [`execute_remote_task_lp()`](#execute_remote_task_lp) | Execute a FlyteTask, or FlyteLaunchplan. |
| [`execute_remote_wf()`](#execute_remote_wf) | Execute a FlyteWorkflow. |
| [`fast_package()`](#fast_package) | Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location. |
| [`fast_register_workflow()`](#fast_register_workflow) | Use this method to register a workflow with zip mode. |
| [`fetch_active_launchplan()`](#fetch_active_launchplan) | Returns the active version of the launch plan if it exists or returns None. |
| [`fetch_execution()`](#fetch_execution) | Fetch a workflow execution entity from flyte admin. |
| [`fetch_launch_plan()`](#fetch_launch_plan) | Fetch a launchplan entity from flyte admin. |
| [`fetch_task()`](#fetch_task) | Fetch a task entity from flyte admin. |
| [`fetch_task_lazy()`](#fetch_task_lazy) | Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily. |
| [`fetch_workflow()`](#fetch_workflow) | Fetch a workflow entity from flyte admin. |
| [`fetch_workflow_lazy()`](#fetch_workflow_lazy) | Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily. |
| [`find_launch_plan()`](#find_launch_plan) |  |
| [`find_launch_plan_for_node()`](#find_launch_plan_for_node) |  |
| [`for_endpoint()`](#for_endpoint) |  |
| [`for_sandbox()`](#for_sandbox) |  |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted. |
| [`generate_console_url()`](#generate_console_url) | Generate a Flyteconsole URL for the given Flyte remote endpoint. |
| [`get()`](#get) | General function that works with flyte tiny urls. |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin. |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution. |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) |  |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan. |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin. |
| [`list_signals()`](#list_signals) | . |
| [`list_tasks_by_version()`](#list_tasks_by_version) |  |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities. |
| [`recent_executions()`](#recent_executions) |  |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options. |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode. |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote. |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow. |
| [`reject()`](#reject) | . |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration. |
| [`set_input()`](#set_input) | . |
| [`set_signal()`](#set_signal) | . |
| [`sync()`](#sync) | This function was previously a singledispatchmethod. |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state. |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution. |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state. |
| [`terminate()`](#terminate) | Terminate a workflow execution. |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service. |
| [`wait()`](#wait) | Wait for an execution to finish. |


#### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
)
```
Given a launchplan, activate it, all previous versions are deactivated.


| Parameter | Type |
|-|-|
| `ident` | `Identifier` |

#### approve()

```python
def approve(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    data: typing.Union[LiteralsResolver, Literal, LiteralMap],
    download_to: str,
    recursive: bool,
)
```
Download the data to the specified location. If the data is a LiteralsResolver, LiteralMap and if recursive is
specified, then all file like objects will be recursively downloaded (e.g. FlyteFile/Dir (blob),
StructuredDataset etc).

Note: That it will use your sessions credentials to access the remote location. For sandbox, this should be
automatically configured, assuming you are running sandbox locally. For other environments, you will need to
configure your credentials appropriately.



| Parameter | Type |
|-|-|
| `data` | `typing.Union[LiteralsResolver, Literal, LiteralMap]` |
| `download_to` | `str` |
| `recursive` | `bool` |

#### execute()

```python
def execute(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity.

This method supports:
- ``Flyte{Task, Workflow, LaunchPlan}`` remote module objects.
- ``@task``-decorated functions and ``TaskTemplate`` tasks.
- ``@workflow``-decorated functions.
- ``LaunchPlan`` objects.

For local entities, this code will attempt to find the entity first, and if missing, will compile and register
the object.

Not all arguments are relevant in all circumstances. For example, there's no reason to use the serialization
settings for entities that have already been registered on Admin.



| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_launch_plan()

```python
def execute_local_launch_plan(
    entity: LaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    name: typing.Optional[str],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a locally defined `LaunchPlan`.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `name` | `typing.Optional[str]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_task()

```python
def execute_local_task(
    entity: PythonTask,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute a @task-decorated function or TaskTemplate task.



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_workflow()

```python
def execute_local_workflow(
    entity: WorkflowBase,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteWorkflowExecution
```
Execute an @workflow decorated function.



| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_reference_launch_plan()

```python
def execute_reference_launch_plan(
    entity: ReferenceLaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceLaunchPlan.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceLaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_task()

```python
def execute_reference_task(
    entity: ReferenceTask,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceTask.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_workflow()

```python
def execute_reference_workflow(
    entity: ReferenceWorkflow,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a ReferenceWorkflow.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_task_lp()

```python
def execute_remote_task_lp(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a FlyteTask, or FlyteLaunchplan.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_wf()

```python
def execute_remote_wf(
    entity: FlyteWorkflow,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
) -> FlyteWorkflowExecution
```
Execute a FlyteWorkflow.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `FlyteWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### fast_package()

```python
def fast_package(
    root: os.PathLike,
    deref_symlinks: bool,
    output: str,
    options: typing.Optional[FastPackageOptions],
) -> typing.Tuple[bytes, str]
```
Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location


| Parameter | Type |
|-|-|
| `root` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `output` | `str` |
| `options` | `typing.Optional[FastPackageOptions]` |

#### fast_register_workflow()

```python
def fast_register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
    fast_package_options: typing.Optional[FastPackageOptions],
) -> FlyteWorkflow
```
Use this method to register a workflow with zip mode.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### fetch_active_launchplan()

```python
def fetch_active_launchplan(
    project: str,
    domain: str,
    name: str,
) -> typing.Optional[FlyteLaunchPlan]
```
Returns the active version of the launch plan if it exists or returns None


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_execution()

```python
def fetch_execution(
    project: str,
    domain: str,
    name: str,
) -> FlyteWorkflowExecution
```
Fetch a workflow execution entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_launch_plan()

```python
def fetch_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteLaunchPlan
```
Fetch a launchplan entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task()

```python
def fetch_task(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteTask
```
Fetch a task entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task_lazy()

```python
def fetch_task_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity
```
Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow()

```python
def fetch_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> FlyteWorkflow
```
Fetch a workflow entity from flyte admin.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow_lazy()

```python
def fetch_workflow_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> LazyEntity[FlyteWorkflow]
```
Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### find_launch_plan()

```python
def find_launch_plan(
    lp_ref: id_models,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type |
|-|-|
| `lp_ref` | `id_models` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### find_launch_plan_for_node()

```python
def find_launch_plan_for_node(
    node: Node,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
)
```
| Parameter | Type |
|-|-|
| `node` | `Node` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### for_sandbox()

```python
def for_sandbox(
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
) -> 'FlyteRemote'
```
| Parameter | Type |
|-|-|
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### generate_console_http_domain()

```python
def generate_console_http_domain()
```
This should generate the domain where console is hosted.

:return:


#### generate_console_url()

```python
def generate_console_url(
    entity: typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan],
)
```
Generate a Flyteconsole URL for the given Flyte remote endpoint.
This will automatically determine if this is an execution or an entity and change the type automatically


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan]` |

#### get()

```python
def get(
    flyte_uri: typing.Optional[str],
) -> typing.Optional[typing.Union[LiteralsResolver, Literal, HTML, bytes]]
```
General function that works with flyte tiny urls. This can return outputs (in the form of LiteralsResolver, or
individual Literals for singular requests), or HTML if passed a deck link, or bytes containing HTML,
if ipython is not available locally.


| Parameter | Type |
|-|-|
| `flyte_uri` | `typing.Optional[str]` |

#### get_domains()

```python
def get_domains()
```
Lists registered domains from flyte admin.

:returns: typing.List[flytekit.models.domain.Domain]


#### get_execution_metrics()

```python
def get_execution_metrics(
    id: WorkflowExecutionIdentifier,
    depth: int,
) -> FlyteExecutionSpan
```
Get the metrics for a given execution.


| Parameter | Type |
|-|-|
| `id` | `WorkflowExecutionIdentifier` |
| `depth` | `int` |

#### get_extra_headers_for_protocol()

```python
def get_extra_headers_for_protocol(
    native_url,
)
```
| Parameter | Type |
|-|-|
| `native_url` |  |

#### launch_backfill()

```python
def launch_backfill(
    project: str,
    domain: str,
    from_date: datetime,
    to_date: datetime,
    launchplan: str,
    launchplan_version: str,
    execution_name: str,
    version: str,
    dry_run: bool,
    execute: bool,
    parallel: bool,
    failure_policy: typing.Optional[WorkflowFailurePolicy],
    overwrite_cache: typing.Optional[bool],
) -> typing.Optional[FlyteWorkflowExecution, FlyteWorkflow, WorkflowBase]
```
Creates and launches a backfill workflow for the given launchplan. If launchplan version is not specified,
then the latest launchplan is retrieved.
The from_date is exclusive and end_date is inclusive and backfill run for all instances in between. ::
-> (start_date - exclusive, end_date inclusive)

If dry_run is specified, the workflow is created and returned.
If execute==False is specified then the workflow is created and registered.
In the last case, the workflow is created, registered and executed.

The `parallel` flag can be used to generate a workflow where all launchplans can be run in parallel. Default
is that execute backfill is run sequentially



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `from_date` | `datetime` |
| `to_date` | `datetime` |
| `launchplan` | `str` |
| `launchplan_version` | `str` |
| `execution_name` | `str` |
| `version` | `str` |
| `dry_run` | `bool` |
| `execute` | `bool` |
| `parallel` | `bool` |
| `failure_policy` | `typing.Optional[WorkflowFailurePolicy]` |
| `overwrite_cache` | `typing.Optional[bool]` |

#### list_projects()

```python
def list_projects(
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
    sort_by: typing.Optional[admin_common_models.Sort],
) -> typing.List[Project]
```
Lists registered projects from flyte admin.



| Parameter | Type |
|-|-|
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |
| `sort_by` | `typing.Optional[admin_common_models.Sort]` |

#### list_signals()

```python
def list_signals(
    execution_name: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: int,
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[Signal]
```
| Parameter | Type |
|-|-|
| `execution_name` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `int` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### list_tasks_by_version()

```python
def list_tasks_by_version(
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
) -> typing.List[FlyteTask]
```
| Parameter | Type |
|-|-|
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |

#### raw_register()

```python
def raw_register(
    cp_entity: FlyteControlPlaneEntity,
    settings: SerializationSettings,
    version: str,
    create_default_launchplan: bool,
    options: Options,
    og_entity: FlyteLocalEntity,
) -> typing.Optional[Identifier]
```
Raw register method, can be used to register control plane entities. Usually if you have a Flyte Entity like a
WorkflowBase, Task, LaunchPlan then use other methods. This should be used only if you have already serialized entities



| Parameter | Type |
|-|-|
| `cp_entity` | `FlyteControlPlaneEntity` |
| `settings` | `SerializationSettings` |
| `version` | `str` |
| `create_default_launchplan` | `bool` |
| `options` | `Options` |
| `og_entity` | `FlyteLocalEntity` |

#### recent_executions()

```python
def recent_executions(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
) -> typing.List[FlyteWorkflowExecution]
```
| Parameter | Type |
|-|-|
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### register_launch_plan()

```python
def register_launch_plan(
    entity: LaunchPlan,
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
) -> FlyteLaunchPlan
```
Register a given launchplan, possibly applying overrides from the provided options. If the underlying workflow
is not already registered, it, along with any underlying entities, will also be registered. If the underlying
workflow does exist (with the given project/domain/version), then only the launchplan will be registered.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### register_script()

```python
def register_script(
    entity: typing.Union[WorkflowBase, PythonTask, LaunchPlan],
    image_config: typing.Optional[ImageConfig],
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    destination_dir: str,
    copy_all: bool,
    default_launch_plan: bool,
    options: typing.Optional[Options],
    source_path: typing.Optional[str],
    module_name: typing.Optional[str],
    envs: typing.Optional[typing.Dict[str, str]],
    fast_package_options: typing.Optional[FastPackageOptions],
) -> typing.Union[FlyteWorkflow, FlyteTask, FlyteLaunchPlan, ReferenceEntity]
```
Use this method to register a workflow via script mode.


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[WorkflowBase, PythonTask, LaunchPlan]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `destination_dir` | `str` |
| `copy_all` | `bool` |
| `default_launch_plan` | `bool` |
| `options` | `typing.Optional[Options]` |
| `source_path` | `typing.Optional[str]` |
| `module_name` | `typing.Optional[str]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### register_task()

```python
def register_task(
    entity: PythonTask,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
) -> FlyteTask
```
Register a qualified task (PythonTask) with Remote
For any conflicting parameters method arguments are regarded as overrides



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |

#### register_workflow()

```python
def register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
) -> FlyteWorkflow
```
Use this method to register a workflow.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |

#### reject()

```python
def reject(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### remote_context()

```python
def remote_context()
```
Context manager with remote-specific configuration.


#### set_input()

```python
def set_input(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project,
    domain,
    python_type,
    literal_type,
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` |  |
| `domain` |  |
| `python_type` |  |
| `literal_type` |  |

#### set_signal()

```python
def set_signal(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    python_type: typing.Optional[typing.Type],
    literal_type: typing.Optional[type_models.LiteralType],
)
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `python_type` | `typing.Optional[typing.Type]` |
| `literal_type` | `typing.Optional[type_models.LiteralType]` |

#### sync()

```python
def sync(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
This function was previously a singledispatchmethod. We've removed that but this function remains
so that we don't break people.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_execution()

```python
def sync_execution(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Sync a FlyteWorkflowExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_node_execution()

```python
def sync_node_execution(
    execution: FlyteNodeExecution,
    node_mapping: typing.Dict[str, FlyteNode],
) -> FlyteNodeExecution
```
Get data backing a node execution. These FlyteNodeExecution objects should've come from Admin with the model
fields already populated correctly. For purposes of the remote experience, we'd like to supplement the object
with some additional fields:
- inputs/outputs
- task/workflow executions, and/or underlying node executions in the case of parent nodes
- TypedInterface (remote wrapper type)

A node can have several different types of executions behind it. That is, the node could've run (perhaps
multiple times because of retries):
- A task
- A static subworkflow
- A dynamic subworkflow (which in turn may have run additional tasks, subwfs, and/or launch plans)
- A launch plan

The data model is complicated, so ascertaining which of these happened is a bit tricky. That logic is
encapsulated in this function.


| Parameter | Type |
|-|-|
| `execution` | `FlyteNodeExecution` |
| `node_mapping` | `typing.Dict[str, FlyteNode]` |

#### sync_task_execution()

```python
def sync_task_execution(
    execution: FlyteTaskExecution,
    entity_interface: typing.Optional[TypedInterface],
) -> FlyteTaskExecution
```
Sync a FlyteTaskExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteTaskExecution` |
| `entity_interface` | `typing.Optional[TypedInterface]` |

#### terminate()

```python
def terminate(
    execution: FlyteWorkflowExecution,
    cause: str,
)
```
Terminate a workflow execution.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `cause` | `str` |

#### upload_file()

```python
def upload_file(
    to_upload: pathlib.Path,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    filename_root: typing.Optional[str],
) -> typing.Tuple[bytes, str]
```
Function will use remote's client to hash and then upload the file using Admin's data proxy service.



| Parameter | Type |
|-|-|
| `to_upload` | `pathlib.Path` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `filename_root` | `typing.Optional[str]` |

#### wait()

```python
def wait(
    execution: FlyteWorkflowExecution,
    timeout: typing.Optional[typing.Union[timedelta, int]],
    poll_interval: typing.Optional[typing.Union[timedelta, int]],
    sync_nodes: bool,
) -> FlyteWorkflowExecution
```
Wait for an execution to finish.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `timeout` | `typing.Optional[typing.Union[timedelta, int]]` |
| `poll_interval` | `typing.Optional[typing.Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `client` |  | {{< multiline >}}Return a SynchronousFlyteClient for additional operations.
{{< /multiline >}} |
| `config` |  | {{< multiline >}}Image config.
{{< /multiline >}} |
| `context` |  |  |
| `default_domain` |  | {{< multiline >}}Default project to use when fetching or executing flyte entities.
{{< /multiline >}} |
| `default_project` |  | {{< multiline >}}Default project to use when fetching or executing flyte entities.
{{< /multiline >}} |
| `file_access` |  | {{< multiline >}}File access provider to use for offloading non-literal inputs/outputs.
{{< /multiline >}} |
| `interactive_mode_enabled` |  | {{< multiline >}}If set to True, the FlyteRemote will pickle the task/workflow.
{{< /multiline >}} |

## flytekit.HashMethod

Flyte-specific object used to wrap the hash function for a specific type


```python
class HashMethod(
    function: typing.Callable[[~T], str],
)
```
| Parameter | Type |
|-|-|
| `function` | `typing.Callable[[~T], str]` |

### Methods

| Method | Description |
|-|-|
| [`calculate()`](#calculate) | Calculate hash for `obj`. |


#### calculate()

```python
def calculate(
    obj: ~T,
) -> str
```
Calculate hash for `obj`.


| Parameter | Type |
|-|-|
| `obj` | `~T` |

## flytekit.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
class ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry. |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled. |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment. |
| [`image_name()`](#image_name) | Full image name with tag. |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec. |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process. |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process. |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory. |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process. |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
) -> ImageSpec
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
) -> ImageSpec
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `tag` |  | {{< multiline >}}Calculate a hash from the image spec. The hash will be the tag of the image.
We will also read the content of the requirement file and the source root to calculate the hash.
Therefore, it will generate different hash if new dependencies are added or the source code is changed.

Keep in mind the fields source_root and copy may be changed by update_image_spec_copy_handling, so when
you call this property in relation to that function matter will change the output.
{{< /multiline >}} |

## flytekit.Labels

```python
class Labels(
    values,
)
```
Label values to be applied to a workflow execution resource.



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Labels
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

## flytekit.LaunchPlan

Launch Plans are one of the core constructs of Flyte. Please take a look at the discussion in the
:std:ref:`core concepts <flyte:divedeep-launchplans>` if you are unfamiliar with them.

Every workflow is registered with a default launch plan, which is just a launch plan with none of the additional
attributes set - no default values, fixed values, schedules, etc. Assuming you have the following workflow

.. code-block:: python

@workflow
def wf(a: int, c: str) -> str:
...

Create the default launch plan with

.. code-block:: python

LaunchPlan.get_or_create(workflow=my_wf)

If you specify additional parameters, you'll also have to give the launch plan a unique name. Default and
fixed inputs can be expressed as Python native values like so:

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # fixed_and_default_start
:end-before: # fixed_and_default_end
:language: python
:dedent: 4

Additionally, a launch plan can be configured to run on a schedule and emit notifications.


Please see the relevant Schedule and Notification objects as well.

To configure the remaining parameters, you'll need to import the relevant model objects as well.

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # schedule_start
:end-before: # schedule_end
:language: python
:dedent: 4

.. code-block:: python

from flytekit.models.common import Annotations, AuthRole, Labels, RawOutputDataConfig

Then use as follows

.. literalinclude:: ../../../tests/flytekit/unit/core/test_launch_plan.py
:start-after: # auth_role_start
:end-before: # auth_role_end
:language: python
:dedent: 4


```python
class LaunchPlan(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    parameters: _interface_models.ParameterMap,
    fixed_inputs: _literal_models.LiteralMap,
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `parameters` | `_interface_models.ParameterMap` |
| `fixed_inputs` | `_literal_models.LiteralMap` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`clone_with()`](#clone_with) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create()`](#create) |  |
| [`get_default_launch_plan()`](#get_default_launch_plan) | Users should probably call the get_or_create function defined below instead. |
| [`get_or_create()`](#get_or_create) | This function offers a friendlier interface for creating launch plans. |


#### clone_with()

```python
def clone_with(
    name: str,
    parameters: Optional[_interface_models.ParameterMap],
    fixed_inputs: Optional[_literal_models.LiteralMap],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `parameters` | `Optional[_interface_models.ParameterMap]` |
| `fixed_inputs` | `Optional[_literal_models.LiteralMap]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create()

```python
def create(
    name: str,
    workflow: _annotated_workflow.WorkflowBase,
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

#### get_default_launch_plan()

```python
def get_default_launch_plan(
    ctx: FlyteContext,
    workflow: _annotated_workflow.WorkflowBase,
) -> LaunchPlan
```
Users should probably call the get_or_create function defined below instead. A default launch plan is the one
that will just pick up whatever default values are defined in the workflow function signature (if any) and
use the default auth information supplied during serialization, with no notifications or schedules.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `workflow` | `_annotated_workflow.WorkflowBase` |

#### get_or_create()

```python
def get_or_create(
    workflow: _annotated_workflow.WorkflowBase,
    name: Optional[str],
    default_inputs: Optional[Dict[str, Any]],
    fixed_inputs: Optional[Dict[str, Any]],
    schedule: Optional[_schedule_model.Schedule],
    notifications: Optional[List[_common_models.Notification]],
    labels: Optional[_common_models.Labels],
    annotations: Optional[_common_models.Annotations],
    raw_output_data_config: Optional[_common_models.RawOutputDataConfig],
    max_parallelism: Optional[int],
    security_context: Optional[security.SecurityContext],
    auth_role: Optional[_common_models.AuthRole],
    trigger: Optional[LaunchPlanTriggerBase],
    overwrite_cache: Optional[bool],
    auto_activate: bool,
) -> LaunchPlan
```
This function offers a friendlier interface for creating launch plans. If the name for the launch plan is not
supplied, this assumes you are looking for the default launch plan for the workflow. If it is specified, it
will be used. If creating the default launch plan, none of the other arguments may be specified.

The resulting launch plan is also cached and if called again with the same name, the
cached version is returned



| Parameter | Type |
|-|-|
| `workflow` | `_annotated_workflow.WorkflowBase` |
| `name` | `Optional[str]` |
| `default_inputs` | `Optional[Dict[str, Any]]` |
| `fixed_inputs` | `Optional[Dict[str, Any]]` |
| `schedule` | `Optional[_schedule_model.Schedule]` |
| `notifications` | `Optional[List[_common_models.Notification]]` |
| `labels` | `Optional[_common_models.Labels]` |
| `annotations` | `Optional[_common_models.Annotations]` |
| `raw_output_data_config` | `Optional[_common_models.RawOutputDataConfig]` |
| `max_parallelism` | `Optional[int]` |
| `security_context` | `Optional[security.SecurityContext]` |
| `auth_role` | `Optional[_common_models.AuthRole]` |
| `trigger` | `Optional[LaunchPlanTriggerBase]` |
| `overwrite_cache` | `Optional[bool]` |
| `auto_activate` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `annotations` |  |  |
| `fixed_inputs` |  |  |
| `interface` |  |  |
| `labels` |  |  |
| `max_parallelism` |  |  |
| `name` |  |  |
| `notifications` |  |  |
| `overwrite_cache` |  |  |
| `parameters` |  |  |
| `python_interface` |  |  |
| `raw_output_data_config` |  |  |
| `saved_inputs` |  |  |
| `schedule` |  |  |
| `security_context` |  |  |
| `should_auto_activate` |  |  |
| `trigger` |  |  |
| `workflow` |  |  |

## flytekit.LaunchPlanReference

A reference object containing metadata that points to a remote launch plan.


```python
class LaunchPlanReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.Literal

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type |
|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `hash` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
) -> Literal
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type |
|-|-|
| `metadata` | `typing.Dict[str, str]` |

#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `collection` |  | {{< multiline >}}If not None, this value holds a collection of Literal values which can be further unpacked.
{{< /multiline >}} |
| `hash` |  | {{< multiline >}}If not None, this value holds a hash that represents the literal for caching purposes.
{{< /multiline >}} |
| `is_empty` |  |  |
| `map` |  | {{< multiline >}}If not None, this value holds a map of Literal values which can be further unpacked.
{{< /multiline >}} |
| `metadata` |  | {{< multiline >}}This value holds metadata about the literal.
{{< /multiline >}} |
| `offloaded_metadata` |  | {{< multiline >}}This value holds metadata about the offloaded literal.
{{< /multiline >}} |
| `scalar` |  | {{< multiline >}}If not None, this value holds a scalar value which can be further unpacked.
{{< /multiline >}} |
| `value` |  | {{< multiline >}}Returns one of the scalar, collection, or map properties based on which one is set.
{{< /multiline >}} |

## flytekit.LiteralType

```python
class LiteralType(
    simple,
    schema,
    collection_type,
    map_value_type,
    blob,
    enum_type,
    union_type,
    structured_dataset_type,
    metadata,
    structure,
    annotation,
)
```
This is a oneof message, only one of the kwargs may be set, representing one of the Flyte types.



| Parameter | Type |
|-|-|
| `simple` |  |
| `schema` |  |
| `collection_type` |  |
| `map_value_type` |  |
| `blob` |  |
| `enum_type` |  |
| `union_type` |  |
| `structured_dataset_type` |  |
| `metadata` |  |
| `structure` |  |
| `annotation` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> LiteralType
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `annotation` |  |  |
| `blob` |  |  |
| `collection_type` |  | {{< multiline >}}The collection value type
{{< /multiline >}} |
| `enum_type` |  |  |
| `is_empty` |  |  |
| `map_value_type` |  | {{< multiline >}}The Value for a dictionary. Key is always string
{{< /multiline >}} |
| `metadata` |  |  |
| `schema` |  |  |
| `simple` |  |  |
| `structure` |  |  |
| `structured_dataset_type` |  |  |
| `union_type` |  |  |

## flytekit.Options

These are options that can be configured for a launchplan during registration or overridden during an execution.
For instance two people may want to run the same workflow but have the offloaded data stored in two different
buckets. Or you may want labels or annotations to be different. This object is used when launching an execution
in a Flyte backend, and also when registering launch plans.



```python
class Options(
    labels: typing.Optional[flytekit.models.common.Labels],
    annotations: typing.Optional[flytekit.models.common.Annotations],
    raw_output_data_config: typing.Optional[flytekit.models.common.RawOutputDataConfig],
    security_context: typing.Optional[flytekit.models.security.SecurityContext],
    max_parallelism: typing.Optional[int],
    notifications: typing.Optional[typing.List[flytekit.models.common.Notification]],
    disable_notifications: typing.Optional[bool],
    overwrite_cache: typing.Optional[bool],
)
```
| Parameter | Type |
|-|-|
| `labels` | `typing.Optional[flytekit.models.common.Labels]` |
| `annotations` | `typing.Optional[flytekit.models.common.Annotations]` |
| `raw_output_data_config` | `typing.Optional[flytekit.models.common.RawOutputDataConfig]` |
| `security_context` | `typing.Optional[flytekit.models.security.SecurityContext]` |
| `max_parallelism` | `typing.Optional[int]` |
| `notifications` | `typing.Optional[typing.List[flytekit.models.common.Notification]]` |
| `disable_notifications` | `typing.Optional[bool]` |
| `overwrite_cache` | `typing.Optional[bool]` |

### Methods

| Method | Description |
|-|-|
| [`default_from()`](#default_from) |  |


#### default_from()

```python
def default_from(
    k8s_service_account: typing.Optional[str],
    raw_data_prefix: typing.Optional[str],
) -> Options
```
| Parameter | Type |
|-|-|
| `k8s_service_account` | `typing.Optional[str]` |
| `raw_data_prefix` | `typing.Optional[str]` |

## flytekit.PagerDuty

This notification should be used when sending emails to the PagerDuty service.

.. code-block:: python

from flytekit.models.core.execution import WorkflowExecutionPhase

PagerDuty(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])


```python
class PagerDuty(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> Notification
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `email` |  |  |
| `is_empty` |  |  |
| `pager_duty` |  |  |
| `phases` |  | {{< multiline >}}A list of phases to which users can associate the notifications.
{{< /multiline >}} |
| `slack` |  |  |

## flytekit.PodTemplate

Custom PodTemplate specification for a Task.


```python
class PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
)
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.PythonFunctionTask

A Python Function task should be used as the base for all extensions that have a python function. It will
automatically detect interface of the python function and when serialized on the hosted Flyte platform handles the
writing execution command to execute the function

It is advised this task is used using the @task decorator as follows

.. code-block: python

@task
def my_func(a: int) -> str:
...

In the above code, the name of the function, the module, and the interface (inputs = int and outputs = str) will be
auto detected.


```python
class PythonFunctionTask(
    task_config: T,
    task_function: Callable,
    task_type,
    ignore_input_vars: Optional[List[str]],
    execution_mode: ExecutionBehavior,
    task_resolver: Optional[TaskResolverMixin],
    node_dependency_hints: Optional[Iterable[Union['PythonFunctionTask', '_annotated_launch_plan.LaunchPlan', WorkflowBase]]],
    pickle_untyped: bool,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `task_config` | `T` |
| `task_function` | `Callable` |
| `task_type` |  |
| `ignore_input_vars` | `Optional[List[str]]` |
| `execution_mode` | `ExecutionBehavior` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `node_dependency_hints` | `Optional[Iterable[Union['PythonFunctionTask', '_annotated_launch_plan.LaunchPlan', WorkflowBase]]]` |
| `pickle_untyped` | `bool` |
| `kwargs` | ``**kwargs`` |

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
) -> Any
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
) -> typing.Optional[typing.Dict[str, typing.Any]]
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

## flytekit.PythonInstanceTask

This class should be used as the base class for all Tasks that do not have a user defined function body, but have
a platform defined execute method. (Execute needs to be overridden). This base class ensures that the module loader
will invoke the right class automatically, by capturing the module name and variable in the module name.

.. code-block: python

x = MyInstanceTask(name="x", .....)

# this can be invoked as
x(a=5) # depending on the interface of the defined task


```python
class PythonInstanceTask(
    name: str,
    task_config: T,
    task_type: str,
    task_resolver: Optional[TaskResolverMixin],
    kwargs,
)
```
Please see class level documentation.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `task_config` | `T` |
| `task_type` | `str` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition. |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor. |
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
) -> typing.Optional[typing.Dict[str, typing.Any]]
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
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `metadata` |  |  |
| `name` |  |  |
| `python_interface` |  | {{< multiline >}}Returns this task's python interface.
{{< /multiline >}} |
| `resources` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_resolver` |  |  |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.Resources

This class is used to specify both resource requests and resource limits.

.. code-block:: python

Resources(cpu="1", mem="2048")  # This is 1 CPU and 2 KB of memory
Resources(cpu="100m", mem="2Gi")  # This is 1/10th of a CPU and 2 gigabytes of memory
Resources(cpu=0.5, mem=1024) # This is 500m CPU and 1 KB of memory

# For Kubernetes-based tasks, pods use ephemeral local storage for scratch space, caching, and for logs.
# This allocates 1Gi of such local storage.
Resources(ephemeral_storage="1Gi")

When used together with `@task(resources=)`, you a specific the request and limits with one object.
When the value is set to a tuple or list, the first value is the request and the
second value is the limit. If the value is a single value, then both the requests and limit is
set to that value. For example, the `Resource(cpu=("1", "2"), mem=1024)` will set the cpu request to 1, cpu limit to 2,
mem limit and request to 1024.

.. note::

Persistent storage is not currently supported on the Flyte backend.

Please see the :std:ref:`User Guide <cookbook:customizing task resources>` for detailed examples.
Also refer to the `K8s conventions. <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>`__


```python
class Resources(
    cpu: typing.Union[str, int, float, list, tuple, NoneType],
    mem: typing.Union[str, int, list, tuple, NoneType],
    gpu: typing.Union[str, int, list, tuple, NoneType],
    ephemeral_storage: typing.Union[str, int, NoneType],
)
```
| Parameter | Type |
|-|-|
| `cpu` | `typing.Union[str, int, float, list, tuple, NoneType]` |
| `mem` | `typing.Union[str, int, list, tuple, NoneType]` |
| `gpu` | `typing.Union[str, int, list, tuple, NoneType]` |
| `ephemeral_storage` | `typing.Union[str, int, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

## flytekit.SQLTask

Base task types for all SQL tasks. See :py:class:`flytekit.extras.sqlite3.task.SQLite3Task`
and :py:class:`flytekitplugins.athena.task.AthenaTask` for examples of how to use it as a base class.

.. autoclass:: flytekit.extras.sqlite3.task.SQLite3Task
:noindex:


```python
class SQLTask(
    name: str,
    query_template: str,
    task_config: typing.Optional[~T],
    task_type,
    inputs: typing.Optional[typing.Dict[str, typing.Tuple[typing.Type, typing.Any]]],
    metadata: typing.Optional[flytekit.core.base_task.TaskMetadata],
    outputs: typing.Optional[typing.Dict[str, typing.Type]],
    kwargs,
)
```
This SQLTask should mostly just be used as a base class for other SQL task types and should not be used
directly. See :py:class:`flytekit.extras.sqlite3.task.SQLite3Task`


| Parameter | Type |
|-|-|
| `name` | `str` |
| `query_template` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `task_type` |  |
| `inputs` | `typing.Optional[typing.Dict[str, typing.Tuple[typing.Type, typing.Any]]]` |
| `metadata` | `typing.Optional[flytekit.core.base_task.TaskMetadata]` |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `kwargs` | ``**kwargs`` |

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
| [`get_query()`](#get_query) |  |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte. |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name. |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name. |
| [`interpolate_query()`](#interpolate_query) | This function will fill in the query template with the provided kwargs and return the interpolated query. |
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
) -> typing.Optional[flytekit.models.task.Container]
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
) -> typing.Optional[typing.Dict[str, typing.Any]]
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
) -> typing.Optional[flytekit.models.task.K8sPod]
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_query()

```python
def get_query(
    kwargs,
) -> str
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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

#### interpolate_query()

```python
def interpolate_query(
    query_template,
    kwargs,
) -> typing.Any
```
This function will fill in the query template with the provided kwargs and return the interpolated query.
Please note that when SQL tasks run in Flyte, this step is done by the task executor.


| Parameter | Type |
|-|-|
| `query_template` |  |
| `kwargs` | ``**kwargs`` |

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
| `query_template` |  |  |
| `security_context` |  |  |
| `task_config` |  | {{< multiline >}}Returns the user-specified task config which is used for plugin-specific handling of the task.
{{< /multiline >}} |
| `task_type` |  |  |
| `task_type_version` |  |  |

## flytekit.Scalar

```python
class Scalar(
    primitive: typing.Optional[flytekit.models.literals.Primitive],
    blob: typing.Optional[flytekit.models.literals.Blob],
    binary: typing.Optional[flytekit.models.literals.Binary],
    schema: typing.Optional[flytekit.models.literals.Schema],
    union: typing.Optional[flytekit.models.literals.Union],
    none_type: typing.Optional[flytekit.models.literals.Void],
    error: typing.Optional[flytekit.models.types.Error],
    generic: typing.Optional[google.protobuf.struct_pb2.Struct],
    structured_dataset: typing.Optional[flytekit.models.literals.StructuredDataset],
)
```
Scalar wrapper around Flyte types.  Only one can be specified.



| Parameter | Type |
|-|-|
| `primitive` | `typing.Optional[flytekit.models.literals.Primitive]` |
| `blob` | `typing.Optional[flytekit.models.literals.Blob]` |
| `binary` | `typing.Optional[flytekit.models.literals.Binary]` |
| `schema` | `typing.Optional[flytekit.models.literals.Schema]` |
| `union` | `typing.Optional[flytekit.models.literals.Union]` |
| `none_type` | `typing.Optional[flytekit.models.literals.Void]` |
| `error` | `typing.Optional[flytekit.models.types.Error]` |
| `generic` | `typing.Optional[google.protobuf.struct_pb2.Struct]` |
| `structured_dataset` | `typing.Optional[flytekit.models.literals.StructuredDataset]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> flytekit.models.literals.Scalar
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `binary` |  |  |
| `blob` |  |  |
| `error` |  |  |
| `generic` |  |  |
| `is_empty` |  |  |
| `none_type` |  |  |
| `primitive` |  |  |
| `schema` |  |  |
| `structured_dataset` |  |  |
| `union` |  |  |
| `value` |  | {{< multiline >}}Returns whichever value is set
{{< /multiline >}} |

## flytekit.Secret

See :std:ref:`cookbook:secrets` for usage examples.



```python
class Secret(
    group: typing.Optional[str],
    key: typing.Optional[str],
    group_version: typing.Optional[str],
    mount_requirement: <enum 'MountType'>,
    env_var: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `group` | `typing.Optional[str]` |
| `key` | `typing.Optional[str]` |
| `group_version` | `typing.Optional[str]` |
| `mount_requirement` | `<enum 'MountType'>` |
| `env_var` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Secret,
) -> Secret
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Secret` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.SecurityContext

This is a higher level wrapper object that for the most part users shouldn't have to worry about. You should
be able to just use :py:class:`flytekit.Secret` instead.


```python
class SecurityContext(
    run_as: typing.Optional[flytekit.models.security.Identity],
    secrets: typing.Optional[typing.List[flytekit.models.security.Secret]],
    tokens: typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]],
)
```
| Parameter | Type |
|-|-|
| `run_as` | `typing.Optional[flytekit.models.security.Identity]` |
| `secrets` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` |
| `tokens` | `typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.SecurityContext,
) -> SecurityContext
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.SecurityContext` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.SensorEngine

This is the base class for all async connectors.
It defines the interface that all connectors must implement.
The connector service is responsible for invoking connectors. The propeller will communicate with the connector service
to create tasks, get the status of tasks, and delete tasks.

All the connectors should be registered in the ConnectorRegistry.
Connector Service
will look up the connector based on the task type. Every task type can only have one connector.


```python
def SensorEngine()
```
### Methods

| Method | Description |
|-|-|
| [`create()`](#create) | Return a resource meta that can be used to get the status of the task. |
| [`delete()`](#delete) | Delete the task. |
| [`get()`](#get) | Return the status of the task, and return the outputs in some cases. |
| [`get_logs()`](#get_logs) | Return the metrics for the task. |
| [`get_metrics()`](#get_metrics) | Return the metrics for the task. |


#### create()

```python
def create(
    task_template: flytekit.models.task.TaskTemplate,
    inputs: typing.Optional[flytekit.models.literals.LiteralMap],
    kwarg,
) -> flytekit.sensor.base_sensor.SensorMetadata
```
Return a resource meta that can be used to get the status of the task.


| Parameter | Type |
|-|-|
| `task_template` | `flytekit.models.task.TaskTemplate` |
| `inputs` | `typing.Optional[flytekit.models.literals.LiteralMap]` |
| `kwarg` |  |

#### delete()

```python
def delete(
    resource_meta: flytekit.sensor.base_sensor.SensorMetadata,
    kwargs,
)
```
Delete the task. This call should be idempotent. It should raise an error if fails to delete the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.sensor.base_sensor.SensorMetadata` |
| `kwargs` | ``**kwargs`` |

#### get()

```python
def get(
    resource_meta: flytekit.sensor.base_sensor.SensorMetadata,
    kwargs,
) -> flytekit.extend.backend.base_connector.Resource
```
Return the status of the task, and return the outputs in some cases. For example, bigquery job
can't write the structured dataset to the output location, so it returns the output literals to the propeller,
and the propeller will write the structured dataset to the blob store.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.sensor.base_sensor.SensorMetadata` |
| `kwargs` | ``**kwargs`` |

#### get_logs()

```python
def get_logs(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskLogsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

#### get_metrics()

```python
def get_metrics(
    resource_meta: flytekit.extend.backend.base_connector.ResourceMeta,
    kwargs,
) -> flyteidl.admin.agent_pb2.GetTaskMetricsResponse
```
Return the metrics for the task.


| Parameter | Type |
|-|-|
| `resource_meta` | `flytekit.extend.backend.base_connector.ResourceMeta` |
| `kwargs` | ``**kwargs`` |

### Properties

| Property | Type | Description |
|-|-|-|
| `metadata_type` |  |  |
| `task_category` |  | {{< multiline >}}task category that the connector supports
{{< /multiline >}} |

## flytekit.Slack

This notification should be used when sending emails to the Slack.

.. code-block:: python

from flytekit.models.core.execution import WorkflowExecutionPhase

Slack(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])


```python
class Slack(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> Notification
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `email` |  |  |
| `is_empty` |  |  |
| `pager_duty` |  |  |
| `phases` |  | {{< multiline >}}A list of phases to which users can associate the notifications.
{{< /multiline >}} |
| `slack` |  |  |

## flytekit.SourceCode

Link to source code used to define this task or workflow.


```python
class SourceCode(
    link: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `link` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.description_entity_pb2.SourceCode,
) -> SourceCode
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.admin.description_entity_pb2.SourceCode` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `dataframe` | `typing.Optional[typing.Any]` |
| `uri` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`iter()`](#iter) |  |
| [`open()`](#open) |  |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### all()

```python
def all()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    info,
) -> StructuredDataset
```
| Parameter | Type |
|-|-|
| `info` |  |

#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### iter()

```python
def iter()
```
#### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
| Parameter | Type |
|-|-|
| `dataframe_type` | `Type[DF]` |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
#### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `expected` | `LiteralType` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `dataframe` |  |  |
| `literal` |  |  |
| `metadata` |  |  |

## flytekit.StructuredDatasetFormat

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.


## flytekit.StructuredDatasetTransformerEngine

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.


```python
def StructuredDatasetTransformerEngine()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at. |
| [`dict_to_structured_dataset()`](#dict_to_structured_dataset) |  |
| [`encode()`](#encode) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
| [`get_decoder()`](#get_decoder) |  |
| [`get_encoder()`](#get_encoder) |  |
| [`get_literal_type()`](#get_literal_type) | Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`iter_as()`](#iter_as) |  |
| [`open_as()`](#open_as) | . |
| [`register()`](#register) | Call this with any Encoder or Decoder to register it with the flytekit type system. |
| [`register_for_protocol()`](#register_for_protocol) | See the main register function instead. |
| [`register_renderer()`](#register_renderer) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[StructuredDataset],
    v: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[StructuredDataset]` |
| `v` | `typing.Any` |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: Union[StructuredDataset, typing.Any],
    python_type: Union[Type[StructuredDataset], Type],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `Union[StructuredDataset, typing.Any]` |
| `python_type` | `Union[Type[StructuredDataset], Type]` |
| `expected` | `LiteralType` |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at
the start of a task execution, is the column subsetting behavior. For example, if you have,

def t1() -> Annotated[StructuredDataset, kwtypes(col_a=int, col_b=float)]: ...
def t2(in_a: Annotated[StructuredDataset, kwtypes(col_b=float)]): ...

where t2(in_a=t1()), when t2 does in_a.open(pd.DataFrame).all(), it should get a DataFrame
with only one column.

+-----------------------------+-----------------------------------------+--------------------------------------+
|                             |          StructuredDatasetType of the incoming Literal                         |
+-----------------------------+-----------------------------------------+--------------------------------------+
| StructuredDatasetType       | Has columns defined                     |  [] columns or None                  |
| of currently running task   |                                         |                                      |
+=============================+=========================================+======================================+
|    Has columns              | The StructuredDatasetType passed to the decoder will have the columns          |
|    defined                  | as defined by the type annotation of the currently running task.               |
|                             |                                                                                |
|                             | Decoders **should** then subset the incoming data to the columns requested.    |
|                             |                                                                                |
+-----------------------------+-----------------------------------------+--------------------------------------+
|   [] columns or None        | StructuredDatasetType passed to decoder | StructuredDatasetType passed to the  |
|                             | will have the columns from the incoming | decoder will have an empty list of   |
|                             | Literal. This is the scenario where     | columns.                             |
|                             | the Literal returned by the running     |                                      |
|                             | task will have more information than    |                                      |
|                             | the running task's signature.           |                                      |
+-----------------------------+-----------------------------------------+--------------------------------------+


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### dict_to_structured_dataset()

```python
def dict_to_structured_dataset(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### encode()

```python
def encode(
    ctx: FlyteContext,
    sd: StructuredDataset,
    df_type: Type,
    protocol: str,
    format: str,
    structured_literal_type: StructuredDatasetType,
) -> Literal
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `StructuredDataset` |
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |
| `structured_literal_type` | `StructuredDatasetType` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
sd: StructuredDataset

@workflow
def wf(dc: DC):
t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `Binary` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -> protobuf struct         -> resolved protobuf struct   -> expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
sd: StructuredDataset

@workflow
def wf(dc: DC):
t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `generic` | `Struct` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### get_decoder()

```python
def get_decoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_encoder()

```python
def get_encoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[Type[StructuredDataset], typing.Any],
) -> LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type |
|-|-|
| `t` | `typing.Union[Type[StructuredDataset], typing.Any]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[StructuredDataset]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### iter_as()

```python
def iter_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> typing.Iterator[DF]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `literals.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `StructuredDatasetMetadata` |

#### open_as()

```python
def open_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> DF
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `sd` | `literals.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `StructuredDatasetMetadata` |

#### register()

```python
def register(
    h: Handlers,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
Call this with any Encoder or Decoder to register it with the flytekit type system. If your handler does not
specify a protocol (e.g. s3, gs, etc.) field, then



| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

#### register_for_protocol()

```python
def register_for_protocol(
    h: Handlers,
    protocol: str,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
See the main register function instead.


| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `protocol` | `str` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

#### register_renderer()

```python
def register_renderer(
    python_type: Type,
    renderer: Renderable,
)
```
| Parameter | Type |
|-|-|
| `python_type` | `Type` |
| `renderer` | `Renderable` |

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `python_val` | `typing.Any` |
| `python_type` | `Type[T]` |
| `expected` | `LiteralType` |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `lv` | `Literal` |
| `expected_python_type` | `Type[T]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` |  |  |
| `name` |  |  |
| `python_type` |  | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` |  | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

## flytekit.StructuredDatasetType

```python
class StructuredDatasetType(
    columns: typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn],
    format: str,
    external_schema_type: str,
    external_schema_bytes: bytes,
)
```
| Parameter | Type |
|-|-|
| `columns` | `typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn]` |
| `format` | `str` |
| `external_schema_type` | `str` |
| `external_schema_bytes` | `bytes` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.types_pb2.StructuredDatasetType
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.StructuredDatasetType` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `columns` |  |  |
| `external_schema_bytes` |  |  |
| `external_schema_type` |  |  |
| `format` |  |  |
| `is_empty` |  |  |

## flytekit.TaskMetadata

Metadata for a Task. Things like retries and whether or not caching is turned on, and cache version are specified
here.

See the :std:ref:`IDL <idl:protos/docs/core/core:taskmetadata>` for the protobuf definition.

Attributes:
cache (bool): Indicates if caching should be enabled. See :std:ref:`Caching <cookbook:caching>`.
cache_serialize (bool): Indicates if identical (i.e. same inputs) instances of this task should be executed in serial when caching is enabled. See :std:ref:`Caching <cookbook:caching>`.
cache_version (str): Version to be used for the cached value.
cache_ignore_input_vars (Tuple[str, ...]): Input variables that should not be included when calculating hash for cache.
interruptible (Optional[bool]): Indicates that this task can be interrupted and/or scheduled on nodes with lower QoS guarantees that can include pre-emption.
deprecated (str): Can be used to provide a warning message for a deprecated task. An absence or empty string indicates that the task is active and not deprecated.
retries (int): for retries=n; n > 0, on failures of this task, the task will be retried at-least n number of times.
timeout (Optional[Union[datetime.timedelta, int]]): The maximum duration for which one execution of this task should run. The execution will be terminated if the runtime exceeds this timeout.
pod_template_name (Optional[str]): The name of an existing PodTemplate resource in the cluster which will be used for this task.
generates_deck (bool): Indicates whether the task will generate a Deck URI.
is_eager (bool): Indicates whether the task should be treated as eager.


```python
class TaskMetadata(
    cache: bool,
    cache_serialize: bool,
    cache_version: str,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    interruptible: typing.Optional[bool],
    deprecated: str,
    retries: int,
    timeout: typing.Union[datetime.timedelta, int, NoneType],
    pod_template_name: typing.Optional[str],
    generates_deck: bool,
    is_eager: bool,
)
```
| Parameter | Type |
|-|-|
| `cache` | `bool` |
| `cache_serialize` | `bool` |
| `cache_version` | `str` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |
| `interruptible` | `typing.Optional[bool]` |
| `deprecated` | `str` |
| `retries` | `int` |
| `timeout` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `pod_template_name` | `typing.Optional[str]` |
| `generates_deck` | `bool` |
| `is_eager` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`to_taskmetadata_model()`](#to_taskmetadata_model) | Converts to _task_model. |


#### to_taskmetadata_model()

```python
def to_taskmetadata_model()
```
Converts to _task_model.TaskMetadata


### Properties

| Property | Type | Description |
|-|-|-|
| `retry_strategy` |  |  |

## flytekit.TaskReference

A reference object containing metadata that points to a remote task.


```python
class TaskReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

## flytekit.VersionParameters

Parameters used for version hash generation.

param func: The function to generate a version for. This is an optional parameter and can be any callable
that matches the specified parameter and return types.
:type func: Optional[Callable[P, FuncOut]]


```python
class VersionParameters(
    func: typing.Callable[~P, ~FuncOut],
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType],
    pod_template: typing.Optional[flytekit.core.pod_template.PodTemplate],
    pod_template_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `func` | `typing.Callable[~P, ~FuncOut]` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, NoneType]` |
| `pod_template` | `typing.Optional[flytekit.core.pod_template.PodTemplate]` |
| `pod_template_name` | `typing.Optional[str]` |

## flytekit.Workflow

An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is
better suited to programmatic applications.

Assuming you have some tasks like so

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_tasks_start
:end-before: # docs_tasks_end
:language: python
:dedent: 4

You could create a workflow imperatively like so

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_start
:end-before: # docs_end
:language: python
:dedent: 4

This workflow would be identical on the back-end to

.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
:start-after: # docs_equivalent_start
:end-before: # docs_equivalent_end
:language: python
:dedent: 4

Note that the only reason we need the ``NamedTuple`` is so we can name the output the same thing as in the
imperative example. The imperative paradigm makes the naming of workflow outputs easier, but this isn't a big
deal in function-workflows because names tend to not be necessary.


```python
class Workflow(
    name: str,
    failure_policy: Optional[WorkflowFailurePolicy],
    interruptible: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` |
| `interruptible` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_entity()`](#add_entity) | Anytime you add an entity, all the inputs to the entity must be bound. |
| [`add_launch_plan()`](#add_launch_plan) |  |
| [`add_on_failure_handler()`](#add_on_failure_handler) | This is a special function that mimics the add_entity function, but this is only used. |
| [`add_subwf()`](#add_subwf) |  |
| [`add_task()`](#add_task) |  |
| [`add_workflow_input()`](#add_workflow_input) | Adds an input to the workflow. |
| [`add_workflow_output()`](#add_workflow_output) | Add an output with the given name from the given node output. |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`create_conditional()`](#create_conditional) |  |
| [`execute()`](#execute) | Called by local_execute. |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`ready()`](#ready) | This function returns whether or not the workflow is in a ready state, which means. |


#### add_entity()

```python
def add_entity(
    entity: Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase],
    kwargs,
) -> Node
```
Anytime you add an entity, all the inputs to the entity must be bound.


| Parameter | Type |
|-|-|
| `entity` | `Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase]` |
| `kwargs` | ``**kwargs`` |

#### add_launch_plan()

```python
def add_launch_plan(
    launch_plan: _annotated_launch_plan.LaunchPlan,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `launch_plan` | `_annotated_launch_plan.LaunchPlan` |
| `kwargs` | ``**kwargs`` |

#### add_on_failure_handler()

```python
def add_on_failure_handler(
    entity,
)
```
This is a special function that mimics the add_entity function, but this is only used
to add the failure node. Failure nodes are special because we don't want
them to be part of the main workflow.


| Parameter | Type |
|-|-|
| `entity` |  |

#### add_subwf()

```python
def add_subwf(
    sub_wf: WorkflowBase,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `sub_wf` | `WorkflowBase` |
| `kwargs` | ``**kwargs`` |

#### add_task()

```python
def add_task(
    task: PythonTask,
    kwargs,
) -> Node
```
| Parameter | Type |
|-|-|
| `task` | `PythonTask` |
| `kwargs` | ``**kwargs`` |

#### add_workflow_input()

```python
def add_workflow_input(
    input_name: str,
    python_type: Type,
) -> Promise
```
Adds an input to the workflow.


| Parameter | Type |
|-|-|
| `input_name` | `str` |
| `python_type` | `Type` |

#### add_workflow_output()

```python
def add_workflow_output(
    output_name: str,
    p: Union[Promise, List[Promise], Dict[str, Promise]],
    python_type: Optional[Type],
)
```
Add an output with the given name from the given node output.


| Parameter | Type |
|-|-|
| `output_name` | `str` |
| `p` | `Union[Promise, List[Promise], Dict[str, Promise]]` |
| `python_type` | `Optional[Type]` |

#### compile()

```python
def compile(
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### create_conditional()

```python
def create_conditional(
    name: str,
) -> ConditionalSection
```
| Parameter | Type |
|-|-|
| `name` | `str` |

#### execute()

```python
def execute(
    kwargs,
)
```
Called by local_execute. This function is how local execution for imperative workflows runs. Because when an
entity is added using the add_entity function, all inputs to that entity should've been already declared, we
can just iterate through the nodes in order and we shouldn't run into any dependency issues. That is, we force
the user to declare entities already in a topological sort. To keep track of outputs, we create a map to
start things off, filled in only with the workflow inputs (if any). As things are run, their outputs are stored
in this map.
After all nodes are run, we fill in workflow level outputs the same way as any other previous node.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### ready()

```python
def ready()
```
This function returns whether or not the workflow is in a ready state, which means
* Has at least one node
* All workflow inputs are bound

These conditions assume that all nodes and workflow i/o changes were done with the functions above, which
do additional checking.


### Properties

| Property | Type | Description |
|-|-|-|
| `compilation_state` |  | {{< multiline >}}Compilation is done a bit at a time, one task or other entity call at a time. This is why this workflow
class has to keep track of its own compilation state.
{{< /multiline >}} |
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `inputs` |  | {{< multiline >}}This holds the input promises to the workflow. The nodes in these Promise objects should always point to
the global start node.
{{< /multiline >}} |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.WorkflowExecutionPhase

This class holds enum values used for setting notifications. See :py:class:`flytekit.Email`
for sample usage.


### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    int_value,
) -> Text
```
| Parameter | Type |
|-|-|
| `int_value` |  |

## flytekit.WorkflowFailurePolicy

Defines the behavior for a workflow execution in the case of an observed node execution failure. By default, a
workflow execution will immediately enter a failed state if a component node fails.


## flytekit.WorkflowReference

A reference object containing metadata that points to a remote workflow.


```python
class WorkflowReference(
    project: str,
    domain: str,
    name: str,
    version: str,
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  |  |
| `resource_type` |  |  |

