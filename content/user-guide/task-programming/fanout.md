---
title: Fanout
weight: 17
variants: +flyte +union
---

# Fanout

Flyte is designed to scale effortlessly, allowing you to run workflows with large fanouts.
When you need to execute many tasks in parallel—such as processing a large dataset or running hyperparameter sweeps—Flyte provides powerful patterns to implement these operations efficiently.

{{< note >}}
In Flyte 1, mapping a task over many inputs used `map_task()` (the `flytekit.map_task` API). In Flyte 2, fan out with `asyncio.gather()` or `flyte.map()`.
{{< /note >}}

{{< variant union >}}
{{< markdown >}}
> [!NOTE]
> By default fanouts in Union are limited to a maximum size.
> Adjustment can made to this maximum by consulting with the Union team.
> Full documentation of this aspect of fanout is coming soon.
{{< /markdown >}}
{{< /variant >}}

## Understanding fanout

A "fanout" pattern occurs when you spawn multiple tasks concurrently.
Each task runs in its own container and contributes an output that you later collect.
The most common way to implement this is using the [`asyncio.gather`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather) function.

In Flyte terminology, each individual task execution is called an "action"—this represents a specific invocation of a task with particular inputs. When you call a task multiple times in a loop, you create multiple actions.

## Example

We start by importing our required packages, defining our Flyte environment, and creating a simple task that fetches user data from a mock API.

{{< code file="/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="setup" lang="python" >}}

### Parallel execution

Next we implement the most common fanout pattern, which is to collect task invocations and execute them in parallel using `asyncio.gather()`:

{{< code file="/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="parallel" lang="python" >}}

### Running the example

To actually run our example, we create a main guard that initializes Flyte and runs our main driver task:

{{< code file="/unionai-examples/v2/user-guide/task-programming/fanout/fanout.py" fragment="run" lang="python" >}}

## How Flyte handles concurrency and parallelism

In the example we use a standard `asyncio.gather()` pattern.
When this pattern is used in a normal Python environment, the tasks would execute **concurrently** (cooperatively sharing a single thread through the event loop), but not in true **parallel** (multiple CPU cores simultaneously).

However, **Flyte transforms this concurrency model into true parallelism**. When you use `asyncio.gather()` in a Flyte task:

1. **Flyte acts as a distributed event loop**: Instead of scheduling coroutines on a single machine, Flyte schedules each task action to run in its own container across the cluster
2. **Concurrent becomes parallel**: What would be cooperative multitasking in regular Python becomes true parallel execution across multiple machines
3. **Native Python patterns**: You use familiar `asyncio` patterns, but Flyte automatically distributes the work

This means that when you write:
```python
results = await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
```

Instead of three coroutines sharing one CPU, you get three separate containers running simultaneously, each with their own CPU, memory, and resources. Flyte seamlessly bridges the gap between Python's concurrency model and distributed parallel computing, allowing for massive scalability while maintaining the familiar async/await programming model.

## Iterative fanout: recursive feature elimination

Fanout isn't limited to a single parallel burst—you can fan out **repeatedly**, using the results of one round to shape the next.
A good real-world example is [recursive feature elimination (RFE)](https://github.com/flyteorg/flyte-sdk/blob/main/examples/ml/rfe.py), a feature-selection technique that repeatedly trains a model with one candidate feature held out, drops the feature whose removal least hurts the score, and repeats until a single feature remains.
Every iteration is itself a fanout: for each remaining feature, a `train` action runs in parallel with that feature dropped, scored by cross-validation.

The `train` task evaluates the model with a single feature held out and returns its cross-validated score:

```python
@worker.task
async def train(features: list[str], drop: str) -> float:
    features.remove(drop)

    X, y = fetch_california_housing(as_frame=True, return_X_y=True)
    fold = KFold(n_splits=5, random_state=42, shuffle=True)
    model = LinearRegression()

    scores = cross_val_score(estimator=model, X=X[features], y=y, cv=fold, scoring="r2")
    return float(scores.mean())
```

The `rfe` driver task runs the elimination loop.
Each round wraps its fanout in a `flyte.group` context (see [Grouping actions](./grouping-actions)) so the iterations appear as collapsible folders in the UI, and uses `asyncio.gather()` to evaluate every candidate feature in parallel:

```python
@worker.task
async def rfe():
    x, _y = fetch_california_housing(as_frame=True, return_X_y=True)
    features = list(x.columns)

    for i in range(len(features) - 1):
        with flyte.group(f"iteration-{i}"):
            runs = {feature: train(list(features), drop=feature) for feature in features}
            values = await asyncio.gather(*(runs[feature] for feature in runs))
            scores = dict(zip(runs.keys(), values))
            best = max(scores, key=scores.get)
            features.remove(best)
```

Because each `train` call becomes its own action, every iteration's candidate evaluations run as separate containers in true parallel, while grouping keeps the nested rounds organized in the run tree.

{{< note >}}
The full runnable example lives in the [Flyte SDK repository](https://github.com/flyteorg/flyte-sdk/blob/main/examples/ml/rfe.py). From a local checkout of the `flyte-sdk` repository, run it with `uv run --prerelease=allow examples/ml/rfe.py` (the command uses a repo-relative path).
{{< /note >}}