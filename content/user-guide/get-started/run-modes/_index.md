---
title: Run modes
description: Run the same task code in your Python process, on a devbox, or on a remote cluster.
icon: play-circle
weight: 3
variants: +flyte +union
---

# Run modes

{{< key product_full_name >}} supports three execution modes, letting you choose the right trade-off between speed and fidelity at each stage of development:

## Two things vary, not one

Each mode answers two separate questions, and it helps to keep them apart:

- **How the task runs.** Either **in-process**, directly in your Python interpreter, or **on-cluster**, inside a container that a Flyte cluster schedules. The `--local` flag selects in-process.
- **Where the cluster is.** Either a **local cluster** on your own machine, or a **remote cluster** somewhere else.

The devbox is why the distinction matters: it is a real Flyte cluster, so tasks run on-cluster in containers, but it runs on your laptop. It is on-cluster and local at the same time.

Throughout the docs, **remote** always answers the second question. A remote cluster is one that is not on your machine. Containerized execution is called **on-cluster**, never remote.

|                    | In-process              | On-cluster |
|--------------------|-------------------------|------------|
| **Local machine**  | Local (`--local`)       | Devbox     |
| **Remote cluster** | —                       | Remote     |

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
| **⚡️ Execution** | In-process Python | On-cluster, local Docker | On-cluster, your remote cluster |
| **🐳 Docker required** | No | Yes | Yes (local image build) |
| **💻 Flyte UI** | No (TUI only) | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally, pushed to a registry |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged across all three modes. Start with local execution for fast feedback, move to the Devbox to validate on-cluster execution, then deploy to your Flyte cluster for production.

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Devbox | Remote |
|--------|-------------------|--------|--------|
| **⚡️ Execution** | In-process Python | On-cluster, local Docker | On-cluster, remote |
| **🐳 Docker required** | No | Yes | No (remote build) |
| **💻 Flyte UI** | TUI, or the console with `--tracked` | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally or remotely |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged across all three modes. Start with local execution for fast feedback, move to the Devbox to validate on-cluster execution, then deploy to a remote cluster for production.

{{< /markdown >}}
{{< /variant >}}
