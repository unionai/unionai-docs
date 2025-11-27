---
title: ErrorHandlingCommand
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ErrorHandlingCommand

**Package:** `flytekit.clis.sdk_in_container.utils`

Helper class that wraps the invoke method of a click command to catch exceptions and print them in a nice way.


```python
class ErrorHandlingCommand(
    args: *args,
    kwargs: **kwargs,
)
```
Create RichGroup instance.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`add_command()`](#add_command) | Register another :class:`Command` with this group. |
| [`add_command_to_panel()`](#add_command_to_panel) |  |
| [`add_panel()`](#add_panel) | Add a RichPanel to the RichCommand. |
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
| [`get_help_option()`](#get_help_option) | Return the help option object. |
| [`get_help_option_names()`](#get_help_option_names) | Returns the names for the help option. |
| [`get_params()`](#get_params) |  |
| [`get_rich_table_row()`](#get_rich_table_row) | Create a row for the rich table corresponding with this parameter. |
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


### add_command()

```python
def add_command(
    cmd: click.Command,
    name: Optional[str],
    aliases: Optional[Iterable[str]],
    panel: Optional[Union[str, List[str]]],
)
```
Register another :class:`Command` with this group. If the name
is not provided, the name of the command is used.


| Parameter | Type | Description |
|-|-|-|
| `cmd` | `click.Command` | |
| `name` | `Optional[str]` | |
| `aliases` | `Optional[Iterable[str]]` | |
| `panel` | `Optional[Union[str, List[str]]]` | |

### add_command_to_panel()

```python
def add_command_to_panel(
    command: click.Command,
    panel_name: Union[str, Iterable[str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `command` | `click.Command` | |
| `panel_name` | `Union[str, Iterable[str]]` | |

### add_panel()

```python
def add_panel(
    panel: 'RichPanel[Any, Any]',
)
```
Add a RichPanel to the RichCommand.


| Parameter | Type | Description |
|-|-|-|
| `panel` | `'RichPanel[Any, Any]'` | |

### collect_usage_pieces()

```python
def collect_usage_pieces(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns all the pieces that go into the usage line and returns
it as a list of strings.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### command()

```python
def command(
    args: *args,
    kwargs: **kwargs,
) -> Union[Callable[[Callable[..., Any]], RichCommand], RichCommand]
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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### format_commands()

```python
def format_commands(
    ctx: click.Context,
    formatter: click.HelpFormatter,
)
```
Extra format methods for multi methods that adds all the commands
after the options.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |
| `formatter` | `click.HelpFormatter` | |

### format_epilog()

```python
def format_epilog(
    ctx: RichContext,
    formatter: RichHelpFormatter,
)
```
Writes the epilog into the formatter if it exists.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `RichContext` | |
| `formatter` | `RichHelpFormatter` | |

### format_help()

```python
def format_help(
    ctx: RichContext,
    formatter: RichHelpFormatter,
)
```
Writes the help into the formatter if it exists.

This is a low-level method called by :meth:`get_help`.

This calls the following methods:

-   :meth:`format_usage`
-   :meth:`format_help_text`
-   :meth:`format_options`
-   :meth:`format_epilog`


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `RichContext` | |
| `formatter` | `RichHelpFormatter` | |

### format_help_text()

```python
def format_help_text(
    ctx: RichContext,
    formatter: RichHelpFormatter,
)
```
Writes the help text to the formatter if it exists.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `RichContext` | |
| `formatter` | `RichHelpFormatter` | |

### format_options()

```python
def format_options(
    ctx: click.Context,
    formatter: click.HelpFormatter,
)
```
Writes all the options into the formatter if they exist.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |
| `formatter` | `click.HelpFormatter` | |

### format_usage()

```python
def format_usage(
    ctx: click.core.Context,
    formatter: click.formatting.HelpFormatter,
)
```
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `formatter` | `click.formatting.HelpFormatter` | |

### get_command()

```python
def get_command(
    ctx: click.Context,
    cmd_name: str,
) -> Optional[click.Command]
```
Given a context and a command name, this returns a
:class:`Command` object if it exists or returns `None`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |
| `cmd_name` | `str` | |

### get_help()

```python
def get_help(
    ctx: click.core.Context,
) -> str
```
Formats the help into a string and returns it.

Calls :meth:`format_help` internally.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### get_help_option()

```python
def get_help_option(
    ctx: click.Context,
) -> Union[click.Option, None]
```
Return the help option object.

Skipped if :attr:`add_help_option` is ``False``.

.. versionchanged:: 8.1.8
    The help option is now cached to avoid creating it multiple times.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |

### get_help_option_names()

```python
def get_help_option_names(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns the names for the help option.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### get_params()

```python
def get_params(
    ctx: click.core.Context,
) -> typing.List[ForwardRef('Parameter')]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### get_rich_table_row()

```python
def get_rich_table_row(
    ctx: 'RichContext',
    formatter: 'RichHelpFormatter',
    panel: Optional['RichCommandPanel'],
) -> 'RichPanelRow'
```
Create a row for the rich table corresponding with this parameter.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `'RichContext'` | |
| `formatter` | `'RichHelpFormatter'` | |
| `panel` | `Optional['RichCommandPanel']` | |

### get_short_help_str()

```python
def get_short_help_str(
    limit: int,
) -> str
```
Gets short help for the command or makes it by shortening the
long help string.


| Parameter | Type | Description |
|-|-|-|
| `limit` | `int` | |

### get_usage()

```python
def get_usage(
    ctx: click.core.Context,
) -> str
```
Formats the usage line into a string and returns it.

Calls :meth:`format_usage` internally.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### group()

```python
def group(
    args: *args,
    kwargs: **kwargs,
) -> Union[Callable[[Callable[..., Any]], 'RichGroup'], 'RichGroup']
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


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### invoke()

```python
def invoke(
    ctx: click.core.Context,
) -> typing.Any
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### list_commands()

```python
def list_commands(
    ctx: click.core.Context,
) -> typing.List[str]
```
Returns a list of subcommand names in the order they should
appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### main()

```python
def main(
    args: *args,
    prog_name: Optional[str],
    complete_var: Optional[str],
    standalone_mode: bool,
    windows_expand_args: bool,
    extra: Any,
) -> Any
```
This is the way to invoke a script with all the bells and
whistles as a command line application.  This will always terminate
the application after a call.  If this is not wanted, ``SystemExit``
needs to be caught.

This method is also available by directly calling the instance of
a :class:`Command`.



| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | the arguments that should be used for parsing.  If not provided, ``sys.argv[1:]`` is used. |
| `prog_name` | `Optional[str]` | the program name that should be used.  By default the program name is constructed by taking the file name from ``sys.argv[0]``. |
| `complete_var` | `Optional[str]` | the environment variable that controls the bash completion support.  The default is ``"_&lt;prog_name&gt;_COMPLETE"`` with prog_name in uppercase. |
| `standalone_mode` | `bool` | the default behavior is to invoke the script in standalone mode.  Click will then handle exceptions and convert them into error messages and the function will never return but shut down the interpreter.  If this is set to `False` they will be propagated to the caller and the return value of this function is the return value of :meth:`invoke`. |
| `windows_expand_args` | `bool` | Expand glob patterns, user dir, and env vars in command line args on Windows. |
| `extra` | `Any` | extra keyword arguments are forwarded to the context constructor.  See :class:`Context` for more information.  .. versionchanged:: 8.0.1 Added the ``windows_expand_args`` parameter to allow disabling command line arg expansion on Windows.  .. versionchanged:: 8.0 When taking arguments from ``sys.argv`` on Windows, glob patterns, user dir, and env vars are expanded.  .. versionchanged:: 3.0 Added the ``standalone_mode`` parameter. |

### make_context()

```python
def make_context(
    info_name: typing.Optional[str],
    args: *args,
    parent: typing.Optional[click.core.Context],
    extra: typing.Any,
) -> click.core.Context
```
This function when given an info name and arguments will kick
off the parsing and create a new :class:`Context`.  It does not
invoke the actual command callback though.

To quickly customize the context class used without overriding
this method, set the :attr:`context_class` attribute.



| Parameter | Type | Description |
|-|-|-|
| `info_name` | `typing.Optional[str]` | the info name for this invocation.  Generally this is the most descriptive name for the script or command.  For the toplevel script it's usually the name of the script, for commands below it's the name of the command. |
| `args` | `*args` | the arguments to parse as list of strings. |
| `parent` | `typing.Optional[click.core.Context]` | the parent context if available. |
| `extra` | `typing.Any` | extra keyword arguments forwarded to the context constructor.  .. versionchanged:: 8.0 Added the :attr:`context_class` attribute. |

### make_parser()

```python
def make_parser(
    ctx: click.core.Context,
) -> click.parser.OptionParser
```
Creates the underlying option parser for this command.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### parse_args()

```python
def parse_args(
    ctx: click.core.Context,
    args: *args,
) -> typing.List[str]
```
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `args` | `*args` | |

### resolve_command()

```python
def resolve_command(
    ctx: click.core.Context,
    args: *args,
) -> typing.Tuple[typing.Optional[str], typing.Optional[click.core.Command], typing.List[str]]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `args` | `*args` | |

### result_callback()

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



| Parameter | Type | Description |
|-|-|-|
| `replace` | `bool` | if set to `True` an already existing result callback will be removed.  .. versionchanged:: 8.0 Renamed from ``resultcallback``.  .. versionadded:: 3.0 |

### shell_complete()

```python
def shell_complete(
    ctx: click.core.Context,
    incomplete: str,
) -> typing.List[ForwardRef('CompletionItem')]
```
Return a list of completions for the incomplete value. Looks
at the names of options, subcommands, and chained
multi-commands.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | Invocation context for this command. |
| `incomplete` | `str` | Value being completed. May be empty.  .. versionadded:: 8.0 |

### to_info_dict()

```python
def to_info_dict(
    ctx: click.Context,
) -> Dict[str, Any]
```
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | A  .. versionadded:: 8.0 |

## Properties

| Property | Type | Description |
|-|-|-|
| `console` |  | {{< multiline >}}Rich Console.

This is a separate instance from the help formatter that allows full control of the
console configuration.

See `rich_config` decorator for how to apply the settings.
{{< /multiline >}} |
| `help_config` |  | {{< multiline >}}Rich Help Configuration.
{{< /multiline >}} |

