---
title: Sandbox sessions
weight: 2
variants: -flyte +union
---

# Sandbox sessions

Both the [local](./local-sandboxes) and [remote](./remote-sandboxes) transports implement the same `Session` API. Everything on this page works identically whether you opened the session with `sb.local.session(...)` or `sb.session(...)` — only how you create the session differs.

## Lifecycle

A session follows the contract **open → run → close**. The recommended way to manage it is an `async with` block, which opens the session on entry and closes it on exit:

```python
from union import sandbox as sb

async with sb.local.session() as sbx:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
# session closed automatically here
```

You can also manage the lifetime yourself — open with `.open()` and close with `.close()`:

```python
sbx = await sb.local.session().open()
try:
    proc = await sbx.run("uname -a", stdout=True)
    out, _ = await proc.communicate_text()
finally:
    await sbx.close()
```

> [!NOTE] Remote sessions open lazily
> For a remote `SandboxSession`, `async with` (or `await sbx`) waits for the pod to become addressable, but the transport health-check is deferred to the **first** `run()` / `put_bytes` / `get_bytes` call. This lets your own setup work overlap with pod startup. See [Remote sandboxes](./remote-sandboxes) for the detached-lifetime pattern.

## Running commands

`run()` executes one command in the sandbox and returns a `SandboxProcess` — a subprocess-like handle you drain for output:

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
| `stdout` / `stderr` | `True` / `False` / `PIPE` / `INHERIT` / `DEVNULL` | How to handle each stream. `True` captures it (pipe); `False` discards. Constants are exported as `sb.PIPE`, `sb.INHERIT`, `sb.DEVNULL`. |
| `env` | `dict[str, str]` | Extra environment variables for the process. |
| `cwd` | `str` | Working directory, resolved under the sandbox work dir. |
| `script_type` | `"shell"` / `"python"` | Interpret `cmd` as a shell command or a Python script. |
| `network_mode` | `"blocked"` / `"open"` / `"allowlist"` | Network posture for this call (see below). |
| `network_allowlist` | `list[str]` | CIDRs / DNS patterns, used only with `network_mode="allowlist"`. |
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

## Transferring bytes

Push and pull raw bytes to and from the sandbox filesystem without shelling out:

```python
await sbx.put_bytes("/tmp/sandbox-work/input.json", b'{"x": 1}')

data = await sbx.get_bytes("/tmp/sandbox-work/result.json", max_bytes=10 * 1024 * 1024)
```

This is the simplest way to move a file into a sandbox before running a command, or to retrieve a result afterward.

## Errors vs. non-zero exits

A **non-zero exit of your own code is not an error.** It returns normally; branch on `proc.returncode`:

```python
proc = await sbx.run("exit 5", stdout=True)
await proc.communicate()
print(proc.returncode)   # 5 — no exception raised
```

`communicate()` / `wait()` raise `SandboxExecutionError` only when the process never reached a real exit — a server-side spawn failure, or a stream that died before termination:

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

## Network policy

Every call gets one of three network postures. Set the default on the session and override it per `run()`:

```python
# 1. Blocked (default): fresh network namespace, only loopback.
await sbx.run("curl -fsS https://example.com/")                    # fails — no network

# 2. Open: full host network.
await sbx.run("curl -fsS https://example.com/", network_mode="open")

# 3. Allow-list: a per-call HTTP CONNECT proxy 403s anything off the list.
await sbx.run(
    "pip install requests",
    network_mode="allowlist",
    network_allowlist=["pypi.org", "*.pythonhosted.org", "10.0.0.0/8"],
)
```

The two knobs read as:

- `network_mode` — the posture selector: `"blocked"`, `"open"`, or `"allowlist"`.
- `network_allowlist` — the allow-list entries (CIDRs or DNS patterns), used only with `network_mode="allowlist"`.

> [!WARNING] The allow-list is proxy-based, not a kernel wall
> `network_allowlist` constrains clients that honour the `HTTPS_PROXY` environment variable (pip, curl, requests, boto3, huggingface_hub). It is **not** a kernel-level firewall and does not constrain adversarial code that ignores the proxy. For a hard network boundary, use `network_mode="blocked"`.
