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

```bash
kind create cluster --name flyte
```

This creates a single-node cluster and points your `kubectl` context at it. Confirm it
is up:

```bash
kubectl cluster-info --context kind-flyte
```

> [!WARNING] Planning to add authentication? Create the cluster with a port mapping
> The optional [auth setup](#7-add-authentication-via-an-ingress-controller-optional)
> reaches Flyte through a Traefik ingress on the node's port `30080`, but a default kind
> cluster maps no host port to it — so `http://flyte.local` won't resolve from your
> browser. A cluster's port mappings are fixed **at creation time** and can't be added
> later, so if you intend to do step 7, create the cluster like this instead (and skip
> the plain `kind create cluster` above):
> ```bash
> kind create cluster --name flyte --config - <<'EOF'
> kind: Cluster
> apiVersion: kind.x-k8s.io/v1alpha4
> nodes:
>   - role: control-plane
>     extraPortMappings:
>       - containerPort: 30080   # Traefik's web nodePort (set in step 7)
>         hostPort: 80           # reach the ingress at http://flyte.local
>         protocol: TCP
> EOF
> ```
> The base port-forward access in step 6 doesn't need this; only the ingress in step 7
> does. If you already created a plain cluster and want auth, delete it
> (`kind delete cluster --name flyte`) and recreate it with the config above.

## 3. Deploy the dependencies

kind has no object store or database of its own, so deploy them. The main path runs
both inside the cluster; if you already have a PostgreSQL you want to reuse, use the
second tab.

{{< tabs "local-deps" >}}
{{< tab "In-cluster (MinIO + PostgreSQL)" >}}
{{< markdown >}}
Add the Bitnami chart repo and install MinIO and PostgreSQL into the `flyte` namespace:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
kubectl create namespace flyte

# PostgreSQL — sets the password and a database named "flyte"
helm install postgres bitnami/postgresql -n flyte \
  --set auth.username=flyte \
  --set auth.password=flyte \
  --set auth.database=flyte \
  --set image.repository=bitnamilegacy/postgresql \
  --set global.security.allowInsecureImages=true

# MinIO — sets the root credentials and creates a "flyte" bucket
helm install minio bitnami/minio -n flyte \
  --set auth.rootUser=minio \
  --set auth.rootPassword=miniostorage \
  --set defaultBuckets=flyte \
  --set image.repository=bitnamilegacy/minio \
  --set console.image.repository=bitnamilegacy/minio-object-browser \
  --set clientImage.repository=bitnamilegacy/minio-client \
  --set defaultInitContainers.volumePermissions.image.repository=bitnamilegacy/os-shell \
  --set global.security.allowInsecureImages=true
```

> [!NOTE] Why the `bitnamilegacy` image overrides
> In late 2025 Bitnami moved its free container images to the `bitnamilegacy`
> Docker Hub org and stopped publishing new tags under `bitnami/*`. The chart
> defaults still point at `bitnami/*`, so an unmodified install fails with
> `ImagePullBackOff` (image `not found`). The `--set …image.repository` flags
> redirect each image to `bitnamilegacy/*`; `allowInsecureImages=true` lets the
> chart use a registry other than its pinned default.

This gives you the in-cluster service addresses the values file below points at:

- PostgreSQL: `postgres-postgresql.flyte.svc.cluster.local:5432`
- MinIO: `http://minio.flyte.svc.cluster.local:9000`
{{< /markdown >}}
{{< /tab >}}
{{< tab "Use your own PostgreSQL" >}}
{{< markdown >}}
Install only MinIO for object storage, and point the database config at your existing
PostgreSQL instead:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
kubectl create namespace flyte

helm install minio bitnami/minio -n flyte \
  --set auth.rootUser=minio \
  --set auth.rootPassword=miniostorage \
  --set defaultBuckets=flyte \
  --set image.repository=bitnamilegacy/minio \
  --set console.image.repository=bitnamilegacy/minio-object-browser \
  --set clientImage.repository=bitnamilegacy/minio-client \
  --set defaultInitContainers.volumePermissions.image.repository=bitnamilegacy/os-shell \
  --set global.security.allowInsecureImages=true
```

The `bitnamilegacy/*` overrides are required because Bitnami no longer publishes
these images under `bitnami/*` — see the note in the first tab.

In the values file below, replace the `database.postgres` block with your own host,
database name, and credentials. The database must already exist. If it isn't reachable
over an in-cluster service name, use an address kind can reach — for a database running
on your host, that is `host.docker.internal`.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

## 4. Write the values file

Create `values-local.yaml`. This points Flyte at the in-cluster PostgreSQL and MinIO,
uses static access keys (no cloud workload identity), and skips the ingress — you'll
reach Flyte with `kubectl port-forward`:

```yaml
# values-local.yaml — local kind deployment
fullnameOverride: flyte

configuration:
  database:
    postgres:
      host: postgres-postgresql.flyte.svc.cluster.local
      port: 5432
      dbname: flyte
      username: flyte
      password: flyte
      options: "sslmode=disable"        # in-cluster Postgres has no TLS here
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

serviceAccount:
  create: true
  annotations: {}                       # no IRSA/Workload Identity locally

ingress:
  create: false                         # reach Flyte via port-forward instead
```

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
