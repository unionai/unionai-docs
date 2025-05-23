---
title: Decorating workflows
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Decorating workflows

The behavior of workflows can be modified in a lightweight fashion by using the built-in `functools.wraps`
decorator pattern, similar to using decorators to
[customize task behavior](#decorating_tasks). However, unlike in the case of
tasks, we need to do a little extra work to make sure that the DAG underlying the workflow executes tasks in the correct order.

## Setup-teardown pattern

The main use case of decorating `@{{< key kit_as >}}.workflow`-decorated functions is to establish a setup-teardown pattern to execute task
before and after your main workflow logic. This is useful when integrating with other external services
like [wandb](https://wandb.ai/site) or [clearml](https://clear.ml/), which enable you to track metrics of model training runs.

To begin, create a file called `decorating_workflows`.

Import the necessary libraries:

```python
from functools import partial, wraps
from unittest.mock import MagicMock

import {{< key kit_import >}}
from flytekit import FlyteContextManager
from flytekit.core.node_creation import create_node
```

Let's define the tasks we need for setup and teardown. In this example, we use the
`unittest.mock.MagicMock` class to create a fake external service that we want to initialize at the
beginning of our workflow and finish at the end.

```python
external_service = MagicMock()


@{{< key kit_as >}}.task
def setup():
    print("initializing external service")
    external_service.initialize(id=flytekit.current_context().execution_id)


@{{< key kit_as >}}.task
def teardown():
    print("finish external service")
    external_service.complete(id=flytekit.current_context().execution_id)
```

As you can see, you can even use Flytekit's current context to access the `execution_id` of the current workflow
if you need to link Flyte with the external service so that you reference the same unique identifier in both the
external service and Flyte.

## Workflow decorator

We create a decorator that we want to use to wrap our workflow function.

```python
def setup_teardown(fn=None, *, before, after):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # get the current flyte context to obtain access to the compilation state of the workflow DAG.
        ctx = FlyteContextManager.current_context()

        # defines before node
        before_node = create_node(before)
        # ctx.compilation_state.nodes == [before_node]

        # under the hood, flytekit compiler defines and threads
        # together nodes within the `my_workflow` function body
        outputs = fn(*args, **kwargs)
        # ctx.compilation_state.nodes == [before_node, *nodes_created_by_fn]

        # defines the after node
        after_node = create_node(after)
        # ctx.compilation_state.nodes == [before_node, *nodes_created_by_fn, after_node]

        # compile the workflow correctly by making sure `before_node`
        # runs before the first workflow node and `after_node`
        # runs after the last workflow node.
        if ctx.compilation_state is not None:
            # ctx.compilation_state.nodes is a list of nodes defined in the
            # order of execution above
            workflow_node0 = ctx.compilation_state.nodes[1]
            workflow_node1 = ctx.compilation_state.nodes[-2]
            before_node >> workflow_node0
            workflow_node1 >> after_node
        return outputs

    if fn is None:
        return partial(setup_teardown, before=before, after=after)

    return wrapper
```

There are a few key pieces to note in the `setup_teardown` decorator above:

1. It takes a `before` and `after` argument, both of which need to be `@{{< key kit_as >}}.task`-decorated functions. These
   tasks will run before and after the main workflow function body.
2. The [create_node](https://github.com/flyteorg/flytekit/blob/9e156bb0cf3d1441c7d1727729e8f9b4bbc3f168/flytekit/core/node_creation.py#L18) function
   to create nodes associated with the `before` and `after` tasks.
3. When `fn` is called, under the hood the system creates all the nodes associated with the workflow function body
4. The code within the `if ctx.compilation_state is not None:` conditional is executed at compile time, which
   is where we extract the first and last nodes associated with the workflow function body at index `1` and `-2`.
5. The `>>` right shift operator ensures that `before_node` executes before the
   first node and `after_node` executes after the last node of the main workflow function body.

## Defining the DAG

We define two tasks that will constitute the workflow.

```python
@{{< key kit_as >}}.task
def t1(x: float) -> float:
    return x - 1


@{{< key kit_as >}}.task
def t2(x: float) -> float:
    return x**2
```

And then create our decorated workflow:

```python
@{{< key kit_as >}}.workflow
@setup_teardown(before=setup, after=teardown)
def decorating_workflow(x: float) -> float:
    return t2(x=t1(x=x))

```

## Run the example on the Flyte cluster

To run the provided workflow on the Flyte cluster, use the following command:

{{< variant flyte >}}
{{< markdown >}}
```bash
pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/advanced_composition/advanced_composition/decorating_workflows.py \
  decorating_workflow --x 10.0
```
{{< /markdown >}}
{{< /variant >}}

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}
```bash
union run --remote decorating_workflows.py decorating_workflow --x 10.0
```
{{< /markdown >}}
{{< /variant >}}
