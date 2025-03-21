---
title: flytekit.core.python_auto_container
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.python_auto_container

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerabc) | Helper class that provides a standard way to create an ABC using. |
| [`BaseAccelerator`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerbaseaccelerator) | Base class for all accelerator types. |
| [`CopyFileDetection`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containercopyfiledetection) | Create a collection of name/value pairs. |
| [`DefaultNotebookTaskResolver`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaultnotebooktaskresolver) | This resolved is used when the task is defined in a notebook. |
| [`DefaultTaskResolver`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerdefaulttaskresolver) | Please see the notes in the TaskResolverMixin as it describes this default behavior. |
| [`FlyteContextManager`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteTrackedABC`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerflytetrackedabc) | This class exists because if you try to inherit from abc. |
| [`ImageBuildEngine`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`ImageConfig`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerimageconfig) | We recommend you to use ImageConfig. |
| [`ImageSpec`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`PickledEntity`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentity) | Represents the structure of the pickled object stored in the . |
| [`PickledEntityMetadata`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerpickledentitymetadata) | Metadata for a pickled entity containing version information. |
| [`PodTemplate`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerpodtemplate) | Custom PodTemplate specification for a Task. |
| [`PythonAutoContainerTask`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythonautocontainertask) | A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the. |
| [`PythonTask`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerpythontask) | Base Class for all Tasks with a Python native ``Interface``. |
| [`ResourceSpec`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerresourcespec) | None. |
| [`Resources`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerresources) | This class is used to specify both resource requests and resource limits. |
| [`Secret`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containersecret) | See :std:ref:`cookbook:secrets` for usage examples. |
| [`SecurityContext`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containersecuritycontext) | This is a higher level wrapper object that for the most part users shouldn't have to worry about. |
| [`SerializationSettings`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containerserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`TaskMetadata`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containertaskmetadata) | Metadata for a Task. |
| [`TaskResolverMixin`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containertaskresolvermixin) | Flytekit tasks interact with the Flyte platform very, very broadly in two steps. |
| [`TrackedInstance`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containertrackedinstance) | Please see the notes for the metaclass above first. |
| [`TypeVar`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containertypevar) | Type variable. |
| [`timeit`](.././flytekit.core.python_auto_container#flytekitcorepython_auto_containertimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

## flytekit.core.python_auto_container.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.core.python_auto_container.BaseAccelerator

Base class for all accelerator types. This class is not meant to be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.core.python_auto_container.CopyFileDetection

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.core.python_auto_container.DefaultNotebookTaskResolver

This resolved is used when the task is defined in a notebook. It is used to load the task from the notebook.


```python
def DefaultNotebookTaskResolver(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) | None |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task |
| [`name()`](#name) | None |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task |


#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: List[str],
):
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `List[str]` |

#### loader_args()

```python
def loader_args(
    settings: SerializationSettings,
    task: PythonAutoContainerTask,
):
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
| `task` | `PythonAutoContainerTask` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
):
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| instantiated_in |  |  |
| lhs |  |  |
| location |  |  |

## flytekit.core.python_auto_container.DefaultTaskResolver

Please see the notes in the TaskResolverMixin as it describes this default behavior.


```python
def DefaultTaskResolver(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) | None |
| [`get_all_tasks()`](#get_all_tasks) | Future proof method |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task |
| [`name()`](#name) | None |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task |


#### find_lhs()

```python
def find_lhs()
```
#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: List[str],
):
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `List[str]` |

#### loader_args()

```python
def loader_args(
    settings: SerializationSettings,
    task: PythonAutoContainerTask,
):
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |
| `task` | `PythonAutoContainerTask` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
):
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| instantiated_in |  |  |
| lhs |  |  |
| location |  |  |

## flytekit.core.python_auto_container.FlyteContextManager

FlyteContextManager manages the execution context within Flytekit. It holds global state of either compilation
or Execution. It is not thread-safe and can only be run as a single threaded application currently.
Context's within Flytekit is useful to manage compilation state and execution state. Refer to ``CompilationState``
and ``ExecutionState`` for more information. FlyteContextManager provides a singleton stack to manage these contexts.

Typical usage is

.. code-block:: python

FlyteContextManager.initialize()
with FlyteContextManager.with_context(o) as ctx:
pass

# If required - not recommended you can use
FlyteContextManager.push_context()
# but correspondingly a pop_context should be called
FlyteContextManager.pop_context()


### Methods

| Method | Description |
|-|-|
| [`add_signal_handler()`](#add_signal_handler) | None |
| [`current_context()`](#current_context) | None |
| [`get_origin_stackframe()`](#get_origin_stackframe) | None |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context |
| [`pop_context()`](#pop_context) | None |
| [`push_context()`](#push_context) | None |
| [`size()`](#size) | None |
| [`with_context()`](#with_context) | None |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
):
```
| Parameter | Type |
|-|-|
| `handler` | `typing.Callable[[int, FrameType], typing.Any]` |

#### current_context()

```python
def current_context()
```
#### get_origin_stackframe()

```python
def get_origin_stackframe(
    limit,
):
```
| Parameter | Type |
|-|-|
| `limit` |  |

#### initialize()

```python
def initialize()
```
Re-initializes the context and erases the entire context


#### pop_context()

```python
def pop_context()
```
#### push_context()

```python
def push_context(
    ctx: FlyteContext,
    f: Optional[traceback.FrameSummary],
):
```
| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `f` | `Optional[traceback.FrameSummary]` |

#### size()

```python
def size()
```
#### with_context()

```python
def with_context(
    b: FlyteContext.Builder,
):
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.core.python_auto_container.FlyteTrackedABC

This class exists because if you try to inherit from abc.ABC and TrackedInstance by itself, you'll get the
well-known ``TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass
of the metaclasses of all its bases`` error.


### Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC |


#### register()

```python
def register(
    cls,
    subclass,
):
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type |
|-|-|
| `cls` |  |
| `subclass` |  |

## flytekit.core.python_auto_container.ImageBuildEngine

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


### Methods

| Method | Description |
|-|-|
| [`build()`](#build) | None |
| [`get_registry()`](#get_registry) | None |
| [`register()`](#register) | None |


#### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### get_registry()

```python
def get_registry()
```
#### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
):
```
| Parameter | Type |
|-|-|
| `builder_type` | `str` |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` |
| `priority` | `int` |

## flytekit.core.python_auto_container.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
default_image (Optional[Image]): The default image to be used as a container for task serialization.
images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
def ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name |
| [`auto_default_image()`](#auto_default_image) | None |
| [`create_from()`](#create_from) | None |
| [`find_image()`](#find_image) | Return an image, by name, if it exists |
| [`from_dict()`](#from_dict) | None |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
):
```
Reads from config file or from img_name
Note that this function does not take into account the flytekit default images (see the Dockerfiles at the
base of this repo). To pick those up, see the auto_default_image function..



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |
| `img_name` | `Optional[str]` |

#### auto_default_image()

```python
def auto_default_image()
```
#### create_from()

```python
def create_from(
    default_image: Optional[Image],
    other_images: typing.Optional[typing.List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
):
```
Return an image, by name, if it exists.


| Parameter | Type |
|-|-|
| `name` |  |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_images()

```python
def from_images(
    default_image: str,
    m: typing.Optional[typing.Dict[str, str]],
):
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

.. code:: python

ImageConfig.from_dict(
"ghcr.io/flyteorg/flytecookbook:v1.0.0",
{
"spark": "ghcr.io/flyteorg/myspark:...",
"other": "...",
}
)

urn:


| Parameter | Type |
|-|-|
| `default_image` | `str` |
| `m` | `typing.Optional[typing.Dict[str, str]]` |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
):
```
Validates the image to match the standard format. Also validates that only one default image
is provided. a default image, is one that is specified as ``default=<image_uri>`` or just ``<image_uri>``. All
other images should be provided with a name, in the format ``name=<image_uri>`` This method can be used with the
CLI



| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `tuple` |

## flytekit.core.python_auto_container.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
def ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment |
| [`image_name()`](#image_name) | Full image name with tag |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
):
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| tag |  |  |

## flytekit.core.python_auto_container.PickledEntity

Represents the structure of the pickled object stored in the .pkl file for interactive mode.

Attributes:
metadata: Metadata about the pickled entities including Python version
entities: Dictionary mapping entity names to their PythonAutoContainerTask instances


```python
def PickledEntity(
    metadata: PickledEntityMetadata,
    entities: Dict[str, PythonAutoContainerTask],
):
```
| Parameter | Type |
|-|-|
| `metadata` | `PickledEntityMetadata` |
| `entities` | `Dict[str, PythonAutoContainerTask]` |

## flytekit.core.python_auto_container.PickledEntityMetadata

Metadata for a pickled entity containing version information.

Attributes:
python_version: The Python version string (e.g. "3.12.0") used to create the pickle


```python
def PickledEntityMetadata(
    python_version: str,
):
```
| Parameter | Type |
|-|-|
| `python_version` | `str` |

## flytekit.core.python_auto_container.PodTemplate

Custom PodTemplate specification for a Task.


```python
def PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
):
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

## flytekit.core.python_auto_container.PythonAutoContainerTask

A Python AutoContainer task should be used as the base for all extensions that want the user's code to be in the
container and the container information to be automatically captured.
This base will auto configure the image and image version to be used for all its derivatives.

If you are looking to extend, you might prefer to use ``PythonFunctionTask`` or ``PythonInstanceTask``


```python
def PythonAutoContainerTask(
    name: str,
    task_config: T,
    task_type,
    container_image: Optional[Union[str, ImageSpec]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    environment: Optional[Dict[str, str]],
    task_resolver: Optional[TaskResolverMixin],
    secret_requests: Optional[List[Secret]],
    pod_template: Optional[PodTemplate],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `task_config` | `T` |
| `task_type` |  |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `environment` | `Optional[Dict[str, str]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `pod_template` | `Optional[PodTemplate]` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_command()`](#get_command) | Returns the command which should be used in the container definition for the serialized version of this task |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_default_command()`](#get_default_command) | Returns the default pyflyte-execute command used to run this on hosted Flyte platforms |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_image()`](#get_image) | Update image spec based on fast registration usage, and return string representing the image |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`reset_command_fn()`](#reset_command_fn) | Resets the command which should be used in the container definition of this task to the default arguments |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |
| [`set_command_fn()`](#set_command_fn) | By default, the task will run on the Flyte platform using the pyflyte-execute command |
| [`set_resolver()`](#set_resolver) | By default, flytekit uses the DefaultTaskResolver to resolve the task |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_command()

```python
def get_command(
    settings: SerializationSettings,
):
```
Returns the command which should be used in the container definition for the serialized version of this task
registered on a hosted Flyte platform.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_config()

```python
def get_config(
    settings: SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_default_command()

```python
def get_default_command(
    settings: SerializationSettings,
):
```
Returns the default pyflyte-execute command used to run this on hosted Flyte platforms.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_image()

```python
def get_image(
    settings: SerializationSettings,
):
```
Update image spec based on fast registration usage, and return string representing the image


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### reset_command_fn()

```python
def reset_command_fn()
```
Resets the command which should be used in the container definition of this task to the default arguments.
This is useful when the command line is overridden at serialization time.


#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### set_command_fn()

```python
def set_command_fn(
    get_command_fn: Optional[Callable[[SerializationSettings], List[str]]],
):
```
By default, the task will run on the Flyte platform using the pyflyte-execute command.
However, it can be useful to update the command with which the task is serialized for specific cases like
running map tasks ("pyflyte-map-execute") or for fast-executed tasks.


| Parameter | Type |
|-|-|
| `get_command_fn` | `Optional[Callable[[SerializationSettings], List[str]]]` |

#### set_resolver()

```python
def set_resolver(
    resolver: TaskResolverMixin,
):
```
By default, flytekit uses the DefaultTaskResolver to resolve the task. This method allows the user to set a custom
task resolver. It can be useful to override the task resolver for specific cases like running tasks in the jupyter notebook.


| Parameter | Type |
|-|-|
| `resolver` | `TaskResolverMixin` |

### Properties

| Property | Type | Description |
|-|-|-|
| container_image |  |  |
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| resources |  |  |
| security_context |  |  |
| task_config |  |  |
| task_resolver |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.core.python_auto_container.PythonTask

Base Class for all Tasks with a Python native ``Interface``. This should be directly used for task types, that do
not have a python function to be executed. Otherwise refer to :py:class:`flytekit.PythonFunctionTask`.


```python
def PythonTask(
    task_type: str,
    name: str,
    task_config: typing.Optional[~T],
    interface: typing.Optional[flytekit.core.interface.Interface],
    environment: typing.Optional[typing.Dict[str, str]],
    disable_deck: typing.Optional[bool],
    enable_deck: typing.Optional[bool],
    deck_fields: typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `task_type` | `str` |
| `name` | `str` |
| `task_config` | `typing.Optional[~T]` |
| `interface` | `typing.Optional[flytekit.core.interface.Interface]` |
| `environment` | `typing.Optional[typing.Dict[str, str]]` |
| `disable_deck` | `typing.Optional[bool]` |
| `enable_deck` | `typing.Optional[bool]` |
| `deck_fields` | `typing.Optional[typing.Tuple[flytekit.deck.deck.DeckField, ...]]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) | Generates a node that encapsulates this task in a workflow definition |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition |
| [`dispatch_execute()`](#dispatch_execute) | This method translates Flyte's Type system based input values and invokes the actual call to the executor |
| [`execute()`](#execute) | This method will be invoked to execute the task |
| [`find_lhs()`](#find_lhs) | None |
| [`get_config()`](#get_config) | Returns the task config as a serializable dictionary |
| [`get_container()`](#get_container) | Returns the container definition (if any) that is used to run the task on hosted Flyte |
| [`get_custom()`](#get_custom) | Return additional plugin-specific custom data (if any) as a serializable dictionary |
| [`get_extended_resources()`](#get_extended_resources) | Returns the extended resources to allocate to the task on hosted Flyte |
| [`get_input_types()`](#get_input_types) | Returns the names and python types as a dictionary for the inputs of this task |
| [`get_k8s_pod()`](#get_k8s_pod) | Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte |
| [`get_sql()`](#get_sql) | Returns the Sql definition (if any) that is used to run the task on hosted Flyte |
| [`get_type_for_input_var()`](#get_type_for_input_var) | Returns the python type for an input variable by name |
| [`get_type_for_output_var()`](#get_type_for_output_var) | Returns the python type for the specified output variable by name |
| [`local_execute()`](#local_execute) | This function is used only in the local execution path and is responsible for calling dispatch execute |
| [`local_execution_mode()`](#local_execution_mode) | None |
| [`post_execute()`](#post_execute) | Post execute is called after the execution has completed, with the user_params and can be used to clean-up, |
| [`pre_execute()`](#pre_execute) | This is the method that will be invoked directly before executing the task method and before all the inputs |
| [`sandbox_execute()`](#sandbox_execute) | Call dispatch_execute, in the context of a local sandbox execution |


#### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
):
```
Generates a node that encapsulates this task in a workflow definition.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


#### dispatch_execute()

```python
def dispatch_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
This method translates Flyte's Type system based input values and invokes the actual call to the executor
This method is also invoked during runtime.

* ``VoidPromise`` is returned in the case when the task itself declares no outputs.
* ``Literal Map`` is returned when the task returns either one more outputs in the declaration. Individual outputs
may be none
* ``DynamicJobSpec`` is returned when a dynamic workflow is executed


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

#### execute()

```python
def execute(
    kwargs,
):
```
This method will be invoked to execute the task.


| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

#### find_lhs()

```python
def find_lhs()
```
#### get_config()

```python
def get_config(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the task config as a serializable dictionary. This task config consists of metadata about the custom
defined for this task.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_container()

```python
def get_container(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the container definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_custom()

```python
def get_custom(
    settings: flytekit.configuration.SerializationSettings,
):
```
Return additional plugin-specific custom data (if any) as a serializable dictionary.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_extended_resources()

```python
def get_extended_resources(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the extended resources to allocate to the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_input_types()

```python
def get_input_types()
```
Returns the names and python types as a dictionary for the inputs of this task.


#### get_k8s_pod()

```python
def get_k8s_pod(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the kubernetes pod definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_sql()

```python
def get_sql(
    settings: flytekit.configuration.SerializationSettings,
):
```
Returns the Sql definition (if any) that is used to run the task on hosted Flyte.


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |

#### get_type_for_input_var()

```python
def get_type_for_input_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for an input variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### get_type_for_output_var()

```python
def get_type_for_output_var(
    k: str,
    v: typing.Any,
):
```
Returns the python type for the specified output variable by name.


| Parameter | Type |
|-|-|
| `k` | `str` |
| `v` | `typing.Any` |

#### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
):
```
This function is used only in the local execution path and is responsible for calling dispatch execute.
Use this function when calling a task with native values (or Promises containing Flyte literals derived from
Python native values).


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `kwargs` | ``**kwargs`` |

#### local_execution_mode()

```python
def local_execution_mode()
```
#### post_execute()

```python
def post_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
    rval: typing.Any,
):
```
Post execute is called after the execution has completed, with the user_params and can be used to clean-up,
or alter the outputs to match the intended tasks outputs. If not overridden, then this function is a No-op



| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |
| `rval` | `typing.Any` |

#### pre_execute()

```python
def pre_execute(
    user_params: typing.Optional[flytekit.core.context_manager.ExecutionParameters],
):
```
This is the method that will be invoked directly before executing the task method and before all the inputs
are converted. One particular case where this is useful is if the context is to be modified for the user process
to get some user space parameters. This also ensures that things like SparkSession are already correctly
setup before the type transformers are called

This should return either the same context of the mutated context


| Parameter | Type |
|-|-|
| `user_params` | `typing.Optional[flytekit.core.context_manager.ExecutionParameters]` |

#### sandbox_execute()

```python
def sandbox_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    input_literal_map: flytekit.models.literals.LiteralMap,
):
```
Call dispatch_execute, in the context of a local sandbox execution. Not invoked during runtime.


| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `input_literal_map` | `flytekit.models.literals.LiteralMap` |

### Properties

| Property | Type | Description |
|-|-|-|
| deck_fields |  |  |
| disable_deck |  |  |
| docs |  |  |
| enable_deck |  |  |
| environment |  |  |
| instantiated_in |  |  |
| interface |  |  |
| lhs |  |  |
| location |  |  |
| metadata |  |  |
| name |  |  |
| python_interface |  |  |
| security_context |  |  |
| task_config |  |  |
| task_type |  |  |
| task_type_version |  |  |

## flytekit.core.python_auto_container.ResourceSpec

```python
def ResourceSpec(
    requests: flytekit.core.resources.Resources,
    limits: flytekit.core.resources.Resources,
):
```
| Parameter | Type |
|-|-|
| `requests` | `flytekit.core.resources.Resources` |
| `limits` | `flytekit.core.resources.Resources` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_multiple_resource()`](#from_multiple_resource) | Convert Resources that represent both a requests and limits into a ResourceSpec |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### from_multiple_resource()

```python
def from_multiple_resource(
    resource: flytekit.core.resources.Resources,
):
```
Convert Resources that represent both a requests and limits into a ResourceSpec.


| Parameter | Type |
|-|-|
| `resource` | `flytekit.core.resources.Resources` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

## flytekit.core.python_auto_container.Resources

This class is used to specify both resource requests and resource limits.

.. code-block:: python

Resources(cpu="1", mem="2048")  # This is 1 CPU and 2 KB of memory
Resources(cpu="100m", mem="2Gi")  # This is 1/10th of a CPU and 2 gigabytes of memory
Resources(cpu=0.5, mem=1024) # This is 500m CPU and 1 KB of memory

# For Kubernetes-based tasks, pods use ephemeral local storage for scratch space, caching, and for logs.
# This allocates 1Gi of such local storage.
Resources(ephemeral_storage="1Gi")

When used together with `@task(resources=)`, you a specific the request and limits with one object.
When the value is set to a tuple or list, the first value is the request and the
second value is the limit. If the value is a single value, then both the requests and limit is
set to that value. For example, the `Resource(cpu=("1", "2"), mem=1024)` will set the cpu request to 1, cpu limit to 2,
mem limit and request to 1024.

.. note::

Persistent storage is not currently supported on the Flyte backend.

Please see the :std:ref:`User Guide <cookbook:customizing task resources>` for detailed examples.
Also refer to the `K8s conventions. <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>`__


```python
def Resources(
    cpu: typing.Union[str, int, float, list, tuple, NoneType],
    mem: typing.Union[str, int, list, tuple, NoneType],
    gpu: typing.Union[str, int, list, tuple, NoneType],
    ephemeral_storage: typing.Union[str, int, NoneType],
):
```
| Parameter | Type |
|-|-|
| `cpu` | `typing.Union[str, int, float, list, tuple, NoneType]` |
| `mem` | `typing.Union[str, int, list, tuple, NoneType]` |
| `gpu` | `typing.Union[str, int, list, tuple, NoneType]` |
| `ephemeral_storage` | `typing.Union[str, int, NoneType]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    d,
    dialect,
):
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
):
```
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

## flytekit.core.python_auto_container.Secret

See :std:ref:`cookbook:secrets` for usage examples.



```python
def Secret(
    group: typing.Optional[str],
    key: typing.Optional[str],
    group_version: typing.Optional[str],
    mount_requirement: <enum 'MountType'>,
    env_var: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `group` | `typing.Optional[str]` |
| `key` | `typing.Optional[str]` |
| `group_version` | `typing.Optional[str]` |
| `mount_requirement` | `<enum 'MountType'>` |
| `env_var` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.Secret,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.Secret` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.core.python_auto_container.SecurityContext

This is a higher level wrapper object that for the most part users shouldn't have to worry about. You should
be able to just use :py:class:`flytekit.Secret` instead.


```python
def SecurityContext(
    run_as: typing.Optional[flytekit.models.security.Identity],
    secrets: typing.Optional[typing.List[flytekit.models.security.Secret]],
    tokens: typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]],
):
```
| Parameter | Type |
|-|-|
| `run_as` | `typing.Optional[flytekit.models.security.Identity]` |
| `secrets` | `typing.Optional[typing.List[flytekit.models.security.Secret]]` |
| `tokens` | `typing.Optional[typing.List[flytekit.models.security.OAuth2TokenRequest]]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.security_pb2.SecurityContext,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.security_pb2.SecurityContext` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |

## flytekit.core.python_auto_container.SerializationSettings

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
project (str): The project (if any) with which to register entities under.
domain (str): The domain (if any) with which to register entities under.
version (str): The version (if any) with which to register entities under.
image_config (ImageConfig): The image config used to define task container images.
env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
virtualenv at serialization time won't match the in-container value at execution time. This optional value
is used to provide the in-container virtualenv path
python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
container execution.
entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
entrypoint program.
fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
can be fast registered (and thus omit building a Docker image) this object contains additional parameters
for serialization.
source_root (Optional[str]): The root directory of the source code.


```python
def SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `image_config` | `ImageConfig` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `version` | `typing.Optional[str]` |
| `env` | `Optional[Dict[str, str]]` |
| `git_repo` | `Optional[str]` |
| `python_interpreter` | `str` |
| `flytekit_virtualenv_root` | `Optional[str]` |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` |
| `source_root` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is |
| [`for_image()`](#for_image) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_transport()`](#from_transport) | None |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings |
| [`schema()`](#schema) | None |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
):
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
):
```
| Parameter | Type |
|-|-|
| `image` | `str` |
| `version` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `python_interpreter_path` | `str` |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
):
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_transport()

```python
def from_transport(
    s: str,
):
```
| Parameter | Type |
|-|-|
| `s` | `str` |

#### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
):
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


#### to_dict()

```python
def to_dict(
    encode_json,
):
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
):
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
):
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -> /opt/venv


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


### Properties

| Property | Type | Description |
|-|-|-|
| entrypoint_settings |  |  |
| serialized_context |  |  |

## flytekit.core.python_auto_container.TaskMetadata

Metadata for a Task. Things like retries and whether or not caching is turned on, and cache version are specified
here.

See the :std:ref:`IDL <idl:protos/docs/core/core:taskmetadata>` for the protobuf definition.

Attributes:
cache (bool): Indicates if caching should be enabled. See :std:ref:`Caching <cookbook:caching>`.
cache_serialize (bool): Indicates if identical (i.e. same inputs) instances of this task should be executed in serial when caching is enabled. See :std:ref:`Caching <cookbook:caching>`.
cache_version (str): Version to be used for the cached value.
cache_ignore_input_vars (Tuple[str, ...]): Input variables that should not be included when calculating hash for cache.
interruptible (Optional[bool]): Indicates that this task can be interrupted and/or scheduled on nodes with lower QoS guarantees that can include pre-emption.
deprecated (str): Can be used to provide a warning message for a deprecated task. An absence or empty string indicates that the task is active and not deprecated.
retries (int): for retries=n; n > 0, on failures of this task, the task will be retried at-least n number of times.
timeout (Optional[Union[datetime.timedelta, int]]): The maximum duration for which one execution of this task should run. The execution will be terminated if the runtime exceeds this timeout.
pod_template_name (Optional[str]): The name of an existing PodTemplate resource in the cluster which will be used for this task.
generates_deck (bool): Indicates whether the task will generate a Deck URI.
is_eager (bool): Indicates whether the task should be treated as eager.


```python
def TaskMetadata(
    cache: bool,
    cache_serialize: bool,
    cache_version: str,
    cache_ignore_input_vars: typing.Tuple[str, ...],
    interruptible: typing.Optional[bool],
    deprecated: str,
    retries: int,
    timeout: typing.Union[datetime.timedelta, int, NoneType],
    pod_template_name: typing.Optional[str],
    generates_deck: bool,
    is_eager: bool,
):
```
| Parameter | Type |
|-|-|
| `cache` | `bool` |
| `cache_serialize` | `bool` |
| `cache_version` | `str` |
| `cache_ignore_input_vars` | `typing.Tuple[str, ...]` |
| `interruptible` | `typing.Optional[bool]` |
| `deprecated` | `str` |
| `retries` | `int` |
| `timeout` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `pod_template_name` | `typing.Optional[str]` |
| `generates_deck` | `bool` |
| `is_eager` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`to_taskmetadata_model()`](#to_taskmetadata_model) | Converts to _task_model |


#### to_taskmetadata_model()

```python
def to_taskmetadata_model()
```
Converts to _task_model.TaskMetadata


### Properties

| Property | Type | Description |
|-|-|-|
| retry_strategy |  |  |

## flytekit.core.python_auto_container.TaskResolverMixin

Flytekit tasks interact with the Flyte platform very, very broadly in two steps. They need to be uploaded to Admin,
and then they are run by the user upon request (either as a single task execution or as part of a workflow). In any
case, at execution time, for most tasks (that is those that generate a container target) the container image
containing the task needs to be spun up again at which point the container needs to know which task it's supposed
to run and how to rehydrate the task object.

For example, the serialization of a simple task ::

# in repo_root/workflows/example.py
@task
def t1(...) -> ...: ...

might result in a container with arguments like ::

pyflyte-execute --inputs s3://path/inputs.pb --output-prefix s3://outputs/location         --raw-output-data-prefix /tmp/data         --resolver flytekit.core.python_auto_container.default_task_resolver         --         task-module repo_root.workflows.example task-name t1

At serialization time, the container created for the task will start out automatically with the ``pyflyte-execute``
bit, along with the requisite input/output args and the offloaded data prefix. Appended to that will be two things,

#. the ``location`` of the task's task resolver, followed by two dashes, followed by
#. the arguments provided by calling the ``loader_args`` function below.

The ``default_task_resolver`` declared below knows that

* When ``loader_args`` is called on a task, to look up the module the task is in, and the name of the task (the
key of the task in the module, either the function name, or the variable it was assigned to).
* When ``load_task`` is called, it interprets the first part of the command as the module to call
``importlib.import_module`` on, and then looks for a key ``t1``.

This is just the default behavior. Users should feel free to implement their own resolvers.


### Methods

| Method | Description |
|-|-|
| [`get_all_tasks()`](#get_all_tasks) | Future proof method |
| [`load_task()`](#load_task) | Given the set of identifier keys, should return one Python Task or raise an error if not found |
| [`loader_args()`](#loader_args) | Return a list of strings that can help identify the parameter Task |
| [`name()`](#name) | None |
| [`task_name()`](#task_name) | Overridable function that can optionally return a custom name for a given task |


#### get_all_tasks()

```python
def get_all_tasks()
```
Future proof method. Just making it easy to access all tasks (Not required today as we auto register them)


#### load_task()

```python
def load_task(
    loader_args: typing.List[str],
):
```
Given the set of identifier keys, should return one Python Task or raise an error if not found


| Parameter | Type |
|-|-|
| `loader_args` | `typing.List[str]` |

#### loader_args()

```python
def loader_args(
    settings: flytekit.configuration.SerializationSettings,
    t: flytekit.core.base_task.Task,
):
```
Return a list of strings that can help identify the parameter Task


| Parameter | Type |
|-|-|
| `settings` | `flytekit.configuration.SerializationSettings` |
| `t` | `flytekit.core.base_task.Task` |

#### name()

```python
def name()
```
#### task_name()

```python
def task_name(
    t: flytekit.core.base_task.Task,
):
```
Overridable function that can optionally return a custom name for a given task


| Parameter | Type |
|-|-|
| `t` | `flytekit.core.base_task.Task` |

### Properties

| Property | Type | Description |
|-|-|-|
| location |  |  |

## flytekit.core.python_auto_container.TrackedInstance

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
def TrackedInstance(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) | None |


#### find_lhs()

```python
def find_lhs()
```
### Properties

| Property | Type | Description |
|-|-|-|
| instantiated_in |  |  |
| lhs |  |  |
| location |  |  |

## flytekit.core.python_auto_container.TypeVar

Type variable.

The preferred way to construct a type variable is via the dedicated
syntax for generic functions, classes, and type aliases::

class Sequence[T]:  # T is a TypeVar
...

This syntax can also be used to create bound and constrained type
variables::

# S is a TypeVar bound to str
class StrSequence[S: str]:
...

# A is a TypeVar constrained to str or bytes
class StrOrBytesSequence[A: (str, bytes)]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes

Type variables exist primarily for the benefit of static type
checkers.  They serve as the parameters for generic types as well
as for generic function and type alias definitions.

The variance of type variables is inferred by type checkers when they
are created through the type parameter syntax and when
``infer_variance=True`` is passed. Manually created type variables may
be explicitly marked covariant or contravariant by passing
``covariant=True`` or ``contravariant=True``. By default, manually
created type variables are invariant. See PEP 484 and PEP 695 for more
details.


## flytekit.core.python_auto_container.timeit

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
# your code


```python
def timeit(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |

