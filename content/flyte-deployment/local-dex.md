---
title: A local IdP with Dex (for testing)
variants: +flyte -union
weight: 6
---

# A local IdP with Dex (for testing)

[Step 7 of the kind guide](./local-kind) wires the console behind oauth2-proxy but still
expects an **external** OIDC provider (Okta, Google, ...). This page replaces that
provider with [Dex](https://dexidp.io/) running **inside the same kind cluster**, so you
can test the whole authentication flow with no cloud account and no real users.

> [!WARNING] For local testing only
> Dex here uses in-memory storage and a static test password baked into its config.
> It is an IdP stand-in for development — never use this configuration anywhere real.

This page assumes you've completed [steps 1–6 of the kind guide](./local-kind) and are
about to do step 7. Deploy Dex first (here), then point oauth2-proxy at it.

## The issuer-URL problem

OIDC has one constraint that shapes the whole setup: the **issuer URL must be identical**
everywhere it's seen.

- **oauth2-proxy** (running in-cluster) reaches Dex over a Kubernetes service name.
- **Your browser** reaches Dex to log in, and must land on the *same* issuer the token
  was minted for, or validation fails.

A service name like `dex.flyte.svc.cluster.local` isn't resolvable from your browser; a
`localhost` URL isn't resolvable from inside the cluster. The fix is to serve Dex under
the **same host as Flyte** (`flyte.local`) at a sub-path (`/dex`), and route to it
through Traefik. One URL — `http://flyte.local/dex` — works from both sides.

## 1. Dex configuration

Create `dex-config.yaml`. The issuer is the through-Traefik URL; the two static clients
are oauth2-proxy (confidential, with a secret) and the Flyte CLI (public, for SDK
login). `staticPasswords` gives you a login with no external user store:

```yaml
# dex-config.yaml
issuer: http://flyte.local/dex

storage:
  type: memory

web:
  http: 0.0.0.0:5556

oauth2:
  skipApprovalScreen: true        # auto-approve, no consent screen in dev

staticClients:
  # oauth2-proxy — confidential client (matches the secret you pass in step 7)
  - id: oauth2-proxy
    name: oauth2-proxy
    secret: oauth2-proxy-secret
    redirectURIs:
      - 'http://flyte.local/oauth2/callback'

  # Flyte CLI — public client for SDK/CLI PKCE login
  - id: flytectl
    name: 'Flyte CLI'
    public: true
    redirectURIs:
      - 'http://localhost:53593/callback'

enablePasswordDB: true
staticPasswords:
  # login: admin@example.com / password
  - email: "admin@example.com"
    username: "admin"
    userID: "08a8684b-db88-4b73-90a9-3cd1661f5466"
    # bcrypt hash of the literal string "password" — see the note below
    hash: "$2a$10$y8dpOZQJstU/LFps5YmME.7zKR1PmWFD1gdla7tpyfThTtrZEytBK"
```

> [!WARNING] `hash` must be a real bcrypt hash
> Dex validates the hash at startup and crashes (`CrashLoopBackOff`) with
> `malformed bcrypt hash: hashedSecret too short to be a bcrypted password` if it
> isn't a complete 60-character bcrypt string. The hash above is for `password`;
> to use a different one, generate it yourself rather than editing the string by
> hand:
> ```bash
> htpasswd -bnBC 10 "" 'your-password' | tr -d ':\n' | sed 's/^\$2y/\$2a/'
> ```

## 2. Deploy Dex

The Dex Helm chart renders whatever you pass under its `config` value into a Secret and
mounts it as `config.yaml`. So nest the configuration from step 1 under a top-level
`config:` key in a values file, and hand that to the chart:

```yaml
# dex-values.yaml — indent the whole step-1 config under `config:`
config:
  issuer: http://flyte.local/dex
  storage:
    type: memory
  web:
    http: 0.0.0.0:5556
  oauth2:
    skipApprovalScreen: true
  staticClients:
    - id: oauth2-proxy
      name: oauth2-proxy
      secret: oauth2-proxy-secret
      redirectURIs:
        - 'http://flyte.local/oauth2/callback'
    - id: flytectl
      name: 'Flyte CLI'
      public: true
      redirectURIs:
        - 'http://localhost:53593/callback'
  enablePasswordDB: true
  staticPasswords:
    - email: "admin@example.com"
      username: "admin"
      userID: "08a8684b-db88-4b73-90a9-3cd1661f5466"
      hash: "$2a$10$y8dpOZQJstU/LFps5YmME.7zKR1PmWFD1gdla7tpyfThTtrZEytBK"
```

```bash
helm repo add dex https://charts.dexidp.io
helm repo update

helm install dex dex/dex -n flyte -f dex-values.yaml
```

> [!NOTE] Why not a ConfigMap volume mount
> The chart already defines its own `config` volume, so mounting your own with
> `--set volumes[0].name=config` collides with it (`Duplicate value: "config"`). Passing
> the config under the chart's `config` value, as above, is the supported path and avoids
> the clash.

Confirm Dex came up and read its own issuer back:

```bash
kubectl -n flyte rollout status deploy/dex
kubectl -n flyte get svc dex          # note the port (5556 by default)
```

## 3. Route the issuer path through Traefik

Add an ingress so `http://flyte.local/dex` reaches the Dex service. This is what makes
the single issuer URL resolve from the browser:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dex
  namespace: flyte
spec:
  ingressClassName: traefik
  rules:
  - host: flyte.local
    http:
      paths:
      - path: /dex
        pathType: Prefix
        backend:
          service:
            name: dex
            port:
              number: 5556
```

```bash
kubectl apply -f dex-ingress.yaml
```

Check discovery works through the host path — this is the URL oauth2-proxy will fetch:

```bash
# (with "127.0.0.1 flyte.local" in /etc/hosts and Traefik reachable on the node port)
curl -s http://flyte.local/dex/.well-known/openid-configuration | head
```

A JSON document with `"issuer":"http://flyte.local/dex"` confirms Dex is reachable at
the issuer it advertises.

## 4. Point oauth2-proxy at Dex

Use these values in [step 7's oauth2-proxy install](./local-kind) instead of the
external-IdP placeholders. The `hostAliases` setting is the one addition Dex needs — see
the warning below for why:

```bash
# Dex's issuer is flyte.local, which the pod can't otherwise resolve — point it at Traefik.
TRAEFIK_IP=$(kubectl -n traefik get svc traefik -o jsonpath='{.spec.clusterIP}')

helm install oauth2-proxy oauth2-proxy/oauth2-proxy -n flyte \
  --set config.clientID='oauth2-proxy' \
  --set config.clientSecret='oauth2-proxy-secret' \
  --set config.cookieSecret="$(openssl rand -base64 32)" \
  --set extraArgs.provider=oidc \
  --set extraArgs.oidc-issuer-url='http://flyte.local/dex' \
  --set extraArgs.upstream='static://202' \
  --set extraArgs.reverse-proxy='true' \
  --set extraArgs.set-xauthrequest='true' \
  --set extraArgs.email-domain='*' \
  --set extraArgs.cookie-secure='false' \
  --set extraArgs.ssl-insecure-skip-verify='true' \
  --set "hostAliases[0].ip=$TRAEFIK_IP" \
  --set "hostAliases[0].hostnames[0]=flyte.local"   # resolve the issuer in-cluster
```

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

Then continue with the rest of step 7 (the middlewares and the Flyte ingress).

## 5. Advertise Dex to the SDK/CLI

oauth2-proxy gates the **browser** path, but the SDK/CLI discover where to log in from
Flyte's [auth metadata](./authentication#advertise-your-identity-provider). Point it at
Dex using the public `flytectl` client from step 1, then `helm upgrade`:

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

## 6. Verify the flow

With Dex, oauth2-proxy, and the Flyte ingress all in place, check the flow from the
command line before opening a browser. These use `curl --resolve` to point `flyte.local`
at the local Traefik node port, so they work **without** editing `/etc/hosts` (the
browser still needs the hosts entry):

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

To reach Flyte from a browser, `flyte.local` must resolve to the local Traefik node
port. The `curl --resolve` checks above bypass DNS, but a browser can't — add a hosts
entry once:

```bash
echo "127.0.0.1 flyte.local" | sudo tee -a /etc/hosts
```

Without it the browser can't resolve `flyte.local`. Reaching the console at
`http://127.0.0.1/v2` instead does **not** work: Traefik has no route for that host (you
get a 404), and even past that the OIDC issuer is minted as `flyte.local`, so login would
fail on an issuer mismatch. The hostname must be `flyte.local` end to end.

Then open `http://flyte.local/v2` in a browser, log in as **`admin@example.com` /
`password`**, and you should land in the console. The `X-Auth-Request-Email` header Dex
supplies flows through oauth2-proxy to Flyte and populates `executed_by` on runs you
create — see [Authentication and SSO](./authentication#run-attribution-executed_by).

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| oauth2-proxy `CrashLoopBackOff`, logs stuck on `Performing OIDC Discovery...` | The pod can't resolve `flyte.local` in-cluster. Add the `hostAlias` from step 4 mapping `flyte.local` to Traefik's ClusterIP. |
| oauth2-proxy `CrashLoopBackOff`, logs show `could not fetch .well-known` | oauth2-proxy can't reach the issuer. Confirm step 3's curl returns the discovery doc and that `oidc-issuer-url` matches `issuer` in `dex-config.yaml` **exactly**. |
| Browser: `redirect_uri did not match` | The `oauth2-proxy` static client's `redirectURIs` must list `http://flyte.local/oauth2/callback` verbatim. |
| Login succeeds but loops back to sign-in | Issuer mismatch between what the browser saw and what oauth2-proxy validated. Both must be `http://flyte.local/dex` — not a service name, not `localhost`. |
