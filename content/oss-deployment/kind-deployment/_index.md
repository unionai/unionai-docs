---
title: Kind deployment
variants: +flyte -union
weight: 2
---

# Kind deployment

This guide spins up a complete Flyte stack — the Flyte binary on a
[kind](https://kind.sigs.k8s.io/) cluster, backed by a hosted PostgreSQL and an
S3-compatible object store. kind runs anywhere Docker runs, so the same steps work on
**your own machine** or on a **cloud VM** — tabs below show DigitalOcean, AWS EC2, and
GCP Compute Engine. Either way it's a fast way to try Flyte without running a
production-grade control plane.

> [!WARNING] For evaluation only
> This runs on a single-node kind cluster with static credentials (no workload identity),
> and the optional [auth setup](#7-add-authentication-with-a-local-idp-optional)
> uses a self-signed cert the SDK only accepts via `insecureSkipVerify`. Use it to try
> Flyte — not as a template for a production deployment. For that, see
> [AWS deployment](../aws-deployment). On a cloud VM, remember the stack is reachable
> from the public internet: restrict ports `80`/`443` (and `22`) to your own IP with
> your provider's network controls — a
> [DigitalOcean cloud firewall](https://docs.digitalocean.com/products/networking/firewalls/),
> an [EC2 security group](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html),
> or a [GCP firewall rule](https://cloud.google.com/firewall/docs/firewalls) — while
> you evaluate.

## 1. Prerequisites

{{< tabs "kind-host" >}}
{{< tab "Local machine" >}}
{{< markdown >}}
Install these on your machine:

- [Docker](https://docs.docker.com/get-docker/) (kind runs the cluster in containers)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [`kubectl`](https://kubernetes.io/docs/tasks/tools/)
- [`helm`](https://helm.sh/docs/intro/install/)
{{< /markdown >}}
{{< /tab >}}
{{< tab "DigitalOcean VM" >}}
{{< markdown >}}
Create a Droplet to host the cluster — kind needs a few GB of headroom, so pick at
least 4 vCPUs / 8 GB (e.g. `s-4vcpu-8gb`). Use the dashboard or
[`doctl`](https://docs.digitalocean.com/reference/doctl/):

```bash
doctl compute droplet create flyte-kind \
  --image ubuntu-24-04-x64 --size s-4vcpu-8gb --region nyc1 \
  --ssh-keys <your-ssh-key-id>
```

SSH in and install Docker, kind, `kubectl`, and `helm` on the droplet:

```bash
ssh root@<droplet-ip>

# Docker
curl -fsSL https://get.docker.com | sh

# kind
curl -Lo /usr/local/bin/kind \
  https://github.com/kubernetes-sigs/kind/releases/latest/download/kind-linux-amd64 \
  && chmod +x /usr/local/bin/kind

# kubectl
curl -Lo /usr/local/bin/kubectl \
  "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
  && chmod +x /usr/local/bin/kubectl

# helm
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

From here on, run every `kind`, `kubectl`, and `helm` command in this guide **on the
droplet**; only the SDK/CLI and browser run on your own machine.
{{< /markdown >}}
{{< /tab >}}
{{< tab "AWS EC2" >}}
{{< markdown >}}
Launch an Ubuntu instance to host the cluster — kind needs a few GB of headroom, so
pick at least 4 vCPUs / 8 GB (e.g. `t3.xlarge`). First create a security group that
admits only you — SSH now, and ports `80`/`443` for the optional auth step:

```bash
MY_IP=$(curl -s https://checkip.amazonaws.com)

aws ec2 create-security-group --group-name flyte-kind \
  --description "Flyte kind evaluation"
for port in 22 80 443; do
  aws ec2 authorize-security-group-ingress --group-name flyte-kind \
    --protocol tcp --port $port --cidr ${MY_IP}/32
done
```

Then launch the instance with the current Ubuntu 24.04 AMI (resolved via the public
SSM parameter) and your key pair:

```bash
aws ec2 run-instances \
  --image-id "$(aws ssm get-parameters \
      --names /aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id \
      --query 'Parameters[0].Value' --output text)" \
  --instance-type t3.xlarge \
  --key-name <your-key-pair> \
  --security-groups flyte-kind
```

SSH in (Ubuntu AMIs log in as `ubuntu`, so the installs need `sudo`) and install
Docker, kind, `kubectl`, and `helm`:

```bash
ssh -i <your-key.pem> ubuntu@<instance-public-ip>

# Docker — then let the ubuntu user run it without sudo
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER && newgrp docker

# kind
sudo curl -Lo /usr/local/bin/kind \
  https://github.com/kubernetes-sigs/kind/releases/latest/download/kind-linux-amd64
sudo chmod +x /usr/local/bin/kind

# kubectl
sudo curl -Lo /usr/local/bin/kubectl \
  "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo chmod +x /usr/local/bin/kubectl

# helm
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | sudo bash
```

From here on, run every `kind`, `kubectl`, and `helm` command in this guide **on the
instance**; only the SDK/CLI and browser run on your own machine.
{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP Compute Engine" >}}
{{< markdown >}}
Create an Ubuntu instance to host the cluster — kind needs a few GB of headroom, so
pick at least 4 vCPUs / 8 GB (e.g. `e2-standard-4`):

```bash
gcloud compute instances create flyte-kind \
  --machine-type e2-standard-4 --zone <your-zone> \
  --image-family ubuntu-2404-lts-amd64 --image-project ubuntu-os-cloud \
  --tags flyte-kind
```

GCP blocks inbound `80`/`443` until a firewall rule allows them (needed for the
optional auth step). Scope the rule to the instance's tag and your own IP:

```bash
MY_IP=$(curl -s https://checkip.amazonaws.com)

gcloud compute firewall-rules create flyte-kind-web \
  --allow tcp:80,tcp:443 --target-tags flyte-kind --source-ranges ${MY_IP}/32
```

SSH in (the installs need `sudo`) and install Docker, kind, `kubectl`, and `helm`:

```bash
gcloud compute ssh flyte-kind --zone <your-zone>

# Docker — then let your user run it without sudo
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER && newgrp docker

# kind
sudo curl -Lo /usr/local/bin/kind \
  https://github.com/kubernetes-sigs/kind/releases/latest/download/kind-linux-amd64
sudo chmod +x /usr/local/bin/kind

# kubectl
sudo curl -Lo /usr/local/bin/kubectl \
  "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo chmod +x /usr/local/bin/kubectl

# helm
curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | sudo bash
```

From here on, run every `kind`, `kubectl`, and `helm` command in this guide **on the
instance**; only the SDK/CLI and browser run on your own machine.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

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
>   the optional [auth setup](#7-add-authentication-with-a-local-idp-optional) at
>   `http://flyte.local`.
> - **`30443 → 443`** lets the **SDK/CLI** reach the Traefik ingress over **TLS** at
>   `https://flyte.local`. The SDK only authenticates over HTTPS (see
>   [Letting the SDK authenticate](#letting-the-sdkcli-authenticate-with-auth-enabled)),
>   so this mapping is required if you enable ingress auth *and* want to submit runs from
>   the SDK. Harmless if you never enable auth.
>
> On a **cloud VM** (DigitalOcean, EC2, GCP) the same mappings bind to the VM's
> **public IP** — in step 7, `flyte.local` points at that IP instead of `127.0.0.1`.
> Make sure inbound `80`/`443` are admitted only from your own IP (the security
> group / firewall rules from step 1; see the warning at the top).
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

Make the API reachable at `localhost:8090` on the machine where you run the SDK/CLI:

{{< tabs "kind-access" >}}
{{< tab "Local machine" >}}
{{< markdown >}}
Port-forward the API service:

```bash
kubectl -n flyte port-forward service/flyte-http 8090:8090
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "DigitalOcean VM" >}}
{{< markdown >}}
The port-forward runs on the droplet, so tunnel it back to your own machine over SSH.
This single command starts the port-forward on the droplet *and* exposes it at
`localhost:8090` locally:

```bash
ssh -L 8090:localhost:8090 root@<droplet-ip> \
  kubectl -n flyte port-forward service/flyte-http 8090:8090
```

Keep it running while you use the SDK/CLI — everything below works identically through
the tunnel.
{{< /markdown >}}
{{< /tab >}}
{{< tab "AWS EC2" >}}
{{< markdown >}}
The port-forward runs on the instance, so tunnel it back to your own machine over SSH.
This single command starts the port-forward on the instance *and* exposes it at
`localhost:8090` locally:

```bash
ssh -i <your-key.pem> -L 8090:localhost:8090 ubuntu@<instance-public-ip> \
  kubectl -n flyte port-forward service/flyte-http 8090:8090
```

Keep it running while you use the SDK/CLI — everything below works identically through
the tunnel.
{{< /markdown >}}
{{< /tab >}}
{{< tab "GCP Compute Engine" >}}
{{< markdown >}}
The port-forward runs on the instance, so tunnel it back to your own machine over SSH.
This single command starts the port-forward on the instance *and* exposes it at
`localhost:8090` locally:

```bash
gcloud compute ssh flyte-kind --zone <your-zone> \
  --ssh-flag="-L 8090:localhost:8090" \
  --command="kubectl -n flyte port-forward service/flyte-http 8090:8090"
```

Keep it running while you use the SDK/CLI — everything below works identically through
the tunnel.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

```bash
# In another terminal — list projects over the Connect (HTTP) API:
curl -s -X POST \
  http://localhost:8090/flyteidl2.project.ProjectService/ListProjects \
  -H 'Content-Type: application/json' -d '{}'
```

A JSON response (rather than a connection error) confirms the binary is up and talking
to its database.

### Submitting runs from the SDK

Point the SDK at the API forward (or tunnel) you just started. Write
`~/.flyte/config.yaml`:

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

## 7. Add authentication with a local IdP (optional)

The cloud worked examples in [AWS deployment](../aws-deployment) gate the console with
OIDC single sign-on at the load balancer — on AWS that's the ALB, configured through
`alb.ingress.kubernetes.io/auth-*` annotations. Those annotations are instructions to
the *AWS Load Balancer Controller* and do nothing on kind, which has no ALB.

The pattern is the same on kind; only the ingress controller changes. Here you run
[Traefik](https://doc.traefik.io/traefik/) and delegate auth to
[oauth2-proxy](https://oauth2-proxy.github.io/oauth2-proxy/): Traefik intercepts each
request through a `ForwardAuth` middleware, asks oauth2-proxy whether the caller is
logged in, and redirects to your IdP if not. oauth2-proxy plays the role the ALB played
— an auth proxy at the edge.

For the IdP itself, this step runs [Dex](https://dexidp.io/) **inside the same kind
cluster**, so you can test the whole authentication flow with no cloud account and no
real users — the Dex deployment itself is covered in
[Set up local OIDC provider (Dex)](./local-oidc).

> [!NOTE] Prefer an external provider?
> To validate against a real OIDC provider (Okta, Google, Auth0, …) instead of the
> in-cluster Dex, see [Set up an external OIDC provider](./external-oidc). It follows
> this same step with the Dex-specific parts swapped out.

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
> Neither is possible for a purely-local `flyte.local`. On a **cloud VM** the
> domain route *is* attainable — point a real DNS record at the VM's public IP and
> substitute that hostname for `flyte.local` throughout — but this guide sticks with the
> self-signed chain so the local and cloud-VM paths stay identical.

### Deploy Dex

Deploy Dex into the cluster and route its issuer URL (`http://flyte.local/dex`)
through Traefik, following
[Set up local OIDC provider (Dex)](./local-oidc). Come back here once the discovery
document resolves through Traefik:

```bash
curl -s http://flyte.local/dex/.well-known/openid-configuration | head
# → a JSON document with "issuer":"http://flyte.local/dex"
```

### Deploy oauth2-proxy

Give oauth2-proxy the Dex client details and a random cookie secret. `--set-xauthrequest`
makes it emit the `X-Auth-Request-*` headers Traefik forwards downstream, and
`--reverse-proxy` tells it to trust the forwarded host/proto from Traefik.
`skip-jwt-bearer-tokens`, `oidc-extra-audience`, and `bearer-token-login-fallback` let
the **SDK/CLI** authenticate too (not just the browser) — set them now so you don't have
to upgrade later. The `hostAliases` setting is the one addition an in-cluster Dex needs —
see the warning below for why:

```bash
# 32-byte cookie secret. Must decode to 16/24/32 bytes — head -c 32 trims the
# base64 string, since a raw 44-char value fails oauth2-proxy's length check.
COOKIE_SECRET=$(openssl rand -base64 32 | head -c 32)

# Dex's issuer is flyte.local, which the pod can't otherwise resolve — point it at Traefik.
TRAEFIK_IP=$(kubectl -n traefik get svc traefik -o jsonpath='{.spec.clusterIP}')

helm repo add oauth2-proxy https://oauth2-proxy.github.io/manifests
helm repo update

helm install oauth2-proxy oauth2-proxy/oauth2-proxy -n flyte \
  --set config.clientID='oauth2-proxy' \
  --set config.clientSecret='oauth2-proxy-secret' \
  --set config.cookieSecret="$COOKIE_SECRET" \
  --set extraArgs.provider=oidc \
  --set extraArgs.oidc-issuer-url='http://flyte.local/dex' \
  --set extraArgs.upstream='static://202' \
  --set extraArgs.reverse-proxy='true' \
  --set extraArgs.set-xauthrequest='true' \
  --set extraArgs.email-domain='*' \
  --set extraArgs.cookie-secure='false' \
  --set extraArgs.skip-jwt-bearer-tokens='true' \
  --set extraArgs.oidc-extra-audience='flytectl' \
  --set extraArgs.bearer-token-login-fallback='false' \
  --set "hostAliases[0].ip=$TRAEFIK_IP" \
  --set "hostAliases[0].hostnames[0]=flyte.local"
```

A few of these flags deserve explanation:

- `cookie-secure='false'` — the browser flow runs over local HTTP, not HTTPS.
- `skip-jwt-bearer-tokens='true'` — the browser path uses the session cookie, but the
  **SDK** sends an `Authorization: Bearer` JWT instead. This makes oauth2-proxy verify
  that JWT against Dex's JWKS and pass it through.
- `oidc-extra-audience='flytectl'` — must list the **public client ID** the SDK uses
  (the `flytectl` static client from the [Dex configuration](./local-oidc#dex-configuration);
  also the `flyteClient.clientId` you'll advertise in `authMetadata` below) — its
  tokens carry that as their audience.
  The flag is **singular** — `oidc-extra-audiences` (plural) is not valid and
  crash-loops oauth2-proxy with `unknown flag`.
- `bearer-token-login-fallback='false'` — an invalid token gets a `403`, not an HTML
  login page the SDK can't parse.

Without the SDK flags, the SDK is rejected and `flyte.run` fails the upload with
`Unauthorized`. See
[Letting the SDK authenticate](#letting-the-sdkcli-authenticate-with-auth-enabled) for
the rest of the SDK setup.

> [!WARNING] Why `hostAliases` is required for Dex
> Unlike an external IdP, Dex's issuer is `flyte.local` — a name that resolves on your
> host (via `/etc/hosts`) but **not inside the cluster**, where CoreDNS doesn't know it.
> Without help, oauth2-proxy hangs on `Performing OIDC Discovery...` at startup and
> `CrashLoopBackOff`s. The `hostAliases` flag above adds `flyte.local → Traefik's
> ClusterIP` to the pod's `/etc/hosts`, so `flyte.local/dex` resolves to the same issuer
> from both the pod and the browser, as OIDC requires.
>
> This pins the current ClusterIP. If the Traefik service is recreated with a new IP,
> `helm upgrade` oauth2-proxy with the new value.

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

After `helm upgrade flyte … -f values-local.yaml`, make `flyte.local` resolve to
Traefik from the machine your **browser and SDK** run on (do this once):

{{< tabs "kind-hosts-entry" >}}
{{< tab "Local machine" >}}
{{< markdown >}}
Traefik's node ports are mapped to your own host, so point `flyte.local` at loopback:

```bash
echo "127.0.0.1 flyte.local" | sudo tee -a /etc/hosts
```
{{< /markdown >}}
{{< /tab >}}
{{< tab "DigitalOcean VM" >}}
{{< markdown >}}
Traefik's node ports are bound to the droplet's public IP, so point `flyte.local` there
in **your own machine's** `/etc/hosts` (not the droplet's):

```bash
echo "<droplet-ip> flyte.local" | sudo tee -a /etc/hosts
```

Every other `flyte.local` reference in this step (Dex issuer, redirect URIs, cert SAN,
ingress host) stays exactly the same — only this mapping differs. Alternatively, create
a real DNS A record pointing at the droplet and substitute that hostname everywhere
`flyte.local` appears.
{{< /markdown >}}
{{< /tab >}}
{{< /tabs >}}

Opening the console by raw IP won't work in its place — Traefik has no route for that
host, and the OIDC issuer is `flyte.local`, so login fails on an issuer mismatch. Then
open `http://flyte.local/v2` — Traefik bounces you through Dex and back into the console.

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

### Verify the browser flow

With Dex, oauth2-proxy, and the Flyte ingress all in place, check the flow from the
command line before opening a browser. These use `curl --resolve` to point `flyte.local`
at the Traefik node port, so they work even without the `/etc/hosts` entry (the
browser still needs it):

> [!NOTE] `--resolve` on a DigitalOcean droplet
> The `--resolve flyte.local:<port>:127.0.0.1` flags in this guide assume the curl runs
> on the machine hosting kind. That's still true on a droplet — run them in your SSH
> session and `127.0.0.1` works as-is. To run them from your own machine instead,
> substitute the droplet's public IP for `127.0.0.1`.

```bash
# 1. The console is gated — an unauthenticated request is rejected by the auth middleware:
curl -s -o /dev/null -w "%{http_code}\n" --resolve flyte.local:80:127.0.0.1 \
  http://flyte.local/v2
# → 401   (the oauth2-auth ForwardAuth middleware rejects it; a browser is then
#          redirected to sign-in by the oauth2-signin error middleware)

# 2. The sign-in page is served:
curl -s -o /dev/null -w "%{http_code}\n" --resolve flyte.local:80:127.0.0.1 \
  "http://flyte.local/oauth2/sign_in?rd=http://flyte.local/v2"
# → 200

# 3. Starting login redirects all the way to Dex's login page:
curl -s -o /dev/null -w "%{url_effective}\n" -L --max-redirs 5 \
  --resolve flyte.local:80:127.0.0.1 "http://flyte.local/oauth2/start?rd=http://flyte.local/v2"
# → http://flyte.local/dex/auth/local/login?...   (oauth2-proxy → Dex)
```

> [!NOTE] Why 401 and not 302 on a raw curl
> Traefik's `oauth2-signin` middleware turns the 401 into a sign-in redirect via its
> `errors` handler, which a browser follows automatically. On a plain `curl` you see the
> raw 401 — that still confirms the request is being gated. The redirect itself is
> verified by checks 2 and 3.

Then open `http://flyte.local/v2` in a browser, log in as **`admin@example.com` /
`password`**, and you should land in the console. The `X-Auth-Request-Email` header Dex
supplies flows through oauth2-proxy to Flyte and populates `executed_by` on runs you
create — see [Authentication and SSO](../authentication#run-attribution-executed_by).

### Letting the SDK/CLI authenticate (with auth enabled)

The browser flow above works over plain HTTP, but **the SDK does not**. Like the cloud
walkthrough in [Authentication and SSO](../authentication) — which requires an **HTTPS
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
three things remain: advertise Dex in Flyte's auth metadata, point the SDK at the HTTPS
endpoint, and make Flyte able to reach Dex's discovery document.

#### Advertise Dex to the SDK/CLI

oauth2-proxy gates the **browser** path, but the SDK/CLI discover where to log in from
Flyte's [auth metadata](../authentication#advertise-your-identity-provider). Point it at
Dex using the public `flytectl` client from the
[Dex configuration](./local-oidc#dex-configuration), then `helm upgrade`:

```yaml
# add to values-local.yaml
flyte-core-components:
  runs:
    authMetadata:
      externalAuthServerBaseUrl: http://flyte.local/dex
      flyteClient:
        clientId: flytectl
        redirectUri: http://localhost:53593/callback
        scopes:
          - openid
          - profile
          - offline_access
```

This is the same `authMetadata` block as a real IdP — only the issuer URL points at the
in-cluster Dex. V2 has no auth server of its own; it just advertises Dex.

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

#### Let Flyte reach Dex's discovery document

Because Dex runs **in-cluster** with an issuer that only your host's `/etc/hosts` knows
about, two fixes are needed so Flyte's `GetOAuth2Metadata` — which fetches the IdP's
discovery document to tell the SDK where to log in — actually succeeds. (An **external**
IdP is publicly resolvable and serves the standard discovery paths, so it needs neither —
see [Set up an external OIDC provider](./external-oidc).)

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

Then `flyte.run` opens a browser to Dex, you log in (`admin@example.com` / `password`),
and the SDK submits the run with the resulting token.

### Troubleshooting

| Symptom | Cause and fix |
|---|---|
| oauth2-proxy `CrashLoopBackOff`, logs stuck on `Performing OIDC Discovery...` | The pod can't resolve `flyte.local` in-cluster. Add the `hostAliases` from the [oauth2-proxy install](#deploy-oauth2-proxy) mapping `flyte.local` to Traefik's ClusterIP. |
| oauth2-proxy `CrashLoopBackOff`, logs show `could not fetch .well-known` | oauth2-proxy can't reach the issuer. Confirm the discovery curl in [Route the issuer path](./local-oidc#route-the-issuer-path-through-traefik) returns the discovery doc and that `oidc-issuer-url` matches `issuer` in the Dex config **exactly**. |
| Browser: `Unregistered redirect_uri` / `redirect_uri did not match` | The `oauth2-proxy` static client's `redirectURIs` must list the callback for the scheme you open the console with — `http://flyte.local/oauth2/callback` **and** `https://flyte.local/oauth2/callback` (opening `/v2` over TLS uses the `https` one). List both. |
| Login succeeds but loops back to sign-in | Issuer mismatch between what the browser saw and what oauth2-proxy validated. Both must be `http://flyte.local/dex` — not a service name, not `localhost`. |
| `flyte.run` fails the upload with `Unauthorized`, **no browser opens** | The SDK is on plain HTTP (`insecure: True`) and skipped auth. Use `insecure: False` + `https://flyte.local`. |
| `InitializationError: Service is unavailable` / `EndpointUnavailable`, **no browser opens** | The SDK couldn't reach the API or discovery paths. Two common causes: the auth-discovery/API paths are still behind `oauth2-signin` (apply the two `IngressRoute`s in [Split the API and discovery paths](#split-the-api-and-discovery-paths-off-the-browser-middleware)); or the TLS cert is rejected (next two rows). |
| `invalid peer certificate: ... not valid for name "flyte.local"` | Traefik is serving its default cert (`SAN=*.traefik.default`). Apply the `flyte.local` cert in [Replace the default cert](#replace-the-default-cert-with-one-for-flytelocal). |
| `invalid peer certificate: ... CaUsedAsEndEntity` | The cert is a bare self-signed leaf; the SDK pins it as a CA. Use the two-tier root-CA-signs-leaf chain in [Replace the default cert](#replace-the-default-cert-with-one-for-flytelocal). |
| `Connection refused` to `https://flyte.local` | No TLS listener — Traefik's `websecure` isn't exposed, or the cluster lacks the `30443 → 443` mapping. See [step 2](#2-create-the-kind-cluster) / the [Traefik install](#install-the-ingress-controller). |
| Upload still 401 *after* a successful browser login | oauth2-proxy rejects the Bearer token. Confirm `skip-jwt-bearer-tokens=true` and `oidc-extra-audience=flytectl` ([oauth2-proxy install](#deploy-oauth2-proxy)); check its logs for `audience ... does not match`. |
| `403 Forbidden` on `SelectCluster`, **no browser opens** (oauth2-proxy logs `failed to verify id token signature`) | Stale cached token; Dex's in-memory keys changed on restart. Clear the keyring tokens (block above) and rerun. |
| `GetOAuth2Metadata` returns `... 404 ... oauth-authorization-server` | The well-known rewrite isn't applied — fix (b) in [Let Flyte reach Dex's discovery document](#let-flyte-reach-dexs-discovery-document). |
| `GetOAuth2Metadata` times out (`context deadline exceeded`) | Flyte can't resolve `flyte.local` in-cluster. Apply the `hostAliases` — fix (a) in [Let Flyte reach Dex's discovery document](#let-flyte-reach-dexs-discovery-document). |

## 8. Load a local image into kind (optional)

kind nodes can't pull from the host's Docker daemon. If you build a custom task or
Flyte image, load it into the cluster so pods can run it without a registry:

```bash
kind load docker-image <your-image>:<tag> --name flyte
```

On a DigitalOcean droplet, the image must be in the **droplet's** Docker daemon first —
either build it there, or ship it from your machine with
`docker save <image> | ssh root@<droplet-ip> docker load`.

Reference that exact `<your-image>:<tag>` in your task config; with the image already
present, the default `IfNotPresent` pull policy won't try to fetch it from a registry.

## 9. Tear down

Delete the cluster and Flyte in one command:

```bash
kind delete cluster --name flyte
```

On DigitalOcean, also destroy the droplet so it stops billing:

```bash
doctl compute droplet delete flyte-kind
```

The hosted PostgreSQL and S3/R2 bucket are untouched — clean those up in their own
consoles.

When you're ready to deploy to a real cluster, continue to
[AWS deployment](../aws-deployment).
