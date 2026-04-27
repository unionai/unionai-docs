---
title: Run modes
weight: 4
variants: +flyte +union
---

# Run modes

Flyte supports three execution modes, letting you choose the right trade-off between speed and fidelity at each stage of development:

{{< grid cols=3 >}}

{{< link-card target="running-locally" icon="laptop" title="Local" >}}
Run tasks and apps directly in your local Python process with no K8s cluster or Docker required. Ideal for rapid iteration and debugging.
{{< /link-card >}}

{{< link-card target="running-devbox" icon="box" title="Devbox" >}}
Run tasks and apps in a lightweight Flyte cluster using Docker. Get the full Flyte UI and backend experience on your machine.
{{< /link-card >}}

{{< variant union >}}

{{< link-card target="running-remote" icon="cloud" title="Remote" >}}
Run tasks and apps on a remote Flyte or Union cluster with full production capabilities including GPUs, distributed compute, and cloud-scale resources.
{{< /link-card >}}

{{< /variant >}}

{{< /grid >}}

{{< variant flyte >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Devbox |
|--------|-------------------|--------|
| **⚡️ Execution** | In-process Python | Containerized, local Docker |
| **🐳 Docker required** | No | Yes |
| **💻 Flyte UI** | No (TUI only) | Yes (`localhost:30080`) |
| **📦 Container images** | Ignored | Built locally |
| **🔀 Parallelism** | Sequential | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features |

The same task code runs unchanged across all the two modes. Start local for fast feedback, move to the devbox to validate containerized execution, then deploy to a remote cluster for production.

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Devbox | Remote |
|--------|-------------------|--------|--------|
| **⚡️ Execution** | In-process Python | Containerized, local Docker | Containerized, cloud |
| **🐳 Docker required** | No | Yes | No (remote build) |
| **💻 Flyte UI** | No (TUI only) | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally or remotely |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged across all three modes. Start local for fast feedback, move to the devbox to validate containerized execution, then deploy to a remote cluster for production.

{{< /markdown >}}
{{< /variant >}}