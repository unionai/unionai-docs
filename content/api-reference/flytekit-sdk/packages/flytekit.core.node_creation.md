---
title: flytekit.core.node_creation
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.node_creation

## Directory

### Methods

| Method | Description |
|-|-|
| [`create_node()`](#create_node) | This is the function you want to call if you need to specify dependencies between tasks that don't consume and/or. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### create_node()

```python
def create_node(
    entity: Union[PythonTask, LaunchPlan, WorkflowBase, RemoteEntity],
    args,
    kwargs,
) -> Union[Node, VoidPromise]
```
This is the function you want to call if you need to specify dependencies between tasks that don't consume and/or
don't produce outputs. For example, if you have t1() and t2(), both of which do not take in nor produce any
outputs, how do you specify that t2 should run before t1? ::

    t1_node = create_node(t1)
    t2_node = create_node(t2)

    t2_node.runs_before(t1_node)
    # OR
    t2_node >> t1_node

This works for tasks that take inputs as well, say a ``t3(in1: int)`` ::

    t3_node = create_node(t3, in1=some_int)  # basically calling t3(in1=some_int)

You can still use this method to handle setting certain overrides ::

    t3_node = create_node(t3, in1=some_int).with_overrides(...)

Outputs, if there are any, will be accessible. A `t4() -> (int, str)` ::

    t4_node = create_node(t4)

In compilation node.o0 has the promise. ::
    t5(in1=t4_node.o0)

If t1 produces only one output, note that in local execution, you still get a wrapper object that
needs to be dereferenced by the output name. ::

    t1_node = create_node(t1)
    t2(t1_node.o0)


| Parameter | Type |
|-|-|
| `entity` | `Union[PythonTask, LaunchPlan, WorkflowBase, RemoteEntity]` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

