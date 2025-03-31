---
title: flytekit.clis.sdk_in_container.get
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.get

## Directory

### Classes

| Class | Description |
|-|-|
| [`Console`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetconsole) | A high level console interface. |
| [`FlyteRemote`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetflyteremote) | Main entrypoint for programmatically accessing a Flyte remote backend. |
| [`Identifier`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetidentifier) | None. |
| [`LaunchPlanState`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetlaunchplanstate) | None. |
| [`NamedEntityIdentifier`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetnamedentityidentifier) | None. |
| [`ResourceType`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetresourcetype) | None. |
| [`Sort`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergetsort) | None. |
| [`Table`](.././flytekit.clis.sdk_in_container.get#flytekitclissdk_in_containergettable) | A console renderable to draw a table. |

## flytekit.clis.sdk_in_container.get.Console

A high level console interface.



```python
def Console(
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
):
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
| [`begin_capture()`](#begin_capture) | Begin capturing console output |
| [`bell()`](#bell) | Play a 'bell' sound (if supported by the terminal) |
| [`capture()`](#capture) | A context manager to *capture* the result of print() or log() in a string, |
| [`clear()`](#clear) | Clear the screen |
| [`clear_live()`](#clear_live) | Clear the Live instance |
| [`control()`](#control) | Insert non-printing control codes |
| [`end_capture()`](#end_capture) | End capture mode and return captured string |
| [`export_html()`](#export_html) | Generate HTML from console contents (requires record=True argument in constructor) |
| [`export_svg()`](#export_svg) | Generate an SVG from the console contents (requires record=True in Console constructor) |
| [`export_text()`](#export_text) | Generate text from console contents (requires record=True argument in constructor) |
| [`get_style()`](#get_style) | Get a Style instance by its theme name or parse a definition |
| [`input()`](#input) | Displays a prompt and waits for input from the user |
| [`line()`](#line) | Write new line(s) |
| [`log()`](#log) | Log rich content to the terminal |
| [`measure()`](#measure) | Measure a renderable |
| [`on_broken_pipe()`](#on_broken_pipe) | This function is called when a `BrokenPipeError` is raised |
| [`out()`](#out) | Output to the terminal |
| [`pager()`](#pager) | A context manager to display anything printed within a "pager" |
| [`pop_render_hook()`](#pop_render_hook) | Pop the last renderhook from the stack |
| [`pop_theme()`](#pop_theme) | Remove theme from top of stack, restoring previous theme |
| [`print()`](#print) | Print to the console |
| [`print_exception()`](#print_exception) | Prints a rich render of the last exception and traceback |
| [`print_json()`](#print_json) | Pretty prints JSON |
| [`push_render_hook()`](#push_render_hook) | Add a new render hook to the stack |
| [`push_theme()`](#push_theme) | Push a new theme on to the top of the stack, replacing the styles from the previous theme |
| [`render()`](#render) | Render an object in to an iterable of `Segment` instances |
| [`render_lines()`](#render_lines) | Render objects in to a list of lines |
| [`render_str()`](#render_str) | Convert a string to a Text instance |
| [`rule()`](#rule) | Draw a line with optional centered title |
| [`save_html()`](#save_html) | Generate HTML from console contents and write to a file (requires record=True argument in constructor) |
| [`save_svg()`](#save_svg) | Generate an SVG file from the console contents (requires record=True in Console constructor) |
| [`save_text()`](#save_text) | Generate text from console and save to a given location (requires record=True argument in constructor) |
| [`screen()`](#screen) | Context manager to enable and disable 'alternative screen' mode |
| [`set_alt_screen()`](#set_alt_screen) | Enables alternative screen mode |
| [`set_live()`](#set_live) | Set Live instance |
| [`set_window_title()`](#set_window_title) | Set the title of the console terminal window |
| [`show_cursor()`](#show_cursor) | Show or hide the cursor |
| [`status()`](#status) | Display a status and spinner |
| [`update_screen()`](#update_screen) | Update the screen at a given offset |
| [`update_screen_lines()`](#update_screen_lines) | Update lines of the screen at a given offset |
| [`use_theme()`](#use_theme) | Use a different theme for the duration of the context manager |


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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
```
Set Live instance. Used by Live context manager.



| Parameter | Type |
|-|-|
| `live` | `Live` |

#### set_window_title()

```python
def set_window_title(
    title: str,
):
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
):
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
):
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
):
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
):
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
):
```
Use a different theme for the duration of the context manager.



| Parameter | Type |
|-|-|
| `theme` | `rich.theme.Theme` |
| `inherit` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| color_system |  |  |
| encoding |  |  |
| file |  |  |
| height |  |  |
| is_alt_screen |  |  |
| is_dumb_terminal |  |  |
| is_terminal |  |  |
| options |  |  |
| size |  |  |
| width |  |  |

## flytekit.clis.sdk_in_container.get.FlyteRemote

Main entrypoint for programmatically accessing a Flyte remote backend.

The term 'remote' is synonymous with 'backend' or 'deployment' and refers to a hosted instance of the
Flyte platform, which comes with a Flyte Admin server on some known URI.


```python
def FlyteRemote(
    config: Config,
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: typing.Optional[bool],
    kwargs,
):
```
Initialize a FlyteRemote object.

:type kwargs: All arguments that can be passed to create the SynchronousFlyteClient. These are usually grpc
parameters, if you want to customize credentials, ssl handling etc.


| Parameter | Type |
|-|-|
| `config` | `Config` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `typing.Optional[bool]` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`activate_launchplan()`](#activate_launchplan) | Given a launchplan, activate it, all previous versions are deactivated |
| [`approve()`](#approve) |  |
| [`auto()`](#auto) | None |
| [`download()`](#download) | Download the data to the specified location |
| [`execute()`](#execute) | Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity |
| [`execute_local_launch_plan()`](#execute_local_launch_plan) | Execute a locally defined `LaunchPlan` |
| [`execute_local_task()`](#execute_local_task) | Execute a @task-decorated function or TaskTemplate task |
| [`execute_local_workflow()`](#execute_local_workflow) | Execute an @workflow decorated function |
| [`execute_reference_launch_plan()`](#execute_reference_launch_plan) | Execute a ReferenceLaunchPlan |
| [`execute_reference_task()`](#execute_reference_task) | Execute a ReferenceTask |
| [`execute_reference_workflow()`](#execute_reference_workflow) | Execute a ReferenceWorkflow |
| [`execute_remote_task_lp()`](#execute_remote_task_lp) | Execute a FlyteTask, or FlyteLaunchplan |
| [`execute_remote_wf()`](#execute_remote_wf) | Execute a FlyteWorkflow |
| [`fast_package()`](#fast_package) | Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location |
| [`fast_register_workflow()`](#fast_register_workflow) | Use this method to register a workflow with zip mode |
| [`fetch_active_launchplan()`](#fetch_active_launchplan) | Returns the active version of the launch plan if it exists or returns None |
| [`fetch_execution()`](#fetch_execution) | Fetch a workflow execution entity from flyte admin |
| [`fetch_launch_plan()`](#fetch_launch_plan) | Fetch a launchplan entity from flyte admin |
| [`fetch_task()`](#fetch_task) | Fetch a task entity from flyte admin |
| [`fetch_task_lazy()`](#fetch_task_lazy) | Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`fetch_workflow()`](#fetch_workflow) | Fetch a workflow entity from flyte admin |
| [`fetch_workflow_lazy()`](#fetch_workflow_lazy) | Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily |
| [`find_launch_plan()`](#find_launch_plan) | None |
| [`find_launch_plan_for_node()`](#find_launch_plan_for_node) | None |
| [`for_endpoint()`](#for_endpoint) | None |
| [`for_sandbox()`](#for_sandbox) | None |
| [`generate_console_http_domain()`](#generate_console_http_domain) | This should generate the domain where console is hosted |
| [`generate_console_url()`](#generate_console_url) | Generate a Flyteconsole URL for the given Flyte remote endpoint |
| [`get()`](#get) | General function that works with flyte tiny urls |
| [`get_domains()`](#get_domains) | Lists registered domains from flyte admin |
| [`get_execution_metrics()`](#get_execution_metrics) | Get the metrics for a given execution |
| [`get_extra_headers_for_protocol()`](#get_extra_headers_for_protocol) | None |
| [`launch_backfill()`](#launch_backfill) | Creates and launches a backfill workflow for the given launchplan |
| [`list_projects()`](#list_projects) | Lists registered projects from flyte admin |
| [`list_signals()`](#list_signals) |  |
| [`list_tasks_by_version()`](#list_tasks_by_version) | None |
| [`raw_register()`](#raw_register) | Raw register method, can be used to register control plane entities |
| [`recent_executions()`](#recent_executions) | None |
| [`register_launch_plan()`](#register_launch_plan) | Register a given launchplan, possibly applying overrides from the provided options |
| [`register_script()`](#register_script) | Use this method to register a workflow via script mode |
| [`register_task()`](#register_task) | Register a qualified task (PythonTask) with Remote |
| [`register_workflow()`](#register_workflow) | Use this method to register a workflow |
| [`reject()`](#reject) |  |
| [`remote_context()`](#remote_context) | Context manager with remote-specific configuration |
| [`set_input()`](#set_input) |  |
| [`set_signal()`](#set_signal) |  |
| [`sync()`](#sync) | This function was previously a singledispatchmethod |
| [`sync_execution()`](#sync_execution) | Sync a FlyteWorkflowExecution object with its corresponding remote state |
| [`sync_node_execution()`](#sync_node_execution) | Get data backing a node execution |
| [`sync_task_execution()`](#sync_task_execution) | Sync a FlyteTaskExecution object with its corresponding remote state |
| [`terminate()`](#terminate) | Terminate a workflow execution |
| [`upload_file()`](#upload_file) | Function will use remote's client to hash and then upload the file using Admin's data proxy service |
| [`wait()`](#wait) | Wait for an execution to finish |


#### activate_launchplan()

```python
def activate_launchplan(
    ident: Identifier,
):
```
Given a launchplan, activate it, all previous versions are deactivated.


| Parameter | Type |
|-|-|
| `ident` | `Identifier` |

#### approve()

```python
def approve(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### download()

```python
def download(
    data: typing.Union[LiteralsResolver, Literal, LiteralMap],
    download_to: str,
    recursive: bool,
):
```
Download the data to the specified location. If the data is a LiteralsResolver, LiteralMap and if recursive is
specified, then all file like objects will be recursively downloaded (e.g. FlyteFile/Dir (blob),
StructuredDataset etc).

Note: That it will use your sessions credentials to access the remote location. For sandbox, this should be
automatically configured, assuming you are running sandbox locally. For other environments, you will need to
configure your credentials appropriately.



| Parameter | Type |
|-|-|
| `data` | `typing.Union[LiteralsResolver, Literal, LiteralMap]` |
| `download_to` | `str` |
| `recursive` | `bool` |

#### execute()

```python
def execute(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a task, workflow, or launchplan, either something that's been declared locally, or a fetched entity.

This method supports:
- ``Flyte{Task, Workflow, LaunchPlan}`` remote module objects.
- ``@task``-decorated functions and ``TaskTemplate`` tasks.
- ``@workflow``-decorated functions.
- ``LaunchPlan`` objects.

For local entities, this code will attempt to find the entity first, and if missing, will compile and register
the object.

Not all arguments are relevant in all circumstances. For example, there's no reason to use the serialization
settings for entities that have already been registered on Admin.



| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan, FlyteWorkflow, PythonTask, WorkflowBase, LaunchPlan, ReferenceEntity]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_launch_plan()

```python
def execute_local_launch_plan(
    entity: LaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    name: typing.Optional[str],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a locally defined `LaunchPlan`.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `name` | `typing.Optional[str]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_task()

```python
def execute_local_task(
    entity: PythonTask,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute a @task-decorated function or TaskTemplate task.



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_local_workflow()

```python
def execute_local_workflow(
    entity: WorkflowBase,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    name: str,
    version: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    image_config: typing.Optional[ImageConfig],
    options: typing.Optional[Options],
    wait: bool,
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Execute an @workflow decorated function.



| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### execute_reference_launch_plan()

```python
def execute_reference_launch_plan(
    entity: ReferenceLaunchPlan,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceLaunchPlan.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceLaunchPlan` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_task()

```python
def execute_reference_task(
    entity: ReferenceTask,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceTask.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceTask` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_reference_workflow()

```python
def execute_reference_workflow(
    entity: ReferenceWorkflow,
    inputs: typing.Dict[str, typing.Any],
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a ReferenceWorkflow.


| Parameter | Type |
|-|-|
| `entity` | `ReferenceWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_task_lp()

```python
def execute_remote_task_lp(
    entity: typing.Union[FlyteTask, FlyteLaunchPlan],
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a FlyteTask, or FlyteLaunchplan.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteTask, FlyteLaunchPlan]` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### execute_remote_wf()

```python
def execute_remote_wf(
    entity: FlyteWorkflow,
    inputs: typing.Dict[str, typing.Any],
    project: str,
    domain: str,
    execution_name: typing.Optional[str],
    execution_name_prefix: typing.Optional[str],
    options: typing.Optional[Options],
    wait: bool,
    type_hints: typing.Optional[typing.Dict[str, typing.Type]],
    overwrite_cache: typing.Optional[bool],
    interruptible: typing.Optional[bool],
    envs: typing.Optional[typing.Dict[str, str]],
    tags: typing.Optional[typing.List[str]],
    cluster_pool: typing.Optional[str],
    execution_cluster_label: typing.Optional[str],
):
```
Execute a FlyteWorkflow.

NOTE: the name and version arguments are currently not used and only there consistency in the function signature


| Parameter | Type |
|-|-|
| `entity` | `FlyteWorkflow` |
| `inputs` | `typing.Dict[str, typing.Any]` |
| `project` | `str` |
| `domain` | `str` |
| `execution_name` | `typing.Optional[str]` |
| `execution_name_prefix` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `wait` | `bool` |
| `type_hints` | `typing.Optional[typing.Dict[str, typing.Type]]` |
| `overwrite_cache` | `typing.Optional[bool]` |
| `interruptible` | `typing.Optional[bool]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `tags` | `typing.Optional[typing.List[str]]` |
| `cluster_pool` | `typing.Optional[str]` |
| `execution_cluster_label` | `typing.Optional[str]` |

#### fast_package()

```python
def fast_package(
    root: os.PathLike,
    deref_symlinks: bool,
    output: str,
    options: typing.Optional[FastPackageOptions],
):
```
Packages the given paths into an installable zip and returns the md5_bytes and the URL of the uploaded location


| Parameter | Type |
|-|-|
| `root` | `os.PathLike` |
| `deref_symlinks` | `bool` |
| `output` | `str` |
| `options` | `typing.Optional[FastPackageOptions]` |

#### fast_register_workflow()

```python
def fast_register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
    fast_package_options: typing.Optional[FastPackageOptions],
):
```
Use this method to register a workflow with zip mode.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### fetch_active_launchplan()

```python
def fetch_active_launchplan(
    project: str,
    domain: str,
    name: str,
):
```
Returns the active version of the launch plan if it exists or returns None


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_execution()

```python
def fetch_execution(
    project: str,
    domain: str,
    name: str,
):
```
Fetch a workflow execution entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |

#### fetch_launch_plan()

```python
def fetch_launch_plan(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a launchplan entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task()

```python
def fetch_task(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a task entity from flyte admin.



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_task_lazy()

```python
def fetch_task_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Similar to fetch_task, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow()

```python
def fetch_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Fetch a workflow entity from flyte admin.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### fetch_workflow_lazy()

```python
def fetch_workflow_lazy(
    project: str,
    domain: str,
    name: str,
    version: str,
):
```
Similar to fetch_workflow, just that it returns a LazyEntity, which will fetch the workflow lazily.


| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `name` | `str` |
| `version` | `str` |

#### find_launch_plan()

```python
def find_launch_plan(
    lp_ref: id_models,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
):
```
| Parameter | Type |
|-|-|
| `lp_ref` | `id_models` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### find_launch_plan_for_node()

```python
def find_launch_plan_for_node(
    node: Node,
    node_launch_plans: Dict[id_models, launch_plan_models.LaunchPlanSpec],
):
```
| Parameter | Type |
|-|-|
| `node` | `Node` |
| `node_launch_plans` | `Dict[id_models, launch_plan_models.LaunchPlanSpec]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### for_sandbox()

```python
def for_sandbox(
    default_project: typing.Optional[str],
    default_domain: typing.Optional[str],
    data_upload_location: str,
    interactive_mode_enabled: bool,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `default_project` | `typing.Optional[str]` |
| `default_domain` | `typing.Optional[str]` |
| `data_upload_location` | `str` |
| `interactive_mode_enabled` | `bool` |
| `kwargs` | ``**kwargs`` |

#### generate_console_http_domain()

```python
def generate_console_http_domain()
```
This should generate the domain where console is hosted.

:return:


#### generate_console_url()

```python
def generate_console_url(
    entity: typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan],
):
```
Generate a Flyteconsole URL for the given Flyte remote endpoint.
This will automatically determine if this is an execution or an entity and change the type automatically


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[FlyteWorkflowExecution, FlyteNodeExecution, FlyteTaskExecution, FlyteWorkflow, FlyteTask, WorkflowExecutionIdentifier, Identifier, FlyteLaunchPlan]` |

#### get()

```python
def get(
    flyte_uri: typing.Optional[str],
):
```
General function that works with flyte tiny urls. This can return outputs (in the form of LiteralsResolver, or
individual Literals for singular requests), or HTML if passed a deck link, or bytes containing HTML,
if ipython is not available locally.


| Parameter | Type |
|-|-|
| `flyte_uri` | `typing.Optional[str]` |

#### get_domains()

```python
def get_domains()
```
Lists registered domains from flyte admin.

:returns: typing.List[flytekit.models.domain.Domain]


#### get_execution_metrics()

```python
def get_execution_metrics(
    id: WorkflowExecutionIdentifier,
    depth: int,
):
```
Get the metrics for a given execution.


| Parameter | Type |
|-|-|
| `id` | `WorkflowExecutionIdentifier` |
| `depth` | `int` |

#### get_extra_headers_for_protocol()

```python
def get_extra_headers_for_protocol(
    native_url,
):
```
| Parameter | Type |
|-|-|
| `native_url` |  |

#### launch_backfill()

```python
def launch_backfill(
    project: str,
    domain: str,
    from_date: datetime,
    to_date: datetime,
    launchplan: str,
    launchplan_version: str,
    execution_name: str,
    version: str,
    dry_run: bool,
    execute: bool,
    parallel: bool,
    failure_policy: typing.Optional[WorkflowFailurePolicy],
    overwrite_cache: typing.Optional[bool],
):
```
Creates and launches a backfill workflow for the given launchplan. If launchplan version is not specified,
then the latest launchplan is retrieved.
The from_date is exclusive and end_date is inclusive and backfill run for all instances in between. ::
-> (start_date - exclusive, end_date inclusive)

If dry_run is specified, the workflow is created and returned.
If execute==False is specified then the workflow is created and registered.
In the last case, the workflow is created, registered and executed.

The `parallel` flag can be used to generate a workflow where all launchplans can be run in parallel. Default
is that execute backfill is run sequentially



| Parameter | Type |
|-|-|
| `project` | `str` |
| `domain` | `str` |
| `from_date` | `datetime` |
| `to_date` | `datetime` |
| `launchplan` | `str` |
| `launchplan_version` | `str` |
| `execution_name` | `str` |
| `version` | `str` |
| `dry_run` | `bool` |
| `execute` | `bool` |
| `parallel` | `bool` |
| `failure_policy` | `typing.Optional[WorkflowFailurePolicy]` |
| `overwrite_cache` | `typing.Optional[bool]` |

#### list_projects()

```python
def list_projects(
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
    sort_by: typing.Optional[admin_common_models.Sort],
):
```
Lists registered projects from flyte admin.



| Parameter | Type |
|-|-|
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |
| `sort_by` | `typing.Optional[admin_common_models.Sort]` |

#### list_signals()

```python
def list_signals(
    execution_name: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: int,
    filters: typing.Optional[typing.List[filter_models.Filter]],
):
```
| Parameter | Type |
|-|-|
| `execution_name` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `int` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### list_tasks_by_version()

```python
def list_tasks_by_version(
    version: str,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
):
```
| Parameter | Type |
|-|-|
| `version` | `str` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |

#### raw_register()

```python
def raw_register(
    cp_entity: FlyteControlPlaneEntity,
    settings: SerializationSettings,
    version: str,
    create_default_launchplan: bool,
    options: Options,
    og_entity: FlyteLocalEntity,
):
```
Raw register method, can be used to register control plane entities. Usually if you have a Flyte Entity like a
WorkflowBase, Task, LaunchPlan then use other methods. This should be used only if you have already serialized entities



| Parameter | Type |
|-|-|
| `cp_entity` | `FlyteControlPlaneEntity` |
| `settings` | `SerializationSettings` |
| `version` | `str` |
| `create_default_launchplan` | `bool` |
| `options` | `Options` |
| `og_entity` | `FlyteLocalEntity` |

#### recent_executions()

```python
def recent_executions(
    project: typing.Optional[str],
    domain: typing.Optional[str],
    limit: typing.Optional[int],
    filters: typing.Optional[typing.List[filter_models.Filter]],
):
```
| Parameter | Type |
|-|-|
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `limit` | `typing.Optional[int]` |
| `filters` | `typing.Optional[typing.List[filter_models.Filter]]` |

#### register_launch_plan()

```python
def register_launch_plan(
    entity: LaunchPlan,
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    options: typing.Optional[Options],
    serialization_settings: typing.Optional[SerializationSettings],
):
```
Register a given launchplan, possibly applying overrides from the provided options. If the underlying workflow
is not already registered, it, along with any underlying entities, will also be registered. If the underlying
workflow does exist (with the given project/domain/version), then only the launchplan will be registered.



| Parameter | Type |
|-|-|
| `entity` | `LaunchPlan` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `options` | `typing.Optional[Options]` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |

#### register_script()

```python
def register_script(
    entity: typing.Union[WorkflowBase, PythonTask, LaunchPlan],
    image_config: typing.Optional[ImageConfig],
    version: typing.Optional[str],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    destination_dir: str,
    copy_all: bool,
    default_launch_plan: bool,
    options: typing.Optional[Options],
    source_path: typing.Optional[str],
    module_name: typing.Optional[str],
    envs: typing.Optional[typing.Dict[str, str]],
    fast_package_options: typing.Optional[FastPackageOptions],
):
```
Use this method to register a workflow via script mode.


| Parameter | Type |
|-|-|
| `entity` | `typing.Union[WorkflowBase, PythonTask, LaunchPlan]` |
| `image_config` | `typing.Optional[ImageConfig]` |
| `version` | `typing.Optional[str]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `destination_dir` | `str` |
| `copy_all` | `bool` |
| `default_launch_plan` | `bool` |
| `options` | `typing.Optional[Options]` |
| `source_path` | `typing.Optional[str]` |
| `module_name` | `typing.Optional[str]` |
| `envs` | `typing.Optional[typing.Dict[str, str]]` |
| `fast_package_options` | `typing.Optional[FastPackageOptions]` |

#### register_task()

```python
def register_task(
    entity: PythonTask,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
):
```
Register a qualified task (PythonTask) with Remote
For any conflicting parameters method arguments are regarded as overrides



| Parameter | Type |
|-|-|
| `entity` | `PythonTask` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |

#### register_workflow()

```python
def register_workflow(
    entity: WorkflowBase,
    serialization_settings: typing.Optional[SerializationSettings],
    version: typing.Optional[str],
    default_launch_plan: typing.Optional[bool],
    options: typing.Optional[Options],
):
```
Use this method to register a workflow.


| Parameter | Type |
|-|-|
| `entity` | `WorkflowBase` |
| `serialization_settings` | `typing.Optional[SerializationSettings]` |
| `version` | `typing.Optional[str]` |
| `default_launch_plan` | `typing.Optional[bool]` |
| `options` | `typing.Optional[Options]` |

#### reject()

```python
def reject(
    signal_id: str,
    execution_name: str,
    project: str,
    domain: str,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `project` | `str` |
| `domain` | `str` |

#### remote_context()

```python
def remote_context()
```
Context manager with remote-specific configuration.


#### set_input()

```python
def set_input(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project,
    domain,
    python_type,
    literal_type,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` |  |
| `domain` |  |
| `python_type` |  |
| `literal_type` |  |

#### set_signal()

```python
def set_signal(
    signal_id: str,
    execution_name: str,
    value: typing.Union[literal_models.Literal, typing.Any],
    project: typing.Optional[str],
    domain: typing.Optional[str],
    python_type: typing.Optional[typing.Type],
    literal_type: typing.Optional[type_models.LiteralType],
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_name` | `str` |
| `value` | `typing.Union[literal_models.Literal, typing.Any]` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `python_type` | `typing.Optional[typing.Type]` |
| `literal_type` | `typing.Optional[type_models.LiteralType]` |

#### sync()

```python
def sync(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
):
```
This function was previously a singledispatchmethod. We've removed that but this function remains
so that we don't break people.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_execution()

```python
def sync_execution(
    execution: FlyteWorkflowExecution,
    entity_definition: typing.Union[FlyteWorkflow, FlyteTask],
    sync_nodes: bool,
):
```
Sync a FlyteWorkflowExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `entity_definition` | `typing.Union[FlyteWorkflow, FlyteTask]` |
| `sync_nodes` | `bool` |

#### sync_node_execution()

```python
def sync_node_execution(
    execution: FlyteNodeExecution,
    node_mapping: typing.Dict[str, FlyteNode],
):
```
Get data backing a node execution. These FlyteNodeExecution objects should've come from Admin with the model
fields already populated correctly. For purposes of the remote experience, we'd like to supplement the object
with some additional fields:
- inputs/outputs
- task/workflow executions, and/or underlying node executions in the case of parent nodes
- TypedInterface (remote wrapper type)

A node can have several different types of executions behind it. That is, the node could've run (perhaps
multiple times because of retries):
- A task
- A static subworkflow
- A dynamic subworkflow (which in turn may have run additional tasks, subwfs, and/or launch plans)
- A launch plan

The data model is complicated, so ascertaining which of these happened is a bit tricky. That logic is
encapsulated in this function.


| Parameter | Type |
|-|-|
| `execution` | `FlyteNodeExecution` |
| `node_mapping` | `typing.Dict[str, FlyteNode]` |

#### sync_task_execution()

```python
def sync_task_execution(
    execution: FlyteTaskExecution,
    entity_interface: typing.Optional[TypedInterface],
):
```
Sync a FlyteTaskExecution object with its corresponding remote state.


| Parameter | Type |
|-|-|
| `execution` | `FlyteTaskExecution` |
| `entity_interface` | `typing.Optional[TypedInterface]` |

#### terminate()

```python
def terminate(
    execution: FlyteWorkflowExecution,
    cause: str,
):
```
Terminate a workflow execution.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `cause` | `str` |

#### upload_file()

```python
def upload_file(
    to_upload: pathlib.Path,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    filename_root: typing.Optional[str],
):
```
Function will use remote's client to hash and then upload the file using Admin's data proxy service.



| Parameter | Type |
|-|-|
| `to_upload` | `pathlib.Path` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `filename_root` | `typing.Optional[str]` |

#### wait()

```python
def wait(
    execution: FlyteWorkflowExecution,
    timeout: typing.Optional[typing.Union[timedelta, int]],
    poll_interval: typing.Optional[typing.Union[timedelta, int]],
    sync_nodes: bool,
):
```
Wait for an execution to finish.



| Parameter | Type |
|-|-|
| `execution` | `FlyteWorkflowExecution` |
| `timeout` | `typing.Optional[typing.Union[timedelta, int]]` |
| `poll_interval` | `typing.Optional[typing.Union[timedelta, int]]` |
| `sync_nodes` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| client |  |  |
| config |  |  |
| context |  |  |
| default_domain |  |  |
| default_project |  |  |
| file_access |  |  |
| interactive_mode_enabled |  |  |

## flytekit.clis.sdk_in_container.get.Identifier

```python
def Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
):
```
| Parameter | Type |
|-|-|
| `resource_type` |  |
| `project` |  |
| `domain` |  |
| `name` |  |
| `version` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier |
| [`promote_from_model()`](#promote_from_model) |  |
| [`resource_type_name()`](#resource_type_name) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
):
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
):
```
| Parameter | Type |
|-|-|
| `base_model` |  |

#### resource_type_name()

```python
def resource_type_name()
```
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
| domain |  |  |
| is_empty |  |  |
| name |  |  |
| project |  |  |
| resource_type |  |  |
| version |  |  |

## flytekit.clis.sdk_in_container.get.LaunchPlanState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
):
```
| Parameter | Type |
|-|-|
| `val` |  |

## flytekit.clis.sdk_in_container.get.NamedEntityIdentifier

```python
def NamedEntityIdentifier(
    project,
    domain,
    name,
):
```
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | Stores object to a Flyte-IDL defined protobuf |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
):
```
| Parameter | Type |
|-|-|
| `idl_object` |  |

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
Stores object to a Flyte-IDL defined protobuf.


#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| domain |  |  |
| is_empty |  |  |
| name |  |  |
| project |  |  |

## flytekit.clis.sdk_in_container.get.ResourceType

## flytekit.clis.sdk_in_container.get.Sort

```python
def Sort(
    key,
    direction,
):
```
| Parameter | Type |
|-|-|
| `key` |  |
| `direction` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    text,
):
```
| Parameter | Type |
|-|-|
| `text` |  |

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
| direction |  |  |
| is_empty |  |  |
| key |  |  |

## flytekit.clis.sdk_in_container.get.Table

A console renderable to draw a table.



```python
def Table(
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
):
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
| [`add_column()`](#add_column) | Add a column to the table |
| [`add_row()`](#add_row) | Add a row of renderables |
| [`add_section()`](#add_section) | Add a new section (draw a line after current row) |
| [`get_row_style()`](#get_row_style) | Get the current row style |
| [`grid()`](#grid) | Get a table with no lines, headers, or footer |


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
):
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
):
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
):
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
):
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
| expand |  |  |
| padding |  |  |
| row_count |  |  |

