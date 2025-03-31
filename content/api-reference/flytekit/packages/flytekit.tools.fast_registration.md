---
title: flytekit.tools.fast_registration
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.tools.fast_registration

## Directory

### Classes

| Class | Description |
|-|-|
| [`BarColumn`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationbarcolumn) | Renders a visual progress bar. |
| [`CopyFileDetection`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationcopyfiledetection) | Create a collection of name/value pairs. |
| [`DockerIgnore`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationdockerignore) | Uses docker-py's PatternMatcher to check whether a path is ignored. |
| [`FastPackageOptions`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationfastpackageoptions) | FastPackageOptions is used to set configuration options when packaging files. |
| [`FlyteContextManager`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationflytecontextmanager) | FlyteContextManager manages the execution context within Flytekit. |
| [`FlyteIgnore`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationflyteignore) | Uses a . |
| [`GitIgnore`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationgitignore) | Uses git cli (if available) to list all ignored files and compare with those. |
| [`Ignore`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationignore) | Base for Ignores, implements core logic. |
| [`IgnoreGroup`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationignoregroup) | Groups multiple Ignores and checks a path against them. |
| [`Progress`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationprogress) | Renders an auto-updating progress bar(s). |
| [`StandardIgnore`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationstandardignore) | Retains the standard ignore functionality that previously existed. |
| [`TextColumn`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationtextcolumn) | A column containing text. |
| [`TimeElapsedColumn`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationtimeelapsedcolumn) | Renders time elapsed. |
| [`Tree`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationtree) | A renderable for a tree structure. |
| [`timeit`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationtimeit) | A context manager and a decorator that measures the execution time of the wrapped code block or functions. |

### Errors

| Exception | Description |
|-|-|
| [`FlyteDataNotFoundException`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationflytedatanotfoundexception) | Inappropriate argument value (of correct type). |

### Methods

| Method | Description |
|-|-|
| [`_filehash_update()`](#_filehash_update) |  |
| [`_pathhash_update()`](#_pathhash_update) |  |
| [`compress_tarball()`](#compress_tarball) | Compress code tarball using pigz if available, otherwise gzip. |
| [`compute_digest()`](#compute_digest) | Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`download_distribution()`](#download_distribution) | Downloads a remote code distribution and overwrites any local files. |
| [`fast_package()`](#fast_package) | Takes a source directory and packages everything not covered by common ignores into a tarball. |
| [`get_additional_distribution_loc()`](#get_additional_distribution_loc) | . |
| [`is_display_progress_enabled()`](#is_display_progress_enabled) |  |
| [`ls_files()`](#ls_files) | user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the. |
| [`print_ls_tree()`](#print_ls_tree) |  |
| [`rich_print()`](#rich_print) | Print object(s) supplied via positional arguments. |
| [`tar_strip_file_attributes()`](#tar_strip_file_attributes) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `FAST_FILEENDING` | `str` |  |
| `FAST_PREFIX` | `str` |  |
| `PICKLE_FILE_PATH` | `str` |  |
| `annotations` | `_Feature` |  |
| `logger` | `Logger` |  |

## Methods

#### _filehash_update()

```python
def _filehash_update(
    path: Union[os.PathLike, str],
    hasher: hashlib._Hash,
)
```
| Parameter | Type |
|-|-|
| `path` | `Union[os.PathLike, str]` |
| `hasher` | `hashlib._Hash` |

#### _pathhash_update()

```python
def _pathhash_update(
    path: Union[os.PathLike, str],
    hasher: hashlib._Hash,
)
```
| Parameter | Type |
|-|-|
| `path` | `Union[os.PathLike, str]` |
| `hasher` | `hashlib._Hash` |

#### compress_tarball()

```python
def compress_tarball(
    source: os.PathLike,
    output: os.PathLike,
)
```
Compress code tarball using pigz if available, otherwise gzip


| Parameter | Type |
|-|-|
| `source` | `os.PathLike` |
| `output` | `os.PathLike` |

#### compute_digest()

```python
def compute_digest(
    source: Union[os.PathLike, List[os.PathLike]],
    filter: Optional[callable],
) -> str
```
Walks the entirety of the source dir to compute a deterministic md5 hex digest of the dir contents.


| Parameter | Type |
|-|-|
| `source` | `Union[os.PathLike, List[os.PathLike]]` |
| `filter` | `Optional[callable]` |

#### dataclass()

```python
def dataclass(
    cls,
    init,
    repr,
    eq,
    order,
    unsafe_hash,
    frozen,
    match_args,
    kw_only,
    slots,
    weakref_slot,
)
```
Add dunder methods based on the fields defined in the class.

Examines PEP 526 __annotations__ to determine fields.

If init is true, an __init__() method is added to the class. If repr
is true, a __repr__() method is added. If order is true, rich
comparison dunder methods are added. If unsafe_hash is true, a
__hash__() method is added. If frozen is true, fields may not be
assigned to after instance creation. If match_args is true, the
__match_args__ tuple is added. If kw_only is true, then by default
all fields are keyword-only. If slots is true, a new class with a
__slots__ attribute is returned.


| Parameter | Type |
|-|-|
| `cls` |  |
| `init` |  |
| `repr` |  |
| `eq` |  |
| `order` |  |
| `unsafe_hash` |  |
| `frozen` |  |
| `match_args` |  |
| `kw_only` |  |
| `slots` |  |
| `weakref_slot` |  |

#### download_distribution()

```python
def download_distribution(
    additional_distribution: str,
    destination: str,
)
```
Downloads a remote code distribution and overwrites any local files.


| Parameter | Type |
|-|-|
| `additional_distribution` | `str` |
| `destination` | `str` |

#### fast_package()

```python
def fast_package(
    source: os.PathLike,
    output_dir: os.PathLike,
    deref_symlinks: bool,
    options: Optional[FastPackageOptions],
) -> os.PathLike
```
Takes a source directory and packages everything not covered by common ignores into a tarball
named after a hexdigest of the included files.


| Parameter | Type |
|-|-|
| `source` | `os.PathLike` |
| `output_dir` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `options` | `Optional[FastPackageOptions]` |

#### get_additional_distribution_loc()

```python
def get_additional_distribution_loc(
    remote_location: str,
    identifier: str,
) -> str
```
| Parameter | Type |
|-|-|
| `remote_location` | `str` |
| `identifier` | `str` |

#### is_display_progress_enabled()

```python
def is_display_progress_enabled()
```
#### ls_files()

```python
def ls_files(
    source_path: str,
    copy_file_detection: CopyFileDetection,
    deref_symlinks: bool,
    ignore_group: Optional[IgnoreGroup],
) -> Tuple[List[str], str]
```
user_modules_and_packages is a list of the Python modules and packages, expressed as absolute paths, that the
user has run this pyflyte command with. For pyflyte run for instance, this is just a list of one.
This is used for two reasons.
- Everything in this list needs to be returned. Files are returned and folders are walked.
- A common source path is derived from this is, which is just the common folder that contains everything in the
list. For ex. if you do
$ pyflyte --pkgs a.b,a.c package
Then the common root is just the folder a/. The modules list is filtered against this root. Only files
representing modules under this root are included

If the copy enum is set to loaded_modules, then the loaded sys modules will be used.


| Parameter | Type |
|-|-|
| `source_path` | `str` |
| `copy_file_detection` | `CopyFileDetection` |
| `deref_symlinks` | `bool` |
| `ignore_group` | `Optional[IgnoreGroup]` |

#### print_ls_tree()

```python
def print_ls_tree(
    source: os.PathLike,
    ls: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `source` | `os.PathLike` |
| `ls` | `typing.List[str]` |

#### rich_print()

```python
def rich_print(
    objects: typing.Any,
    sep: str,
    end: str,
    file: typing.Optional[typing.IO[str]],
    flush: bool,
)
```
Print object(s) supplied via positional arguments.
This function has an identical signature to the built-in print.
For more advanced features, see the :class:`~rich.console.Console` class.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `file` | `typing.Optional[typing.IO[str]]` |
| `flush` | `bool` |

#### tar_strip_file_attributes()

```python
def tar_strip_file_attributes(
    tar_info: tarfile.TarInfo,
) -> tarfile.TarInfo
```
| Parameter | Type |
|-|-|
| `tar_info` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.BarColumn

Renders a visual progress bar.



```python
class BarColumn(
    bar_width: typing.Optional[int],
    style: typing.Union[str, ForwardRef('Style')],
    complete_style: typing.Union[str, ForwardRef('Style')],
    finished_style: typing.Union[str, ForwardRef('Style')],
    pulse_style: typing.Union[str, ForwardRef('Style')],
    table_column: typing.Optional[rich.table.Column],
)
```
| Parameter | Type |
|-|-|
| `bar_width` | `typing.Optional[int]` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `complete_style` | `typing.Union[str, ForwardRef('Style')]` |
| `finished_style` | `typing.Union[str, ForwardRef('Style')]` |
| `pulse_style` | `typing.Union[str, ForwardRef('Style')]` |
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table. |
| [`render()`](#render) | Gets a progress bar widget for a task. |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
) -> rich.progress_bar.ProgressBar
```
Gets a progress bar widget for a task.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.tools.fast_registration.CopyFileDetection

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


## flytekit.tools.fast_registration.DockerIgnore

Uses docker-py's PatternMatcher to check whether a path is ignored.


```python
class DockerIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.FastPackageOptions

FastPackageOptions is used to set configuration options when packaging files.


```python
class FastPackageOptions(
    ignores: list[Ignore],
    keep_default_ignores: bool,
    copy_style: Optional[CopyFileDetection],
    show_files: bool,
)
```
| Parameter | Type |
|-|-|
| `ignores` | `list[Ignore]` |
| `keep_default_ignores` | `bool` |
| `copy_style` | `Optional[CopyFileDetection]` |
| `show_files` | `bool` |

## flytekit.tools.fast_registration.FlyteContextManager

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
| [`add_signal_handler()`](#add_signal_handler) |  |
| [`current_context()`](#current_context) |  |
| [`get_origin_stackframe()`](#get_origin_stackframe) |  |
| [`initialize()`](#initialize) | Re-initializes the context and erases the entire context. |
| [`pop_context()`](#pop_context) |  |
| [`push_context()`](#push_context) |  |
| [`size()`](#size) |  |
| [`with_context()`](#with_context) |  |


#### add_signal_handler()

```python
def add_signal_handler(
    handler: typing.Callable[[int, FrameType], typing.Any],
)
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
) -> traceback.FrameSummary
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
) -> FlyteContext
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
) -> Generator[FlyteContext, None, None]
```
| Parameter | Type |
|-|-|
| `b` | `FlyteContext.Builder` |

## flytekit.tools.fast_registration.FlyteDataNotFoundException

Inappropriate argument value (of correct type).


```python
class FlyteDataNotFoundException(
    path: str,
)
```
| Parameter | Type |
|-|-|
| `path` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.tools.fast_registration.FlyteIgnore

Uses a .flyteignore file to determine ignored files.


```python
class FlyteIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.GitIgnore

Uses git cli (if available) to list all ignored files and compare with those.


```python
class GitIgnore(
    root: pathlib._local.Path,
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.Ignore

Base for Ignores, implements core logic. Children have to implement _is_ignored


```python
class Ignore(
    root: str,
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.IgnoreGroup

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
class IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
)
```
| Parameter | Type |
|-|-|
| `root` | `str` |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`list_ignored()`](#list_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### list_ignored()

```python
def list_ignored()
```
#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.Progress

Renders an auto-updating progress bar(s).



```python
class Progress(
    columns: typing.Union[str, rich.progress.ProgressColumn],
    console: typing.Optional[rich.console.Console],
    auto_refresh: bool,
    refresh_per_second: float,
    speed_estimate_period: float,
    transient: bool,
    redirect_stdout: bool,
    redirect_stderr: bool,
    get_time: typing.Optional[typing.Callable[[], float]],
    disable: bool,
    expand: bool,
)
```
| Parameter | Type |
|-|-|
| `columns` | `typing.Union[str, rich.progress.ProgressColumn]` |
| `console` | `typing.Optional[rich.console.Console]` |
| `auto_refresh` | `bool` |
| `refresh_per_second` | `float` |
| `speed_estimate_period` | `float` |
| `transient` | `bool` |
| `redirect_stdout` | `bool` |
| `redirect_stderr` | `bool` |
| `get_time` | `typing.Optional[typing.Callable[[], float]]` |
| `disable` | `bool` |
| `expand` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_task()`](#add_task) | Add a new 'task' to the Progress display. |
| [`advance()`](#advance) | Advance task by a number of steps. |
| [`get_default_columns()`](#get_default_columns) | Get the default columns used for a new Progress instance:. |
| [`get_renderable()`](#get_renderable) | Get a renderable for the progress display. |
| [`get_renderables()`](#get_renderables) | Get a number of renderables for the progress display. |
| [`make_tasks_table()`](#make_tasks_table) | Get a table to render the Progress display. |
| [`open()`](#open) | Track progress while reading from a binary file. |
| [`refresh()`](#refresh) | Refresh (render) the progress information. |
| [`remove_task()`](#remove_task) | Delete a task if it exists. |
| [`reset()`](#reset) | Reset a task so completed is 0 and the clock is reset. |
| [`start()`](#start) | Start the progress display. |
| [`start_task()`](#start_task) | Start a task. |
| [`stop()`](#stop) | Stop the progress display. |
| [`stop_task()`](#stop_task) | Stop a task. |
| [`track()`](#track) | Track progress by iterating over a sequence. |
| [`update()`](#update) | Update information associated with a task. |
| [`wrap_file()`](#wrap_file) | Track progress file reading from a binary file. |


#### add_task()

```python
def add_task(
    description: str,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: bool,
    fields: typing.Any,
) -> rich.progress.TaskID
```
Add a new 'task' to the Progress display.



| Parameter | Type |
|-|-|
| `description` | `str` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `bool` |
| `fields` | `typing.Any` |

#### advance()

```python
def advance(
    task_id: rich.progress.TaskID,
    advance: float,
)
```
Advance task by a number of steps.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `advance` | `float` |

#### get_default_columns()

```python
def get_default_columns()
```
Get the default columns used for a new Progress instance:
- a text column for the description (TextColumn)
- the bar itself (BarColumn)
- a text column showing completion percentage (TextColumn)
- an estimated-time-remaining column (TimeRemainingColumn)
If the Progress instance is created without passing a columns argument,
the default columns defined here will be used.

You can also create a Progress instance using custom columns before
and/or after the defaults, as in this example:

progress = Progress(
SpinnerColumn(),
*Progress.get_default_columns(),
"Elapsed:",
TimeElapsedColumn(),
)

This code shows the creation of a Progress display, containing
a spinner to the left, the default columns, and a labeled elapsed
time column.


#### get_renderable()

```python
def get_renderable()
```
Get a renderable for the progress display.


#### get_renderables()

```python
def get_renderables()
```
Get a number of renderables for the progress display.


#### make_tasks_table()

```python
def make_tasks_table(
    tasks: typing.Iterable[rich.progress.Task],
) -> rich.table.Table
```
Get a table to render the Progress display.



| Parameter | Type |
|-|-|
| `tasks` | `typing.Iterable[rich.progress.Task]` |

#### open()

```python
def open(
    file: typing.Union[str, ForwardRef('PathLike[str]'), bytes],
    mode: typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']],
    buffering: int,
    encoding: typing.Optional[str],
    errors: typing.Optional[str],
    newline: typing.Optional[str],
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
) -> typing.Union[typing.BinaryIO, typing.TextIO]
```
Track progress while reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.Union[str, ForwardRef('PathLike[str]'), bytes]` |
| `mode` | `typing.Union[typing.Literal['rb'], typing.Literal['rt'], typing.Literal['r']]` |
| `buffering` | `int` |
| `encoding` | `typing.Optional[str]` |
| `errors` | `typing.Optional[str]` |
| `newline` | `typing.Optional[str]` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

#### refresh()

```python
def refresh()
```
Refresh (render) the progress information.


#### remove_task()

```python
def remove_task(
    task_id: rich.progress.TaskID,
)
```
Delete a task if it exists.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### reset()

```python
def reset(
    task_id: rich.progress.TaskID,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: typing.Optional[bool],
    description: typing.Optional[str],
    fields: typing.Any,
)
```
Reset a task so completed is 0 and the clock is reset.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `start` | `bool` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `visible` | `typing.Optional[bool]` |
| `description` | `typing.Optional[str]` |
| `fields` | `typing.Any` |

#### start()

```python
def start()
```
Start the progress display.


#### start_task()

```python
def start_task(
    task_id: rich.progress.TaskID,
)
```
Start a task.

Starts a task (used when calculating elapsed time). You may need to call this manually,
if you called ``add_task`` with ``start=False``.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### stop()

```python
def stop()
```
Stop the progress display.


#### stop_task()

```python
def stop_task(
    task_id: rich.progress.TaskID,
)
```
Stop a task.

This will freeze the elapsed time on the task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |

#### track()

```python
def track(
    sequence: typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]],
    total: typing.Optional[float],
    completed: int,
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
    update_period: float,
) -> typing.Iterable[~ProgressType]
```
Track progress by iterating over a sequence.



| Parameter | Type |
|-|-|
| `sequence` | `typing.Union[typing.Iterable[~ProgressType], typing.Sequence[~ProgressType]]` |
| `total` | `typing.Optional[float]` |
| `completed` | `int` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |
| `update_period` | `float` |

#### update()

```python
def update(
    task_id: rich.progress.TaskID,
    total: typing.Optional[float],
    completed: typing.Optional[float],
    advance: typing.Optional[float],
    description: typing.Optional[str],
    visible: typing.Optional[bool],
    refresh: bool,
    fields: typing.Any,
)
```
Update information associated with a task.



| Parameter | Type |
|-|-|
| `task_id` | `rich.progress.TaskID` |
| `total` | `typing.Optional[float]` |
| `completed` | `typing.Optional[float]` |
| `advance` | `typing.Optional[float]` |
| `description` | `typing.Optional[str]` |
| `visible` | `typing.Optional[bool]` |
| `refresh` | `bool` |
| `fields` | `typing.Any` |

#### wrap_file()

```python
def wrap_file(
    file: typing.BinaryIO,
    total: typing.Optional[int],
    task_id: typing.Optional[rich.progress.TaskID],
    description: str,
) -> typing.BinaryIO
```
Track progress file reading from a binary file.



| Parameter | Type |
|-|-|
| `file` | `typing.BinaryIO` |
| `total` | `typing.Optional[int]` |
| `task_id` | `typing.Optional[rich.progress.TaskID]` |
| `description` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| `console` |  |  |
| `finished` |  | {{< multiline >}}Check if all tasks have been completed.
{{< /multiline >}} |
| `task_ids` |  | {{< multiline >}}A list of task IDs.
{{< /multiline >}} |
| `tasks` |  | {{< multiline >}}Get a list of Task instances.
{{< /multiline >}} |

## flytekit.tools.fast_registration.StandardIgnore

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
class StandardIgnore(
    root: pathlib._local.Path,
    patterns: typing.Optional[typing.List[str]],
)
```
| Parameter | Type |
|-|-|
| `root` | `pathlib._local.Path` |
| `patterns` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) |  |
| [`tar_filter()`](#tar_filter) |  |


#### is_ignored()

```python
def is_ignored(
    path: str,
) -> bool
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
) -> typing.Optional[tarfile.TarInfo]
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.TextColumn

A column containing text.


```python
class TextColumn(
    text_format: str,
    style: typing.Union[str, ForwardRef('Style')],
    justify: typing.Literal['default', 'left', 'center', 'right', 'full'],
    markup: bool,
    highlighter: typing.Optional[rich.highlighter.Highlighter],
    table_column: typing.Optional[rich.table.Column],
)
```
| Parameter | Type |
|-|-|
| `text_format` | `str` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `justify` | `typing.Literal['default', 'left', 'center', 'right', 'full']` |
| `markup` | `bool` |
| `highlighter` | `typing.Optional[rich.highlighter.Highlighter]` |
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table. |
| [`render()`](#render) | Should return a renderable object. |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
) -> rich.text.Text
```
Should return a renderable object.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.tools.fast_registration.TimeElapsedColumn

Renders time elapsed.


```python
class TimeElapsedColumn(
    table_column: typing.Optional[rich.table.Column],
)
```
| Parameter | Type |
|-|-|
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table. |
| [`render()`](#render) | Show time elapsed. |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
) -> rich.text.Text
```
Show time elapsed.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.tools.fast_registration.Tree

A renderable for a tree structure.

Attributes:
ASCII_GUIDES (GuideType): Guide lines used when Console.ascii_only is True.
TREE_GUIDES (List[GuideType, GuideType, GuideType]): Default guide lines.



```python
class Tree(
    label: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    style: typing.Union[str, ForwardRef('Style')],
    guide_style: typing.Union[str, ForwardRef('Style')],
    expanded: bool,
    highlight: bool,
    hide_root: bool,
)
```
| Parameter | Type |
|-|-|
| `label` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `guide_style` | `typing.Union[str, ForwardRef('Style')]` |
| `expanded` | `bool` |
| `highlight` | `bool` |
| `hide_root` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add()`](#add) | Add a child tree. |


#### add()

```python
def add(
    label: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    style: typing.Union[str, ForwardRef('Style'), NoneType],
    guide_style: typing.Union[str, ForwardRef('Style'), NoneType],
    expanded: bool,
    highlight: typing.Optional[bool],
) -> Tree
```
Add a child tree.



| Parameter | Type |
|-|-|
| `label` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `guide_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `expanded` | `bool` |
| `highlight` | `typing.Optional[bool]` |

## flytekit.tools.fast_registration.timeit

A context manager and a decorator that measures the execution time of the wrapped code block or functions.
It will append a timing information to TimeLineDeck. For instance:

@timeit("Function description")
def function()

with timeit("Wrapped code block description"):
# your code


```python
class timeit(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

