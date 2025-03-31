---
title: flytekit.clis.sdk_in_container.launchplan
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.launchplan

## Directory

### Classes

| Class | Description |
|-|-|
| [`LaunchPlanState`](.././flytekit.clis.sdk_in_container.launchplan#flytekitclissdk_in_containerlaunchplanlaunchplanstate) |  |
| [`Progress`](.././flytekit.clis.sdk_in_container.launchplan#flytekitclissdk_in_containerlaunchplanprogress) | Renders an auto-updating progress bar(s). |

### Methods

| Method | Description |
|-|-|
| [`domain_option_dec()`](#domain_option_dec) |  |
| [`get_and_save_remote_with_click_context()`](#get_and_save_remote_with_click_context) | NB: This function will by default mutate the click Context. |
| [`project_option_dec()`](#project_option_dec) |  |


## Methods

#### domain_option_dec()

```python
def domain_option_dec(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### get_and_save_remote_with_click_context()

```python
def get_and_save_remote_with_click_context(
    ctx: click.core.Context,
    project: str,
    domain: str,
    save: bool,
    data_upload_location: typing.Optional[str],
) -> flytekit.remote.remote.FlyteRemote
```
NB: This function will by default mutate the click Context.obj dictionary, adding a remote key with value
of the created FlyteRemote object.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `project` | `str` |
| `domain` | `str` |
| `save` | `bool` |
| `data_upload_location` | `typing.Optional[str]` |

#### project_option_dec()

```python
def project_option_dec(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

## flytekit.clis.sdk_in_container.launchplan.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    val,
) -> Text
```
| Parameter | Type |
|-|-|
| `val` |  |

## flytekit.clis.sdk_in_container.launchplan.Progress

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

