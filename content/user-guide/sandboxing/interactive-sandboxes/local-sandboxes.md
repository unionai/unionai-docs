---
title: Local sandboxes
weight: 3
variants: -flyte +union
---

# Local sandboxes

A local sandbox runs sandboxed child processes **inside the current container** via a native Rust extension. It needs no pod, no deployment, and no Union connection — `sb.local.session(...)` works anywhere the library is installed, including a laptop, CI runner, or notebook.

```python
import asyncio
import flyte
from union import sandbox as sb

async def main():
    async with sb.local.session(resources=flyte.Resources(cpu="500m", memory="512Mi")) as sbx:
        proc = await sbx.run("echo total=$(( 2 + 2 ))", stdout=True)
        out, _ = await proc.communicate_text()
        print(out)

asyncio.run(main())
```

The session implements the shared [`Session` API](./sessions) — `run()`, output helpers, byte transfer, and network policy are identical to the remote transport.

## Isolation backends

On open, the local transport auto-detects the strongest isolation available on the host and reports it on each process as `proc.backend`. Override the choice with the `SANDBOX_BACKEND` environment variable.

| Backend | How it works | Unprivileged on K8s | Default? |
|---|---|---|---|
| `bubblewrap` | `bwrap(1)` with `--unshare-all --die-with-parent --cap-drop ALL`, plus a Landlock ruleset as a kernel-side backstop | Yes | Yes (Linux) |
| `userns` | `unshare(2)` + `prctl(NO_NEW_PRIVS)` + `capset` + `setrlimit`, plus Landlock and a seccomp BPF deny-list | Yes | Fallback (Linux) |
| `sandbox-exec` | macOS wrapper around Apple's `sandbox-exec`; restricts writes to the work dir and can deny outbound sockets | n/a | macOS auto |
| `none` | `setpgid` + best-effort `setrlimit`; logs a warning | n/a | Dev only |

On Linux, the sandbox layers namespaces (user / mount / UTS / IPC, plus net unless you opted into host networking), dropped capabilities, a [Landlock](https://docs.kernel.org/userspace-api/landlock.html) filesystem ruleset, and (on `userns`) a seccomp deny-list for syscalls with no legitimate purpose in a sandbox.

> [!NOTE] macOS and other platforms degrade gracefully
> On macOS the backend is `sandbox-exec`; where no strong isolation exists, the backend is `none` and the library logs a warning rather than failing. Treat `none` as development-only — it provides best-effort resource limits but no real isolation.

## Filesystem allow-list

By default the sandbox grants read-only access to system paths (`/usr`, `/lib`, `/etc`, `/proc`, `/sys`, …) and read-write access to `/tmp`, `/dev/shm`, and the per-session work dir. You can **add** host paths to the allow-list — additions never replace the secure defaults:

```python
sbx = sb.local.session(
    read_only_paths=["/opt/models"],         # extend the read-only allow-list
    read_write_paths=["/data/scratch"],      # extend the read-write allow-list
    host_work_dir="/tmp/my-sandbox-work",    # pin the per-session work dir
)
```

Inspect the effective allow-list at any time:

```python
allowlist = sbx.fs_allowlist()
# {"read_only":  ["/usr", "/lib", ..., "/opt/models"],
#  "read_write": ["/tmp", "/dev/shm", ..., "/data/scratch", "/tmp/my-sandbox-work"]}
```

## Security boundary

> [!WARNING] A local sandbox shares your task's container
> The isolation backend constrains the sandboxed child process, but a local sandbox runs in the **same container as the code that launched it**. If the sandbox is breached, the escaping process can reach your **task's own code, mounted secrets, and service-account / cloud credentials** — unless the **task pod itself** runs under gVisor. A local sandbox is only as strong as the pod around it.
>
> For genuinely untrusted code (LLM-generated, third-party, or multi-tenant) where the caller holds sensitive credentials, prefer a [remote sandbox](./remote-sandboxes) (optionally with gVisor), which runs in a separate pod with its own service account and no access to your task's secrets. See [Local vs remote: when to use which](./_index#local-vs-remote-when-to-use-which) for the full trade-off. If you only need a single one-shot, typed-I/O invocation rather than an interactive session, [`flyte.sandbox.create()`](../code-sandboxing) is a simpler fit.
