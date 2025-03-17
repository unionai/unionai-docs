---
title: Workflow
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Workflow

**Package:** `flytekit`

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
def Workflow(
    name: str,
    failure_policy: Optional[WorkflowFailurePolicy],
    interruptible: bool,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `name` | `str` |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` |
| `interruptible` | `bool` |
## Methods

### add_entity()

```python
def add_entity(
    entity: Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase],
    kwargs,
):
```
Anytime you add an entity, all the inputs to the entity must be bound.


| Parameter | Type |
|-|-|
| `entity` | `Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase]` |
| `kwargs` | ``**kwargs`` |
### add_launch_plan()

```python
def add_launch_plan(
    launch_plan: _annotated_launch_plan.LaunchPlan,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `launch_plan` | `_annotated_launch_plan.LaunchPlan` |
| `kwargs` | ``**kwargs`` |
### add_on_failure_handler()

```python
def add_on_failure_handler(
    entity,
):
```
This is a special function that mimics the add_entity function, but this is only used
to add the failure node. Failure nodes are special because we don't want
them to be part of the main workflow.


| Parameter | Type |
|-|-|
| `entity` |  |
### add_subwf()

```python
def add_subwf(
    sub_wf: WorkflowBase,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `sub_wf` | `WorkflowBase` |
| `kwargs` | ``**kwargs`` |
### add_task()

```python
def add_task(
    task: PythonTask,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task` | `PythonTask` |
| `kwargs` | ``**kwargs`` |
### add_workflow_input()

```python
def add_workflow_input(
    input_name: str,
    python_type: Type,
):
```
Adds an input to the workflow.


| Parameter | Type |
|-|-|
| `input_name` | `str` |
| `python_type` | `Type` |
### add_workflow_output()

```python
def add_workflow_output(
    output_name: str,
    p: Union[Promise, List[Promise], Dict[str, Promise]],
    python_type: Optional[Type],
):
```
Add an output with the given name from the given node output.


| Parameter | Type |
|-|-|
| `output_name` | `str` |
| `p` | `Union[Promise, List[Promise], Dict[str, Promise]]` |
| `python_type` | `Optional[Type]` |
### compile()

```python
def compile(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |
### construct_node_metadata()

```python
def construct_node_metadata()
```
No parameters
### create_conditional()

```python
def create_conditional(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
### execute()

```python
def execute(
    kwargs,
):
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
### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `kwargs` | ``**kwargs`` |
### local_execution_mode()

```python
def local_execution_mode()
```
No parameters
### ready()

```python
def ready()
```
This function returns whether or not the workflow is in a ready state, which means
* Has at least one node
* All workflow inputs are bound

These conditions assume that all nodes and workflow i/o changes were done with the functions above, which
do additional checking.


No parameters
