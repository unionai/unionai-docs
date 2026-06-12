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
    await sbx.run("python my_tool.py", network_mode="blocked")       # tighten to blocked
    await sbx.run("uv pip install requests")                         # uses session default
    await sbx.run("python use_requests.py", network_mode="blocked")  # tighten again
```

`sb.PYPI_HOSTS` is an exported convenience list (`pypi.org`, `files.pythonhosted.org`, `*.pythonhosted.org`) for the common case of allowing `uv pip install` and nothing else.

> [!IMPORTANT] Per-call can narrow, not broaden
> On a remote sandbox, the pod's network namespace is committed at session open and can't be widened later. On-device sessions create a fresh network namespace per `run()` and don't have this constraint, but writing for both transports is simplest if you treat session-level as the ceiling everywhere.

## The three postures

| `network_mode`        | What the sandboxed process sees                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `"blocked"` (default) | A fresh network namespace with only loopback. Outbound connections fail at the kernel level.                                                    |
| `"open"`              | The host network. Use only when the sandboxed code is trusted.                                                                                  |
| `"allowlist"`         | A per-call pair of proxies — an HTTP CONNECT proxy and a SOCKS5 proxy — both enforcing the same filter. `HTTP_PROXY` / `HTTPS_PROXY` point at the HTTP proxy and `ALL_PROXY` at the SOCKS5 proxy; anything not on `network_allowlist` is refused. |

`network_allowlist` accepts CIDRs (`10.0.0.0/8`) and DNS patterns including wildcards (`*.pythonhosted.org`). It's only consulted when `network_mode="allowlist"`.

The two proxies exist so different clients can be filtered the same way: HTTP libraries (pip, curl, requests, boto3, huggingface_hub) honour `HTTPS_PROXY`, while non-HTTP TCP clients (git, ssh, database drivers) honour `ALL_PROXY` and route through the SOCKS5 proxy. Both apply the same deny-then-allow check.

## The deny-list

`network_denylist` is the inverse of the allow-list: a set of CIDRs and DNS patterns that are blocked, checked before the allow-list (deny wins). It's a session-level policy. Pass it to `sb.on_device.session(...)` / `sb.session(...)`, not to `run()`, and it's valid with `network_mode="open"` or `"allowlist"` (it has no meaning under `"blocked"`, which already denies everything).

It unlocks two postures a plain allow-list can't express:

- Open egress with carve-outs — `network_mode="open"` plus `network_denylist=[...]`: full egress, except a few named destinations. Everything not denied is allowed.
- A hole punched in an allow-list — `network_mode="allowlist"` plus `network_denylist=[...]`: a host is blocked even when it matches an allow-list wildcard.

```python
async with await sb.session(
    network_mode="open",
    network_denylist=sb.CLOUD_METADATA_DENY,   # block cloud-metadata endpoints, allow the rest
) as sbx:
    ...
```

> [!WARNING] `open` mode does not auto-guard internal ranges
> When you ask for `network_mode="open"`, the internal-IP SSRF backstop is intentionally off since you asked for open egress. So a deny-list-only posture must name the sensitive endpoints explicitly. A bare `169.254.169.254` misses the rest of the link-local range and every IPv6 metadata endpoint, which is exactly what `sb.CLOUD_METADATA_DENY` exists for.

### Blocking cloud metadata

`sb.CLOUD_METADATA_DENY` is an exported list of the well-known cloud instance-metadata (IMDS) and link-local endpoints like the AWS/GCP/Azure IMDS address `169.254.169.254`, the wider IPv4 link-local range, the GCP `metadata.google.internal` hostname, and the AWS IPv6 IMDS endpoint. Splat it into your deny-list and add your own entries:

```python
network_denylist=[*sb.CLOUD_METADATA_DENY, "10.0.0.0/8"]
```

Like the allow-list, this is a guardrail for honest clients, not containment (see the warning below).

## Bring-your-own egress proxy

Instead of the built-in allow/deny proxy, you can route a session's egress through your own inspecting proxy (mitmproxy, squid, a sidecar). Set `network_proxy_url` on the session; the sandbox injects it into the child's `HTTP_PROXY` / `HTTPS_PROXY` and does not start its own proxy. Filtering and inspection are then entirely your proxy's responsibility. `network_allowlist` and `network_denylist` are not applied by the sandbox in this mode. Add a companion `network_socks_url` (`socks5h://...`) to back `ALL_PROXY` so non-HTTP clients route through it too. Both are only meaningful with `network_mode="open"` or `"allowlist"`.

```python
async with sb.on_device.session(
    backend="userns",
    network_mode="open",
    network_proxy_url="http://127.0.0.1:8080",   # your inspecting proxy
    network_socks_url="socks5h://127.0.0.1:1080",
) as sbx:
    ...
```

## What the allow-list actually constrains

> [!WARNING] The allow-list and deny-list are proxy-based, not a kernel wall
> `network_allowlist` and `network_denylist` constrain clients that honour the proxy environment variables: `HTTPS_PROXY` (pip, curl, requests, boto3, huggingface_hub, and most HTTP libraries) and `ALL_PROXY` (git, ssh, database drivers, and other SOCKS5-aware TCP clients). They are not a kernel-level firewall. Adversarial code that bypasses the proxies (raw sockets, DNS-over-UDP, anything that ignores env vars) will not be filtered.
>
> For a hard network boundary against untrusted code, use `network_mode="blocked"`. The allow-list and deny-list are for convenience under trust, not adversarial isolation.

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
    await sbx.run("uv pip install numpy")                        # uses session default
    await sbx.run("python untrusted.py", network_mode="blocked") # tightened
```

## Session default vs per-call override

Two places set network posture, and they accept the same two arguments:

| Where you set it                            | Arguments                             | What it controls                                                                                                                                  |
| ------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sb.on_device.session(...)` / `sb.session(...)` | `network_mode=`, `network_allowlist=`, `network_denylist=` | Default for every `run()` in the session. On a remote sandbox this _also_ sets the pod-level network posture, so the per-call proxy can dial out. |
| `run(...)`                                  | `network_mode=`, `network_allowlist=` | The posture for this one call. Overrides the session default.                                                                                     |

> [!IMPORTANT] Session-level posture sets the pod's network on remote
> On a remote sandbox, the session-level `network_mode` _determines whether the sandbox-server pod has any network at all._ `network_mode="blocked"` at the session level means the pod has no egress, period. A per-call `run(network_mode="allowlist", ...)` will then fail with `Temporary failure in name resolution`, because the per-call proxy has nowhere to dial out from.
>
> Rule of thumb: set the session-level `network_mode` to the **broadest** posture any `run()` in the session needs, then tighten per call. If a session has even one step that needs `pypi.org`, set `network_mode="allowlist"` (or `"open"`) on `sb.session()`; the per-call defaults on other `run()`s will still be `"blocked"`.

## How the proxies are implemented

The on-device transport spins up two short-lived proxies for the `run()` call: an HTTP CONNECT proxy (`HTTP_PROXY` / `HTTPS_PROXY`) and a SOCKS5 proxy (`ALL_PROXY`). Each checks the target against the deny-list first and then the allow-list, and either dials out or refuses (`403` for the HTTP proxy). There is no shared state between calls; each `run()` gets a fresh pair with the policy you passed in. On a remote sandbox the same filtering runs server-side in the sandbox-server pod.

## Related

- [Security model](./security-model). What network isolation buys you and what it doesn't.
- [Running commands](./running-commands). Other `run()` arguments.
- [Filesystem](./filesystem). Staging data into a blocked sandbox with `put_bytes`.
