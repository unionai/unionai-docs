---
title: Run modes
weight: 4
variants: +flyte +union
---

# Run modes

{{< key product_full_name >}} supports three execution modes, letting you choose the right trade-off between speed and fidelity at each stage of development:

{{< grid cols=3 >}}

{{< link-card target="running-locally" icon="laptop" title="Local" >}}
Run tasks and apps directly in your local Python process with no Kubernetes cluster or Docker required. Ideal for rapid iteration and debugging.
{{< /link-card >}}

{{< link-card target="running-devbox" icon="box" title="Devbox" >}}
Run tasks and apps in a lightweight Flyte cluster using Docker. Get the full Flyte UI and backend experience on your machine.
{{< /link-card >}}

{{< link-card target="running-remote" icon="cloud" title="Remote" >}}
Run tasks and apps on a remote cluster with full production capabilities including GPUs, distributed compute, and cloud-scale resources.
{{< /link-card >}}

{{< /grid >}}

{{< variant flyte >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Devbox | Remote |
|--------|-------------------|--------|--------|
| **⚡️ Execution** | In-process Python | Containerized, local Docker | Containerized, on your cluster |
| **🐳 Docker required** | No | Yes | Yes (local image build) |
| **💻 Flyte UI** | No (TUI only) | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally, pushed to a registry |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged across all three modes. Start with local execution for fast feedback, move to the Devbox to validate containerized execution, then deploy to your Flyte cluster for production.

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

The same task code runs unchanged across all three modes. Start with local execution for fast feedback, move to the Devbox to validate containerized execution, then deploy to a remote cluster for production.

{{< /markdown >}}
{{< /variant >}}
