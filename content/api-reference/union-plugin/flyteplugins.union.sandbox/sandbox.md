---
title: Sandbox
description: "A running sandbox session, from ``async with env.session(\"build\") as sb``."
icon: braces
version: 0.21.1
variants: -flyte +union
layout: py_api
---

# Sandbox

**Package:** `flyteplugins.union.sandbox`

A running sandbox session, from ``async with env.session("build") as sb``.

It is ready to use when the block starts, and closed when it exits: its
commands are stopped (SIGTERM, then SIGKILL after a grace period), its disk
synced, and the session succeeds. `cancel` aborts it instead.


## Parameters

```python
class Sandbox(
    ready: Ready,
    client: SandboxClient,
    startup: SessionStartup,
    hint: str,
    env: Any = None,
    scratch: bool = False,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ready` | `Ready` | |
| `client` | `SandboxClient` | |
| `startup` | `SessionStartup` | |
| `hint` | `str` | |
| `env` | `Any` | |
| `scratch` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`cancel()`](#cancel) | Aborts the session now: its commands are killed, and the session ends as aborted. |
| [`close()`](#close) | Ends the session gracefully, and it succeeds: its commands get SIGTERM, and SIGKILL if still running after ``grace`` (seconds or a ``timedelta``; the sandbox allows at most 60); its disk is synced; then its sandbox is removed. |
| [`commit()`](#commit) | Commits the session's disk as it is now, and returns it as a `SandboxVolume`: a task input or output, and what ``env.session(name, volume=...)`` starts a session on a copy of, on any node. |
| [`detach()`](#detach) | Disconnects from the session and leaves it running: every later call on this object is refused, and the session goes on until it is closed or reaches its ``max_duration``. |
| [`fork()`](#fork) | A new session on a copy of this one's disk, now: `commit`, then ``env.session(volume=it)`` on this session's environment. |
| [`fork_close()`](#fork_close) | Closes the session, as `close`, and returns its disk as a `SandboxVolume`. |
| [`port_url()`](#port_url) | The URL of what listens on ``port`` in the sandbox (on its loopback): requests under it reach ``127.0.0.1:<port>`` there, and a WebSocket passes through (``scheme="ws"``). |
| [`process()`](#process) | The `Process` of a command started earlier with `start`, by its `Process.id`: for a client that did not start it, or has lost its ``Process`` (a page reloaded, an app's other replica, a session attached to again or resumed). |
| [`run()`](#run) | Runs ``command`` to the end and returns its `CommandResult`. |
| [`snapshot()`](#snapshot) | Takes the session's disk, memory and processes at one instant and returns them as a `SandboxSnapshot`, once it is committed: ``env.session(name, snapshot=it)`` starts a new session from it, its processes running on from that instant. |
| [`start()`](#start) | Starts ``command`` and returns at once, to stream its output. |
| [`suspend()`](#suspend) | Pauses the session where it is and returns its `SandboxSnapshot`: its disk, memory and processes, taken at one instant. |


### cancel()

```python
def cancel(
    reason: str = 'cancelled',
)
```
Aborts the session now: its commands are killed, and the session
ends as aborted. Leaving the ``async with`` block closes it gracefully
instead (`close`); calling it again does nothing. A suspended
session, not yet resumed, is discarded.


| Parameter | Type | Description |
|-|-|-|
| `reason` | `str` | |

### close()

```python
def close(
    grace: Duration = 10,
    wait: bool = False,
)
```
Ends the session gracefully, and it succeeds: its commands get
SIGTERM, and SIGKILL if still running after ``grace`` (seconds or a
``timedelta``; the sandbox allows at most 60); its disk is synced; then
its sandbox is removed. Leaving the ``async with`` block does this;
calling it again does nothing more.

It returns once the sandbox has closed (at once when no command runs),
and watches for the session's end in the background; ``wait=True``
returns once the session has ended. A session that can't be closed
(its sandbox doesn't answer, or its end doesn't come) is cancelled
instead.


| Parameter | Type | Description |
|-|-|-|
| `grace` | `Duration` | |
| `wait` | `bool` | |

### commit()

```python
def commit()
```
Commits the session's disk as it is now, and returns it as a
`SandboxVolume`: a task input or output, and what
``env.session(name, volume=...)`` starts a session on a copy of, on
any node. The session runs on; its writes wait while the disk is
frozen for the commit. `snapshot` takes its memory and processes
too. A ScratchVolume session can't be committed
(``SandboxUsageError``).


### detach()

```python
def detach()
```
Disconnects from the session and leaves it running: every later
call on this object is refused, and the session goes on until it is
closed or reaches its ``max_duration``. What leaving an
``env.attach(...)`` block does. Does nothing once closed.


### fork()

```python
def fork(
    name: str,
    memory: bool = False,
) -> AsyncIterator[Sandbox]
```
A new session on a copy of this one's disk, now: `commit`,
then ``env.session(volume=it)`` on this session's environment. It
copies the disk, not memory or processes: the child boots fresh, with
every file the parent had. Both run on, apart.

``memory=True`` copies its memory and processes too:
`snapshot`, then ``env.session(name, snapshot=it)``. The child
runs on from where the parent was, its processes and all; it shares
whatever they held (secrets, random state already drawn, locks
taken), and its network connections are gone.

``name`` names the child's session, as ``env.session(name)`` does.
``async with sb.fork("try-fix-1") as child: ...``; the child is closed
when the block exits.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `memory` | `bool` | |

### fork_close()

```python
def fork_close(
    grace: Duration = 10,
) -> SandboxVolume
```
Closes the session, as `close`, and returns its disk as a
`SandboxVolume`. Its commands have stopped, so the disk is
committed as they left it. Leaving the ``async with`` block then does
nothing more. To keep its memory and processes instead, `suspend` it.


| Parameter | Type | Description |
|-|-|-|
| `grace` | `Duration` | |

### port_url()

```python
def port_url(
    port: int,
    scheme: str = 'http',
) -> str
```
The URL of what listens on ``port`` in the sandbox (on its
loopback): requests under it reach ``127.0.0.1:<port>`` there, and a
WebSocket passes through (``scheme="ws"``).

So a server started in the sandbox is used as it is, from where the
session is used:

```python
await sb.start("chromium --headless=new --remote-debugging-port=9222 ...")
version = httpx.get(sb.port_url(9222) + "/json/version").json()
path = urlparse(version["webSocketDebuggerUrl"]).path
browser = await playwright.chromium.connect_over_cdp(sb.port_url(9222, scheme="ws") + path)
```

The URL holds the session's token: whoever has it can call into the
sandbox. Hand it to a client of yours, not to a page. It is the
session's in-cluster address, as ``sb.endpoint`` is, and changes when
a suspended session is restored. A node from before ports were
forwarded answers 404 under it.


| Parameter | Type | Description |
|-|-|-|
| `port` | `int` | |
| `scheme` | `str` | |

### process()

```python
def process(
    id: str,
) -> Process
```
The `Process` of a command started earlier with
`start`, by its `Process.id`: for a client that did not
start it, or has lost its ``Process`` (a page reloaded, an app's
other replica, a session attached to again or resumed).

Its output comes from the earliest the sandbox still keeps (the last
4 MiB of each stream), and what is written to it goes on from where
its stdin is. Raises `ProcessError` if the sandbox has no such
command: it ended more than ten minutes ago, or the sandbox was
started again without it.

One command may be read by several clients at once, each getting all
of its output. Only one should write to it: writes from two are
refused or interleaved, never applied twice.


| Parameter | Type | Description |
|-|-|-|
| `id` | `str` | |

### run()

```python
def run(
    command: str | Sequence[str],
    env: Optional[Mapping[str, str]] = None,
    cwd: str = '.',
    timeout: Optional[Duration] = None,
    check: bool = True,
    input: Optional[Union[bytes, str]] = None,
) -> CommandResult
```
Runs ``command`` to the end and returns its `CommandResult`.

``command`` is a shell command line (``"pip install -r req.txt && pytest"``)
or a list of arguments, which run without a shell interpreting them
(``["python", "main.py", user_input]``). It starts in ``cwd`` (relative
paths are under ``/work``), with ``env`` added to its environment, and is
stopped after ``timeout`` (seconds or a ``timedelta``).

A nonzero exit raises `SandboxCommandFailed`, with its output;
``check=False`` returns the result instead. Running past ``timeout``
raises `SandboxCommandTimedOut`.

The command lives as long as the call: cancelling it (a timeout around
it, a task group failing) kills it, and so does a snapshot or suspend
taken while it runs, which reset the sandbox's connections. Use
`start` for a command that must outlive those.

``input`` is what the command reads on its stdin, to its end
(``sb.run("python3", input="print(6 * 7)")``); without it, its stdin
is empty.


| Parameter | Type | Description |
|-|-|-|
| `command` | `str \| Sequence[str]` | |
| `env` | `Optional[Mapping[str, str]]` | |
| `cwd` | `str` | |
| `timeout` | `Optional[Duration]` | |
| `check` | `bool` | |
| `input` | `Optional[Union[bytes, str]]` | |

### snapshot()

```python
def snapshot(
    wait: bool = True,
) -> Union[SandboxSnapshot, SnapshotFuture]
```
Takes the session's disk, memory and processes at one instant and
returns them as a `SandboxSnapshot`, once it is committed:
``env.session(name, snapshot=it)`` starts a new session from it, its
processes running on from that instant. The session runs on.

Its VM is paused while its memory is written on the node (about half
a second for a 1 GiB VM, less for later snapshots, which write only
what changed), then runs on; committing takes about as long again.
``wait=False`` returns as soon as the VM runs on, with a
`SnapshotFuture`: what the snapshot holds is fixed, and
``await fut.wait()`` returns it once committed. Until then its disk
stays frozen, so the guest's writes to it wait (about 1.8 s in all
for a 1 GiB VM); its CPU, memory and reads don't.

Writing a snapshot resets the sandbox's connections: a `run`
in flight is cut (its command stopped), and the guest's network
connections close; commands from `start` run on.

A ScratchVolume session can't be snapshotted (``SandboxUsageError``).


| Parameter | Type | Description |
|-|-|-|
| `wait` | `bool` | |

### start()

```python
def start(
    command: str | Sequence[str],
    env: Optional[Mapping[str, str]] = None,
    cwd: str = '.',
    timeout: Optional[Duration] = None,
    stdin: bool = False,
    tty: Optional[Tty] = None,
) -> Process
```
Starts ``command`` and returns at once, to stream its output.

Takes the same arguments as `run`. ``async for line in p.stdout``
streams it; ``await p.wait()`` returns its `CommandResult` (and
raises if it failed) once it exits.

The sandbox keeps it running if the stream breaks, and it is attached
to again: a snapshot or suspend (which reset the sandbox's
connections) doesn't stop it. Its ``Process`` ends with the session's
connection, though: after a suspend and a resume, the command runs on,
unobserved.

``stdin=True`` gives it a stdin to write to. Leaving the block ends
its input, so it reads end of file:

```python
async with p.stdin as stdin:
    await stdin.write("print(6 * 7)\n")
```

Without ``stdin``, its stdin is empty.

``tty=sandbox.Tty(rows, cols)`` runs it on a terminal, as it would run
in a terminal window: a shell prompts and does job control, programs
use colour and redraw the screen. What it prints is one stream, to be
read as it comes (``async for chunk in p.stdout.chunks()``), and what
is written to it is what would be typed: ``p.stdin.write(b"ls\n")``,
``p.stdin.write(b"\x03")`` for Ctrl-C. ``await p.resize(rows, cols)``
when the window showing it changes size.

Either way ``await p.signal(signal.SIGTERM)`` signals it.


| Parameter | Type | Description |
|-|-|-|
| `command` | `str \| Sequence[str]` | |
| `env` | `Optional[Mapping[str, str]]` | |
| `cwd` | `str` | |
| `timeout` | `Optional[Duration]` | |
| `stdin` | `bool` | |
| `tty` | `Optional[Tty]` | |

### suspend()

```python
def suspend(
    keep: Duration = datetime.timedelta(seconds=300),
    wait: bool = True,
) -> Union[SandboxSnapshot, SnapshotFuture]
```
Pauses the session where it is and returns its `SandboxSnapshot`:
its disk, memory and processes, taken at one instant.

Its VM stays paused on its node for ``keep`` (seconds or a
``timedelta``, at most an hour), and no longer than the session's
``max_duration``, which keeps running while it is paused. The
``env.session(snapshot=s)`` of the same ``SandboxEnvironment`` object,
in this task, resumes it there, in milliseconds, its processes as they
were. Not resumed by then, the session ends (it succeeds); its
snapshot outlives it, and ``env.session(snapshot=s)`` restores it on a
new session, here or in another task. Leaving the ``async with`` block
does nothing more; `cancel` discards it.

It returns once the snapshot is committed, which takes most of a
suspend's time (about 2 s for a 1 GiB VM, its VM paused within the
first few hundred ms). ``wait=False`` returns as soon as the VM is
paused, with a `SnapshotFuture`: the session is suspended, and
``env.session(snapshot=fut)`` resumes it as above (waiting first for
the commit, if it is still under way); ``await fut.wait()`` returns
the snapshot once committed.

To a resumed session's processes the pause is a stall: their clock
jumps by its length, so timeouts and leases may have run out. The
``Process`` handles of `start` end here (their commands run on,
unobserved), and a `run` in flight is cut.

A ScratchVolume session can't be suspended (``SandboxUsageError``).


| Parameter | Type | Description |
|-|-|-|
| `keep` | `Duration` | |
| `wait` | `bool` | |

