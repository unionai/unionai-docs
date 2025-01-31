# Authoring structure

Flytekit's main focus is to provide users with the ability to create their own tasks and workflows.
In this section, we'll take a closer look at how this works under the hood.

## Types and type engine

Flyte uses its own type system, which is defined in the [IDL](https://github.com/flyteorg/flyte/tree/master/flyteidl). Despite being a dynamic language, Python also has its own type system, which is primarily explained in [PEP 484](https://www.python.org/dev/peps/pep-0484/). Therefore, Flytekit needs to establish a means of bridging the gap between these two type systems.

```{eval-rst}
This is primariliy accomplished through the use of :py:class:`flytekit.extend.TypeEngine`.
The ``TypeEngine`` works by invoking a series of :py:class:`TypeTransformers <flytekit.extend.TypeTransformer>`. Each transformer is responsible for providing the functionality that the engine requires for a given native Python type.
```

## Callable entities

The Flyte user experience is built around three main concepts: [tasks](../../../user-guide/core-concepts/tasks/index.md), [workflows](../../../user-guide/core-concepts/workflows/index.md), and [launch plans](../../../user-guide/core-concepts/launch-plans/index.md). Each of these concepts is supported by one or more Python classes, which are instantiated by decorators (in the case of tasks and workflows) or a regular Python call (in the case of launch plans).

### Tasks

```{eval-rst}

For more information on each of the classes, please refer to the corresponding documentation.

.. autoclass:: flytekit.core.base_task.Task
   :noindex:

.. autoclass:: flytekit.core.base_task.PythonTask
   :noindex:

.. autoclass:: flytekit.core.python_auto_container.PythonAutoContainerTask
   :noindex:

.. autoclass:: flytekit.core.python_function_task.PythonFunctionTask
   :noindex:
```

### Workflows

There are two workflow classes, both of which derive from the `WorkflowBase` class.

```{eval-rst}

.. autoclass:: flytekit.core.workflow.PythonFunctionWorkflow
   :noindex:

.. autoclass:: flytekit.core.workflow.ImperativeWorkflow
   :noindex:
```

### Launch plans

```{eval-rst}

There is one :py:class:`LaunchPlan <flytekit.core.launch_plan.LaunchPlan>` class.

.. autoclass:: flytekit.core.launch_plan.LaunchPlan
   :noindex:
```

## Exception Handling

[Exception handling](https://github.com/flyteorg/flytekit/tree/master/flytekit/exceptions) occurs along two dimensions:

* **System vs. user:** We distinguish between Flytekit/system-level exceptions and user exceptions. For instance, if Flytekit encounters an issue while uploading outputs, it is considered a system exception. On the other hand, if a user raises a `ValueError` due to an unexpected input in the task code, it is classified as a user exception.
* **Recoverable vs. Non-recoverable:** Recoverable errors are retried and counted toward the task's retry count, while non-recoverable errors simply fail. System exceptions are recoverable by default, since they are usually temporary.

:::{note}
Only `flytekit.exceptions.user.FlyteRecoverableException` is a recoverable execption. All other exceptions, including non-Flytekit defined exceptions, are non-recoverable.
:::

### Implementation

If you wish to delve deeper, you can explore the [`FlyteScopedException`](https://github.com/flyteorg/flytekit/blob/master/flytekit/exceptions/scopes.py) classes.

There are two decorators that are used throughout the codebase.

```{eval-rst}

.. currentmodule:: flytekit.exceptions.scopes

.. autofunction:: flytekit.exceptions.scopes.system_entry_point

.. autofunction:: flytekit.exceptions.scopes.user_entry_point
```

## Call patterns

The entities mentioned above (tasks, workflows, and launch plans) are callable and can be invoked to generate one or more units of work in Flyte.

In Pythonic terminology, adding `()` to the end of an entity invokes the `__call__` method on the object.

```{eval-rst}
The behavior that occurs when a callable entity is invoked depends on the current context, specifically the current :py:class:`flytekit.FlyteContext`.
```

### Raw task execution

When a task is executed as part of a unit test, the `@union.task` decorator transforms the decorated function into an instance of the `PythonFunctionTask` object. However, when a user invokes the `task()` function outside of a workflow, the original function is called without any intervention from Flytekit.

### Task execution inside a workflow

When a workflow is executed locally (for instance, as part of a unit test), some modifications are made to the task.

```{eval-rst}

Before proceeding, it is worth noting a special object, the :py:class:`flytekit.extend.Promise`.

.. autoclass:: flytekit.core.promise.Promise
   :noindex:
```

Consider the following workflow:

```{code} python
@union.task
def t1(a: int) -> Tuple[int, str]:
    return a + 2, "world"

@union.task
def t2(a: str, b: str) -> str:
    return b + a

@union.workflow
def my_wf(a: int, b: str) -> Tuple[int, str]:
    x, y = t1(a=a).with_overrides(...)
    d = t2(a=y, b=b)
    return x, d
```

As stated in the [documentation for the Promise object](../extending-flytekit.md#flytekit.extend.Promise), when a task is invoked within a workflow, the Python native values returned by the underlying functions are first converted into Flyte IDL literals and then encapsulated inside Promise objects.
One Promise object is created for each return variable.

When the next task is invoked, the values are extracted from these Promises.

### Compilation

```{eval-rst}
During the workflow compilation process, instead of generating Promise objects that encapsulate literal values, the workflow encapsulates a :py:class:`flytekit.core.promise.NodeOutput`.
This approach aids in tracking the data dependencies between tasks.
```

### Branch skip

```{eval-rst}
If the condition specified in a :py:func:`flytekit.conditional` evaluates to ``False``, Flytekit will avoid invoking the corresponding task. This prevents the unintended execution of the task.
```

```{note}
The execution pattern discussed for tasks can be applied to workflows and launch plans as well.
```
