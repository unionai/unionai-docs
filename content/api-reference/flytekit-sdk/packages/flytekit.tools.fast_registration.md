---
title: flytekit.tools.fast_registration
version: 1.15.4.dev2+g3e3ce2426
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

* [`FlyteDataNotFoundException`](.././flytekit.tools.fast_registration#flytekittoolsfast_registrationflytedatanotfoundexception)

## flytekit.tools.fast_registration.BarColumn

Renders a visual progress bar.



```python
def BarColumn(
    bar_width: typing.Optional[int],
    style: typing.Union[str, ForwardRef('Style')],
    complete_style: typing.Union[str, ForwardRef('Style')],
    finished_style: typing.Union[str, ForwardRef('Style')],
    pulse_style: typing.Union[str, ForwardRef('Style')],
    table_column: typing.Optional[rich.table.Column],
):
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
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table |
| [`render()`](#render) | Gets a progress bar widget for a task |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
):
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
def DockerIgnore(
    root: pathlib.Path,
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.FastPackageOptions

FastPackageOptions is used to set configuration options when packaging files.


```python
def FastPackageOptions(
    ignores: list[Ignore],
    keep_default_ignores: bool,
    copy_style: Optional[CopyFileDetection],
    show_files: bool,
):
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

## flytekit.tools.fast_registration.FlyteDataNotFoundException

Inappropriate argument value (of correct type).


```python
def FlyteDataNotFoundException(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

### Properties

| Property | Type | Description |
|-|-|-|
| timestamp |  |  |

## flytekit.tools.fast_registration.FlyteIgnore

Uses a .flyteignore file to determine ignored files.


```python
def FlyteIgnore(
    root: pathlib.Path,
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.GitIgnore

Uses git cli (if available) to list all ignored files and compare with those.


```python
def GitIgnore(
    root: pathlib.Path,
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.Ignore

Base for Ignores, implements core logic. Children have to implement _is_ignored


```python
def Ignore(
    root: str,
):
```
| Parameter | Type |
|-|-|
| `root` | `str` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.IgnoreGroup

Groups multiple Ignores and checks a path against them. A file is ignored if any
Ignore considers it ignored.


```python
def IgnoreGroup(
    root: str,
    ignores: typing.List[typing.Type[flytekit.tools.ignore.Ignore]],
):
```
| Parameter | Type |
|-|-|
| `root` | `str` |
| `ignores` | `typing.List[typing.Type[flytekit.tools.ignore.Ignore]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`list_ignored()`](#list_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
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
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.Progress

Renders an auto-updating progress bar(s).



```python
def Progress(
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
):
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
| [`add_task()`](#add_task) | Add a new 'task' to the Progress display |
| [`advance()`](#advance) | Advance task by a number of steps |
| [`get_default_columns()`](#get_default_columns) | Get the default columns used for a new Progress instance: |
| [`get_renderable()`](#get_renderable) | Get a renderable for the progress display |
| [`get_renderables()`](#get_renderables) | Get a number of renderables for the progress display |
| [`make_tasks_table()`](#make_tasks_table) | Get a table to render the Progress display |
| [`open()`](#open) | Track progress while reading from a binary file |
| [`refresh()`](#refresh) | Refresh (render) the progress information |
| [`remove_task()`](#remove_task) | Delete a task if it exists |
| [`reset()`](#reset) | Reset a task so completed is 0 and the clock is reset |
| [`start()`](#start) | Start the progress display |
| [`start_task()`](#start_task) | Start a task |
| [`stop()`](#stop) | Stop the progress display |
| [`stop_task()`](#stop_task) | Stop a task |
| [`track()`](#track) | Track progress by iterating over a sequence |
| [`update()`](#update) | Update information associated with a task |
| [`wrap_file()`](#wrap_file) | Track progress file reading from a binary file |


#### add_task()

```python
def add_task(
    description: str,
    start: bool,
    total: typing.Optional[float],
    completed: int,
    visible: bool,
    fields: typing.Any,
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
| console |  |  |
| finished |  |  |
| task_ids |  |  |
| tasks |  |  |

## flytekit.tools.fast_registration.StandardIgnore

Retains the standard ignore functionality that previously existed. Could in theory
by fed with custom ignore patterns from cli.


```python
def StandardIgnore(
    root: pathlib.Path,
    patterns: typing.Optional[typing.List[str]],
):
```
| Parameter | Type |
|-|-|
| `root` | `pathlib.Path` |
| `patterns` | `typing.Optional[typing.List[str]]` |

### Methods

| Method | Description |
|-|-|
| [`is_ignored()`](#is_ignored) | None |
| [`tar_filter()`](#tar_filter) | None |


#### is_ignored()

```python
def is_ignored(
    path: str,
):
```
| Parameter | Type |
|-|-|
| `path` | `str` |

#### tar_filter()

```python
def tar_filter(
    tarinfo: tarfile.TarInfo,
):
```
| Parameter | Type |
|-|-|
| `tarinfo` | `tarfile.TarInfo` |

## flytekit.tools.fast_registration.TextColumn

A column containing text.


```python
def TextColumn(
    text_format: str,
    style: typing.Union[str, ForwardRef('Style')],
    justify: typing.Literal['default', 'left', 'center', 'right', 'full'],
    markup: bool,
    highlighter: typing.Optional[rich.highlighter.Highlighter],
    table_column: typing.Optional[rich.table.Column],
):
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
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table |
| [`render()`](#render) | Should return a renderable object |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
):
```
Should return a renderable object.


| Parameter | Type |
|-|-|
| `task` | `Task` |

## flytekit.tools.fast_registration.TimeElapsedColumn

Renders time elapsed.


```python
def TimeElapsedColumn(
    table_column: typing.Optional[rich.table.Column],
):
```
| Parameter | Type |
|-|-|
| `table_column` | `typing.Optional[rich.table.Column]` |

### Methods

| Method | Description |
|-|-|
| [`get_table_column()`](#get_table_column) | Get a table column, used to build tasks table |
| [`render()`](#render) | Show time elapsed |


#### get_table_column()

```python
def get_table_column()
```
Get a table column, used to build tasks table.


#### render()

```python
def render(
    task: Task,
):
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
def Tree(
    label: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    style: typing.Union[str, ForwardRef('Style')],
    guide_style: typing.Union[str, ForwardRef('Style')],
    expanded: bool,
    highlight: bool,
    hide_root: bool,
):
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
| [`add()`](#add) | Add a child tree |


#### add()

```python
def add(
    label: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    style: typing.Union[str, ForwardRef('Style'), NoneType],
    guide_style: typing.Union[str, ForwardRef('Style'), NoneType],
    expanded: bool,
    highlight: typing.Optional[bool],
):
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
def timeit(
    name: str,
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |

