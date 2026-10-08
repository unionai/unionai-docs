---
title: Onebox (single-pod install)
description: Run the whole Union.ai platform, control plane and data plane, as one pod in your own Kubernetes cluster, installed with one Helm chart.
icon: box
weight: 4
variants: -flyte +union
---

# Onebox

Onebox runs the whole Union.ai platform as **one pod in your own Kubernetes cluster**: the control plane, the data plane that launches your tasks, and the UI. You install it with one Helm chart and give it two things: a PostgreSQL database and an object store bucket. Use it to evaluate Union.ai on infrastructure you control, or for a team that wants a self-contained deployment with no external dependencies.

Unlike a [self-managed](../selfmanaged/_index) or [BYOC](../byoc/_index) deployment, nothing runs in Union.ai's cloud: the control plane is in the same pod as the data plane.

## What runs

| Container | What it does |
|---|---|
| `onebox` | The control plane (runs, actions, projects, identity, authorization), the data plane worker that creates task pods, and the pod admission webhook that injects secrets into them. |
| `console` | The Union.ai UI, served by onebox under `/v2`. |

Everything is served on **one port**: the UI, the API that the SDK and CLI use, and the REST routes. There is no ingress controller, Envoy, Redis, or ScyllaDB to install. Task pods run in the namespace you install onebox into.

## What you provide

| You provide | Chart values |
|---|---|
| A PostgreSQL database onebox can reach, and a user that owns it | `database.host`, `database.name`, `database.user`, and a password in `database.existingSecret` |
| A bucket in Amazon S3, Google Cloud Storage, or an S3-compatible store | `storage.type`, `storage.bucket`, and the credentials the bucket needs |
| Optionally, an authenticating proxy in front of onebox | `identity.*`; see [Authentication](./authentication) |
| Optionally, role-based access control | `authz.enabled`; see [Authorization](./authorization) |

Everything else has a working default. Onebox creates its tables on first start and upgrades them on every upgrade.

## Choose a guide

Start with [Try onebox on k3d](./local-k3d) on your laptop, or install it on [Amazon EKS](./eks), [Google GKE](./gke), or [any other Kubernetes cluster](./kubernetes). Then decide who can reach it and what they can do: [Authentication](./authentication) and [Authorization](./authorization).

{{< subpage-cards >}}

## Ports

| Service port | Who calls it |
|---|---|
| `80` | Users, the SDK, and the CLI: the UI, the API, and the REST routes. Put your authenticating proxy in front of this port. |
| `8082` | Task pods, calling back to launch and track child actions. In-cluster only. |
| `15606` | Workers of reusable containers. In-cluster only. |
| `9443` | The Kubernetes API server, calling the pod admission webhook. |

## Upgrade

```shell
helm upgrade onebox unionai/onebox -n union -f values.yaml
```

Onebox runs one replica and migrates the database on start, so an upgrade restarts it: the UI and API are unavailable until the new pod is ready.

## Uninstall

```shell
helm uninstall onebox -n union
kubectl delete mutatingwebhookconfiguration onebox
```

Onebox registers its pod admission webhook itself when it starts, so `helm uninstall` leaves the `MutatingWebhookConfiguration` behind. It is named after the release's Service (`onebox` for a release named `onebox`). Delete it, or pods created later in that namespace fail admission. The database and the bucket are yours and are left as they are.

## Add-ons

Three features need components you install beside onebox. Onebox starts without them and never waits for them:

| Feature | Needs | Page |
|---|---|---|
| Logs of finished tasks | A log shipper (fluent-bit) writing to the bucket | [Task logs](./logs) |
| The Metrics tab | Prometheus with cAdvisor and kube-state-metrics | [Task metrics](./metrics) |
| Building images in the cluster | BuildKit, a registry, and the build task | [Image builder](./image-builder) |

The Logs tab streams logs of running tasks without any add-on.

## Limitations

- One replica, and one data plane: the cluster onebox runs in.
- Apps and serving, artifacts, and the project and organization dashboards aren't included.
- Union Volumes aren't supported.
