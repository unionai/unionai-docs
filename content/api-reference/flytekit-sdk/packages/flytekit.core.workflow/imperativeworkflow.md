---
title: ImperativeWorkflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImperativeWorkflow

**Package:** `flytekit.core.workflow`

An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is
better suited to programmatic applications.

Assuming you have some tasks like so

&lt;!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
   :start-after: # docs_tasks_start
   :end-before: # docs_tasks_end
   :language: python
   :dedent: 4
--&gt;
```python
@task
def t1(a: str) -> str:
    return a + " world"

@task
def t2():
    print("side effect")
```

You could create a workflow imperatively like so

&lt;!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
   :start-after: # docs_start
   :end-before: # docs_end
   :language: python
   :dedent: 4
--&gt;
```python
# Create the workflow with a name. This needs to be unique within the project and takes the place of the function
# name that's used for regular decorated function-based workflows.
wb = Workflow(name="my_workflow")
# Adds a top level input to the workflow. This is like an input to a workflow function.
wb.add_workflow_input("in1", str)
# Call your tasks.
node = wb.add_entity(t1, a=wb.inputs["in1"])
wb.add_entity(t2)
# This is analogous to a return statement
wb.add_workflow_output("from_n0t1", node.outputs["o0"])
```

This workflow would be identical on the back-end to

&lt;!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_imperative.py
   :start-after: # docs_equivalent_start
   :end-before: # docs_equivalent_end
   :language: python
   :dedent: 4
--&gt;
```python
nt = typing.NamedTuple("wf_output", [("from_n0t1", str)])

@workflow
def my_workflow(in1: str) -> nt:
    x = t1(a=in1)
    t2()
    return nt(x)
```

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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` | |
| `interruptible` | `bool` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `compilation_state` | `None` | Compilation is done a bit at a time, one task or other entity call at a time. This is why this workflow class has to keep track of its own compilation state. |
| `default_options` | `None` |  |
| `docs` | `None` |  |
| `failure_node` | `None` |  |
| `inputs` | `None` | This holds the input promises to the workflow. The nodes in these Promise objects should always point to the global start node. |
| `interface` | `None` |  |
| `name` | `None` |  |
| `nodes` | `None` |  |
| `on_failure` | `None` |  |
| `output_bindings` | `None` |  |
| `python_interface` | `None` |  |
| `short_name` | `None` |  |
| `workflow_metadata` | `None` |  |
| `workflow_metadata_defaults` | `None` |  |

## Methods

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


### add_entity()

```python
def add_entity(
    entity: Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase],
    kwargs,
) -> Node
```
Anytime you add an entity, all the inputs to the entity must be bound.


| Parameter | Type | Description |
|-|-|-|
| `entity` | `Union[PythonTask, _annotated_launch_plan.LaunchPlan, WorkflowBase]` | |
| `kwargs` | `**kwargs` | |

### add_launch_plan()

```python
def add_launch_plan(
    launch_plan: _annotated_launch_plan.LaunchPlan,
    kwargs,
) -> Node
```
| Parameter | Type | Description |
|-|-|-|
| `launch_plan` | `_annotated_launch_plan.LaunchPlan` | |
| `kwargs` | `**kwargs` | |

### add_on_failure_handler()

```python
def add_on_failure_handler(
    entity,
)
```
This is a special function that mimics the add_entity function, but this is only used
to add the failure node. Failure nodes are special because we don't want
them to be part of the main workflow.


| Parameter | Type | Description |
|-|-|-|
| `entity` |  | |

### add_subwf()

```python
def add_subwf(
    sub_wf: WorkflowBase,
    kwargs,
) -> Node
```
| Parameter | Type | Description |
|-|-|-|
| `sub_wf` | `WorkflowBase` | |
| `kwargs` | `**kwargs` | |

### add_task()

```python
def add_task(
    task: PythonTask,
    kwargs,
) -> Node
```
| Parameter | Type | Description |
|-|-|-|
| `task` | `PythonTask` | |
| `kwargs` | `**kwargs` | |

### add_workflow_input()

```python
def add_workflow_input(
    input_name: str,
    python_type: Type,
) -> Promise
```
Adds an input to the workflow.


| Parameter | Type | Description |
|-|-|-|
| `input_name` | `str` | |
| `python_type` | `Type` | |

### add_workflow_output()

```python
def add_workflow_output(
    output_name: str,
    p: Union[Promise, List[Promise], Dict[str, Promise]],
    python_type: Optional[Type],
)
```
Add an output with the given name from the given node output.


| Parameter | Type | Description |
|-|-|-|
| `output_name` | `str` | |
| `p` | `Union[Promise, List[Promise], Dict[str, Promise]]` | |
| `python_type` | `Optional[Type]` | |

### compile()

```python
def compile(
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
### create_conditional()

```python
def create_conditional(
    name: str,
) -> ConditionalSection
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

### execute()

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


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
### ready()

```python
def ready()
```
This function returns whether or not the workflow is in a ready state, which means
  * Has at least one node
  * All workflow inputs are bound

These conditions assume that all nodes and workflow i/o changes were done with the functions above, which
do additional checking.


