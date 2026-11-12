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

With [apps](./apps) on, the chart also runs Knative Serving, Union's Kourier controller (from the `onebox-server` image), and its Envoy gateway (`envoy`). It can also run BuildKit and a registry for the [image builder](./image-builder), and Prometheus for [task metrics](./metrics).

Everything is served on **one port**: the UI, the API that the SDK and CLI use, and the REST routes. There is no ingress controller, Redis, or ScyllaDB to install. Task pods run in the namespace you install onebox into.

## Images

The chart pulls three public images from GitHub's container registry, tagged with the chart's `appVersion`. Each Union.ai release publishes them for amd64 and arm64:

| Image | Chart value |
|---|---|
| `ghcr.io/unionai/onebox-server` | `image.repository` |
| `ghcr.io/unionai/onebox-console` | `console.image.repository` |
| `ghcr.io/unionai/envoy` (only with apps on) | `serving.gateway.envoy.image.repository` |

With the [image builder](./image-builder), task pods also pull `ghcr.io/unionai/imagebuilder/build-image` and `frontend-v2`. [`flyte start onebox`](./try-locally) runs a different image, `ghcr.io/unionai/onebox-local`, with the server and UI images preloaded; its add-ons and image builds pull the rest when they need them.

For an airgapped install or a private mirror, copy each image with all its architectures, point these values at your copies, and add the mirror's pull secret to `imagePullSecrets` if it needs one.

## What you provide

| You provide | Chart values |
|---|---|
| A PostgreSQL database onebox can reach, and a user that owns it | `database.host`, `database.name`, `database.user`, and a password in `database.existingSecret` |
| A bucket in Amazon S3, Google Cloud Storage, Azure Blob Storage, or an S3-compatible store (MinIO, R2, Ceph), with a CORS rule for the UI | `storage.type` (`s3`, `gcs`, or `azure`), `storage.bucket`, and the credentials the bucket needs; see [Bucket CORS](#bucket-cors) |
| Optionally, an authenticating proxy in front of onebox | `identity.*`; see [Authentication](./authentication) |
| Optionally, role-based access control | `authz.enabled`; see [Authorization](./authorization) |
| A license key: a 30-day trial or a contract key, from your Union.ai organization | Added in the UI, or `license.existingSecret`; see [License key](#license-key) |

Everything else has a working default. Onebox creates its tables on first start and upgrades them on every upgrade.

The cluster needs Kubernetes 1.28 or later, and nodes with at least 4 CPUs and 8 GiB of memory to spare for onebox, the UI, and a few task pods. `flyte install onebox --preflight-only` checks these, along with permissions and the database secret; see [Install with the CLI](./kubernetes#install-with-the-cli).

## Bucket CORS

The UI reads some objects straight from the bucket, through presigned URLs: a task's code in the Code tab, and downloads. The browser allows that only if the bucket sends CORS headers for the UI's origin, so give the bucket a CORS rule that allows `GET` and `HEAD` from `https://<host>`, the address your users open. Each guide shows how for its store. Without it, the Code tab shows "We're having trouble loading the code" and the browser's console reports `blocked by CORS policy`.

## Choose a guide

For a proof of concept, start with [Try Union.ai on your machine](./try-locally): one command, `flyte start onebox`, runs everything in one Docker container on your laptop, with nothing to set up first.

To install onebox on a Kubernetes cluster, `flyte install onebox` checks the cluster, asks for the database and bucket, and installs the chart; see [Install with the CLI](./kubernetes#install-with-the-cli). For each step by hand, use the guide for [Amazon EKS](./eks), [Google GKE](./gke), or [any other Kubernetes cluster](./kubernetes). Then decide who can reach it and what they can do: [Authentication](./authentication) and [Authorization](./authorization). [Install the chart on k3d](./local-k3d) runs the same chart in a local k3d cluster, for testing the chart itself.

{{< subpage-cards >}}

## Ports

| Service port | Who calls it |
|---|---|
| `80` | Users, the SDK, and the CLI: the UI, the API, and the REST routes. Put your authenticating proxy in front of this port. |
| `8082` | Task pods, calling back to launch and track child actions. In-cluster only. |
| `15606` | Workers of reusable containers. In-cluster only. |
| `9443` | The Kubernetes API server, calling the pod admission webhook. |
| `8083` | With [apps](./apps) on: the apps gateway, asking onebox who may call an app. Only the gateway. |

## License key

A license key is what lets an install make changes. Without a valid key, onebox is read-only: reads work, changes are refused, and runs in flight finish. Every key is for one install, named by the 32-character install ID onebox generates on first start and keeps across upgrades.

### Get a key

1. In the onebox UI, open **Settings > License** and select **Get a key**. It shows the install ID and links to `license.issueURL` with it, by default Union.ai's sign-up.
2. Sign in to your Union.ai organization, or sign up and create one. You land on the organization's **License Keys** page with the issue dialog open for this install. An account admin issues the key there. Without a contract it's a 30-day trial, one per organization and shared by all its installs. With a contract, the key lasts until the contract ends.
3. Back in onebox, select **Add key** and paste it. An account admin adds keys when [authorization](./authorization) is on. Read-only lifts right away.

You can also mount a key from a Secret:

```shell
kubectl -n union create secret generic onebox-license --from-literal=license-key=<key>
helm upgrade onebox unionai/onebox -n union -f values.yaml \
  --set license.existingSecret=onebox-license
```

Onebox picks up a rotated key in the Secret without a restart. Keys are verified offline, against Union.ai's public keys built into each release; nothing is sent to Union.ai. Only keys Union.ai issues are accepted. `license.issueURL` points **Get a key** somewhere else.

### Limits and entitlements

A key carries the limits and entitlements of the organization it was issued for, such as the maximum number of clusters, users, or concurrent runs, as they were when it was issued. Onebox reports them as the organization's own, and its limit checks hold the install to them. A key issued before keys carried limits, or no key at all, gets the Teams tier's defaults built into the release. The limits can't be changed inside onebox: when the organization's limits change, issue the key again and add the new one.

The checks start in log-only mode: a request over a limit is logged and counted, not refused. To enforce a limit, set its mode in onebox's configuration through the chart's `extraConfig`:

```yaml
extraConfig:
  quotaEnforcement:
    limits:
      max_clusters: enforce
```

## A private CA, extra mounts and proxies

`caBundle` names a ConfigMap (`caBundle.configMap`) or Secret (`caBundle.secret`) key holding a PEM bundle that onebox, the UI, and every task pod trust: for an S3 endpoint, database, identity provider, or registry signed by a private CA. It replaces the system trust store (`SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `AWS_CA_BUNDLE`, and others), so include the public roots if anything is reached over the internet:

```shell
cat /etc/ssl/certs/ca-certificates.crt corp-ca.pem > ca-bundle.pem
kubectl -n union create configmap ca-bundle --from-file=ca-bundle.pem
helm upgrade onebox unionai/onebox -n union -f values.yaml --set caBundle.configMap=ca-bundle
```

`extraVolumes` and `extraVolumeMounts` add volumes to the onebox container. Task pods get theirs from `taskPods.extraVolumes`, `taskPods.extraVolumeMounts`, and `taskPods.extraEnv`, for example an outbound proxy's `HTTPS_PROXY` and `NO_PROXY`, or a shared dataset. Whenever any of these, or `caBundle`, is set, the chart renders a PodTemplate that every task pod starts from, the `build-image` task included. A task's own `pod_template` still applies on top.

## Upgrade

```shell
helm upgrade onebox unionai/onebox -n union -f values.yaml
```

Onebox runs one replica and migrates the database on start, so an upgrade restarts it: the UI and API are unavailable until the new pod is ready.

## Uninstall

```shell
helm uninstall onebox -n union
```

The chart installs the pod admission webhook's `MutatingWebhookConfiguration` and its serving certificate, so `helm uninstall` removes them. What onebox created while running, such as task pods, apps, and secrets, stays until you delete the namespace. Helm never deletes the Knative CRDs the chart installed. The database and the bucket are yours and are left as they are.

## Add-ons

Four features need components beside onebox. The chart can run three of them for you; onebox starts without any of them and never waits for them:

| Feature | Needs | Chart value | Page |
|---|---|---|---|
| Logs of finished tasks | A log shipper (fluent-bit) writing to the bucket | None: you install it | [Task logs](./logs) |
| The Metrics tab | Prometheus with cAdvisor and kube-state-metrics | `prometheus.enabled`, or your own in `metrics.prometheusURL` | [Task metrics](./metrics) |
| Building images in the cluster | BuildKit and a registry | `imageBuilder.bundled.enabled` (evaluation only), or your own | [Image builder](./image-builder) |
| Apps and LLM gateways | Knative Serving with Kourier | `serving.enabled` | [Apps and LLM gateways](./apps) |

The Logs tab streams logs of running tasks without any add-on.

## Debug in VS Code

The **Debug** button reruns a task with a VS Code server in its pod, and **Open VS Code** opens it through onebox. It needs no add-on, but:

- Opening it needs permission to run in the project (the contributor role with authorization on), since the server runs code with the task's credentials.
- Your proxy must pass websockets through. oauth2-proxy and the AWS ALB do by default; so do most Gateway API implementations.
- The task needs memory for VS Code as well as its own work: a task limited to 256Mi is killed while VS Code starts. 2Gi is plenty.

## Limitations

- One replica, and one data plane: the cluster onebox runs in.
- The dashboards' queue panels show no data.

## License

Self-hosted Union.ai is under the [Union License](https://www.union.ai/licensing/union-license). The license is in the chart (`LICENSE`, with Union.ai's copyright in `NOTICE`). The onebox image has it in `/usr/share/doc/onebox/`, and the image `flyte start onebox` runs has it in `/onebox/licenses/`, beside the notices for the third-party software they include.
