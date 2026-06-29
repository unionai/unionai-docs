---
title: Running Flyte locally with kind
variants: +flyte -union
weight: 5
---

# Running Flyte locally with kind

This guide spins up a complete Flyte stack — the Flyte binary on a local
[kind](https://kind.sigs.k8s.io/) cluster, backed by a hosted PostgreSQL and an
S3-compatible object store. It's a fast way to try Flyte without running a
production-grade control plane.

> [!WARNING] For local evaluation only
> This runs on a single-node kind cluster with static credentials (no workload identity),
> and the optional [auth setup](#7-add-authentication-via-an-ingress-controller-optional)
> uses a self-signed cert the SDK only accepts via `insecureSkipVerify`. Use it to try
> Flyte locally — not as a template for a production deployment. For that, see
> [Installing Flyte](./installing).

## 1. Prerequisites

Install these on your machine:

- [Docker](https://docs.docker.com/get-docker/) (kind runs the cluster in containers)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
- [`helm`](https://helm.sh/docs/intro/install/)

## 2. Create the kind cluster

Create the cluster with two host-port mappings up front. kind fixes a cluster's port
mappings **at creation time** — they can't be added later — so map them now even
though they're only used in the optional auth step:

```bash
kind create cluster --name flyte --config - <<'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 30080   # Traefik's web (HTTP) nodePort (step 7) — browser ingress
        hostPort: 80           # reach the ingress at http://flyte.local
        protocol: TCP
      - containerPort: 30443   # Traefik's websecure (HTTPS) nodePort (step 7) — SDK auth
        hostPort: 443          # reach the TLS ingress at https://flyte.local
        protocol: TCP
EOF
```

This creates a single-node cluster and points your `kubectl` context at it. Confirm it
is up:

```bash
kubectl cluster-info --context kind-flyte
```

> [!NOTE] What the two mappings are for
> - **`30080 → 80`** lets the **browser** reach the Traefik ingress (plain HTTP) used by
>   the optional [auth setup](#7-add-authentication-via-an-ingress-controller-optional) at
>   `http://flyte.local`.
> - **`30443 → 443`** lets the **SDK/CLI** reach the Traefik ingress over **TLS** at
>   `https://flyte.local`. The SDK only authenticates over HTTPS (see
>   [Letting the SDK authenticate](#letting-the-sdkcli-authenticate-with-auth-enabled)),
>   so this mapping is required if you enable ingress auth *and* want to submit runs from
>   the SDK. Harmless if you never enable auth.
>
> If you already created a plain `kind create cluster --name flyte` without these, delete
> it (`kind delete cluster --name flyte`) and recreate it with the config above.

## 3. Deploy the dependencies

kind runs only the Flyte binary; the database and object store are hosted. You need a
PostgreSQL (Supabase or another external/self-hosted instance) and an S3-compatible
object store (AWS S3 or Cloudflare R2). The two choices are independent. Each config
block below plugs into [the values file in step 4](#4-write-the-values-file).

Create the namespace:

```bash
kubectl create namespace flyte
```

### PostgreSQL

Create a project at [supabase.com](https://supabase.com/), then open **Project
Settings → Database → Connection string** and switch the tab to **Session pooler**.
Use that string, **not** the direct connection. (Another external or self-hosted
PostgreSQL works the same way — supply its host, database, user, and password, with
`sslmode` to match. For a DB on your host machine, use `host.docker.internal` as the
host. The database must already exist.)

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

### Object store

Both AWS S3 and Cloudflare R2 have publicly-resolvable endpoints, so the off-cluster
SDK uploads code bundles to presigned URLs directly — no nodePort or `signedURL`
override is needed.

{{< tabs "local-objectstore" >}}
{{< tab "AWS S3" >}}
{{< markdown >}}
Create an S3 bucket in your AWS account and an IAM user (or access key) that can read
and write it.

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
`auto` for the region.

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

Create `values-local.yaml` by dropping in the `database` and `storage` blocks from
[step 3](#3-deploy-the-dependencies). It uses static access keys (no cloud workload
identity) and skips the ingress — you'll reach Flyte with `kubectl port-forward`:

```yaml
# values-local.yaml — local kind deployment
fullnameOverride: flyte

configuration:
  # ── your PostgreSQL block (from step 3) — Supabase shown ──
  database:
    postgres:
      host: aws-1-ap-northeast-1.pooler.supabase.com   # <- your project's pooler host
      port: 5432
      dbname: postgres
      username: postgres.<project-ref>
      password: <your-supabase-db-password>
      options: "sslmode=require"
  # ── your object-store block (from step 3) — AWS S3 shown ──
  storage:
    metadataContainer: <your-s3-bucket>
    userDataContainer: <your-s3-bucket>
    provider: s3
    providerConfig:
      s3:
        region: <bucket-region>
        authType: accesskey
        accessKey: <aws-access-key-id>
        secretKey: <aws-secret-access-key>

serviceAccount:
  create: true
  annotations: {}                       # no IRSA/Workload Identity locally

ingress:
  create: false                         # reach Flyte via port-forward instead
```

Swap in the R2 storage block if you chose Cloudflare R2.

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

The code-bundle upload needs no extra setup — only the one API port-forward is required,
never a second one for the object store. The S3/R2 endpoint is publicly resolvable, so
the SDK uploads to the presigned URL directly.

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

Install Traefik with its Helm chart and expose **both** entrypoints on the kind node's
nodePorts — `web` (HTTP) on `30080` and `websecure` (HTTPS) on `30443`, the ports the
cluster maps to host `80` and `443` (see the warning in
[step 2](#2-create-the-kind-cluster)). The browser uses HTTP; **the SDK needs HTTPS** —
expose both up front so you don't have to reinstall later.

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update

helm install traefik traefik/traefik -n traefik --create-namespace \
  --set "service.type=NodePort" \
  --set "ports.web.nodePort=30080" \
  --set "ports.websecure.nodePort=30443"
```

Traefik installs its CRDs (including `Middleware`), registers a `traefik` IngressClass,
and serves a **default self-signed certificate** on `websecure`. If your cluster lacks
the `30080 → 80` / `30443 → 443` mappings from [step 2](#2-create-the-kind-cluster),
Traefik is unreachable at `flyte.local` and you'll need to recreate the cluster.

#### Replace the default cert with one for `flyte.local`

Traefik's built-in cert is rejected by the SDK for two reasons, hit in sequence if you
only set `insecureSkipVerify` later:

- Its SAN is `*.traefik.default`, so the hostname check fails with
  `certificate not valid for name "flyte.local"`. The SDK validates the SAN **even with
  `insecureSkipVerify`** (that flag relaxes CA trust, not the hostname).
- The SDK implements `insecureSkipVerify` by fetching the server's cert chain and
  **pinning it as the CA**. A bare self-signed leaf then fails with `CaUsedAsEndEntity` —
  rustls won't use a leaf cert as a CA.

The fix is a **two-tier chain**: a self-signed root CA that signs a leaf carrying
`SAN=flyte.local`. Traefik serves `leaf + CA`; the SDK pins the root as CA and validates
the leaf against it. (You can skip this if you only need the browser console — it's the
SDK that requires a trusted-chain TLS cert.)

```bash
# 1. Root CA (CA:TRUE)
openssl req -x509 -nodes -newkey rsa:2048 -days 3650 \
  -keyout ca.key -out ca.crt -subj "/CN=flyte-local-ca" \
  -addext "basicConstraints=critical,CA:TRUE" \
  -addext "keyUsage=critical,keyCertSign,cRLSign"

# 2. Leaf key + CSR
openssl req -nodes -newkey rsa:2048 -keyout leaf.key -out leaf.csr \
  -subj "/CN=flyte.local"

# 3. CA signs the leaf (CA:FALSE, SAN=flyte.local, server auth)
openssl x509 -req -in leaf.csr -CA ca.crt -CAkey ca.key -CAcreateserial \
  -days 3650 -out leaf.crt \
  -extfile <(printf "subjectAltName=DNS:flyte.local\nbasicConstraints=critical,CA:FALSE\nkeyUsage=critical,digitalSignature,keyEncipherment\nextendedKeyUsage=serverAuth")

# 4. Secret holds the full chain (leaf + CA) so Traefik serves both
cat leaf.crt ca.crt > fullchain.crt
kubectl -n traefik create secret tls flyte-local-tls \
  --cert=fullchain.crt --key=leaf.key
```

Point Traefik's cluster-wide default cert at that secret with a `TLSStore` named
`default` (the only name Traefik honours for the fallback cert), then restart Traefik:

```bash
kubectl apply -f - <<'EOF'
apiVersion: traefik.io/v1alpha1
kind: TLSStore
metadata:
  name: default
  namespace: traefik
spec:
  defaultCertificate:
    secretName: flyte-local-tls
EOF

kubectl -n traefik rollout restart deploy/traefik
```

> [!NOTE] A self-signed CA still needs `insecureSkipVerify`
> This cert chains to a **self-signed root the SDK doesn't trust**, so the SDK config
> [below](#point-the-sdk-at-the-https-endpoint) still sets `insecureSkipVerify` to accept
> it — inherent to any private/self-signed CA (AWS Private CA included), not a Traefik
> limitation. To drop it entirely, either install `ca.crt` into each client's system
> trust store, or front Flyte with a **publicly-resolvable domain** and a publicly-trusted
> cert (e.g. Traefik's ACME / Let's Encrypt resolver — the cloud ALB's ACM equivalent).
> Neither is possible for a purely-local `flyte.local`.

### Deploy oauth2-proxy

Give oauth2-proxy your IdP details and a random cookie secret. `--set-xauthrequest`
makes it emit the `X-Auth-Request-*` headers Traefik forwards downstream, and
`--reverse-proxy` tells it to trust the forwarded host/proto from Traefik. The last three
flags let the **SDK/CLI** authenticate too (not just the browser) — set them now so you
don't have to upgrade later:

```bash
# 32-byte cookie secret. Must decode to 16/24/32 bytes — head -c 32 trims the
# base64 string, since a raw 44-char value fails oauth2-proxy's length check.
COOKIE_SECRET=$(openssl rand -base64 32 | head -c 32)

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
  --set extraArgs.cookie-secure='false' \    # local HTTP, not HTTPS
  --set extraArgs.skip-jwt-bearer-tokens='true' \      # accept SDK Bearer JWTs
  --set extraArgs.oidc-extra-audience='<public-client-id>' \  # SDK client's audience (singular flag!)
  --set extraArgs.bearer-token-login-fallback='false'  # invalid token → 403, not HTML login
```

The browser path uses the session cookie; the **SDK** sends an `Authorization: Bearer`
JWT instead. `skip-jwt-bearer-tokens` makes oauth2-proxy verify that JWT against the IdP's
JWKS and pass it through, while `oidc-extra-audience` must list the **public client ID**
the SDK uses (the `flyteClient.clientId` from your `authMetadata`) — its tokens carry that
as their audience. The flag is **singular** — `oidc-extra-audiences` (plural) is not valid
and crash-loops oauth2-proxy with `unknown flag`. Without these, the SDK is rejected and
`flyte.run` fails the upload with `Unauthorized`. See
[Letting the SDK authenticate](#letting-the-sdkcli-authenticate-with-auth-enabled) for the
rest of the SDK setup.

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

#### Split the API and discovery paths off the browser middleware

This gates the **browser** correctly, but the same `oauth2-signin` redirect on **every**
path breaks the SDK (the cloud walkthrough avoids this by splitting into three ingresses —
`ingress` / `apiJwtIngress` / `wellknownIngress` — since ALB can't mix cookie-OIDC and JWT
auth on one). Two path groups need different handling:

- **Auth-discovery** (`AuthMetadataService`, `IdentityService`) — the SDK reads these
  *before* it has a token, so they must **bypass auth**. Gated, they return a `text/plain`
  401 that ConnectRPC reports as `UNAVAILABLE`, and the SDK never starts login.
- **The `flyteidl2.*` API** — needs `oauth2-auth` (Bearer validation) but **not**
  `oauth2-signin`, so an unauthenticated call gets a clean gRPC 401 the SDK retries after
  login, not sign-in HTML.

Add two higher-priority `IngressRoute`s — Traefik matches the highest `priority` first,
so these win over the `flyte-http` Ingress for their paths:

```bash
kubectl apply -f - <<'EOF'
# Discovery — highest priority, NO middleware. The SDK reads these before it has a
# token; they must reach Flyte directly so it returns the real metadata (issuer,
# client ID), not oauth2-proxy's unparseable 401. (Equivalent of wellknownIngress.)
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: flyte-auth-discovery
  namespace: flyte
spec:
  entryPoints: [web, websecure]
  routes:
    - kind: Rule
      priority: 300
      match: Host(`flyte.local`) && (PathPrefix(`/flyteidl2.auth.AuthMetadataService`) || PathPrefix(`/flyteidl2.auth.IdentityService`))
      services:
        - name: flyte-http
          port: 8090
          scheme: h2c          # gRPC over cleartext HTTP/2 to the backend
---
# API — oauth2-auth only (validates Bearer tokens), no oauth2-signin redirect, so an
# unauthenticated call gets a clean 401 the SDK can act on. (Equivalent of apiJwtIngress.)
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: flyte-api-bearer
  namespace: flyte
spec:
  entryPoints: [web, websecure]
  routes:
    - kind: Rule
      priority: 100
      match: Host(`flyte.local`) && PathPrefix(`/flyteidl2.`)
      middlewares:
        - name: oauth2-auth
      services:
        - name: flyte-http
          port: 8090
          scheme: h2c
EOF
```

Now `flyte.local` routes three ways by precedence: discovery (300) bypasses auth, the
API (100) requires a Bearer token, and everything else — the `/v2` console — falls
through to the `flyte-http` Ingress with the full browser middleware chain. Verify the
discovery path returns JSON rather than oauth2-proxy's 401:

```bash
curl -s -X POST --resolve flyte.local:443:127.0.0.1 -k \
  https://flyte.local/flyteidl2.auth.AuthMetadataService/GetPublicClientConfig \
  -H 'Content-Type: application/json' -d '{}' | head -c 120
# → {"clientId":"flytectl", ...}   (JSON, not "Unauthorized")
```

### Letting the SDK/CLI authenticate (with auth enabled)

The browser flow above works over plain HTTP, but **the SDK does not**. Like the cloud
walkthrough in [Authentication and SSO](./authentication) — which requires an **HTTPS
listener** because "OIDC auth only applies to HTTPS rules" — the SDK path here only works
over **TLS**. The reason is in the SDK itself: it attaches its auth interceptors (PKCE
browser login, token injection) **only when the client uses TLS**. With `insecure: True`
it assumes "plaintext endpoint ⇒ no auth server" and skips authentication entirely, so an
SDK pointed at `http://flyte.local` sends **no token**, oauth2-proxy rejects every call,
and `flyte.run` fails the code-bundle upload with `Unauthorized` — without ever opening a
browser login.

With oauth2-proxy configured for Bearer tokens (the SDK flags in
[Deploy oauth2-proxy](#deploy-oauth2-proxy)), Traefik's TLS listener exposed, and the
`flyte.local` cert in place ([Install the ingress controller](#replace-the-default-cert-with-one-for-flytelocal)),
two things remain: point the SDK at the HTTPS endpoint, and — **if your IdP runs
in-cluster** — make Flyte able to reach its discovery document.

#### Point the SDK at the HTTPS endpoint

In `~/.flyte/config.yaml`, reach Flyte over TLS and accept the self-signed CA from the
[Traefik install](#replace-the-default-cert-with-one-for-flytelocal):

```yaml
admin:
  endpoint: dns:///flyte.local        # must match SelectCluster's clusterEndpoint (no :80)
  insecure: False                     # use TLS — the SDK only authenticates over TLS
  insecureSkipVerify: True            # accept the self-signed CA (see the note above)
  authType: Pkce
task:
  org: local
  domain: development
  project: flytesnacks
```

> [!WARNING] The key is `insecureSkipVerify` (camelCase)
> The SDK reads `admin.insecureSkipVerify`. The snake_case `insecure_skip_verify` is
> silently ignored, so the SDK keeps full verification and fails on the self-signed cert.
> The SDK also reads the **project-local** `.flyte/config.yaml` (in the directory you run
> from) before `~/.flyte/config.yaml` — make sure the flag is in whichever file actually
> applies.

> [!WARNING] `endpoint` must match what `SelectCluster` returns
> Before uploading, the SDK calls `SelectCluster`; if the returned `clusterEndpoint`
> differs from your `admin.endpoint`, it builds a *separate* per-cluster session for the
> upload that may skip auth. Check the value and match it exactly:
> ```bash
> curl -s -X POST --resolve flyte.local:443:127.0.0.1 -k \
>   https://flyte.local/flyteidl2.cluster.ClusterService/SelectCluster \
>   -H 'Content-Type: application/json' \
>   -d '{"operation":"OPERATION_CREATE_UPLOAD_LOCATION","project":"flytesnacks","domain":"development","org":"local"}'
> # → {"clusterEndpoint":"https://flyte.local"}  ⇒  endpoint: dns:///flyte.local  (no :443)
> ```

#### If your IdP runs in-cluster (e.g. Dex)

An **external** IdP (Okta, Google, …) is publicly resolvable and serves the standard
discovery paths, so it needs nothing extra here. An **in-cluster** IdP like
[Dex](./local-dex) needs two fixes so Flyte's `GetOAuth2Metadata` — which fetches the
IdP's discovery document to tell the SDK where to log in — actually succeeds:

**(a) DNS.** Flyte fetches `http://flyte.local/dex/...`, but `flyte.local` isn't
resolvable inside the cluster (it's only in your host's `/etc/hosts`), so the fetch times
out. Point `flyte.local` at Traefik's ClusterIP from inside the Flyte pod:

```bash
TRAEFIK_IP=$(kubectl -n traefik get svc traefik -o jsonpath='{.spec.clusterIP}')

helm upgrade flyte flyteorg/flyte-binary -n flyte -f values-local.yaml \
  --set "deployment.extraPodSpec.hostAliases[0].ip=$TRAEFIK_IP" \
  --set "deployment.extraPodSpec.hostAliases[0].hostnames[0]=flyte.local"
```

**(b) Discovery path.** Flyte fetches the RFC 8414 path
`/.well-known/oauth-authorization-server`, but Dex only serves the OIDC path
`/.well-known/openid-configuration` (the former returns `404`). The two carry the same
endpoints, so rewrite one to the other at Traefik:

```bash
kubectl apply -f - <<'EOF'
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: dex-wellknown-rewrite
  namespace: flyte
spec:
  replacePathRegex:
    regex: ^/dex/\.well-known/oauth-authorization-server$
    replacement: /dex/.well-known/openid-configuration
---
apiVersion: traefik.io/v1alpha1
kind: IngressRoute
metadata:
  name: dex-oauth-metadata
  namespace: flyte
spec:
  entryPoints: [web, websecure]
  routes:
    - kind: Rule
      priority: 200   # match before the /dex Ingress
      match: Host(`flyte.local`) && Path(`/dex/.well-known/oauth-authorization-server`)
      middlewares:
        - name: dex-wellknown-rewrite
      services:
        - name: dex
          port: 5556
EOF
```

Verify both fixes landed — this should return JSON, not a `404` or a timeout:

```bash
curl -s -X POST --resolve flyte.local:443:127.0.0.1 -k \
  https://flyte.local/flyteidl2.auth.AuthMetadataService/GetOAuth2Metadata \
  -H 'Content-Type: application/json' -d '{}' | head -c 200
```

**First clear any stale SDK token from a previous cluster.** The SDK caches OAuth
tokens in the keyring (macOS Keychain), keyed by endpoint host — `kind delete cluster`
doesn't wipe them. Dex's `storage: memory` mints new signing keys on every restart, so
an old token fails oauth2-proxy's signature check with `403 Forbidden` on
`SelectCluster` and **no browser opens**. Clear it after any cluster/Dex recreate:

```bash
# macOS; "not found" is fine. Linux: keyring del flyte.local access_token / refresh_token
for k in access_token refresh_token; do security delete-generic-password -s flyte.local -a "$k" 2>/dev/null; done
```

Then `flyte.run` opens a browser to the IdP, you log in (`admin@example.com` / `password`
with the [Dex setup](./local-dex)), and the SDK submits the run with the resulting token.

#### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte.run` fails the upload with `Unauthorized`, **no browser opens** | The SDK is on plain HTTP (`insecure: True`) and skipped auth. Use `insecure: False` + `https://flyte.local`. |
| `InitializationError: Service is unavailable` / `EndpointUnavailable`, **no browser opens** | The SDK couldn't reach the API or discovery paths. Two common causes: the auth-discovery/API paths are still behind `oauth2-signin` (apply the two `IngressRoute`s in [Split the API and discovery paths](#split-the-api-and-discovery-paths-off-the-browser-middleware)); or the TLS cert is rejected (next two rows). |
| `invalid peer certificate: ... not valid for name "flyte.local"` | Traefik is serving its default cert (`SAN=*.traefik.default`). Apply the `flyte.local` cert in [Replace the default cert](#replace-the-default-cert-with-one-for-flytelocal). |
| `invalid peer certificate: ... CaUsedAsEndEntity` | The cert is a bare self-signed leaf; the SDK pins it as a CA. Use the two-tier root-CA-signs-leaf chain in [Replace the default cert](#replace-the-default-cert-with-one-for-flytelocal). |
| `Connection refused` to `https://flyte.local` | No TLS listener — Traefik's `websecure` isn't exposed, or the cluster lacks the `30443 → 443` mapping. See [step 2](#2-create-the-kind-cluster) / the [Traefik install](#install-the-ingress-controller). |
| Upload still 401 *after* a successful browser login | oauth2-proxy rejects the Bearer token. Confirm `skip-jwt-bearer-tokens=true` and `oidc-extra-audience=<your-client-id>` ([oauth2-proxy install](#deploy-oauth2-proxy)); check its logs for `audience ... does not match`. |
| `403 Forbidden` on `SelectCluster`, **no browser opens** (oauth2-proxy logs `failed to verify id token signature`) | Stale cached token; Dex's in-memory keys changed on restart. Clear the keyring tokens (block above) and rerun. |
| `GetOAuth2Metadata` returns `... 404 ... oauth-authorization-server` | In-cluster IdP only: the well-known rewrite isn't applied (b). |
| `GetOAuth2Metadata` times out (`context deadline exceeded`) | In-cluster IdP only: Flyte can't resolve the IdP host in-cluster. Apply the `hostAliases` (a). |

## 8. Load a local image into kind (optional)

kind nodes can't pull from your local Docker daemon. If you build a custom task or
Flyte image locally, load it into the cluster so pods can run it without a registry:

```bash
kind load docker-image <your-image>:<tag> --name flyte
```

Reference that exact `<your-image>:<tag>` in your task config; with the image already
present, the default `IfNotPresent` pull policy won't try to fetch it from a registry.

## 9. Tear down

Delete the cluster and Flyte in one command:

```bash
kind delete cluster --name flyte
```

The hosted PostgreSQL and S3/R2 bucket are untouched — clean those up in their own
consoles.

When you're ready to deploy to a real cluster, continue to
[Installing Flyte](./installing).
