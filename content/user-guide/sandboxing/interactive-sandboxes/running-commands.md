---
title: Running commands
weight: 3
variants: -flyte +union
---

# Running commands

Once you have an open session, everything below works the same whether you got it from `sb.on_device.session(...)` or `await sb.session(...)`. The `Session` API is identical across transports.

## Lifecycle

A session follows `open → run → close`. The recommended shape is an `async with` block:

```python
from union import sandbox as sb

async with sb.on_device.session(backend="userns") as sbx:  # userns: runs on a vanilla pod, no extra capabilities
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
# session closed automatically here
```

You can also manage the lifetime yourself:

```python
sbx = await sb.on_device.session(backend="userns").open()
try:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
finally:
    await sbx.close()
```

> [!NOTE] Remote sessions open lazily
> For a remote `SandboxSession`, `async with sbx` (or `await sbx`) waits for the pod to become addressable, but the transport health-check is deferred to the first `run()` / `put_bytes` / `get_bytes` call. Your own setup work overlaps with pod startup. See [Deployment](./deployment) for the detached-lifetime pattern.

## `run()`

`run()` executes one command in the sandbox and returns a `SandboxProcess`, a subprocess-like handle you drain for output:

```python
proc = await sbx.run(
    "python -c 'import os; print(os.uname())'",
    stdout=True,                                    # PIPE | INHERIT | DEVNULL | False
    stderr=True,
    env={"FOO": "bar"},
    cwd="/tmp",                                     # under the sandbox work dir
    script_type="shell",                            # "shell" | "python"
    network_mode="allowlist",                       # "blocked" | "open" | "allowlist"
    network_allowlist=["pypi.org", "*.pythonhosted.org"],
    timeout_s=30,
)
```

| Argument | Type | Meaning |
|---|---|---|
| `cmd` | `str` | The command (shell) or script (`script_type="python"`) to run. |
| `stdout`, `stderr` | `True` / `False` / `PIPE` / `INHERIT` / `DEVNULL` | How to handle each stream. `True` captures (pipe); `False` discards. Constants are exported as `sb.PIPE`, `sb.INHERIT`, `sb.DEVNULL`. |
| `env` | `dict[str, str]` | Extra environment variables for the process. |
| `cwd` | `str` | Working directory, resolved under the sandbox work dir. |
| `script_type` | `"shell"` / `"python"` | Interpret `cmd` as a shell command or a Python script. |
| `network_mode` | `"blocked"` / `"open"` / `"allowlist"` | Network posture for this call. See [Networking](./networking). |
| `network_allowlist` | `list[str]` | CIDRs or DNS patterns, used only with `network_mode="allowlist"`. |
| `timeout_s` | `float` | Kill the process after this many seconds. |

> [!NOTE] `network_denylist` is set on the session, not per `run()`
> `run()` takes `network_mode` and `network_allowlist` per call, but not `network_denylist`. The deny-list is a session-level policy; pass it to `sb.on_device.session(...)` / `sb.session(...)`. See [Networking](./networking).

## One-shot commands: `exec()` and `run_code()`

`run()` returns a process handle that you manage directly. If you only need the command output, use one of the helper methods, which combine `run()` and `communicate()` into a single call.

`exec()` runs a command to completion and returns an `ExecResult` (exit code plus decoded streams):

```python
result = await sbx.exec("ls -la")
result.returncode   # int
result.stdout       # decoded str
result.stderr       # decoded str
result.ok           # True when returncode == 0

result = await sbx.exec("false", check=True)   # raises SandboxCommandError on non-zero
```

`run_code()` is the shortest path from Python source to its stdout. It runs `code` as a Python script (`script_type="python"`), raises `SandboxCommandError` on a non-zero exit, and returns the decoded stdout:

```python
out = await sbx.run_code("print(2 + 2)")   # "4\n"
```

Both take the same `env`, `cwd`, `network_mode`, `network_allowlist`, and `timeout_s` arguments as `run()`. `SandboxCommandError` carries the failing command and the full `ExecResult` (`err.result.stderr` for diagnostics); both are exported from `union.sandbox`.

Reach for `run()` when you need to stream output, branch on a non-zero exit without an exception, or inspect process metadata; reach for `exec()` / `run_code()` for the common capture-and-go case.

## Reading output

`SandboxProcess` gives you three ways to consume output:

```python
proc = await sbx.run("my-command", stdout=True, stderr=True)

# 1. Drain everything at once (bytes)
out, err = await proc.communicate()

# 2. Drain everything at once, decoded to str
out, err = await proc.communicate_text()

# 3. Stream lines as they arrive
async for line in proc.iter_stdout_lines():
    print(line)
async for line in proc.iter_stderr_lines():
    print(line)
```

After the process exits, inspect it:

```python
proc.returncode          # int exit code (None until it exits)
proc.runtime_ms          # wall-clock execution time
proc.backend             # "bubblewrap" | "userns" | "sandbox-exec" | "none"
proc.termination_reason  # "" on a clean exit, otherwise a reason string
```

## Script vs shell

`script_type="shell"` (the default) runs `cmd` through the sandbox shell. `script_type="python"` runs `cmd` as a Python script in the sandbox's interpreter, which is cleaner for multi-line code:

> [!NOTE] `python` vs `python3` on the host
> These examples use `python`. The remote sandbox image is based on `flyte.Image.from_debian_base()`, which ships both `python` and `pip` on PATH, so `python` always works there. The on-device transport runs against the host's Python: stock macOS has no `python` symlink, so use `python3` there (and for installs, prefer `uv pip install` — the session venv is uv-managed and ships no `pip`).

```python
proc = await sbx.run(
    """
    import json, pathlib
    data = json.loads(pathlib.Path("/tmp/my-job/in.json").read_text())
    print(sum(data["values"]))
    """,
    script_type="python",
    stdout=True,
)
```

## Installing packages: install is just a `run()`

A session keeps one shared virtualenv on its work dir, and every Python `run()` uses it. So there's no separate install API. Installing a package is an ordinary `run()`, and it persists for the life of the session:

```python
async with sb.on_device.session(
    backend="userns",
    network_mode="allowlist",
    network_allowlist=sb.PYPI_HOSTS,
) as sbx:
    await sbx.run("uv pip install requests") # lands in the session venv
    out = await sbx.run_code("import requests; print(requests.__version__)")
```

Install once, import anywhere: the package a `run()` installs is visible to every later `run()` in the same session. The session venv is built `--system-site-packages` so it can read the owner interpreter's packages, but installs go into the session venv only; the task's own Python is never mutated. The venv is `uv`-managed and ships no `pip`, so use `uv pip install` (not bare `pip`).

> [!NOTE] Only the work dir and the session venv persist
> Files written under the session work dir, and packages installed into the shared session venv, survive across `run()` calls. The writable scratch mounts (`/tmp`, `/dev/shm`) are a fresh tmpfs on every `run()`, so anything written to bare `/tmp` does not carry over; the rest of the filesystem is read-only. Note the default work dir lives at `/tmp/sandbox-work`. That's a separate persistent mount, distinct from the per-run `/tmp` scratch. See [Filesystem](./filesystem).

## Errors vs non-zero exits

A **non-zero exit of your own code is not an error.** It returns normally; branch on `proc.returncode`:

```python
proc = await sbx.run("exit 5", stdout=True)
await proc.communicate()
print(proc.returncode)   # 5, no exception raised
```

`communicate()` / `wait()` raise `SandboxExecutionError` only when the process never reached a real exit, for example a server-side spawn failure or a stream that died before termination:

```python
from union.sandbox import SandboxExecutionError

try:
    out, err = await proc.communicate()
except SandboxExecutionError as e:
    print(e.reason)        # e.g. "server crashed", "stream died"
    print(e.returncode)    # a fabricated -1 (no real exit occurred)
    print(e.backend)       # which backend was in use
    print(e.runtime_ms)    # how long before it failed
```

The split matters for agent loops: a sandboxed command failing its assertions is *signal*, and you handle it with `proc.returncode`. Only an exception means the sandbox itself misbehaved.

## Timeouts

`timeout_s` on `run()` kills a single process; sessions get their own timeout (remote sessions take it as `sb.session(timeout=...)`, defaulting to one hour). When `timeout_s` fires, the process is signalled and `proc.returncode` reflects the termination; the session stays open and you can run more commands.

## Related

- [Networking](./networking). What `network_mode` and `network_allowlist` actually constrain.
- [Filesystem](./filesystem). `put_bytes` / `get_bytes` to move data in and out without shelling out.
- [Security model](./security-model). What the backend reported in `proc.backend` actually defends against.
