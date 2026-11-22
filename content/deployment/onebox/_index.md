---
title: Self-hosted (single-cluster install)
description: Run Union.ai, its workflow services and UI, in your own Kubernetes cluster, installed with one Helm chart.
icon: box
weight: 4
variants: -flyte +union
---

# Self-hosted Union.ai

Self-hosted Union.ai runs **in your own Kubernetes cluster**: the services that store and run your workflows, and the web UI. You install it with one Helm chart, `onebox`, and connect it to a PostgreSQL database and an object storage bucket. Nothing runs in Union.ai's cloud. Use it to evaluate Union.ai on infrastructure you control, or for a team that wants everything in its own cluster.

## What runs

| Component | What it does |
|---|---|
| **onebox** | Runs your workflows: it stores runs, projects, users, and their permissions, launches each task as a pod, and serves the API that the SDK and CLI use. |
| **The UI** | The Union.ai web app, in the same pod as onebox and served by it at `/v2`. |
| **Node agent** | One per node: mounts [Union Volumes](../../user-guide/tasks/task-programming/volumes/_index) (shared, persistent storage for tasks) into task pods. |

Users, the SDK, and the CLI reach the UI, the API, and sign-in through one port, `80`; the other [ports](#ports) are for traffic inside the cluster. Task pods run in the namespace you install onebox into.

Some features need more components, which the chart can run for you: Knative Serving and a gateway for [apps](./apps), BuildKit and a registry for the [image builder](./image-builder), and Prometheus for [task metrics](./metrics). See [Add-ons](#add-ons).

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

| Requirement | Configuration |
|---|---|
| A PostgreSQL database, and a user that owns it | `database.host`, `database.name`, `database.user`, and the password in `database.existingSecret` |
| An object storage bucket | `storage.type`, `storage.bucket`, and the bucket's credentials |
| A license key | Added in the UI, or `license.existingSecret`; see [License key](#license-key) |

The bucket can be in Amazon S3, Google Cloud Storage (`storage.type: gcs`), Azure Blob Storage (`azure`), or an S3-compatible store such as MinIO, Cloudflare R2, or Ceph (`s3`). It needs a CORS rule for the UI; see [Bucket CORS](#bucket-cors).

Before you give anyone else access, put an authenticating proxy in front of onebox and turn on role-based access control; see [Authentication](./authentication) and [Authorization](./authorization).

Everything else has a working default. Onebox creates its tables on first start and upgrades them on every upgrade.

## Minimum requirements

| | Minimum |
|---|---|
| Kubernetes | 1.28 or later. On GKE, a Standard cluster: Autopilot isn't supported. |
| Cluster capacity | 4 CPUs and 8 GiB of memory to spare across the nodes that accept pods, for onebox, the UI, and a few task pods. Your tasks need room of their own beyond that. |
| Onebox | One pod, requesting 1 CPU and 2 GiB of memory (the chart's default). That runs 4,000 tasks at once and starts 128 runs a second; see [Sizing](#sizing). |
| PostgreSQL | A connection limit above `database.maxOpenConnections`, which is 40 by default. Beyond an evaluation, use a managed database such as Amazon RDS or Cloud SQL. |
| On your machine | Docker with 4 CPUs and 8 GB of memory, to [try Union.ai locally](./try-locally). |

`flyte install onebox --preflight-only` checks the Kubernetes version and the cluster's capacity, along with permissions and the database secret; see [Install with the CLI](./kubernetes#install-with-the-cli).

## Bucket CORS

The UI reads some objects straight from the bucket, through presigned URLs: a task's code in the Code tab, and downloads. The browser allows that only if the bucket sends CORS headers for the UI's origin, so give the bucket a CORS rule that allows `GET` and `HEAD` from `https://<host>`, the address your users open. Each guide shows how for its store. Without it, the Code tab shows "We're having trouble loading the code" and the browser's console reports `blocked by CORS policy`.

## Choose a guide

For a proof of concept, start with [Try Union.ai on your machine](./try-locally): one command, `flyte start onebox`, runs everything in one Docker container on your laptop, with nothing to set up first.

To install onebox on a Kubernetes cluster, `flyte install onebox` checks the cluster, asks for the database and bucket, and installs the chart; see [Install with the CLI](./kubernetes#install-with-the-cli). For each step by hand, use the guide for [Amazon EKS](./eks), [Google GKE](./gke), or [any other Kubernetes cluster](./kubernetes). Then decide who can reach it and what they can do: [Authentication](./authentication) and [Authorization](./authorization). [Install the chart on k3d](./local-k3d) runs the same chart in a local k3d cluster, for testing the chart itself.

{{< subpage-cards >}}

## Ports

| Service port | Who calls it |
|---|---|
| `80` | Users, the SDK, and the CLI: the UI, the API, and sign-in. Put your authenticating proxy in front of this port. |
| `8082` | Task pods, to start and track the tasks they call. In-cluster only. |
| `15606` | Task workers that [reuse a running container](../../user-guide/tasks/task-configuration/reusable-containers) across tasks. In-cluster only. |
| `9443` | The Kubernetes API server, calling onebox's webhook that adds secrets to task pods. |
| `8083` | With [apps](./apps) on: the apps gateway, asking onebox who may call an app. Only the gateway. |

## License key

A license key is what lets an installation make changes. Without a valid key, onebox is read-only: reads work, changes are refused, and runs in flight finish. Each installation needs its own key, issued for its 32-character install ID, which onebox generates on first start and keeps across upgrades.

### Get a key

1. In the onebox UI, open **Settings → License** and select **Get a key**. It opens Union.ai's sign-up with this installation's ID.
2. Sign in to your Union.ai organization, or sign up and create one. You land on the organization's **License Keys** page with this installation filled in. An administrator of your Union.ai organization issues the key there. Without a contract, it's a 30-day trial; an organization has one trial period, shared by all its installations. With a contract, the key lasts until the contract ends.
3. Back in the onebox UI, select **Add key** and paste it. With [authorization](./authorization) on, adding a key needs the installation's `admin` role. Read-only lifts right away.

You can also mount a key from a Secret:

```shell
kubectl -n union create secret generic onebox-license --from-literal=license-key=<key>
helm upgrade onebox unionai/onebox -n union -f values.yaml \
  --set license.existingSecret=onebox-license
```

Onebox picks up a rotated key in the Secret without a restart. Keys are verified offline, against Union.ai's public keys built into each release; nothing is sent to Union.ai. Only keys Union.ai issues are accepted.

To send **Get a key** to your own license-request page instead, set `license.issueURL`. Keys still have to come from Union.ai.

### Limits and entitlements

A key records your organization's limits and features when it is issued, such as the maximum number of users or concurrent runs. Onebox holds the installation to them. They can't be changed inside onebox: when your organization's limits change, issue the key again and add the new one.

By default, a request over a limit is logged and counted, not refused. To refuse it, set the limit's mode through the chart's `extraConfig`:

```yaml
extraConfig:
  quotaEnforcement:
    limits:
      max_users: enforce
```

## A private CA, extra mounts and proxies

`caBundle` names a ConfigMap (`caBundle.configMap`) or Secret (`caBundle.secret`) key holding a PEM bundle that onebox, the UI, and every task pod trust: for an S3 endpoint, database, identity provider, or registry signed by a private CA. It replaces the system trust store (`SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `AWS_CA_BUNDLE`, and others), so include the public roots if anything is reached over the internet:

```shell
cat /etc/ssl/certs/ca-certificates.crt corp-ca.pem > ca-bundle.pem
kubectl -n union create configmap ca-bundle --from-file=ca-bundle.pem
helm upgrade onebox unionai/onebox -n union -f values.yaml --set caBundle.configMap=ca-bundle
```

`extraVolumes` and `extraVolumeMounts` add volumes to the onebox container. Task pods get theirs from `taskPods.extraVolumes`, `taskPods.extraVolumeMounts`, and `taskPods.extraEnv`, for example an outbound proxy's `HTTPS_PROXY` and `NO_PROXY`, or a shared dataset. These task-pod settings, and `caBundle`, apply to every task, image builds included. A task's own `pod_template` applies on top of them.

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
| Apps and LLM gateways | Knative Serving and a gateway | `serving.enabled` | [Apps and LLM gateways](./apps) |

The Logs tab streams logs of running tasks without any add-on.

## Debug in VS Code

The **Debug** button reruns a task with a VS Code server in its pod, and **Open VS Code** opens it through onebox. It needs no add-on, but:

- Opening it needs permission to run in the project (the contributor role with authorization on), since the server runs code with the task's credentials.
- Your proxy must pass websockets through. oauth2-proxy and the AWS ALB do by default; so do most Gateway API implementations.
- The task needs memory for VS Code as well as its own work: a task limited to 256Mi is killed while VS Code starts. 2Gi is plenty.

## Sizing

Size onebox by how many runs you start a second: CPU runs out first. Memory stays within the container's limit, because onebox sets its Go memory limit to 90% of it. These numbers need Self-hosted Base 2026.11.14 or later.

Measured in November 2026 on AWS, with onebox as one replica (CPU and memory requests equal to limits), PostgreSQL 16, and short tasks. Every run succeeded:

| | 1 CPU, 2 GiB (the chart's default) | 2 CPUs, 4 GiB |
|---|---|---|
| Runs started a second, sustained | 128 with no errors. Accepted within 0.2 seconds at 32 a second, 0.5 seconds at 64, and 1.5 seconds at 128 (95th percentile) | 128 with no errors, accepted within 0.15 seconds (95th percentile) |
| Tasks running at once | 4,000 (as many as the test cluster held) | 4,000 (as many as the test cluster held) |
| What runs out first | CPU: onebox uses its full CPU from 64 runs a second | CPU: onebox nears its 2 CPUs at 128 runs a second |
| Onebox memory at its busiest | 1.8 GiB, with about 13,000 actions in flight | 3.3 GiB |
| PostgreSQL at its busiest | 0.4 CPUs, 1.2 GiB, about 230 connections | 0.65 CPUs, 1.1 GiB, about 190 connections |

Each task adds about 10 KB to the database.

Onebox runs at most 500 tasks at a time; the rest wait in the queue until one finishes. To run more at once, raise the limit to what your cluster can run:

```yaml
extraConfig:
  leaseworker:
    capacity: 4000
```

To accept runs quickly above about 32 a second, give onebox 2 CPUs. For thousands of tasks at once, also give it more database connections:

```yaml
resources:
  requests: {cpu: "2", memory: 4Gi}
  limits: {memory: 4Gi}
database:
  maxOpenConnections: 100
```

Give PostgreSQL 1 CPU and a connection limit of at least 300.

## Limitations

- Onebox runs as a single replica, without high availability.
- Tasks run only in the cluster onebox is installed in.
- The dashboards' queue panels show no data.

## License

Self-hosted Union.ai is under the [Union License](https://www.union.ai/licensing/union-license). The license is in the chart (`LICENSE`, with Union.ai's copyright in `NOTICE`). The onebox image has it in `/usr/share/doc/onebox/`, and the image `flyte start onebox` runs has it in `/onebox/licenses/`, beside the notices for the third-party software they include.
