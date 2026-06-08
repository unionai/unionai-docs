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

async with sb.on_device.session(backend="userns") as sbx:
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
    "python3 -c 'import os; print(os.uname())'",
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

```python
proc = await sbx.run(
    """
    import json, pathlib
    data = json.loads(pathlib.Path("in.json").read_text())  # under the work dir
    print(sum(data["values"]))
    """,
    script_type="python",
    stdout=True,
)
```

## Installing packages

A session keeps **one venv on its work dir**, and every `run()` uses it. Installing is therefore just another `run()`: install in one call, import in the next, for the life of the session — like pip on a long-lived machine.

```python
async with await sb.session(
    network_mode="allowlist", network_allowlist=sb.PYPI_HOSTS,
) as sbx:
    await sbx.run("uv pip install pandas")
    await sbx.run("import pandas; print(pandas.__version__)", script_type="python")
```

The session venv is uv-managed and ships no `pip`, so install with **`uv pip install`** (not `pip`). It's a distinct environment from the owner interpreter — installs land in the session venv, never in the task's own Python. Installing needs egress to PyPI, so open the session with `network_mode="allowlist"` and `network_allowlist=sb.PYPI_HOSTS` (the `pypi.org` / `pythonhosted.org` hosts). See [Networking](./networking).

> [!NOTE] Work dir persists, `/tmp` does not
> The work dir is the session's persistent disk — files written there in one `run()` are visible to the next, and `cwd` defaults to it. The rest of the filesystem, **including `/tmp`**, is reset for every command. Keep state you need across calls in the work dir. See [Filesystem](./filesystem).

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
