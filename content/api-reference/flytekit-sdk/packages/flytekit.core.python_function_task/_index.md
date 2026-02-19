---
title: flytekit.core.python_function_task
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.python_function_task

## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncPythonFunctionTask`](../flytekit.core.python_function_task/asyncpythonfunctiontask) | This is the base task for eager tasks, as well as normal async tasks. |
| [`EagerAsyncPythonFunctionTask`](../flytekit.core.python_function_task/eagerasyncpythonfunctiontask) | This is the base eager task (aka eager workflow) type. |
| [`EagerFailureHandlerTask`](../flytekit.core.python_function_task/eagerfailurehandlertask) |  |
| [`EagerFailureTaskResolver`](../flytekit.core.python_function_task/eagerfailuretaskresolver) |  |
| [`PythonFunctionTask`](../flytekit.core.python_function_task/pythonfunctiontask) | A Python Function task should be used as the base for all extensions that have a python function. |
| [`PythonInstanceTask`](../flytekit.core.python_function_task/pythoninstancetask) | This class should be used as the base class for all Tasks that do not have a user defined function body, but have. |

### Variables

| Property | Type | Description |
|-|-|-|
| `CLEANUP_LOOP_DELAY_SECONDS` | `int` |  |
| `EAGER_ROOT_ENV_NAME` | `str` |  |
| `T` | `TypeVar` |  |
| `eager_failure_task_resolver` | `EagerFailureTaskResolver` |  |

