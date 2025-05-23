---
title: Decorating tasks
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Decorating tasks

You can easily change how tasks behave by using decorators to wrap your task functions.

In order to make sure that your decorated function contains all the type annotation and docstring
information that Flyte needs, you will need to use the built-in `functools.wraps` decorator.

To begin, create a file called `decorating_tasks.py`.

Add the the imports:

```python
import logging
import {{< key kit_import >}}
from functools import partial, wraps
```

Create a logger to monitor the execution's progress.

```python
logger = logging.getLogger(__file__)
```

## Using a single decorator

We define a decorator that logs the input and output details for a decorated task.

```python
def log_io(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logger.info(f"task {fn.__name__} called with args: {args}, kwargs: {kwargs}")
        out = fn(*args, **kwargs)
        logger.info(f"task {fn.__name__} output: {out}")
        return out

    return wrapper
```

We create a task named `t1` that is decorated with `log_io`.

> [!NOTE]
> The order of invoking the decorators is important. `@task` should always be the outer-most decorator.

```python
@{{< key kit_as >}}.task
@log_io
def t1(x: int) -> int:
    return x + 1
```

## Stacking multiple decorators

You can also stack multiple decorators on top of each other as long as `@task` is the outer-most decorator.

We define a decorator that verifies if the output from the decorated function is a positive number before it's returned.
If this assumption is violated, it raises a `ValueError` exception.

```python
def validate_output(fn=None, *, floor=0):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        out = fn(*args, **kwargs)
        if out <= floor:
            raise ValueError(f"output of task {fn.__name__} must be a positive number, found {out}")
        return out

    if fn is None:
        return partial(validate_output, floor=floor)

    return wrapper
```

> [!NOTE]
> The output of the `validate_output` task uses `functools.partial` to implement parameterized decorators.

We define a function that uses both the logging and validator decorators.

```python
@{{< key kit_as >}}.task
@log_io
@validate_output(floor=10)
def t2(x: int) -> int:
    return x + 10
```

Finally, we compose a workflow that calls `t1` and `t2`.

```python
@{{< key kit_as >}}.workflow
def decorating_task_wf(x: int) -> int:
    return t2(x=t1(x=x))
```

## Run the example on {{< key product_name >}}

To run the workflow, execute the following command:

{{< variant flyte >}}
{{< markdown >}}
```bash
pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/advanced_composition/advanced_composition/decorating_tasks.py \
  decorating_task_wf --x 10
```
{{< /markdown >}}
{{< /variant >}}

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}
```bash
union run --remote decorating_tasks.py decorating_task_wf --x 10
```
{{< /markdown >}}
{{< /variant >}}
