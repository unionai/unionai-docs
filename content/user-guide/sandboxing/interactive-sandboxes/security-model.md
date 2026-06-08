---
title: Security model
weight: 2
variants: -flyte +union
---

# Security model

> [!NOTE] On-device is for development, remote is for production
> An **on-device** sandbox shares a container with the code that launched it. That's fine for development on a laptop, CI, or sanity-checking your install, but it doesn't isolate the sandboxed process from your task's own code, secrets, and cloud credentials. **This page is about production posture, which means a remote sandbox.** The "blast radius" section below justifies why; the rest of the page assumes you're picking knobs on a remote `SandboxEnvironment`.

A production sandbox is built from two independent layers:

1. **The isolation backend** running _inside_ the sandbox pod, which constrains the sandboxed process (filesystem, syscalls, capabilities, network namespace).
2. **The pod runtime**, which is whether the pod's syscalls hit the host kernel directly or go through a user-space kernel like gVisor.

These are independent. A sandbox pod can run `userns` inside a gVisor pod, or `bubblewrap` inside a vanilla container pod. Pick each layer for what it actually defends against.

## Isolation backends

The backend is always **explicit** — there's no auto-detection and no silent downgrade. On-device, you pass it as `sb.on_device.session(backend=...)`; on remote, you set it with `SandboxEnvironment(sandbox_mode=...)`. If the chosen backend isn't usable where the session runs (e.g. `bubblewrap` on a pod without `CAP_SYS_ADMIN`), `run()` fails loudly rather than falling back to weaker isolation. The library reports the active backend on each process as `proc.backend`.

| Backend        | How it works                                                                                                        | Notes                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `bubblewrap`   | `bwrap(1)` with `--unshare-all --die-with-parent --cap-drop ALL`, plus a Landlock ruleset as a kernel-side backstop | Strongest; the default on-device `backend`. Needs `CAP_SYS_ADMIN` + unconfined AppArmor on the pod (see below). |
| `userns`       | `unshare(2)` + `prctl(NO_NEW_PRIVS)` + `capset` + `setrlimit`, plus Landlock and a seccomp BPF deny-list            | Lite backend; runs in a vanilla pod with no extra capabilities. Remote default (`sandbox_mode`). |
| `sandbox-exec` | macOS wrapper around Apple's `sandbox-exec`; restricts writes to the work dir and can deny outbound sockets         | macOS on-device only                                                                                      |
| `none`         | `setpgid` + best-effort `setrlimit`; logs a warning                                                                 | Dev fallback only; no filesystem/network jail                                                          |

Both `userns` and `bubblewrap` layer namespaces (user, mount, UTS, IPC, net), dropped capabilities, and a [Landlock](https://docs.kernel.org/userspace-api/landlock.html) filesystem ruleset. `userns` additionally enforces a seccomp BPF deny-list for syscalls with no legitimate purpose in a sandbox.

`bubblewrap` and `userns` are equivalent in security posture. The practical difference is the pod they need: `userns` runs anywhere (a vanilla unprivileged pod), while `bubblewrap` needs the pod to carry `CAP_SYS_ADMIN` + an unconfined AppArmor profile. The remote default is `userns` for that reason (`bwrap` also isn't always present in minimal images). Pick `bubblewrap` if you prefer its ruleset model or already rely on it.

## Pod security for the bubblewrap backend

`bubblewrap` runs as a **non-root** user via unprivileged user namespaces — it is not privileged. But the containerd default seccomp profile only permits the `mount` / `pivot_root` / `setns` / `unshare` syscalls `bwrap` needs when the container's capability set includes `CAP_SYS_ADMIN`, and the default AppArmor profile must be `unconfined` so those calls aren't blocked.

`flyte.PodTemplate().allow_nested_sandboxing()` grants exactly that — `CAP_SYS_ADMIN` plus unconfined AppArmor, `allowPrivilegeEscalation: false`, and nothing else. How you apply it depends on the transport:

- **On-device:** put it on the task that opens the session, since the sandbox child runs in that pod.

  ```python
  bwrap_env = flyte.TaskEnvironment(
      name="sandboxed-task",
      image=sb.base_sandbox_image,
      pod_template=flyte.PodTemplate().allow_nested_sandboxing(),
  )

  @bwrap_env.task
  async def main() -> str:
      async with sb.on_device.session(backend="bubblewrap") as sbx:
          ...
  ```

- **Remote:** the `SandboxEnvironment` derives the pod template from `sandbox_mode`/`sys_cap_admin` for you — `sandbox_mode="bwrap"` carries the grant automatically. See [Deployment](./deployment).

The `userns` backend needs **none** of this — it runs in a vanilla pod. Choose `userns` to keep the pod's host attack surface minimal; choose `bubblewrap` (with the template) when you want its ruleset.

## Blast radius: why remote

The backend constrains the sandboxed process. What an _escaping_ process can reach is determined by where the sandbox runs.

> [!WARNING] An on-device sandbox shares the caller's container
> An on-device sandbox runs inside the **same container as the code that launched it**. If the backend is breached, the escaping process can reach your **task's own code, mounted secrets, and service-account or cloud credentials**. The pod boundary is the only thing still containing it; unless the **task pod itself** runs under gVisor, that boundary is the host kernel.
>
> Treat on-device as a dev-time convenience, not a production isolation boundary.

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
