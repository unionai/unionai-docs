---
title: flyte.models
version: 0.2.0b10.dev2+g9bf3bb9
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
| Parameter | Type |
|-|-|
| `name` | `str` |
| `run_name` | `str \| None` |
| `project` | `str \| None` |
| `domain` | `str \| None` |
| `org` | `str \| None` |

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


| Parameter | Type |
|-|-|
| `name` | `str \| None` |

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


| Parameter | Type |
|-|-|
| `task_call_seq` | `int` |
| `task_hash` | `str` |
| `input_hash` | `str` |
| `group` | `str \| None` |

## flyte.models.Checkpoints

A class representing the checkpoints for a task. This is used to store the checkpoints for the task execution.


```python
class Checkpoints(
    prev_checkpoint_path: str | None,
    checkpoint_path: str | None,
)
```
| Parameter | Type |
|-|-|
| `prev_checkpoint_path` | `str \| None` |
| `checkpoint_path` | `str \| None` |

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
| Parameter | Type |
|-|-|
| `computed_version` | `str` |
| `destination` | `str` |
| `tgz` | `str \| None` |
| `pkl` | `str \| None` |
| `downloaded_path` | `pathlib.Path \| None` |

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


| Parameter | Type |
|-|-|
| `path` | `pathlib.Path` |

## flyte.models.GroupData

```python
class GroupData(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

## flyte.models.NativeInterface

A class representing the native interface for a task. This is used to interact with the task and its execution
context.


```python
class NativeInterface(
    inputs: Dict[str, Tuple[Type, Any]],
    outputs: Dict[str, Type],
    docstring: Optional[Docstring],
)
```
| Parameter | Type |
|-|-|
| `inputs` | `Dict[str, Tuple[Type, Any]]` |
| `outputs` | `Dict[str, Type]` |
| `docstring` | `Optional[Docstring]` |

### Methods

| Method | Description |
|-|-|
| [`convert_to_kwargs()`](#convert_to_kwargs) | Convert the given arguments to keyword arguments based on the native interface. |
| [`from_callable()`](#from_callable) | Extract the native interface from the given function. |
| [`from_types()`](#from_types) | Create a new NativeInterface from the given types. |
| [`get_input_types()`](#get_input_types) | Get the input types for the task. |
| [`has_outputs()`](#has_outputs) | Check if the task has outputs. |


#### convert_to_kwargs()

```python
def convert_to_kwargs(
    args,
    kwargs,
) -> Dict[str, Any]
```
Convert the given arguments to keyword arguments based on the native interface. This is used to convert the
arguments to the correct types for the task execution.


| Parameter | Type |
|-|-|
| `args` | `*args` |
| `kwargs` | `**kwargs` |

#### from_callable()

```python
def from_callable(
    func: Callable,
) -> NativeInterface
```
Extract the native interface from the given function. This is used to create a native interface for the task.


| Parameter | Type |
|-|-|
| `func` | `Callable` |

#### from_types()

```python
def from_types(
    inputs: Dict[str, Type],
    outputs: Dict[str, Type],
) -> NativeInterface
```
Create a new NativeInterface from the given types. This is used to create a native interface for the task.


| Parameter | Type |
|-|-|
| `inputs` | `Dict[str, Type]` |
| `outputs` | `Dict[str, Type]` |

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


## flyte.models.RawDataPath

A class representing the raw data path for a task. This is used to store the raw data for the task execution and
also get mutations on the path.


```python
class RawDataPath(
    path: str,
)
```
| Parameter | Type |
|-|-|
| `path` | `str` |

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


| Parameter | Type |
|-|-|
| `local_folder` | `str \| pathlib.Path \| None` |

#### get_random_remote_path()

```python
def get_random_remote_path(
    file_name: Optional[str],
) -> str
```
Returns a random path for uploading a file/directory to.



| Parameter | Type |
|-|-|
| `file_name` | `Optional[str]` |

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
    image_cache: ImageCache | None,
    root_dir: Optional[pathlib.Path],
)
```
| Parameter | Type |
|-|-|
| `version` | `str` |
| `project` | `str \| None` |
| `domain` | `str \| None` |
| `org` | `str \| None` |
| `code_bundle` | `Optional[CodeBundle]` |
| `input_path` | `str` |
| `output_path` | `str` |
| `image_cache` | `ImageCache \| None` |
| `root_dir` | `Optional[pathlib.Path]` |

### Methods

| Method | Description |
|-|-|
| [`get_entrypoint_path()`](#get_entrypoint_path) | Get the entrypoint path for the task. |


#### get_entrypoint_path()

```python
def get_entrypoint_path(
    interpreter_path: str,
) -> str
```
Get the entrypoint path for the task. This is used to determine the entrypoint for the task execution.


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

## flyte.models.TaskContext

A context class to hold the current task executions context.
This can be used to access various contextual parameters in the task execution by the user.



```python
class TaskContext(
    action: ActionID,
    version: str,
    raw_data_path: RawDataPath,
    output_path: str,
    run_base_dir: str,
    report: Report,
    group_data: GroupData | None,
    checkpoints: Checkpoints | None,
    code_bundle: CodeBundle | None,
    compiled_image_cache: ImageCache | None,
    data: Dict[str, Any],
    mode: Literal['local', 'remote', 'hybrid'],
)
```
| Parameter | Type |
|-|-|
| `action` | `ActionID` |
| `version` | `str` |
| `raw_data_path` | `RawDataPath` |
| `output_path` | `str` |
| `run_base_dir` | `str` |
| `report` | `Report` |
| `group_data` | `GroupData \| None` |
| `checkpoints` | `Checkpoints \| None` |
| `code_bundle` | `CodeBundle \| None` |
| `compiled_image_cache` | `ImageCache \| None` |
| `data` | `Dict[str, Any]` |
| `mode` | `Literal['local', 'remote', 'hybrid']` |

### Methods

| Method | Description |
|-|-|
| [`replace()`](#replace) |  |


#### replace()

```python
def replace(
    kwargs,
) -> TaskContext
```
| Parameter | Type |
|-|-|
| `kwargs` | `**kwargs` |

