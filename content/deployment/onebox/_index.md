---
title: Self-hosted (single-cluster install)
description: Run the whole Union.ai platform, control plane and data plane, in your own Kubernetes cluster, installed with one Helm chart.
icon: box
weight: 4
variants: -flyte +union
---

# Self-hosted Union.ai

Self-hosted Union.ai runs the whole platform **in your own Kubernetes cluster**: the control plane, the data plane that launches your tasks, and the UI, all from one `onebox` binary and the UI's image. You install it with one Helm chart, `onebox`, and give it two things: a PostgreSQL database and an object store bucket. Use it to evaluate Union.ai on infrastructure you control, or for a team that wants a self-contained deployment with no external dependencies.

Unlike a [self-managed](../selfmanaged/_index) or [BYOC](../byoc/_index) deployment, nothing runs in Union.ai's cloud: the control plane is in the same pod as the data plane.

## What runs

| Workload | Image | What it does |
|---|---|---|
| `onebox` Deployment, `onebox` container | `onebox-server` | The control plane (runs, actions, projects, identity, authorization), the data plane worker that creates task pods, and the pod admission webhook that injects secrets into them. |
| `onebox` Deployment, `console` container | `onebox-console` | The Union.ai UI, served by onebox under `/v2`. |
| `onebox-node-agent` DaemonSet | `onebox-server` | Runs on every node: the CSI driver (`volumes.union.ai`) that mounts Union Volumes into task pods, and the node-shared Volume cache. |

With [apps](./apps) on, the chart also runs Union's Kourier controller (from the `onebox-server` image) and its Envoy gateway (`envoy`).

Everything is served on **one port**: the UI, the API that the SDK and CLI use, and the REST routes. There is no ingress controller, Redis, or ScyllaDB to install. Task pods run in the namespace you install onebox into.

## Images

The chart pulls three public images from GitHub's container registry, tagged with the chart's `appVersion`. Each Union.ai release publishes them for amd64 and arm64:

| Image | Chart value |
|---|---|
| `ghcr.io/unionai/onebox-server` | `image.repository` |
| `ghcr.io/unionai/onebox-console` | `console.image.repository` |
| `ghcr.io/unionai/envoy` (only with apps on) | `serving.gateway.envoy.image.repository` |

For an airgapped install or a private mirror, copy each image with all its architectures, point these values at your copies, and add the mirror's pull secret to `imagePullSecrets` if it needs one.

## What you provide

| You provide | Chart values |
|---|---|
| A PostgreSQL database onebox can reach, and a user that owns it | `database.host`, `database.name`, `database.user`, and a password in `database.existingSecret` |
| A bucket in Amazon S3, Google Cloud Storage, or an S3-compatible store, with a CORS rule for the UI | `storage.type`, `storage.bucket`, and the credentials the bucket needs; see [Bucket CORS](#bucket-cors) |
| Optionally, an authenticating proxy in front of onebox | `identity.*`; see [Authentication](./authentication) |
| Optionally, role-based access control | `authz.enabled`; see [Authorization](./authorization) |

Everything else has a working default. Onebox creates its tables on first start and upgrades them on every upgrade.

## Bucket CORS

The UI reads some objects straight from the bucket, through presigned URLs: a task's code in the Code tab, and downloads. The browser allows that only if the bucket sends CORS headers for the UI's origin, so give the bucket a CORS rule that allows `GET` and `HEAD` from `https://<host>`, the address your users open. Each guide shows how for its store. Without it, the Code tab shows "We're having trouble loading the code" and the browser's console reports `blocked by CORS policy`.

## Choose a guide

For a proof of concept, start with [Try Union.ai on your machine](./try-locally): one command, `flyte start onebox`, runs everything in one Docker container on your laptop, with nothing to set up first.

To install onebox on a Kubernetes cluster, use the guide for [Amazon EKS](./eks), [Google GKE](./gke), or [any other Kubernetes cluster](./kubernetes). Then decide who can reach it and what they can do: [Authentication](./authentication) and [Authorization](./authorization). [Install the chart on k3d](./local-k3d) runs the same chart in a local k3d cluster, for testing the chart itself.

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

Four features need components you install beside onebox. Onebox starts without them and never waits for them:

| Feature | Needs | Page |
|---|---|---|
| Logs of finished tasks | A log shipper (fluent-bit) writing to the bucket | [Task logs](./logs) |
| The Metrics tab | Prometheus with cAdvisor and kube-state-metrics | [Task metrics](./metrics) |
| Building images in the cluster | BuildKit and a registry | [Image builder](./image-builder) |
| Apps and LLM gateways | Knative Serving with Kourier | [Apps and LLM gateways](./apps) |

The Logs tab streams logs of running tasks without any add-on.

## Debug in VS Code

The **Debug** button reruns a task with a VS Code server in its pod, and **Open VS Code** opens it through onebox. It needs no add-on, but:

- Opening it needs permission to run in the project (the contributor role with authorization on), since the server runs code with the task's credentials.
- Your proxy must pass websockets through. oauth2-proxy and the AWS ALB do by default; so do most Gateway API implementations.
- The task needs memory for VS Code as well as its own work: a task limited to 256Mi is killed while VS Code starts. 2Gi is plenty.

## Limitations

- One replica, and one data plane: the cluster onebox runs in.
- Apps and serving, and artifacts aren't included.
- The dashboards' queue panels show no data.
- Union Volumes aren't supported.

## License

Self-hosted Union.ai is under the [Union License](https://www.union.ai/licensing/union-license). The license is in the chart (`LICENSE`, with Union.ai's copyright in `NOTICE`). The onebox image has it in `/usr/share/doc/onebox/`, and the image `flyte start onebox` runs has it in `/onebox/licenses/`, beside the notices for the third-party software they include.
