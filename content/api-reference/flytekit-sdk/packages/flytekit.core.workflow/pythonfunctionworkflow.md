---
title: PythonFunctionWorkflow
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PythonFunctionWorkflow

**Package:** `flytekit.core.workflow`

Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte.
This Python object represents a workflow  defined by a function and decorated with the
{{&lt; py_func_ref `@workflow &lt;flytekit.workflow&gt;` &gt;}} decorator. Please see notes on that object for additional information.



```python
class PythonFunctionWorkflow(
    workflow_function: Callable,
    metadata: WorkflowMetadata,
    default_metadata: WorkflowMetadataDefaults,
    docstring: Optional[Docstring],
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
)
```
| Parameter | Type | Description |
|-|-|-|
| `workflow_function` | `Callable` | |
| `metadata` | `WorkflowMetadata` | |
| `default_metadata` | `WorkflowMetadataDefaults` | |
| `docstring` | `Optional[Docstring]` | |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` | |
| `docs` | `Optional[Documentation]` | |
| `pickle_untyped` | `bool` | |
| `default_options` | `Optional[Options]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `default_options` | `None` |  |
| `docs` | `None` |  |
| `failure_node` | `None` |  |
| `function` | `None` |  |
| `instantiated_in` | `None` |  |
| `interface` | `None` |  |
| `lhs` | `None` |  |
| `location` | `None` |  |
| `name` | `None` |  |
| `nodes` | `None` |  |
| `on_failure` | `None` |  |
| `output_bindings` | `None` |  |
| `python_interface` | `None` |  |
| `short_name` | `None` |  |
| `workflow_metadata` | `None` |  |
| `workflow_metadata_defaults` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`compile()`](#compile) | Supply static Python native values in the kwargs if you want them to be used in the compilation. |
| [`construct_node_metadata()`](#construct_node_metadata) |  |
| [`execute()`](#execute) | This function is here only to try to streamline the pattern between workflows and tasks. |
| [`find_lhs()`](#find_lhs) |  |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method. |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found. |
| [`loader_args()`](#loader_args) | This is responsible for turning an instance of a task into args that the load_task function can reconstitute. |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task. |


### add()

```python
def add(
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` | |

### compile()

```python
def compile(
    kwargs,
)
```
Supply static Python native values in the kwargs if you want them to be used in the compilation. This mimics
a 'closure' in the traditional sense of the word.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
### execute()

```python
def execute(
    kwargs,
)
```
This function is here only to try to streamline the pattern between workflows and tasks. Since tasks
call execute from dispatch_execute which is in local_execute, workflows should also call an execute inside
local_execute. This makes mocking cleaner.


| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### find_lhs()

```python
def find_lhs()
```
### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


### load_task()

```python
def load_task(
    loader_args: typing.List[str],
) -> flytekit.core.python_auto_container.PythonAutoContainerTask
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type | Description |
|-|-|-|
| `loader_args` | `typing.List[str]` | |

### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.python_auto_container.PythonAutoContainerTask,
) -> typing.List[str]
```
This is responsible for turning an instance of a task into args that the load_task function can reconstitute.


| Parameter | Type | Description |
|-|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` | |
| `t` | `flytekit.core.python_auto_container.PythonAutoContainerTask` | |

### local_execute()

```python
def local_execute(
    ctx: FlyteContext,
    kwargs,
) -> Union[Tuple[Promise], Promise, VoidPromise, None]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
### task_name()

```python
def task_name(
    t: PythonAutoContainerTask,
) -> str
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type | Description |
|-|-|-|
| `t` | `PythonAutoContainerTask` | |

