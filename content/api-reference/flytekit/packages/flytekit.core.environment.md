---
title: flytekit.core.environment
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.environment

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.environment#flytekitcoreenvironmentany) | Special type indicating an unconstrained type. |
| [`Console`](.././flytekit.core.environment#flytekitcoreenvironmentconsole) | A high level console interface. |
| [`Environment`](.././flytekit.core.environment#flytekitcoreenvironmentenvironment) |  |
| [`Panel`](.././flytekit.core.environment#flytekitcoreenvironmentpanel) | A console renderable that draws a border around its contents. |
| [`ParamSpec`](.././flytekit.core.environment#flytekitcoreenvironmentparamspec) | Parameter specification variable. |
| [`Pretty`](.././flytekit.core.environment#flytekitcoreenvironmentpretty) | A rich renderable that pretty prints an object. |
| [`TypeVar`](.././flytekit.core.environment#flytekitcoreenvironmenttypevar) | Type variable. |
| [`partial`](.././flytekit.core.environment#flytekitcoreenvironmentpartial) | Create a new function with partial application of the given arguments. |

### Methods

| Method | Description |
|-|-|
| [`forge()`](#forge) |  |
| [`inherit()`](#inherit) |  |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |
| [`wraps()`](#wraps) | Decorator factory to apply update_wrapper() to a wrapper function. |


### Variables

| Property | Type | Description |
|-|-|-|
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |

## Methods

#### forge()

```python
def forge(
    source: typing.Callable[typing.Concatenate[typing.Any, ~P], ~T],
) -> typing.Callable[[typing.Callable], typing.Callable[typing.Concatenate[typing.Any, ~P], ~T]]
```
| Parameter | Type |
|-|-|
| `source` | `typing.Callable[typing.Concatenate[typing.Any, ~P], ~T]` |

#### inherit()

```python
def inherit(
    old: dict[str, typing.Any],
    new: dict[str, typing.Any],
) -> dict[str, typing.Any]
```
| Parameter | Type |
|-|-|
| `old` | `dict[str, typing.Any]` |
| `new` | `dict[str, typing.Any]` |

#### task()

```python
def task(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

#### wraps()

```python
def wraps(
    wrapped,
    assigned,
    updated,
)
```
Decorator factory to apply update_wrapper() to a wrapper function

Returns a decorator that invokes update_wrapper() with the decorated
function as the wrapper argument and the arguments to wraps() as the
remaining arguments. Default arguments are as for update_wrapper().
This is a convenience function to simplify applying partial() to
update_wrapper().


| Parameter | Type |
|-|-|
| `wrapped` |  |
| `assigned` |  |
| `updated` |  |

## flytekit.core.environment.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.environment.Console

A high level console interface.



```python
class Console(
    color_system: typing.Optional[typing.Literal['auto', 'standard', '256', 'truecolor', 'windows']],
    force_terminal: typing.Optional[bool],
    force_jupyter: typing.Optional[bool],
    force_interactive: typing.Optional[bool],
    soft_wrap: bool,
    theme: typing.Optional[rich.theme.Theme],
    stderr: bool,
    file: typing.Optional[typing.IO[str]],
    quiet: bool,
    width: typing.Optional[int],
    height: typing.Optional[int],
    style: typing.Union[str, ForwardRef('Style'), NoneType],
    no_color: typing.Optional[bool],
    tab_size: int,
    record: bool,
    markup: bool,
    emoji: bool,
    emoji_variant: typing.Optional[typing.Literal['emoji', 'text']],
    highlight: bool,
    log_time: bool,
    log_path: bool,
    log_time_format: typing.Union[str, typing.Callable[[datetime.datetime], rich.text.Text]],
    highlighter: typing.Optional[ForwardRef('HighlighterType')],
    legacy_windows: typing.Optional[bool],
    safe_box: bool,
    get_datetime: typing.Optional[typing.Callable[[], datetime.datetime]],
    get_time: typing.Optional[typing.Callable[[], float]],
    _environ: typing.Optional[typing.Mapping[str, str]],
)
```
| Parameter | Type |
|-|-|
| `color_system` | `typing.Optional[typing.Literal['auto', 'standard', '256', 'truecolor', 'windows']]` |
| `force_terminal` | `typing.Optional[bool]` |
| `force_jupyter` | `typing.Optional[bool]` |
| `force_interactive` | `typing.Optional[bool]` |
| `soft_wrap` | `bool` |
| `theme` | `typing.Optional[rich.theme.Theme]` |
| `stderr` | `bool` |
| `file` | `typing.Optional[typing.IO[str]]` |
| `quiet` | `bool` |
| `width` | `typing.Optional[int]` |
| `height` | `typing.Optional[int]` |
| `style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `no_color` | `typing.Optional[bool]` |
| `tab_size` | `int` |
| `record` | `bool` |
| `markup` | `bool` |
| `emoji` | `bool` |
| `emoji_variant` | `typing.Optional[typing.Literal['emoji', 'text']]` |
| `highlight` | `bool` |
| `log_time` | `bool` |
| `log_path` | `bool` |
| `log_time_format` | `typing.Union[str, typing.Callable[[datetime.datetime], rich.text.Text]]` |
| `highlighter` | `typing.Optional[ForwardRef('HighlighterType')]` |
| `legacy_windows` | `typing.Optional[bool]` |
| `safe_box` | `bool` |
| `get_datetime` | `typing.Optional[typing.Callable[[], datetime.datetime]]` |
| `get_time` | `typing.Optional[typing.Callable[[], float]]` |
| `_environ` | `typing.Optional[typing.Mapping[str, str]]` |

### Methods

| Method | Description |
|-|-|
| [`begin_capture()`](#begin_capture) | Begin capturing console output. |
| [`bell()`](#bell) | Play a 'bell' sound (if supported by the terminal). |
| [`capture()`](#capture) | A context manager to *capture* the result of print() or log() in a string,. |
| [`clear()`](#clear) | Clear the screen. |
| [`clear_live()`](#clear_live) | Clear the Live instance. |
| [`control()`](#control) | Insert non-printing control codes. |
| [`end_capture()`](#end_capture) | End capture mode and return captured string. |
| [`export_html()`](#export_html) | Generate HTML from console contents (requires record=True argument in constructor). |
| [`export_svg()`](#export_svg) | Generate an SVG from the console contents (requires record=True in Console constructor). |
| [`export_text()`](#export_text) | Generate text from console contents (requires record=True argument in constructor). |
| [`get_style()`](#get_style) | Get a Style instance by its theme name or parse a definition. |
| [`input()`](#input) | Displays a prompt and waits for input from the user. |
| [`line()`](#line) | Write new line(s). |
| [`log()`](#log) | Log rich content to the terminal. |
| [`measure()`](#measure) | Measure a renderable. |
| [`on_broken_pipe()`](#on_broken_pipe) | This function is called when a `BrokenPipeError` is raised. |
| [`out()`](#out) | Output to the terminal. |
| [`pager()`](#pager) | A context manager to display anything printed within a "pager". |
| [`pop_render_hook()`](#pop_render_hook) | Pop the last renderhook from the stack. |
| [`pop_theme()`](#pop_theme) | Remove theme from top of stack, restoring previous theme. |
| [`print()`](#print) | Print to the console. |
| [`print_exception()`](#print_exception) | Prints a rich render of the last exception and traceback. |
| [`print_json()`](#print_json) | Pretty prints JSON. |
| [`push_render_hook()`](#push_render_hook) | Add a new render hook to the stack. |
| [`push_theme()`](#push_theme) | Push a new theme on to the top of the stack, replacing the styles from the previous theme. |
| [`render()`](#render) | Render an object in to an iterable of `Segment` instances. |
| [`render_lines()`](#render_lines) | Render objects in to a list of lines. |
| [`render_str()`](#render_str) | Convert a string to a Text instance. |
| [`rule()`](#rule) | Draw a line with optional centered title. |
| [`save_html()`](#save_html) | Generate HTML from console contents and write to a file (requires record=True argument in constructor). |
| [`save_svg()`](#save_svg) | Generate an SVG file from the console contents (requires record=True in Console constructor). |
| [`save_text()`](#save_text) | Generate text from console and save to a given location (requires record=True argument in constructor). |
| [`screen()`](#screen) | Context manager to enable and disable 'alternative screen' mode. |
| [`set_alt_screen()`](#set_alt_screen) | Enables alternative screen mode. |
| [`set_live()`](#set_live) | Set Live instance. |
| [`set_window_title()`](#set_window_title) | Set the title of the console terminal window. |
| [`show_cursor()`](#show_cursor) | Show or hide the cursor. |
| [`status()`](#status) | Display a status and spinner. |
| [`update_screen()`](#update_screen) | Update the screen at a given offset. |
| [`update_screen_lines()`](#update_screen_lines) | Update lines of the screen at a given offset. |
| [`use_theme()`](#use_theme) | Use a different theme for the duration of the context manager. |


#### begin_capture()

```python
def begin_capture()
```
Begin capturing console output. Call :meth:`end_capture` to exit capture mode and return output.


#### bell()

```python
def bell()
```
Play a 'bell' sound (if supported by the terminal).


#### capture()

```python
def capture()
```
A context manager to *capture* the result of print() or log() in a string,
rather than writing it to the console.

Example:
>>> from rich.console import Console
>>> console = Console()
>>> with console.capture() as capture:
...     console.print("[bold magenta]Hello World[/]")
>>> print(capture.get())

Returns:
Capture: Context manager with disables writing to the terminal.


#### clear()

```python
def clear(
    home: bool,
)
```
Clear the screen.



| Parameter | Type |
|-|-|
| `home` | `bool` |

#### clear_live()

```python
def clear_live()
```
Clear the Live instance.


#### control()

```python
def control(
    control: rich.control.Control,
)
```
Insert non-printing control codes.



| Parameter | Type |
|-|-|
| `control` | `rich.control.Control` |

#### end_capture()

```python
def end_capture()
```
End capture mode and return captured string.

Returns:
str: Console output.


#### export_html()

```python
def export_html(
    theme: typing.Optional[rich.terminal_theme.TerminalTheme],
    clear: bool,
    code_format: typing.Optional[str],
    inline_styles: bool,
) -> str
```
Generate HTML from console contents (requires record=True argument in constructor).



| Parameter | Type |
|-|-|
| `theme` | `typing.Optional[rich.terminal_theme.TerminalTheme]` |
| `clear` | `bool` |
| `code_format` | `typing.Optional[str]` |
| `inline_styles` | `bool` |

#### export_svg()

```python
def export_svg(
    title: str,
    theme: typing.Optional[rich.terminal_theme.TerminalTheme],
    clear: bool,
    code_format: str,
    font_aspect_ratio: float,
    unique_id: typing.Optional[str],
) -> str
```
Generate an SVG from the console contents (requires record=True in Console constructor).



| Parameter | Type |
|-|-|
| `title` | `str` |
| `theme` | `typing.Optional[rich.terminal_theme.TerminalTheme]` |
| `clear` | `bool` |
| `code_format` | `str` |
| `font_aspect_ratio` | `float` |
| `unique_id` | `typing.Optional[str]` |

#### export_text()

```python
def export_text(
    clear: bool,
    styles: bool,
) -> str
```
Generate text from console contents (requires record=True argument in constructor).



| Parameter | Type |
|-|-|
| `clear` | `bool` |
| `styles` | `bool` |

#### get_style()

```python
def get_style(
    name: typing.Union[str, rich.style.Style],
    default: typing.Union[rich.style.Style, str, NoneType],
) -> rich.style.Style
```
Get a Style instance by its theme name or parse a definition.



| Parameter | Type |
|-|-|
| `name` | `typing.Union[str, rich.style.Style]` |
| `default` | `typing.Union[rich.style.Style, str, NoneType]` |

#### input()

```python
def input(
    prompt: typing.Union[str, ForwardRef('Text')],
    markup: bool,
    emoji: bool,
    password: bool,
    stream: typing.Optional[typing.TextIO],
) -> str
```
Displays a prompt and waits for input from the user. The prompt may contain color / style.

It works in the same way as Python's builtin :func:`input` function and provides elaborate line editing and history features if Python's builtin :mod:`readline` module is previously loaded.



| Parameter | Type |
|-|-|
| `prompt` | `typing.Union[str, ForwardRef('Text')]` |
| `markup` | `bool` |
| `emoji` | `bool` |
| `password` | `bool` |
| `stream` | `typing.Optional[typing.TextIO]` |

#### line()

```python
def line(
    count: int,
)
```
Write new line(s).



| Parameter | Type |
|-|-|
| `count` | `int` |

#### log()

```python
def log(
    objects: typing.Any,
    sep: str,
    end: str,
    style: typing.Union[rich.style.Style, str, NoneType],
    justify: typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']],
    emoji: typing.Optional[bool],
    markup: typing.Optional[bool],
    highlight: typing.Optional[bool],
    log_locals: bool,
    _stack_offset: int,
)
```
Log rich content to the terminal.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `style` | `typing.Union[rich.style.Style, str, NoneType]` |
| `justify` | `typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']]` |
| `emoji` | `typing.Optional[bool]` |
| `markup` | `typing.Optional[bool]` |
| `highlight` | `typing.Optional[bool]` |
| `log_locals` | `bool` |
| `_stack_offset` | `int` |

#### measure()

```python
def measure(
    renderable: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    options: typing.Optional[rich.console.ConsoleOptions],
) -> rich.measure.Measurement
```
Measure a renderable. Returns a :class:`~rich.measure.Measurement` object which contains
information regarding the number of characters required to print the renderable.



| Parameter | Type |
|-|-|
| `renderable` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `options` | `typing.Optional[rich.console.ConsoleOptions]` |

#### on_broken_pipe()

```python
def on_broken_pipe()
```
This function is called when a `BrokenPipeError` is raised.

This can occur when piping Textual output in Linux and macOS.
The default implementation is to exit the app, but you could implement
this method in a subclass to change the behavior.

See https://docs.python.org/3/library/signal.html#note-on-sigpipe for details.


#### out()

```python
def out(
    objects: typing.Any,
    sep: str,
    end: str,
    style: typing.Union[rich.style.Style, str, NoneType],
    highlight: typing.Optional[bool],
)
```
Output to the terminal. This is a low-level way of writing to the terminal which unlike
:meth:`~rich.console.Console.print` won't pretty print, wrap text, or apply markup, but will
optionally apply highlighting and a basic style.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `style` | `typing.Union[rich.style.Style, str, NoneType]` |
| `highlight` | `typing.Optional[bool]` |

#### pager()

```python
def pager(
    pager: typing.Optional[rich.pager.Pager],
    styles: bool,
    links: bool,
) -> rich.console.PagerContext
```
A context manager to display anything printed within a "pager". The pager application
is defined by the system and will typically support at least pressing a key to scroll.



| Parameter | Type |
|-|-|
| `pager` | `typing.Optional[rich.pager.Pager]` |
| `styles` | `bool` |
| `links` | `bool` |

#### pop_render_hook()

```python
def pop_render_hook()
```
Pop the last renderhook from the stack.


#### pop_theme()

```python
def pop_theme()
```
Remove theme from top of stack, restoring previous theme.


#### print()

```python
def print(
    objects: typing.Any,
    sep: str,
    end: str,
    style: typing.Union[rich.style.Style, str, NoneType],
    justify: typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']],
    overflow: typing.Optional[typing.Literal['fold', 'crop', 'ellipsis', 'ignore']],
    no_wrap: typing.Optional[bool],
    emoji: typing.Optional[bool],
    markup: typing.Optional[bool],
    highlight: typing.Optional[bool],
    width: typing.Optional[int],
    height: typing.Optional[int],
    crop: bool,
    soft_wrap: typing.Optional[bool],
    new_line_start: bool,
)
```
Print to the console.



| Parameter | Type |
|-|-|
| `objects` | `typing.Any` |
| `sep` | `str` |
| `end` | `str` |
| `style` | `typing.Union[rich.style.Style, str, NoneType]` |
| `justify` | `typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']]` |
| `overflow` | `typing.Optional[typing.Literal['fold', 'crop', 'ellipsis', 'ignore']]` |
| `no_wrap` | `typing.Optional[bool]` |
| `emoji` | `typing.Optional[bool]` |
| `markup` | `typing.Optional[bool]` |
| `highlight` | `typing.Optional[bool]` |
| `width` | `typing.Optional[int]` |
| `height` | `typing.Optional[int]` |
| `crop` | `bool` |
| `soft_wrap` | `typing.Optional[bool]` |
| `new_line_start` | `bool` |

#### print_exception()

```python
def print_exception(
    width: typing.Optional[int],
    extra_lines: int,
    theme: typing.Optional[str],
    word_wrap: bool,
    show_locals: bool,
    suppress: typing.Iterable[typing.Union[str, module]],
    max_frames: int,
)
```
Prints a rich render of the last exception and traceback.



| Parameter | Type |
|-|-|
| `width` | `typing.Optional[int]` |
| `extra_lines` | `int` |
| `theme` | `typing.Optional[str]` |
| `word_wrap` | `bool` |
| `show_locals` | `bool` |
| `suppress` | `typing.Iterable[typing.Union[str, module]]` |
| `max_frames` | `int` |

#### print_json()

```python
def print_json(
    json: typing.Optional[str],
    data: typing.Any,
    indent: typing.Union[NoneType, int, str],
    highlight: bool,
    skip_keys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    default: typing.Optional[typing.Callable[[typing.Any], typing.Any]],
    sort_keys: bool,
)
```
Pretty prints JSON. Output will be valid JSON.



| Parameter | Type |
|-|-|
| `json` | `typing.Optional[str]` |
| `data` | `typing.Any` |
| `indent` | `typing.Union[NoneType, int, str]` |
| `highlight` | `bool` |
| `skip_keys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `default` | `typing.Optional[typing.Callable[[typing.Any], typing.Any]]` |
| `sort_keys` | `bool` |

#### push_render_hook()

```python
def push_render_hook(
    hook: rich.console.RenderHook,
)
```
Add a new render hook to the stack.



| Parameter | Type |
|-|-|
| `hook` | `rich.console.RenderHook` |

#### push_theme()

```python
def push_theme(
    theme: rich.theme.Theme,
    inherit: bool,
)
```
Push a new theme on to the top of the stack, replacing the styles from the previous theme.
Generally speaking, you should call :meth:`~rich.console.Console.use_theme` to get a context manager, rather
than calling this method directly.



| Parameter | Type |
|-|-|
| `theme` | `rich.theme.Theme` |
| `inherit` | `bool` |

#### render()

```python
def render(
    renderable: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    options: typing.Optional[rich.console.ConsoleOptions],
) -> typing.Iterable[rich.segment.Segment]
```
Render an object in to an iterable of `Segment` instances.

This method contains the logic for rendering objects with the console protocol.
You are unlikely to need to use it directly, unless you are extending the library.



| Parameter | Type |
|-|-|
| `renderable` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `options` | `typing.Optional[rich.console.ConsoleOptions]` |

#### render_lines()

```python
def render_lines(
    renderable: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    options: typing.Optional[rich.console.ConsoleOptions],
    style: typing.Optional[rich.style.Style],
    pad: bool,
    new_lines: bool,
) -> typing.List[typing.List[rich.segment.Segment]]
```
Render objects in to a list of lines.

The output of render_lines is useful when further formatting of rendered console text
is required, such as the Panel class which draws a border around any renderable object.



| Parameter | Type |
|-|-|
| `renderable` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `options` | `typing.Optional[rich.console.ConsoleOptions]` |
| `style` | `typing.Optional[rich.style.Style]` |
| `pad` | `bool` |
| `new_lines` | `bool` |

#### render_str()

```python
def render_str(
    text: str,
    style: typing.Union[str, rich.style.Style],
    justify: typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']],
    overflow: typing.Optional[typing.Literal['fold', 'crop', 'ellipsis', 'ignore']],
    emoji: typing.Optional[bool],
    markup: typing.Optional[bool],
    highlight: typing.Optional[bool],
    highlighter: typing.Optional[typing.Callable[[typing.Union[str, ForwardRef('Text')]], ForwardRef('Text')]],
) -> Text
```
Convert a string to a Text instance. This is called automatically if
you print or log a string.



| Parameter | Type |
|-|-|
| `text` | `str` |
| `style` | `typing.Union[str, rich.style.Style]` |
| `justify` | `typing.Optional[typing.Literal['default', 'left', 'center', 'right', 'full']]` |
| `overflow` | `typing.Optional[typing.Literal['fold', 'crop', 'ellipsis', 'ignore']]` |
| `emoji` | `typing.Optional[bool]` |
| `markup` | `typing.Optional[bool]` |
| `highlight` | `typing.Optional[bool]` |
| `highlighter` | `typing.Optional[typing.Callable[[typing.Union[str, ForwardRef('Text')]], ForwardRef('Text')]]` |

#### rule()

```python
def rule(
    title: typing.Union[str, ForwardRef('Text')],
    characters: str,
    style: typing.Union[str, rich.style.Style],
    align: typing.Literal['left', 'center', 'right'],
)
```
Draw a line with optional centered title.



| Parameter | Type |
|-|-|
| `title` | `typing.Union[str, ForwardRef('Text')]` |
| `characters` | `str` |
| `style` | `typing.Union[str, rich.style.Style]` |
| `align` | `typing.Literal['left', 'center', 'right']` |

#### save_html()

```python
def save_html(
    path: str,
    theme: typing.Optional[rich.terminal_theme.TerminalTheme],
    clear: bool,
    code_format: str,
    inline_styles: bool,
)
```
Generate HTML from console contents and write to a file (requires record=True argument in constructor).



| Parameter | Type |
|-|-|
| `path` | `str` |
| `theme` | `typing.Optional[rich.terminal_theme.TerminalTheme]` |
| `clear` | `bool` |
| `code_format` | `str` |
| `inline_styles` | `bool` |

#### save_svg()

```python
def save_svg(
    path: str,
    title: str,
    theme: typing.Optional[rich.terminal_theme.TerminalTheme],
    clear: bool,
    code_format: str,
    font_aspect_ratio: float,
    unique_id: typing.Optional[str],
)
```
Generate an SVG file from the console contents (requires record=True in Console constructor).



| Parameter | Type |
|-|-|
| `path` | `str` |
| `title` | `str` |
| `theme` | `typing.Optional[rich.terminal_theme.TerminalTheme]` |
| `clear` | `bool` |
| `code_format` | `str` |
| `font_aspect_ratio` | `float` |
| `unique_id` | `typing.Optional[str]` |

#### save_text()

```python
def save_text(
    path: str,
    clear: bool,
    styles: bool,
)
```
Generate text from console and save to a given location (requires record=True argument in constructor).



| Parameter | Type |
|-|-|
| `path` | `str` |
| `clear` | `bool` |
| `styles` | `bool` |

#### screen()

```python
def screen(
    hide_cursor: bool,
    style: typing.Union[str, ForwardRef('Style'), NoneType],
) -> ScreenContext
```
Context manager to enable and disable 'alternative screen' mode.



| Parameter | Type |
|-|-|
| `hide_cursor` | `bool` |
| `style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |

#### set_alt_screen()

```python
def set_alt_screen(
    enable: bool,
) -> bool
```
Enables alternative screen mode.

Note, if you enable this mode, you should ensure that is disabled before
the application exits. See :meth:`~rich.Console.screen` for a context manager
that handles this for you.



| Parameter | Type |
|-|-|
| `enable` | `bool` |

#### set_live()

```python
def set_live(
    live: Live,
)
```
Set Live instance. Used by Live context manager.



| Parameter | Type |
|-|-|
| `live` | `Live` |

#### set_window_title()

```python
def set_window_title(
    title: str,
) -> bool
```
Set the title of the console terminal window.

Warning: There is no means within Rich of "resetting" the window title to its
previous value, meaning the title you set will persist even after your application
exits.

``fish`` shell resets the window title before and after each command by default,
negating this issue. Windows Terminal and command prompt will also reset the title for you.
Most other shells and terminals, however, do not do this.

Some terminals may require configuration changes before you can set the title.
Some terminals may not support setting the title at all.

Other software (including the terminal itself, the shell, custom prompts, plugins, etc.)
may also set the terminal window title. This could result in whatever value you write
using this method being overwritten.



| Parameter | Type |
|-|-|
| `title` | `str` |

#### show_cursor()

```python
def show_cursor(
    show: bool,
) -> bool
```
Show or hide the cursor.



| Parameter | Type |
|-|-|
| `show` | `bool` |

#### status()

```python
def status(
    status: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    spinner: str,
    spinner_style: typing.Union[str, ForwardRef('Style')],
    speed: float,
    refresh_per_second: float,
) -> Status
```
Display a status and spinner.



| Parameter | Type |
|-|-|
| `status` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `spinner` | `str` |
| `spinner_style` | `typing.Union[str, ForwardRef('Style')]` |
| `speed` | `float` |
| `refresh_per_second` | `float` |

#### update_screen()

```python
def update_screen(
    renderable: typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str],
    region: typing.Optional[rich.region.Region],
    options: typing.Optional[rich.console.ConsoleOptions],
)
```
Update the screen at a given offset.



| Parameter | Type |
|-|-|
| `renderable` | `typing.Union[rich.console.ConsoleRenderable, rich.console.RichCast, str]` |
| `region` | `typing.Optional[rich.region.Region]` |
| `options` | `typing.Optional[rich.console.ConsoleOptions]` |

#### update_screen_lines()

```python
def update_screen_lines(
    lines: typing.List[typing.List[rich.segment.Segment]],
    x: int,
    y: int,
)
```
Update lines of the screen at a given offset.



| Parameter | Type |
|-|-|
| `lines` | `typing.List[typing.List[rich.segment.Segment]]` |
| `x` | `int` |
| `y` | `int` |

#### use_theme()

```python
def use_theme(
    theme: rich.theme.Theme,
    inherit: bool,
) -> rich.console.ThemeContext
```
Use a different theme for the duration of the context manager.



| Parameter | Type |
|-|-|
| `theme` | `rich.theme.Theme` |
| `inherit` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `color_system` |  | {{< multiline >}}Get color system string.

Returns:
Optional[str]: "standard", "256" or "truecolor".
{{< /multiline >}} |
| `encoding` |  | {{< multiline >}}Get the encoding of the console file, e.g. ``"utf-8"``.

Returns:
str: A standard encoding string.
{{< /multiline >}} |
| `file` |  | {{< multiline >}}Get the file object to write to.
{{< /multiline >}} |
| `height` |  | {{< multiline >}}Get the height of the console.

Returns:
int: The height (in lines) of the console.
{{< /multiline >}} |
| `is_alt_screen` |  | {{< multiline >}}Check if the alt screen was enabled.

Returns:
bool: True if the alt screen was enabled, otherwise False.
{{< /multiline >}} |
| `is_dumb_terminal` |  | {{< multiline >}}Detect dumb terminal.

Returns:
bool: True if writing to a dumb terminal, otherwise False.
{{< /multiline >}} |
| `is_terminal` |  | {{< multiline >}}Check if the console is writing to a terminal.

Returns:
bool: True if the console writing to a device capable of
understanding terminal codes, otherwise False.
{{< /multiline >}} |
| `options` |  | {{< multiline >}}Get default console options.
{{< /multiline >}} |
| `size` |  | {{< multiline >}}Get the size of the console.

Returns:
ConsoleDimensions: A named tuple containing the dimensions.
{{< /multiline >}} |
| `width` |  | {{< multiline >}}Get the width of the console.

Returns:
int: The width (in characters) of the console.
{{< /multiline >}} |

## flytekit.core.environment.Environment

```python
class Environment(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
)
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`dynamic()`](#dynamic) | Please first see the comments for :py:func:`flytekit. |
| [`extend()`](#extend) | This is the core decorator to use for any task type in flytekit. |
| [`show()`](#show) |  |
| [`task()`](#task) | This is the core decorator to use for any task type in flytekit. |
| [`update()`](#update) | This is the core decorator to use for any task type in flytekit. |


#### dynamic()

```python
def dynamic(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
Please first see the comments for :py:func:`flytekit.task` and :py:func:`flytekit.workflow`. This ``dynamic``
concept is an amalgamation of both and enables the user to pursue some :std:ref:`pretty incredible <cookbook:advanced_merge_sort>`
constructs.

In short, a task's function is run at execution time only, and a workflow function is run at compilation time only (local
execution notwithstanding). A dynamic workflow is modeled on the backend as a task, but at execution time, the function
body is run to produce a workflow. It is almost as if the decorator changed from ``@task`` to ``@workflow`` except workflows
cannot make use of their inputs like native Python values whereas dynamic workflows can.
The resulting workflow is passed back to the Flyte engine and is
run as a :std:ref:`subworkflow <cookbook:subworkflows>`.  Simple usage

.. code-block::

@dynamic
def my_dynamic_subwf(a: int) -> (typing.List[str], int):
s = []
for i in range(a):
s.append(t1(a=i))
return s, 5

Note in the code block that we call the Python ``range`` operator on the input. This is typically not allowed in a
workflow but it is here. You can even express dependencies between tasks.

.. code-block::

@dynamic
def my_dynamic_subwf(a: int, b: int) -> int:
x = t1(a=a)
return t2(b=b, x=x)

See the :std:ref:`cookbook <cookbook:subworkflows>` for a longer discussion.


| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

#### extend()

```python
def extend(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

#### show()

```python
def show()
```
#### task()

```python
def task(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

#### update()

```python
def update(
    _task_function: Optional[Callable[P, FuncOut]],
    task_config: Optional[T],
    cache: Union[bool, Cache],
    retries: int,
    interruptible: Optional[bool],
    deprecated: str,
    timeout: Union[datetime.timedelta, int],
    container_image: Optional[Union[str, ImageSpec]],
    environment: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    secret_requests: Optional[List[Secret]],
    execution_mode: PythonFunctionTask.ExecutionBehavior,
    node_dependency_hints: Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]],
    task_resolver: Optional[TaskResolverMixin],
    docs: Optional[Documentation],
    disable_deck: Optional[bool],
    enable_deck: Optional[bool],
    deck_fields: Optional[Tuple[DeckField, ...]],
    pod_template: Optional['PodTemplate'],
    pod_template_name: Optional[str],
    accelerator: Optional[BaseAccelerator],
    pickle_untyped: bool,
    shared_memory: Optional[Union[L[True], str]],
    resources: Optional[Resources],
    kwargs,
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionTask[T]], PythonFunctionTask[T]]
```
This is the core decorator to use for any task type in flytekit.

Tasks are the building blocks of Flyte. They represent users code. Tasks have the following properties

* Versioned (usually tied to the git revision SHA1)
* Strong interfaces (specified inputs and outputs)
* Declarative
* Independently executable
* Unit testable

For a simple python task,

.. code-block:: python

@task
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

For specific task types

.. code-block:: python

@task(task_config=Spark(), retries=3)
def my_task(x: int, y: typing.Dict[str, str]) -> str:
...

Please see some cookbook :std:ref:`task examples <cookbook:tasks>` for additional information.



| Parameter | Type |
|-|-|
| `_task_function` | `Optional[Callable[P, FuncOut]]` |
| `task_config` | `Optional[T]` |
| `cache` | `Union[bool, Cache]` |
| `retries` | `int` |
| `interruptible` | `Optional[bool]` |
| `deprecated` | `str` |
| `timeout` | `Union[datetime.timedelta, int]` |
| `container_image` | `Optional[Union[str, ImageSpec]]` |
| `environment` | `Optional[Dict[str, str]]` |
| `requests` | `Optional[Resources]` |
| `limits` | `Optional[Resources]` |
| `secret_requests` | `Optional[List[Secret]]` |
| `execution_mode` | `PythonFunctionTask.ExecutionBehavior` |
| `node_dependency_hints` | `Optional[Iterable[Union[PythonFunctionTask, _annotated_launchplan.LaunchPlan, _annotated_workflow.WorkflowBase]]]` |
| `task_resolver` | `Optional[TaskResolverMixin]` |
| `docs` | `Optional[Documentation]` |
| `disable_deck` | `Optional[bool]` |
| `enable_deck` | `Optional[bool]` |
| `deck_fields` | `Optional[Tuple[DeckField, ...]]` |
| `pod_template` | `Optional['PodTemplate']` |
| `pod_template_name` | `Optional[str]` |
| `accelerator` | `Optional[BaseAccelerator]` |
| `pickle_untyped` | `bool` |
| `shared_memory` | `Optional[Union[L[True], str]]` |
| `resources` | `Optional[Resources]` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.environment.Panel

A console renderable that draws a border around its contents.

Example:
>>> console.print(Panel("Hello, World!"))



```python
class Panel(
    renderable: RenderableType,
    box: rich.box.Box,
    title: typing.Union[str, ForwardRef('Text'), NoneType],
    title_align: typing.Literal['left', 'center', 'right'],
    subtitle: typing.Union[str, ForwardRef('Text'), NoneType],
    subtitle_align: typing.Literal['left', 'center', 'right'],
    safe_box: typing.Optional[bool],
    expand: bool,
    style: typing.Union[str, ForwardRef('Style')],
    border_style: typing.Union[str, ForwardRef('Style')],
    width: typing.Optional[int],
    height: typing.Optional[int],
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
    highlight: bool,
)
```
| Parameter | Type |
|-|-|
| `renderable` | `RenderableType` |
| `box` | `rich.box.Box` |
| `title` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `title_align` | `typing.Literal['left', 'center', 'right']` |
| `subtitle` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `subtitle_align` | `typing.Literal['left', 'center', 'right']` |
| `safe_box` | `typing.Optional[bool]` |
| `expand` | `bool` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `border_style` | `typing.Union[str, ForwardRef('Style')]` |
| `width` | `typing.Optional[int]` |
| `height` | `typing.Optional[int]` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |
| `highlight` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`fit()`](#fit) | An alternative constructor that sets expand=False. |


#### fit()

```python
def fit(
    renderable: RenderableType,
    box: rich.box.Box,
    title: typing.Union[str, ForwardRef('Text'), NoneType],
    title_align: typing.Literal['left', 'center', 'right'],
    subtitle: typing.Union[str, ForwardRef('Text'), NoneType],
    subtitle_align: typing.Literal['left', 'center', 'right'],
    safe_box: typing.Optional[bool],
    style: typing.Union[str, ForwardRef('Style')],
    border_style: typing.Union[str, ForwardRef('Style')],
    width: typing.Optional[int],
    height: typing.Optional[int],
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
    highlight: bool,
) -> Panel
```
An alternative constructor that sets expand=False.


| Parameter | Type |
|-|-|
| `renderable` | `RenderableType` |
| `box` | `rich.box.Box` |
| `title` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `title_align` | `typing.Literal['left', 'center', 'right']` |
| `subtitle` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `subtitle_align` | `typing.Literal['left', 'center', 'right']` |
| `safe_box` | `typing.Optional[bool]` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `border_style` | `typing.Union[str, ForwardRef('Style')]` |
| `width` | `typing.Optional[int]` |
| `height` | `typing.Optional[int]` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |
| `highlight` | `bool` |

## flytekit.core.environment.ParamSpec

Parameter specification variable.

The preferred way to construct a parameter specification is via the
dedicated syntax for generic functions, classes, and type aliases,
where the use of '**' creates a parameter specification::

type IntFunc[**P] = Callable[P, int]

The following syntax creates a parameter specification that defaults
to a callable accepting two positional-only arguments of types int
and str:

type IntFuncDefault[**P = (int, str)] = Callable[P, int]

For compatibility with Python 3.11 and earlier, ParamSpec objects
can also be created as follows::

P = ParamSpec('P')
DefaultP = ParamSpec('DefaultP', default=(int, str))

Parameter specification variables exist primarily for the benefit of
static type checkers.  They are used to forward the parameter types of
one callable to another callable, a pattern commonly found in
higher-order functions and decorators.  They are only valid when used
in ``Concatenate``, or as the first argument to ``Callable``, or as
parameters for user-defined Generics. See class Generic for more
information on generic types.

An example for annotating a decorator::

def add_logging[**P, T](f: Callable[P, T]) -> Callable[P, T]:
'''A type-safe decorator to add logging to a function.'''
def inner(*args: P.args, **kwargs: P.kwargs) -> T:
logging.info(f'{f.__name__} was called')
return f(*args, **kwargs)
return inner

@add_logging
def add_two(x: float, y: float) -> float:
'''Add two numbers together.'''
return x + y

Parameter specification variables can be introspected. e.g.::

>>> P = ParamSpec("P")
>>> P.__name__
'P'

Note that only parameter specification variables defined in the global
scope can be pickled.


## flytekit.core.environment.Pretty

A rich renderable that pretty prints an object.



```python
class Pretty(
    _object: typing.Any,
    highlighter: typing.Optional[ForwardRef('HighlighterType')],
    indent_size: int,
    justify: typing.Optional[ForwardRef('JustifyMethod')],
    overflow: typing.Optional[ForwardRef('OverflowMethod')],
    no_wrap: typing.Optional[bool],
    indent_guides: bool,
    max_length: typing.Optional[int],
    max_string: typing.Optional[int],
    max_depth: typing.Optional[int],
    expand_all: bool,
    margin: int,
    insert_line: bool,
)
```
| Parameter | Type |
|-|-|
| `_object` | `typing.Any` |
| `highlighter` | `typing.Optional[ForwardRef('HighlighterType')]` |
| `indent_size` | `int` |
| `justify` | `typing.Optional[ForwardRef('JustifyMethod')]` |
| `overflow` | `typing.Optional[ForwardRef('OverflowMethod')]` |
| `no_wrap` | `typing.Optional[bool]` |
| `indent_guides` | `bool` |
| `max_length` | `typing.Optional[int]` |
| `max_string` | `typing.Optional[int]` |
| `max_depth` | `typing.Optional[int]` |
| `expand_all` | `bool` |
| `margin` | `int` |
| `insert_line` | `bool` |

## flytekit.core.environment.TypeVar

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

Type variables can also have defaults:

class IntDefault[T = int]:
...

However, if desired, reusable type variables can also be constructed
manually, like so::

T = TypeVar('T')  # Can be anything
S = TypeVar('S', bound=str)  # Can be any subtype of str
A = TypeVar('A', str, bytes)  # Must be exactly str or bytes
D = TypeVar('D', default=int)  # Defaults to int

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


## flytekit.core.environment.partial

Create a new function with partial application of the given arguments
and keywords.


