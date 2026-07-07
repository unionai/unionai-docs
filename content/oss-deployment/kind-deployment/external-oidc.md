---
title: Set up external OIDC provider
variants: +flyte -union
weight: 2
---

# Set up external OIDC provider

[Step 7 of the Kind evaluation guide](_index#7-add-authentication-with-a-local-idp-optional)
gates the console behind Traefik and oauth2-proxy using [Dex](https://dexidp.io/) as a
throwaway in-cluster IdP. This page is the same setup with a **real external OIDC
provider** (Okta, Google, Auth0, …) instead of Dex — useful when you want to test the
authentication flow against the provider you'll actually use.

This page assumes you've completed [steps 1–6 of the Kind evaluation guide](_index) and are
about to do step 7. Register an app at your provider first: it needs the redirect URI
`http://<host>/oauth2/callback`, and you'll need its client ID and secret ready.

An external IdP is *simpler* than the in-cluster Dex: its issuer is publicly
resolvable and it serves the standard discovery paths, so none of Dex's `hostAliases`
or well-known-rewrite workarounds apply here.

## Install the ingress controller

Install Traefik with its Helm chart and expose **both** entrypoints on the kind node's
nodePorts — `web` (HTTP) on `30080` and `websecure` (HTTPS) on `30443`, the ports the
cluster maps to host `80` and `443` (see
[step 2 of the Kind evaluation guide](_index#2-create-the-kind-cluster)). The browser uses
HTTP; **the SDK needs HTTPS** — expose both up front so you don't have to reinstall
later.

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
the `30080 → 80` / `30443 → 443` mappings from step 2, Traefik is unreachable at
`flyte.local` and you'll need to recreate the cluster.

Then replace Traefik's default certificate with one for `flyte.local`, exactly as in
[the Kind evaluation guide](_index#replace-the-default-cert-with-one-for-flytelocal) — the
SDK rejects the built-in cert, and the fix (a two-tier root-CA-signs-leaf chain) is
identical whichever IdP you use.

## Deploy oauth2-proxy

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
the SDK uses (the `flyteClient.clientId` from your `authMetadata` — see
[Advertise your IdP](#advertise-your-idp-to-the-sdkcli) below) — its tokens carry that
as their audience. The flag is **singular** — `oidc-extra-audiences` (plural) is not valid
and crash-loops oauth2-proxy with `unknown flag`. Without these, the SDK is rejected and
`flyte.run` fails the upload with `Unauthorized`.

## Create the ForwardAuth middleware

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

## Create the Flyte ingress with the middleware

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

### Split the API and discovery paths off the browser middleware

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

## Advertise your IdP to the SDK/CLI

oauth2-proxy gates the **browser** path, but the SDK/CLI discover where to log in from
Flyte's [auth metadata](../authentication#advertise-your-identity-provider). Register
a **public (PKCE) client** at your IdP with the `http://localhost:53593/callback`
redirect, point `authMetadata` at it, then `helm upgrade`:

```yaml
# add to values-local.yaml
flyte-core-components:
  runs:
    authMetadata:
      externalAuthServerBaseUrl: https://<your-idp>/oauth2/default
      flyteClient:
        clientId: <public-client-id>
        redirectUri: http://localhost:53593/callback
        scopes:
          - openid
          - profile
          - offline_access
```

## Letting the SDK/CLI authenticate

The browser flow above works over plain HTTP, but **the SDK does not** — it attaches its
auth interceptors (PKCE browser login, token injection) **only when the client uses
TLS**. With `insecure: True` it assumes "plaintext endpoint ⇒ no auth server" and skips
authentication entirely, so an SDK pointed at `http://flyte.local` sends **no token**,
oauth2-proxy rejects every call, and `flyte.run` fails the code-bundle upload with
`Unauthorized` — without ever opening a browser login.

In `~/.flyte/config.yaml`, reach Flyte over TLS and accept the self-signed CA from the
[Traefik install](#install-the-ingress-controller):

```yaml
admin:
  endpoint: dns:///flyte.local        # must match SelectCluster's clusterEndpoint (no :80)
  insecure: False                     # use TLS — the SDK only authenticates over TLS
  insecureSkipVerify: True            # accept the self-signed CA
  authType: Pkce
task:
  org: local
  domain: development
  project: flytesnacks
```

The `insecureSkipVerify` and `SelectCluster` caveats from
[the Kind evaluation guide](_index#point-the-sdk-at-the-https-endpoint) apply unchanged.
Because your IdP is publicly resolvable and serves the standard
`/.well-known/oauth-authorization-server` path, Flyte's `GetOAuth2Metadata` works
without the DNS and discovery-path fixes the in-cluster Dex needs.

Then `flyte.run` opens a browser to your IdP, you log in, and the SDK submits the run
with the resulting token.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `flyte.run` fails the upload with `Unauthorized`, **no browser opens** | The SDK is on plain HTTP (`insecure: True`) and skipped auth. Use `insecure: False` + `https://flyte.local`. |
| `InitializationError: Service is unavailable` / `EndpointUnavailable`, **no browser opens** | The SDK couldn't reach the API or discovery paths. Two common causes: the auth-discovery/API paths are still behind `oauth2-signin` (apply the two `IngressRoute`s in [Split the API and discovery paths](#split-the-api-and-discovery-paths-off-the-browser-middleware)); or the TLS cert is rejected (see the cert section of the [Kind evaluation guide](_index#replace-the-default-cert-with-one-for-flytelocal)). |
| `Connection refused` to `https://flyte.local` | No TLS listener — Traefik's `websecure` isn't exposed, or the cluster lacks the `30443 → 443` mapping. See [step 2 of the Kind evaluation guide](_index#2-create-the-kind-cluster) / the [Traefik install](#install-the-ingress-controller). |
| Upload still 401 *after* a successful browser login | oauth2-proxy rejects the Bearer token. Confirm `skip-jwt-bearer-tokens=true` and `oidc-extra-audience=<your-client-id>` ([oauth2-proxy install](#deploy-oauth2-proxy)); check its logs for `audience ... does not match`. |
| Browser: `Unregistered redirect_uri` | The exact callback isn't registered on the IdP app. Add `http://flyte.local/oauth2/callback` **and** `https://flyte.local/oauth2/callback` (opening `/v2` over TLS uses the `https` one). |
