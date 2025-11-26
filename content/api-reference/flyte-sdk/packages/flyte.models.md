---
title: flyte.models
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`ActionID`](.././flyte.models#flytemodelsactionid) | A class representing the ID of an Action, nested within a Run. |
| [`Checkpoints`](.././flyte.models#flytemodelscheckpoints) | A class representing the checkpoints for a task. |
| [`CodeBundle`](.././flyte.models#flytemodelscodebundle) | A class representing a code bundle for a task. |
| [`GroupData`](.././flyte.models#flytemodelsgroupdata) |  |
| [`NativeInterface`](.././flyte.models#flytemodelsnativeinterface) | A class representing the native interface for a task. |
| [`PathRewrite`](.././flyte.models#flytemodelspathrewrite) | Configuration for rewriting paths during input loading. |
| [`RawDataPath`](.././flyte.models#flytemodelsrawdatapath) | A class representing the raw data path for a task. |
| [`SerializationContext`](.././flyte.models#flytemodelsserializationcontext) | This object holds serialization time contextual information, that can be used when serializing the task and. |
| [`TaskContext`](.././flyte.models#flytemodelstaskcontext) | A context class to hold the current task executions context. |

### Methods

| Method | Description |
|-|-|
| [`generate_random_name()`](#generate_random_name) | Generate a random name for the task. |


### Variables

| Property | Type | Description |
|-|-|-|
| `MAX_INLINE_IO_BYTES` | `int` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### generate_random_name()

```python
def generate_random_name()
```
Generate a random name for the task. This is used to create unique names for tasks.
TODO we can use unique-namer in the future, for now its just guids


## flyte.models.ActionID

A class representing the ID of an Action, nested within a Run. This is used to identify a specific action on a task.


```python
class ActionID(
    name: str,
    run_name: str | None,
    project: str | None,
    domain: str | None,
    org: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `run_name` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `org` | `str \| None` | |

### Methods

| Method | Description |
|-|-|
| [`create_random()`](#create_random) |  |
| [`new_sub_action()`](#new_sub_action) | Create a new sub-run with the given name. |
| [`new_sub_action_from()`](#new_sub_action_from) | Make a deterministic name. |


#### create_random()

```python
def create_random()
```
#### new_sub_action()

```python
def new_sub_action(
    name: str | None,
) -> ActionID
```
Create a new sub-run with the given name. If  name is None, a random name will be generated.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str \| None` | |

#### new_sub_action_from()

```python
def new_sub_action_from(
    task_call_seq: int,
    task_hash: str,
    input_hash: str,
    group: str | None,
) -> ActionID
```
Make a deterministic name


| Parameter | Type | Description |
|-|-|-|
| `task_call_seq` | `int` | |
| `task_hash` | `str` | |
| `input_hash` | `str` | |
| `group` | `str \| None` | |

## flyte.models.Checkpoints

A class representing the checkpoints for a task. This is used to store the checkpoints for the task execution.


```python
class Checkpoints(
    prev_checkpoint_path: str | None,
    checkpoint_path: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `prev_checkpoint_path` | `str \| None` | |
| `checkpoint_path` | `str \| None` | |

## flyte.models.CodeBundle

A class representing a code bundle for a task. This is used to package the code and the inflation path.
The code bundle computes the version of the code using the hash of the code.



```python
class CodeBundle(
    computed_version: str,
    destination: str,
    tgz: str | None,
    pkl: str | None,
    downloaded_path: pathlib.Path | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `computed_version` | `str` | The version of the code bundle. This is the hash of the code. |
| `destination` | `str` | The destination path for the code bundle to be inflated to. |
| `tgz` | `str \| None` | Optional path to the tgz file. |
| `pkl` | `str \| None` | Optional path to the pkl file. |
| `downloaded_path` | `pathlib.Path \| None` | The path to the downloaded code bundle. This is only available during runtime, when the code bundle has been downloaded and inflated. |

### Methods

| Method | Description |
|-|-|
| [`with_downloaded_path()`](#with_downloaded_path) | Create a new CodeBundle with the given downloaded path. |


#### with_downloaded_path()

```python
def with_downloaded_path(
    path: pathlib.Path,
) -> CodeBundle
```
Create a new CodeBundle with the given downloaded path.


| Parameter | Type | Description |
|-|-|-|
| `path` | `pathlib.Path` | |

## flyte.models.GroupData

```python
class GroupData(
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |

## flyte.models.NativeInterface

A class representing the native interface for a task. This is used to interact with the task and its execution
context.


```python
class NativeInterface(
    inputs: Dict[str, Tuple[Type, Any]],
    outputs: Dict[str, Type],
    docstring: Optional[Docstring],
    _remote_defaults: Optional[Dict[str, literals_pb2.Literal]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Dict[str, Tuple[Type, Any]]` | |
| `outputs` | `Dict[str, Type]` | |
| `docstring` | `Optional[Docstring]` | |
| `_remote_defaults` | `Optional[Dict[str, literals_pb2.Literal]]` | |

### Methods

| Method | Description |
|-|-|
| [`convert_to_kwargs()`](#convert_to_kwargs) | Convert the given arguments to keyword arguments based on the native interface. |
| [`from_callable()`](#from_callable) | Extract the native interface from the given function. |
| [`from_types()`](#from_types) | Create a new NativeInterface from the given types. |
| [`get_input_types()`](#get_input_types) | Get the input types for the task. |
| [`has_outputs()`](#has_outputs) | Check if the task has outputs. |
| [`num_required_inputs()`](#num_required_inputs) | Get the number of required inputs for the task. |
| [`required_inputs()`](#required_inputs) | Get the names of the required inputs for the task. |


#### convert_to_kwargs()

```python
def convert_to_kwargs(
    args,
    kwargs,
) -> Dict[str, Any]
```
Convert the given arguments to keyword arguments based on the native interface. This is used to convert the
arguments to the correct types for the task execution.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

#### from_callable()

```python
def from_callable(
    func: Callable,
) -> NativeInterface
```
Extract the native interface from the given function. This is used to create a native interface for the task.


| Parameter | Type | Description |
|-|-|-|
| `func` | `Callable` | |

#### from_types()

```python
def from_types(
    inputs: Dict[str, Tuple[Type, Type[_has_default] | Type[inspect._empty]]],
    outputs: Dict[str, Type],
    default_inputs: Optional[Dict[str, literals_pb2.Literal]],
) -> NativeInterface
```
Create a new NativeInterface from the given types. This is used to create a native interface for the task.


| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Dict[str, Tuple[Type, Type[_has_default] \| Type[inspect._empty]]]` | A dictionary of input names and their types and a value indicating if they have a default value. |
| `outputs` | `Dict[str, Type]` | A dictionary of output names and their types. |
| `default_inputs` | `Optional[Dict[str, literals_pb2.Literal]]` | Optional dictionary of default inputs for remote tasks. :return: A NativeInterface object with the given inputs and outputs. |

#### get_input_types()

```python
def get_input_types()
```
Get the input types for the task. This is used to get the types of the inputs for the task execution.


#### has_outputs()

```python
def has_outputs()
```
Check if the task has outputs. This is used to determine if the task has outputs or not.


#### num_required_inputs()

```python
def num_required_inputs()
```
Get the number of required inputs for the task. This is used to determine how many inputs are required for the
task execution.


#### required_inputs()

```python
def required_inputs()
```
Get the names of the required inputs for the task. This is used to determine which inputs are required for the
task execution.
:return: A list of required input names.


## flyte.models.PathRewrite

Configuration for rewriting paths during input loading.


```python
class PathRewrite(
    old_prefix: str,
    new_prefix: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `old_prefix` | `str` | |
| `new_prefix` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`from_str()`](#from_str) | Create a PathRewrite from a string pattern of the form `old_prefix->new_prefix`. |


#### from_str()

```python
def from_str(
    pattern: str,
) -> PathRewrite
```
Create a PathRewrite from a string pattern of the form `old_prefix-&gt;new_prefix`.


| Parameter | Type | Description |
|-|-|-|
| `pattern` | `str` | |

## flyte.models.RawDataPath

A class representing the raw data path for a task. This is used to store the raw data for the task execution and
also get mutations on the path.


```python
class RawDataPath(
    path: str,
    path_rewrite: Optional[PathRewrite],
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `path_rewrite` | `Optional[PathRewrite]` | |

### Methods

| Method | Description |
|-|-|
| [`from_local_folder()`](#from_local_folder) | Create a new context attribute object, with local path given. |
| [`get_random_remote_path()`](#get_random_remote_path) | Returns a random path for uploading a file/directory to. |


#### from_local_folder()

```python
def from_local_folder(
    local_folder: str | pathlib.Path | None,
) -> RawDataPath
```
Create a new context attribute object, with local path given. Will be created if it doesn't exist.
:return: Path to the temporary directory


| Parameter | Type | Description |
|-|-|-|
| `local_folder` | `str \| pathlib.Path \| None` | |

#### get_random_remote_path()

```python
def get_random_remote_path(
    file_name: Optional[str],
) -> str
```
Returns a random path for uploading a file/directory to. This file/folder will not be created, it's just a path.



| Parameter | Type | Description |
|-|-|-|
| `file_name` | `Optional[str]` | If given, will be joined after a randomly generated portion. :return: |

## flyte.models.SerializationContext

This object holds serialization time contextual information, that can be used when serializing the task and
various parameters of a tasktemplate. This is only available when the task is being serialized and can be
during a deployment or runtime.



```python
class SerializationContext(
    version: str,
    project: str | None,
    domain: str | None,
    org: str | None,
    code_bundle: Optional[CodeBundle],
    input_path: str,
    output_path: str,
    interpreter_path: str,
    image_cache: ImageCache | None,
    root_dir: Optional[pathlib.Path],
)
```
| Parameter | Type | Description |
|-|-|-|
| `version` | `str` | The version of the task |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `org` | `str \| None` | |
| `code_bundle` | `Optional[CodeBundle]` | The code bundle for the task. This is used to package the code and the inflation path. |
| `input_path` | `str` | The path to the inputs for the task. This is used to determine where the inputs will be located |
| `output_path` | `str` | The path to the outputs for the task. This is used to determine where the outputs will be located |
| `interpreter_path` | `str` | |
| `image_cache` | `ImageCache \| None` | |
| `root_dir` | `Optional[pathlib.Path]` | |

### Methods

| Method | Description |
|-|-|
| [`get_entrypoint_path()`](#get_entrypoint_path) | Get the entrypoint path for the task. |


#### get_entrypoint_path()

```python
def get_entrypoint_path(
    interpreter_path: Optional[str],
) -> str
```
Get the entrypoint path for the task. This is used to determine the entrypoint for the task execution.


| Parameter | Type | Description |
|-|-|-|
| `interpreter_path` | `Optional[str]` | The path to the interpreter (python) |

## flyte.models.TaskContext

A context class to hold the current task executions context.
This can be used to access various contextual parameters in the task execution by the user.



```python
class TaskContext(
    action: ActionID,
    version: str,
    raw_data_path: RawDataPath,
    input_path: str | None,
    output_path: str,
    run_base_dir: str,
    report: Report,
    group_data: GroupData | None,
    checkpoints: Checkpoints | None,
    code_bundle: CodeBundle | None,
    compiled_image_cache: ImageCache | None,
    data: Dict[str, Any],
    mode: Literal['local', 'remote', 'hybrid'],
    interactive_mode: bool,
    custom_context: Dict[str, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `action` | `ActionID` | The action ID of the current execution. This is always set, within a run. |
| `version` | `str` | The version of the executed task. This is set when the task is executed by an action and will be set on all sub-actions. |
| `raw_data_path` | `RawDataPath` | |
| `input_path` | `str \| None` | |
| `output_path` | `str` | |
| `run_base_dir` | `str` | |
| `report` | `Report` | |
| `group_data` | `GroupData \| None` | |
| `checkpoints` | `Checkpoints \| None` | |
| `code_bundle` | `CodeBundle \| None` | |
| `compiled_image_cache` | `ImageCache \| None` | |
| `data` | `Dict[str, Any]` | |
| `mode` | `Literal['local', 'remote', 'hybrid']` | |
| `interactive_mode` | `bool` | |
| `custom_context` | `Dict[str, str]` | Context metadata for the action. If an action receives context, it'll automatically pass it to any actions it spawns. Context will not be used for cache key computation. |

### Methods

| Method | Description |
|-|-|
| [`is_in_cluster()`](#is_in_cluster) | Check if the task is running in a cluster. |
| [`replace()`](#replace) |  |


#### is_in_cluster()

```python
def is_in_cluster()
```
Check if the task is running in a cluster.
:return: bool


#### replace()

```python
def replace(
    kwargs,
) -> TaskContext
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

