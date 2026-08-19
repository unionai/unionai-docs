---
title: flytekit.clis.sdk_in_container.build
version: 1.16.28
variants: +flyte +union
layout: py_api
---

# flytekit.clis.sdk_in_container.build

## Directory

### Classes

| Class | Description |
|-|-|
| [`BuildCommand`](.././flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildcommand) | A click command group for building a image for flyte workflows & tasks in a file. |
| [`BuildParams`](.././flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildparams) |  |
| [`BuildWorkflowCommand`](.././flytekit.clis.sdk_in_container.build#flytekitclissdk_in_containerbuildbuildworkflowcommand) | click multicommand at the python file layer, subcommands should be all the workflows in the file. |

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

## flytekit.clis.sdk_in_container.build.BuildCommand

A click command group for building a image for flyte workflows & tasks in a file.


### Parameters

```python
class BuildCommand(
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
    *args,
    **kwargs,
)
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` |  | |
| `*args` |  | |
| `**kwargs` |  | |

## flytekit.clis.sdk_in_container.build.BuildParams

### Parameters

```python
class BuildParams(
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
    fast: bool = False,
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
| `fast` | `bool` | |

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
## flytekit.clis.sdk_in_container.build.BuildWorkflowCommand

click multicommand at the python file layer, subcommands should be all the workflows in the file.


### Parameters

```python
class BuildWorkflowCommand(
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

