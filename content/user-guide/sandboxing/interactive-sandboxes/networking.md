---
title: Networking
weight: 4
variants: -flyte +union
---

# Networking

A sandbox session has two layers of network posture: a **session-level default** that bounds what the session can ever reach, and a **per-call override** on each `run()` that can tighten within that bound. Set the session-level posture to the broadest thing any `run()` in the session needs; per-call overrides narrow from there.

```python
async with await sb.session(
    network_mode="allowlist",
    network_allowlist=sb.PYPI_HOSTS,
) as sbx:
    await sbx.run("python3 my_tool.py", network_mode="blocked")      # tighten to blocked
    await sbx.run("uv pip install requests")                         # uses session default
    await sbx.run("python3 use_requests.py", network_mode="blocked") # tighten again
```

`sb.PYPI_HOSTS` is an exported convenience list (`pypi.org`, `files.pythonhosted.org`, `*.pythonhosted.org`) for the common case of allowing `uv pip install` and nothing else.

> [!IMPORTANT] Per-call can narrow, not broaden
> On a remote sandbox, the pod's network namespace is committed at session open and can't be widened later. On-device sessions create a fresh network namespace per `run()` and don't have this constraint, but writing for both transports is simplest if you treat session-level as the ceiling everywhere.

## The three postures

| `network_mode`        | What the sandboxed process sees                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `"blocked"` (default) | A fresh network namespace with only loopback. Outbound connections fail at the kernel level.                                                    |
| `"open"`              | The host network. Use only when the sandboxed code is trusted.                                                                                  |
| `"allowlist"`         | A per-call HTTP CONNECT proxy. `HTTP_PROXY` and `HTTPS_PROXY` are set in the process env; the proxy `403`s anything not on `network_allowlist`. |

`network_allowlist` accepts CIDRs (`10.0.0.0/8`) and DNS patterns including wildcards (`*.pythonhosted.org`). It's only consulted when `network_mode="allowlist"`.

## What the allow-list actually constrains

> [!WARNING] The allow-list is proxy-based, not a kernel wall
> `network_allowlist` constrains clients that honour the `HTTPS_PROXY` environment variable: pip, curl, requests, boto3, huggingface_hub, and most HTTP libraries. It is **not** a kernel-level firewall. Adversarial code that bypasses the proxy (raw sockets, DNS-over-UDP, anything that ignores env vars) will not be filtered.
>
> For a hard network boundary against untrusted code, use `network_mode="blocked"`. The allow-list is for convenience under trust, not adversarial isolation.

So:

- You're installing dependencies or hitting a known API from your own code: `allowlist` is the right tool. Lower friction than tearing the session down, audit-friendly.
- You're running untrusted code and want to permit only certain egress: don't rely on `allowlist`. Use `blocked` and stage the data the sandboxed code needs via [`put_bytes`](./filesystem) before the call.

## Setting a default for the session

Pass `network_mode=` and `network_allowlist=` to `session(...)` to set the default for the whole session; individual `run()` calls still override it:

```python
async with sb.on_device.session(
    backend="userns",
    network_mode="allowlist",
    network_allowlist=sb.PYPI_HOSTS,
) as sbx:
    await sbx.run("uv pip install numpy")             # uses session default
    await sbx.run("python3 untrusted.py", network_mode="blocked")  # tightened
```

## Session default vs per-call override

Two places set network posture, and they accept the same two arguments:

| Where you set it                            | Arguments                             | What it controls                                                                                                                                  |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sb.on_device.session(...)` / `sb.session(...)` | `network_mode=`, `network_allowlist=` | Default for every `run()` in the session. On a remote sandbox this _also_ sets the pod-level network posture, so the per-call proxy can dial out. |
| `run(...)`                                  | `network_mode=`, `network_allowlist=` | The posture for this one call. Overrides the session default.                                                                                     |

> [!IMPORTANT] Session-level posture sets the pod's network on remote
> On a remote sandbox, the session-level `network_mode` _determines whether the sandbox-server pod has any network at all._ `network_mode="blocked"` at the session level means the pod has no egress, period. A per-call `run(network_mode="allowlist", ...)` will then fail with `Temporary failure in name resolution`, because the per-call proxy has nowhere to dial out from.
>
> Rule of thumb: set the session-level `network_mode` to the **broadest** posture any `run()` in the session needs, then tighten per call. If a session has even one step that needs `pypi.org`, set `network_mode="allowlist"` (or `"open"`) on `sb.session()`; the per-call defaults on other `run()`s will still be `"blocked"`.

## How the proxy is implemented

The on-device transport spins a short-lived HTTP CONNECT proxy for the duration of the `run()` call. It terminates the CONNECT, checks the target against the allow-list, and either dials out or returns `403`. There is no shared state between calls; each `run()` gets a fresh proxy with the allow-list you passed in.

## Related

- [Security model](./security-model). What network isolation buys you and what it doesn't.
- [Running commands](./running-commands). Other `run()` arguments.
- [Filesystem](./filesystem). Staging data into a blocked sandbox with `put_bytes`.
