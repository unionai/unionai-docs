---
title: Run modes
description: Run the same task code locally in your Python process, or remotely on a devbox or a deployed cluster.
icon: play-circle
weight: 3
variants: +flyte +union
---

# Run modes

A run is either **local** or **remote**. The same task code runs unchanged either way, so you can choose the right trade-off between speed and fidelity at each stage of development.

## Local and remote

- **Local** runs the task in-process, directly in your Python interpreter. There is no cluster and no container. Select it with `flyte run --local` or `flyte.with_runcontext(mode="local")`.
- **Remote** runs the task on a Flyte backend, inside a container that a cluster schedules. It is the default: `flyte run` without `--local`, or `mode="remote"`. Your configuration decides which backend.

A remote backend is either a **devbox** on your own machine or a **deployed cluster** in the cloud or on-premises. "Remote" describes how the run executes, not where the machine is: a devbox run is remote even though the devbox runs on your laptop. This is how the CLI and SDK use the word throughout.

| Mode | How the task runs | Backend |
|------|-------------------|---------|
| Local (`--local`) | In-process | None |
| Remote | In a container, on a cluster | A devbox on your machine |
| Remote | In a container, on a cluster | A deployed cluster, in the cloud or on-premises |

{{< variant union >}}
{{< markdown >}}

### Watching a local run

A local run can also report its progress to {{< key product_name >}}. Add `--tracked` and the run still executes in-process on your machine, but it appears in the console under **Tracked Runs**. Tracking changes what you can see, not where the run executes. See [Track local runs in the console](./running-locally#track-local-runs-in-the-console).

{{< /markdown >}}
{{< /variant >}}

{{< grid cols=3 >}}

{{< link-card target="running-locally" icon="laptop" title="Local" >}}
Run tasks and apps directly in your local Python process with no Kubernetes cluster or Docker required. Ideal for rapid iteration and debugging.
{{< /link-card >}}

{{< link-card target="running-devbox" icon="box" title="Devbox" >}}
Run tasks and apps in a lightweight Flyte cluster using Docker. Get the full Flyte UI and backend experience on your machine.
{{< /link-card >}}

{{< link-card target="running-remote" icon="cloud" title="Deployed cluster" >}}
Run tasks and apps on a deployed cluster, in the cloud or on-premises, with full production capabilities including GPUs and distributed compute.
{{< /link-card >}}

{{< /grid >}}

{{< variant flyte >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Remote: devbox | Remote: deployed cluster |
|--------|-------------------|--------|--------|
| **⚡️ Execution** | In-process Python | On-cluster, local Docker | On-cluster, your Flyte cluster |
| **🐳 Docker required** | No | Yes | Yes (local image build) |
| **💻 Flyte UI** | No (TUI only) | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally, pushed to a registry |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged on all three. Start with local execution for fast feedback, move to the Devbox to validate on-cluster execution, then deploy to your Flyte cluster for production.

{{< /markdown >}}
{{< /variant >}}

{{< variant union >}}
{{< markdown >}}

| Aspect | Local (`--local`) | Remote: devbox | Remote: deployed cluster |
|--------|-------------------|--------|--------|
| **⚡️ Execution** | In-process Python | On-cluster, local Docker | On-cluster, cloud or on-premises |
| **🐳 Docker required** | No | Yes | No (remote build) |
| **💻 Flyte UI** | TUI, or the console with `--tracked` | Yes (`localhost:30080`) | Yes |
| **📦 Container images** | Ignored | Built locally | Built locally or remotely |
| **🔀 Parallelism** | Sequential | Cluster-level | Cluster-level |
| **⭐️ Best for** | Fast iteration, debugging | Testing container builds, full Flyte features | Production, GPUs, scale |

The same task code runs unchanged on all three. Start with local execution for fast feedback, move to the Devbox to validate on-cluster execution, then run on a deployed cluster for production.

{{< /markdown >}}
{{< /variant >}}
