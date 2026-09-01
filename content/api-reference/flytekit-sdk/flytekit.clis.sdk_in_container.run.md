---
title: flytekit.clis.sdk_in_container.run
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.clis.sdk_in_container.run

## Directory

### Classes

| Class | Description |
|-|-|
| [`DynamicEntityLaunchCommand`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrundynamicentitylaunchcommand) | This is a dynamic command that is created for each launch plan. |
| [`Entities`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunentities) | NamedTuple to group all entities in a file. |
| [`RemoteEntityGroup`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunremoteentitygroup) | click multicommand that retrieves launchplans from a remote flyte instance and executes them. |
| [`RunCommand`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunruncommand) | A click command group for registering and executing flyte workflows & tasks in a file. |
| [`RunLevelComputedParams`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelcomputedparams) | This class is used to store the computed parameters that are used to run a workflow / task / launchplan. |
| [`RunLevelParams`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunrunlevelparams) | This class is used to store the parameters that are used to run a workflow / task / launchplan. |
| [`WorkflowCommand`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |
| [`YamlFileReadingCommand`](./flytekit.clis.sdk_in_container.run#flytekitclissdk_in_containerrunyamlfilereadingcommand) |  |

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
    type_hints: typing.Optional[typing.Dict[str, typing.Type]] = None,
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

## flytekit.clis.sdk_in_container.run.DynamicEntityLaunchCommand

This is a dynamic command that is created for each launch plan. This is used to execute a launch plan.
It will fetch the launch plan from remote and create parameters from all the inputs of the launch plan.


### Parameters

```python
class DynamicEntityLaunchCommand(
    name: str,
    h: str,
    entity_name: str,
    launcher: str,
    **kwargs,
)
```
Create Rich Command instance.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `h` | `str` | |
| `entity_name` | `str` | |
| `launcher` | `str` | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`get_params()`](#get_params) |  |
| [`invoke()`](#invoke) | Default or None values should be ignored. |


#### get_params()

```python
def get_params(
    ctx: click.core.Context,
) -> typing.List[ForwardRef('click.Parameter')]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
) -> typing.Any
```
Default or None values should be ignored. Only values that are provided by the user should be passed to the
remote execution.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

## flytekit.clis.sdk_in_container.run.Entities

NamedTuple to group all entities in a file


### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`matching_lp()`](#matching_lp) | Returns the variable name of the launch plan in the file. |


#### all()

```python
def all()
```
#### matching_lp()

```python
def matching_lp(
    lp_name: str,
) -> typing.Optional[str]
```
Returns the variable name of the launch plan in the file


| Parameter | Type | Description |
|-|-|-|
| `lp_name` | `str` | |

## flytekit.clis.sdk_in_container.run.RemoteEntityGroup

click multicommand that retrieves launchplans from a remote flyte instance and executes them.


### Parameters

```python
class RemoteEntityGroup(
    command_name: str,
)
```
Create RichGroup instance.


| Parameter | Type | Description |
|-|-|-|
| `command_name` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`get_command()`](#get_command) | Given a context and a command name, this returns a. |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should. |


#### get_command()

```python
def get_command(
    ctx,
    name,
)
```
Given a context and a command name, this returns a
`Command` object if it exists or returns `None`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `name` |  | |

#### list_commands()

```python
def list_commands(
    ctx,
)
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |

## flytekit.clis.sdk_in_container.run.RunCommand

A click command group for registering and executing flyte workflows & tasks in a file.


### Parameters

```python
class RunCommand(
    *args,
    **kwargs,
)
```
Create RichGroup instance.


| Parameter | Type | Description |
|-|-|-|
| `*args` |  | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`get_command()`](#get_command) | Given a context and a command name, this returns a. |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should. |


#### get_command()

```python
def get_command(
    ctx,
    filename,
)
```
Given a context and a command name, this returns a
`Command` object if it exists or returns `None`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `filename` |  | |

#### list_commands()

```python
def list_commands(
    ctx,
    add_remote: bool = True,
)
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `add_remote` | `bool` | |

## flytekit.clis.sdk_in_container.run.RunLevelComputedParams

This class is used to store the computed parameters that are used to run a workflow / task / launchplan.
Computed parameters are created during the execution


### Parameters

```python
class RunLevelComputedParams(
    project_root: typing.Optional[str] = None,
    module: typing.Optional[str] = None,
    temp_file_name: typing.Optional[str] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project_root` | `typing.Optional[str]` | |
| `module` | `typing.Optional[str]` | |
| `temp_file_name` | `typing.Optional[str]` | |

## flytekit.clis.sdk_in_container.run.RunLevelParams

This class is used to store the parameters that are used to run a workflow / task / launchplan.


### Parameters

```python
class RunLevelParams(
    config_file: typing.Optional[str] = None,
    verbose: bool = False,
    pkgs: typing.List[str] = <factory>,
    project: str = 'flytesnacks',
    domain: str = 'development',
    destination_dir: str = '.',
    copy_all: bool = False,
    copy: typing.Optional[flytekit.constants.CopyFileDetection] = 'auto',
    image_config: flytekit.configuration.ImageConfig = <factory>,
    service_account: str = '',
    wait_execution: bool = False,
    poll_interval: int = None,
    dump_snippet: bool = False,
    overwrite_cache: bool = False,
    interruptible: typing.Optional[bool] = None,
    envvars: typing.Dict[str, str] = <factory>,
    resource_requests: typing.Optional[flytekit.core.resources.Resources] = None,
    resource_limits: typing.Optional[flytekit.core.resources.Resources] = None,
    tags: typing.List[str] = <factory>,
    name: str = None,
    labels: typing.Dict[str, str] = <factory>,
    annotations: typing.Dict[str, str] = <factory>,
    raw_output_data_prefix: str = None,
    max_parallelism: int = None,
    disable_notifications: bool = False,
    remote: bool = False,
    limit: int = 50,
    cluster_pool: str = '',
    execution_cluster_label: str = '',
    computed_params: flytekit.clis.sdk_in_container.run.RunLevelComputedParams = <factory>,
    _remote: typing.Optional[flytekit.remote.remote.FlyteRemote] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[str]` | |
| `verbose` | `bool` | |
| `pkgs` | `typing.List[str]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `destination_dir` | `str` | |
| `copy_all` | `bool` | |
| `copy` | `typing.Optional[flytekit.constants.CopyFileDetection]` | |
| `image_config` | `flytekit.configuration.ImageConfig` | |
| `service_account` | `str` | |
| `wait_execution` | `bool` | |
| `poll_interval` | `int` | |
| `dump_snippet` | `bool` | |
| `overwrite_cache` | `bool` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envvars` | `typing.Dict[str, str]` | |
| `resource_requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `resource_limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `tags` | `typing.List[str]` | |
| `name` | `str` | |
| `labels` | `typing.Dict[str, str]` | |
| `annotations` | `typing.Dict[str, str]` | |
| `raw_output_data_prefix` | `str` | |
| `max_parallelism` | `int` | |
| `disable_notifications` | `bool` | |
| `remote` | `bool` | |
| `limit` | `int` | |
| `cluster_pool` | `str` | |
| `execution_cluster_label` | `str` | |
| `computed_params` | `flytekit.clis.sdk_in_container.run.RunLevelComputedParams` | |
| `_remote` | `typing.Optional[flytekit.remote.remote.FlyteRemote]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_remote` | `bool` |  |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`options()`](#options) | Return the set of base parameters added to every pyflyte run workflow subcommand. |
| [`remote_instance()`](#remote_instance) |  |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> RunLevelParams
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |

#### options()

```python
def options()
```
Return the set of base parameters added to every pyflyte run workflow subcommand.


#### remote_instance()

```python
def remote_instance()
```
## flytekit.clis.sdk_in_container.run.WorkflowCommand

click multicommand at the python file layer, subcommands should be all the workflows in the file.


### Parameters

```python
class WorkflowCommand(
    filename: str,
    *args,
    **kwargs,
)
```
Create RichGroup instance.


| Parameter | Type | Description |
|-|-|-|
| `filename` | `str` | |
| `*args` |  | |
| `**kwargs` |  | |

### Methods

| Method | Description |
|-|-|
| [`get_command()`](#get_command) | This command uses the filename with which this command was created, and the string name of the entity passed. |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should. |


#### get_command()

```python
def get_command(
    ctx,
    exe_entity,
)
```
This command uses the filename with which this command was created, and the string name of the entity passed
  after the Python filename on the command line, to load the Python object, and then return the Command that
  click should run.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | The click Context object. |
| `exe_entity` |  | string of the flyte entity provided by the user. Should be the name of a workflow, or task function. |

#### list_commands()

```python
def list_commands(
    ctx,
)
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |

## flytekit.clis.sdk_in_container.run.YamlFileReadingCommand

### Parameters

```python
class YamlFileReadingCommand(
    name: str,
    params: typing.List[click.core.Option],
    help: str,
    callback: typing.Callable = None,
)
```
Create Rich Command instance.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `params` | `typing.List[click.core.Option]` | |
| `help` | `str` | |
| `callback` | `typing.Callable` | |

### Methods

| Method | Description |
|-|-|
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser. |


#### parse_args()

```python
def parse_args(
    ctx: click.core.Context,
    args: typing.List[str],
) -> typing.List[str]
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by `make_context`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `args` | `typing.List[str]` | |

