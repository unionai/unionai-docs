---
title: Eager workflows
weight: 5
variants: +flyte +serverless +byoc +byok
---

# Eager workflows

> [!NOTE]
> This feature is experimental and the API is subject to breaking changes.
> If you encounter any issues please reach out to the Union team.

Eager workflows allow you to create workflows that give you runtime access to
intermediary task/subworkflow outputs.

Both static and dynamic workflows have a key limitation: while they provide
compile-time and runtime type safety, respectively, they both suffer from
inflexibility in expressing asynchronous execution graphs that many Python
programmers may be accustomed to by using, for example, the
[asyncio](https://docs.python.org/3/library/asyncio.html) library.

Unlike static and dynamic workflows, eager workflows allow you to use all of
the Python constructs that you're familiar with via the `asyncio` API. To
understand what this looks like, let's define a very basic eager workflow
using the `@eager` decorator.

```python
from union import task, workflow
from flytekit.experimental import eager


@union.task
def add_one(x: int) -> int:
    return x + 1


@union.task
def double(x: int) -> int:
    return x * 2


@eager
async def simple_eager_workflow(x: int) -> int:
    out = await add_one(x=x)
    if out < 0:
        return -1
    return await double(x=out)
```

As we can see in the code above, we define an `async` function called
`simple_eager_workflow` that takes an integer as input and returns an integer.
By decorating this function with `@eager`, we now have the ability to invoke
tasks, static subworkflows, and even other eager subworkflows in an _eager_
fashion such that we can materialize their outputs and use them inside the
parent eager workflow itself.

In the `simple_eager_workflow` function, we can see that we're `await`ing
the output of the `add_one` task and assigning it to the `out` variable. If
`out` is a negative integer, the workflow will return `-1`. Otherwise, it
will double the output of `add_one` and return it.

Unlike in static and dynamic workflows, this variable is actually
the Python integer that is the result of `x + 1` and not a Promise.

## How eager workflows work

When you decorate a function with `@eager`, any function invoked within it
that's decorated with `@union.task`, `@union.workflow`, or `@eager` becomes
an [awaitable](https://docs.python.org/3/library/asyncio-task.html#awaitables)
object within the lifetime of the parent eager workflow execution. Note that
this happens automatically and you don't need to use the `async` keyword when
defining a task or workflow that you want to invoke within an eager workflow.

> [!NOTE]
> With eager workflows, you basically have access to the Python `asyncio`
> interface to define extremely flexible execution graphs. The trade-off is that
> you lose the compile-time type safety that you get with regular static workflows
> and to a lesser extent, dynamic workflows.
>
> We're leveraging Python's native `async` capabilities in order to:
>
> 1. Materialize the output of tasks and subworkflows so you can operate
>    on them without spinning up another pod and also determine the shape of the
>    workflow graph in an extremely flexible manner.
> 2. Provide an alternative way of achieving concurrency in {{< var product_upper >}}. {{< var product_upper >}} has
>    concurrency built into it, so all tasks and subworkflows will execute concurrently
>    assuming that they don't have any dependencies on each other. However, eager
>    workflows provide a Python-native way of doing this, with the main downside
>    being that you lose the benefits of statically compiled workflows, such as
>    compile-time analysis and first-class data lineage tracking.

Similar to [dynamic workflows](./dynamic-workflows.md), eager workflows are
actually tasks. The main difference is that, while dynamic workflows compile
a static workflow at runtime using materialized inputs, eager workflows do
not compile any workflow at all. Instead, they use the [`FlyteRemote`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote)
object together with Python's `asyncio` API to kick off tasks and subworkflow
executions eagerly whenever you `await` on a coroutine. This means that eager
workflows can materialize an output of a task or subworkflow and use it as a
Python object in the underlying runtime environment.

## Eager workflow use cases

In this section, we'll cover a few of the use cases that you can accomplish
with eager workflows, some of which you can't accomplish with static or dynamic
workflows.

### Operating on task and subworkflow outputs

One of the biggest benefits of eager workflows is that you can materialize
task and subworkflow outputs as Python values and do operations on them just
like you would in any other Python function. Let's look at another example:

```python
@eager
async def another_eager_workflow(x: int) -> int:
    out = await add_one(x=x)

    # out is a Python integer
    out = out - 1

    return await double(x=out)
```

Since `out` is an actual Python integer and not a Promise, we can do operations
on it at runtime, inside the eager workflow function body. This is not possible
with static or dynamic workflows.

### Pythonic conditionals

As you saw in the `simple_eager_workflow` workflow above, you can use regular
Python conditionals in your eager workflows. Let's look at a more complicated
example:

```python
@union.task
def gt_100(x: int) -> bool:
    return x > 100


@eager
async def eager_workflow_with_conditionals(x: int) -> int:
    out = await add_one(x=x)

    if out < 0:
        return -1
    elif await gt_100(x=out):
        return 100
    else:
        out = await double(x=out)

    assert out >= -1
    return out
```

In the above example, we're using the eager workflow's Python runtime
to check if `out` is negative, but we're also using the `gt_100` task in the
`elif` statement, which will be executed in a separate task.

### Loops

You can gather the outputs of multiple tasks or subworkflows into a list:

```python
import asyncio


@eager
async def eager_workflow_with_for_loop(x: int) -> int:
    outputs = []

    for i in range(x):
        outputs.append(add_one(x=i))

    outputs = await asyncio.gather(*outputs)
    return await double(x=sum(outputs))
```

### Static subworkflows

You can invoke static workflows from within an eager workflow:

```python
@union.workflow
def subworkflow(x: int) -> int:
    out = add_one(x=x)
    return double(x=out)


@eager
async def eager_workflow_with_static_subworkflow(x: int) -> int:
    out = await subworkflow(x=x)
    assert out == (x + 1) * 2
    return out
```

### Eager subworkflows

You can have nested eager subworkflows inside a parent eager workflow:

```python
@eager
async def eager_subworkflow(x: int) -> int:
    return await add_one(x=x)


@eager
async def nested_eager_workflow(x: int) -> int:
    out = await eager_subworkflow(x=x)
    return await double(x=out)
```

### Catching exceptions

You can catch exceptions in eager workflows through `EagerException`:

```python
from flytekit.experimental import EagerException


@union.task
def raises_exc(x: int) -> int:
    if x <= 0:
        raise TypeError
    return x


@eager
async def eager_workflow_with_exception(x: int) -> int:
    try:
        return await raises_exc(x=x)
    except EagerException:
        return -1
```

Even though the `raises_exc` exception task raises a `TypeError`, the
`eager_workflow_with_exception` runtime will raise an `EagerException` and
you'll need to specify `EagerException` as the exception type in your `try... except`
block.

> [!NOTE]
> This is a current limitation in the `@eager` workflow implementation.

## Executing eager workflows

As with most {{< var product_upper >}} constructs, you can execute eager workflows both locally
and remotely.

### Local execution

You can execute eager workflows locally by simply calling them like a regular
`async` function:

```python
if __name__ == "__main__":
    result = asyncio.run(simple_eager_workflow(x=5))
    print(f"Result: {result}")  # "Result: 12"
```

This just uses the `asyncio.run` function to execute the eager workflow just
like any other Python async code. This is useful for local debugging as you're
developing your workflows and tasks.

### Remote Union cluster execution

Under the hood, `@eager` workflows use the [`UnionRemote`](../../../api-reference/union-sdk/union-remote/index.md)
object to kick off task, static workflow, and eager workflow executions.

In order to actually execute them on a Union cluster, you'll need to configure
eager workflows with a `UnionRemote` object and secrets configuration that
allows you to authenticate into the cluster via a client secret key.

```python
from union import UnionRemote
from flytekit.configuration import Config

@eager(
    remote=UnionRemote(
        config=Config.auto(config_file="config.yaml"),
        default_project="{{< var default_project >}}",
        default_domain="development",
    ),
    client_secret_group="<my_client_secret_group>",
    client_secret_key="<my_client_secret_key>",
)
async def eager_workflow_remote(x: int) -> int:
    ...
```

Where `config.yaml` contains a Union config file and `my_client_secret_group` and `my_client_secret_key` are the secret group and key that you've configured for your Union
instance.

### Sandbox Flyte cluster execution

When using a sandbox cluster started with `uctl demo start`, however, the
`client_secret_group` and `client_secret_key` are not required, since the
default sandbox configuration does not require key-based authentication.

```python
from flytekit.configuration import Config
from union import UnionRemote


@eager(
    remote=FlyteRemote(
        config=Config.for_sandbox(),
        default_project="{{< var default_project >}}",
        default_domain="development",
    )
)
async def eager_workflow_sandbox(x: int) -> int:
    out = await add_one(x=x)
    if out < 0:
        return -1
    return await double(x=out)
```

> [!NOTE]
> When executing eager workflows on a remote Union cluster, Union will execute the
> latest version of tasks, static workflows, and eager workflows that are on
> the `default_project` and `default_domain` as specified in the `UnionRemote`
> object. This means that you need to pre-register all entities that are
> invoked inside of the eager workflow.

### Registering and running

Assuming that your code is configured correctly, you will need to
register all of the task and subworkflows that are used with your eager
workflow with `union register`:

```shell
union --config <path/to/config.yaml> register \
 --project <project> \
 --domain <domain> \
 --image <image> \
 path/to/eager_workflows.py
```

And then run it with `union run`:

```shell
union --config <path/to/config.yaml> run \
 --project <project> \
 --domain <domain> \
 --image <image> \
 path/to/eager_workflows.py simple_eager_workflow --x 10
```

> [!NOTE]
> You need to register the tasks/workflows associated with your eager workflow because eager workflows are actually tasks under the hood,
> which means that `union run` has no way of knowing what tasks and subworkflows are invoked inside of it.

## Eager workflows in the UI

Since eager workflows are an experimental feature, there is currently no first-class representation of them in the UI. When you register an eager workflow, you'll be able to see it in the task view.

When you execute an eager workflow, the tasks and subworkflows invoked within it **will not appear** on the node, graph, or timeline view. As mentioned above, this is because eager workflows are actually Flyte tasks under the hood and Union has no way of knowing the shape of the execution graph before actually executing them.

However, at the end of execution, you'll be able to use [Flyte Decks](https://docs.flyte.org/en/latest/user_guide/development_lifecycle/decks.html) to see a list of all the tasks and subworkflows that were executed within the eager workflow.

## Limitations

As eager workflows are still experimental, there are a few limitations to keep in mind:

- You cannot invoke [dynamic workflows](./dynamic-workflows.md), [map tasks](../tasks/task-types.md#map-tasks), or [launch plans](../launch-plans/index.md) inside an eager workflow.
- [Context managers](https://docs.python.org/3/library/contextlib.html) will only work on locally executed functions within the eager workflow, i.e. using a context manager to modify the behavior of a task or subworkflow will not work because they are executed on a completely different pod.
- All exceptions raised by Flyte tasks or workflows will be caught and raised as an [`EagerException`](../../../api-reference/union-sdk/experimental-features.md) at runtime.
- All task/subworkflow outputs are materialized as Python values, which includes offloaded types like `FlyteFile`, `FlyteDirectory`, `StructuredDataset`, and `pandas.DataFrame` will be fully downloaded into the pod running the eager workflow. This prevents you from incrementally downloading or streaming very large datasets in eager workflows.
- Union entities that are invoked inside an eager workflow must be registered under the same project and domain as the eager workflow itself. The eager workflow will execute the latest version of these entities.
- The UI currently does not have a first-class way of viewing eager workflows, but it can be accessed via the task list view and the execution graph is viewable via Flyte Decks.
