---
title: flytekit.clis.sdk_in_container.run
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.run

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicEntityLaunchCommand`](../flytekit.clis.sdk_in_container.run/dynamicentitylaunchcommand) | This is a dynamic command that is created for each launch plan. |
| [`Entities`](../flytekit.clis.sdk_in_container.run/entities) | NamedTuple to group all entities in a file. |
| [`RemoteEntityGroup`](../flytekit.clis.sdk_in_container.run/remoteentitygroup) | click multicommand that retrieves launchplans from a remote flyte instance and executes them. |
| [`RunCommand`](../flytekit.clis.sdk_in_container.run/runcommand) | A click command group for registering and executing flyte workflows & tasks in a file. |
| [`RunLevelComputedParams`](../flytekit.clis.sdk_in_container.run/runlevelcomputedparams) | This class is used to store the computed parameters that are used to run a workflow / task / launchplan. |
| [`RunLevelParams`](../flytekit.clis.sdk_in_container.run/runlevelparams) | This class is used to store the parameters that are used to run a workflow / task / launchplan. |
| [`WorkflowCommand`](../flytekit.clis.sdk_in_container.run/workflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`YamlFileReadingCommand`](../flytekit.clis.sdk_in_container.run/yamlfilereadingcommand) | Richly formatted click Command. |

### Methods

| Method | Description |
|-|-|
| [`dump_flyte_remote_snippet()`](#dump_flyte_remote_snippet) |  |
| [`get_entities_in_file()`](#get_entities_in_file) | Returns a list of flyte workflow names and list of Flyte tasks in a file. |
| [`is_optional()`](#is_optional) | Checks if the given type is Optional Type. |
| [`load_naive_entity()`](#load_naive_entity) | Load the workflow of a script file. |
| [`options_from_run_params()`](#options_from_run_params) |  |
| [`run_command()`](#run_command) | Returns a function that is used to implement WorkflowCommand and execute a flyte workflow. |
| [`run_remote()`](#run_remote) | Helper method that executes the given remote FlyteLaunchplan, FlyteWorkflow or FlyteTask. |
| [`to_click_option()`](#to_click_option) | This handles converting workflow input types to supported click parameters with callbacks to initialize. |


## Methods

#### dump_flyte_remote_snippet()

```python
def dump_flyte_remote_snippet(
    execution: flytekit.remote.executions.FlyteWorkflowExecution,
    project: str,
    domain: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `execution` | `flytekit.remote.executions.FlyteWorkflowExecution` | |
| `project` | `str` | |
| `domain` | `str` | |

#### get_entities_in_file()

```python
def get_entities_in_file(
    filename: pathlib.Path,
    should_delete: bool,
) -> flytekit.clis.sdk_in_container.run.Entities
```
Returns a list of flyte workflow names and list of Flyte tasks in a file.


| Parameter | Type | Description |
|-|-|-|
| `filename` | `pathlib.Path` | |
| `should_delete` | `bool` | |

#### is_optional()

```python
def is_optional(
    _type,
)
```
Checks if the given type is Optional Type


| Parameter | Type | Description |
|-|-|-|
| `_type` |  | |

#### load_naive_entity()

```python
def load_naive_entity(
    module_name: str,
    entity_name: str,
    project_root: str,
) -> typing.Union[flytekit.core.workflow.WorkflowBase, flytekit.core.base_task.PythonTask]
```
Load the workflow of a script file.
N.B.: it assumes that the file is self-contained, in other words, there are no relative imports.


| Parameter | Type | Description |
|-|-|-|
| `module_name` | `str` | |
| `entity_name` | `str` | |
| `project_root` | `str` | |

#### options_from_run_params()

```python
def options_from_run_params(
    run_level_params: flytekit.clis.sdk_in_container.run.RunLevelParams,
) -> flytekit.core.options.Options
```
| Parameter | Type | Description |
|-|-|-|
| `run_level_params` | `flytekit.clis.sdk_in_container.run.RunLevelParams` | |

#### run_command()

```python
def run_command(
    ctx: click.core.Context,
    entity: typing.Union[flytekit.core.workflow.PythonFunctionWorkflow, flytekit.core.base_task.PythonTask, flytekit.core.launch_plan.LaunchPlan],
)
```
Returns a function that is used to implement WorkflowCommand and execute a flyte workflow.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `entity` | `typing.Union[flytekit.core.workflow.PythonFunctionWorkflow, flytekit.core.base_task.PythonTask, flytekit.core.launch_plan.LaunchPlan]` | |

#### run_remote()

```python
def run_remote(
    remote: flytekit.remote.remote.FlyteRemote,
    entity: typing.Union[flytekit.remote.entities.FlyteWorkflow, flytekit.remote.entities.FlyteTask, flytekit.remote.entities.FlyteLaunchPlan],
    project: str,
    domain: str,
    inputs: typing.Dict[str, typing.Any],
    run_level_params: flytekit.clis.sdk_in_container.run.RunLevelParams,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
)
```
Helper method that executes the given remote FlyteLaunchplan, FlyteWorkflow or FlyteTask


| Parameter | Type | Description |
|-|-|-|
| `remote` | `flytekit.remote.remote.FlyteRemote` | |
| `entity` | `typing.Union[flytekit.remote.entities.FlyteWorkflow, flytekit.remote.entities.FlyteTask, flytekit.remote.entities.FlyteLaunchPlan]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `inputs` | `typing.Dict[str, typing.Any]` | |
| `run_level_params` | `flytekit.clis.sdk_in_container.run.RunLevelParams` | |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` | |

#### to_click_option()

```python
def to_click_option(
    ctx: click.core.Context,
    flyte_ctx: flytekit.core.context_manager.FlyteContext,
    input_name: str,
    literal_var: flytekit.models.interface.Variable,
    python_type: typing.Type,
    default_val: typing.Any,
    required: bool,
) -> click.core.Option
```
This handles converting workflow input types to supported click parameters with callbacks to initialize
the input values to their expected types.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `flyte_ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `input_name` | `str` | |
| `literal_var` | `flytekit.models.interface.Variable` | |
| `python_type` | `typing.Type` | |
| `default_val` | `typing.Any` | |
| `required` | `bool` | |

