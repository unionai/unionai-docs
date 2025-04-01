---
title: flytekit.core.workflow
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`ImperativeWorkflow`](.././flytekit.core.workflow#flytekitcoreworkflowimperativeworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`PythonFunctionWorkflow`](.././flytekit.core.workflow#flytekitcoreworkflowpythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`ReferenceWorkflow`](.././flytekit.core.workflow#flytekitcoreworkflowreferenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`WorkflowBase`](.././flytekit.core.workflow#flytekitcoreworkflowworkflowbase) |  |
| [`WorkflowMetadata`](.././flytekit.core.workflow#flytekitcoreworkflowworkflowmetadata) |  |
| [`WorkflowMetadataDefaults`](.././flytekit.core.workflow#flytekitcoreworkflowworkflowmetadatadefaults) | This class is similarly named to the one above. |

### Methods

| Method | Description |
|-|-|
| [`construct_input_promises()`](#construct_input_promises) |  |
| [`get_promise()`](#get_promise) | This is a helper function that will turn a binding into a Promise object, using a lookup map. |
| [`get_promise_map()`](#get_promise_map) | Local execution of imperatively defined workflows is done node by node. |
| [`reference_workflow()`](#reference_workflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`workflow()`](#workflow) | This decorator declares a function to be a Flyte workflow. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FuncOut` | `TypeVar` |  |
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |

## Methods

#### construct_input_promises()

```python
def construct_input_promises(
    inputs: List[str],
) -> Dict[str, Promise]
```
| Parameter | Type |
|-|-|
| `inputs` | `List[str]` |

#### get_promise()

```python
def get_promise(
    binding_data: _literal_models.BindingData,
    outputs_cache: Dict[Node, Dict[str, Promise]],
) -> Promise
```
This is a helper function that will turn a binding into a Promise object, using a lookup map. Please see
get_promise_map for the rest of the details.


| Parameter | Type |
|-|-|
| `binding_data` | `_literal_models.BindingData` |
| `outputs_cache` | `Dict[Node, Dict[str, Promise]]` |

#### get_promise_map()

```python
def get_promise_map(
    bindings: List[_literal_models.Binding],
    outputs_cache: Dict[Node, Dict[str, Promise]],
) -> Dict[str, Promise]
```
Local execution of imperatively defined workflows is done node by node. This function will fill in the node's
entity's input arguments, which are specified using the bindings list, and a map of nodes to its outputs.
Basically this takes the place of propeller in resolving bindings, pulling in outputs from previously completed
nodes and filling in the necessary inputs.


| Parameter | Type |
|-|-|
| `bindings` | `List[_literal_models.Binding]` |
| `outputs_cache` | `Dict[Node, Dict[str, Promise]]` |

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

## flytekit.core.workflow.ImperativeWorkflow

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
class ImperativeWorkflow(
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

## flytekit.core.workflow.PythonFunctionWorkflow

Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte.
This Python object represents a workflow  defined by a function and decorated with the
:py:func:`@workflow <flytekit.workflow>` decorator. Please see notes on that object for additional information.


```python
class PythonFunctionWorkflow(
    workflow_function: Callable,
    metadata: WorkflowMetadata,
    default_metadata: WorkflowMetadataDefaults,
    docstring: Optional[Docstring],
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
)
```
| Parameter | Type |
|-|-|
| `workflow_function` | `Callable` |
| `metadata` | `WorkflowMetadata` |
| `default_metadata` | `WorkflowMetadataDefaults` |
| `docstring` | `Optional[Docstring]` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `pickle_untyped` | `bool` |
| `default_options` | `Optional[Options]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) | Supply static Python native values in the kwargs if you want them to be used in the compilation. |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) | This function is here only to try to streamline the pattern between workflows and tasks. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### compile()

```python
def compile(
    kwargs,
)
```
Supply static Python native values in the kwargs if you want them to be used in the compilation. This mimics
a 'closure' in the traditional sense of the word.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
)
```
This function is here only to try to streamline the pattern between workflows and tasks. Since tasks
call execute from dispatch_execute which is in local_execute, workflows should also call an execute inside
local_execute. This makes mocking cleaner.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

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
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `function` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.core.workflow.ReferenceWorkflow

A reference workflow is a pointer to a workflow that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.


```python
class ReferenceWorkflow(
    project: str,
    domain: str,
    name: str,
    version: str,
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
)
```
| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) | Please see the local_execute comments in the main task. |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |
| [`unwrap_literal_map_and_execute()`](#unwrap_literal_map_and_execute) | Please see the implementation of the dispatch_execute function in the real task. |


#### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
#### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

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
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
Please see the local_execute comments in the main task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `PythonAutoContainerTask` |

#### unwrap_literal_map_and_execute()

```python
def unwrap_literal_map_and_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
) -> flytekit.models.literals.LiteralMap
```
Please see the implementation of the dispatch_execute function in the real task.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `function` |  |  |
| `id` |  |  |
| `instantiated_in` |  |  |
| `interface` |  |  |
| `lhs` |  |  |
| `location` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `reference` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.core.workflow.WorkflowBase

```python
class WorkflowBase(
    name: str,
    workflow_metadata: WorkflowMetadata,
    workflow_metadata_defaults: WorkflowMetadataDefaults,
    python_interface: Interface,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    default_options: Optional[Options],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `workflow_metadata` | `WorkflowMetadata` |
| `workflow_metadata_defaults` | `WorkflowMetadataDefaults` |
| `python_interface` | `Interface` |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` |
| `docs` | `Optional[Documentation]` |
| `default_options` | `Optional[Options]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


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
#### execute()

```python
def execute(
    kwargs,
)
```
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
### Properties

| Property | Type | Description |
|-|-|-|
| `default_options` |  |  |
| `docs` |  |  |
| `failure_node` |  |  |
| `interface` |  |  |
| `name` |  |  |
| `nodes` |  |  |
| `on_failure` |  |  |
| `output_bindings` |  |  |
| `python_interface` |  |  |
| `short_name` |  |  |
| `workflow_metadata` |  |  |
| `workflow_metadata_defaults` |  |  |

## flytekit.core.workflow.WorkflowMetadata

```python
class WorkflowMetadata(
    on_failure: WorkflowFailurePolicy,
)
```
| Parameter | Type |
|-|-|
| `on_failure` | `WorkflowFailurePolicy` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_model()`](#to_flyte_model) |  |


#### to_flyte_model()

```python
def to_flyte_model()
```
## flytekit.core.workflow.WorkflowMetadataDefaults

This class is similarly named to the one above. Please see the IDL for more information but essentially, this
WorkflowMetadataDefaults class represents the defaults that are handed down to a workflow's tasks, whereas
WorkflowMetadata represents metadata about the workflow itself.


```python
class WorkflowMetadataDefaults(
    interruptible: bool,
)
```
| Parameter | Type |
|-|-|
| `interruptible` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_model()`](#to_flyte_model) |  |


#### to_flyte_model()

```python
def to_flyte_model()
```
