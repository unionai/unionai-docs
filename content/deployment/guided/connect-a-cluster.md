---
title: Connect your own cluster
description: Point Union at a Kubernetes cluster you own, so your workloads run on your infrastructure instead of your machine.
icon: hdd-network
weight: 1
variants: -flyte +union
---

# Connect your own cluster

You have an organization. Now give {{< key product_name >}} a Kubernetes cluster to run workloads on. Your code, data and credentials stay in that cluster.

**Nothing dials in.** You install an agent into your cluster, and the agent connects out to {{< key product_name >}}. You do not open a port, expose an endpoint, or hand over cluster credentials.

> [!NOTE] This is not the same as a self-managed deployment
> On this path you register the cluster first, and the agent then installs the data plane for you. The [Self-managed deployment](../selfmanaged/_index) guides describe the opposite order: you provision and install the data plane yourself, then register the control-plane record. Follow one or the other, not both.

## What you'll need

- A Kubernetes cluster you can reach with `kubectl`.
- An S3-compatible object store that the cluster can reach, and its access key and secret.
- Optionally, a container registry the cluster can push to and pull from.

All of this works on a local cluster. See [Trying it on a local cluster](#trying-it-on-a-local-cluster).

## 1. Set up a cluster pool

A cluster pool groups clusters that share an object store, secrets and an image registry. Your first cluster needs one, and a new organization starts without any, so the console asks for this first.

Select your provider, then fill in the store the cluster will use:

| Field | What it is |
|-------|------------|
| **Object store** | The S3-compatible bucket, and optional prefix, {{< key product_name >}} stores metadata in. For example, `s3://union-data`. |
| **Object store endpoint** | Where the S3-compatible API is reached **from inside the cluster**. Plain `http://` is fine for a store running in the cluster. |
| **Image registry** | Optional. The registry images are pushed to and pulled from. |

The endpoint is resolved by the agent from inside your cluster, not by {{< key product_name >}}, so an address that only exists on your cluster network is expected here.

<!-- screenshot: cluster-pool form, On-Prem tab, fields filled. Frame the object-store endpoint field + its helper text, since "from inside the cluster" is the non-obvious part. Staging-safe: no region list or domain suffix on this screen. -->

Select **Create cluster pool**. The console then takes you to **Clusters**, ready to connect one.

## 2. Create the storage secret

Your object store's keys stay in your cluster. {{< key product_name >}} is only told the *name* of the Kubernetes secret that holds them.

Create the namespace and the secret:

```bash
kubectl create namespace union --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic storage-credentials \
  --namespace union \
  --from-literal=access_key_id=<your-access-key> \
  --from-literal=secret_key=<your-secret-key>
```

You can do this before or straight after registering the cluster. The agent reads it when it connects.

## 3. Register the cluster

Select **New Cluster** and fill in three things:

| Field | Notes |
|-------|-------|
| **Cluster name** | The name the cluster is registered under. It **cannot be changed** once the cluster is connected. |
| **Cluster pool** | The pool from step 1. It supplies the object store the cluster deploys with. |
| **Credentials secret name** | The name of the secret you created in step 2, for example `storage-credentials`. |

<!-- screenshot: "Connect your cluster" dialog with the three fields filled. Frame the whole dialog; the "Nothing dials in" line in the subhead is worth showing. -->

Select **Register cluster**. The cluster now exists as a record, and the console moves on to installing the agent.

Registering does not put anything on your cluster by itself. That is the next step.

## 4. Install the agent

<!-- ⚠️ NOT YET REACHABLE. The console shows "Preparing the install command…" and never resolves it.
     Blocked on ENG26-1184 "Register new clusters and return Helm install secret" (Jeev, Todo,
     not started) — the backend does not yet mint the install secret the command needs.
     Verified stuck on staging 2026-09-04 against org docs-coldrun-0903, cluster kind-local.
     DO NOT PUBLISH THIS SECTION until the command has been run end to end and captured. -->

The console shows a command to run against the cluster you want {{< key product_name >}} to use. Run it, and the agent installs itself and connects out.

<!-- placeholder: the exact install command goes here, verbatim from the console, once ENG26-1184
     lands. Do not reconstruct it from the signup app's /connect page — that is the older
     self-managed helm path (`helm upgrade --install unionai-dataplane charts/dataplane …`) and
     may not be what this dialog emits. Capture it, do not infer it. -->

## 5. Wait for the data plane

Installation runs in two phases, both shown in the console:

| Phase | What is happening |
|-------|-------------------|
| **Agent installation** | The agent starts in your cluster and connects out to {{< key product_name >}}. |
| **Union installation** | {{< key product_name >}} installs the data plane through that connection. |

Alongside them the console reports **connectivity** and **health** for the cluster.

Installing the data plane takes a few minutes on a new cluster, mostly spent pulling images. You can leave the page while it runs.

<!-- screenshot: the Status panel mid-install, showing both phases and connectivity. Partially
     capturable today — the panel appears on registration and shows "Agent installation:
     installing…" with "connectivity: disconnected" — but it never progresses without step 4,
     so a *successful* shot needs ENG26-1184. -->

## 6. Run a workload on the cluster

<!-- ⚠️ UNVERIFIED. Plausible from the run-mode model but never observed, because step 4 blocks.
     Confirm the exact command and what the reader sees before publishing. -->

With a connected cluster, drop `--local` and the same code runs on-cluster instead of in your Python process:

```bash
flyte run temperatures.py hottest
```

The run appears under **Runs** in your project, not under **Tracked Runs** — that section is for runs that execute on your own machine. See [Run modes](../../user-guide/get-started/run-modes/_index) for how the two differ.

## Trying it on a local cluster

You do not need cloud infrastructure to see this working. A local Kubernetes cluster and an in-cluster object store are enough, and the endpoint field is designed for exactly this.

Create a cluster with [kind](https://kind.sigs.k8s.io):

```bash
kind create cluster --name union-local
```

Deploy MinIO into it and create a bucket. Putting MinIO in a namespace called `minio` gives it the in-cluster address `http://minio.minio.svc.cluster.local:9000`, which is what you enter as the object store endpoint:

<!-- code include: the MinIO manifest belongs in unionai-examples once this page is unblocked,
     rather than being pasted inline here. Verified working: namespace + Deployment + Service,
     quay.io/minio/minio, emptyDir storage, root user/password via a Secret. -->

Then follow the steps above, using:

| Field | Value |
|-------|-------|
| Object store | `s3://union-data` |
| Object store endpoint | `http://minio.minio.svc.cluster.local:9000` |
| Image registry | leave blank |

> [!WARNING] For evaluation only
> A local cluster has no persistent storage, no capacity to speak of, and disappears when you delete it. Use it to understand the flow, not to run real work.

## Next steps

- **[Cluster pools](../../user-guide/cluster-workload-management/cluster-pools)** — managing pools from the CLI, including multiple pools.
- **[Clusters](../../user-guide/cluster-workload-management/clusters)** — inspecting cluster state and capacity, and moving a cluster between pools.
- **[Queues](../../user-guide/cluster-workload-management/queues)** — routing workloads across your clusters.
