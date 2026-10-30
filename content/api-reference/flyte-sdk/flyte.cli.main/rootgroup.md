---
title: RootGroup
description: "The `flyte` group."
icon: braces
version: 2.12.2
variants: +flyte +union
layout: py_api
---

# RootGroup

**Package:** `flyte.cli.main`

The `flyte` group. Its options (`--image-builder`, `--endpoint`, `--org`, and so on) belong to
`flyte` itself and go before the subcommand. When one is placed after the subcommand instead,
click reports it as unknown and may suggest an unrelated subcommand option, so the error is
replaced with one that says where the option goes.


## Parameters

```python
class RootGroup(
    *args,
    lazy_commands: Mapping[str, str],
    **kwargs,
)
```
Initialize RichGroup class.


| Parameter | Type | Description |
|-|-|-|
| `*args` |  | |
| `lazy_commands` | `Mapping[str, str]` | |
| `**kwargs` |  | |

## Methods

| Method | Description |
|-|-|
| [`get_command()`](#get_command) | Given a context and a command name, this returns a `Command` object if it exists or returns ``None``. |
| [`invoke()`](#invoke) | Given a context, this invokes the attached callback (if it exists) in the right way. |
| [`list_commands()`](#list_commands) | Returns a list of subcommand names in the order they should appear. |


### get_command()

```python
def get_command(
    ctx: click.Context,
    cmd_name: str,
) -> click.Command | None
```
Given a context and a command name, this returns a `Command`
object if it exists or returns ``None``.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |
| `cmd_name` | `str` | |

### invoke()

```python
def invoke(
    ctx: click.core.Context,
)
```
Given a context, this invokes the attached callback (if it exists)
in the right way.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |

### list_commands()

```python
def list_commands(
    ctx: click.Context,
) -> list[str]
```
Returns a list of subcommand names in the order they should appear.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.Context` | |

