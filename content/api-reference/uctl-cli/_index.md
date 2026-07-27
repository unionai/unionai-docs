---
title: Uctl CLI
weight: 7
variants: -flyte +union
---

# Uctl CLI

`uctl` is a compiled (Go) command-line tool for **Union administrators**. In Flyte 2, most of its former
functionality has moved to the **`flyte` CLI** (and the `flyteplugins-union` plugin). `uctl` is now needed
only for a **narrow set of self-managed and organization-admin operations** that the `flyte` CLI does not
(yet) cover — chiefly **self-managed dataplane provisioning**.

> [!NOTE]
> For general CLI work — running and deploying workflows, and managing projects, secrets, roles, clusters,
> and queues — use the [`flyte` CLI](../flyte-cli/). Reach for `uctl` only for the self-managed / org-admin
> operations listed under [Commands](#commands) below.

## Which CLI do I use?

| Task | Use |
|------|-----|
| Run, deploy, and manage workflows, tasks, projects, secrets, RBAC, clusters, and queues | [`flyte` CLI](../flyte-cli/) — `flyte run`, `flyte deploy`, `flyte create …` |
| Set project/domain defaults (task resources, default queue, service account, labels…) | `flyte` settings — `flyte get settings` / `flyte edit settings` |
| Provision self-managed dataplane resources; manage cluster config templates, cluster node pools, and organization domains | **`uctl`** — see [Commands](#commands) |

Former `uctl` commands and their `flyte` equivalents:

| Former `uctl` command | Now |
|------|-----|
| `uctl create/get/update/delete execution` | `flyte run`, `flyte get run`, `flyte abort run`, `flyte rerun` |
| `uctl register` | `flyte deploy` |
| `uctl create/get/update project` | `flyte create/get/update project` |
| `uctl create/get/update/delete role` · `policy` · `api-key` · `user` · `cluster` · `cluster-pool` | `flyte create/get/update/delete role` · `policy` · `api-key` · `user` · `cluster` · `cluster-pool` |
| `uctl get/update task-resource-attribute`, `execution-queue-attribute`, `workflow-execution-config` | `flyte get/edit settings` (and `flyte create/get/update queue`) |
| `uctl config init` | `flyte create config` |
| `uctl demo` | `flyte start devbox` |

## Installation

{{< tabs >}}
{{< tab "macOS" >}}
{{< markdown >}}

To install `uctl` on a Mac, use [Homebrew](https://brew.sh/), `curl`, or manually download the binary.

**Homebrew**

```shell
$ brew tap unionai/homebrew-tap
$ brew install uctl
```

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Linux" >}}
{{< markdown >}}

To install `uctl` on Linux, use `curl` or manually download the binary.

**curl**

To use `curl`, set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< tab "Windows" >}}
{{< markdown >}}

To install `uctl` on Windows, use `curl` or manually download the binary.

**curl**

To use `curl`, in a Linux shell (such as [WSL](https://learn.microsoft.com/en-us/windows/wsl/install)), set `BINDIR` to the install location (it defaults to `./bin`) and run the following command:

```shell
$ curl -sL https://raw.githubusercontent.com/unionai/uctl/main/install.sh | bash
```

**Manual download**

To download the binary manually, see the [`uctl` releases page](https://github.com/unionai/uctl/releases).

{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## Configuration

To create a configuration file with your Union connection information, run the following command, replacing
`<union-host-url>` with the URL of your Union instance:

```shell
$ uctl config init --host <union-host-url>
```

This creates a configuration file at `~/.union/config.yaml`. `uctl` searches for configuration files in the
following order:

* `--config <path-to-config>` flag
* `UNION_CONFIG` environment variable
* `UCTL_CONFIG` environment variable
* `~/.union/config.yaml` file
* `~/.uctl/config.yaml` file

## Commands

Run `uctl <command> --help` for the full flags and usage of any command below.

### Self-managed dataplane provisioning

* **`uctl selfserve provision-dataplane-resources`** — Provision dataplane resources for an existing Union
  organization. This is the current tool for self-managed dataplane onboarding; see the per-provider
  [self-managed deployment runbooks](../../deployment/selfmanaged/) for the full flow.

### Cluster configuration

Manage self-managed cluster configuration templates:

* **`uctl apply clusterconfig`** — Store a cluster configuration template in the organization.
* **`uctl get clusterconfig`** — Retrieve a cluster configuration template.
* **`uctl delete clusterconfig`** — Delete a cluster configuration template.

### Cluster node pools

* **`uctl get clusternodepool`** — List the node pools of a cluster.
* **`uctl delete clusternodepool`** — Delete a cluster node pool.

### Domains

Manage the domains of your organization:

* **`uctl create domain`** — Create a new domain within your organization.
* **`uctl get domain`** — Retrieve the domains of your organization.
* **`uctl update domain`** — Update a domain.
* **`uctl delete domain`** — Delete a domain.
