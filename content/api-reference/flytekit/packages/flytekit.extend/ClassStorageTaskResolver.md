---
title: ClassStorageTaskResolver
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ClassStorageTaskResolver

**Package:** `flytekit.extend`

Stores tasks inside a class variable. The class must be inherited from at the point of usage because the task
loading process basically relies on the same sequence of things happening.


```python
def ClassStorageTaskResolver(
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

### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
):
```
| Parameter | Type |
|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |
### find_lhs()

```python
def find_lhs()
```
No parameters
### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


No parameters
### load_task()

```python
def load_task(
    loader_args: typing.List[str],
):
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |
### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
):
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` |
### name()

```python
def name()
```
No parameters
### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
):
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |
