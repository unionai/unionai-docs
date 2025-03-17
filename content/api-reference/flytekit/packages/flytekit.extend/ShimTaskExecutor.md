---
title: ShimTaskExecutor
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ShimTaskExecutor

**Package:** `flytekit.extend`

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
def ShimTaskExecutor(
    args,
    kwargs,
):
```
Initialize self.  See help(type(self)) for accurate signature.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |
## Methods

### execute_from_model()

```python
def execute_from_model(
    tt: _task_model.TaskTemplate,
    kwargs,
):
```
This function must be overridden and is where all the business logic for running a task should live. Keep in
mind that you're only working with the ``TaskTemplate``. You won't have access to any information in the task
that wasn't serialized into the template.



| Parameter | Type |
|-|-|
| `tt` | `_task_model.TaskTemplate` |
| `kwargs` | ``**kwargs`` |
### find_lhs()

```python
def find_lhs()
```
No parameters
