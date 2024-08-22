# Custom tasks

Flytekit ships with an extensible task system to make it easy for anyone to extend and add new task types.

```{note}
To contribute a new task type, see the [prebuilt container task plugins](https://docs.flyte.org/en/latest/user_guide/extending/prebuilt_container_task_plugins.html#prebuilt-container) and [user container task plugins](https://docs.flyte.org/en/latest/user_guide/extending/user_container_task_plugins.html#user-container) documentation.
```

## Base task

```{eval-rst}

.. currentmodule:: flytekit.core.base_task

.. autosummary::
   :nosignatures:

   ~kwtypes
   ~PythonTask
   ~Task
   ~TaskResolverMixin
   ~IgnoreOutputs

```

## Python function task

```{eval-rst}

.. currentmodule:: flytekit.core.python_function_task

.. autosummary::
   :nosignatures:

   ~PythonFunctionTask
   ~PythonInstanceTask

```

## Shell task

```{eval-rst}

.. currentmodule:: flytekit.extras.tasks.shell

.. autosummary::
   :nosignatures:

    ~ShellTask
    ~OutputLocation

```

## SQLite3 task

```{eval-rst}

.. currentmodule:: flytekit.extras.sqlite3.task

.. autosummary::
    :nosignatures:

    ~SQLite3Task
    ~SQLite3Config

```

