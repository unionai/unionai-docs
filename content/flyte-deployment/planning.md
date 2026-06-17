---
title: Planning your deployment
variants: +flyte -union
weight: 1
---

# Planning your Flyte deployment

Before you install Flyte, it helps to understand what the deployment is made of and
which external dependencies you need to provide yourself.

## Architecture

Flyte runs as a **single unified binary**. One container image bundles all of the
backend components into one process:

| Component | Responsibility |
|---|---|
| Runs service | Accepts and stores run/task/workflow requests; owns the database. |
| Actions / task controller | Reconciles task executions onto Kubernetes. |
| Data proxy | Issues signed URLs for uploading and downloading data to the object store. |
| Secret service | Mediates access to Kubernetes secrets for tasks. |

A second image serves the web **console** as a static single-page application. It is
deployed as its own Deployment and Service but has no backend configuration of its
own — it talks to the Flyte API on the same origin (same ingress host) and is served
under a base path (default `/v2`, configurable via `console.basePath`).

Because everything is one process, you scale Flyte **vertically** — give the
Deployment more CPU and memory — rather than scaling individual microservices.

### Networking

Flyte clients (the SDK and CLI) speak [buf Connect](https://connectrpc.com/) **over
HTTP**, so a **single HTTP ingress** serves the console, the API, and the
auth-discovery endpoints — there is no separate gRPC port to expose. The single
ingress routes, by path, to two backends:

- `console.basePath` (default `/v2`, and `/v2/*`) → the console Service.
- the `flyteidl2.*` Connect service paths (for example
  `/flyteidl2.project.ProjectService`, `/flyteidl2.workflow.RunService`,
  `/flyteidl2.task.TaskService`, `/flyteidl2.dataproxy.DataProxyService`) and the
  auth-discovery paths (`/.well-known/oauth-authorization-server`,
  `/flyteidl2.auth.*`) → the Flyte binary's HTTP Service.

## External dependencies

The chart deploys the Flyte binary and console, but it does **not** provision the
infrastructure they depend on. Provision these before installing, regardless of cloud:

### Kubernetes cluster

Use a [supported Kubernetes version](https://kubernetes.io/releases/version-skew-policy/#supported-versions).
Flyte does not constrain the provider or how you stand the cluster up — managed
offerings (EKS, GKE, AKS), self-managed clusters, and on-prem all work.

### Relational database

Flyte stores its persistent records in **PostgreSQL** (12 or newer). The binary reads
a single database configuration, rendered by the chart under `runs.database` from your
`configuration.database` values. Provision a database and a user before installing;
the chart can create the database password Secret for you, or you can mount it from
your own secret manager.

### Object store

Flyte uses an object store to hold task inputs/outputs, metadata, and uploaded data.
The chart supports **S3, GCS, and Azure Blob Storage**. You need at least one bucket,
and the identity Flyte runs as needs these minimum permissions on it:

- `GetObject`
- `PutObject`
- `ListBucket`
- `DeleteObject`

You can use the same bucket for both metadata (`metadataContainer`) and user data
(`userDataContainer`).

## Optional dependencies

Flyte runs without these, but integrates with them when present.

### Ingress controller

To expose Flyte beyond `kubectl port-forward`, you need an ingress controller already
installed in the cluster (the chart creates the Ingress resource, but something has to
reconcile it). Commonly used controllers:

| Environment | Controller |
|---|---|
| AWS | AWS Load Balancer Controller (ALB) |
| GCP / Azure / on-prem | NGINX, Traefik |

### DNS

For anything beyond local testing, point a DNS record at your ingress host so clients
and the console reach Flyte at a stable address instead of `localhost`.

### SSL/TLS

Use a valid certificate to secure traffic between clients and Flyte. On AWS this is
typically an ACM certificate attached to the ALB; elsewhere it is a TLS Secret
referenced from the Ingress.

## Container images

The chart deploys two images, configurable under `deployment.image` and
`console.image`. You normally don't need to set these — the chart ships with working
defaults:

| Image | Default repository |
|---|---|
| Flyte binary | `cr.flyte.org/flyteorg/flyte-binary-v2` |
| Console | `ghcr.io/unionai-oss/flyteconsole-v2` |

When you're ready, continue to [Installing Flyte](./installing).
