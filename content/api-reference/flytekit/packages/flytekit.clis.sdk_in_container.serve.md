---
title: flytekit.clis.sdk_in_container.serve
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.serve

## Directory

### Classes

| Class | Description |
|-|-|
| [`Console`](.././flytekit.clis.sdk_in_container.serve#flytekitclissdk_in_containerserveconsole) | A high level console interface. |
| [`Table`](.././flytekit.clis.sdk_in_container.serve#flytekitclissdk_in_containerservetable) | A console renderable to draw a table. |

### Methods

| Method | Description |
|-|-|
| [`_start_grpc_server()`](#_start_grpc_server) |  |
| [`_start_health_check_server()`](#_start_health_check_server) |  |
| [`_start_http_server()`](#_start_http_server) |  |
| [`add_AgentMetadataServiceServicer_to_server()`](#add_agentmetadataserviceservicer_to_server) |  |
| [`add_AsyncAgentServiceServicer_to_server()`](#add_asyncagentserviceservicer_to_server) |  |
| [`add_SyncAgentServiceServicer_to_server()`](#add_syncagentserviceservicer_to_server) |  |
| [`print_metadata()`](#print_metadata) |  |


## Methods

#### _start_grpc_server()

```python
def _start_grpc_server(
    name: str,
    port: int,
    prometheus_port: int,
    worker: int,
    timeout: int,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `port` | `int` |
| `prometheus_port` | `int` |
| `worker` | `int` |
| `timeout` | `int` |

#### _start_health_check_server()

```python
def _start_health_check_server(
    server: grpc.Server,
    worker: int,
)
```
| Parameter | Type |
|-|-|
| `server` | `grpc.Server` |
| `worker` | `int` |

#### _start_http_server()

```python
def _start_http_server(
    prometheus_port: int,
)
```
| Parameter | Type |
|-|-|
| `prometheus_port` | `int` |

#### add_AgentMetadataServiceServicer_to_server()

```python
def add_AgentMetadataServiceServicer_to_server(
    servicer,
    server,
)
```
| Parameter | Type |
|-|-|
| `servicer` |  |
| `server` |  |

#### add_AsyncAgentServiceServicer_to_server()

```python
def add_AsyncAgentServiceServicer_to_server(
    servicer,
    server,
)
```
| Parameter | Type |
|-|-|
| `servicer` |  |
| `server` |  |

#### add_SyncAgentServiceServicer_to_server()

```python
def add_SyncAgentServiceServicer_to_server(
    servicer,
    server,
)
```
| Parameter | Type |
|-|-|
| `servicer` |  |
| `server` |  |

#### print_metadata()

```python
def print_metadata(
    name: str,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |

## flytekit.clis.sdk_in_container.serve.Console

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

## flytekit.clis.sdk_in_container.serve.Table

A console renderable to draw a table.



```python
class Table(
    headers: typing.Union[rich.table.Column, str],
    title: typing.Union[str, ForwardRef('Text'), NoneType],
    caption: typing.Union[str, ForwardRef('Text'), NoneType],
    width: typing.Optional[int],
    min_width: typing.Optional[int],
    box: typing.Optional[rich.box.Box],
    safe_box: typing.Optional[bool],
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
    collapse_padding: bool,
    pad_edge: bool,
    expand: bool,
    show_header: bool,
    show_footer: bool,
    show_edge: bool,
    show_lines: bool,
    leading: int,
    style: typing.Union[str, ForwardRef('Style')],
    row_styles: typing.Optional[typing.Iterable[typing.Union[str, ForwardRef('Style')]]],
    header_style: typing.Union[str, ForwardRef('Style'), NoneType],
    footer_style: typing.Union[str, ForwardRef('Style'), NoneType],
    border_style: typing.Union[str, ForwardRef('Style'), NoneType],
    title_style: typing.Union[str, ForwardRef('Style'), NoneType],
    caption_style: typing.Union[str, ForwardRef('Style'), NoneType],
    title_justify: JustifyMethod,
    caption_justify: JustifyMethod,
    highlight: bool,
)
```
| Parameter | Type |
|-|-|
| `headers` | `typing.Union[rich.table.Column, str]` |
| `title` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `caption` | `typing.Union[str, ForwardRef('Text'), NoneType]` |
| `width` | `typing.Optional[int]` |
| `min_width` | `typing.Optional[int]` |
| `box` | `typing.Optional[rich.box.Box]` |
| `safe_box` | `typing.Optional[bool]` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |
| `collapse_padding` | `bool` |
| `pad_edge` | `bool` |
| `expand` | `bool` |
| `show_header` | `bool` |
| `show_footer` | `bool` |
| `show_edge` | `bool` |
| `show_lines` | `bool` |
| `leading` | `int` |
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `row_styles` | `typing.Optional[typing.Iterable[typing.Union[str, ForwardRef('Style')]]]` |
| `header_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `footer_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `border_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `title_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `caption_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `title_justify` | `JustifyMethod` |
| `caption_justify` | `JustifyMethod` |
| `highlight` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`add_column()`](#add_column) | Add a column to the table. |
| [`add_row()`](#add_row) | Add a row of renderables. |
| [`add_section()`](#add_section) | Add a new section (draw a line after current row). |
| [`get_row_style()`](#get_row_style) | Get the current row style. |
| [`grid()`](#grid) | Get a table with no lines, headers, or footer. |


#### add_column()

```python
def add_column(
    header: RenderableType,
    footer: RenderableType,
    header_style: typing.Union[str, ForwardRef('Style'), NoneType],
    highlight: typing.Optional[bool],
    footer_style: typing.Union[str, ForwardRef('Style'), NoneType],
    style: typing.Union[str, ForwardRef('Style'), NoneType],
    justify: JustifyMethod,
    vertical: VerticalAlignMethod,
    overflow: OverflowMethod,
    width: typing.Optional[int],
    min_width: typing.Optional[int],
    max_width: typing.Optional[int],
    ratio: typing.Optional[int],
    no_wrap: bool,
)
```
Add a column to the table.



| Parameter | Type |
|-|-|
| `header` | `RenderableType` |
| `footer` | `RenderableType` |
| `header_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `highlight` | `typing.Optional[bool]` |
| `footer_style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `justify` | `JustifyMethod` |
| `vertical` | `VerticalAlignMethod` |
| `overflow` | `OverflowMethod` |
| `width` | `typing.Optional[int]` |
| `min_width` | `typing.Optional[int]` |
| `max_width` | `typing.Optional[int]` |
| `ratio` | `typing.Optional[int]` |
| `no_wrap` | `bool` |

#### add_row()

```python
def add_row(
    renderables: typing.Optional[ForwardRef('RenderableType')],
    style: typing.Union[str, ForwardRef('Style'), NoneType],
    end_section: bool,
)
```
Add a row of renderables.



| Parameter | Type |
|-|-|
| `renderables` | `typing.Optional[ForwardRef('RenderableType')]` |
| `style` | `typing.Union[str, ForwardRef('Style'), NoneType]` |
| `end_section` | `bool` |

#### add_section()

```python
def add_section()
```
Add a new section (draw a line after current row).


#### get_row_style()

```python
def get_row_style(
    console: Console,
    index: int,
) -> typing.Union[str, ForwardRef('Style')]
```
Get the current row style.


| Parameter | Type |
|-|-|
| `console` | `Console` |
| `index` | `int` |

#### grid()

```python
def grid(
    headers: typing.Union[rich.table.Column, str],
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
    collapse_padding: bool,
    pad_edge: bool,
    expand: bool,
) -> Table
```
Get a table with no lines, headers, or footer.



| Parameter | Type |
|-|-|
| `headers` | `typing.Union[rich.table.Column, str]` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |
| `collapse_padding` | `bool` |
| `pad_edge` | `bool` |
| `expand` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `expand` |  | {{< multiline >}}Setting a non-None self.width implies expand.
{{< /multiline >}} |
| `padding` |  | {{< multiline >}}Get cell padding.
{{< /multiline >}} |
| `row_count` |  | {{< multiline >}}Get the current number of rows.
{{< /multiline >}} |

