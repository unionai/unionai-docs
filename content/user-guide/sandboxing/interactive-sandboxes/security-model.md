---
title: Security model
weight: 2
variants: -flyte +union
---

# Security model

> [!NOTE] On-device is for development, remote is for production
> An on-device sandbox shares a container with the code that launched it. That's fine for development on a laptop, CI or sanity-checking your install, but it doesn't isolate the sandboxed process from your task's own code, secrets and cloud credentials. This page is about production posture, which means a remote sandbox. The "blast radius" section below justifies why; the rest of the page assumes you're picking knobs on a remote `SandboxEnvironment`.

A production sandbox is built from two independent layers:

1. **The isolation backend** running inside the sandbox pod, which constrains the sandboxed process (filesystem, syscalls, capabilities, network namespace).
2. **The pod runtime**, which is whether the pod's syscalls hit the host kernel directly or go through a user-space kernel like gVisor.

These are independent. A sandbox pod can run `userns` inside a gVisor pod, or `bubblewrap` inside a vanilla container pod. Pick each layer for what it actually defends against.

## Isolation backends

The library reports the backend on each process as `proc.backend`. On a remote sandbox, set it with `SandboxEnvironment(sandbox_mode=...)`.

| Backend        | How it works                                                                                                        | Default?                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `userns`       | `unshare(2)` + `prctl(NO_NEW_PRIVS)` + `capset` + `setrlimit`, plus Landlock and a seccomp BPF deny-list            | Remote default                                                                                        |
| `bubblewrap`   | `bwrap(1)` with `--unshare-all --die-with-parent --cap-drop ALL`, plus a Landlock ruleset as a kernel-side backstop | On-device default (needs `CAP_SYS_ADMIN` + unconfined AppArmor); opt-in for remote (`DEFAULT_SANDBOX_ENV_BWRAP` or `sandbox_mode="bwrap"`) |
| `sandbox-exec` | macOS wrapper around Apple's `sandbox-exec`; restricts writes to the work dir and can deny outbound sockets         | macOS on-device only                                                                                  |
| `none`         | `setpgid` + best-effort `setrlimit`; logs a warning                                                                 | Dev only (no isolation)                                                                               |

Both `userns` and `bubblewrap` layer namespaces, dropped capabilities, a [Landlock](https://docs.kernel.org/userspace-api/landlock.html) filesystem ruleset, and a seccomp BPF deny-list. They are not equally strong though: `bubblewrap` is the stronger backend. With `CAP_SYS_ADMIN` it pivots into a fresh mount root, which closes the gap where the sandbox shares the pod's root filesystem. `userns` is the lite variant: it runs in a vanilla pod with no extra capabilities, but it leaves that shared-rootfs gap open, so its mount isolation is weaker.

The remote default is `userns` because it runs anywhere (`bwrap` needs `CAP_SYS_ADMIN` + unconfined AppArmor and isn't always present in minimal images). When you can grant the pod those capabilities and want the strongest in-pod isolation, choose `bubblewrap`.

## Pod security for the bubblewrap backend

`bubblewrap` runs as a non-root user via unprivileged user namespaces. But the containerd default seccomp profile only permits the `mount` / `pivot_root` / `setns` / `unshare` syscalls `bwrap` needs when the container's capability set includes `CAP_SYS_ADMIN`, and the default AppArmor profile must be `unconfined` so those calls aren't blocked.

`flyte.PodTemplate().allow_nested_sandboxing()` grants exactly that: `CAP_SYS_ADMIN` plus unconfined AppArmor, `allowPrivilegeEscalation: false`. How you apply it depends on the transport:

- On-device: put it on the task that opens the session, since the sandbox child runs in that pod.

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

- Remote: the `SandboxEnvironment` derives the pod template from `sandbox_mode` / `sys_cap_admin` for you and `sandbox_mode="bwrap"` carries the grant automatically. See [Deployment](./deployment).

The `userns` backend needs none of this because it runs in a vanilla pod. Choose `userns` when you can't (or don't want to) grant the pod extra capabilities; choose `bubblewrap` when you can, for its stronger isolation — at the cost of the `CAP_SYS_ADMIN` + AppArmor grant above.

## Blast radius: why remote

The backend constrains the sandboxed process. What an _escaping_ process can reach is determined by where the sandbox runs.

> [!WARNING] An on-device sandbox shares the caller's container
> An on-device sandbox runs inside the same container as the code that launched it. If the backend is breached, the escaping process can reach your task's own code, mounted secrets, and service-account or cloud credentials. The pod boundary is the only thing still containing it; unless the task pod itself runs under gVisor, that boundary is the host kernel.
>
> This matters only when the sandboxed code is untrusted: for trusted code (your own prompts and tools, not exposed to end users) on-device is a perfectly good production choice. When the code is untrusted, prefer a remote sandbox so an escape lands in a throwaway pod, not your workload.

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

Backend choice does affect isolation strength: `bubblewrap` is stronger than `userns`-lite (it closes the shared-rootfs gap, as above), so prefer `bubblewrap` when the pod can carry `CAP_SYS_ADMIN` + AppArmor and `userns` when it can't. But both are solid process-level isolation that's fine for production in a normal container pod. You don't need gVisor to run a sandbox responsibly. The bigger lever as trust drops is the pod runtime (`container` vs `gvisor`) and tenant isolation (shared `SandboxEnvironment` vs one per tenant).

| Trust level                                                   | Pod runtime           | Tenant isolation                                               | Per-call notes                                                                                                            |
| ------------------------------------------------------------- | --------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Trusted (your own code/prompts, not exposed to end users)     | `container`           | Shared env is fine                                             | Default `network_mode="blocked"`; allow-list when you need it. Process isolation is sufficient.                          |
| Semi-trusted (vetted third-party libraries, your own ML code) | `container`           | Shared env is fine                                             | Default `network_mode="blocked"`; allow-list when you need it.                                                            |
| Untrusted (LLM-generated from end-user input, user-submitted) | `gvisor` (recommended) | Shared env is fine                                             | Stage inputs via `put_bytes`; keep `network_mode="blocked"` unless a step needs egress.                                   |
| Multi-tenant, hostile inputs assumed                          | `gvisor`           | One `SandboxEnvironment` per tenant; no cross-tenant pod reuse | `network_mode="blocked"` on every `run()`; the proxy allow-list is not adversarial-safe (see [Networking](./networking)). |

The principle: **let the workload pick the floor, let the threat model pick the ceiling**. The default backend is the floor and is appropriate for the common case. Reach for gVisor when you're actually running hostile code or sharing the system across tenants — not as a blanket requirement.

## What's not in scope

- **Side-channel attacks** (timing, cache, Spectre-class) are not addressed by any backend here. If you need defense against them, you need hardware partitioning, not a sandbox.
- **Resource exhaustion** is bounded by `Resources(...)` on the sandbox pod and per-call `timeout_s` on `run()`. The backends do not prevent a sandboxed process from using all the CPU and memory the pod gives it.
- **The proxy-based network allow-list** is not a kernel-level firewall. See [Networking](./networking) for what it does and does not protect against.

## Related

- [Networking](./networking). Per-call `network_mode` and what the allow-list actually constrains.
- [Filesystem](./filesystem). Default filesystem allow-list and how to extend it.
- [Deployment](./deployment). `SandboxEnvironment`, custom images, and per-launch overrides.
