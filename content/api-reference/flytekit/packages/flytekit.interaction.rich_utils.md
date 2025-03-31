---
title: flytekit.interaction.rich_utils
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.interaction.rich_utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`Callback`](.././flytekit.interaction.rich_utils#flytekitinteractionrich_utilscallback) | Base class and interface for callback mechanism. |
| [`Progress`](.././flytekit.interaction.rich_utils#flytekitinteractionrich_utilsprogress) | Renders an auto-updating progress bar(s). |
| [`RichCallback`](.././flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) | Base class and interface for callback mechanism. |

## flytekit.interaction.rich_utils.Callback

Base class and interface for callback mechanism

This class can be used directly for monitoring file transfers by
providing ``callback=Callback(hooks=...)`` (see the ``hooks`` argument,
below), or subclassed for more specialised behaviour.

Parameters
----------
size: int (optional)
Nominal quantity for the value that corresponds to a complete
transfer, e.g., total number of tiles or total number of
bytes
value: int (0)
Starting internal counter value
hooks: dict or None
A dict of named functions to be called on each update. The signature
of these must be ``f(size, value, **kwargs)``


```python
class Callback(
    size,
    value,
    hooks,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `size` |  |
| `value` |  |
| `hooks` |  |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute_update()`](#absolute_update) | Set the internal value state. |
| [`as_callback()`](#as_callback) | Transform callback=. |
| [`branch()`](#branch) | Set callbacks for child transfers. |
| [`branch_coro()`](#branch_coro) | Wraps a coroutine, and pass a new child callback to it. |
| [`branched()`](#branched) | Return callback for child transfers. |
| [`call()`](#call) | Execute hook(s) with current state. |
| [`close()`](#close) | Close callback. |
| [`no_op()`](#no_op) |  |
| [`relative_update()`](#relative_update) | Delta increment the internal counter. |
| [`set_size()`](#set_size) | Set the internal maximum size attribute. |
| [`wrap()`](#wrap) | Wrap an iterable to call ``relative_update`` on each iterations. |


#### absolute_update()

```python
def absolute_update(
    value,
)
```
Set the internal value state

Triggers ``call()``

Parameters
----------
value: int


| Parameter | Type |
|-|-|
| `value` |  |

#### as_callback()

```python
def as_callback(
    maybe_callback,
)
```
Transform callback=... into Callback instance

For the special value of ``None``, return the global instance of
``NoOpCallback``. This is an alternative to including
``callback=DEFAULT_CALLBACK`` directly in a method signature.


| Parameter | Type |
|-|-|
| `maybe_callback` |  |

#### branch()

```python
def branch(
    path_1,
    path_2,
    kwargs,
)
```
Set callbacks for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The passed kwargs are
to be *mutated* to add ``callback=``, if this class supports branching
to children.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
kwargs: dict
arguments passed to child method, e.g., put_file.

Returns
-------


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### branch_coro()

```python
def branch_coro(
    fn,
)
```
Wraps a coroutine, and pass a new child callback to it.


| Parameter | Type |
|-|-|
| `fn` |  |

#### branched()

```python
def branched(
    path_1,
    path_2,
    kwargs,
)
```
Return callback for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The function returns a callback
that has to be passed to the child method, e.g., put_file,
as `callback=` argument.

The implementation uses `callback.branch` for compatibility.
When implementing callbacks, it is recommended to override this function instead
of `branch` and avoid calling `super().branched(...)`.

Prefer using this function over `branch`.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
**kwargs:
Arbitrary keyword arguments

Returns
-------
callback: Callback
A callback instance to be passed to the child method


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### call()

```python
def call(
    hook_name,
    kwargs,
)
```
Execute hook(s) with current state

Each function is passed the internal size and current value

Parameters
----------
hook_name: str or None
If given, execute on this hook
kwargs: passed on to (all) hook(s)


| Parameter | Type |
|-|-|
| `hook_name` |  |
| `kwargs` | ``**kwargs`` |

#### close()

```python
def close()
```
Close callback.


#### no_op()

```python
def no_op(
    _,
    __,
)
```
| Parameter | Type |
|-|-|
| `_` |  |
| `__` |  |

#### relative_update()

```python
def relative_update(
    inc,
)
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type |
|-|-|
| `inc` |  |

#### set_size()

```python
def set_size(
    size,
)
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type |
|-|-|
| `size` |  |

#### wrap()

```python
def wrap(
    iterable,
)
```
Wrap an iterable to call ``relative_update`` on each iterations

Parameters
----------
iterable: Iterable
The iterable that is being wrapped


| Parameter | Type |
|-|-|
| `iterable` |  |

## flytekit.interaction.rich_utils.Progress

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

## flytekit.interaction.rich_utils.RichCallback

Base class and interface for callback mechanism

This class can be used directly for monitoring file transfers by
providing ``callback=Callback(hooks=...)`` (see the ``hooks`` argument,
below), or subclassed for more specialised behaviour.

Parameters
----------
size: int (optional)
Nominal quantity for the value that corresponds to a complete
transfer, e.g., total number of tiles or total number of
bytes
value: int (0)
Starting internal counter value
hooks: dict or None
A dict of named functions to be called on each update. The signature
of these must be ``f(size, value, **kwargs)``


```python
class RichCallback(
    rich_kwargs: typing.Optional[typing.Dict],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `rich_kwargs` | `typing.Optional[typing.Dict]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`absolute_update()`](#absolute_update) | Set the internal value state. |
| [`as_callback()`](#as_callback) | Transform callback=. |
| [`branch()`](#branch) | Set callbacks for child transfers. |
| [`branch_coro()`](#branch_coro) | Wraps a coroutine, and pass a new child callback to it. |
| [`branched()`](#branched) | Return callback for child transfers. |
| [`call()`](#call) | Execute hook(s) with current state. |
| [`close()`](#close) | Close callback. |
| [`no_op()`](#no_op) |  |
| [`relative_update()`](#relative_update) | Delta increment the internal counter. |
| [`set_size()`](#set_size) | Set the internal maximum size attribute. |
| [`wrap()`](#wrap) | Wrap an iterable to call ``relative_update`` on each iterations. |


#### absolute_update()

```python
def absolute_update(
    value,
)
```
Set the internal value state

Triggers ``call()``

Parameters
----------
value: int


| Parameter | Type |
|-|-|
| `value` |  |

#### as_callback()

```python
def as_callback(
    maybe_callback,
)
```
Transform callback=... into Callback instance

For the special value of ``None``, return the global instance of
``NoOpCallback``. This is an alternative to including
``callback=DEFAULT_CALLBACK`` directly in a method signature.


| Parameter | Type |
|-|-|
| `maybe_callback` |  |

#### branch()

```python
def branch(
    path_1,
    path_2,
    kwargs,
)
```
Set callbacks for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The passed kwargs are
to be *mutated* to add ``callback=``, if this class supports branching
to children.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
kwargs: dict
arguments passed to child method, e.g., put_file.

Returns
-------


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### branch_coro()

```python
def branch_coro(
    fn,
)
```
Wraps a coroutine, and pass a new child callback to it.


| Parameter | Type |
|-|-|
| `fn` |  |

#### branched()

```python
def branched(
    path_1,
    path_2,
    kwargs,
)
```
Return callback for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The function returns a callback
that has to be passed to the child method, e.g., put_file,
as `callback=` argument.

The implementation uses `callback.branch` for compatibility.
When implementing callbacks, it is recommended to override this function instead
of `branch` and avoid calling `super().branched(...)`.

Prefer using this function over `branch`.

Parameters
----------
path_1: str
Child's source path
path_2: str
Child's destination path
**kwargs:
Arbitrary keyword arguments

Returns
-------
callback: Callback
A callback instance to be passed to the child method


| Parameter | Type |
|-|-|
| `path_1` |  |
| `path_2` |  |
| `kwargs` | ``**kwargs`` |

#### call()

```python
def call(
    hook_name,
    kwargs,
)
```
Execute hook(s) with current state

Each function is passed the internal size and current value

Parameters
----------
hook_name: str or None
If given, execute on this hook
kwargs: passed on to (all) hook(s)


| Parameter | Type |
|-|-|
| `hook_name` |  |
| `kwargs` | ``**kwargs`` |

#### close()

```python
def close()
```
Close callback.


#### no_op()

```python
def no_op(
    _,
    __,
)
```
| Parameter | Type |
|-|-|
| `_` |  |
| `__` |  |

#### relative_update()

```python
def relative_update(
    inc,
)
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type |
|-|-|
| `inc` |  |

#### set_size()

```python
def set_size(
    size,
)
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type |
|-|-|
| `size` |  |

#### wrap()

```python
def wrap(
    iterable,
)
```
Wrap an iterable to call ``relative_update`` on each iterations

Parameters
----------
iterable: Iterable
The iterable that is being wrapped


| Parameter | Type |
|-|-|
| `iterable` |  |

