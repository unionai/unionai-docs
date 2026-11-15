---
title: Run commands
description: Run commands in a VM sandbox, stream their output, send them input, give them a terminal, and reach servers they start.
weight: 3
variants: -flyte +union
---

# Run commands

An agent loop runs a command, reads the output, and decides what to do next. A test suite streams results for minutes. A REPL needs input. A dev server listens on a port. VM sandboxes cover each of these with two calls: `sb.run()` runs a command to the end, and `sb.start()` starts one and hands you its streams.

```python
async with code_runner.session("agent-turn") as sb:
    result = await sb.run("pytest -x tests/", check=False)
    if not result.ok:
        feedback = result.stdout[-20000:] + result.stderr[-20000:]
```

## Run a command to the end

`sb.run(command)` waits for the command to exit and returns a `CommandResult`.

- A string runs as a shell command line: `sb.run("ls -la | wc -l")`.
- A list runs without a shell: `sb.run(["python", "main.py", "--fast"])`. Use a list when arguments come from untrusted input, so nothing is parsed as shell syntax.

| Argument | Default | What it does |
| --- | --- | --- |
| `env` | None | Extra environment variables for this command. |
| `cwd` | `"."` | Working directory. Relative paths are under `/work`. |
| `timeout` | None | Stop the command after this many seconds, or a `timedelta`. |
| `check` | `True` | Raise `SandboxCommandFailed` if it exits nonzero. |
| `input` | None | Bytes or text to send to its stdin, then close it. |

A `CommandResult` has:

| Field | What it holds |
| --- | --- |
| `exit_code` | The exit code. `ok` is `True` when it is 0. |
| `stdout`, `stderr` | Output decoded as UTF-8. Each keeps at most the last 64 MiB. |
| `duration` | Wall time in seconds, measured in the sandbox. |
| `timed_out` | Whether it was stopped for running past `timeout`. |
| `truncated` | Whether output was dropped to stay within 64 MiB. |
| `reason` | Why it ended, when the sandbox says: a timeout or a signal. |

### Handle failures

By default a nonzero exit raises `SandboxCommandFailed`, and a timeout raises `SandboxCommandTimedOut`, a subclass of it. The exception's `.result` is the `CommandResult`. Both are Flyte user errors, so a task that lets one escape fails as its own error and isn't retried as a system failure.

In an agent loop, a failing command is information for the model, not an error. Pass `check=False` and read the result:

```python
result = await sb.run(["/bin/bash", "-lc", command], timeout=120, check=False)
exit_code = 124 if result.timed_out else result.exit_code
observation = f"exit {exit_code}\n{result.stdout}{result.stderr}"
```

If a command fails because it needed the network, the error message says which network the sandbox has and how to change it.

### Cancel a command

A command run with `sb.run()` lives as long as the call. If you cancel the call, for example with `asyncio.wait_for`, the command is killed in the sandbox.

## Stream output

`sb.start(command)` starts a command and returns a `Process` right away. Read its output as it is written, then wait for its result:

```python
p = await sb.start("pytest -v tests/")
async for line in p.stdout:  # lines, as bytes
    print(line.decode(), end="")
result = await p.wait()  # a CommandResult; raises on a nonzero exit unless check=False
```

`p.stderr` streams the same way. `p.wait()` returns the full output whether or not you streamed it.

Unlike `sb.run()`, a started command keeps running in the sandbox if your connection breaks, or across a snapshot or suspend. To pick it up again from another process, or after reconnecting, pass its `p.id` to `sb.process(id)`. The new `Process` replays output from the last 4 MiB of each stream that the sandbox keeps. The sandbox keeps a command for 10 minutes after it ends.

## Send input

Run a command to the end on some input:

```python
result = await sb.run(["python", "-c", "import sys; print(sys.stdin.read().upper())"], input="hello")
```

Or start it with a stdin you write to over time:

```python
p = await sb.start(["python", "-i", "-q"], stdin=True)
async with p.stdin as stdin:  # leaving the block closes its input
    await stdin.write("print(6 * 7)\n")
result = await p.wait()
```

## Give a command a terminal

Pass a `sandbox.Tty` to run a command on a terminal, as in a terminal window. A shell prints a prompt and does job control, and programs use color and redraw the screen. What it prints comes on one stream, `p.stdout`, read as chunks of bytes:

```python
p = await sb.start("bash", tty=sandbox.Tty(rows=30, cols=120))
await p.stdin.write("ls --color\n")
await p.stdin.write(b"\x03")  # Ctrl-C
await p.resize(40, 160)  # follow the window size
async for chunk in p.stdout.chunks():
    ...
```

This is what you need to put a terminal in a web page. Wire the page's keystrokes to `p.stdin.write` and send `p.stdout.chunks()` back over a WebSocket.

## Send a signal

```python
import signal

await p.signal(signal.SIGTERM)
```

## Reach a server in the sandbox

Nothing outside a sandbox can connect to it except its own client. To reach a server that runs in the sandbox, use `sb.port_url(port)`:

```python
await sb.start("python -m http.server 8000")
url = sb.port_url(8000)  # http://.../port/8000
ws_url = sb.port_url(9222, scheme="ws")  # WebSockets pass through too
```

From a task or an app, the URL is the session's own address in your cluster. From outside the cluster, it is a Union.ai data proxy URL, and requests to it need your Union.ai credentials. See [Use sandboxes outside a task](./outside-tasks).

For example, Playwright can drive a Chromium started in the sandbox with `--remote-debugging-port=9222` through `connect_over_cdp(sb.port_url(9222, scheme="ws") + path)`.

## Run commands in parallel

One session runs many commands at once. Different sessions are independent VMs. Use `asyncio.gather` for either:

```python
results = await asyncio.gather(
    sb.run("ruff check ."),
    sb.run("mypy src"),
    sb.run("pytest -q"),
    return_exceptions=True,
)
```
