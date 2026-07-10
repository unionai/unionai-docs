---
title: AWS deployment
variants: +flyte -union
weight: 3
---

# AWS deployment

This guide installs Flyte with the `flyte-binary` Helm chart. It assumes you have
already provisioned the [external dependencies](./overview) — a Kubernetes cluster, a
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
      password: <db-password>          # creates a mounted Secret (or use passwordPath)
      options: "sslmode=require"       # use sslmode=disable only for local/dev
  storage:
    metadataContainer: <bucket-name>   # object-store bucket Flyte reads and writes
    provider: s3                       # s3 | gcs | azure
    providerConfig:
      s3:
        region: <region>              # e.g. us-east-1
        authType: iam                 # iam (recommended) | accesskey

serviceAccount:
  create: true
  annotations: {}                     # IRSA role binding — see step 4
```

The required fields:

| Setting | Key | Notes |
|---|---|---|
| Database host | `configuration.database.postgres.host` | Reachable from the cluster. |
| Database name | `configuration.database.postgres.dbname` | Must already exist. |
| Database user | `configuration.database.postgres.username` | Default `postgres`. |
| Database password | `configuration.database.postgres.password` | Creates and mounts a Secret. Use `passwordPath` instead to mount your own. The two are mutually exclusive. |
| Storage bucket | `configuration.storage.metadataContainer` | The object-store bucket Flyte reads and writes. |
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

**IRSA (recommended).** Annotate the service account with an IAM role that can access
the bucket:

```yaml
serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<flyte-role>
```

**Static keys** for S3-compatible stores such as MinIO — not recommended for
production:

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
the cluster, enable the ingress. A **single HTTP ingress** serves the console and the
API — there is no separate gRPC ingress (see the
[Deployment overview](./overview)).

```yaml
ingress:
  create: true
  host: <flyte.example.com>
  # Your cloud's native ingress class, e.g. alb (EKS), gce (GKE),
  # azure-application-gateway (AKS). See the Deployment overview for the options.
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


## 7. Tear down

Uninstall the Helm release and delete the namespace:

```bash
helm uninstall flyte -n flyte
kubectl delete namespace flyte
```

Uninstalling the release removes the ingress resource, which prompts the ingress
controller (e.g. the AWS Load Balancer Controller) to delete the load balancer it
provisioned.

{{< WARNING >}}
Confirm the ALB is gone in the AWS console so it stops billing.
{{< /WARNING >}}

The external dependencies — the RDS database, the S3 bucket, and the EKS cluster
itself — are untouched. Delete those separately in the AWS console (or with the tool
you provisioned them with) if you no longer need them.

Next: secure the deployment with [Authentication and SSO](./authentication).

## Full Values File Example

A fuller values file for an AWS/EKS cluster — RDS for PostgreSQL, S3 for storage, IRSA
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
      password: <db-password>          # chart stores this in a Secret, not the ConfigMap
      options: "sslmode=require"
  storage:
    metadataContainer: <flyte-bucket>
    provider: s3
    providerConfig:
      s3:
        region: <region>
        authType: iam
  inline:
    executor:
      defaultK8sServiceAccount: flyte   # task pods inherit S3 access via IRSA

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

## Default task resources

Anything under `configuration.inline` is merged into the rendered Flyte config, which
is how you set options the top-level values don't expose directly.

Set the default CPU and memory **requests** for task pods that don't specify their own,
via the Kubernetes plugin config:

```yaml
configuration:
  inline:
    plugins:
      k8s:
        default-cpus: 500m
        default-memory: 1Gi
```

## Default scheduling for task pods

Add tolerations, affinity / node selectors, or injected environment variables to every
task pod under `configuration.inline.plugins.k8s`:

```yaml
configuration:
  inline:
    plugins:
      k8s:
        default-tolerations:
          - key: flyte.org/node-role
            operator: Equal
            value: worker
            effect: NoSchedule
        default-affinity: {}             # a standard core/v1 Affinity
        default-env-vars:
          - MY_ENV_VAR: value            # injected into every task pod
```

## OpenTelemetry

Flyte exports traces (and metrics, which reuse the trace exporter) via OpenTelemetry.
It's off by default (`otel.type: noop`). Point it at a collector under
`configuration.inline.otel`:

```yaml
configuration:
  inline:
    otel:
      type: otlpgrpc                    # noop | file | jaeger | otlpgrpc | otlphttp
      otlpgrpc:
        endpoint: http://otel-collector.flyte.svc.cluster.local:4317
      # Trace sampling — keep a fraction in production.
      sampler:
        parentSampler: traceid
        traceIdRatio: 0.01             # sample 1% of traces
```

| `otel.type` | Where it sends | Endpoint key |
|---|---|---|
| `otlpgrpc` | OTLP collector over gRPC (recommended) | `otlpgrpc.endpoint` |
| `otlphttp` | OTLP collector over HTTP | `otlphttp.endpoint` |
| `jaeger` / `file` | Jaeger / a local file | `jaeger.*` / `file.*` |
| `noop` | disabled (default) | — |

Prefer `otlpgrpc` — the `otlphttp` metric exporter reuses the trace endpoint path.
Send to any OTLP collector (e.g. the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/),
which can fan metrics out to Prometheus and traces to Jaeger/Tempo).

## Database password from a Secret

When you set `configuration.database.postgres.password`, the chart writes it into a
Kubernetes Secret (kept out of the plaintext ConfigMap) and mounts it into the Flyte
pod — the password lives only in your values file. The same applies to S3 access keys
when `authType: accesskey`.

To keep the password out of the values file too, leave
`configuration.database.postgres.password` empty and either:

- reference an existing Kubernetes Secret with `configuration.extraInlineSecretRefs`, or
- mount the password as a file and point
  `configuration.database.postgres.passwordPath` at it.
