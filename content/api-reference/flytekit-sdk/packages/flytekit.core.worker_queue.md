---
title: flytekit.core.worker_queue
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.worker_queue

## Directory

### Classes

| Class | Description |
|-|-|
| [`Controller`](.././flytekit.core.worker_queue#flytekitcoreworker_queuecontroller) | This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint. |
| [`Update`](.././flytekit.core.worker_queue#flytekitcoreworker_queueupdate) |  |
| [`WorkItem`](.././flytekit.core.worker_queue#flytekitcoreworker_queueworkitem) | This is a class to keep track of what the user requested. |

### Variables

| Property | Type | Description |
|-|-|-|
| `EAGER_ROOT_ENV_NAME` | `str` |  |
| `EAGER_TAG_KEY` | `str` |  |
| `EAGER_TAG_ROOT_KEY` | `str` |  |
| `NODE_HTML_TEMPLATE` | `str` |  |
| `handling_signal` | `int` |  |

## flytekit.core.worker_queue.Controller

This controller object is responsible for kicking off and monitoring executions against a Flyte Admin endpoint
using a FlyteRemote object. It is used only for running eager tasks. It exposes one async method, `add`, which
should be called by the eager task to run a sub-flyte-entity (task, workflow, or a nested eager task).

The controller maintains a dictionary of entries, where each entry is a list of WorkItems. They are maintained
in a list because the number of times and order that each task (or subwf, lp) is called affects the execution name
which is consistently hashed.

After calling `add`, a background thread is started to reconcile the state of this dictionary of WorkItem entries.
Executions that should be kicked off will be kicked off, and ones that are running will be checked. This runs
in a loop similar to a controller loop in a k8s operator.


```python
class Controller(
    remote: FlyteRemote,
    ss: SerializationSettings,
    tag: str,
    root_tag: str,
    exec_prefix: str,
)
```
| Parameter | Type |
|-|-|
| `remote` | `FlyteRemote` |
| `ss` | `SerializationSettings` |
| `tag` | `str` |
| `root_tag` | `str` |
| `exec_prefix` | `str` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) | Add an entity along with the requested inputs to be submitted to Admin for running and return a future. |
| [`for_sandbox()`](#for_sandbox) |  |
| [`get_env()`](#get_env) | In order for downstream tasks to correctly set the root label, this needs to pass down that information. |
| [`get_execution_name()`](#get_execution_name) | Make a deterministic name. |
| [`get_labels()`](#get_labels) | These labels keep track of the current and root (in case of nested) eager execution, that is responsible for. |
| [`get_signal_handler()`](#get_signal_handler) | TODO: At some point, this loop would be ideally managed by the loop manager, and the signal handler should. |
| [`launch_execution()`](#launch_execution) | This function launches executions. |
| [`reconcile_one()`](#reconcile_one) | This is responsible for processing one work item. |
| [`render_html()`](#render_html) | Render the callstack as a deck presentation to be shown after eager workflow execution. |


#### add()

```python
def add(
    entity: RunnableEntity,
    input_kwargs: dict[str, typing.Any],
) -> typing.Any
```
Add an entity along with the requested inputs to be submitted to Admin for running and return a future


| Parameter | Type |
|-|-|
| `entity` | `RunnableEntity` |
| `input_kwargs` | `dict[str, typing.Any]` |

#### for_sandbox()

```python
def for_sandbox(
    exec_prefix: typing.Optional[str],
) -> Controller
```
| Parameter | Type |
|-|-|
| `exec_prefix` | `typing.Optional[str]` |

#### get_env()

```python
def get_env()
```
In order for downstream tasks to correctly set the root label, this needs to pass down that information.


#### get_execution_name()

```python
def get_execution_name(
    entity: RunnableEntity,
    idx: int,
    input_kwargs: dict[str, typing.Any],
) -> str
```
Make a deterministic name


| Parameter | Type |
|-|-|
| `entity` | `RunnableEntity` |
| `idx` | `int` |
| `input_kwargs` | `dict[str, typing.Any]` |

#### get_labels()

```python
def get_labels()
```
These labels keep track of the current and root (in case of nested) eager execution, that is responsible for
kicking off this execution.


#### get_signal_handler()

```python
def get_signal_handler()
```
TODO: At some point, this loop would be ideally managed by the loop manager, and the signal handler should
  gracefully initiate shutdown of all loops, calling .cancel() on all tasks, allowing each loop to clean up,
  starting with the deepest loop/thread first and working up.
  https://github.com/flyteorg/flyte/issues/6068


#### launch_execution()

```python
def launch_execution(
    wi: WorkItem,
    idx: int,
) -> FlyteWorkflowExecution
```
This function launches executions.


| Parameter | Type |
|-|-|
| `wi` | `WorkItem` |
| `idx` | `int` |

#### reconcile_one()

```python
def reconcile_one(
    update: Update,
)
```
This is responsible for processing one work item. Will launch, update, set error on the update object
Any errors are captured in the update object.


| Parameter | Type |
|-|-|
| `update` | `Update` |

#### render_html()

```python
def render_html()
```
Render the callstack as a deck presentation to be shown after eager workflow execution.


## flytekit.core.worker_queue.Update

```python
class Update(
    work_item: WorkItem,
    idx: int,
    status: typing.Optional[ItemStatus],
    wf_exec: typing.Optional[FlyteWorkflowExecution],
    error: typing.Optional[BaseException],
)
```
| Parameter | Type |
|-|-|
| `work_item` | `WorkItem` |
| `idx` | `int` |
| `status` | `typing.Optional[ItemStatus]` |
| `wf_exec` | `typing.Optional[FlyteWorkflowExecution]` |
| `error` | `typing.Optional[BaseException]` |

## flytekit.core.worker_queue.WorkItem

This is a class to keep track of what the user requested. Since it captures the arguments that the user wants
to run the entity with, an arbitrary map, can't make this frozen.


```python
class WorkItem(
    entity: RunnableEntity,
    input_kwargs: dict[str, typing.Any],
    result: typing.Any,
    error: typing.Optional[BaseException],
    status: ItemStatus,
    wf_exec: typing.Optional[FlyteWorkflowExecution],
    python_interface: typing.Optional[Interface],
    uuid: typing.Optional[uuid.UUID],
)
```
| Parameter | Type |
|-|-|
| `entity` | `RunnableEntity` |
| `input_kwargs` | `dict[str, typing.Any]` |
| `result` | `typing.Any` |
| `error` | `typing.Optional[BaseException]` |
| `status` | `ItemStatus` |
| `wf_exec` | `typing.Optional[FlyteWorkflowExecution]` |
| `python_interface` | `typing.Optional[Interface]` |
| `uuid` | `typing.Optional[uuid.UUID]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_in_terminal_state` |  |  |

