---
title: Running Flyte locally with kind
variants: +flyte -union
weight: 5
---

# Running Flyte locally with kind

This guide spins up a complete Flyte stack — the Flyte binary plus an in-cluster
PostgreSQL and an S3-compatible object store (MinIO) — on a local
[kind](https://kind.sigs.k8s.io/) cluster. It's the fastest way to try Flyte without
provisioning any cloud infrastructure.

> [!WARNING] For local evaluation only
> This setup has no TLS, no authentication, and runs its database and object store
> inside the cluster with static credentials. Use it to try Flyte locally — not as a
> template for a production deployment. For that, see [Installing Flyte](./installing).

## 1. Prerequisites

Install these on your machine:

- [Docker](https://docs.docker.com/get-docker/) (kind runs the cluster in containers)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
- [`helm`](https://helm.sh/docs/intro/install/)

## 2. Create the kind cluster

Create the cluster with two host-port mappings up front. kind fixes a cluster's port
mappings **at creation time** — they can't be added later — and both are awkward to add
after the fact, so map them now even though they're used in later steps:

```bash
kind create cluster --name flyte --config - <<'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 30002   # MinIO's nodePort (set in step 3) — presigned uploads
        hostPort: 30002        # reach the object store at http://localhost:30002
        protocol: TCP
      - containerPort: 30080   # Traefik's web nodePort (set in step 7) — the ingress
        hostPort: 80           # reach the ingress at http://flyte.local
        protocol: TCP
EOF
```

This creates a single-node cluster and points your `kubectl` context at it. Confirm it
is up:

```bash
kubectl cluster-info --context kind-flyte
```

> [!NOTE] What the two mappings are for
> - **`30002 → 30002`** lets the SDK reach MinIO directly to upload code bundles. Flyte
>   signs upload URLs with a host the SDK must be able to resolve; the SDK is off-cluster,
>   so it can't use the in-cluster service DNS. This mapping exposes MinIO's nodePort on
>   `localhost:30002`, which is what [step 4](#4-write-the-values-file) signs the URLs
>   with. Without it, `flyte.run` fails the upload with `Unauthorized`. (On a real cloud
>   this never comes up — the S3 endpoint is already publicly resolvable.)
> - **`30080 → 80`** lets the browser reach the Traefik ingress used by the optional
>   [auth setup](#7-add-authentication-via-an-ingress-controller-optional) at
>   `http://flyte.local`.
>
> If you already created a plain `kind create cluster --name flyte` without these, delete
> it (`kind delete cluster --name flyte`) and recreate it with the config above.

## 3. Deploy the dependencies

kind has no object store or database of its own, so Flyte needs one of each. Pick a
PostgreSQL and an object store below — the all-local pair (in-cluster PostgreSQL +
MinIO) needs no cloud account, or you can point at a hosted service like Supabase,
AWS S3, or Cloudflare R2. The two choices are independent; mix and match. Each tab's
config block plugs into [the values file in step 4](#4-write-the-values-file).

Create the namespace once, whichever options you pick:

```bash
kubectl create namespace flyte
```

### PostgreSQL

{{< tabs "local-postgres" >}}
{{< tab "In-cluster PostgreSQL" >}}
{{< markdown >}}
Install Bitnami's PostgreSQL chart into the `flyte` namespace:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm install postgres bitnami/postgresql -n flyte \
  --set auth.username=flyte \
  --set auth.password=flyte \
  --set auth.database=flyte \
  --set image.repository=bitnamilegacy/postgresql \
  --set global.security.allowInsecureImages=true
```

> [!NOTE] Why the `bitnamilegacy` image overrides
> In late 2025 Bitnami moved its free container images to the `bitnamilegacy`
> Docker Hub org and stopped publishing new tags under `bitnami/*`. The chart
> defaults still point at `bitnami/*`, so an unmodified install fails with
> `ImagePullBackOff` (image `not found`). The `--set …image.repository` flags
> redirect each image to `bitnamilegacy/*`; `allowInsecureImages=true` lets the
> chart use a registry other than its pinned default.

In-cluster service address for the values file:
`postgres-postgresql.flyte.svc.cluster.local:5432`.

```yaml
  database:
    postgres:
      host: postgres-postgresql.flyte.svc.cluster.local
      port: 5432
      dbname: flyte
      username: flyte
      password: flyte
      options: "sslmode=disable"        # in-cluster Postgres has no TLS here
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Supabase (hosted)" >}}
{{< markdown >}}
Nothing to install in the cluster — create a project at [supabase.com](https://supabase.com/),
then open **Project Settings → Database → Connection string** and switch the tab to
**Session pooler**. Use that string, **not** the direct connection.

> [!WARNING] Use the session pooler, not the direct connection
> Supabase's direct host (`db.<project-ref>.supabase.co`) resolves to **IPv6 only**.
> A kind cluster is IPv4-only, so the Flyte pod can't reach it — `wait-for-db` passes
> (it only probes the port) but Flyte then crash-loops on `failed to connect`. The
> **session pooler** host (`aws-<n>-<region>.pooler.supabase.com`) has IPv4, so use it.
> Use the **session** pooler on port `5432`, not the transaction pooler (`6543`) —
> Flyte's migrations need session semantics.
>
> Two things the pooler changes versus the direct string, both shown verbatim in the
> Session pooler tab — **copy them, don't guess**:
> - **Username carries the project ref**: `postgres.<project-ref>`, not bare `postgres`.
> - **The region must match your project's**: `aws-<n>-<region>.pooler.supabase.com`.
>   A mismatched region connects but is rejected with `tenant/user not found`.

```yaml
  database:
    postgres:
      # From the "Session pooler" connection string — copy host and username verbatim.
      host: aws-1-ap-northeast-1.pooler.supabase.com   # <- your project's pooler host
      port: 5432                        # session mode (not 6543 transaction mode)
      dbname: postgres                  # Supabase's default database
      username: postgres.<project-ref>  # pooler requires the ref-qualified username
      password: <your-supabase-db-password>
      options: "sslmode=require"        # Supabase requires TLS
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

### Object store

{{< tabs "local-objectstore" >}}
{{< tab "In-cluster MinIO" >}}
{{< markdown >}}
Install MinIO into the `flyte` namespace. It creates a `flyte` bucket and exposes its
API on nodePort `30002` so the off-cluster SDK can upload to presigned URLs:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

helm install minio bitnami/minio -n flyte \
  --set auth.rootUser=minio \
  --set auth.rootPassword=miniostorage \
  --set defaultBuckets=flyte \
  --set service.type=NodePort \
  --set service.nodePorts.api=30002 \
  --set image.repository=bitnamilegacy/minio \
  --set console.image.repository=bitnamilegacy/minio-object-browser \
  --set clientImage.repository=bitnamilegacy/minio-client \
  --set defaultInitContainers.volumePermissions.image.repository=bitnamilegacy/os-shell \
  --set global.security.allowInsecureImages=true
```

The `bitnamilegacy/*` overrides are required because Bitnami no longer publishes these
images under `bitnami/*` — see the note under the in-cluster PostgreSQL tab.

The presigned-upload host (`signedURL` block) is the reason step 2 maps nodePort
`30002 → 30002`: the SDK signs uploads with `localhost:30002`, which the cluster routes
straight to MinIO.

```yaml
  storage:
    metadataContainer: flyte
    userDataContainer: flyte
    provider: s3
    providerConfig:
      s3:
        endpoint: http://minio.flyte.svc.cluster.local:9000
        authType: accesskey
        accessKey: minio
        secretKey: miniostorage
        disableSSL: true                # MinIO is served over plain HTTP here
        v2Signing: false                # set true if MinIO rejects v4 signatures
        region: us-east-1               # any value; MinIO ignores it
  inline:
    storage:
      signedURL:
        stowConfigOverride:
          # The SDK uploads code bundles to a presigned URL that Flyte signs.
          # In-cluster, Flyte reaches MinIO at the service DNS above — but your
          # off-cluster SDK can't resolve that name, so the upload fails with
          # "Unauthorized". Sign these URLs with MinIO's nodePort instead, which
          # the cluster maps to localhost:30002 (see step 2). On a real cloud
          # this isn't needed: the S3 endpoint is already publicly resolvable.
          endpoint: http://localhost:30002
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "AWS S3" >}}
{{< markdown >}}
Create an S3 bucket in your AWS account and an IAM user (or access key) that can read
and write it. With a real, publicly-resolvable S3 endpoint the SDK uploads to presigned
URLs directly, so **no MinIO nodePort and no `signedURL` override** are needed — you can
drop the `30002` mapping from step 2 if you're not also running MinIO.

```yaml
  storage:
    metadataContainer: <your-s3-bucket>
    userDataContainer: <your-s3-bucket>
    provider: s3
    providerConfig:
      s3:
        region: <bucket-region>         # e.g. us-east-1
        authType: accesskey
        accessKey: <aws-access-key-id>
        secretKey: <aws-secret-access-key>
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "Cloudflare R2" >}}
{{< markdown >}}
Create an R2 bucket and an R2 API token (Access Key ID + Secret) in the Cloudflare
dashboard. R2 is S3-compatible: point the `endpoint` at your account's R2 URL and use
`auto` for the region. Its endpoint is publicly resolvable, so like S3 it needs **no
MinIO nodePort and no `signedURL` override**.

```yaml
  storage:
    metadataContainer: <your-r2-bucket>
    userDataContainer: <your-r2-bucket>
    provider: s3
    providerConfig:
      s3:
        endpoint: https://<account-id>.r2.cloudflarestorage.com
        region: auto                    # R2 ignores region; "auto" is conventional
        authType: accesskey
        accessKey: <r2-access-key-id>
        secretKey: <r2-secret-access-key>
        v2Signing: false
```
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## 4. Write the values file

Create `values-local.yaml` by dropping in the `database` and `storage` blocks from the
PostgreSQL and object-store tabs you picked in [step 3](#3-deploy-the-dependencies). It
uses static access keys (no cloud workload identity) and skips the ingress — you'll
reach Flyte with `kubectl port-forward`:

```yaml
# values-local.yaml — local kind deployment
fullnameOverride: flyte

configuration:
  # ── paste your PostgreSQL block here (from step 3) ──
  database:
    postgres:
      host: postgres-postgresql.flyte.svc.cluster.local
      port: 5432
      dbname: flyte
      username: flyte
      password: flyte
      options: "sslmode=disable"
  # ── paste your object-store block here (from step 3) ──
  storage:
    metadataContainer: flyte
    userDataContainer: flyte
    provider: s3
    providerConfig:
      s3:
        endpoint: http://minio.flyte.svc.cluster.local:9000
        authType: accesskey
        accessKey: minio
        secretKey: miniostorage
        disableSSL: true
        v2Signing: false
        region: us-east-1
  # The signedURL override below is MinIO-only — it makes the SDK sign uploads
  # with localhost:30002 (see step 2). Drop this whole `inline.storage` block
  # when using S3 or R2; their endpoints are already publicly resolvable.
  inline:
    storage:
      signedURL:
        stowConfigOverride:
          endpoint: http://localhost:30002

serviceAccount:
  create: true
  annotations: {}                       # no IRSA/Workload Identity locally

ingress:
  create: false                         # reach Flyte via port-forward instead
```

The block above shows the all-local pair (in-cluster PostgreSQL + MinIO). If you chose
Supabase, S3, or R2, swap the matching block for that tab's — and for S3/R2 remove the
`inline.storage` block, since the `signedURL` override only exists to route uploads
through MinIO's nodePort.

## 5. Install Flyte

```bash
helm repo add flyteorg https://flyteorg.github.io/flyte
helm repo update

helm install flyte flyteorg/flyte-binary -n flyte -f values-local.yaml
```

Watch the rollout:

```bash
kubectl -n flyte rollout status deploy/flyte
kubectl -n flyte get pods
```

A `wait-for-db` init container blocks startup until PostgreSQL is reachable, so a pod
stuck in `Init` usually means the database isn't up yet or the host/credentials are
wrong.

## 6. Access Flyte

Port-forward the API service and point the SDK/CLI at `localhost`:

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

### Submitting runs from the SDK

Point the SDK at the API forward you just started. Write `~/.flyte/config.yaml`:

```yaml
# ~/.flyte/config.yaml
admin:
  endpoint: dns:///localhost:8090   # the port-forwarded API
  insecure: True                    # plain HTTP, no TLS
task:
  org: local
  domain: development
  project: flytesnacks
```

The code-bundle upload needs no extra setup: Flyte signs the presigned URL with
`localhost:30002` (from [step 4](#4-write-the-values-file)), which the cluster maps
straight to MinIO (from [step 2](#2-create-the-kind-cluster)). Only the one API
port-forward is required — MinIO is reached over its nodePort, not a second forward.

> [!NOTE] `Unauthorized` on upload
> If `flyte.run` fails the code-bundle upload with `Unauthorized`, the signed MinIO host
> isn't reachable from your machine. Check that the cluster has the `30002 → 30002`
> mapping (`docker ps --filter name=flyte-control-plane --format '{{.Ports}}'`), that
> MinIO was installed with `service.type=NodePort` and `service.nodePorts.api=30002`, and
> that `signedURL.stowConfigOverride.endpoint` is `http://localhost:30002`.

## 7. Add authentication via an ingress controller (optional)

The cloud worked examples in [Installing Flyte](./installing) gate the console with
OIDC single sign-on at the load balancer — on AWS that's the ALB, configured through
`alb.ingress.kubernetes.io/auth-*` annotations. Those annotations are instructions to
the *AWS Load Balancer Controller* and do nothing on kind, which has no ALB.

The pattern is the same on kind; only the ingress controller changes. Here you run
[Traefik](https://doc.traefik.io/traefik/) and delegate auth to
[oauth2-proxy](https://oauth2-proxy.github.io/oauth2-proxy/): Traefik intercepts each
request through a `ForwardAuth` middleware, asks oauth2-proxy whether the caller is
logged in, and redirects to your IdP if not. oauth2-proxy plays the role the ALB played
— an auth proxy at the edge.

> [!NOTE] You still need an IdP
> oauth2-proxy validates against an OIDC provider. Either register an app at an external
> provider (Okta, Google, Auth0, …) with the redirect URI `http://<host>/oauth2/callback`
> and have its client ID and secret ready, or run a throwaway IdP in the cluster — see
> [A local IdP with Dex](./local-dex) for a fully-local setup with test users.

### Install the ingress controller

Install Traefik with its Helm chart and expose it on the kind node's HTTP port `30080` —
the port the cluster maps to host port `80` (see the warning in
[step 2](#2-create-the-kind-cluster)). If your cluster doesn't have that mapping,
`http://flyte.local` won't reach Traefik and you'll need to recreate the cluster.

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update

helm install traefik traefik/traefik -n traefik --create-namespace \
  --set "ports.web.nodePort=30080" \
  --set "service.type=NodePort"
```

Traefik installs its CRDs (including `Middleware`) and registers a `traefik`
IngressClass.

### Deploy oauth2-proxy

Give oauth2-proxy your IdP details and a random cookie secret. `--set-xauthrequest`
makes it emit the `X-Auth-Request-*` headers Traefik forwards downstream, and
`--reverse-proxy` tells it to trust the forwarded host/proto from Traefik:

```bash
# 32-byte cookie secret, base64-encoded
COOKIE_SECRET=$(openssl rand -base64 32)

helm repo add oauth2-proxy https://oauth2-proxy.github.io/manifests
helm repo update

helm install oauth2-proxy oauth2-proxy/oauth2-proxy -n flyte \
  --set config.clientID='<oidc-client-id>' \
  --set config.clientSecret='<oidc-client-secret>' \
  --set config.cookieSecret="$COOKIE_SECRET" \
  --set extraArgs.provider=oidc \
  --set extraArgs.oidc-issuer-url='https://<your-idp>/oauth2/default' \
  --set extraArgs.upstream='static://202' \
  --set extraArgs.reverse-proxy='true' \
  --set extraArgs.set-xauthrequest='true' \
  --set extraArgs.email-domain='*' \
  --set extraArgs.cookie-secure='false'      # local HTTP, not HTTPS
```

### Create the ForwardAuth middleware

Two Traefik `Middleware` objects: one sends each request to oauth2-proxy for a verdict
and forwards the identity headers; the other catches the `401` an unauthenticated
request gets and redirects it to the oauth2-proxy sign-in page.

```yaml
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: oauth2-auth
  namespace: flyte
spec:
  forwardAuth:
    address: http://oauth2-proxy.flyte.svc.cluster.local/oauth2/auth
    trustForwardHeader: true
    # Forwarded to Flyte; these feed executed_by run attribution.
    authResponseHeaders:
      - X-Auth-Request-User
      - X-Auth-Request-Email
---
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: oauth2-signin
  namespace: flyte
spec:
  errors:
    status:
      - "401"
    service:
      name: oauth2-proxy
      port: 80
    query: "/oauth2/sign_in?rd={url}"
```

### Create the Flyte ingress with the middleware

Re-render Flyte with the ingress enabled and pointed at Traefik. The
`traefik.ingress.kubernetes.io/router.middlewares` annotation chains both middlewares
onto every route — this is the Traefik equivalent of the ALB's `auth-type: oidc`. The
reference format is `<namespace>-<name>@kubernetescrd`:

```yaml
# add to values-local.yaml, replacing the `ingress.create: false` block
ingress:
  create: true
  host: flyte.local                 # add "127.0.0.1 flyte.local" to /etc/hosts
  ingressClassName: traefik
  httpAnnotations:
    traefik.ingress.kubernetes.io/router.middlewares: flyte-oauth2-signin@kubernetescrd,flyte-oauth2-auth@kubernetescrd
```

You also need a route that sends `/oauth2` to oauth2-proxy itself so the sign-in
redirect resolves. Apply it alongside the Flyte release:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: oauth2-proxy
  namespace: flyte
spec:
  ingressClassName: traefik
  rules:
  - host: flyte.local
    http:
      paths:
      - path: /oauth2
        pathType: Prefix
        backend:
          service:
            name: oauth2-proxy
            port:
              number: 80
```

After `helm upgrade flyte … -f values-local.yaml`, add a hosts entry so the browser can
resolve `flyte.local` to the local Traefik node port (do this once):

```bash
echo "127.0.0.1 flyte.local" | sudo tee -a /etc/hosts
```

`http://127.0.0.1/v2` won't work in its place — Traefik has no route for that host, and
the OIDC issuer is `flyte.local`, so login fails on an issuer mismatch. Then open
`http://flyte.local/v2` — Traefik bounces you through the IdP and back into the console.
SDK/CLI clients that send an `Authorization: Bearer` token authenticate against the same
IdP.

To make the API trust those tokens (rather than only gating the browser), turn on
Flyte's own token validation as well — see
[Authentication and SSO](./authentication) for `configuration.auth`.

## 8. Load a local image into kind (optional)

kind nodes can't pull from your local Docker daemon. If you build a custom task or
Flyte image locally, load it into the cluster so pods can run it without a registry:

```bash
kind load docker-image <your-image>:<tag> --name flyte
```

Reference that exact `<your-image>:<tag>` in your task config; with the image already
present, the default `IfNotPresent` pull policy won't try to fetch it from a registry.

## 9. Tear down

Delete the whole cluster — Flyte, PostgreSQL, MinIO, and all data — in one command:

```bash
kind delete cluster --name flyte
```

When you're ready to deploy to a real cluster, continue to
[Installing Flyte](./installing).
