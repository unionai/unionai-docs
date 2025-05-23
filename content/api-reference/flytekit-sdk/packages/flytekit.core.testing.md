---
title: flytekit.core.testing
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.testing

## Directory

### Methods

| Method | Description |
|-|-|
| [`patch()`](#patch) | This is a decorator used for testing. |
| [`task_mock()`](#task_mock) | Use this method to mock a task declaration. |


## Methods

#### patch()

```python
def patch(
    target: typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.workflow.WorkflowBase, flytekit.core.reference_entity.ReferenceEntity],
)
```
This is a decorator used for testing.


| Parameter | Type |
|-|-|
| `target` | `typing.Union[flytekit.core.base_task.PythonTask, flytekit.core.workflow.WorkflowBase, flytekit.core.reference_entity.ReferenceEntity]` |

#### task_mock()

```python
def task_mock(
    t: flytekit.core.base_task.PythonTask,
) -> typing.Generator[unittest.mock.MagicMock, NoneType, NoneType]
```
Use this method to mock a task declaration. It can mock any Task in Flytekit as long as it has a python native
interface associated with it.

The returned object is a MagicMock and allows to perform all such methods. This MagicMock, mocks the execute method
on the PythonTask

Usage:

    ```python
    @task
    def t1(i: int) -> int:
        pass

    with task_mock(t1) as m:
        m.side_effect = lambda x: x
        t1(10)
        # The mock is valid only within this context
    ```


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.PythonTask` |

