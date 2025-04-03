# Decorating tasks

You can easily change how tasks behave by using decorators to wrap your task functions.

In order to make sure that your decorated function contains all the type annotation and docstring
information that Flyte needs, you will need to use the built-in `functools.wraps` decorator.

To begin, import the required dependencies.

```python
# File: advanced_composition/decorating_tasks.py
# Lines: 1-4
```

Create a logger to monitor the execution's progress.

```python
# File: advanced_composition/decorating_tasks.py
# Line: 7
```

## Using a single decorator

We define a decorator that logs the input and output details for a decorated task.

```python
# File: advanced_composition/decorating_tasks.py
# Object: log_io
```

We create a task named `t1` that is decorated with `log_io`.

> [!NOTE]
> The order of invoking the decorators is important. `@task` should always be the outer-most decorator.

```python
# File: advanced_composition/decorating_tasks.py
# Object: t1
```

## Stacking multiple decorators

You can also stack multiple decorators on top of each other as long as `@task` is the outer-most decorator.

We define a decorator that verifies if the output from the decorated function is a positive number before it's returned.
If this assumption is violated, it raises a `ValueError` exception.

```python
# File: advanced_composition/decorating_tasks.py
# Object: validate_output
```

> [!NOTE]
> The output of the `validate_output` task uses `functools.partial` to implement parameterized decorators.

We define a function that uses both the logging and validator decorators.

```python
# File: advanced_composition/decorating_tasks.py
# Object: t2
```

Finally, we compose a workflow that calls `t1` and `t2`.

```python
# File: advanced_composition/decorating_tasks.py
# Lines: 53-59
```

## Run the example on the Flyte cluster

To run the provided workflow on the Flyte cluster, use the following command:

```bash
pyflyte run --remote \
  https://raw.githubusercontent.com/flyteorg/flytesnacks/69dbe4840031a85d79d9ded25f80397c6834752d/examples/advanced_composition/advanced_composition/decorating_tasks.py \
  decorating_task_wf --x 10
```

In this example, you learned how to modify the behavior of tasks via function decorators using the built-in
`functools.wraps` decorator pattern. To learn more about how to extend Flyte at a deeper level, for
example creating custom types, custom tasks or backend plugins,
see [Extending Flyte](https://www.union.ai/docs/flyte/plugins_extend).
