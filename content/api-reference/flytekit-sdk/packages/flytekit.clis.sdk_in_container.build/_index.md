---
title: flytekit.clis.sdk_in_container.build
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.build

## Directory

### Classes

| Class | Description |
|-|-|
| [`BuildCommand`](../flytekit.clis.sdk_in_container.build/buildcommand) | A click command group for building a image for flyte workflows & tasks in a file. |
| [`BuildParams`](../flytekit.clis.sdk_in_container.build/buildparams) |  |
| [`BuildWorkflowCommand`](../flytekit.clis.sdk_in_container.build/buildworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |

### Methods

| Method | Description |
|-|-|
| [`build_command()`](#build_command) | Returns a function that is used to implement WorkflowCommand and build an image for flyte workflows. |


## Methods

#### build_command()

```python
def build_command(
    ctx: click.core.Context,
    entity: typing.Union[flytekit.core.workflow.PythonFunctionWorkflow, flytekit.core.base_task.PythonTask],
)
```
Returns a function that is used to implement WorkflowCommand and build an image for flyte workflows.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `entity` | `typing.Union[flytekit.core.workflow.PythonFunctionWorkflow, flytekit.core.base_task.PythonTask]` | |

