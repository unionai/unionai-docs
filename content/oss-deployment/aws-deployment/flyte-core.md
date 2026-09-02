---
title: flyte-core deployment
description: Install Flyte on AWS as one Deployment per component with the flyte-core chart, grant object-store access, and expose it through an ingress.
icon: diagram-2
variants: +flyte -union
weight: 2
---

# flyte-core deployment

This guide installs Flyte with the `flyte-core` Helm chart, which runs each Flyte
component in its **own Deployment** — `runs`, `actions`, `events`, `cache`,
`dataproxy`, `secret`, `executor`, and optionally `app` — so you can scale, schedule,
and roll them out independently. If you don't need that, the
[`flyte-binary` chart](./flyte-binary) packs the same components into a single pod
and is simpler to operate.

It assumes you have already provisioned the
[external dependencies](../overview) (a Kubernetes cluster, a PostgreSQL database, and
an object-store bucket) and that you have `helm` and `kubectl` configured against your
cluster.

## 1. Add the Helm repository

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm repo update
```

The `helm install` commands below reference the chart as `flyteorg/flyte-core`.

> [!WARNING] `flyte-core` is also the name of the Flyte 1 chart
> The same repository publishes `flyte-core` v1.x — a completely different chart, for
> Flyte 1. Flyte 2 is the v2.x line. `helm install` picks the highest version and so
> resolves to v2, but pin it if you want to be sure:
>
> ```bash
> helm search repo flyteorg/flyte-core --versions | head
> ```

## 2. Write a values file

Create a `values.yaml` with the minimum configuration. Everything in angle brackets is
a placeholder you replace:

```yaml
# values.yaml — minimal flyte-core configuration

# fullnameOverride prefixes every resource name (here: flyte-runs, flyte-actions,
# flyte-console, flyte-service-account). Without it the chart names its resources
# `runs`, `actions`, `console` — generic enough to collide with anything else in
# the namespace, so set it.
fullnameOverride: flyte

configuration:
  database:
    postgres:
      host: <postgres-host>            # e.g. my-db.example.com
      port: 5432
      dbname: flyte                    # database must already exist
      username: flyte
      password: <db-password>          # written to a mounted Secret (or use passwordPath)
      options: "sslmode=require"       # use sslmode=disable only for local/dev
  storage:
    metadataContainer: <bucket-name>   # object-store bucket Flyte reads and writes
    provider: s3                       # s3 | gcs | azure
    providerConfig:
      s3:
        region: <region>              # e.g. us-east-1
        authType: iam                 # iam (recommended) | accesskey
  runs:
    # Base URI for run inputs and outputs. Must point into the same bucket
    # as configuration.storage.metadataContainer above.
    storagePrefix: "s3://<bucket-name>"

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
| Run storage prefix | `configuration.runs.storagePrefix` | Base URI for run inputs and outputs. Defaults to `s3://flyte-data`, which you almost certainly do not own, so set it. Must point into the same bucket as `metadataContainer`. |
| Service account | `serviceAccount.annotations` | Cloud IAM binding for object-store access (step 4). |

The chart renders this one `configuration` block into a per-component ConfigMap and
projects it into every pod, so database and storage settings are written once and
shared. Only the component-level knobs under `components.*` are set per service.

> [!NOTE] Components find each other automatically
> `configuration.<component>.<peer>Service.url` defaults to a template that resolves
> to the peer's in-cluster Service — `http://flyte-actions.flyte:8080` for the example
> above. Setting `fullnameOverride` or installing into a different namespace is picked
> up automatically; you only override these URLs to point a component at a service
> outside the release.

## 3. Install

Render the manifests first to check your values, then install for real:

```bash
# Dry run — renders templates without touching the cluster
helm install flyte flyteorg/flyte-core -n flyte --create-namespace -f values.yaml --dry-run

# Install
helm install flyte flyteorg/flyte-core -n flyte --create-namespace -f values.yaml
```

Watch the rollout. There is one Deployment per enabled component, plus the console:

```bash
kubectl -n flyte rollout status deploy/flyte-runs
kubectl -n flyte get deploy
kubectl -n flyte get pods
```

A default install brings up eight Deployments: `flyte-runs`, `flyte-actions`,
`flyte-events`, `flyte-cache`, `flyte-dataproxy`, `flyte-secret`, `flyte-executor`,
and `flyte-console`. The `app` component is disabled by default because it needs
Knative Serving — see [Enable app serving](../app-serving).

A `wait-for-database` init container blocks `flyte-runs` and `flyte-cache` until the
database is reachable, so a pod stuck in `Init` usually means the database host,
credentials, or network policy are wrong. The other components have no init container
and will come up regardless; check `flyte-runs` first when something looks wrong.

## 4. Grant object-store access

The Flyte pods and the task pods they launch need credentials to read and write the
bucket. Prefer cloud-native workload identity over static keys.

**IRSA (recommended).** Annotate the service account with an IAM role that can access
the bucket. All components share this one service account unless a component sets
`components.<name>.serviceAccountName`:

```yaml
serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<flyte-role>
```

**Static keys** for S3-compatible stores such as MinIO, not recommended for
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
Run them under a service account that carries the IAM binding:

```yaml
configuration:
  executor:
    defaultK8sServiceAccount: flyte-service-account   # IAM-annotated SA tasks run as
```

> [!WARNING] The service account name is not `flyte`
> With `fullnameOverride: flyte` the chart creates a service account called
> **`flyte-service-account`**, not `flyte` — `flyte-binary` names the same thing
> `flyte`. Set `serviceAccount.name` if you want to choose the name yourself, and make
> `defaultK8sServiceAccount` match whatever it ends up being. A name that doesn't
> exist in the task namespace means task pods start without the IAM binding and fail
> on their first object-store read.

Task pods run in `configuration.kubernetes.namespace`, which defaults to the release
namespace. If you point it elsewhere, the service account must exist there.

## 5. Expose Flyte with an ingress

By default the chart only creates `ClusterIP` Services. To reach Flyte from outside
the cluster, enable the ingress. A **single HTTP ingress** serves the console and the
API — but unlike `flyte-binary`, it fans out across several backend Services, one path
prefix per Connect service:

```yaml
ingress:
  create: true
  host: <flyte.example.com>
  # Your cloud's native ingress class, e.g. alb (EKS), gce (GKE),
  # azure-application-gateway (AKS). See the Deployment overview for the options.
  ingressClassName: <ingress-class>
```

That renders one `Ingress` named `flyte-http` carrying fifteen path prefixes (two
more when `app` is enabled):

| Path prefix | Backend |
|---|---|
| `/v2` (`console.basePath`) | `flyte-console` |
| `/flyteidl2.workflow.RunService`, `.task.TaskService`, `.trigger.TriggerService`, `.project.ProjectService`, `.auth.IdentityService` | `flyte-runs` |
| `/flyteidl2.actions.ActionsService` | `flyte-actions` |
| `/flyteidl2.workflow.EventsProxyService` | `flyte-events` |
| `/flyteidl2.cacheservice.v2.CacheService` | `flyte-cache` |
| `/flyteidl2.dataproxy.DataProxyService`, `.cluster.ClusterService`, `.workflow.TranslatorService` | `flyte-dataproxy` |
| `/flyteidl2.secret.SecretService` | `flyte-secret` |
| `/.well-known/oauth-authorization-server`, `/flyteidl2.auth.AuthMetadataService` | `flyte-runs` |
| `/flyteidl2.app.AppService`, `.app.AppLogsService` | `flyte-app` (only when `components.app.enabled`) |

Paths for disabled components are skipped. The `executor` has no ingress route — it
is a controller, not an API.

The console is served under `console.basePath` (default `/v2`) on this same host. It
talks to the API same-origin, so it only works when the console and the API are behind
the **same ingress host**: always expose them together.

> [!WARNING] One health check for many target groups
> A fan-out ingress gives your controller a separate target group per backend Service,
> and an ingress-level health-check annotation applies to all of them. The Flyte
> components serve `/healthz` on port 8080; the console is a static web server whose
> own probes hit `console.basePath` instead. Override the console's health check on
> its Service:
>
> ```yaml
> console:
>   service:
>     annotations:
>       alb.ingress.kubernetes.io/healthcheck-path: /v2
> ```
>
> Every component and the console accept `service.annotations`, so you can tune any
> target group individually the same way.

For provider-specific ingress annotations (TLS, ALB scheme, health checks), add them
under `ingress.httpAnnotations`. As in `flyte-binary`, the ingress can also be split
in three — `ingress.apiJwtIngress` for SDK requests carrying an `Authorization: Bearer`
token and `ingress.wellknownIngress` for the unauthenticated auth-discovery endpoints
— which is what lets an ALB gate the console with cookie-OIDC without locking out
machine clients. See the AWS/EKS example below and the
[Authentication and SSO](../authentication) page.

## 6. Verify the installation

**Without an ingress**, port-forward the `runs` service and call a Connect endpoint:

```bash
kubectl -n flyte port-forward service/flyte-runs 8080:8080
```

```bash
# In another terminal — list projects over the Connect (HTTP) API:
curl -s -X POST \
  http://localhost:8080/flyteidl2.project.ProjectService/ListProjects \
  -H 'Content-Type: application/json' -d '{}'
```

A JSON response (rather than a connection error) confirms `flyte-runs` is up and
talking to its database.

Every component serves `/healthz` and `/readyz` on its own port 8080, and the chart
wires both into the pod's liveness and readiness probes — so `Running` **and** ready
across all of them is the health check:

```bash
kubectl -n flyte get pods -o wide
```

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

> [!WARNING] Confirm the load balancer is gone
> Check the AWS console that the ALB was actually deleted, so it stops billing.

The external dependencies (the RDS database, the S3 bucket, and the EKS cluster
itself) are untouched. Delete those separately in the AWS console (or with the tool
you provisioned them with) if you no longer need them.

## Full Values File Example

A fuller values file for an AWS/EKS cluster: RDS for PostgreSQL, S3 for storage, IRSA
for credentials, an ALB ingress, and the two API-facing components scaled out. Replace
every placeholder; no real account IDs, hostnames, or ARNs are included.

```yaml
# values-core-eks.yaml
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
  runs:
    storagePrefix: "s3://<flyte-bucket>"  # same bucket as metadataContainer
  executor:
    defaultK8sServiceAccount: flyte-service-account  # task pods inherit S3 access via IRSA

components:
  # The two components on the request path — scale these first.
  runs:
    replicaCount: 2
    resources:
      requests: { cpu: 500m, memory: 1Gi }
  actions:
    replicaCount: 2
    resources:
      requests: { cpu: 500m, memory: 1Gi }
  # The chart pins the executor to one replica — give it headroom, not replicas.
  executor:
    resources:
      requests: { cpu: 500m, memory: 2Gi }
  app:
    enabled: false                      # requires Knative Serving

serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::<account-id>:role/<flyte-role>

ingress:
  create: true
  host: <flyte.example.com>
  ingressClassName: alb
  httpAnnotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP": 80}, {"HTTPS": 443}]'
    alb.ingress.kubernetes.io/ssl-redirect: "443"
    alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account-id>:certificate/<cert-id>
    alb.ingress.kubernetes.io/healthcheck-path: /healthz

console:
  service:
    annotations:
      alb.ingress.kubernetes.io/healthcheck-path: /v2   # the console has no /healthz route
```

Install it the same way:

```bash
helm install flyte flyteorg/flyte-core -n flyte --create-namespace -f values-core-eks.yaml
```

## Scaling and scheduling individual components

This is the reason to run `flyte-core` at all. Every component takes the same set of
pod-level knobs under `components.<name>`:

```yaml
components:
  actions:
    replicaCount: 4
    resources:
      requests: { cpu: "1", memory: 2Gi }
      limits: { memory: 4Gi }
    nodeSelector:
      workload: flyte-control-plane
    tolerations:
      - key: flyte.org/node-role
        operator: Equal
        value: control-plane
        effect: NoSchedule
    topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: ScheduleAnyway
        labelSelector:
          matchLabels:
            app.kubernetes.io/component: actions
```

Also available per component: `image`, `extraEnv`, `envFrom`, `affinity`,
`priorityClassName`, `podLabels`, `podAnnotations`, `livenessProbe`, `readinessProbe`,
`startupProbe`, `initContainers`, `sidecars`, `extraVolumes`, `extraVolumeMounts`,
`strategy`, `extraPodSpec`, and `service.{type,annotations,labels,clusterIP}`.

> [!WARNING] The executor is always one replica
> `components.executor` has no `replicaCount` — the chart hardcodes `replicas: 1`.
> The executor reconciles `TaskAction` resources and hosts the pod admission webhook,
> and leader election is off by default (`configuration.executor.leaderElect: false`),
> so a second replica would duplicate work rather than share it. Give it more CPU and
> memory instead; `configuration.executor.maxConcurrentReconciles` (default `512`)
> controls how much it does in parallel.

Disable a component you don't need with `components.<name>.enabled: false`. Its
Deployment, Service, ConfigMap, and ingress paths all disappear together. The other
components address it by URL and will fail their calls to it, so in practice `app` is
the only one you turn off — and it already is by default.

## Default task resources

Anything under `configuration.inline` is merged into the rendered Flyte config of
**every** component, which is how you set options the top-level values don't expose
directly.

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
```

> [!WARNING] `default-env-vars` replaces the chart's own defaults
> Unlike `flyte-binary`, `flyte-core` ships a non-empty `configuration.inline`: it sets
> `plugins.k8s.default-env-vars` to the three `_U_*` variables that tell every task pod
> where the `actions` service is. Helm replaces lists rather than merging them, so a
> `default-env-vars` of your own **drops** them and tasks will fail to report back.
> Re-supply all three:
>
> ```yaml
> configuration:
>   inline:
>     plugins:
>       k8s:
>         default-env-vars:
>           - _U_EP_OVERRIDE: "flyte-actions.flyte:8080"   # <fullname>-actions.<namespace>
>           - _U_INSECURE: "true"
>           - _U_USE_ACTIONS: "1"
>           - MY_ENV_VAR: value
> ```

## OpenTelemetry

Flyte exports traces (and metrics, which reuse the trace exporter) via OpenTelemetry.
It's off by default (`otel.type: noop`). Point it at a collector under
`configuration.inline.otel`, which reaches every component at once:

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
| `noop` | disabled (default) | - |

Prefer `otlpgrpc`: the `otlphttp` metric exporter reuses the trace endpoint path.
Send to any OTLP collector (e.g. the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/),
which can fan metrics out to Prometheus and traces to Jaeger/Tempo).

The `executor` additionally serves Prometheus metrics on
`configuration.executor.metricsPort` (default `10254`), exposed as the `metrics` port
on the `flyte-executor` Service.

## Configuring passwords from Secrets

When you set `configuration.database.postgres.password`, the chart writes it into a
single Kubernetes Secret (kept out of the plaintext ConfigMaps) and projects it into
every component pod: the password lives only in your values file. The same applies to
S3 access keys when `authType: accesskey`.

To keep the **database password** out of the values file too, leave
`configuration.database.postgres.password` empty and either:

- reference an existing Kubernetes Secret with `configuration.extraInlineSecretRefs`, or
- mount the password as a file and point
  `configuration.database.postgres.passwordPath` at it.

When `authType: accesskey`, keep the **S3 secret key** out of the values file the
same way: leave `configuration.storage.providerConfig.s3.secretKey` empty and
either:

- reference an existing Kubernetes Secret with `configuration.extraInlineSecretRefs`, or
- mount the secret key as a file and point
  `configuration.storage.providerConfig.s3.secretKeyPath` at it.

On the recommended `authType: iam` path there is no storage secret to manage.

## Values differences from flyte-binary

The two charts configure the same platform but organize their values differently. A
`values.yaml` written for one will not install the other. The settings that move:

| Setting | `flyte-binary` | `flyte-core` |
|---|---|---|
| Run storage prefix | `flyte-core-components.runs.storagePrefix` | `configuration.runs.storagePrefix` |
| Task-pod namespace | `flyte-core-components.actions.kubernetes.namespace` | `configuration.kubernetes.namespace` |
| Data proxy upload/download | `flyte-core-components.dataproxy.*` | `configuration.dataproxy.*` |
| Task service account | `configuration.inline.executor.defaultK8sServiceAccount` | `configuration.executor.defaultK8sServiceAccount` (a real values key) |
| Enabled task plugins | `enabled_plugins` | `enabledPlugins` |
| Co-pilot image | `configuration.co-pilot.image` | `configuration.coPilot.image` |
| Log plugins (CloudWatch, Stackdriver, …) | `configuration.logging.plugins` | not templated — set under `configuration.inline` |
| Default `configuration.inline` | `{}` | non-empty (co-pilot image, `default-env-vars`) |
| Pod-level settings | `deployment.*` (one pod) | `components.<name>.*` (one per component) |
| API port | `8090` | `8080` per component |
| API Service | `flyte-http` (one) | `flyte-runs`, `flyte-actions`, … (one each) |
| Service account name | `flyte` | `flyte-service-account` |
| DB init container | `wait-for-db` | `wait-for-database` (on `runs` and `cache` only) |

Everything else — the `configuration.database`, `configuration.storage`,
`serviceAccount`, `console`, and `ingress` blocks, including `apiJwtIngress` and
`wellknownIngress` — is shaped the same in both charts.

Next: secure the deployment with [Authentication and SSO](../authentication).
