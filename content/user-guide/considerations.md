---
title: Considerations
weight: 14
variants: +flyte +serverless +byoc +selfmanaged
---

# Considerations

Flyte 2 represents a substantial change from Flyte 1.
While the static graph execution model will soon be available and will mirror Flyte 1 almost exactly, the primary mode of execution in Flyte 2 should remain pure-Python-based.
That is, each Python-based task action has the ability to act as its own engine, kicking off sub-actions, and assembling the outputs, passing them to yet other sub-actions and such.

While this model of execution comes with an enormous amount of flexibility, as the examples in this tutorial demonstrate, that flexibility does warrant some caveats to keep in mind when authoring your tasks.

## Non-deterministic behavior

When a task launches another task, a new Action ID is determined.
This ID is a hash of the inputs to the task, the task definition itself, along with some other information.
The fact that this ID is consistently hashed is important when it comes to things like recovery and replay.

For example, assume you have the following tasks

```python
@env.task
async def t1():
    val = get_int_input()
    await t2(int=val)

@env.task
async def t2(val: int): ...
```

If you run `t1`, and it launches the downstream `t2` task, and then the pod executing `t1` fails, when Flyte restarts `t1` it will automatically detect that `t2` is still running and will just use that.
If `t2` ends up finishing in the interim, those results would just be used.

However, if you introduce non-determinism into the picture, then that guarantee is no longer there.
To give a contrived example:

```python
@env.task
async def t1():
    val = get_int_input()
    now = datetime.now()

    if now.second % 2 == 0:
        await t2(int=val)
    else:
        await t3(int=val)
```

Here, depending on what time it is, either `t2` or `t3` may end up running.
In the earlier scenario, if `t1` crashes unexpectedly, and Flyte retries the execution, a different downstream task may get kicked off instead.

## Type safety

In Flyte 1, the top-level workflow was defined by a Python-like DSL that was compiled into a static DAG composed of tasks, each of which was, internally, defined in real Python.
The system was able to guarantee type safety across task boundaries because the task definitions were static and the inputs and outputs were defined in a way that Flytekit could validate them.

In Flyte 2, the top-level workflow is defined by Python code that runs at runtime.
This means that the system can no longer guarantee type safety at the workflow level.

Happily, the Python ecosystem has evolved considerably since Flyte 1, and Python type hints are now a standard way to define types.

Consequently, in Flyte 2, developers should use Python type hints and type checkers like `mypy` to ensure type safety at all levels, including the top-most task (i.e., the "workflow" level).

## Driver pod requirements

Tasks don't have to kick off downstream tasks of course and may themselves represent a leaf level atomic unit of compute.
However, when tasks do run other tasks, and more so if they assemble the outputs of those other tasks, then that parent task becomes a driver
pod of sorts.
In Flyte 1, this assembling of intermediate outputs was done by Flyte Propeller.
In 2, it's done by the parent task.

This means that the pod running your parent task must be appropriately sized, and should ideally not be CPU-bound. For example,
if you had this also scenario,

```python
@env.task
async def t_main():
    await t1()
    local_cpu_intensive_function()
    await t2()
```
The pod running `t_main` will hang in between tasks `t1` and `t2`. Your parent tasks should ideally focus only on orchestration.

### OOM risk from materialized IO

Something maybe more nuanced to keep in mind is that if you're not using the soon-to-be-released ref mode, outputs are actually
materialized. That is, if you have the following scenario,

```python
@env.task
async def produce_1gb_list() -> List[float]: ...

@env.task
async def t1():
    list_floats = produce_1gb_list()
    t2(floats=list_floats)
```

The pod running `t1` needs to have memory to handle that 1 GB of floats. Those numbers will be materialized in that pod's memory.
This can lead to out of memory issues.

Note that `flyte.io.File` and `flyte.io.Dir` will not suffer from this because while those are materialized, they're only materialized as pointers to offloaded data, so their memory footprint is much lower.
