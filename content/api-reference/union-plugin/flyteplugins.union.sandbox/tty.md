---
title: Tty
description: "A terminal for a command to run on (``sb.start(command, tty=Tty(30, 120))``)."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# Tty

**Package:** `flyteplugins.union.sandbox`

A terminal for a command to run on (``sb.start(command, tty=Tty(30, 120))``).

The command then sees a terminal on its stdin, stdout and stderr, as it
would in a terminal window: a shell prints a prompt and does job control,
programs use colour and redraw the screen, and Ctrl-C
(``p.stdin.write(b"\x03")``) interrupts what is running. What it prints is one stream, ``p.stdout``.


## Parameters

```python
class Tty(
    rows: int = 24,
    cols: int = 80,
    term: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `rows` | `int` | |
| `cols` | `int` | |
| `term` | `str` | |

