---
title: flytekit.clis.sdk_in_container.utils
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.clis.sdk_in_container.utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`Console`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsconsole) | A high level console interface. |
| [`ErrorHandlingCommand`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilserrorhandlingcommand) | Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way. |
| [`Field`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsfield) |  |
| [`MappingProxyType`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsmappingproxytype) | Read-only proxy of a mapping. |
| [`Panel`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspanel) | A console renderable that draws a border around its contents. |
| [`PyFlyteParams`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilspyflyteparams) |  |
| [`Syntax`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilssyntax) | Construct a Syntax object to render syntax highlighted code. |
| [`Traceback`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilstraceback) | A Console renderable that renders a traceback. |

### Errors

| Exception | Description |
|-|-|
| [`FlyteCompilationException`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflytecompilationexception) | Common base class for all non-exit exceptions. |
| [`FlyteException`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflyteexception) | Common base class for all non-exit exceptions. |
| [`FlyteInvalidInputException`](.././flytekit.clis.sdk_in_container.utils#flytekitclissdk_in_containerutilsflyteinvalidinputexception) | Common base class for all non-exit exceptions. |

### Methods

| Method | Description |
|-|-|
| [`annotate_exception_with_code()`](#annotate_exception_with_code) | Annotate the exception with the source code, and will be printed in the rich panel. |
| [`dataclass()`](#dataclass) | Add dunder methods based on the fields defined in the class. |
| [`domain_option_dec()`](#domain_option_dec) |  |
| [`field()`](#field) | Return an object to identify dataclass fields. |
| [`get_level_from_cli_verbosity()`](#get_level_from_cli_verbosity) | Converts a verbosity level from the CLI to a logging level. |
| [`get_option_from_metadata()`](#get_option_from_metadata) |  |
| [`make_click_option_field()`](#make_click_option_field) |  |
| [`pretty_print_exception()`](#pretty_print_exception) | This method will print the exception in a nice way. |
| [`pretty_print_grpc_error()`](#pretty_print_grpc_error) | This method will print the grpc error that us more human readable. |
| [`pretty_print_traceback()`](#pretty_print_traceback) | This method will print the Traceback of an error. |
| [`project_option_dec()`](#project_option_dec) |  |
| [`remove_unwanted_traceback_frames()`](#remove_unwanted_traceback_frames) | Custom function to remove certain frames from the traceback. |
| [`validate_package()`](#validate_package) | This method will validate the packages passed in by the user. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SOURCE_CODE` | `str` |  |
| `domain_option` | `Option` |  |
| `logger` | `Logger` |  |
| `project_option` | `Option` |  |

## Methods

#### annotate_exception_with_code()

```python
def annotate_exception_with_code(
    exception: flytekit.exceptions.user.FlyteUserException,
    fn: typing.Callable,
    param_name: typing.Optional[str],
) -> flytekit.exceptions.user.FlyteUserException
```
Annotate the exception with the source code, and will be printed in the rich panel.


| Parameter | Type |
|-|-|
| `exception` | `flytekit.exceptions.user.FlyteUserException` |
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

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

#### domain_option_dec()

```python
def domain_option_dec(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### field()

```python
def field(
    default,
    default_factory,
    init,
    repr,
    hash,
    compare,
    metadata,
    kw_only,
)
```
Return an object to identify dataclass fields.

default is the default value of the field.  default_factory is a
0-argument function called to initialize a field's value.  If init
is true, the field will be a parameter to the class's __init__()
function.  If repr is true, the field will be included in the
object's repr().  If hash is true, the field will be included in the
object's hash().  If compare is true, the field will be used in
comparison functions.  metadata, if specified, must be a mapping
which is stored but not otherwise examined by dataclass.  If kw_only
is true, the field will become a keyword-only parameter to
__init__().

It is an error to specify both default and default_factory.


| Parameter | Type |
|-|-|
| `default` |  |
| `default_factory` |  |
| `init` |  |
| `repr` |  |
| `hash` |  |
| `compare` |  |
| `metadata` |  |
| `kw_only` |  |

#### get_level_from_cli_verbosity()

```python
def get_level_from_cli_verbosity(
    verbosity: int,
) -> int
```
Converts a verbosity level from the CLI to a logging level.



| Parameter | Type |
|-|-|
| `verbosity` | `int` |

#### get_option_from_metadata()

```python
def get_option_from_metadata(
    metadata: mappingproxy,
) -> click.core.Option
```
| Parameter | Type |
|-|-|
| `metadata` | `mappingproxy` |

#### make_click_option_field()

```python
def make_click_option_field(
    o: click.core.Option,
) -> dataclasses.Field
```
| Parameter | Type |
|-|-|
| `o` | `click.core.Option` |

#### pretty_print_exception()

```python
def pretty_print_exception(
    e: Exception,
    verbosity: int,
)
```
This method will print the exception in a nice way. It will also check if the exception is a grpc.RpcError and
print it in a human-readable way.


| Parameter | Type |
|-|-|
| `e` | `Exception` |
| `verbosity` | `int` |

#### pretty_print_grpc_error()

```python
def pretty_print_grpc_error(
    e: grpc.RpcError,
)
```
This method will print the grpc error that us more human readable.


| Parameter | Type |
|-|-|
| `e` | `grpc.RpcError` |

#### pretty_print_traceback()

```python
def pretty_print_traceback(
    e: Exception,
    verbosity: int,
)
```
This method will print the Traceback of an error.
Print the traceback in a nice formatted way if verbose is set to True.


| Parameter | Type |
|-|-|
| `e` | `Exception` |
| `verbosity` | `int` |

#### project_option_dec()

```python
def project_option_dec(
    f: ~FC,
) -> ~FC
```
| Parameter | Type |
|-|-|
| `f` | `~FC` |

#### remove_unwanted_traceback_frames()

```python
def remove_unwanted_traceback_frames(
    tb: traceback,
    unwanted_module_names: typing.List[str],
) -> traceback
```
Custom function to remove certain frames from the traceback.


| Parameter | Type |
|-|-|
| `tb` | `traceback` |
| `unwanted_module_names` | `typing.List[str]` |

#### validate_package()

```python
def validate_package(
    ctx,
    param,
    values,
)
```
This method will validate the packages passed in by the user. It will check that the packages are in the correct
format, and will also split the packages if the user passed in a comma separated list.


| Parameter | Type |
|-|-|
| `ctx` |  |
| `param` |  |
| `values` |  |

## flytekit.clis.sdk_in_container.utils.Console

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

## flytekit.clis.sdk_in_container.utils.ErrorHandlingCommand

Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way.


```python
class ErrorHandlingCommand(
    args: `*args`,
    kwargs: `**kwargs`,
)
```
Initialize RichGroup class.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Registers another :class:`Command` with this group. |
| [`collect_usage_pieces()`](#collect_usage_pieces) | Returns all the pieces that go into the usage line and returns. |
| [`command()`](#command) | A shortcut decorator for declaring and attaching a command to. |
| [`format_commands()`](#format_commands) | Extra format methods for multi methods that adds all the commands. |
| [`format_epilog()`](#format_epilog) | Writes the epilog into the formatter if it exists. |
| [`format_help()`](#format_help) | Writes the help into the formatter if it exists. |
| [`format_help_text()`](#format_help_text) | Writes the help text to the formatter if it exists. |
| [`format_options()`](#format_options) | Writes all the options into the formatter if they exist. |
| [`format_usage()`](#format_usage) | Writes the usage line into the formatter. |
| [`get_command()`](#get_command) | Given a context and a command name, this returns a. |
| [`get_help()`](#get_help) | Formats the help into a string and returns it. |
| [`get_help_option()`](#get_help_option) | Returns the help option object. |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option. |
| [`get_params()`](#get_params) |  |
| [`get_short_help_str()`](#get_short_help_str) | Gets short help for the command or makes it by shortening the. |
| [`get_usage()`](#get_usage) | Formats the usage line into a string and returns it. |
| [`group()`](#group) | A shortcut decorator for declaring and attaching a group to. |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists). |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should. |
| [`main()`](#main) | This is the way to invoke a script with all the bells and. |
| [`make_context()`](#make_context) | This function when given an info name and arguments will kick. |
| [`make_parser()`](#make_parser) | Creates the underlying option parser for this command. |
| [`parse_args()`](#parse_args) | Given a context and a list of arguments this creates the parser. |
| [`resolve_command()`](#resolve_command) |  |
| [`result_callback()`](#result_callback) | Adds a result callback to the command. |
| [`shell_complete()`](#shell_complete) | Return a list of completions for the incomplete value. |
| [`to_info_dict()`](#to_info_dict) | Gather information that could be useful for a tool generating. |


#### add_command()

```python
def add_command(
    cmd: click.core.Command,
    name: typing.Optional[str],
)
```
Registers another :class:`Command` with this group.  If the name
is not provided, the name of the command is used.


| Parameter | Type |
|-|-|
| `cmd` | `click.core.Command` |
| `name` | `typing.Optional[str]` |

#### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### command()

```python
def command(
    args: `*args`,
    kwargs: `**kwargs`,
) -> typing.Union[typing.Callable[[typing.Callable[..., typing.Any]], rich_click.rich_command.RichCommand], rich_click.rich_command.RichCommand]
```
A shortcut decorator for declaring and attaching a command to
the group. This takes the same arguments as :func:`command` and
immediately registers the created command with this group by
calling :meth:`add_command`.

To customize the command class used, set the
:attr:`command_class` attribute.

.. versionchanged:: 8.1
This decorator can be applied without parentheses.

.. versionchanged:: 8.0
Added the :attr:`command_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### format_commands()

```python
def format_commands(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Extra format methods for multi methods that adds all the commands
after the options.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_epilog()

```python
def format_epilog(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the epilog into the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_help()

```python
def format_help(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the help into the formatter if it exists.

This is a low-level method called by :meth:`get_help`.

This calls the following methods:

-   :meth:`format_usage`
-   :meth:`format_help_text`
-   :meth:`format_options`
-   :meth:`format_epilog`


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_help_text()

```python
def format_help_text(
    ctx: rich_click.rich_context.RichContext,
    formatter: rich_click.rich_help_formatter.RichHelpFormatter,
)
```
Writes the help text to the formatter if it exists.


| Parameter | Type |
|-|-|
| `ctx` | `rich_click.rich_context.RichContext` |
| `formatter` | `rich_click.rich_help_formatter.RichHelpFormatter` |

#### format_options()

```python
def format_options(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
)
```
Writes all the options into the formatter if they exist.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### format_usage()

```python
def format_usage(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
)
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `formatter` | `click.formatting.HelpFormatter` |

#### get_command()

```python
def get_command(
    ctx: click.core.Context,
    cmd_name: str,
) -> typing.Optional[click.core.Command]
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `cmd_name` | `str` |

#### get_help()

```python
def get_help(
    ctx: click.core.Context,
) -> str
```
Formats the help into a string and returns it.

Calls :meth:`format_help` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option()

```python
def get_help_option(
    ctx: click.core.Context,
) -> typing.Optional[ForwardRef('Option')]
```
Returns the help option object.

Unless ``add_help_option`` is ``False``.

.. versionchanged:: 8.1.8
The help option is now cached to avoid creating it multiple times.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_help_option_names()

```python
def get_help_option_names(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns the names for the help option.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_params()

```python
def get_params(
    ctx: click.core.Context,
) -> typing.List[ForwardRef('Parameter')]
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
) -> str
```
Gets short help for the command or makes it by shortening the
long help string.


| Parameter | Type |
|-|-|
| `limit` | `int` |

#### get_usage()

```python
def get_usage(
    ctx: click.core.Context,
) -> str
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### group()

```python
def group(
    args: `*args`,
    kwargs: `**kwargs`,
) -> typing.Union[typing.Callable[[typing.Callable[..., typing.Any]], ForwardRef('RichGroup')], ForwardRef('RichGroup')]
```
A shortcut decorator for declaring and attaching a group to
the group. This takes the same arguments as :func:`group` and
immediately registers the created group with this group by
calling :meth:`add_command`.

To customize the group class used, set the :attr:`group_class`
attribute.

.. versionchanged:: 8.1
This decorator can be applied without parentheses.

.. versionchanged:: 8.0
Added the :attr:`group_class` attribute.


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### invoke()

```python
def invoke(
    ctx: click.core.Context,
) -> typing.Any
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### list_commands()

```python
def list_commands(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### main()

```python
def main(
    args: `*args`,
    prog_name: typing.Optional[str],
    complete_var: typing.Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: typing.Any,
) -> typing.Any
```
This is the way to invoke a script with all the bells and
whistles as a command line application.  This will always terminate
the application after a call.  If this is not wanted, ``SystemExit``
needs to be caught.

This method is also available by directly calling the instance of
a :class:`Command`.



| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `prog_name` | `typing.Optional[str]` |
| `complete_var` | `typing.Optional[str]` |
| `standalone_mode` | `bool` |
| `windows_expand_args` | `bool` |
| `extra` | `typing.Any` |

#### make_context()

```python
def make_context(
    info_name: typing.Optional[str],
    args: `*args`,
    parent: typing.Optional[click.core.Context],
    extra: typing.Any,
) -> rich_click.rich_context.RichContext
```
This function when given an info name and arguments will kick
off the parsing and create a new :class:`Context`.  It does not
invoke the actual command callback though.

To quickly customize the context class used without overriding
this method, set the :attr:`context_class` attribute.



| Parameter | Type |
|-|-|
| `info_name` | `typing.Optional[str]` |
| `args` | ``*args`` |
| `parent` | `typing.Optional[click.core.Context]` |
| `extra` | `typing.Any` |

#### make_parser()

```python
def make_parser(
    ctx: click.core.Context,
) -> click.parser.OptionParser
```
Creates the underlying option parser for this command.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

#### parse_args()

```python
def parse_args(
    ctx: click.core.Context,
    args: `*args`,
) -> typing.List[str]
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### resolve_command()

```python
def resolve_command(
    ctx: click.core.Context,
    args: `*args`,
) -> typing.Tuple[typing.Optional[str], typing.Optional[click.core.Command], typing.List[str]]
```
| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `args` | ``*args`` |

#### result_callback()

```python
def result_callback(
    replace: bool,
) -> typing.Callable[[~F], ~F]
```
Adds a result callback to the command.  By default if a
result callback is already registered this will chain them but
this can be disabled with the `replace` parameter.  The result
callback is invoked with the return value of the subcommand
(or the list of return values from all subcommands if chaining
is enabled) as well as the parameters as they would be passed
to the main callback.

Example::

@click.group()
@click.option('-i', '--input', default=23)
def cli(input):
return 42

@cli.result_callback()
def process_result(result, input):
return result + input



| Parameter | Type |
|-|-|
| `replace` | `bool` |

#### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of completions for the incomplete value. Looks
at the names of options, subcommands, and chained
multi-commands.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |
| `incomplete` | `str` |

#### to_info_dict()

```python
def to_info_dict(
    ctx: click.core.Context,
) -> typing.Dict[str, typing.Any]
```
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.



| Parameter | Type |
|-|-|
| `ctx` | `click.core.Context` |

### Properties

| Property | Type | Description |
|-|-|-|
| `console` |  | {{< multiline >}}Rich Console.

This is a separate instance from the help formatter that allows full control of the
console configuration.

See `rich_config` decorator for how to apply the settings.
{{< /multiline >}} |
| `help_config` |  | {{< multiline >}}Rich Help Configuration.
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.Field

```python
class Field(
    default,
    default_factory,
    init,
    repr,
    hash,
    compare,
    metadata,
    kw_only,
)
```
| Parameter | Type |
|-|-|
| `default` |  |
| `default_factory` |  |
| `init` |  |
| `repr` |  |
| `hash` |  |
| `compare` |  |
| `metadata` |  |
| `kw_only` |  |

## flytekit.clis.sdk_in_container.utils.FlyteCompilationException

Common base class for all non-exit exceptions.


```python
class FlyteCompilationException(
    fn: typing.Callable,
    param_name: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `fn` | `typing.Callable` |
| `param_name` | `typing.Optional[str]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.FlyteException

Common base class for all non-exit exceptions.


```python
class FlyteException(
    args,
    timestamp: typing.Optional[float],
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `timestamp` | `typing.Optional[float]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.FlyteInvalidInputException

Common base class for all non-exit exceptions.


```python
class FlyteInvalidInputException(
    request: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `request` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `timestamp` |  | {{< multiline >}}The timestamp as fractional seconds since epoch
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.MappingProxyType

Read-only proxy of a mapping.


## flytekit.clis.sdk_in_container.utils.Panel

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

## flytekit.clis.sdk_in_container.utils.PyFlyteParams

```python
class PyFlyteParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[str]` |
| `verbose` | `bool` |
| `pkgs` | `typing.List[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |


#### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> PyFlyteParams
```
| Parameter | Type |
|-|-|
| `d` | `typing.Dict[str, typing.Any]` |

## flytekit.clis.sdk_in_container.utils.Syntax

Construct a Syntax object to render syntax highlighted code.



```python
class Syntax(
    code: str,
    lexer: typing.Union[pygments.lexer.Lexer, str],
    theme: typing.Union[str, rich.syntax.SyntaxTheme],
    dedent: bool,
    line_numbers: bool,
    start_line: int,
    line_range: typing.Optional[typing.Tuple[typing.Optional[int], typing.Optional[int]]],
    highlight_lines: typing.Optional[typing.Set[int]],
    code_width: typing.Optional[int],
    tab_size: int,
    word_wrap: bool,
    background_color: typing.Optional[str],
    indent_guides: bool,
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
)
```
| Parameter | Type |
|-|-|
| `code` | `str` |
| `lexer` | `typing.Union[pygments.lexer.Lexer, str]` |
| `theme` | `typing.Union[str, rich.syntax.SyntaxTheme]` |
| `dedent` | `bool` |
| `line_numbers` | `bool` |
| `start_line` | `int` |
| `line_range` | `typing.Optional[typing.Tuple[typing.Optional[int], typing.Optional[int]]]` |
| `highlight_lines` | `typing.Optional[typing.Set[int]]` |
| `code_width` | `typing.Optional[int]` |
| `tab_size` | `int` |
| `word_wrap` | `bool` |
| `background_color` | `typing.Optional[str]` |
| `indent_guides` | `bool` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |

### Methods

| Method | Description |
|-|-|
| [`from_path()`](#from_path) | Construct a Syntax object from a file. |
| [`get_theme()`](#get_theme) | Get a syntax theme instance. |
| [`guess_lexer()`](#guess_lexer) | Guess the alias of the Pygments lexer to use based on a path and an optional string of code. |
| [`highlight()`](#highlight) | Highlight code and return a Text instance. |
| [`stylize_range()`](#stylize_range) | Adds a custom style on a part of the code, that will be applied to the syntax display when it's rendered. |


#### from_path()

```python
def from_path(
    path: str,
    encoding: str,
    lexer: typing.Union[pygments.lexer.Lexer, str, NoneType],
    theme: typing.Union[str, rich.syntax.SyntaxTheme],
    dedent: bool,
    line_numbers: bool,
    line_range: typing.Optional[typing.Tuple[int, int]],
    start_line: int,
    highlight_lines: typing.Optional[typing.Set[int]],
    code_width: typing.Optional[int],
    tab_size: int,
    word_wrap: bool,
    background_color: typing.Optional[str],
    indent_guides: bool,
    padding: typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]],
) -> Syntax
```
Construct a Syntax object from a file.



| Parameter | Type |
|-|-|
| `path` | `str` |
| `encoding` | `str` |
| `lexer` | `typing.Union[pygments.lexer.Lexer, str, NoneType]` |
| `theme` | `typing.Union[str, rich.syntax.SyntaxTheme]` |
| `dedent` | `bool` |
| `line_numbers` | `bool` |
| `line_range` | `typing.Optional[typing.Tuple[int, int]]` |
| `start_line` | `int` |
| `highlight_lines` | `typing.Optional[typing.Set[int]]` |
| `code_width` | `typing.Optional[int]` |
| `tab_size` | `int` |
| `word_wrap` | `bool` |
| `background_color` | `typing.Optional[str]` |
| `indent_guides` | `bool` |
| `padding` | `typing.Union[int, typing.Tuple[int], typing.Tuple[int, int], typing.Tuple[int, int, int, int]]` |

#### get_theme()

```python
def get_theme(
    name: typing.Union[str, rich.syntax.SyntaxTheme],
) -> rich.syntax.SyntaxTheme
```
Get a syntax theme instance.


| Parameter | Type |
|-|-|
| `name` | `typing.Union[str, rich.syntax.SyntaxTheme]` |

#### guess_lexer()

```python
def guess_lexer(
    path: str,
    code: typing.Optional[str],
) -> str
```
Guess the alias of the Pygments lexer to use based on a path and an optional string of code.
If code is supplied, it will use a combination of the code and the filename to determine the
best lexer to use. For example, if the file is ``index.html`` and the file contains Django
templating syntax, then "html+django" will be returned. If the file is ``index.html``, and no
templating language is used, the "html" lexer will be used. If no string of code
is supplied, the lexer will be chosen based on the file extension..



| Parameter | Type |
|-|-|
| `path` | `str` |
| `code` | `typing.Optional[str]` |

#### highlight()

```python
def highlight(
    code: str,
    line_range: typing.Optional[typing.Tuple[typing.Optional[int], typing.Optional[int]]],
) -> rich.text.Text
```
Highlight code and return a Text instance.



| Parameter | Type |
|-|-|
| `code` | `str` |
| `line_range` | `typing.Optional[typing.Tuple[typing.Optional[int], typing.Optional[int]]]` |

#### stylize_range()

```python
def stylize_range(
    style: typing.Union[str, ForwardRef('Style')],
    start: typing.Tuple[int, int],
    end: typing.Tuple[int, int],
    style_before: bool,
)
```
Adds a custom style on a part of the code, that will be applied to the syntax display when it's rendered.
Line numbers are 1-based, while column indexes are 0-based.



| Parameter | Type |
|-|-|
| `style` | `typing.Union[str, ForwardRef('Style')]` |
| `start` | `typing.Tuple[int, int]` |
| `end` | `typing.Tuple[int, int]` |
| `style_before` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `default_lexer` |  | {{< multiline >}}A Pygments Lexer to use if one is not specified or invalid.
{{< /multiline >}} |
| `lexer` |  | {{< multiline >}}The lexer for this syntax, or None if no lexer was found.

Tries to find the lexer by name if a string was passed to the constructor.
{{< /multiline >}} |

## flytekit.clis.sdk_in_container.utils.Traceback

A Console renderable that renders a traceback.



```python
class Traceback(
    trace: typing.Optional[rich.traceback.Trace],
    width: typing.Optional[int],
    code_width: typing.Optional[int],
    extra_lines: int,
    theme: typing.Optional[str],
    word_wrap: bool,
    show_locals: bool,
    locals_max_length: int,
    locals_max_string: int,
    locals_hide_dunder: bool,
    locals_hide_sunder: bool,
    indent_guides: bool,
    suppress: typing.Iterable[typing.Union[str, module]],
    max_frames: int,
)
```
| Parameter | Type |
|-|-|
| `trace` | `typing.Optional[rich.traceback.Trace]` |
| `width` | `typing.Optional[int]` |
| `code_width` | `typing.Optional[int]` |
| `extra_lines` | `int` |
| `theme` | `typing.Optional[str]` |
| `word_wrap` | `bool` |
| `show_locals` | `bool` |
| `locals_max_length` | `int` |
| `locals_max_string` | `int` |
| `locals_hide_dunder` | `bool` |
| `locals_hide_sunder` | `bool` |
| `indent_guides` | `bool` |
| `suppress` | `typing.Iterable[typing.Union[str, module]]` |
| `max_frames` | `int` |

### Methods

| Method | Description |
|-|-|
| [`extract()`](#extract) | Extract traceback information. |
| [`from_exception()`](#from_exception) | Create a traceback from exception info. |


#### extract()

```python
def extract(
    exc_type: typing.Type[BaseException],
    exc_value: BaseException,
    traceback: typing.Optional[traceback],
    show_locals: bool,
    locals_max_length: int,
    locals_max_string: int,
    locals_hide_dunder: bool,
    locals_hide_sunder: bool,
) -> rich.traceback.Trace
```
Extract traceback information.



| Parameter | Type |
|-|-|
| `exc_type` | `typing.Type[BaseException]` |
| `exc_value` | `BaseException` |
| `traceback` | `typing.Optional[traceback]` |
| `show_locals` | `bool` |
| `locals_max_length` | `int` |
| `locals_max_string` | `int` |
| `locals_hide_dunder` | `bool` |
| `locals_hide_sunder` | `bool` |

#### from_exception()

```python
def from_exception(
    exc_type: typing.Type[typing.Any],
    exc_value: BaseException,
    traceback: typing.Optional[traceback],
    width: typing.Optional[int],
    code_width: typing.Optional[int],
    extra_lines: int,
    theme: typing.Optional[str],
    word_wrap: bool,
    show_locals: bool,
    locals_max_length: int,
    locals_max_string: int,
    locals_hide_dunder: bool,
    locals_hide_sunder: bool,
    indent_guides: bool,
    suppress: typing.Iterable[typing.Union[str, module]],
    max_frames: int,
) -> Traceback
```
Create a traceback from exception info



| Parameter | Type |
|-|-|
| `exc_type` | `typing.Type[typing.Any]` |
| `exc_value` | `BaseException` |
| `traceback` | `typing.Optional[traceback]` |
| `width` | `typing.Optional[int]` |
| `code_width` | `typing.Optional[int]` |
| `extra_lines` | `int` |
| `theme` | `typing.Optional[str]` |
| `word_wrap` | `bool` |
| `show_locals` | `bool` |
| `locals_max_length` | `int` |
| `locals_max_string` | `int` |
| `locals_hide_dunder` | `bool` |
| `locals_hide_sunder` | `bool` |
| `indent_guides` | `bool` |
| `suppress` | `typing.Iterable[typing.Union[str, module]]` |
| `max_frames` | `int` |

