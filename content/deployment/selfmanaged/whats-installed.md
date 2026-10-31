---
title: What Union.ai installs in your cluster
description: What connecting your cluster installs, the permissions it runs with, and what it costs in your cloud account.
icon: box-seam
weight: 4
variants: -flyte +union
---

# What Union.ai installs in your cluster

When you [connect your cluster](./connect-a-cluster), two things are installed into it: the agent, which you install, and the data plane, which Union.ai installs through the agent. Everything runs in your cluster, in your cloud account.

## The agent

The install command you copy from the Union.ai UI installs the agent with Helm, as the release `dp-agent` in the `dataplane-agent` namespace. The agent connects out to Union.ai; nothing connects in to your cluster.

## The data plane

Once the agent connects, Union.ai installs Union.ai's `dataplane` Helm chart through it, into the namespace you entered when you registered the cluster, or `union` if you left it empty. The UI shows this phase as **Installing the Union operator**.

Union.ai sets the chart's values for your cluster's provider, and the agent manages the chart and its values. The table shows the values a newly connected cluster gets; a cluster connected earlier keeps the chart version and values it was installed with. It lists only the components those values set. Every other component, such as the executor, OpenCost, the DCGM exporter and serving, takes the chart's default, which this page does not cover:

| Component | AWS | GCP | Azure |
|---|---|---|---|
| Proxy, with secret management in your cloud's secret store | On | On | On |
| Image builder, running BuildKit in rootful mode | On | On | On |
| RBAC for Prometheus and kube-state-metrics | Created | Created | Created |
| metrics-server | On | Off: GKE runs its own | Off: AKS runs its own |
| Fluent Bit | Chart default | Off: GKE's own Fluent Bit ships the logs | Off |
| ingress-nginx | Off | Off | Off |

## Permissions

The data plane connected from the Union.ai UI runs in standard mode, so the chart creates cluster-wide ClusterRoles as well as Roles in its own namespace. Tasks still run only in the namespace you registered. See [Kubernetes access controls](./architecture/kubernetes-rbac) for the roles and what each can reach.

## What it costs

The resources the data plane runs on are in your own cloud account, and your cloud provider bills you for them whether or not any workload runs:

- **AWS.** [Provision your AWS resources](./aws/_index) lists the billable resources it creates.
- **GCP and Azure.** The provisioning pages for [GCP](./gcp/_index) and [Azure](./azure/_index) list the billable resources they create.

Union.ai's 30-day free trial covers Union.ai's own charges, not your cloud provider's. Your cloud costs apply from the moment you create the resources, during the trial too.
