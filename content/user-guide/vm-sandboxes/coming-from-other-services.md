---
title: Coming from other sandbox services
description: Map the concepts of a hosted sandbox service, such as templates, snapshots, and preview URLs, to their VM sandbox equivalents.
weight: 10
variants: -flyte +union
---

# Coming from other sandbox services

You have an agent that already runs on a hosted sandbox service, and you want to move it into your own cloud. Most of what you use has a direct equivalent. This table maps each concept to the call that replaces it.

| Concept | VM sandboxes |
| --- | --- |
| Sandbox template or configuration | `sandbox.SandboxEnvironment(...)` |
| Create a sandbox | `async with env.session("name") as sb:` |
| Run a command and wait | `await sb.run("pytest -x")` |
| Run a command and stream its output | `p = await sb.start(...)`, then `async for line in p.stdout` |
| Interactive terminal (PTY) | `sb.start("bash", tty=sandbox.Tty(rows, cols))` |
| File system | `sb.fs.read_text`, `write_text`, `ls`, `upload_dir`, `download_dir` |
| Network policy | `sandbox.Network.blocked()`, `.pypi()`, `.allow(...)`, `.internet()` |
| Preview URL for a port | `sb.port_url(8080)` |
| Named sandbox, reconnect later | `env.attach(name)` |
| Tags | `SandboxEnvironment(labels={...})` |
| Filesystem snapshot | `await sb.commit()` returns a `SandboxVolume` |
| Memory snapshot | `await sb.snapshot()` returns a `SandboxSnapshot` |
| Pause and resume | `await sb.suspend()`, then `env.session(name, snapshot=s)` |
| Persistent volume | `SandboxEnvironment(publish=...)` and `SandboxVolume.from_artifact(name)` |
| Terminate | Leave the `async with` block, or `await sb.cancel()` |

Two differences matter most:

- **Everything runs in your cloud.** The VMs, the code, and every saved disk and snapshot stay in your data plane. Scheduling goes through the Union.ai control plane, as it does for tasks.
- **Sandboxes are part of your runs.** A session opened from a task is an action in that task's run. Retries, caching, traces, and the run view in the UI apply to the code that drives the sandbox. Saved disks can be task inputs and outputs.
