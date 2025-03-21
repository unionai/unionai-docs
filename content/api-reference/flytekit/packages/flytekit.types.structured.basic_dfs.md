---
title: flytekit.types.structured.basic_dfs
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.types.structured.basic_dfs

## Directory

### Classes

| Class | Description |
|-|-|
| [`ArrowToParquetEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsarrowtoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`CSVToPandasDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfscsvtopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`DataConfig`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsdataconfig) | Any data storage specific configuration. |
| [`FlyteContext`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsflytecontext) | This is an internal-facing context object, that most users will not have to deal with. |
| [`PandasToCSVEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastocsvencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`PandasToParquetEncodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspandastoparquetencodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToArrowDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettoarrowdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`ParquetToPandasDecodingHandler`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsparquettopandasdecodinghandler) | Helper class that provides a standard way to create an ABC using. |
| [`Path`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfspath) | PurePath subclass that can make system calls. |
| [`StructuredDataset`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetDecoder`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetdecoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetEncoder`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetencoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetMetadata`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasetmetadata) | None. |
| [`StructuredDatasetType`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsstructureddatasettype) | None. |
| [`TypeVar`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfstypevar) | Type variable. |

### Errors

* [`NoCredentialsError`](.././flytekit.types.structured.basic_dfs#flytekittypesstructuredbasic_dfsnocredentialserror)

## flytekit.types.structured.basic_dfs.ArrowToParquetEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ArrowToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
):
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.CSVToPandasDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def CSVToPandasDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
):
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.DataConfig

Any data storage specific configuration. Please do not use this to store secrets, in S3 case, as it is used in
Flyte sandbox environment we store the access key id and secret.
All DataPersistence plugins are passed all DataConfig and the plugin should correctly use the right config


```python
def DataConfig(
    s3: S3Config,
    gcs: GCSConfig,
    azure: AzureBlobStorageConfig,
    generic: GenericPersistenceConfig,
):
```
| Parameter | Type |
|-|-|
| `s3` | `S3Config` |
| `gcs` | `GCSConfig` |
| `azure` | `AzureBlobStorageConfig` |
| `generic` | `GenericPersistenceConfig` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.types.structured.basic_dfs.FlyteContext

This is an internal-facing context object, that most users will not have to deal with. It's essentially a globally
available grab bag of settings and objects that allows flytekit to do things like convert complex types, run and
compile workflows, serialize Flyte entities, etc.

Even though this object as a ``current_context`` function on it, it should not be called directly. Please use the
:py:class:`flytekit.FlyteContextManager` object instead.

Please do not confuse this object with the :py:class:`flytekit.ExecutionParameters` object.


```python
def FlyteContext(
    file_access: FileAccessProvider,
    level: int,
    flyte_client: Optional['friendly_client.SynchronousFlyteClient'],
    compilation_state: Optional[CompilationState],
    execution_state: Optional[ExecutionState],
    serialization_settings: Optional[SerializationSettings],
    in_a_condition: bool,
    origin_stackframe: Optional[traceback.FrameSummary],
    output_metadata_tracker: Optional[OutputMetadataTracker],
    worker_queue: Optional[Controller],
):
```
| Parameter | Type |
|-|-|
| `file_access` | `FileAccessProvider` |
| `level` | `int` |
| `flyte_client` | `Optional['friendly_client.SynchronousFlyteClient']` |
| `compilation_state` | `Optional[CompilationState]` |
| `execution_state` | `Optional[ExecutionState]` |
| `serialization_settings` | `Optional[SerializationSettings]` |
| `in_a_condition` | `bool` |
| `origin_stackframe` | `Optional[traceback.FrameSummary]` |
| `output_metadata_tracker` | `Optional[OutputMetadataTracker]` |
| `worker_queue` | `Optional[Controller]` |

### Methods

| Method | Description |
|-|-|
| [`current_context()`](#current_context) | This method exists only to maintain backwards compatibility |
| [`enter_conditional_section()`](#enter_conditional_section) | None |
| [`get_deck()`](#get_deck) | Returns the deck that was created as part of the last execution |
| [`get_origin_stackframe_repr()`](#get_origin_stackframe_repr) | None |
| [`new_builder()`](#new_builder) | None |
| [`new_compilation_state()`](#new_compilation_state) | Creates and returns a default compilation state |
| [`new_execution_state()`](#new_execution_state) | Creates and returns a new default execution state |
| [`set_stackframe()`](#set_stackframe) | None |
| [`with_client()`](#with_client) | None |
| [`with_compilation_state()`](#with_compilation_state) | None |
| [`with_execution_state()`](#with_execution_state) | None |
| [`with_file_access()`](#with_file_access) | None |
| [`with_new_compilation_state()`](#with_new_compilation_state) | None |
| [`with_output_metadata_tracker()`](#with_output_metadata_tracker) | None |
| [`with_serialization_settings()`](#with_serialization_settings) | None |
| [`with_worker_queue()`](#with_worker_queue) | None |


#### current_context()

```python
def current_context()
```
This method exists only to maintain backwards compatibility. Please use
``FlyteContextManager.current_context()`` instead.

Users of flytekit should be wary not to confuse the object returned from this function
with :py:func:`flytekit.current_context`


#### enter_conditional_section()

```python
def enter_conditional_section()
```
#### get_deck()

```python
def get_deck()
```
Returns the deck that was created as part of the last execution.

The return value depends on the execution environment. In a notebook, the return value is compatible with
IPython.display and should be rendered in the notebook.

.. code-block:: python

with flytekit.new_context() as ctx:
my_task(...)
ctx.get_deck()

OR if you wish to explicitly display

.. code-block:: python

from IPython import display
display(ctx.get_deck())


#### get_origin_stackframe_repr()

```python
def get_origin_stackframe_repr()
```
#### new_builder()

```python
def new_builder()
```
#### new_compilation_state()

```python
def new_compilation_state(
    prefix: str,
):
```
Creates and returns a default compilation state. For most of the code this should be the entrypoint
of compilation, otherwise the code should always uses - with_compilation_state


| Parameter | Type |
|-|-|
| `prefix` | `str` |

#### new_execution_state()

```python
def new_execution_state(
    working_dir: Optional[os.PathLike],
):
```
Creates and returns a new default execution state. This should be used at the entrypoint of execution,
in all other cases it is preferable to use with_execution_state


| Parameter | Type |
|-|-|
| `working_dir` | `Optional[os.PathLike]` |

#### set_stackframe()

```python
def set_stackframe(
    s: traceback.FrameSummary,
):
```
| Parameter | Type |
|-|-|
| `s` | `traceback.FrameSummary` |

#### with_client()

```python
def with_client(
    c: SynchronousFlyteClient,
):
```
| Parameter | Type |
|-|-|
| `c` | `SynchronousFlyteClient` |

#### with_compilation_state()

```python
def with_compilation_state(
    c: CompilationState,
):
```
| Parameter | Type |
|-|-|
| `c` | `CompilationState` |

#### with_execution_state()

```python
def with_execution_state(
    es: ExecutionState,
):
```
| Parameter | Type |
|-|-|
| `es` | `ExecutionState` |

#### with_file_access()

```python
def with_file_access(
    fa: FileAccessProvider,
):
```
| Parameter | Type |
|-|-|
| `fa` | `FileAccessProvider` |

#### with_new_compilation_state()

```python
def with_new_compilation_state()
```
#### with_output_metadata_tracker()

```python
def with_output_metadata_tracker(
    t: OutputMetadataTracker,
):
```
| Parameter | Type |
|-|-|
| `t` | `OutputMetadataTracker` |

#### with_serialization_settings()

```python
def with_serialization_settings(
    ss: SerializationSettings,
):
```
| Parameter | Type |
|-|-|
| `ss` | `SerializationSettings` |

#### with_worker_queue()

```python
def with_worker_queue(
    wq: Controller,
):
```
| Parameter | Type |
|-|-|
| `wq` | `Controller` |

### Properties

| Property | Type | Description |
|-|-|-|
| user_space_params |  |  |

## flytekit.types.structured.basic_dfs.NoCredentialsError

No credentials could be found.


```python
def NoCredentialsError(
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `kwargs` | ``**kwargs`` |

## flytekit.types.structured.basic_dfs.PandasToCSVEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def PandasToCSVEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
):
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.PandasToParquetEncodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def PandasToParquetEncodingHandler()
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the |


#### encode()

```python
def encode(
    ctx: flytekit.core.context_manager.FlyteContext,
    structured_dataset: flytekit.types.structured.structured_dataset.StructuredDataset,
    structured_dataset_type: flytekit.models.types.StructuredDatasetType,
):
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `structured_dataset` | `flytekit.types.structured.structured_dataset.StructuredDataset` |
| `structured_dataset_type` | `flytekit.models.types.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.ParquetToArrowDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ParquetToArrowDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
):
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.ParquetToPandasDecodingHandler

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def ParquetToPandasDecodingHandler()
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal |


#### decode()

```python
def decode(
    ctx: flytekit.core.context_manager.FlyteContext,
    flyte_value: flytekit.models.literals.StructuredDataset,
    current_task_metadata: flytekit.models.literals.StructuredDatasetMetadata,
):
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` |
| `flyte_value` | `flytekit.models.literals.StructuredDataset` |
| `current_task_metadata` | `flytekit.models.literals.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.Path

PurePath subclass that can make system calls.

Path represents a filesystem path but unlike PurePath, also offers
methods to do system calls on path objects. Depending on your system,
instantiating a Path will return either a PosixPath or a WindowsPath
object. You can also instantiate a PosixPath or WindowsPath directly,
but cannot instantiate a WindowsPath on a POSIX system or vice versa.


```python
def Path(
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
| [`absolute()`](#absolute) | Return an absolute version of this path by prepending the current |
| [`as_posix()`](#as_posix) | Return the string representation of the path with forward (/) |
| [`as_uri()`](#as_uri) | Return the path as a 'file' URI |
| [`chmod()`](#chmod) | Change the permissions of the path, like os |
| [`cwd()`](#cwd) | Return a new path pointing to the current working directory |
| [`exists()`](#exists) | Whether this path exists |
| [`expanduser()`](#expanduser) | Return a new path with expanded ~ and ~user constructs |
| [`glob()`](#glob) | Iterate over this subtree and yield all existing files (of any |
| [`group()`](#group) | Return the group name of the file gid |
| [`hardlink_to()`](#hardlink_to) | Make this path a hard link pointing to the same file as *target* |
| [`home()`](#home) | Return a new path pointing to the user's home directory (as |
| [`is_absolute()`](#is_absolute) | True if the path is absolute (has both a root and, if applicable, |
| [`is_block_device()`](#is_block_device) | Whether this path is a block device |
| [`is_char_device()`](#is_char_device) | Whether this path is a character device |
| [`is_dir()`](#is_dir) | Whether this path is a directory |
| [`is_fifo()`](#is_fifo) | Whether this path is a FIFO |
| [`is_file()`](#is_file) | Whether this path is a regular file (also True for symlinks pointing |
| [`is_junction()`](#is_junction) | Whether this path is a junction |
| [`is_mount()`](#is_mount) | Check if this path is a mount point |
| [`is_relative_to()`](#is_relative_to) | Return True if the path is relative to another path or False |
| [`is_reserved()`](#is_reserved) | Return True if the path contains one of the special names reserved |
| [`is_socket()`](#is_socket) | Whether this path is a socket |
| [`is_symlink()`](#is_symlink) | Whether this path is a symbolic link |
| [`iterdir()`](#iterdir) | Yield path objects of the directory contents |
| [`joinpath()`](#joinpath) | Combine this path with one or several arguments, and return a |
| [`lchmod()`](#lchmod) | Like chmod(), except if the path points to a symlink, the symlink's |
| [`lstat()`](#lstat) | Like stat(), except if the path points to a symlink, the symlink's |
| [`match()`](#match) | Return True if this path matches the given pattern |
| [`mkdir()`](#mkdir) | Create a new directory at this given path |
| [`open()`](#open) | Open the file pointed to by this path and return a file object, as |
| [`owner()`](#owner) | Return the login name of the file owner |
| [`read_bytes()`](#read_bytes) | Open the file in bytes mode, read it, and close the file |
| [`read_text()`](#read_text) | Open the file in text mode, read it, and close the file |
| [`readlink()`](#readlink) | Return the path to which the symbolic link points |
| [`relative_to()`](#relative_to) | Return the relative path to another path identified by the passed |
| [`rename()`](#rename) | Rename this path to the target path |
| [`replace()`](#replace) | Rename this path to the target path, overwriting if that path exists |
| [`resolve()`](#resolve) | Make the path absolute, resolving all symlinks on the way and also |
| [`rglob()`](#rglob) | Recursively yield all existing files (of any kind, including |
| [`rmdir()`](#rmdir) | Remove this directory |
| [`samefile()`](#samefile) | Return whether other_path is the same or not as this file |
| [`stat()`](#stat) | Return the result of the stat() system call on this path, like |
| [`symlink_to()`](#symlink_to) | Make this path a symlink pointing to the target path |
| [`touch()`](#touch) | Create this file with the given access mode, if it doesn't exist |
| [`unlink()`](#unlink) | Remove this file or link |
| [`walk()`](#walk) | Walk the directory tree from this directory, similar to os |
| [`with_name()`](#with_name) | Return a new path with the file name changed |
| [`with_segments()`](#with_segments) | Construct a new path object from any number of path-like objects |
| [`with_stem()`](#with_stem) | Return a new path with the stem changed |
| [`with_suffix()`](#with_suffix) | Return a new path with the file suffix changed |
| [`write_bytes()`](#write_bytes) | Open the file in bytes mode, write to it, and close the file |
| [`write_text()`](#write_text) | Open the file in text mode, write to it, and close the file |


#### absolute()

```python
def absolute()
```
Return an absolute version of this path by prepending the current
working directory. No normalization or symlink resolution is performed.

Use resolve() to get the canonical path to a file.


#### as_posix()

```python
def as_posix()
```
Return the string representation of the path with forward (/)
slashes.


#### as_uri()

```python
def as_uri()
```
Return the path as a 'file' URI.


#### chmod()

```python
def chmod(
    mode,
    follow_symlinks,
):
```
Change the permissions of the path, like os.chmod().


| Parameter | Type |
|-|-|
| `mode` |  |
| `follow_symlinks` |  |

#### cwd()

```python
def cwd()
```
Return a new path pointing to the current working directory.


#### exists()

```python
def exists(
    follow_symlinks,
):
```
Whether this path exists.

This method normally follows symlinks; to check whether a symlink exists,
add the argument follow_symlinks=False.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### expanduser()

```python
def expanduser()
```
Return a new path with expanded ~ and ~user constructs
(as returned by os.path.expanduser)


#### glob()

```python
def glob(
    pattern,
    case_sensitive,
):
```
Iterate over this subtree and yield all existing files (of any
kind, including directories) matching the given relative pattern.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### group()

```python
def group()
```
Return the group name of the file gid.


#### hardlink_to()

```python
def hardlink_to(
    target,
):
```
Make this path a hard link pointing to the same file as *target*.

Note the order of arguments (self, target) is the reverse of os.link's.


| Parameter | Type |
|-|-|
| `target` |  |

#### home()

```python
def home()
```
Return a new path pointing to the user's home directory (as
returned by os.path.expanduser('~')).


#### is_absolute()

```python
def is_absolute()
```
True if the path is absolute (has both a root and, if applicable,
a drive).


#### is_block_device()

```python
def is_block_device()
```
Whether this path is a block device.


#### is_char_device()

```python
def is_char_device()
```
Whether this path is a character device.


#### is_dir()

```python
def is_dir()
```
Whether this path is a directory.


#### is_fifo()

```python
def is_fifo()
```
Whether this path is a FIFO.


#### is_file()

```python
def is_file()
```
Whether this path is a regular file (also True for symlinks pointing
to regular files).


#### is_junction()

```python
def is_junction()
```
Whether this path is a junction.


#### is_mount()

```python
def is_mount()
```
Check if this path is a mount point


#### is_relative_to()

```python
def is_relative_to(
    other,
    _deprecated,
):
```
Return True if the path is relative to another path or False.



| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |

#### is_reserved()

```python
def is_reserved()
```
Return True if the path contains one of the special names reserved
by the system, if any.


#### is_socket()

```python
def is_socket()
```
Whether this path is a socket.


#### is_symlink()

```python
def is_symlink()
```
Whether this path is a symbolic link.


#### iterdir()

```python
def iterdir()
```
Yield path objects of the directory contents.

The children are yielded in arbitrary order, and the
special entries '.' and '..' are not included.


#### joinpath()

```python
def joinpath(
    pathsegments,
):
```
Combine this path with one or several arguments, and return a
new path representing either a subpath (if all arguments are relative
paths) or a totally different path (if one of the arguments is
anchored).


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### lchmod()

```python
def lchmod(
    mode,
):
```
Like chmod(), except if the path points to a symlink, the symlink's
permissions are changed, rather than its target's.


| Parameter | Type |
|-|-|
| `mode` |  |

#### lstat()

```python
def lstat()
```
Like stat(), except if the path points to a symlink, the symlink's
status information is returned, rather than its target's.


#### match()

```python
def match(
    path_pattern,
    case_sensitive,
):
```
Return True if this path matches the given pattern.


| Parameter | Type |
|-|-|
| `path_pattern` |  |
| `case_sensitive` |  |

#### mkdir()

```python
def mkdir(
    mode,
    parents,
    exist_ok,
):
```
Create a new directory at this given path.


| Parameter | Type |
|-|-|
| `mode` |  |
| `parents` |  |
| `exist_ok` |  |

#### open()

```python
def open(
    mode,
    buffering,
    encoding,
    errors,
    newline,
):
```
Open the file pointed to by this path and return a file object, as
the built-in open() function does.


| Parameter | Type |
|-|-|
| `mode` |  |
| `buffering` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

#### owner()

```python
def owner()
```
Return the login name of the file owner.


#### read_bytes()

```python
def read_bytes()
```
Open the file in bytes mode, read it, and close the file.


#### read_text()

```python
def read_text(
    encoding,
    errors,
):
```
Open the file in text mode, read it, and close the file.


| Parameter | Type |
|-|-|
| `encoding` |  |
| `errors` |  |

#### readlink()

```python
def readlink()
```
Return the path to which the symbolic link points.


#### relative_to()

```python
def relative_to(
    other,
    _deprecated,
    walk_up,
):
```
Return the relative path to another path identified by the passed
arguments.  If the operation is not possible (because this is not
related to the other path), raise ValueError.

The *walk_up* parameter controls whether `..` may be used to resolve
the path.


| Parameter | Type |
|-|-|
| `other` |  |
| `_deprecated` |  |
| `walk_up` |  |

#### rename()

```python
def rename(
    target,
):
```
Rename this path to the target path.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### replace()

```python
def replace(
    target,
):
```
Rename this path to the target path, overwriting if that path exists.

The target path may be absolute or relative. Relative paths are
interpreted relative to the current working directory, *not* the
directory of the Path object.

Returns the new Path instance pointing to the target path.


| Parameter | Type |
|-|-|
| `target` |  |

#### resolve()

```python
def resolve(
    strict,
):
```
Make the path absolute, resolving all symlinks on the way and also
normalizing it.


| Parameter | Type |
|-|-|
| `strict` |  |

#### rglob()

```python
def rglob(
    pattern,
    case_sensitive,
):
```
Recursively yield all existing files (of any kind, including
directories) matching the given relative pattern, anywhere in
this subtree.


| Parameter | Type |
|-|-|
| `pattern` |  |
| `case_sensitive` |  |

#### rmdir()

```python
def rmdir()
```
Remove this directory.  The directory must be empty.


#### samefile()

```python
def samefile(
    other_path,
):
```
Return whether other_path is the same or not as this file
(as returned by os.path.samefile()).


| Parameter | Type |
|-|-|
| `other_path` |  |

#### stat()

```python
def stat(
    follow_symlinks,
):
```
Return the result of the stat() system call on this path, like
os.stat() does.


| Parameter | Type |
|-|-|
| `follow_symlinks` |  |

#### symlink_to()

```python
def symlink_to(
    target,
    target_is_directory,
):
```
Make this path a symlink pointing to the target path.
Note the order of arguments (link, target) is the reverse of os.symlink.


| Parameter | Type |
|-|-|
| `target` |  |
| `target_is_directory` |  |

#### touch()

```python
def touch(
    mode,
    exist_ok,
):
```
Create this file with the given access mode, if it doesn't exist.


| Parameter | Type |
|-|-|
| `mode` |  |
| `exist_ok` |  |

#### unlink()

```python
def unlink(
    missing_ok,
):
```
Remove this file or link.
If the path is a directory, use rmdir() instead.


| Parameter | Type |
|-|-|
| `missing_ok` |  |

#### walk()

```python
def walk(
    top_down,
    on_error,
    follow_symlinks,
):
```
Walk the directory tree from this directory, similar to os.walk().


| Parameter | Type |
|-|-|
| `top_down` |  |
| `on_error` |  |
| `follow_symlinks` |  |

#### with_name()

```python
def with_name(
    name,
):
```
Return a new path with the file name changed.


| Parameter | Type |
|-|-|
| `name` |  |

#### with_segments()

```python
def with_segments(
    pathsegments,
):
```
Construct a new path object from any number of path-like objects.
Subclasses may override this method to customize how new path objects
are created from methods like `iterdir()`.


| Parameter | Type |
|-|-|
| `pathsegments` |  |

#### with_stem()

```python
def with_stem(
    stem,
):
```
Return a new path with the stem changed.


| Parameter | Type |
|-|-|
| `stem` |  |

#### with_suffix()

```python
def with_suffix(
    suffix,
):
```
Return a new path with the file suffix changed.  If the path
has no suffix, add given suffix.  If the given suffix is an empty
string, remove the suffix from the path.


| Parameter | Type |
|-|-|
| `suffix` |  |

#### write_bytes()

```python
def write_bytes(
    data,
):
```
Open the file in bytes mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |

#### write_text()

```python
def write_text(
    data,
    encoding,
    errors,
    newline,
):
```
Open the file in text mode, write to it, and close the file.


| Parameter | Type |
|-|-|
| `data` |  |
| `encoding` |  |
| `errors` |  |
| `newline` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| anchor |  |  |
| drive |  |  |
| name |  |  |
| parent |  |  |
| parents |  |  |
| parts |  |  |
| root |  |  |
| stem |  |  |
| suffix |  |  |
| suffixes |  |  |

## flytekit.types.structured.basic_dfs.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
def StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `dataframe` | `typing.Optional[typing.Any]` |
| `uri` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) | None |
| [`column_names()`](#column_names) | None |
| [`columns()`](#columns) | None |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`iter()`](#iter) | None |
| [`open()`](#open) | None |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) | None |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### all()

```python
def all()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

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

#### iter()

```python
def iter()
```
#### open()

```python
def open(
    dataframe_type: Type[DF],
):
```
| Parameter | Type |
|-|-|
| `dataframe_type` | `Type[DF]` |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
):
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `expected` | `LiteralType` |

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

### Properties

| Property | Type | Description |
|-|-|-|
| dataframe |  |  |
| literal |  |  |
| metadata |  |  |

## flytekit.types.structured.basic_dfs.StructuredDatasetDecoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def StructuredDatasetDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
):
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



| Parameter | Type |
|-|-|
| `python_type` | `Type[DF]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |
| `additional_protocols` | `Optional[List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal |


#### decode()

```python
def decode(
    ctx: FlyteContext,
    flyte_value: literals.StructuredDataset,
    current_task_metadata: StructuredDatasetMetadata,
):
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `flyte_value` | `literals.StructuredDataset` |
| `current_task_metadata` | `StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.StructuredDatasetEncoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
def StructuredDatasetEncoder(
    python_type: Type[T],
    protocol: Optional[str],
    supported_format: Optional[str],
):
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the |


#### encode()

```python
def encode(
    ctx: FlyteContext,
    structured_dataset: StructuredDataset,
    structured_dataset_type: StructuredDatasetType,
):
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `structured_dataset` | `StructuredDataset` |
| `structured_dataset_type` | `StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| protocol |  |  |
| python_type |  |  |
| supported_format |  |  |

## flytekit.types.structured.basic_dfs.StructuredDatasetMetadata

```python
def StructuredDatasetMetadata(
    structured_dataset_type: typing.Optional[flytekit.models.types.StructuredDatasetType],
):
```
| Parameter | Type |
|-|-|
| `structured_dataset_type` | `typing.Optional[flytekit.models.types.StructuredDatasetType]` |

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
    pb2_object: flyteidl.core.literals_pb2.StructuredDatasetMetadata,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.StructuredDatasetMetadata` |

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
| structured_dataset_type |  |  |

## flytekit.types.structured.basic_dfs.StructuredDatasetType

```python
def StructuredDatasetType(
    columns: typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn],
    format: str,
    external_schema_type: str,
    external_schema_bytes: bytes,
):
```
| Parameter | Type |
|-|-|
| `columns` | `typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn]` |
| `format` | `str` |
| `external_schema_type` | `str` |
| `external_schema_bytes` | `bytes` |

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
    proto: flyteidl.core.types_pb2.StructuredDatasetType,
):
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.types_pb2.StructuredDatasetType` |

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
| columns |  |  |
| external_schema_bytes |  |  |
| external_schema_type |  |  |
| format |  |  |
| is_empty |  |  |

## flytekit.types.structured.basic_dfs.TypeVar

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


