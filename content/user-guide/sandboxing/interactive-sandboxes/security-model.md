---
title: Security model
weight: 2
variants: -flyte +union
---

# Security model

> [!NOTE] Local is for development, remote is for production
> A **local** sandbox shares a container with the code that launched it. That's fine for development on a laptop, CI, or sanity-checking your install, but it doesn't isolate the sandboxed process from your task's own code, secrets, and cloud credentials. **This page is about production posture, which means a remote sandbox.** The "blast radius" section below justifies why; the rest of the page assumes you're picking knobs on a remote `SandboxEnvironment`.

A production sandbox is built from two independent layers:

1. **The isolation backend** running _inside_ the sandbox pod, which constrains the sandboxed process (filesystem, syscalls, capabilities, network namespace).
2. **The pod runtime**, which is whether the pod's syscalls hit the host kernel directly or go through a user-space kernel like gVisor.

These are independent. A sandbox pod can run `userns` inside a gVisor pod, or `bubblewrap` inside a vanilla container pod. Pick each layer for what it actually defends against.

## Isolation backends

The library reports the backend on each process as `proc.backend`. On a remote sandbox, set it with `SandboxEnvironment(sandbox_mode=...)`.

| Backend        | How it works                                                                                                        | Default?                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `userns`       | `unshare(2)` + `prctl(NO_NEW_PRIVS)` + `capset` + `setrlimit`, plus Landlock and a seccomp BPF deny-list            | Remote default                                                                                        |
| `bubblewrap`   | `bwrap(1)` with `--unshare-all --die-with-parent --cap-drop ALL`, plus a Landlock ruleset as a kernel-side backstop | Opt-in for remote (`DEFAULT_SANDBOX_ENV_BWRAP` or `sandbox_mode="bwrap"`); default for local on Linux |
| `sandbox-exec` | macOS wrapper around Apple's `sandbox-exec`; restricts writes to the work dir and can deny outbound sockets         | macOS local only                                                                                      |
| `none`         | `setpgid` + best-effort `setrlimit`; logs a warning                                                                 | Dev fallback only                                                                                     |

Both `userns` and `bubblewrap` layer namespaces (user, mount, UTS, IPC, net), dropped capabilities, and a [Landlock](https://docs.kernel.org/userspace-api/landlock.html) filesystem ruleset. `userns` additionally enforces a seccomp BPF deny-list for syscalls with no legitimate purpose in a sandbox.

The remote default is `userns` rather than `bubblewrap` because `bwrap` isn't always present in minimal container images. They are equivalent in security posture; pick `bubblewrap` if you prefer its ruleset model or already rely on it.

## Blast radius: why remote

The backend constrains the sandboxed process. What an _escaping_ process can reach is determined by where the sandbox runs.

> [!WARNING] A local sandbox shares the caller's container
> A local sandbox runs inside the **same container as the code that launched it**. If the backend is breached, the escaping process can reach your **task's own code, mounted secrets, and service-account or cloud credentials**. The pod boundary is the only thing still containing it; unless the **task pod itself** runs under gVisor, that boundary is the host kernel.
>
> Treat local as a dev-time convenience, not a production isolation boundary.

A remote sandbox runs in its own pod with:

- a typically minimal image (no caller code, no toolchain)
- its own service account (no task secrets, no cloud credentials)
- no access to whatever the caller mounted

The escape blast radius is the sandbox pod, not your workload. Hardening that pod with gVisor (below) further reduces what an escape can do to the host kernel.

## Pod runtime: gVisor

Independent from the in-pod backend:

- `sandbox_mode` (`userns` or `bwrap`) selects the **in-pod** backend constraining the sandboxed process.
- `runtime` (`container` or `gvisor`) selects how the **pod itself** is run.

Setting `runtime="gvisor"` puts `runtimeClassName: gvisor` on the sandbox pod, so its syscalls go through the [gVisor](https://gvisor.dev/) application kernel rather than hitting the host kernel directly. Recommended whenever the sandboxed code is untrusted or the workload is multi-tenant.

```python
hardened = sb.SandboxEnvironment(
    name="hardened-sandbox",
    sandbox_mode="userns",
    runtime="gvisor",
)
```

> [!NOTE] gVisor must be enabled on the cluster
> `runtime="gvisor"` requires the `gvisor` RuntimeClass to be installed and enabled in your cluster. In most cases, talk to your Union solutions engineer to enable it.

## Choosing a posture

Backend choice (`userns` vs `bwrap`) isn't really a threat-model decision; both layer namespaces, capability drops, and Landlock, and they're close enough in posture that the right call is usually "whatever is in your image." The defaults are fine for production. What _does_ change with trust level is the **pod runtime** (`container` vs `gvisor`) and **tenant isolation** (shared `SandboxEnvironment` vs one per tenant).

| Trust level                                                   | Pod runtime  | Tenant isolation                                               | Per-call notes                                                                                                            |
| ------------------------------------------------------------- | ------------ | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Semi-trusted (your own ML code, vetted third-party libraries) | `container`  | Shared env is fine                                             | Default `network_mode="blocked"`; allow-list when you need it.                                                            |
| Untrusted (LLM-generated, user-submitted, agent-generated)    | **`gvisor`** | Shared env is fine                                             | Stage inputs via `put_bytes`; keep `network_mode="blocked"` unless a step needs egress.                                   |
| Multi-tenant, hostile inputs assumed                          | **`gvisor`** | One `SandboxEnvironment` per tenant; no cross-tenant pod reuse | `network_mode="blocked"` on every `run()`; the proxy allow-list is not adversarial-safe (see [Networking](./networking)). |

The principle: **let the workload pick the floor, let the threat model pick the ceiling**. The default backend is the floor and is appropriate for the common case. Reach for gVisor when the kernel attack surface itself is in scope.

## What's not in scope

- **Side-channel attacks** (timing, cache, Spectre-class) are not addressed by any backend here. If you need defense against them, you need hardware partitioning, not a sandbox.
- **Resource exhaustion** is bounded by `Resources(...)` on the sandbox pod and per-call `timeout_s` on `run()`. The backends do not prevent a sandboxed process from using all the CPU and memory the pod gives it.
- **The proxy-based network allow-list** is not a kernel-level firewall. See [Networking](./networking) for what it does and does not protect against.

## Related

- [Networking](./networking). Per-call `network_mode` and what the allow-list actually constrains.
- [Filesystem](./filesystem). Default filesystem allow-list and how to extend it.
- [Deployment](./deployment). `SandboxEnvironment`, custom images, and per-launch overrides.
