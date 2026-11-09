---
title: What Union.ai installs in your cluster
description: The cloud resources and in-cluster services a self-managed data plane runs on, the permissions they hold, and what they cost while idle.
icon: box-seam
weight: 4
variants: -flyte +union
---

# What Union.ai installs in your cluster

Union.ai runs your tasks in your own cloud account. Your code, data, logs and container images stay there. Union.ai's control plane stores run metadata and pointers to your data, not the data itself.

To make this work, setup puts resources in two places: cloud resources you create when you [provision your cloud resources](./_index#aws-gcp-and-azure-set-up-from-the-unionai-ui), and services Union.ai installs in your Kubernetes cluster when you [connect your cluster](./connect-a-cluster). Union.ai's services run all the time, so your cloud bill includes a fixed amount even when no tasks run: on AWS, about **$400–450 per month** at on-demand prices. See [What it costs when nothing is running](#what-it-costs-when-nothing-is-running).

## Cloud resources you create

| Resource | Examples | What Union.ai uses it for |
|---|---|---|
| Kubernetes cluster | EKS, GKE or AKS | Runs Union.ai's services and your tasks. Nodes are added when tasks need them and removed when idle. |
| Object store bucket | S3, GCS or Azure Blob Storage | Stores task inputs, outputs, artifacts, code bundles and logs. |
| Container registry | ECR, Artifact Registry or ACR | Stores the images Union.ai builds for your tasks. |
| Workload identity | IAM roles, GCP service accounts or Azure managed identities | Gives Union.ai's services and your tasks access to the bucket, registry and secrets, with no long-lived keys. |
| Secret store | Secrets Manager, Secret Manager or Key Vault | Holds your task secrets and the key Union.ai's services use to authenticate. |

The provisioning page for [AWS](./aws/_index), [GCP](./gcp/_index) or [Azure](./azure/_index) creates these and lists the billable resources among them.

## Services Union.ai installs

The install command you copy from the Union.ai UI installs the agent with Helm, as the release `dp-agent` in the `dataplane-agent` namespace, together with two monitoring agents in the `monitoring-endpoints` namespace. The agent connects out to Union.ai, then installs Union.ai's `dataplane` Helm chart into the namespace you entered when you registered the cluster, or `union` if you left it empty. Nothing connects in to your cluster: you don't open ports or share cluster credentials.

The table lists what the agent installs on AWS, with the CPU and memory each service requests:

| Service | What it does | Requested CPU / memory |
|---|---|---|
| Deployment agent and monitoring agents | Install and update Union.ai's services and report install health | 400m / 256 MiB |
| Union.ai operator | Connects your cluster to Union.ai's control plane | 150m / 384 MiB |
| Operator proxy | Gives your browser and the Union.ai UI secure access to data plane resources and apps | 1 vCPU / 1000 MiB |
| Data proxy | Lets the Union.ai UI read your data directly from your object store | 250m / 250 MiB |
| Leaseworker | Runs your tasks as pods | 300m / 512 MiB |
| Pod webhook | Adds Union.ai-specific information to task pods | 200m / 500 MiB |
| Connector service | Runs tasks that call external services such as data warehouses and APIs | 200m / 768 MiB |
| Image builder | Builds task images and pushes them to your registry | 200m / 4 GiB |
| Prometheus and Metrics Server | Collect the metrics behind run dashboards and resource usage views | 1.1 vCPU / 1.2 GiB |
| Fluent Bit (one per node) | Sends task logs to long-term storage | None set |
| Volume mount broker (one per node) | Mounts Union.ai Volumes into tasks | 30m / 32 MiB per node |
| App serving (Knative Serving, Kourier, Envoy) | Runs the apps you deploy and scales them to zero when idle | 2.8 vCPU / 3.8 GiB |
| **Total** | | **About 6.7 vCPU / 12.7 GiB** |

On GCP and Azure, the data plane doesn't install Metrics Server, because GKE and AKS run their own, and doesn't install Fluent Bit.

Requested resources are what Kubernetes reserves for each service. At idle the services use far less, about 0.1 vCPU and 2 GiB in total, but your nodes are sized to the requests, so the requests set your bill.

The figures were measured on an idle AWS cluster connected in October 2026, with data plane chart 2026.10.1. A cluster connected earlier keeps the chart version it was installed with, so its services can differ.

## Permissions

A data plane connected from the Union.ai UI runs in standard mode. The chart creates cluster-wide ClusterRoles as well as Roles in its own namespace, so some of Union.ai's permissions span the whole cluster. Your tasks still run only in the namespace you registered. [Kubernetes access controls](./kubernetes-rbac) lists the roles and what each can reach.

Two services run privileged pods: the image builder, which runs BuildKit in rootful mode, and the volume mount broker.

## What it costs when nothing is running

Union.ai's services run all the time, so your cloud bill includes a fixed amount even when no tasks run. On AWS, an idle cluster costs about **$400–450 per month** at on-demand prices:

| Cost | About ($/month) |
|---|---|
| Nodes for Union.ai's services (4 small nodes) | 230–275 |
| EKS cluster fee and EKS Auto Mode fee | 108 |
| NAT gateway, node disks and data transfer | 61 |
| Public IP, Secrets Manager and S3 | 4 |

These figures assume us-east-2, on-demand prices, EKS Auto Mode, the default settings with app serving on, and no tasks running. Your cost depends on your region, your discounts, and how your cloud packs nodes. GCP and Azure have not been measured yet.

**Not included:**

- Compute for your tasks, which is added when tasks run and removed when they finish.
- Storage, which grows with your data.
- Union.ai's subscription fee, which is billed separately. The 30-day free trial covers Union.ai's fee, not your cloud provider's: your cloud costs apply from the moment you create the resources, during the trial too.

## Lower your baseline

Cover the always-on nodes with your cloud's commitment discount, such as AWS Savings Plans, GCP committed use discounts, or Azure reservations.

Union.ai is continually working to make this baseline cheaper and to reduce the resources its services need.

## See it yourself

```shell
kubectl get pods -n dataplane-agent
kubectl get pods -n union
kubectl top pods -n union
```

If you entered a different namespace when you registered the cluster, replace `union` with it.
