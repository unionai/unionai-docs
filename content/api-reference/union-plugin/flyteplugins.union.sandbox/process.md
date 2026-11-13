---
title: Process
description: "A running command, from `Sandbox.start`."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# Process

**Package:** `flyteplugins.union.sandbox`

A running command, from `Sandbox.start`.

Stream its output as it comes with ``async for line in p.stdout`` (or
``p.stderr``): lines as bytes. ``await p.wait()`` waits for it to exit and
returns its `CommandResult`, with its output whether or not it was
streamed (at most `MAX_KEPT_BYTES` of each stream, its end).

One started with ``stdin=True`` or ``tty=`` is also written to
(`stdin`); one on a terminal is told its size (`resize`); any
started command can be sent a signal (`signal`).


## Parameters

```python
class Process(
    command: str = '',
    timeout: Optional[float] = None,
    hint: str = '',
)
```
| Parameter | Type | Description |
|-|-|-|
| `command` | `str` | |
| `timeout` | `Optional[float]` | |
| `hint` | `str` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `id` | `str` | Its name in the sandbox, for `Sandbox.process` to find it by from another client (a page reloaded, an app's other replica, this one after a restart). Empty for one run with `Sandbox.run`. |
| `stdin` | `Input` | The command's stdin, to write to. It needs ``stdin=True`` or ``tty=`` at `Sandbox.start`.  ``async with p.stdin as stdin:`` ends the command's input when the block is left, so the command reads end of file:  `p = await sb.start("python3 -", stdin=True) async with p.stdin as stdin: await stdin.write("print(6 * 7)\n") print((await p.wait()).stdout)`  ``await p.stdin.write(b"ls\n")`` writes without ending it: what is typed at a command on a terminal. |

## Methods

| Method | Description |
|-|-|
| [`resize()`](#resize) | Tells the command's terminal its size, as a terminal window does when it is resized. |
| [`signal()`](#signal) | Sends ``signal`` (``signal.SIGINT``, ``signal.SIGTERM``, ...) to the command and everything it started. |
| [`wait()`](#wait) | Waits for it to exit; its `CommandResult`. |


### resize()

```python
def resize(
    rows: int,
    cols: int,
)
```
Tells the command's terminal its size, as a terminal window does
when it is resized. It needs ``tty=`` at `Sandbox.start`.


| Parameter | Type | Description |
|-|-|-|
| `rows` | `int` | |
| `cols` | `int` | |

### signal()

```python
def signal(
    signal: int,
)
```
Sends ``signal`` (``signal.SIGINT``, ``signal.SIGTERM``, ...) to the
command and everything it started.

One that stops a command (SIGTERM, SIGKILL, SIGHUP, SIGSTOP) or
continues it (SIGCONT) is sent again while the sandbox does not
answer, as other calls are. Any other is sent once: if the sandbox
cannot be reached this raises, and the signal may or may not have
arrived.


| Parameter | Type | Description |
|-|-|-|
| `signal` | `int` | |

### wait()

```python
def wait(
    check: bool = True,
) -> CommandResult
```
Waits for it to exit; its `CommandResult`.

With ``check`` (the default) a nonzero exit raises
`SandboxCommandFailed`, and running past its ``timeout`` raises
`SandboxCommandTimedOut`; both carry the result. A session that
failed or ended under it raises `SandboxSessionError` (or
`SandboxSessionEnded`, saying why) either way.


| Parameter | Type | Description |
|-|-|-|
| `check` | `bool` | |

