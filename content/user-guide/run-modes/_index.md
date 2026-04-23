---
title: Run modes
weight: 4
variants: +flyte +union
sidebar_expanded: true
---

# Run modes

Flyte supports three execution modes, letting you choose the right trade-off between speed and fidelity at each stage of development:

{{< grid >}}

{{< link-card target="running-locally" icon="laptop" title="Local" >}}
Run tasks directly in your local Python process with no cluster or Docker required. Ideal for rapid iteration and debugging.
{{< /link-card >}}

{{< link-card target="running-devbox" icon="package" title="Devbox" >}}
Run tasks in a lightweight local Flyte cluster using Docker. Get the full Flyte environment — UI, scheduler, and containerized execution — on your machine.
{{< /link-card >}}

{{< link-card target="running-remote" icon="cloud" title="Remote" >}}
Run tasks on a remote Flyte or Union cluster with full production capabilities including GPUs, distributed compute, and cloud-scale resources.
{{< /link-card >}}

{{< /grid >}}

| Mode | Docker required | Flyte UI | Execution | Best for |
|------|----------------|----------|-----------|----------|
| **Local** | No | No (TUI only) | In-process Python | Fast iteration, debugging |
| **Devbox** | Yes | Yes (`localhost:30080`) | Containerized, local | Testing container builds, full Flyte features |
| **Remote** | No (remote build) | Yes | Containerized, cloud | Production, GPUs, scale |

The same task code runs unchanged across all three modes. Start local for fast feedback, move to the devbox to validate containerized execution, then deploy to a remote cluster for production.
