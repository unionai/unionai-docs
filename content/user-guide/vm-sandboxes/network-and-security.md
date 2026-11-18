---
title: Network and security
description: What code in a VM sandbox can and cannot reach, how to open the network safely, and where secrets, snapshots, and published disks can expose data.
weight: 6
variants: -flyte +union
---

# Network and security

Your agent needs `pip install` to work, but it should not be able to send your repository to an address it read in a web page. A VM sandbox starts with no network at all. You open exactly what the code needs, and the policy is enforced outside the VM, where the code cannot change it.

```python
from flyteplugins.union import sandbox

agent_env = sandbox.SandboxEnvironment(
    name="coding-agent",
    network=sandbox.Network.allow("pypi.org", "*.pypi.org", "files.pythonhosted.org", "github.com"),
)
```

## Choose a network

| Network | What the sandbox can reach |
| --- | --- |
| `sandbox.Network.blocked()` | Nothing but its own loopback. The default. |
| `sandbox.Network.pypi()` | Only PyPI: `pypi.org`, `*.pypi.org`, and `files.pythonhosted.org`. |
| `sandbox.Network.allow(*domains, cidrs=())` | Only the domains and CIDR ranges you list. `*.example.com` matches subdomains. |
| `sandbox.Network.internet()` | All outbound traffic, except the ranges below. |

How the rules apply:

- **Enforced outside the VM.** The microVM has no network device. Its traffic leaves only through an agent on the node, which applies the policy to every TCP and UDP flow. Code with root in the VM cannot change it.
- **Domain allowlists use the sandbox's own DNS.** Names not on the list do not resolve, and a TLS connection's server name must be one of the allowed domains.
- **Your cluster is closed unless you open it.** Private ranges (your cluster's pods, services, and nodes) are refused in every mode unless `cidrs` names them.
- **The cloud metadata server is always unreachable.** Link-local addresses, including `169.254.169.254`, are refused in every mode, even with `Network.internet()`. Code in a sandbox cannot read the node's cloud credentials.
- **TLS is end to end.** The agent checks the server name a connection asks for, but does not terminate TLS.
- **Nothing connects in from the network.** A sandbox is reached only through its session API, which takes the session's token. Servers in the sandbox are reached through `sb.port_url()`. Inside your cluster, that URL carries the token. See [Port URLs](#port-urls).

A network is either open or an allowlist. Setting both raises a `ValueError`.

To reach an internal service, such as a package mirror in your VPC, allow its range explicitly:

```python
sandbox.Network.allow("pypi.internal.example.com", cidrs=("10.20.0.0/24",))
```

## What isolates a sandbox

This table describes the default runtime, a microVM. A gVisor sandbox (`runtime_class="gvisor"`) isolates code with a user-space kernel instead of a virtual machine, and can run on the nodes that run your other workloads. See [Isolation trade-offs](./runtimes#isolation-trade-offs) before you choose it for hostile code.

| Layer | What it gives you |
| --- | --- |
| A microVM per session | Each session is a Firecracker VM with its own guest kernel. A kernel exploit in one sandbox does not land in the node's kernel or in another sandbox. |
| A disk per session | Each session runs on its own disk, or its own copy-on-write copy of a committed disk. One session never sees another's writes. |
| No pod, no service account | A session is not a Kubernetes pod. It has no service account token and no cloud identity of its own. |
| A dedicated node pool | Sessions run on your microVM node pool, separate from the nodes that run your task pods. |
| Network policy outside the VM | See [Choose a network](#choose-a-network). |

## Trade-offs to plan for

The VM boundary protects your infrastructure from the code. It does not protect anything you put inside the VM. Each of these is a way to hand untrusted code something it should not have.

### Secrets

A secret declared on a `SandboxEnvironment` is mounted into the VM. Every command in the session can read it, including the untrusted code.

> [!WARNING] Keep credentials with the driver
> Do not give a sandbox your model API key, a cloud credential, or a token with write access, unless the code in it must have that credential. Keep credentials in the task, app, or script that drives the sandbox. The driver calls the model, sends commands into the sandbox, and reads results out. This is how the [SWE-Gym tutorial](../../tutorials/reinforcement-learning/swe-gym-sandboxes/_index) is built: the sandboxes get no secrets and, except for one build step, no network.

If a sandbox needs a credential, scope it to what that code needs: a read-only token, and a network allowlist with only the host it is for. An allowlist limits where a stolen secret can be sent.

Secrets work only on microVM nodes configured for them. On a node without that configuration, a session that declares a secret fails with `SecretNotFound`. Ask your Union.ai solutions team.

### Snapshots and forks with memory

`sb.snapshot()`, `sb.suspend()`, and `sb.fork(memory=True)` copy a VM's memory. Anything in memory goes with it: secrets that a process read, tokens, keys, and random state already drawn. A session restored from a snapshot shares all of it with the original. Snapshots are stored in your data plane's object store. See [Snapshot, suspend, and resume](./snapshots).

### Published and committed disks

A committed or published disk holds every file the session left on it, including files the untrusted code wrote. If a published disk is the starting point for later sessions, anything the code planted on it, such as a modified `~/.bashrc` or a patched package, runs in every later session. Publish disks from sessions whose code you trust, such as a build step, and start untrusted work on copies of them.

Published disks are artifacts in your project. Anyone who can read artifacts in that project can start a session on them.

### Port URLs

`sb.port_url(port)` is how your code reaches a server in the sandbox. What the URL exposes depends on where it was made:

- **From a task or an app**, the URL is the session's address in your cluster and includes the session's token. Anyone who has the URL, and can reach your cluster's network, can call into the sandbox. Keep it in the driver. Do not send it to a browser, log it, or return it from an API.
- **From outside the cluster**, the URL is a Union.ai data proxy URL with no token in it. Each request needs the caller's own Union.ai credentials.

To show a sandbox's server to a user, have your app proxy the requests and keep the URL on the server side.

### Where the driver runs

The code that drives a sandbox (calls `sb.run`, reads files, holds credentials) runs in an ordinary task, app, or script. The sandbox protects that driver from the commands it sends. It does not protect the driver from output it trusts. Treat output from a sandbox as untrusted input: don't `eval` it, don't use it to build shell commands for the driver's own machine, and size-limit what you read.

## Calls and permissions

- Opening a session takes permission to create runs in the project, as running a task does.
- From outside a cluster, every call to a session goes through the Union.ai data proxy and is authorized as the user or API key that signed in. Port URLs from `sb.port_url()` need the same credentials. Nothing on the path holds the session's own token except the platform.
- Inside a cluster, tasks and apps call a session's address directly.

## Related pages

- [Sandboxing](../agents/sandboxing/_index): the risks of running LLM-generated code, and the other sandbox types Flyte offers.
- [Configure a sandbox](./configure).
