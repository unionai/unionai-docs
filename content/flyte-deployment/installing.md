---
title: Installing Flyte
variants: +flyte -union
weight: 2
---

# Installing Flyte

This guide installs Flyte with the `flyte-binary` Helm chart. It assumes you have
already provisioned the [external dependencies](./planning) — a Kubernetes cluster, a
PostgreSQL database, and an object-store bucket — and that you have `helm` and
`kubectl` configured against your cluster.

## 1. Add the Helm repository

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm repo update
```

The `helm install` commands below reference the chart as `flyteorg/flyte-binary`.

## 2. Write a values file

Create a `values.yaml` with the minimum configuration. Everything in angle brackets is
a placeholder you replace:

```yaml
# values.yaml — minimal Flyte configuration

# fullnameOverride names all resources (here: flyte, flyte-http, flyte-console).
# Give each release a distinct name if you run more than one Flyte instance.
fullnameOverride: flyte

configuration:
  database:
    postgres:
      host: <postgres-host>            # e.g. my-db.example.com
      port: 5432
      dbname: flyte                    # database must already exist
      username: flyte
      # Setting password here makes the chart create a Secret and mount it.
      # Leave empty and use passwordPath to mount your own secret instead.
      password: <db-password>
      options: "sslmode=require"       # use sslmode=disable only for local/dev
  storage:
    metadataContainer: <bucket-name>   # bucket for Flyte metadata
    userDataContainer: <bucket-name>   # bucket for task I/O (can be the same bucket)
    provider: s3                       # s3 | gcs | azure
    providerConfig:
      s3:
        region: <region>               # e.g. us-east-1
        authType: iam                  # iam (recommended) | accesskey

serviceAccount:
  create: true
  # Bind a cloud IAM identity here so Flyte can reach the object store. See step 4.
  annotations: {}
```

The required fields:

| Setting | Key | Notes |
|---|---|---|
| Database host | `configuration.database.postgres.host` | Reachable from the cluster. |
| Database name | `configuration.database.postgres.dbname` | Must already exist. |
| Database user | `configuration.database.postgres.username` | Default `postgres`. |
| Database password | `configuration.database.postgres.password` | Creates and mounts a Secret. Use `passwordPath` instead to mount your own. The two are mutually exclusive. |
| Metadata bucket | `configuration.storage.metadataContainer` | Object-store bucket for metadata. |
| User-data bucket | `configuration.storage.userDataContainer` | Bucket for task inputs/outputs; can equal the metadata bucket. |
| Storage provider | `configuration.storage.provider` | `s3`, `gcs`, or `azure`. |
| Storage region | `configuration.storage.providerConfig.s3.region` | S3 region (S3 provider). |
| Service account | `serviceAccount.annotations` | Cloud IAM binding for object-store access (step 4). |

## 3. Install

Render the manifests first to check your values, then install for real:

```bash
# Dry run — renders templates without touching the cluster
helm install flyte flyteorg/flyte-binary -n flyte --create-namespace -f values.yaml --dry-run

# Install
helm install flyte flyteorg/flyte-binary -n flyte --create-namespace -f values.yaml
```

Watch the rollout:

```bash
kubectl -n flyte rollout status deploy/flyte
kubectl -n flyte get pods
```

A `wait-for-db` init container blocks startup until the database is reachable, so a
pod stuck in `Init` usually means the database host, credentials, or network policy
are wrong.

## 4. Grant object-store access

The Flyte pod and the task pods it launches need credentials to read and write the
bucket. Prefer cloud-native workload identity over static keys.

**AWS (IRSA).** Annotate the service account with an IAM role that has access to the
bucket:

```yaml
serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<flyte-role>
```

**GCP (Workload Identity).** Annotate with the Google service account, and keep
`provider: gcs` with `providerConfig.gcs.project: <project-id>`:

```yaml
serviceAccount:
  create: true
  annotations:
    iam.gke.io/gcp-service-account: <gsa-name>@<project-id>.iam.gserviceaccount.com
```

**Static access keys (S3-compatible / MinIO, not recommended for production).**

```yaml
configuration:
  storage:
    providerConfig:
      s3:
        authType: accesskey
        accessKey: <access-key>
        secretKey: <secret-key>
        endpoint: <https://minio.example.com>   # for non-AWS S3-compatible stores
        disableSSL: false
        v2Signing: false                          # set true for some MinIO setups
```

**Task pods.** Tasks run in their own pods, which need the same object-store access.
Run them under a service account that carries the IAM binding by setting it in the
executor config (merged via `configuration.inline`):

```yaml
configuration:
  inline:
    executor:
      defaultK8sServiceAccount: flyte   # IAM-annotated SA tasks run as
```

## 5. Expose Flyte with an ingress

By default the chart only creates `ClusterIP` Services. To reach Flyte from outside
the cluster, enable the ingress. A **single HTTP ingress** serves the console, the
API, and the auth-discovery endpoints — there is no separate gRPC ingress (see
[Planning](./planning)).

```yaml
ingress:
  create: true
  host: <flyte.example.com>
  # Your cloud's native ingress class, e.g. alb (EKS), gce (GKE),
  # azure-application-gateway (AKS). See Planning for the options.
  ingressClassName: <ingress-class>
```

The console is served under `console.basePath` (default `/v2`) on this same host. It
talks to the API same-origin, so it only works when the console and the API are behind
the **same ingress host** — always expose them together.

For provider-specific ingress annotations (TLS, ALB scheme, health checks), add them
under `ingress.httpAnnotations`. See the AWS/EKS example below and the
[Authentication and SSO](./authentication) page.

## 6. Verify the installation

**Without an ingress**, port-forward the API service and call a Connect endpoint:

```bash
kubectl -n flyte port-forward service/flyte-http 8090:8090
```

```bash
# In another terminal — list projects over the Connect (HTTP) API:
curl -s -X POST \
  http://localhost:8090/flyteidl2.project.ProjectService/ListProjects \
  -H 'Content-Type: application/json' -d '{}'
```

A JSON response (rather than a connection error) confirms the binary is up and talking
to its database.

**With an ingress**, open `https://<flyte.example.com>/v2` in a browser to load the
console, and point the SDK/CLI at the same host.

## AWS/EKS worked example

A fuller values file for an EKS cluster using RDS for PostgreSQL, S3 for storage, IRSA
for credentials, and an ALB ingress. Replace every placeholder; no real account IDs,
hostnames, or ARNs are included.

```yaml
# values-eks.yaml
fullnameOverride: flyte

configuration:
  database:
    postgres:
      host: <flyte-db>.<id>.<region>.rds.amazonaws.com
      port: 5432
      dbname: flyte
      username: flyte
      password: <db-password>
      options: "sslmode=require"
  storage:
    metadataContainer: <flyte-bucket>
    userDataContainer: <flyte-bucket>
    provider: s3
    providerConfig:
      s3:
        region: <region>
        authType: iam
  # Optional overrides merged into the rendered config.
  inline:
    executor:
      # Task pods run as this service account so they inherit S3 access via IRSA.
      defaultK8sServiceAccount: flyte

serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<flyte-role>

ingress:
  create: true
  host: <flyte.example.com>
  httpAnnotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS": 443}]'
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account-id>:certificate/<cert-id>
    alb.ingress.kubernetes.io/healthcheck-path: /healthz
    alb.ingress.kubernetes.io/healthcheck-port: "8090"
```

Install it the same way:

```bash
helm install flyte flyteorg/flyte-binary -n flyte --create-namespace -f values-eks.yaml
```

## Advanced configuration

The chart merges anything under `configuration.inline` into the rendered Flyte config,
which is how you set options the top-level values don't expose directly:

- **Default task resources** — `task_resources.defaults` / `.limits`.
- **Default pod scheduling for tasks** — `plugins.k8s.default-env-vars`,
  `default-tolerations`, `default-affinity`.
- **OpenTelemetry traces/metrics** — `otel.type` (`otlpgrpc`, `otlphttp`, …) and the
  matching exporter endpoint.

To supply the database password (or other secrets) from an existing Kubernetes Secret
instead of putting it in the values file, leave `password` empty and reference the
Secret with `configuration.extraInlineSecretRefs`, or mount a file and point
`configuration.database.postgres.passwordPath` at it.

Next: secure the deployment with [Authentication and SSO](./authentication).
